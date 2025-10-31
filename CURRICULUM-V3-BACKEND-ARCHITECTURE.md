# 🏗️ CURRICULUM V3 - BACKEND ARCHITECTURE PLAN

**Date:** October 29, 2025  
**Status:** Final Planning Before Implementation  
**Agent:** Kaitiaki Aronui V3.0

---

## 🎯 **PURPOSE**

Build a robust backend system to:
1. Store ~2,500-3,500 curriculum statements from 3 different NZ Curriculum versions
2. Enable cross-version equivalence mapping
3. Power a gorgeous, fast UI for browsing
4. Support perfect curriculum integration for teaching resources
5. Handle future updates when MoE changes curriculum (again)

---

## 📊 **DATABASE SCHEMA**

### **New Tables** (3 tables for curriculum)

```sql
-- 1. CURRICULUM STATEMENTS
-- Stores individual statements from all curriculum versions
CREATE TABLE curriculum_statements (
    id BIGSERIAL PRIMARY KEY,
    
    -- Version Identification
    curriculum_version TEXT NOT NULL, -- '2007_nzc', 'temataiaho_2025', 'draft_2025'
    version_status TEXT NOT NULL DEFAULT 'draft', -- 'draft', 'consultation', 'approved', 'mandatory', 'archived'
    effective_date DATE, -- When it becomes mandatory
    consultation_end_date DATE, -- For drafts
    
    -- Hierarchical Structure (flexible for different versions)
    learning_area TEXT NOT NULL, -- 'English', 'Mathematics', 'Social Sciences', etc.
    phase TEXT, -- Phase 1-5 (Te Mātaiaho) or NULL (2007 NZC)
    level INTEGER, -- Level 1-8 (2007 NZC) or NULL (Te Mātaiaho)
    strand TEXT, -- Subject-specific (e.g., 'Text Studies', 'History', 'Number')
    sub_strand TEXT, -- Further breakdown if needed
    element TEXT, -- 'Knowledge' or 'Practices' (Te Mātaiaho only)
    
    -- Content
    statement_text TEXT NOT NULL, -- The actual curriculum statement (verbatim)
    context TEXT, -- Additional context or notes
    examples TEXT[], -- Example applications
    year_levels INTEGER[], -- [9, 10] for Phase 4, etc.
    
    -- Metadata
    tahurangi_url TEXT, -- Source URL on Tahurangi
    section_id TEXT, -- Unique identifier from Tahurangi (if available)
    quality_score INTEGER DEFAULT 100, -- For future quality tracking
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    archived_at TIMESTAMP WITH TIME ZONE,
    
    -- Search optimization
    search_vector TSVECTOR GENERATED ALWAYS AS (
        to_tsvector('english', 
            COALESCE(statement_text, '') || ' ' || 
            COALESCE(context, '') || ' ' ||
            COALESCE(learning_area, '') || ' ' ||
            COALESCE(strand, '')
        )
    ) STORED,
    
    -- Constraints
    CONSTRAINT valid_version CHECK (curriculum_version IN ('2007_nzc', 'temataiaho_2025', 'draft_2025')),
    CONSTRAINT valid_status CHECK (version_status IN ('draft', 'consultation', 'approved', 'mandatory', 'archived')),
    CONSTRAINT valid_quality CHECK (quality_score >= 0 AND quality_score <= 100),
    CONSTRAINT level_or_phase CHECK (level IS NOT NULL OR phase IS NOT NULL)
);

-- Indexes for performance
CREATE INDEX idx_curriculum_version ON curriculum_statements(curriculum_version);
CREATE INDEX idx_curriculum_learning_area ON curriculum_statements(learning_area);
CREATE INDEX idx_curriculum_phase ON curriculum_statements(phase);
CREATE INDEX idx_curriculum_level ON curriculum_statements(level);
CREATE INDEX idx_curriculum_strand ON curriculum_statements(strand);
CREATE INDEX idx_curriculum_status ON curriculum_statements(version_status);
CREATE INDEX idx_curriculum_year_levels ON curriculum_statements USING GIN(year_levels);
CREATE INDEX idx_curriculum_search ON curriculum_statements USING GIN(search_vector);
CREATE INDEX idx_curriculum_effective_date ON curriculum_statements(effective_date) WHERE effective_date IS NOT NULL;

-- Full-text search function
CREATE OR REPLACE FUNCTION search_curriculum_statements(
    search_query TEXT,
    limit_count INTEGER DEFAULT 50
)
RETURNS TABLE (
    id BIGINT,
    curriculum_version TEXT,
    learning_area TEXT,
    statement_text TEXT,
    relevance_score REAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        cs.id,
        cs.curriculum_version,
        cs.learning_area,
        cs.statement_text,
        ts_rank(cs.search_vector, plainto_tsquery('english', search_query)) AS relevance_score
    FROM curriculum_statements cs
    WHERE cs.search_vector @@ plainto_tsquery('english', search_query)
    ORDER BY relevance_score DESC
    LIMIT limit_count;
END;
$$ LANGUAGE plpgsql;


-- 2. CURRICULUM EQUIVALENCES
-- Maps statements across different curriculum versions
CREATE TABLE curriculum_equivalences (
    id BIGSERIAL PRIMARY KEY,
    
    -- Source statement
    source_statement_id BIGINT NOT NULL REFERENCES curriculum_statements(id) ON DELETE CASCADE,
    
    -- Target statement
    target_statement_id BIGINT NOT NULL REFERENCES curriculum_statements(id) ON DELETE CASCADE,
    
    -- Equivalence type
    equivalence_type TEXT NOT NULL DEFAULT 'similar', 
    -- 'exact' - Same content, different version
    -- 'similar' - Covers similar concepts
    -- 'prerequisite' - Source is prerequisite to target
    -- 'expanded' - Target expands on source
    -- 'narrowed' - Target narrows source
    -- 'replaced' - Target replaces source
    
    -- Confidence
    confidence DECIMAL(3,2) DEFAULT 1.0, -- 0.00 to 1.00
    mapping_source TEXT DEFAULT 'manual', -- 'manual', 'ai_generated', 'expert_validated'
    
    -- Notes
    mapping_notes TEXT,
    validated_by TEXT, -- Agent or human who validated
    validated_at TIMESTAMP WITH TIME ZONE,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT no_self_reference CHECK (source_statement_id != target_statement_id),
    CONSTRAINT valid_equivalence CHECK (equivalence_type IN ('exact', 'similar', 'prerequisite', 'expanded', 'narrowed', 'replaced')),
    CONSTRAINT valid_confidence CHECK (confidence >= 0 AND confidence <= 1),
    CONSTRAINT unique_mapping UNIQUE (source_statement_id, target_statement_id, equivalence_type)
);

-- Indexes
CREATE INDEX idx_equiv_source ON curriculum_equivalences(source_statement_id);
CREATE INDEX idx_equiv_target ON curriculum_equivalences(target_statement_id);
CREATE INDEX idx_equiv_type ON curriculum_equivalences(equivalence_type);
CREATE INDEX idx_equiv_confidence ON curriculum_equivalences(confidence) WHERE confidence >= 0.8;

-- Function to get equivalent statements
CREATE OR REPLACE FUNCTION get_equivalent_statements(
    statement_id_input BIGINT,
    min_confidence DECIMAL DEFAULT 0.7
)
RETURNS TABLE (
    equivalent_id BIGINT,
    equivalent_version TEXT,
    equivalent_learning_area TEXT,
    equivalent_text TEXT,
    equivalence_type TEXT,
    confidence DECIMAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        cs.id,
        cs.curriculum_version,
        cs.learning_area,
        cs.statement_text,
        ce.equivalence_type,
        ce.confidence
    FROM curriculum_equivalences ce
    JOIN curriculum_statements cs ON cs.id = ce.target_statement_id
    WHERE ce.source_statement_id = statement_id_input
      AND ce.confidence >= min_confidence
    ORDER BY ce.confidence DESC, ce.equivalence_type;
END;
$$ LANGUAGE plpgsql;


-- 3. RESOURCE CURRICULUM TAGS
-- Links teaching resources to curriculum statements
CREATE TABLE resource_curriculum_tags (
    id BIGSERIAL PRIMARY KEY,
    
    -- Resource reference
    resource_id UUID REFERENCES resources(id) ON DELETE CASCADE,
    
    -- Curriculum statement reference
    curriculum_statement_id BIGINT NOT NULL REFERENCES curriculum_statements(id) ON DELETE CASCADE,
    
    -- Tag metadata
    alignment_strength TEXT DEFAULT 'core', -- 'core', 'extended', 'tangential'
    alignment_notes TEXT,
    
    -- Who tagged it
    tagged_by TEXT, -- 'system', agent name, or user ID
    validated BOOLEAN DEFAULT FALSE,
    validated_by TEXT,
    validated_at TIMESTAMP WITH TIME ZONE,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Constraints
    CONSTRAINT valid_alignment CHECK (alignment_strength IN ('core', 'extended', 'tangential')),
    CONSTRAINT unique_tag UNIQUE (resource_id, curriculum_statement_id)
);

-- Indexes
CREATE INDEX idx_resource_tags_resource ON resource_curriculum_tags(resource_id);
CREATE INDEX idx_resource_tags_statement ON resource_curriculum_tags(curriculum_statement_id);
CREATE INDEX idx_resource_tags_strength ON resource_curriculum_tags(alignment_strength);
CREATE INDEX idx_resource_tags_validated ON resource_curriculum_tags(validated) WHERE validated = true;

-- Function to get resources for curriculum statement
CREATE OR REPLACE FUNCTION get_resources_for_curriculum(
    statement_id_input BIGINT,
    alignment_filter TEXT DEFAULT 'core'
)
RETURNS TABLE (
    resource_id UUID,
    resource_title TEXT,
    resource_type TEXT,
    resource_path TEXT,
    alignment_strength TEXT,
    quality_score INTEGER
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        r.id,
        r.title,
        r.type,
        r.path,
        rct.alignment_strength,
        gr.quality_score
    FROM resource_curriculum_tags rct
    JOIN resources r ON r.id = rct.resource_id
    LEFT JOIN graphrag_resources gr ON gr.file_path = r.path
    WHERE rct.curriculum_statement_id = statement_id_input
      AND rct.alignment_strength = alignment_filter
      AND r.is_active = true
    ORDER BY gr.quality_score DESC NULLS LAST, r.created_at DESC;
END;
$$ LANGUAGE plpgsql;

-- Row Level Security
ALTER TABLE curriculum_statements ENABLE ROW LEVEL SECURITY;
ALTER TABLE curriculum_equivalences ENABLE ROW LEVEL SECURITY;
ALTER TABLE resource_curriculum_tags ENABLE ROW LEVEL SECURITY;

-- Public read access (all users can view curriculum)
CREATE POLICY "Allow public read access to curriculum" ON curriculum_statements
    FOR SELECT USING (true);
    
CREATE POLICY "Allow public read access to equivalences" ON curriculum_equivalences
    FOR SELECT USING (true);
    
CREATE POLICY "Allow public read access to tags" ON resource_curriculum_tags
    FOR SELECT USING (true);

-- Teachers/admins can add/edit tags
CREATE POLICY "Teachers can manage tags" ON resource_curriculum_tags
    FOR ALL USING (
        EXISTS (
            SELECT 1 FROM profiles 
            WHERE user_id = auth.uid() 
            AND role IN ('teacher', 'admin')
        )
    );
```

