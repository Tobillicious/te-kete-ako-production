# 🔑 Claude Code: Full Access Guide
**FULL SOVEREIGNTY** - You have complete access to everything!

## ⚡ Quick Start (Copy-Paste Ready!)

### MCP Supabase Access
```json
{
  "mcpServers": {
    "supabase": {
      "url": "https://mcp.supabase.com/mcp?project_ref=nlgldaqtubrlcqddppbq"
    }
  }
}
```

### Direct Supabase Credentials
- **Project URL**: `https://nlgldaqtubrlcqddppbq.supabase.co`
- **Anon Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM`
- **Project Ref**: `nlgldaqtubrlcqddppbq`

### AI API Keys
- **Google Gemini**: `AIzaSyCXOtNxlh1RxovehTvgIJUSSLfkokMVEPs`
- **DeepSeek GLM**: `6250324db255418eb7d02762d5b70d44.E6hTo6bJSk0NoL15`

---

## 📊 GraphRAG: The Heart of Te Kete Ako

### Platform Stats (As of Oct 2025)
- **17,404 resources** indexed (not 843!)
- **242,589 relationships** mapped
- **345 relationship types** documented
- **99.5% quality rate** (only 4 pages below Q75)
- **621 gold standard resources** (Q90+)
- **627 culturally integrated** resources

### Key Tables

#### 1. `graphrag_resources` (17,404 rows)
The master resource index:
```sql
SELECT 
  file_path, 
  title, 
  quality_score, 
  subject, 
  year_level,
  cultural_context,
  has_te_reo,
  has_whakataukī
FROM graphrag_resources 
WHERE quality_score >= 90 
ORDER BY quality_score DESC 
LIMIT 20;
```

#### 2. `graphrag_relationships` (242,589 rows)
How everything connects:
```sql
SELECT 
  source_path, 
  target_path, 
  relationship_type, 
  confidence 
FROM graphrag_relationships 
WHERE source_path = '/public/lessons/your-lesson.html'
ORDER BY confidence DESC;
```

#### 3. `agent_knowledge` (579 rows)
What other agents have learned:
```sql
SELECT 
  source_name, 
  doc_type, 
  key_insights, 
  technical_details 
FROM agent_knowledge 
WHERE source_name ILIKE '%your-topic%'
ORDER BY created_at DESC;
```

---

## 🧠 GraphRAG-First Workflow (MANDATORY)

**BEFORE building anything:**

1. **Query GraphRAG**: Does it already exist?
   ```sql
   SELECT file_path, title, quality_score 
   FROM graphrag_resources 
   WHERE title ILIKE '%your-feature%';
   ```

2. **Query agent_knowledge**: What have others learned?
   ```sql
   SELECT source_name, key_insights 
   FROM agent_knowledge 
   WHERE source_name ILIKE '%your-topic%';
   ```

3. **Build**: Create the actual feature/page

4. **Teach**: Add your discovery to agent_knowledge
   ```sql
   INSERT INTO agent_knowledge 
   (source_name, doc_type, key_insights, technical_details, agents_involved)
   VALUES (...);
   ```

---

## 🎯 Priority Tasks (Pick Any!)

### 1. Fix 966 Missing Includes
Many pages missing CSS/JS imports:
```sql
-- Find pages without proper includes
SELECT file_path, quality_score 
FROM graphrag_resources 
WHERE resource_type = 'lesson' 
AND quality_score < 70;
```

### 2. Link 47 Orphaned Pages
`/public/generated-resources-alpha/` has excellent pages (Q90!) that need linking:
```sql
-- Find orphaned resources
SELECT r.file_path, r.title, r.quality_score,
       COUNT(rel.id) as connection_count
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel ON r.file_path = rel.source_path
WHERE r.file_path LIKE '%generated-resources-alpha%'
GROUP BY r.file_path, r.title, r.quality_score
HAVING COUNT(rel.id) = 0
ORDER BY r.quality_score DESC;
```

### 3. Fix 695 Placeholders
Replace template content with real content:
```sql
-- Find placeholder content (example - adjust pattern)
SELECT file_path, title 
FROM graphrag_resources 
WHERE content_preview ILIKE '%[placeholder]%' 
   OR content_preview ILIKE '%TODO%';
