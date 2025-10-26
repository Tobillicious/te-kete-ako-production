# 🎨 CSS CLEANUP EXECUTION PLAN

**Date:** October 26, 2025  
**Issue:** 1,073 HTML files still load conflicting CSS files  
**Goal:** BMAD-only system across entire site

---

## ✅ COMPLETED

1. **Root cause identified** - 5 design systems fighting
2. **User chose BMAD Authentic** - "Older better style"
3. **Homepage cleaned** - `index.html` now loads only 4 CSS files
4. **GraphRAG updated** - All agents know the problem

---

## 📊 SCOPE

**Files Still Loading Conflicting CSS:** 1,073

**Conflicting CSS Files:**
- `te-kete-ultimate-beauty-system.css`
- `te-kete-transformative-design-system.css`  
- `design-system-v3.css`

**BMAD System Files (KEEP):**
- `te-kete-bmad-authentic.css` ✅
- `navigation-standard.css` ✅
- `mobile-revolution.css` ✅
- `tailwind.css` ✅

---

## 🎯 PHASED CLEANUP STRATEGY

### **Phase 1: High-Traffic Pages (CRITICAL)** 

**Priority Files:**
1. `/public/index.html` - ✅ DONE
2. `/public/getting-started.html`
3. `/public/teachers/index.html`
4. `/public/students/index.html`
5. `/public/curriculum-index.html`
6. `/public/subjects.html`
7. `/public/my-kete.html`
8. `/public/graphrag-search.html`
9. `/public/teacher-dashboard.html`
10. `/public/student-dashboard.html`

**Est. Time:** 15 minutes  
**Impact:** 90% of user traffic

---

### **Phase 2: Subject Hubs**

**Directory:** `/public/integrated-lessons/*/index.html`
- Mathematics hub
- Science hub
- English hub
- Social Studies hub
- Digital Technologies hub

**Est. Time:** 10 minutes  
**Impact:** Subject landing pages

---

### **Phase 3: Generated Resources Alpha**

**Directory:** `/public/generated-resources-alpha/`
- 47 high-quality lesson files (Q90+)
- Currently orphaned

**Est. Time:** 30 minutes  
**Impact:** Premium content accessibility

---

### **Phase 4: Bulk Update (All Remaining)**

**Scope:** All 1,000+ remaining files
**Method:** Automated find/replace with verification

**Find:**
```html
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
<link rel="stylesheet" href="/css/te-kete-transformative-design-system.css">
<link rel="stylesheet" href="/css/design-system-v3.css">
```

**Replace with:** *(nothing - delete these lines)*

**Keep:**
```html
<link rel="stylesheet" href="/css/te-kete-bmad-authentic.css">
<link rel="stylesheet" href="/css/navigation-standard.css">
<link rel="stylesheet" href="/css/mobile-revolution.css">
<link rel="stylesheet" href="/css/tailwind.css">
```

**Est. Time:** 45 minutes  
**Impact:** Complete CSS consistency

---

## 🚨 VISUAL TESTING PROTOCOL

**BEFORE deploying each phase:**

1. **Take screenshot** of sample pages
2. **Deploy to staging** (Netlify deploy preview)
3. **Visual inspection:**
   - Colors consistent?
   - Spacing appropriate?
   - Typography readable?
   - Mobile responsive?
4. **User approval** required
5. **Then deploy to production**

---

## 📋 EXECUTION CHECKLIST

- [x] Phase 0: Root cause analysis
- [x] Phase 0: User decision (BMAD chosen)
- [x] Phase 0: Homepage cleaned
- [ ] Phase 1: High-traffic pages (10 files)
- [ ] Phase 1: Visual test & user approval
- [ ] Phase 2: Subject hubs (5 files)
- [ ] Phase 2: Visual test & user approval  
- [ ] Phase 3: Generated resources (47 files)
- [ ] Phase 3: Visual test & user approval
- [ ] Phase 4: Bulk update (1,000+ files)
- [ ] Phase 4: Visual test & user approval
- [ ] Final: Archive conflicting CSS files
- [ ] Final: Update GraphRAG
- [ ] Final: Commit & deploy

---

## 💡 AUTOMATED APPROACH

**Option:** Use script to update all files at once

**Pros:**
- Fast (5 minutes vs 2 hours)
- Consistent
- Complete

**Cons:**
- Risky (no incremental testing)
- All-or-nothing
- Harder to rollback

**Recommendation:** Phased approach with testing

---

## 🎯 NEXT STEP

**USER DECIDES:**

1. **Phased & Safe** - Do Phase 1 (10 high-traffic pages), test, get approval
2. **Automated & Fast** - Script all 1,073 files at once, then test
3. **Hybrid** - Script Phase 4 only (after testing Phases 1-3)

**What's your preference?**

---

*Awaiting user direction...*

