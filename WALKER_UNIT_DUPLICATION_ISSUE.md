# 🔗 Walker Unit File Duplication Issue
**Discovered by:** Kaitiaki Tūhono (Guardian of Connections)  
**Date:** 2025-10-14  
**Priority:** Medium (causes maintenance complexity)

---

## 📊 Issue Summary

The Walker Unit lessons exist in **3 separate locations** with slight naming variations, causing:
- Maintenance complexity (changes need to be made 3x)
- Link confusion (multiple valid paths to same content)
- Storage redundancy (~15 duplicate files)

---

## 📁 Current File Locations

### Location 1: `/public/lessons/walker-lesson-X.html` (5 files)
```
walker-lesson-1.1-who-was-ranginui-walker.html
walker-lesson-1.2-the-great-migration.html
walker-lesson-1.3-years-of-anger.html
walker-lesson-1.4-a-forum-for-justice.html
walker-lesson-1.5-reclaiming-the-narrative.html
```

### Location 2: `/public/lessons/walker/lesson-X.html` (5 files)
```
lesson-1-1-who-was-ranginui-walker.html
lesson-1-2-the-great-migration.html
lesson-1-3-years-of-anger.html
lesson-1-4-a-forum-for-justice.html
lesson-1-5-reclaiming-the-narrative.html
```

### Location 3: `/public/units/walker-unit/walker-lesson-X.html` (5 files)
```
walker-lesson-1.1-who-was-ranginui-walker.html
walker-lesson-1.2-the-great-migration.html
walker-lesson-1.3-years-of-anger.html
walker-lesson-1.4-a-forum-for-justice.html
walker-lesson-1.5-reclaiming-the-narrative.html
```

### Hub Page: `/public/lessons/walker/index.html` ✅
This is the canonical hub page that should link to all lessons.

---

## 🎯 Recommended Solution

**Option 1: Consolidate to `/public/units/walker-unit/`** (Preferred)
- Aligns with other units (y8-critical-thinking, y9-science-ecology)
- Clear hierarchical structure
- Easier to maintain

**Option 2: Consolidate to `/public/lessons/walker/`**
- Current hub page location
- Keeps lessons with other standalone lessons

**Option 3: Keep current structure but add redirects**
- Maintain all 3 locations
- Add HTML redirects from duplicates to canonical version
- Less clean but preserves existing links

---

## 📋 Implementation Steps (Option 1 - Recommended)

1. **Choose canonical location:** `/public/units/walker-unit/`

2. **Update all internal links** to point to canonical location:
   - curriculum-index.html
   - Any cross-references from other lessons
   - Hub page (/lessons/walker/index.html)

3. **Create redirects** from old locations:
   ```html
   <!-- In /public/lessons/walker-lesson-1.1-who-was-ranginui-walker.html -->
   <meta http-equiv="refresh" content="0; url=/units/walker-unit/walker-lesson-1.1-who-was-ranginui-walker.html">
   ```

4. **Update navigation arrays** in JavaScript files

5. **Test all navigation paths** to Walker Unit

6. **Document canonical URLs** in sitemap

---

## ⚠️ Impact Assessment

**Low Risk:**
- Files are duplicates (same content)
- Hub page exists and working
- Can implement gradually with redirects

**Medium Complexity:**
- Need to update links across site
- Should coordinate with agent-4 (Navigation Specialist)
- Requires testing after changes

**High Value:**
- Simplifies future maintenance
- Reduces confusion for content creators
- Aligns with site structure standards

---

## 🤝 Coordination Needed

**Agent-4 (Navigation Specialist):**
- Review recommended structure
- Implement consolidation plan
- Test all navigation flows

**Agent-3 (Content Specialist):**
- Verify no content differences between duplicates
- Confirm which version is most current

**Agent-12 (Overseer):**
- Approve consolidation approach
- Coordinate timing with other work

---

## 📝 Current Status

- ✅ Issue identified and documented
- ✅ All 3 locations mapped
- ✅ Links within unit fixed to use correct hub
- ⏳ Consolidation plan needs team approval
- ⏳ Implementation pending coordination

---

**Documented by:** Kaitiaki Tūhono (Guardian of Connections)  
**Next Action:** Coordinate with agent-4 and agent-12 for implementation

*"Ko te tūhono te pūtake o te mātauranga"*  
*Connection is the foundation of knowledge*


