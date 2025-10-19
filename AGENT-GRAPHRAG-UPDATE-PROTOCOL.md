# 🤖 Agent GraphRAG Update Protocol

**Purpose:** Ensure agents update GraphRAG knowledge graph as they work  
**Status:** ACTIVE - All agents must follow  
**Date:** October 19, 2025

---

## 🎯 The Problem

GraphRAG becomes outdated when agents create new files but don't add them to the knowledge graph. This causes:
- ❌ New resources invisible to search
- ❌ Connection counts incorrect
- ❌ Orphaned excellent resources
- ❌ Platform loses intelligence over time

---

## ✅ The Solution: Self-Updating Protocol

**Every agent MUST update GraphRAG after creating/modifying files.**

---

## 📋 Agent Workflow

### **Step 1: Do Your Work**
- Create lessons, components, hubs, documentation
- Make improvements to existing resources
- Build new features

### **Step 2: Update GraphRAG** (NEW - REQUIRED!)

After creating files, run this SQL:

```sql
-- Add new resource to GraphRAG
INSERT INTO graphrag_resources (
  file_path, 
  resource_type, 
  title, 
  quality_score, 
  cultural_context, 
  year_level, 
  subject, 
  has_te_reo, 
  has_whakataukī, 
  content_preview,
  metadata
)
VALUES (
  '/public/path/to/your-new-file.html',
  'Lesson',  -- or Component, Hub, Documentation, etc.
  'Your Resource Title',
  85,  -- Quality score 0-100
  true,  -- Does it have cultural integration?
  'Years 9-11',
  'Science',
  false,  -- Has Te Reo Māori?
  false,  -- Has Whakataukī?
  'Brief description of what this resource does...',
  '{"key": "value", "any": "metadata"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  updated_at = NOW(),
  quality_score = EXCLUDED.quality_score;
```

### **Step 3: Create Relationships**

Link your new resource to related ones:

```sql
INSERT INTO graphrag_relationships (
  source_path, 
  target_path, 
  relationship_type, 
  confidence, 
  metadata
)
VALUES
  ('/public/your-new-file.html', '/public/related-file.html', 'related_content', 0.85, '{}'::jsonb),
  ('/public/your-new-file.html', '/public/science-hub.html', 'featured_on', 0.95, '{}'::jsonb),
  ('/public/your-component.js', '/public/uses-component.html', 'used_by', 0.98, '{}'::jsonb)
ON CONFLICT DO NOTHING;
```

### **Step 4: Log Agent Knowledge**

Preserve what you learned:

```sql
INSERT INTO agent_knowledge (
  source_type, 
  source_name, 
  doc_type, 
  key_insights, 
  technical_details, 
  agents_involved
)
VALUES (
  'agent_session',
  'Brief description of what you did',
  'technical_implementation',  -- or bug_fix, enhancement, etc.
  ARRAY[
    'Key insight 1',
    'Key insight 2',
    'Important discovery 3'
  ],
  jsonb_build_object(
    'files_created', ARRAY['/path1', '/path2'],
    'problem_solved', 'Description',
    'approach', 'How you solved it'
  ),
  ARRAY['your_agent_id', 'collaborator_agent']
);
```

---

## 📊 Relationship Types Reference

Use these standard relationship types:

### **Content Relationships:**
- `unit_contains_lesson` - Unit ➜ Lesson
- `lesson_has_handout` - Lesson ➜ Handout
- `has_interactive_game` - Lesson ➜ Game
- `prerequisite` - Earlier ➜ Later (learning sequence)
- `related_content` - Similar topics
- `progression_pathway` - Skill development chain

### **Cultural Relationships:**
- `shared_cultural_element` - Common Māori concepts
- `shared_whakataukī` - Same proverbs
- `shared_māori_value` - Common values
- `cultural_thread` - Cultural continuity
- `cultural_excellence_network` - High-quality cultural resources

### **Technical Relationships:**
- `powers_feature` - Component ➜ Page using it
- `used_by` - Component ➜ Page
- `styles_page` - CSS ➜ Page
- `documents` - Documentation ➜ Code
- `implements_priority` - Code ➜ Roadmap item
- `solves_discovery` - Code ➜ Report finding

### **Pedagogical Relationships:**
- `same_subject` - Same subject area
- `same_year_level` - Same age group
- `cross_curricular_link` - Across subjects
- `skill_progression` - Skill development

---

## 🎯 Quality Score Guidelines

| Score | Meaning | Criteria |
|-------|---------|----------|
| 95-100 | Excellent | Production-ready, culturally integrated, well-tested |
| 90-94 | Very Good | High quality, minor improvements possible |
| 85-89 | Good | Solid resource, functional |
| 80-84 | Acceptable | Works but needs enhancement |
| <80 | Needs Work | Incomplete or low quality |

---

## 🔍 How to Check if Resource is in GraphRAG

Before adding, check if it exists:

```sql
SELECT file_path, title, quality_score, created_at
FROM graphrag_resources
WHERE file_path LIKE '%your-file-name%';
```

---

## 📝 Real Examples from Today

### **Example 1: Dynamic Connection Counter**

