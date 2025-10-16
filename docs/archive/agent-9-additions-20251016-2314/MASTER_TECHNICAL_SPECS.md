# Technical Specs - Master Reference

*Auto-generated: 2025-10-16 22:49*

**Source:** Synthesized from 1 MD files

---

## MASTER_TECH_SPECS.md

# 🔧 TE KETE AKO - MASTER TECHNICAL SPECIFICATIONS

**Last Updated:** Oct 16, 2025  
**Purpose:** THE ONLY technical reference - use this!

---

## 🎨 **CSS (USE ONLY THESE 8 FILES):**

```html
<!-- CANONICAL CSS SYSTEM -->
<link rel="stylesheet" href="/css/te-kete-unified-design-system.css" />
<link rel="stylesheet" href="/css/component-library.css" />
<link rel="stylesheet" href="/css/animations-professional.css" />
<link rel="stylesheet" href="/css/beautiful-navigation.css" />
<link rel="stylesheet" href="/css/mobile-optimization.css" />
<link rel="stylesheet" href="/css/print.css" media="print" />

<!-- Optional: For lessons -->
<link rel="stylesheet" href="/css/lesson-professionalization.css" />

<!-- Optional: For unit indexes -->
<link rel="stylesheet" href="/css/unit-index-professionalization.css" />
```

**DON'T use:** Any CSS in /css/archive/ or minified paths

---

## 🔐 **AUTHENTICATION:**

### **Supabase:**
```
URL: https://nlgldaqtubrlcqddppbq.supabase.co
Anon Key: (in /public/js/supabase-client.js)
```

### **Pages:**
```
Student Signup: /signup-student.html
Teacher Signup: /signup-teacher.html
Login: /login.html (to be created)
Student Dashboard: /student-portal.html (to be created)
Teacher Dashboard: /teachers/dashboard.html ✅
```

### **Database Tables:**
```
profiles (extended with 20+ NZ fields)
nz_schools (real NZ schools)
teacher_classes (class management)
student_progress (learning tracking)
kamar_sync_log (integration logging)
agent_coordination (agent work tracking) ✅ NEW
```

---

## 🧭 **NAVIGATION:**

### **Components:**
```
Mega Menu: /components/navigation-mega-menu.html
Related Resources: /components/related-resources.html ✅ NEW
Phenomenal Hero: /components/phenomenal-hero.html
```

### **JavaScript:**
```
Auth: /js/supabase-auth.js (canonical)
Navigation: /js/navigation-enhanced.js
Related Resources: /js/related-resources.js ✅ NEW
```

---

## 📊 **GRAPHRAG (Supabase):**

### **Tables:**
```
resources: 1,566 entries (lessons, handouts, units, etc)
agent_coordination: Agent work tracking ✅ NEW
```

### **Query Pattern:**
```sql
-- Find related resources
SELECT title, path, subject, level
FROM resources
WHERE type = 'lesson'
AND subject = 'Social Studies'
AND level LIKE '%8%'
LIMIT 5;
```

---

## 🏗️ **CONTENT STRUCTURE:**

```
UNIT
├─ /units/{unit-name}/index.html
├─ /units/{unit-name}/lessons/
│  ├─ lesson-1.html
│  └─ lesson-2.html
├─ /units/{unit-name}/resources/ (optional)
└─ Related via GraphRAG
```

---

## 📱 **DEVELOPMENT:**

```bash
# Run dev server:
npm run dev
# Serves on http://localhost:5173

# Check agent coordination:
python3 scripts/agent-coordination-check.py

# Log work:
python3 scripts/log-agent-work.py
```

---

**This is THE technical reference. Update THIS, not create new specs!**



---