---

## 🔄 **DATA FLOW ARCHITECTURE**

### **Phase 1: Data Extraction (Scraping)**

```
Tahurangi Website
    ↓ (DeepSeek scrapes)
Raw HTML/JSON files
    ↓ (Parse & Structure)
Structured JSON
    ↓ (Validate & Clean)
SUPABASE: curriculum_statements table
```

**Process:**
1. **Scraping Script** (Python, delegated to DeepSeek):
   - Navigate Tahurangi pages
   - Extract statement text (verbatim)
   - Capture hierarchy (learning area → phase/level → strand → element)
   - Save as JSON files (one per subject/phase)

2. **Validation Script** (Python):
   - Check for completeness
   - Validate structure
   - Flag duplicates
   - Report missing data

3. **Upload Script** (Python):
   - Bulk INSERT into `curriculum_statements`
   - Transaction-based (all or nothing per subject)
   - Log results

### **Phase 2: GraphRAG Integration**

```
SUPABASE: curriculum_statements
    ↓
SUPABASE: graphrag_resources (new curriculum nodes)
    +
SUPABASE: graphrag_relationships (curriculum → resource links)
```

**Process:**
1. **Create GraphRAG Nodes**:
   ```sql
   INSERT INTO graphrag_resources (
       file_path,
       resource_type,
       title,
       subject,
       year_level,
       metadata,
       quality_score
   )
   SELECT 
       'curriculum://' || curriculum_version || '/' || learning_area || '/' || id,
       'curriculum_statement',
       LEFT(statement_text, 100) || '...',
       learning_area,
       CASE 
           WHEN year_levels IS NOT NULL THEN year_levels[1]::TEXT
           ELSE level::TEXT
       END,
       jsonb_build_object(
           'curriculum_version', curriculum_version,
           'phase', phase,
           'level', level,
           'strand', strand,
           'element', element,
           'statement_id', id
       ),
       100
   FROM curriculum_statements;
   ```

