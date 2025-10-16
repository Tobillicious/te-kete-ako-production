# 🤖 FOR FUTURE AGENTS - PLATFORM GUIDE

**Updated:** October 16, 2025  
**Purpose:** Orient new agents to Te Kete Ako development  
**Status:** Production platform, continuous improvement  

---

## 🎯 MISSION

**Build a production-quality educational platform** that:
- Integrates mātauranga Māori authentically
- Serves NZ secondary schools (Y7-13)
- Provides complete, curriculum-aligned lessons
- Grows systematically over 18 months
- Maintains cultural integrity always

**NOT:** Creating demos, prototypes, or temporary solutions  
**YES:** Building sustainable, production-ready features

---

## 📊 CURRENT STATE (October 16, 2025)

### **Platform Statistics:**
```
Total Resources: 1,520
Complete Lessons: 583
Handouts: 500+
HTML Pages: 1,500+
Professional Styling: 91.5% (1,329 pages)
Mega Menu: 607+ pages
```

### **Technical State:**
```
CSS System: Unified (6 canonical files)
Navigation: Mega menu (professional dropdown)
Mobile: Responsive throughout
Performance: 71.1% optimized
Accessibility: WCAG AA (ongoing improvement)
```

---

## 🏗️ ARCHITECTURE

### **CSS Architecture (CANONICAL):**

**Use ONLY these CSS files:**
```
1. te-kete-unified-design-system.css (foundation)
2. component-library.css (components)
3. animations-professional.css (animations)
4. beautiful-navigation.css (navigation)
5. mobile-optimization.css (responsive)
6. print.css (printing)
```

**DO NOT create new design systems!**  
If something's missing, ADD to existing files.

### **Navigation:**
- Mega menu component: `/public/components/navigation-mega-menu.html`
- Loaded via fetch on all pages
- Professional dropdown with smooth animations
- Mobile hamburger menu included

### **Directory Structure:**
```
/public/
  ├── index.html (homepage)
  ├── units/ (all unit content)
  ├── generated-resources-alpha/ (resources)
  ├── handouts/ (printable materials)
  ├── components/ (reusable components)
  ├── css/ (canonical CSS only!)
  └── js/ (JavaScript)
```

---

## 🚨 CRITICAL RULES

### **1. NO Demo Divergence**
- Build features for PRODUCTION use
- Everything must be permanent and sustainable
- No temporary "demo" versions
- Ask: "Will this be valuable after Oct 22?" (must be YES)

### **2. Coordinate via MCP & GraphRAG**
**Before starting ANY work:**
1. Check GraphRAG for recent updates
2. Read SESSION_COMPLETE files
3. Check ACTIVE_QUESTIONS.md
4. Verify no one else working on same area
5. Update GraphRAG with your plans

**After completing work:**
1. Insert GraphRAG record
2. Update coordination files
3. Document changes
4. Test thoroughly

### **3. CSS Coordination**
- Use canonical CSS files ONLY
- Check CSS_ARCHITECTURE_CANONICAL.md first
- Don't create competing systems
- Coordinate with other agents

### **4. Cultural Integrity**
- Consult on Te Reo Māori usage
- Verify cultural accuracy
- Respectful representation always
- When unsure, ASK

### **5. Quality Standards**
- Test on multiple browsers
- Verify mobile experience
- Check accessibility
- Performance matters
- Real NZ resources (verify links!)

---

## 📁 KEY FILES TO READ FIRST

### **Current State:**
1. `SESSION_COMPLETE_OCT16_EVENING.md` - Latest status
2. `COLLABORATIVE_ACTION_PLAN_OCT16.md` - Team priorities
3. `HONEST_ASSESSMENT_QUALITY.md` - Quality status

### **Architecture:**
1. `CSS_ARCHITECTURE_CANONICAL.md` - CSS system (CRITICAL!)
2. `18_MONTH_ROADMAP.md` - Long-term vision
3. `CULTURAL_INTEGRITY_STATEMENT.md` - Cultural approach

### **Coordination:**
1. `ACTIVE_QUESTIONS.md` - Current issues/questions
2. GraphRAG - Query for recent work
3. Any AGENT_COORDINATION_*.md files

---

## 🔧 COMMON TASKS

### **Adding Mega Menu to a Page:**
```html
<body>
    <!-- Professional Mega Menu Navigation -->
    <script>
        fetch('/components/navigation-mega-menu.html')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>
    <!-- Rest of page content -->
</body>
```

### **Loading Canonical CSS:**
```html
<head>
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">
    <link rel="stylesheet" href="/css/component-library.css">
    <link rel="stylesheet" href="/css/animations-professional.css">
    <link rel="stylesheet" href="/css/beautiful-navigation.css">
    <link rel="stylesheet" href="/css/mobile-optimization.css">
    <link rel="stylesheet" href="/css/print.css" media="print">
</head>
```

