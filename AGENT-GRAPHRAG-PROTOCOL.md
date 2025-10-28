# 🤖 Agent GraphRAG Protocol

**For:** All AI agents working on Te Kete Ako  
**Purpose:** How to use and maintain GraphRAG properly  
**Updated:** October 28, 2025

---

## 🎯 **What is GraphRAG?**

GraphRAG is our **lightweight knowledge graph** that tracks:
1. **Teaching resources** (handouts, lessons, units, games)
2. **Relationships** between resources (unit→lesson, prerequisites, recommendations)
3. **Site structure** for agent onboarding

**Location:** Supabase PostgreSQL
- `graphrag_resources` table (126 resources, 328 kB)
- `graphrag_relationships` table (38 relationships, 128 kB)

---

## 📋 **When to Use GraphRAG:**

### ✅ **DO use GraphRAG for:**

1. **Onboarding** - Understanding site structure
   ```sql
   SELECT * FROM graphrag_resources 
   WHERE resource_type = 'unit-plan';
   ```

2. **Finding related content**
   ```sql
   SELECT * FROM graphrag_relationships
   WHERE source_path = $current_resource;
   ```

3. **Unit navigation**
   ```sql
   SELECT target.* FROM graphrag_relationships rel
   JOIN graphrag_resources target ON rel.target_path = target.file_path
   WHERE rel.source_path = 'units/unit-2-decolonized-history.html'
     AND rel.relationship_type = 'unit_contains_lesson';
   ```

### ❌ **DON'T use GraphRAG for:**

1. **Production content delivery** - Use `resources` table instead
2. **User-facing features** - Use `resources` table
3. **Storing large data** - Keep it minimal!

---

## 🏗️ **Two-Table System:**

### **1. `resources` Table (Production)**
- **Purpose:** Curated content for users
- **Size:** 126 resources
- **Used by:** browse.html, My Kete, search
- **Columns:** id, title, path, type, subject, level, featured, etc.

### **2. `graphrag_resources` Table (Knowledge)**
- **Purpose:** Agent knowledge & relationships
- **Size:** 126 resources
- **Used by:** Agent onboarding, related resources
- **Columns:** id, file_path, title, resource_type, subject, year_level, quality_score, etc.

**Why both?**
- `resources` = User-facing (optimized for queries)
- `graphrag_resources` = Agent-facing (optimized for relationships)

---

## ➕ **Adding New Content:**

### **Step 1: Add to resources table**
```sql
INSERT INTO resources (
  title, 
  path, 
  type, 
  subject, 
  level,
  description,
  featured,
  is_active
) VALUES (
  'My New Handout',
  'handouts/my-new-handout.html',
  'handout',
  'english',
  '8',
  'Description of the handout',
  false,
  true
);
```

### **Step 2: Add to graphrag_resources**
```sql
INSERT INTO graphrag_resources (
  file_path,
  resource_type,
  title,
  subject,
  year_level,
  quality_score,
  cultural_context,
  archive_status
) VALUES (
  'handouts/my-new-handout.html',
  'handout',
  'My New Handout',
  'english',
  '8',
  90,
  true,
  'active'
);
```

### **Step 3: Add relationships (if needed)**

Only add if:
- ✅ Part of a unit (unit→lesson)
- ✅ Has prerequisites (lesson→prerequisite)
- ✅ Hand-curated recommendation (resource→related, max 3-5)

```sql
-- Example: Add lesson to unit
INSERT INTO graphrag_relationships (
  source_path,
  target_path,
  relationship_type,
  confidence,
  metadata
) VALUES (
  'units/unit-2-decolonized-history.html',
  'handouts/my-new-handout.html',
  'unit_includes_handout',
  1.0,
  '{"unit": "Unit 2", "purpose": "supplementary reading"}'::jsonb
);
```

---

## 🔗 **Relationship Guidelines:**

### **Relationship Types (Keep Minimal!):**