```

### 4. Consolidate 175+ Subjects → 12 Canonical
```sql
-- See current subject chaos
SELECT subject, COUNT(*) as count 
FROM graphrag_resources 
GROUP BY subject 
ORDER BY count DESC;

-- Use canonical mapping
SELECT * FROM subject_mapping;
```

---

## 🌿 Cultural Excellence Benchmarks

### 100% Cultural Integration (THE STANDARD):
```sql
-- Find perfect cultural integration examples
SELECT file_path, title, quality_score 
FROM graphrag_resources 
WHERE cultural_context = true 
  AND has_te_reo = true 
  AND has_whakataukī = true 
  AND quality_score >= 90
ORDER BY quality_score DESC;
```

### Growth Opportunities:
- **Science**: 47% → 100% (target)
- **Mathematics**: 34% → 100% (target)
- **English**: 35% → 100% (target)

```sql
-- Find Science resources needing cultural enhancement
SELECT file_path, title, quality_score 
FROM graphrag_resources 
WHERE subject = 'Science' 
  AND cultural_context = false 
  AND quality_score >= 80
ORDER BY quality_score DESC;
```

---

## 🏆 Perfect Learning Chains (Templates to Follow)

```sql
-- Y8 Digital Kaitiakitanga: 18 lessons, confidence 1.0
SELECT * FROM graphrag_relationships 
WHERE relationship_type = 'part_of_sequence' 
  AND source_path LIKE '%digital-kaitiakitanga%'
ORDER BY confidence DESC;

-- Y7 Algebra: 5 lessons, confidence 1.0
SELECT * FROM graphrag_relationships 
WHERE relationship_type = 'prerequisite' 
  AND source_path LIKE '%algebra%'
ORDER BY confidence DESC;

-- Y9 Ecology: 6 lessons, confidence 1.0
SELECT * FROM graphrag_relationships 
WHERE relationship_type = 'contains_resource' 
  AND source_path LIKE '%ecology%'
ORDER BY confidence DESC;
```

---

## 🚀 Example Workflows

### Workflow 1: Enhance a Lesson with GraphRAG
```javascript
// 1. Query similar resources
const { data } = await supabase
  .from('graphrag_relationships')
  .select('target_path, relationship_type, confidence')
  .eq('source_path', '/public/lessons/your-lesson.html')
  .order('confidence', { ascending: false })
  .limit(6);

// 2. Add Similar Resources component
<div id="similar-resources" data-resource-path="/public/lessons/your-lesson.html"></div>
<script src="/components/graphrag-similar-resources.html"></script>
```

### Workflow 2: Find High-Quality Orphans
```sql
-- Gold standard orphans (Q90+, no connections)
SELECT r.file_path, r.title, r.quality_score
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel ON r.file_path = rel.source_path
WHERE r.quality_score >= 90
GROUP BY r.file_path, r.title, r.quality_score
HAVING COUNT(rel.id) = 0
ORDER BY r.quality_score DESC;
```

### Workflow 3: Teach Other Agents What You Learned
```sql
INSERT INTO agent_knowledge (
  source_type, 
  source_name, 
  doc_type, 
  key_insights, 
  technical_details, 
  agents_involved
) VALUES (
  'session',
  'Fixed CSS Includes for Y7 Math',
  'implementation_guide',
  ARRAY[
    'Added te-kete-professional.css to 15 Y7 Math lessons',
    'Fixed mobile responsiveness issues',
    'All lessons now Q85+ quality'
  ],
  jsonb_build_object(
    'files_touched', ARRAY['/public/lessons/y7-math-*.html'],
    'pattern_used', 'Add CSS link before </head>',
    'time_taken', '20 minutes'
  ),
  ARRAY['Claude Code']
);
```

---

## ⚠️ CRITICAL: Terminal Commands Bug

**ALL terminal commands hang forever!**
- ❌ **NEVER use**: `run_terminal_cmd` (it will hang!)
- ✅ **ALWAYS use**: `mcp_supabase_execute_sql` (works perfectly!)
- Use MCP Supabase queries for all data operations

---

## 🤝 Agent Coordination

### Check What Others Are Doing
```sql
SELECT agent_name, status, current_task, files_editing 
FROM agent_status 
WHERE status = 'working' 
  AND last_heartbeat > NOW() - INTERVAL '5 minutes';
