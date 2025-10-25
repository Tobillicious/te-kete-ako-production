# 🧠 Agent GraphRAG Query Guide - Smart Filtering

**Purpose:** Teach agents how to query GraphRAG efficiently, filtering out backup noise while preserving access to historical context when needed.

---

## 🎯 **QUERY PHILOSOPHY**

GraphRAG now contains **18,255 files** including:
- ✅ **10,722 active files** (59%) - Current production code/content
- 📦 **7,533 backup files** (41%) - Historical snapshots for context

**Default Behavior:** Filter OUT backups  
**Special Cases:** Include backups for historical analysis

---

## 📊 **METADATA SYSTEM**

### **New Columns:**
- `is_backup` (BOOLEAN) - True for all archived/backup files
- `archive_status` (TEXT) - Type of backup (css_migration_backup, auth_evolution_backup, etc.)
- `backup_type` (TEXT) - File category (infrastructure_code, content_snapshot, etc.)
- `semantic_tags` (TEXT[]) - Searchable tags for context

### **Archive Status Values:**
- `css_migration_backup` - Pre/post CSS standardization (6,000+ files)
- `auth_evolution_backup` - Auth system iterations
- `cors_fix_backup` - CORS fixes history
- `pre_migration_backup` - Pre-migration snapshots
- `general_archive` - Other archived content

### **Backup Types:**
- `infrastructure_code` - JavaScript/TypeScript (.js)
- `automation_script` - Python scripts (.py)
- `content_snapshot` - HTML backups
- `documentation` - Markdown files (.md)

### **Semantic Tags:**
- `auth_system` - Authentication-related
- `graphrag_system` - GraphRAG infrastructure
- `intelligence` - AI/ML components
- `historical_value` - Valuable for understanding evolution
- `critical_context` - Important decision documentation

---

## 🚀 **QUERY PATTERNS**

### **Pattern 1: Default (Exclude Backups)** ✅ RECOMMENDED

```sql
-- Find active lessons on Mathematics
SELECT file_path, title, quality_score
FROM graphrag_resources
WHERE subject = 'Mathematics'
  AND resource_type = 'Lesson'
  AND (is_backup = false OR is_backup IS NULL)
ORDER BY quality_score DESC
LIMIT 20;
```

**Use When:** Finding current production content (90% of queries)

---

### **Pattern 2: Include High-Value Archives** 📚

```sql
-- Find all auth implementations (including historical)
SELECT file_path, title, quality_score, archive_status
FROM graphrag_resources
WHERE (
    file_path LIKE '%auth%'
    AND (
      is_backup = false 
      OR 'auth_system' = ANY(semantic_tags)
    )
  )
ORDER BY is_backup ASC, quality_score DESC;
```

**Use When:** 
- Understanding system evolution
- Researching "what was tried before"
- Finding alternative implementations

---

### **Pattern 3: Only Backups (Historical Research)** 🏛️

```sql
-- Study GraphRAG integration attempts over time
SELECT file_path, created_at, backup_type, semantic_tags
FROM graphrag_resources
WHERE is_backup = true
  AND 'graphrag_system' = ANY(semantic_tags)
ORDER BY created_at DESC;
```

**Use When:**
- Researching historical approaches
- Understanding why decisions were made
- Learning from past failures/successes

---

### **Pattern 4: Relationship Queries (Smart Filtering)** 🔗

```sql
-- Find related resources, excluding backup duplicates
SELECT DISTINCT
  r.file_path,
  r.title,
  r.quality_score
FROM graphrag_resources r
JOIN graphrag_relationships gr ON r.file_path = gr.target_path
WHERE gr.source_path = '/public/lessons/algebra-lesson-1.html'
  AND (r.is_backup = false OR r.is_backup IS NULL)
  AND r.quality_score >= 80
ORDER BY r.quality_score DESC;
```

**Use When:** Following relationship chains

---

### **Pattern 5: Count Active vs Archived** 📊