2. **Create Relationships**:
   - **Curriculum → Resource** (via `resource_curriculum_tags`)
   - **Curriculum → Curriculum** (via `curriculum_equivalences`)
   - **Curriculum → Prerequisite Curriculum** (learning progressions)

### **Phase 3: UI Data Delivery**

```
curriculum-v3.html (Frontend)
    ↓ (JavaScript fetch)
Supabase API
    ↓ (Query curriculum_statements)
JSON response
    ↓ (Render UI)
Beautiful curriculum browser
```

---

## 🚀 **API LAYER DESIGN**

### **Frontend JavaScript API** (`js/curriculum-api.js`)

```javascript
// Curriculum V3 API
const CurriculumAPI = {
    
    // Get all learning areas for a version
    async getLearningAreas(version = 'temataiaho_2025') {
        const { data, error } = await supabase
            .from('curriculum_statements')
            .select('learning_area')
            .eq('curriculum_version', version)
            .order('learning_area');
        
        if (error) throw error;
        return [...new Set(data.map(d => d.learning_area))];
    },
    
    // Get phases for a learning area (Te Mātaiaho)
    async getPhases(learningArea, version = 'temataiaho_2025') {
        const { data, error } = await supabase
            .from('curriculum_statements')
            .select('phase, year_levels')
            .eq('curriculum_version', version)
            .eq('learning_area', learningArea)
            .not('phase', 'is', null)
            .order('phase');
        
        if (error) throw error;
        
        // Deduplicate and format
        const phases = {};
        data.forEach(item => {
            if (!phases[item.phase]) {
                phases[item.phase] = {
                    phase: item.phase,
                    years: item.year_levels
                };
            }
        });
        return Object.values(phases);
    },
    
    // Get statements for specific phase/strand
    async getStatements(filters) {
        let query = supabase
            .from('curriculum_statements')
            .select('*')
            .eq('curriculum_version', filters.version)
            .eq('learning_area', filters.learningArea);
        
        if (filters.phase) query = query.eq('phase', filters.phase);
        if (filters.level) query = query.eq('level', filters.level);
        if (filters.strand) query = query.eq('strand', filters.strand);
        if (filters.element) query = query.eq('element', filters.element);
        
        const { data, error } = await query.order('id');
        
        if (error) throw error;
        return data;
    },
    
    // Get equivalent statements across versions
    async getEquivalents(statementId, minConfidence = 0.7) {
        const { data, error } = await supabase
            .rpc('get_equivalent_statements', {
                statement_id_input: statementId,
                min_confidence: minConfidence
            });
        
        if (error) throw error;
        return data;
    },
    
    // Get resources tagged to statement
    async getResources(statementId, alignmentFilter = 'core') {
        const { data, error } = await supabase
            .rpc('get_resources_for_curriculum', {
                statement_id_input: statementId,
                alignment_filter: alignmentFilter
            });
        
        if (error) throw error;
        return data;
    },
    
    // Search curriculum
    async search(searchTerm, limit = 50) {
        const { data, error } = await supabase
            .rpc('search_curriculum_statements', {
                search_query: searchTerm,
                limit_count: limit
            });
        
        if (error) throw error;
        return data;
    },
    
    // Get timeline for curriculum changes
    async getTimeline(learningArea) {
        const { data, error } = await supabase
            .from('curriculum_statements')
            .select('curriculum_version, version_status, effective_date, consultation_end_date')
            .eq('learning_area', learningArea)
            .not('effective_date', 'is', null)
            .order('effective_date', { ascending: false });
        
        if (error) throw error;
        
        // Group by version
        const timeline = {};
        data.forEach(item => {
            if (!timeline[item.curriculum_version]) {
                timeline[item.curriculum_version] = {
                    version: item.curriculum_version,
                    status: item.version_status,
                    effectiveDate: item.effective_date,
                    consultationEnd: item.consultation_end_date
                };
            }
        });
        return Object.values(timeline);
    }
};
```

