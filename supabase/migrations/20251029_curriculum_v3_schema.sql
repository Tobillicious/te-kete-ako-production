-- ============================================================================
-- CURRICULUM V3 - DATABASE SCHEMA
-- Created: October 29, 2025
-- Purpose: Store all NZ Curriculum versions with cross-version mapping
-- ============================================================================

-- ============================================================================
-- TABLE 1: CURRICULUM STATEMENTS
-- Stores individual curriculum statements from all versions
-- ============================================================================

CREATE TABLE IF NOT EXISTS curriculum_statements (
    id BIGSERIAL PRIMARY KEY,
    
    -- Version Identification
    curriculum_version TEXT NOT NULL,
    version_status TEXT NOT NULL DEFAULT 'draft',
    effective_date DATE,
    consultation_end_date DATE,
    
    -- Hierarchical Structure (flexible for different versions)
    learning_area TEXT NOT NULL,
    phase TEXT,
    level INTEGER,
    strand TEXT,
    sub_strand TEXT,
    element TEXT,
    
    -- Content
    statement_text TEXT NOT NULL,
    context TEXT,
    examples TEXT[],
    year_levels INTEGER[],
    
    -- Metadata
    tahurangi_url TEXT,
    section_id TEXT,
    quality_score INTEGER DEFAULT 100,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    archived_at TIMESTAMP WITH TIME ZONE,
    
    -- Constraints
    CONSTRAINT valid_version CHECK (curriculum_version IN ('2007_nzc', 'temataiaho_2025', 'draft_2025')),
    CONSTRAINT valid_status CHECK (version_status IN ('draft', 'consultation', 'approved', 'mandatory', 'archived')),
    CONSTRAINT valid_quality CHECK (quality_score >= 0 AND quality_score <= 100),
    CONSTRAINT level_or_phase CHECK (level IS NOT NULL OR phase IS NOT NULL)
);

-- Add full-text search column
ALTER TABLE curriculum_statements ADD COLUMN IF NOT EXISTS search_vector TSVECTOR 
    GENERATED ALWAYS AS (
        to_tsvector('english', 
            COALESCE(statement_text, '') || ' ' || 
            COALESCE(context, '') || ' ' ||
            COALESCE(learning_area, '') || ' ' ||
            COALESCE(strand, '')
        )
    ) STORED;

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_curriculum_version ON curriculum_statements(curriculum_version);
CREATE INDEX IF NOT EXISTS idx_curriculum_learning_area ON curriculum_statements(learning_area);
CREATE INDEX IF NOT EXISTS idx_curriculum_phase ON curriculum_statements(phase) WHERE phase IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_curriculum_level ON curriculum_statements(level) WHERE level IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_curriculum_strand ON curriculum_statements(strand) WHERE strand IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_curriculum_status ON curriculum_statements(version_status);
CREATE INDEX IF NOT EXISTS idx_curriculum_year_levels ON curriculum_statements USING GIN(year_levels);
CREATE INDEX IF NOT EXISTS idx_curriculum_search ON curriculum_statements USING GIN(search_vector);
CREATE INDEX IF NOT EXISTS idx_curriculum_effective_date ON curriculum_statements(effective_date) WHERE effective_date IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_curriculum_active ON curriculum_statements(version_status, archived_at) WHERE archived_at IS NULL;

COMMENT ON TABLE curriculum_statements IS 'All NZ Curriculum statements from 2007, Te Mātaiaho 2025, and Draft 2025 versions';
COMMENT ON COLUMN curriculum_statements.curriculum_version IS '2007_nzc, temataiaho_2025, or draft_2025';
COMMENT ON COLUMN curriculum_statements.version_status IS 'draft, consultation, approved, mandatory, or archived';
COMMENT ON COLUMN curriculum_statements.phase IS 'Phase 1-5 for Te Mātaiaho (NULL for 2007 NZC)';
COMMENT ON COLUMN curriculum_statements.level IS 'Level 1-8 for 2007 NZC (NULL for Te Mātaiaho)';
COMMENT ON COLUMN curriculum_statements.element IS 'Knowledge or Practices (Te Mātaiaho only)';