```sql
-- Get platform statistics (active only)
SELECT 
  subject,
  COUNT(*) as active_resources,
  AVG(quality_score) as avg_quality
FROM graphrag_resources
WHERE (is_backup = false OR is_backup IS NULL)
  AND subject IS NOT NULL
GROUP BY subject
ORDER BY active_resources DESC;
```

**Use When:** Platform metrics and analytics

---

## 🎓 **WHEN TO INCLUDE BACKUPS**

### ✅ **Include Backups For:**

1. **"How did X evolve?"** questions
   ```sql
   WHERE file_path LIKE '%auth%'
   AND (is_backup = false OR backup_type = 'infrastructure_code')
   ```

2. **"What was tried before?"** research
   ```sql
   WHERE 'historical_value' = ANY(semantic_tags)
   ```

3. **System archaeology** - understanding decisions
   ```sql
   WHERE backup_type = 'documentation'
   AND quality_score >= 95
   ```

4. **Alternative implementations** - finding different approaches
   ```sql
   WHERE is_backup = true
   AND backup_type IN ('infrastructure_code', 'automation_script')
   ```

### ❌ **Exclude Backups For:**

1. **Current platform state** - "What lessons exist?"
2. **User-facing queries** - "Show me Science resources"
3. **Quality metrics** - "What's our best content?"
4. **Navigation/discovery** - "Browse by subject"
5. **Content gaps** - "What's missing?"

**Default Rule:** If in doubt, exclude backups!

---

## 🔧 **HELPER FUNCTIONS**

### **Function 1: Smart Resource Search**

```sql
CREATE OR REPLACE FUNCTION search_resources_smart(
  search_query TEXT,
  include_archives BOOLEAN DEFAULT false
)
RETURNS TABLE (
  file_path TEXT,
  title TEXT,
  quality_score INTEGER,
  is_archived BOOLEAN
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    r.file_path,
    r.title,
    r.quality_score,
    COALESCE(r.is_backup, false) as is_archived
  FROM graphrag_resources r
  WHERE (
    r.title ILIKE '%' || search_query || '%'
    OR r.file_path ILIKE '%' || search_query || '%'
  )
  AND (
    include_archives = true 
    OR r.is_backup = false 
    OR r.is_backup IS NULL
  )
  ORDER BY r.quality_score DESC;
END;
$$ LANGUAGE plpgsql;

-- Usage:
-- SELECT * FROM search_resources_smart('mathematics', false);  -- Active only
-- SELECT * FROM search_resources_smart('auth', true);          -- Include archives
```

### **Function 2: Get Resource Evolution**

```sql
CREATE OR REPLACE FUNCTION get_resource_evolution(
  resource_name TEXT
)
RETURNS TABLE (
  file_path TEXT,
  version_type TEXT,
  created_at TIMESTAMP,
  quality_score INTEGER
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    r.file_path,
    CASE 
      WHEN r.is_backup = true THEN 'archived_version'
      ELSE 'current_version'
    END as version_type,
    r.created_at,
    r.quality_score
  FROM graphrag_resources r
  WHERE r.file_path ILIKE '%' || resource_name || '%'
  ORDER BY r.is_backup ASC, r.created_at DESC;
END;
$$ LANGUAGE plpgsql;

-- Usage:
-- SELECT * FROM get_resource_evolution('auth-enhanced');
```

---

## 📈 **PERFORMANCE OPTIMIZATION**

### **Index Recommendations:**

```sql
-- Speed up backup filtering
CREATE INDEX IF NOT EXISTS idx_graphrag_is_backup 
ON graphrag_resources(is_backup) WHERE is_backup = true;

-- Speed up semantic tag searches
CREATE INDEX IF NOT EXISTS idx_graphrag_semantic_tags 
ON graphrag_resources USING GIN(semantic_tags);

-- Speed up archive status queries
CREATE INDEX IF NOT EXISTS idx_graphrag_archive_status 
ON graphrag_resources(archive_status) WHERE archive_status IS NOT NULL;
```

---