---

## ⚡ **PERFORMANCE STRATEGY**

### **1. Materialized Views** (for frequent queries)

```sql
-- View: Quick lookup for UI dropdowns
CREATE MATERIALIZED VIEW curriculum_navigation AS
SELECT 
    curriculum_version,
    learning_area,
    phase,
    level,
    strand,
    element,
    COUNT(*) as statement_count,
    MIN(effective_date) as effective_date,
    MIN(version_status) as version_status
FROM curriculum_statements
GROUP BY curriculum_version, learning_area, phase, level, strand, element
ORDER BY curriculum_version, learning_area, phase, level, strand, element;

CREATE UNIQUE INDEX idx_curriculum_nav ON curriculum_navigation(
    curriculum_version, learning_area, 
    COALESCE(phase, 'null'), COALESCE(level, -1), 
    COALESCE(strand, 'null'), COALESCE(element, 'null')
);

-- Refresh function (call after bulk updates)
CREATE OR REPLACE FUNCTION refresh_curriculum_navigation()
RETURNS VOID AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY curriculum_navigation;
END;
$$ LANGUAGE plpgsql;
```

### **2. Caching Strategy**

- **Frontend (IndexedDB)**:
  - Cache navigation structure (learning areas, phases, strands)
  - Cache viewed statements for offline access
  - TTL: 24 hours