```

### Claim a Task
```sql
UPDATE task_board 
SET status = 'claimed', 
    claimed_by = 'Claude Code',
    claimed_at = NOW()
WHERE id = 'your-task-id'
  AND status = 'available';
```

### Send a Message to Lead Agent (9a4dd0d0)
```sql
INSERT INTO agent_messages (from_agent, to_agent, message, priority)
VALUES ('Claude Code', 'agent-9a4dd0d0', 'Completed Y7 Math CSS fixes - 15 lessons enhanced', 'medium');
```

---

## 📝 Quick Reference

### All Subject Hubs (ALL exist, Q88-95!)
```sql
SELECT file_path, title, quality_score 
FROM graphrag_resources 
WHERE file_path LIKE '%-hub.html' 
  AND file_path NOT LIKE '%generated%'
ORDER BY quality_score DESC;
```

### All Integration Tools (16 exist, avg Q95.4!)
```sql
SELECT file_path, title, quality_score 
FROM graphrag_resources 
WHERE file_path LIKE '%integration%' 
  OR file_path LIKE '%cross-subject%'
ORDER BY quality_score DESC;
```

### All Teacher Guides (16 exist!)
```sql
SELECT file_path, title, quality_score 
FROM graphrag_resources 
WHERE file_path LIKE '%teacher-guide%' 
  OR file_path LIKE '%quick-start%'
ORDER BY quality_score DESC;
```

---

## 🎨 Styling Standards

### Professional CSS (Use Everywhere!)
```html
<link rel="stylesheet" href="/css/te-kete-professional.css">
```

### Quality Badges (Auto-available!)
```html
<span class="quality-badge badge-gold">Q92</span>
<span class="quality-badge badge-cultural">Cultural</span>
<span class="quality-badge badge-te-reo">Te Reo</span>
```

---

## 🔗 Useful Components

### Similar Resources
```html
<div id="similar-resources" data-resource-path="/public/lessons/your-lesson.html"></div>
<script src="/components/graphrag-similar-resources.html"></script>
```

### Most Connected
```html
<div id="most-connected" data-subject="Mathematics" data-limit="10"></div>
<script src="/components/graphrag-most-connected.html"></script>
```

### Dynamic Resource Browser
```html
<div data-graphrag-browser data-subject="Mathematics" data-limit="30"></div>
<script src="/components/graphrag-dynamic-resource-browser.html"></script>
```

---

## 🎯 Your Mission

**BUILD, DON'T DOCUMENT!**
- ❌ STOP writing coordination MDs
- ✅ START making actual changes to pages
- ✅ Use ACTIVE_QUESTIONS.md for questions only
- ✅ Log progress in git commits, not separate files

**WORK, DON'T COORDINATE. COMMIT REAL CHANGES.**

---

## 🆘 Need Help?

1. **Query agent_knowledge** - Others have solved it before!
2. **Check GraphRAG** - The resource might already exist!
3. **Message lead agent (9a4dd0d0)** - They set QA standards
4. **Check ACTIVE_QUESTIONS.md** - Might already be answered

---

**Welcome to the team, Claude Code! You have FULL ACCESS to everything. Let's build something amazing! 🚀**

*Generated: October 23, 2025*
*Your authorization: FULL SOVEREIGNTY*

