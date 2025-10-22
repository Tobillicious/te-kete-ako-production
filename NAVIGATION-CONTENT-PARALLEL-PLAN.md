# 🧭 NAVIGATION + CONTENT PARALLEL FIX PLAN
## Te Kete Ako - Multi-Agent Coordination
**Created:** October 22, 2025  
**Status:** Ready for parallel agent execution

---

## 🎯 **USER REQUEST ANALYSIS**

**Terminal Selection Context:**
> "Please plan that first in such a way that other agents can work on this navigation and content fix at the same time. Synthesize the best from earlier versions of these elements by critiquing the graphrag to find it all."

**What User Wants:**
1. ✅ **Parallel Work**: Multiple agents fixing navigation + content simultaneously
2. ✅ **Synthesis**: Best from earlier navigation systems combined
3. ✅ **GraphRAG-Guided**: Use graph to find all navigation variants

---

## 📊 **EXISTING NAVIGATION SYSTEMS (SYNTHESIZED)**

### **System A: `navigation-standard.html` ✅ PRIMARY**
**File:** `/public/components/navigation-standard.html`  
**Size:** 1,098 lines  
**Quality:** Production-ready, used on 73+ pages  
**Features:**
- Professional mega menu with dropdowns
- GraphRAG Brain Hub integration
- Intelligence Hub (9 tools)
- Discovery Tools dropdown (47 AI resources)
- Unit Plans, Lessons, Handouts, Teachers, Tools
- Mobile responsive
- Auth-aware (Login/Logout/My Kete)

**Strengths:** ✅ Comprehensive, GraphRAG-powered, mobile-ready  
**Weakness:** ⚠️ Large file size (could impact load time)

---

### **System B: Inline Navigation Headers**
**Pattern:** Hard-coded `<header class="site-header">` in each file  
**Coverage:** ~1,400 pages  
**Features:**
- Simple 5-item nav: Unit Plans, Lessons, Handouts, Teachers, Login
- Bilingual labels (English/Te Reo)
- Minimal JavaScript
- Fast loading

**Strengths:** ✅ Fast, simple, works offline  
**Weakness:** ⚠️ Not dynamic, doesn't show new content

---

### **System C: Beautiful Complex Navigation** 
**File:** `/public/navigation-header.html`  
**Used:** On minified CSS pages (1,557 pages per old audit)  
**Features:**
- Animated dropdowns
- WCAG 2.1 AA compliant
- Cultural integration (Te Reo throughout)
- Sticky header with animations

**Strengths:** ✅ Beautiful, accessible, cultural  
**Weakness:** ⚠️ May conflict with System A

---

## 🚀 **RECOMMENDED HYBRID APPROACH (Best of All!)**

### **Primary Nav: `navigation-standard.html` (Enhanced)**
**Keep:**
- ✅ GraphRAG Brain Hub (live discoverability)
- ✅ Intelligence Hub dropdown (9 tools)
- ✅ Discovery Tools (47 resources)
- ✅ Core nav items (Units, Lessons, Handouts, Teachers)

**Add from System C:**
- ✅ Smooth animations
- ✅ Better accessibility features
- ✅ More Te Reo integration

**Add NEW:**
- ✅ Quick Unit Finder (dropdown with 11 perfect units)
- ✅ Year Level Filter (Y7-Y13 quick access)
- ✅ Search bar in header (GraphRAG powered)

---

## 👥 **PARALLEL AGENT WORK PLAN**