- **API (Supabase Edge Functions)** - Future:
  - Cache common queries (e.g., "English Phase 4 statements")
  - TTL: 1 hour
  - Invalidate on curriculum updates

### **3. Pagination**

```javascript
// Paginated statement loading
async getStatementsPaginated(filters, page = 1, pageSize = 50) {
    const from = (page - 1) * pageSize;
    const to = from + pageSize - 1;
    
    const { data, error, count } = await supabase
        .from('curriculum_statements')
        .select('*', { count: 'exact' })
        .match(filters)
        .range(from, to)
        .order('id');
    
    if (error) throw error;
    
    return {
        data,
        totalCount: count,
        totalPages: Math.ceil(count / pageSize),
        currentPage: page
    };
}
```

### **4. Database Optimization**

- **Partial Indexes**: Only index active/mandatory statements for common queries
- **BRIN Indexes**: For timestamp columns (created_at, effective_date)
- **Connection Pooling**: Supabase handles this automatically
- **Query Optimization**: Use `EXPLAIN ANALYZE` to optimize slow queries

---

## 🔄 **UPDATE & VERSIONING STRATEGY**

### **Scenario 1: New Draft Released** (e.g., Phase 5 Years 11-13)

```sql
-- 1. Insert new statements with draft status
INSERT INTO curriculum_statements (
    curriculum_version,
    version_status,
    learning_area,
    phase,
    strand,
    element,
    statement_text,
    year_levels,
    effective_date,
    consultation_end_date,
    tahurangi_url
) VALUES (
    'temataiaho_2025',
    'consultation',
    'English',
    'Phase 5',
    'Text Studies',
    'Knowledge',
    '...',
    ARRAY[11, 12, 13],
    '2026-01-01',
    '2025-12-15',
    'https://...'
);

-- 2. Refresh materialized views
SELECT refresh_curriculum_navigation();

-- 3. UI automatically shows new phase with status badge
```

