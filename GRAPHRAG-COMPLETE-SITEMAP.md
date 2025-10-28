# 🗺️ GraphRAG Complete Site Map

**Created:** October 28, 2025  
**Purpose:** Comprehensive index of EVERYTHING on Te Kete Ako  
**For:** All agents (comprehensive knowledge at a glance)

---

## 📊 **Complete System Overview:**

### **Total Resources: 185**

```
📚 Teaching Content:      126 resources
   ├── Handouts:          69
   ├── Lessons:           34
   ├── Unit Plans:        10
   ├── Videos:            7
   └── Games:             6

🌐 Platform Pages:        27 pages
   ├── Navigation:        7 (browse, index, etc.)
   ├── Auth:              5 (login, register, etc.)
   ├── Dashboards:        5 (my-kete, teacher, student)
   ├── System:            5 (about, contact, help, etc.)
   └── Utility:           5 (curriculum browser, AI hub, etc.)

📝 Templates:             4 files
   ├── Handout Template
   ├── Lesson Template
   ├── Unit Template
   └── Game Template

🔧 System Files:          8 files
   ├── CSS:               3 (main.css, maori-icons.css, etc.)
   └── JS:                5 (auth-ui.js, main.js, etc.)

📄 Agent Docs:            20 documents
   └── Protocols, handoffs, status reports

🔗 Relationships:         96 connections
   └── How everything connects
```

**Total Database Size:** ~560 kB (0.56 MB)

---

## 🎯 **Querying by Category:**

### **1. Teaching Content Only (For Content Work):**
```sql
SELECT * FROM graphrag_resources
WHERE resource_type IN ('handout', 'lesson', 'unit-plan', 'game', 'video')
ORDER BY resource_type, title;

-- Or use helper function
SELECT * FROM get_teaching_resources();
```

**Returns:** 126 teaching resources (excludes platform/agent stuff)

---

### **2. Platform Structure (For Understanding Site):**
```sql
SELECT * FROM graphrag_resources
WHERE resource_type LIKE '%_page'
ORDER BY resource_type, title;

-- Or use helper function
SELECT * FROM get_platform_pages();
```

**Returns:** 27 pages categorized as:
- `nav_page` - Browse, index, handouts list, etc.
- `auth_page` - Login, register, password reset
- `dashboard_page` - My Kete, teacher/student dashboards
- `system_page` - About, contact, help, privacy, terms
- `utility_page` - Curriculum browser, AI hub, etc.

---

### **3. Templates (For Content Creation):**
```sql
SELECT * FROM graphrag_resources
WHERE resource_type = 'template'
ORDER BY title;
```

**Returns:** 4 templates with status in metadata:
- Handout Template (ready)
- Lesson Template (needs auth update)
- Unit Template (needs auth update)
- Game Template (needs checking)

---

### **4. System Files (For Technical Work):**
```sql
SELECT * FROM graphrag_resources
WHERE resource_type IN ('css_file', 'js_file')
ORDER BY metadata->>'priority' DESC NULLS LAST, title;

-- Or use helper function
SELECT * FROM get_system_files();
```

**Returns:** 8 files (3 CSS, 5 JS) with priority and purpose

---

### **5. Agent Docs (For Onboarding):**
```sql
-- Already exists!
SELECT * FROM get_agent_onboarding();
```

---

### **6. Complete Site Map (Everything):**
```sql
-- Category breakdown
SELECT 
  CASE 
    WHEN resource_type IN ('handout', 'lesson', 'unit-plan', 'game', 'video') THEN 'Teaching Content'
    WHEN resource_type LIKE '%_page' THEN 'Platform Pages'
    WHEN resource_type IN ('css_file', 'js_file') THEN 'System Files'
    WHEN resource_type = 'template' THEN 'Templates'
    WHEN resource_type = 'agent_doc' THEN 'Agent Documentation'
  END as category,
  COUNT(*) as count
FROM graphrag_resources
GROUP BY category;
```

---

## 🔗 **Relationship Types:**

### **Teaching Content:**
- `unit_contains_lesson` (34) - Unit → Lessons structure
- `same_subject` (4) - Related teaching resources

### **Platform Dependencies:**
- `uses_stylesheet` (19) - Pages → CSS files
- `uses_script` (5) - Pages → JS files
- `displays_content` (10) - Browse → Teaching resources

### **Agent Coordination:**
- `leads_to` (2) - Previous work → Next task
- `documents` (1) - Implementation → Protocol
- `describes_work_on` (4) - Handoff → Templates

### **Other:**
- Various metadata connections (11)

**Total: 96 relationships**

---

## 🎓 **Agent Use Cases:**

### **"Show me all teaching content":**
```sql
SELECT * FROM get_teaching_resources();
-- Returns 126 resources, NO platform pages
```