| Type | Confidence | When to Use | Example Count |
|------|------------|-------------|---------------|
| `unit_contains_lesson` | 1.0 | Structural unit→lesson links | 34 |
| `prerequisite` | 0.95 | Lesson A must come before B | 0 (add as needed) |
| `recommended_next` | 0.90 | Hand-curated progression | 0 (add as needed) |
| `same_subject` | 0.80 | High-quality related content | 4 |

### **Rules:**

1. **No auto-generation** - Every relationship hand-curated
2. **Max 3-5 relationships per resource** - Quality over quantity
3. **Min confidence 0.80** - Only high-value connections
4. **Clear purpose** - Why does this relationship exist?

---

## 🧹 **Keeping It Clean:**

### **DO:**
- ✅ Track only current, production resources
- ✅ Remove resources when files are deleted
- ✅ Keep relationships minimal and purposeful
- ✅ Update metadata when content changes

### **DON'T:**
- ❌ Add backup files
- ❌ Add test files
- ❌ Auto-generate thousands of relationships
- ❌ Create generic "related_concept" links
- ❌ Let it grow beyond 1,000 resources without review

---

## 📊 **Health Checks:**

Run these queries monthly:

```sql
-- Check size (should stay under 5 MB)
SELECT 
  pg_size_pretty(pg_total_relation_size('graphrag_resources')) as resources_size,
  pg_size_pretty(pg_total_relation_size('graphrag_relationships')) as relationships_size;

-- Check relationship count (should be ~5-10% of resource count)
SELECT 
  (SELECT COUNT(*) FROM graphrag_resources) as resources,
  (SELECT COUNT(*) FROM graphrag_relationships) as relationships;

-- Find orphaned resources (no relationships)
SELECT COUNT(*) FROM graphrag_resources gr
WHERE NOT EXISTS (
  SELECT 1 FROM graphrag_relationships
  WHERE source_path = gr.file_path OR target_path = gr.file_path
);

-- Find broken relationships (paths don't exist)
SELECT COUNT(*) FROM graphrag_relationships rel
WHERE NOT EXISTS (
  SELECT 1 FROM graphrag_resources WHERE file_path = rel.source_path
);
```

---

## 🚨 **Red Flags:**

Alert if you see:
- ⚠️ GraphRAG > 50 MB (cleanup needed)
- ⚠️ Relationships > 1,000 (audit needed)
- ⚠️ Resources with 10+ relationships (too many)
- ⚠️ Confidence < 0.60 relationships (remove)
- ⚠️ Broken path references (cleanup)

---

## 🎓 **Agent Onboarding Sequence:**

### **When starting a new task:**

1. **Read site structure**
   ```sql
   SELECT resource_type, COUNT(*) 
   FROM graphrag_resources 
   GROUP BY resource_type;
   ```

2. **Understand units**
   ```sql
   SELECT * FROM graphrag_resources 
   WHERE resource_type = 'unit-plan'
   ORDER BY title;
   ```

3. **See unit lessons**
   ```sql
   SELECT * FROM graphrag_relationships
   WHERE relationship_type = 'unit_contains_lesson';
   ```

4. **Read current handoff doc**
   - Check `/HANDOFF-TO-NEXT-AGENT-*.md` files

---

## 📚 **Reference Documents:**

- **Rebuild History:** `/GRAPHRAG-REBUILD-OCT28.md`
- **API Guide:** `/GRAPHRAG-API-GUIDE.md`
- **This Protocol:** `/AGENT-GRAPHRAG-PROTOCOL.md`

---

## ✅ **Success Criteria:**

You're using GraphRAG well if:
- ✅ Size stays under 5 MB
- ✅ Every relationship has clear purpose
- ✅ Onboarding is faster (understand structure quickly)
- ✅ No broken references
- ✅ Relationships help users find content

---

**Remember:** GraphRAG is a **tool for agents**, not a replacement for the production database. Keep it minimal, purposeful, and clean!

---

**Created:** October 28, 2025  
**Agent:** Kaitiaki Aronui  
**Next Review:** When adding 100+ new resources

🧺 ✨ 🤖