### **Scenario 2: Draft Becomes Mandatory**

```sql
-- Update status
UPDATE curriculum_statements
SET 
    version_status = 'mandatory',
    updated_at = NOW()
WHERE curriculum_version = 'temataiaho_2025'
  AND learning_area = 'English'
  AND phase = 'Phase 1'
  AND effective_date <= CURRENT_DATE;
```

### **Scenario 3: Curriculum Statement Changed**

```sql
-- Option A: Archive old, insert new
UPDATE curriculum_statements
SET 
    version_status = 'archived',
    archived_at = NOW()
WHERE id = 12345;

INSERT INTO curriculum_statements (
    curriculum_version,
    version_status,
    learning_area,
    phase,
    strand,
    element,
    statement_text,
    year_levels,
    effective_date
) VALUES (
    'temataiaho_2025',
    'mandatory',
    'English',
    'Phase 4',
    'Text Studies',
    'Knowledge',
    'UPDATED STATEMENT TEXT',
    ARRAY[9, 10],
    CURRENT_DATE
);

-- Option B: Track changes in metadata
UPDATE curriculum_statements
SET 
    statement_text = 'UPDATED STATEMENT TEXT',
    metadata = jsonb_set(
        COALESCE(metadata, '{}'::jsonb),
        '{change_history}',
        metadata->'change_history' || jsonb_build_array(
            jsonb_build_object(
                'previous_text', statement_text,
                'changed_at', NOW(),
                'changed_by', 'ministry_update'
            )
        )
    ),
    updated_at = NOW()
WHERE id = 12345;
```

### **Resource Tag Handling**

When curriculum changes, existing resource tags remain pointing to archived statements. Teachers see:
- **Warning**: "This resource is tagged to an archived curriculum statement"
- **Action**: "Update to new statement" (one-click if equivalence exists)

```sql
-- Auto-update tags based on equivalences
UPDATE resource_curriculum_tags rct
SET 
    curriculum_statement_id = ce.target_statement_id,
    alignment_notes = COALESCE(alignment_notes, '') || ' [Auto-updated from archived statement]',
    updated_at = NOW()
FROM curriculum_equivalences ce
WHERE rct.curriculum_statement_id = ce.source_statement_id
  AND ce.equivalence_type = 'replaced'
  AND EXISTS (
      SELECT 1 FROM curriculum_statements cs
      WHERE cs.id = rct.curriculum_statement_id
      AND cs.version_status = 'archived'
  );
```

---

## 🧪 **DATA QUALITY & VALIDATION**

### **1. Import Validation**