```sql
-- Resource added
INSERT INTO graphrag_resources (file_path, resource_type, title, quality_score, ...)
VALUES ('/public/js/graphrag-connection-counter.js', 'JavaScript Component', 
        'GraphRAG Real-Time Connection Counter', 95, ...);

-- Relationships created
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, ...)
VALUES 
  ('/public/js/graphrag-connection-counter.js', '/public/science-hub.html', 'powers_feature', 0.98, ...),
  ('/public/js/graphrag-connection-counter.js', '/public/mathematics-hub.html', 'powers_feature', 0.98, ...);

-- Knowledge logged
INSERT INTO agent_knowledge (source_name, key_insights, ...)
VALUES ('GraphRAG Dynamic Connections Implementation', 
        ARRAY['Connection counts were hardcoded but real counts are different', ...], ...);
```

### **Example 2: New Science Lesson**

```sql
-- Add lesson
INSERT INTO graphrag_resources VALUES (
  '/public/lessons/genetics-advanced.html',
  'Lesson',
  'Advanced Genetics & Whakapapa',
  92,
  true,  -- cultural_context
  'Years 12-13',
  'Science',
  true,  -- has_te_reo
  true,  -- has_whakataukī
  'Advanced genetics integrated with whakapapa concepts...',
  '{"ncea_level": 2, "duration_minutes": 60}'::jsonb
);

-- Link to hub, prerequisites, related content
INSERT INTO graphrag_relationships VALUES
  ('/public/lessons/genetics-advanced.html', '/public/science-hub.html', 'hub_contains_resource', 0.95, ...),
  ('/public/lessons/genetics-basic.html', '/public/lessons/genetics-advanced.html', 'prerequisite', 0.92, ...),
  ('/public/lessons/genetics-advanced.html', '/public/lessons/whakapapa-unit.html', 'shared_cultural_element', 0.88, ...);
```

---

## 🚨 What Happens If You Don't Update GraphRAG?

**Bad outcomes:**
1. Your excellent resource becomes **orphaned** (0-5 connections)
2. Teachers/students **never find it**
3. Connection counts stay **wrong**
4. GraphRAG Intelligence Report marks it as **hidden gem** (wasted effort!)
5. Future agents **can't learn** from your work
6. Platform intelligence **degrades** over time

---

## ✨ Benefits of Updating GraphRAG

**Good outcomes:**
1. ✅ Your resource is **discoverable**
2. ✅ Appears in **GraphRAG-powered recommendations**
3. ✅ Connection counts **accurate**
4. ✅ Contributes to **knowledge graph** growth
5. ✅ Future agents **learn** from your work
6. ✅ Platform becomes **more intelligent**

---

## 🔄 GraphRAG Self-Evolution Cycle

```
Agent Creates Resource
         ↓
Agent Updates GraphRAG
         ↓
Resource Becomes Discoverable
         ↓
Users Find & Use It
         ↓
Relationships Strengthen
         ↓
GraphRAG Gets Smarter
         ↓
Better Recommendations
         ↓
More Value for Everyone
         ↓
(cycle continues...)
```

---

## 🎯 Quick Checklist

After creating/modifying files:

- [ ] Run `graphrag_resources` INSERT for new files
- [ ] Run `graphrag_relationships` INSERT to link resources
- [ ] Run `agent_knowledge` INSERT to log learnings
- [ ] Verify resource appears in search
- [ ] Check connection count is not 0
- [ ] Commit code changes
- [ ] Document what you did

---

## 💡 Pro Tips

1. **Batch Your Updates:** Create all files first, then update GraphRAG once
2. **Use Migrations:** Apply migrations for GraphRAG updates (trackable!)
3. **Check Existing:** Don't create duplicate entries
4. **Use ON CONFLICT:** Handle updates gracefully
5. **Document Relationships:** Add metadata explaining WHY things are connected
6. **Quality Matters:** Accurate quality scores help recommendations

---

## 🔧 Troubleshooting

### **Error: Duplicate file_path**
```sql
-- Use ON CONFLICT to update instead
ON CONFLICT (file_path) DO UPDATE SET updated_at = NOW();
```

### **Can't Find Relationship Type**
Check standard types above or create new meaningful ones.

### **Resource Not Appearing**
- Check `file_path` format (must start with `/public/` usually)
- Verify resource actually exists on filesystem
- Check quality_score (resources <50 may be filtered)

---

## 📚 Further Reading

- `GRAPHRAG-INTEGRATION-SUMMARY.md` - Overview
- `GRAPHRAG-INTELLIGENCE-REPORT.md` - Data analysis
- `GRAPHRAG-NEXT-STEPS.md` - Roadmap
- `GRAPHRAG-DYNAMIC-CONNECTIONS-GUIDE.md` - Component usage

---

## 🌟 Remember

**GraphRAG is only as smart as we make it.**

Every time you update GraphRAG:
- You make the platform smarter
- You help teachers find resources
- You enable better recommendations
- You contribute to collective intelligence

**Update GraphRAG. Build collective intelligence. Nā te mōhiotanga!** 🧠✨

---

**Last Updated:** October 19, 2025  
**Status:** ACTIVE PROTOCOL  
**Compliance:** MANDATORY for all agents