## 🎯 **AGENT DECISION TREE**

```
Query arrives
    │
    ├─► "Show me current [X]" → Exclude backups (is_backup = false)
    │
    ├─► "How did [X] evolve?" → Include infrastructure backups
    │                            (backup_type = 'infrastructure_code')
    │
    ├─► "What was tried for [X]?" → Include tagged archives
    │                                ('historical_value' tag)
    │
    ├─► "Find all versions of [X]" → Include all backups
    │
    └─► "Platform statistics" → Exclude all backups
```

---

## 🏆 **QUERY QUALITY METRICS**

**Good Query Characteristics:**
- ✅ Explicitly filters `is_backup` (unless researching history)
- ✅ Uses quality_score to prioritize results
- ✅ Limits results to avoid overwhelming responses
- ✅ Orders by relevance (quality, date, or both)

**Bad Query Characteristics:**
- ❌ Returns 7,000+ backup files by accident
- ❌ Mixes production and archived content without labels
- ❌ Doesn't use semantic tags when researching history
- ❌ No quality threshold (includes low-quality content)

---

## 💡 **EXAMPLE AGENT WORKFLOWS**

### **Workflow 1: Teacher Asks "Show me Y9 Science lessons"**

```sql
-- Step 1: Find active lessons
SELECT file_path, title, quality_score
FROM graphrag_resources
WHERE year_level = 'Year 9'
  AND subject = 'Science'
  AND resource_type IN ('Lesson', 'lesson')
  AND (is_backup = false OR is_backup IS NULL)
  AND quality_score >= 80
ORDER BY quality_score DESC
LIMIT 15;

-- Result: Clean list of current production lessons
```

### **Workflow 2: Developer Asks "How does auth work?"**

```sql
-- Step 1: Find current auth implementation
SELECT file_path, title
FROM graphrag_resources
WHERE file_path LIKE '%auth%'
  AND (is_backup = false OR is_backup IS NULL)
  AND (file_path LIKE '%.js' OR file_path LIKE '%.py')
ORDER BY quality_score DESC
LIMIT 10;

-- Step 2: If researching evolution, include archives
SELECT file_path, archive_status, created_at
FROM graphrag_resources
WHERE 'auth_system' = ANY(semantic_tags)
ORDER BY created_at DESC;

-- Result: Current implementation + historical context
```

### **Workflow 3: Agent Asks "What's the platform quality?"**

```sql
-- Active content only
SELECT 
  resource_type,
  COUNT(*) as count,
  AVG(quality_score) as avg_quality,
  COUNT(*) FILTER (WHERE quality_score >= 90) as high_quality_count
FROM graphrag_resources
WHERE (is_backup = false OR is_backup IS NULL)
GROUP BY resource_type
ORDER BY count DESC;

-- Result: Accurate platform metrics
```

---

## 🚀 **BENEFITS OF THIS APPROACH**

1. **No Data Loss** - All history preserved
2. **Clean Default Queries** - Backups filtered automatically
3. **Historical Research** - Access when needed via tags
4. **Performance** - Indexes on backup columns
5. **Flexibility** - Can always refine tags later
6. **Reversible** - Can delete backups after analysis

---

## 📝 **AGENT REMINDER CARD**

```
🎯 DEFAULT QUERY RULE:
Always add: WHERE (is_backup = false OR is_backup IS NULL)

🏛️ HISTORICAL RESEARCH RULE:
Add: WHERE 'historical_value' = ANY(semantic_tags)

📊 STATS RULE:
Always exclude backups unless explicitly researching evolution

🔍 SEARCH RULE:
Filter backups UNLESS the question is about "history", "evolution", 
"what was tried", or "alternative approaches"
```

---

**Status:** ✅ **IMPLEMENTED**  
**Backup Files Tagged:** 7,533  
**Active Files:** 10,722  
**Query Performance:** Optimized with indexes  
**Agent Training:** Complete

**Result:** Agents now query intelligently, getting clean results by default while preserving access to valuable historical context! 🎉