```python
# Python validation script
def validate_curriculum_import(data):
    errors = []
    warnings = []
    
    # Required fields
    required = ['curriculum_version', 'learning_area', 'statement_text']
    for field in required:
        if not data.get(field):
            errors.append(f"Missing required field: {field}")
    
    # Must have phase OR level
    if not data.get('phase') and not data.get('level'):
        errors.append("Must have either phase or level")
    
    # Validate year levels
    if data.get('year_levels'):
        if not all(0 <= y <= 13 for y in data['year_levels']):
            errors.append("Invalid year levels (must be 0-13)")
    
    # Check statement length
    if len(data.get('statement_text', '')) < 10:
        warnings.append("Statement text suspiciously short")
    
    # Check for placeholder text
    placeholders = ['lorem ipsum', 'placeholder', 'TODO', 'TBD']
    if any(p in data.get('statement_text', '').lower() for p in placeholders):
        errors.append("Statement contains placeholder text")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'warnings': warnings
    }
```

### **2. Duplicate Detection**

```sql
-- Find potential duplicates
SELECT 
    c1.id as id1,
    c2.id as id2,
    c1.statement_text,
    similarity(c1.statement_text, c2.statement_text) as similarity_score
FROM curriculum_statements c1
JOIN curriculum_statements c2 ON c1.id < c2.id
WHERE c1.curriculum_version = c2.curriculum_version
  AND c1.learning_area = c2.learning_area
  AND similarity(c1.statement_text, c2.statement_text) > 0.8
ORDER BY similarity_score DESC;
```

### **3. Completeness Check**

```sql
-- Check for missing strands
SELECT 
    cs1.learning_area,
    cs1.phase,
    cs1.strand,
    COUNT(*) as statement_count
FROM curriculum_statements cs1
WHERE cs1.curriculum_version = 'temataiaho_2025'
  AND cs1.phase IS NOT NULL
GROUP BY cs1.learning_area, cs1.phase, cs1.strand
HAVING COUNT(*) < 5 -- Flag if fewer than 5 statements per strand
ORDER BY statement_count;
```

---

## 📈 **METRICS & MONITORING**

### **Track These Metrics:**

1. **Coverage**:
   - Statements per subject/phase
   - Completeness % (actual vs expected)

2. **Usage**:
   - Most viewed statements
   - Most searched terms
   - Cross-version comparison frequency

3. **Quality**:
   - Untagged resources (curriculum → resource gaps)
   - Low-confidence equivalences
   - Outdated resource tags

```sql
-- Dashboard query
CREATE OR REPLACE VIEW curriculum_metrics AS
SELECT 
    curriculum_version,
    learning_area,
    COUNT(*) as total_statements,
    COUNT(DISTINCT phase) as phase_count,
    COUNT(DISTINCT strand) as strand_count,
    SUM(CASE WHEN version_status = 'mandatory' THEN 1 ELSE 0 END) as mandatory_count,
    SUM(CASE WHEN version_status = 'draft' THEN 1 ELSE 0 END) as draft_count,
    (SELECT COUNT(*) 
     FROM resource_curriculum_tags rct 
     WHERE rct.curriculum_statement_id = cs.id) as tagged_resources_count
FROM curriculum_statements cs
GROUP BY curriculum_version, learning_area
ORDER BY curriculum_version, learning_area;
```

---

## 🎨 **UI DATA PATTERNS**

### **Pattern 1: Navigation Sidebar**

```javascript
// Load navigation structure
const nav = await CurriculumAPI.getLearningAreas('temataiaho_2025');
// → ['English', 'Mathematics', 'Science', ...]

const phases = await CurriculumAPI.getPhases('English', 'temataiaho_2025');
// → [{phase: 'Phase 1', years: [0,1,2,3]}, {phase: 'Phase 2', years: [4,5,6]}, ...]

// Cache in IndexedDB for instant load
```

### **Pattern 2: Statement List**