-- ============================================================================
-- TABLE 2: CURRICULUM EQUIVALENCES
-- Maps statements across different curriculum versions
-- ============================================================================

CREATE TABLE IF NOT EXISTS curriculum_equivalences (
    id BIGSERIAL PRIMARY KEY,
    
    -- Statement references
    source_statement_id BIGINT NOT NULL REFERENCES curriculum_statements(id) ON DELETE CASCADE,
    target_statement_id BIGINT NOT NULL REFERENCES curriculum_statements(id) ON DELETE CASCADE,
    
    -- Equivalence metadata
    equivalence_type TEXT NOT NULL DEFAULT 'similar',
    confidence DECIMAL(3,2) DEFAULT 1.0,
    mapping_source TEXT DEFAULT 'manual',
    
    -- Validation
    mapping_notes TEXT,
    validated_by TEXT,
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

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_equiv_source ON curriculum_equivalences(source_statement_id);
CREATE INDEX IF NOT EXISTS idx_equiv_target ON curriculum_equivalences(target_statement_id);
CREATE INDEX IF NOT EXISTS idx_equiv_type ON curriculum_equivalences(equivalence_type);
CREATE INDEX IF NOT EXISTS idx_equiv_confidence ON curriculum_equivalences(confidence) WHERE confidence >= 0.8;
CREATE INDEX IF NOT EXISTS idx_equiv_bidirectional ON curriculum_equivalences(source_statement_id, target_statement_id);

COMMENT ON TABLE curriculum_equivalences IS 'Cross-version curriculum mappings (e.g., 2007 Level 5 → 2025 Phase 4)';
COMMENT ON COLUMN curriculum_equivalences.equivalence_type IS 'exact, similar, prerequisite, expanded, narrowed, or replaced';
COMMENT ON COLUMN curriculum_equivalences.confidence IS 'Mapping confidence from 0.00 to 1.00';
COMMENT ON COLUMN curriculum_equivalences.mapping_source IS 'manual, ai_generated, or expert_validated';


-- ============================================================================
-- TABLE 3: RESOURCE CURRICULUM TAGS
-- Links teaching resources to curriculum statements
-- ============================================================================

CREATE TABLE IF NOT EXISTS resource_curriculum_tags (
    id BIGSERIAL PRIMARY KEY,
    
    -- References
    resource_id UUID REFERENCES resources(id) ON DELETE CASCADE,
    curriculum_statement_id BIGINT NOT NULL REFERENCES curriculum_statements(id) ON DELETE CASCADE,
    
    -- Tag metadata
    alignment_strength TEXT DEFAULT 'core',
    alignment_notes TEXT,
    
    -- Validation
    tagged_by TEXT,
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

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_resource_tags_resource ON resource_curriculum_tags(resource_id);
CREATE INDEX IF NOT EXISTS idx_resource_tags_statement ON resource_curriculum_tags(curriculum_statement_id);
CREATE INDEX IF NOT EXISTS idx_resource_tags_strength ON resource_curriculum_tags(alignment_strength);
CREATE INDEX IF NOT EXISTS idx_resource_tags_validated ON resource_curriculum_tags(validated) WHERE validated = true;

COMMENT ON TABLE resource_curriculum_tags IS 'Links teaching resources to specific curriculum statements for perfect alignment';
COMMENT ON COLUMN resource_curriculum_tags.alignment_strength IS 'core (directly addresses), extended (related), or tangential (touches on)';


-- ============================================================================
-- FUNCTIONS
-- ============================================================================

-- Function: Search curriculum statements (full-text search)
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
      AND cs.archived_at IS NULL
    ORDER BY relevance_score DESC
    LIMIT limit_count;
END;
$$ LANGUAGE plpgsql STABLE;

COMMENT ON FUNCTION search_curriculum_statements IS 'Full-text search across all curriculum statements';


-- Function: Get equivalent statements across versions
CREATE OR REPLACE FUNCTION get_equivalent_statements(
    statement_id_input BIGINT,
    min_confidence DECIMAL DEFAULT 0.7
)
RETURNS TABLE (
    equivalent_id BIGINT,
    equivalent_version TEXT,
    equivalent_learning_area TEXT,
    equivalent_phase TEXT,
    equivalent_level INTEGER,
    equivalent_strand TEXT,
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
        cs.phase,
        cs.level,
        cs.strand,
        cs.statement_text,
        ce.equivalence_type,
        ce.confidence
    FROM curriculum_equivalences ce
    JOIN curriculum_statements cs ON cs.id = ce.target_statement_id
    WHERE ce.source_statement_id = statement_id_input
      AND ce.confidence >= min_confidence
      AND cs.archived_at IS NULL
    ORDER BY ce.confidence DESC, ce.equivalence_type;
END;
$$ LANGUAGE plpgsql STABLE;

COMMENT ON FUNCTION get_equivalent_statements IS 'Get equivalent statements from other curriculum versions';


-- Function: Get resources tagged to curriculum statement
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
$$ LANGUAGE plpgsql STABLE;

COMMENT ON FUNCTION get_resources_for_curriculum IS 'Get teaching resources aligned to a curriculum statement';


-- Function: Get curriculum navigation structure (for UI dropdowns)
CREATE OR REPLACE FUNCTION get_curriculum_navigation(
    version_input TEXT DEFAULT 'temataiaho_2025'
)
RETURNS TABLE (
    learning_area TEXT,
    phase TEXT,
    level INTEGER,
    strand TEXT,
    element TEXT,
    statement_count BIGINT,
    year_levels INTEGER[]
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        cs.learning_area,
        cs.phase,
        cs.level,
        cs.strand,
        cs.element,
        COUNT(*) as statement_count,
        ARRAY_AGG(DISTINCT unnest) as year_levels
    FROM curriculum_statements cs
    CROSS JOIN LATERAL unnest(COALESCE(cs.year_levels, ARRAY[]::INTEGER[])) AS unnest
    WHERE cs.curriculum_version = version_input
      AND cs.archived_at IS NULL
    GROUP BY cs.learning_area, cs.phase, cs.level, cs.strand, cs.element
    ORDER BY cs.learning_area, cs.phase, cs.level, cs.strand, cs.element;
END;
$$ LANGUAGE plpgsql STABLE;

COMMENT ON FUNCTION get_curriculum_navigation IS 'Get hierarchical structure for curriculum navigation UI';


-- ============================================================================
-- MATERIALIZED VIEW: Navigation Cache
-- ============================================================================

CREATE MATERIALIZED VIEW IF NOT EXISTS curriculum_navigation AS
SELECT 
    cs.curriculum_version,
    cs.learning_area,
    cs.phase,
    cs.level,
    cs.strand,
    cs.element,
    COUNT(*) as statement_count,
    MIN(cs.effective_date) as effective_date,
    MIN(cs.version_status) as version_status,
    ARRAY_AGG(DISTINCT unnest ORDER BY unnest) as all_year_levels
FROM curriculum_statements cs
CROSS JOIN LATERAL unnest(COALESCE(cs.year_levels, ARRAY[]::INTEGER[])) AS unnest
WHERE cs.archived_at IS NULL
GROUP BY cs.curriculum_version, cs.learning_area, cs.phase, cs.level, cs.strand, cs.element
ORDER BY cs.curriculum_version, cs.learning_area, cs.phase, cs.level, cs.strand, cs.element;

-- Create unique index for concurrent refresh
CREATE UNIQUE INDEX IF NOT EXISTS idx_curriculum_nav_unique ON curriculum_navigation(
    curriculum_version,
    learning_area,
    COALESCE(phase, ''),
    COALESCE(level, -1),
    COALESCE(strand, ''),
    COALESCE(element, '')
);

-- Refresh function
CREATE OR REPLACE FUNCTION refresh_curriculum_navigation()
RETURNS VOID AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY curriculum_navigation;
END;
$$ LANGUAGE plpgsql;

COMMENT ON MATERIALIZED VIEW curriculum_navigation IS 'Cached curriculum structure for fast UI loading';


-- ============================================================================
-- ROW LEVEL SECURITY
-- ============================================================================

ALTER TABLE curriculum_statements ENABLE ROW LEVEL SECURITY;
ALTER TABLE curriculum_equivalences ENABLE ROW LEVEL SECURITY;
ALTER TABLE resource_curriculum_tags ENABLE ROW LEVEL SECURITY;

-- Public read access (all users can view curriculum)
CREATE POLICY "Allow public read curriculum statements" ON curriculum_statements
    FOR SELECT USING (true);

CREATE POLICY "Allow public read curriculum equivalences" ON curriculum_equivalences
    FOR SELECT USING (true);

CREATE POLICY "Allow public read curriculum tags" ON resource_curriculum_tags
    FOR SELECT USING (true);

-- Teachers/admins can manage tags
CREATE POLICY "Teachers can manage curriculum tags" ON resource_curriculum_tags
    FOR ALL USING (
        EXISTS (
            SELECT 1 FROM profiles 
            WHERE user_id = auth.uid() 
            AND role IN ('teacher', 'admin')
        )
    );

-- Only admins can manage curriculum statements (via API/manual)
-- (Scraping scripts will use service role key, bypassing RLS)


-- ============================================================================
-- TRIGGERS
-- ============================================================================

-- Auto-update updated_at timestamp
CREATE OR REPLACE FUNCTION update_curriculum_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_curriculum_statements_timestamp
    BEFORE UPDATE ON curriculum_statements
    FOR EACH ROW
    EXECUTE FUNCTION update_curriculum_updated_at();

CREATE TRIGGER update_curriculum_equivalences_timestamp
    BEFORE UPDATE ON curriculum_equivalences
    FOR EACH ROW
    EXECUTE FUNCTION update_curriculum_updated_at();

CREATE TRIGGER update_resource_curriculum_tags_timestamp
    BEFORE UPDATE ON resource_curriculum_tags
    FOR EACH ROW
    EXECUTE FUNCTION update_curriculum_updated_at();


-- ============================================================================
-- SAMPLE DATA (for testing)
-- ============================================================================

-- Insert sample curriculum statement
INSERT INTO curriculum_statements (
    curriculum_version,
    version_status,
    effective_date,
    learning_area,
    phase,
    strand,
    element,
    statement_text,
    year_levels,
    tahurangi_url,
    quality_score
) VALUES (
    'temataiaho_2025',
    'mandatory',
    '2025-01-01',
    'English',
    'Phase 4',
    'Text Studies',
    'Knowledge',
    'Students understand how texts are shaped by purpose, audience, and context, and how language features and structures create meaning and effect.',
    ARRAY[9, 10],
    'https://newzealandcurriculum.tahurangi.education.govt.nz/example',
    100
) ON CONFLICT DO NOTHING;

-- Log success
DO $$
BEGIN
    RAISE NOTICE '✅ Curriculum V3 schema created successfully!';
    RAISE NOTICE '📊 Tables: curriculum_statements, curriculum_equivalences, resource_curriculum_tags';
    RAISE NOTICE '🔍 Functions: search, get_equivalents, get_resources, get_navigation';
    RAISE NOTICE '⚡ Materialized view: curriculum_navigation';
    RAISE NOTICE '🔒 RLS enabled with public read access';
END $$;

