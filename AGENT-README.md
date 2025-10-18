# 🤖 AGENT README - GraphRAG-Powered Development

**Last Updated:** October 18, 2025  
**For:** Future AI agents working on Te Kete Ako

---

## 🎯 **GOLDEN RULE: GraphRAG IS YOUR SOURCE OF TRUTH**

**DO NOT create coordination MDs. QUERY the GraphRAG instead.**

```sql
-- Everything you need is queryable:
SELECT * FROM graphrag_resources WHERE file_path LIKE '_agent_rules/%';
SELECT * FROM graphrag_resources WHERE file_path LIKE '_dev_patterns/%';
SELECT * FROM graphrag_resources WHERE file_path LIKE '_issues/%';
SELECT * FROM graphrag_resources WHERE file_path LIKE '_session_learnings/%';
```

---

## 🧠 **GRAPHRAG STRUCTURE FOR AGENTS:**

### **`_agent_rules/`** - Mandatory coordination rules
```sql
-- Query all agent rules:
SELECT title, metadata FROM graphrag_resources 
WHERE file_path LIKE '_agent_rules/%'
ORDER BY quality_score DESC;

-- Example rules:
- repo_mission: "Build, don't document"
- md_prohibition: "No coordination MDs"  
- graphrag_first: "Query GraphRAG before asking user"
- commit_progress: "Log in git, not MDs"
```

### **`_dev_patterns/`** - Development patterns learned
```sql
-- Query development patterns:
SELECT title, metadata->>'pattern' as pattern, 
       metadata->>'lesson_learned' as lesson
FROM graphrag_resources 
WHERE file_path LIKE '_dev_patterns/%';

-- Examples:
- css_consolidation: Single canonical CSS
- ai_activation: Load AI via navigation globally
- graphrag_driven_development: Query then build
```

### **`_issues/`** - Active bugs/TODOs
```sql
-- Query active issues:
SELECT title, metadata->>'priority' as priority,
       metadata->>'status' as status
FROM graphrag_resources 
WHERE file_path LIKE '_issues/%'
  AND metadata->>'status' = 'open'
ORDER BY metadata->>'priority';

-- Then query affected files:
SELECT target_path FROM graphrag_relationships
WHERE source_path = '_issues/[issue_id]'
  AND relationship_type = 'affects';
```

### **`_session_learnings/`** - Historical insights
```sql
-- Query past learnings:
SELECT title, metadata->>'key_learnings' as learnings,
       metadata->>'impact' as impact
FROM graphrag_resources
WHERE file_path LIKE '_session_learnings/%'
ORDER BY quality_score DESC;
```

---

## 🚀 **AGENT WORKFLOW:**

### **1. START: Query GraphRAG**
```sql
-- What's the current state?
SELECT COUNT(*) FROM graphrag_resources;
SELECT COUNT(*) FROM graphrag_relationships;

-- What are active issues?
SELECT * FROM graphrag_resources 
WHERE file_path LIKE '_issues/%' 
  AND metadata->>'status' = 'open';

-- What patterns should I follow?
SELECT * FROM graphrag_resources 
WHERE file_path LIKE '_dev_patterns/%';
```

### **2. DISCOVER: Use GraphRAG intelligence**
```sql
-- Find orphaned high-quality resources:
SELECT r.* FROM graphrag_resources r
WHERE quality_score >= 90
  AND (SELECT COUNT(*) FROM graphrag_relationships 
       WHERE source_path = r.file_path OR target_path = r.file_path) < 3;

-- Find cross-subject opportunities:
SELECT * FROM graphrag_relationships
WHERE relationship_type = 'related_content'
  AND confidence > 0.9;
```

### **3. BUILD: Create features, not docs**
- Build actual pages/components
- Use GraphRAG insights to guide development
- Track changes in GraphRAG

### **4. TRACK: Update GraphRAG**
```sql
-- Add new features to GraphRAG:
INSERT INTO graphrag_resources (file_path, resource_type, title, metadata)
VALUES ('public/new-feature.html', 'Page', 'New Feature', '{"built_by": "agent_id"}');

-- Track what enabled it:
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type)
VALUES ('_dev_patterns/some_pattern', 'public/new-feature.html', 'enabled');
```

### **5. COMMIT: Log in git, not MDs**
```bash
git commit -m "feat: Descriptive message with impact

What: Built X feature
Why: GraphRAG showed Y opportunity  
Impact: Z user benefit

GraphRAG queries used:
- Query 1
- Query 2"
```

---

## 📊 **CURRENT PLATFORM STATUS (Query for Live Data):**

```sql
-- Resources:
SELECT COUNT(*) as total FROM graphrag_resources;
SELECT COUNT(*) FROM graphrag_resources WHERE file_path LIKE 'public/%';
SELECT COUNT(*) FROM graphrag_resources WHERE file_path LIKE 'backup_before_css_migration/%';

-- Quality:
SELECT AVG(quality_score) FROM graphrag_resources WHERE file_path LIKE 'public/%';
SELECT COUNT(*) FROM graphrag_resources WHERE quality_score >= 90;

-- Cultural:
SELECT COUNT(*) FROM graphrag_resources WHERE cultural_context = true;
SELECT COUNT(*) FROM graphrag_resources WHERE has_whakataukī = true;

-- Relationships:
SELECT relationship_type, COUNT(*) 
FROM graphrag_relationships 
GROUP BY relationship_type 
ORDER BY COUNT(*) DESC;
```

---

## ⚠️ **RULES (Enforced by _agent_rules/):**

1. **NO new coordination MDs** - Use ACTIVE_QUESTIONS.md only
2. **Query GraphRAG first** - Don't ask user for info that's in the graph
3. **Build, don't document** - Create features, not plans
4. **Commit progress** - Git commits > MD summaries
5. **Track in GraphRAG** - Add metadata for future agents

---

## 🎯 **KNOWN ISSUES (Query _issues/):**

```sql
-- See all active issues:
SELECT * FROM graphrag_resources 
WHERE file_path LIKE '_issues/%' 
  AND metadata->>'status' = 'open'
ORDER BY metadata->>'priority';
```

---

## 📚 **KEY DISCOVERIES (Query _session_learnings/):**

- **Teaching Variants Goldmine**: 13,042 options available
- **18-Step Writers Toolkit**: Longest learning sequence
- **Y8 Digital Kaitiakitanga**: Most culturally influential (31 refs)
- **Unit Plans Hub**: Knowledge graph center (598 influence)
- **178 Post-Legacy Resources**: Innovation era content

---

## 🚨 **IF YOU NEED TO:**

- **Ask coordination questions**: Update ACTIVE_QUESTIONS.md
- **Track a bug**: Add to _issues/ in GraphRAG
- **Document a pattern**: Add to _dev_patterns/ in GraphRAG
- **Share a learning**: Add to _session_learnings/ in GraphRAG

**NEVER**: Create a new coordination/summary/plan MD!

---

**The GraphRAG is your overseer. Query it. Trust it. Build from it.** 🧠👑