```javascript
// Load statements for selected filters
const statements = await CurriculumAPI.getStatements({
    version: 'temataiaho_2025',
    learningArea: 'English',
    phase: 'Phase 4',
    strand: 'Text Studies',
    element: 'Knowledge'
});
// → [{id: 123, statement_text: '...', ...}, ...]

// Render cards with:
// - Statement text
// - Year levels badge
// - Resources count badge
// - "Compare versions" button
```

### **Pattern 3: Cross-Version Comparison**

```javascript
// User clicks "Compare versions" on a statement
const equivalents = await CurriculumAPI.getEquivalents(statementId);
// → [
//     {equivalent_id: 456, equivalent_version: '2007_nzc', equivalent_text: '...', equivalence_type: 'similar', confidence: 0.85},
//     {equivalent_id: 789, equivalent_version: 'draft_2025', equivalent_text: '...', equivalence_type: 'expanded', confidence: 0.92}
//   ]

// Display side-by-side comparison modal
```

### **Pattern 4: Resource Integration**

```javascript
// User clicks "View Resources" on a statement
const resources = await CurriculumAPI.getResources(statementId, 'core');
// → [
//     {resource_id: 'uuid', resource_title: 'Y9 Text Analysis Unit', resource_type: 'unit-plan', resource_path: '/units/...', quality_score: 95},
//     ...
//   ]

// Display resource cards with "Open Resource" button
```

---

## 🚀 **IMPLEMENTATION PHASES**

### **Phase 1: Database Setup** (Week 1)
- [ ] Create 3 tables
- [ ] Create indexes
- [ ] Create SQL functions
- [ ] Set up RLS policies
- [ ] Test with sample data

### **Phase 2: Data Extraction** (Weeks 2-3)
- [ ] Build scraping scripts (DeepSeek)
- [ ] Extract English Phase 1-4 (test case)
- [ ] Build validation pipeline
- [ ] Import to Supabase
- [ ] Verify data quality

### **Phase 3: GraphRAG Integration** (Week 3)
- [ ] Create curriculum nodes in `graphrag_resources`
- [ ] Create relationships in `graphrag_relationships`
- [ ] Test queries

### **Phase 4: API Layer** (Week 4)
- [ ] Build `js/curriculum-api.js`
- [ ] Test all API functions
- [ ] Add error handling
- [ ] Add caching

### **Phase 5: UI Implementation** (Weeks 4-5)
- [ ] Build `curriculum-v3.html`
- [ ] Implement navigation
- [ ] Implement statement display
- [ ] Implement search
- [ ] Implement version comparison
- [ ] Implement resource linking

### **Phase 6: Full Extraction** (Week 6)
- [ ] Extract all 8 subjects × 4 phases (Te Mātaiaho)
- [ ] Extract 2007 NZC (all levels)
- [ ] Extract 6 draft subjects
- [ ] Validate completeness
- [ ] Build equivalence mappings

---

## ✅ **SUCCESS CRITERIA**

1. **Data Completeness**: 100% of available curriculum statements indexed
2. **Performance**: < 200ms page load, < 100ms API responses
3. **Accuracy**: 100% verbatim statements, no placeholders
4. **Usability**: Teachers can find ANY statement in < 3 clicks
5. **Integration**: Resources can be tagged to curriculum statements
6. **Future-proof**: Can handle curriculum updates without schema changes

---

## 🎉 **READY TO BUILD?**

This architecture addresses:
- ✅ Data flow (scraping → validation → Supabase → GraphRAG → UI)
- ✅ API design (CurriculumAPI with 7 core functions)
- ✅ GraphRAG integration (curriculum as knowledge graph nodes)
- ✅ Update/versioning strategy (status tracking, archival, equivalences)
- ✅ Performance (indexes, materialized views, caching, pagination)
- ✅ Data quality (validation, duplicate detection, completeness checks)

**Next step:** Approve this plan, then start Phase 1 (Database Setup)!

---

**He mahi nui tēnei, engari ka taea!**  
(This is a big job, but we can do it!)

🧺 ✨ 📚 🗺️ 🚀