### **Updating GraphRAG:**
```sql
INSERT INTO resources (title, description, path, type, subject, level, tags, author)
VALUES (
    'Your Work Title',
    'Clear description of what you did, why, and impact',
    '/your-work-path',
    'activity',
    'Development',
    'All Levels',
    ARRAY['relevant', 'tags', 'here'],
    'Your Agent Name'
);
```

---

## 🎯 CURRENT PRIORITIES (Oct 2025)

**From Collaborative Action Plan:**

**TIER 1 (Must Do):**
1. Testing & quality assurance
2. Documentation (for Oct 22)
3. Mega menu verification
4. Final polish

**TIER 2 (Should Do):**
1. Git commits (repository health)
2. Performance optimization
3. Accessibility improvements

**TIER 3 (Post-Oct 22):**
1. Additional features
2. Content expansion
3. Advanced capabilities

---

## 💡 DECISION FRAMEWORK

### **Before Adding Anything, Ask:**

1. **Is this production-ready?**
   - Will teachers actually use this?
   - Is it permanent, not temporary?

2. **Does this exist already?**
   - Check existing CSS/components
   - Avoid duplication

3. **Am I coordinating?**
   - Checked GraphRAG?
   - Informed other agents?

4. **Is this culturally appropriate?**
   - Verified Te Reo usage?
   - Respectful representation?

5. **Can I test this?**
   - Multiple browsers?
   - Mobile devices?
   - Accessibility?

**If YES to all → Proceed!**  
**If NO to any → Pause and coordinate**

---

## 🚨 WHAT NOT TO DO

### **DON'T:**
- ❌ Create separate demo versions
- ❌ Add new CSS files without coordination
- ❌ Ignore GraphRAG updates
- ❌ Work in isolation
- ❌ Use temporary solutions
- ❌ Skip testing
- ❌ Assume cultural accuracy

### **DO:**
- ✅ Build for production
- ✅ Use canonical CSS
- ✅ Coordinate via MCP/GraphRAG
- ✅ Collaborate with team
- ✅ Create sustainable solutions
- ✅ Test thoroughly
- ✅ Consult on cultural matters

---

## 📊 HOW TO CHECK CURRENT STATUS

### **Via GraphRAG (Supabase MCP):**
```sql
-- Recent work (last 3 hours)
SELECT title, description, created_at, author
FROM resources
WHERE created_at >= NOW() - INTERVAL '3 hours'
ORDER BY created_at DESC;

-- Total resources
SELECT COUNT(*) FROM resources;
```

### **Via Files:**
```bash
# Latest session summary
cat SESSION_COMPLETE_*.md | tail -1

# Current questions/issues
cat ACTIVE_QUESTIONS.md

# Current priorities
cat COLLABORATIVE_ACTION_PLAN_OCT16.md
```

---

## 🤝 AGENT ROLES

### **Different Agents, Different Strengths:**
- Some focus on CSS/design
- Some focus on content/lessons
- Some focus on testing/QA
- Some focus on coordination
- Some focus on cultural consultation

**Find your strength, coordinate with others!**

---

## 🧺 CULTURAL NOTES

### **Te Reo Māori:**
- Macrons matter! (ā, ē, ī, ō, ū)
- Verify spelling with authoritative sources
- Respect for language essential

### **Cultural Concepts:**
- Whakapapa (genealogy, connections)
- Manaakitanga (hospitality, care)
- Kaitiakitanga (guardianship)
- Whanaungatanga (relationships)

**When in doubt, ASK or RESEARCH!**

---

## ✅ SUCCESS METRICS

### **Technical:**
- Pages load fast (<3s)
- Mobile-responsive
- Accessible (WCAG AA)
- No console errors
- Cross-browser compatible

### **Content:**
- Curriculum-aligned
- Complete lesson plans
- Verified NZ resources
- Culturally authentic
- Ready to use

### **Coordination:**
- GraphRAG updated
- Other agents informed
- Documentation complete
- Tests passed

---

## 🎯 REMEMBER

**You're building something REAL and USEFUL!**

- Teachers will use this
- Students will benefit
- Cultural integrity matters
- Quality over speed
- Coordinate always
- Test thoroughly

**Mā te mōhio ka ora! 🧺✨**

---

**Questions? Check:**
1. ACTIVE_QUESTIONS.md
2. GraphRAG recent updates
3. SESSION_COMPLETE files
4. Or add your question to ACTIVE_QUESTIONS.md!

---

**Welcome to Te Kete Ako development!**  
**Let's build something excellent together!** 🚀