### **"What's the platform structure?":**
```sql
SELECT resource_type, title, file_path 
FROM graphrag_resources
WHERE resource_type LIKE '%_page'
ORDER BY resource_type;
-- Shows all navigation, auth, dashboard pages
```

### **"What templates exist?":**
```sql
SELECT title, file_path, metadata->>'status' as status
FROM graphrag_resources
WHERE resource_type = 'template';
-- Shows 4 templates with their status
```

###**"What CSS files control design?":**
```sql
SELECT title, metadata->>'purpose' as purpose
FROM graphrag_resources
WHERE resource_type = 'css_file';
-- Shows main.css (design system), maori-icons.css, etc.
```

### **"What's my next task?":**
```sql
SELECT * FROM get_next_task();
-- Returns: Template cleanup
```

---

## 📋 **For Growth Phase:**

### **Adding New Content (Automatic):**

When you create new files, just run:
```sql
-- Auto-detect and index
INSERT INTO graphrag_resources (
  file_path,
  resource_type,
  title,
  subject,
  year_level,
  quality_score,
  archive_status
)
SELECT 
  $file_path,
  detect_resource_type($file_path),
  extract_title_from_path($file_path),
  extract_subject($file_path, extract_title_from_path($file_path)),
  extract_year_level($file_path),
  85,  -- Default quality, can update later
  'active'
RETURNING *;
```

**Functions available:**
- `detect_resource_type(path)` - Auto-detect handout/lesson/unit/game/etc.
- `extract_title_from_path(path)` - Clean filename → title
- `extract_subject(path, title)` - Auto-detect math/english/science/etc.
- `extract_year_level(path)` - Extract from filename (y8-, year-8, etc.)

---

## 🔍 **Smart Filtering:**

### **Exclude Platform Cruft:**
```sql
-- Just teaching resources
WHERE resource_type IN ('handout', 'lesson', 'unit-plan', 'game', 'video')
```

### **Platform Structure Only:**
```sql
-- Just site pages
WHERE resource_type LIKE '%_page'
```

### **Everything:**
```sql
-- Complete site map
SELECT * FROM graphrag_resources;
```

---

## 📊 **Current State (Complete):**

| Category | Count | Purpose |
|----------|-------|---------|
| **Teaching Content** | 126 | For teachers/students |
| **Platform Pages** | 27 | Site navigation & features |
| **Templates** | 4 | Content creation |
| **System Files** | 8 | CSS/JS infrastructure |
| **Agent Docs** | 20 | Agent coordination |
| **Total** | **185** | **Complete site map** |

**Relationships:** 96 (how components connect)  
**Database Size:** 560 kB (still tiny!)

---

## 🚀 **For Future Growth:**

### **Adding 100 New Handouts:**
```sql
-- Batch insert with auto-detection
INSERT INTO graphrag_resources (file_path, resource_type, title, subject, year_level, quality_score, archive_status)
SELECT 
  file_path,
  detect_resource_type(file_path),
  extract_title_from_path(file_path),
  extract_subject(file_path, extract_title_from_path(file_path)),
  extract_year_level(file_path),
  85,
  'active'
FROM (
  VALUES 
    ('handouts/new-handout-1.html'),
    ('handouts/new-handout-2.html'),
    -- ... etc
) AS new_files(file_path);
```

**Takes:** < 1 second  
**Manual work:** None (all auto-detected!)

---

## ✅ **What Agents Can Now See:**

### **Complete Picture:**
- ✅ All 126 teaching resources
- ✅ All 27 platform pages (what pages exist)
- ✅ All 4 templates (what can be used for creation)
- ✅ All 8 system files (design system, core JS)
- ✅ All 20 agent docs (onboarding, protocols)
- ✅ How everything connects (96 relationships)

### **Filtered Views:**
- ✅ "Show me only teaching content" (excludes cruft)
- ✅ "Show me navigation structure" (site pages)
- ✅ "Show me templates I can use" (4 templates)
- ✅ "What's the design system?" (CSS files)
- ✅ "What's my next task?" (agent docs)

---

## 💡 **Key Insight:**

**Before:** Only teaching content (incomplete picture)  
**After:** Complete site map (agents understand EVERYTHING)

**Benefit:** Agents can work on ANY part of the system because they can see the whole structure!

---

## 📚 **Reference Queries:**

```sql
-- Complete breakdown
SELECT resource_type, COUNT(*) 
FROM graphrag_resources 
GROUP BY resource_type 
ORDER BY count DESC;

-- Teaching resources only
SELECT COUNT(*) FROM get_teaching_resources();

-- Platform pages only
SELECT COUNT(*) FROM graphrag_resources WHERE resource_type LIKE '%_page';

-- System files
SELECT * FROM get_system_files();

-- Templates
SELECT * FROM graphrag_resources WHERE resource_type = 'template';
```

---

**Created:** October 28, 2025  
**Status:** Comprehensive site map complete  
**Next:** Can add more pages/files as needed

🧺 ✨ 🗺️