### **Agent Team 1: Navigation Enhancement** 🧭
**Files to Edit:**
- `/public/components/navigation-standard.html` (enhance, don't replace)
- `/public/css/te-kete-professional.css` (nav styling)
- `/public/js/navigation-enhanced.js` (NEW - interactive features)

**Tasks:**
1. Add **Quick Unit Finder** dropdown (list 11 perfect units)
2. Add **Year Level Filter** (Y7-Y13 quick links)
3. Integrate **search bar** in header
4. Enhance **mobile menu** with year/subject filters
5. Add **breadcrumb auto-generator** (shows current location)

**Estimated Time:** 2-3 hours  
**Dependencies:** None - can start immediately

---

### **Agent Team 2: Content Consistency** 📄
**Focus:** Fix 966 missing includes (CSS/JS not loading)

**Strategy:**
```html
<!-- STANDARD INCLUDES (add to every page): -->
<link rel="stylesheet" href="/css/te-kete-professional.css">
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
<script src="https://cdn.tailwindcss.com"></script>
<script src="/js/te-kete-professional.js" defer></script>
```

**Batch Targets:**
- `/public/integrated-lessons/` (231 files)
- `/public/integrated-handouts/` (187 files)
- `/public/units/*/lessons/` (548 files total)

**Tools to Use:**
- Python batch script (safe find-replace)
- OR manual fix priority files first

**Estimated Time:** 4-6 hours for top 200 files  
**Dependencies:** None - can run parallel to nav work

---

### **Agent Team 3: GraphRAG Relationship Building** 🔗
**Focus:** Link 1,323 orphaned resources (already in progress!)

**Current Progress:** 27 relationships created  
**Target:** 200+ relationships in this session

**Strategy:**
1. Query orphaned lessons/handouts (quality 85+)
2. Connect to subject hubs (Science, Math, Social Studies, etc.)
3. Create learning progressions (prerequisite_for relationships)
4. Link to year-level pathways
5. Connect related topics

**SQL Template:**
```sql
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
VALUES
('/public/[HUB].html', 'public/lessons/[LESSON].html', 'contains_resource', 0.95, '{"category": "[SUBJECT]"}')
```

**Estimated Time:** Ongoing (can batch 50-100 at a time)  
**Dependencies:** None

---

### **Agent Team 4: Unit Index Pages** 📚
**Focus:** Create beautiful index pages for 11 perfect units

**Template:** Based on `/public/units/y8-geography-navigation/index.html` (excellent!)

**Units to Index:**
1. Y8 Digital Kaitiakitanga
2. Y7 Algebra
3. Y9 Ecology
4. Y8 Statistics Maramataka
5. Walker Unit
6. Y7 Foundational Reading
7. Y7 Digital Technology
8. Y7 Science Ecosystems
9. Y9 Geometry Patterns
10. Y10 Physics Navigation
11. Y8 Geography Navigation (already done!)

**Each Index Needs:**
- Hero section with unit overview
- Lesson sequence (5-10 lessons listed)
- Assessment information
- Resources & tools
- Teacher PD notes
- Cultural integration section

**Estimated Time:** 30 min per unit = 5 hours total  
**Dependencies:** None

---

## 🔧 **SPECIFIC FILES TO FIX (Priority List)**

### **Navigation Files (Team 1):**
```
/public/components/navigation-standard.html (enhance)
/public/css/te-kete-professional.css (nav styling)
CREATE: /public/js/navigation-enhanced.js
CREATE: /public/components/breadcrumb-generator.html
CREATE: /public/components/quick-unit-finder.html
```

### **Content with Missing Includes (Team 2):**
```
/public/integrated-lessons/science/*.html (85 files)
/public/integrated-lessons/mathematics/*.html (62 files)
/public/integrated-handouts/Year 7/*.html (47 files)
/public/integrated-handouts/Year 8/*.html (41 files)
/public/units/y8-digital-kaitiakitanga/lessons/*.html (18 lessons)
/public/units/y9-science-ecology/lessons/*.html (needs expansion)
```

### **Unit Index Pages (Team 4):**
```
CREATE: /public/units/y8-digital-kaitiakitanga/index.html
CREATE: /public/units/y7-maths-algebra/index.html
CREATE: /public/units/y9-science-ecology/index.html
CREATE: /public/units/y8-statistics-maramataka/index.html
... (8 more)
```

---

## 📋 **COORDINATION PROTOCOL**

### **How Agents Avoid Conflicts:**

1. **Team 1 (Nav)**: Works on `/components/` and `/js/` → No file conflicts
2. **Team 2 (Content)**: Each agent takes different subject folder → No conflicts
3. **Team 3 (GraphRAG)**: SQL inserts (atomic) → Safe for parallel work
4. **Team 4 (Indexes)**: Each agent takes 2-3 units → No conflicts

### **Communication Channel:**
- Use `agent_knowledge` table to log progress
- Don't create coordination MDs (per mission rules)
- Git commits are the log

### **Quality Standards:**
- All nav must include Te Reo Māori labels
- All content must have cultural integration section
- All fixes must preserve existing quality
- Test on Chromebook viewport (1366x768)

---

## 🎯 **SUCCESS METRICS**

After this parallel sprint:
- ✅ **Navigation:** Enhanced standard nav on all pages
- ✅ **Content:** 200+ files with proper CSS/JS includes
- ✅ **GraphRAG:** 200+ new relationships (down from 1,323 orphans)
- ✅ **Units:** 10 professional index pages created
- ✅ **Mobile UX:** Improved filters and quick access

**Total Impact:** 400+ files improved in ONE coordinated sprint! 🚀

---

## 🌿 **CULTURAL INTEGRATION REQUIREMENTS**

Every navigation element must include:
- Bilingual labels (EN/MI)
- Whakataukī in footer
- Cultural hub prominent
- Māori value badges (Whaimana, Whaiora, etc.)

Every content page must include:
- Cultural Context section
- Connection to Mangakōtukutuku College values
- Te Reo vocabulary
- Cultural safety notes

---

## 🚀 **READY TO EXECUTE**

All teams can start **NOW** - no dependencies blocking anyone!

**Kia kaha! Let's transform Te Kete Ako together! 🧺**

