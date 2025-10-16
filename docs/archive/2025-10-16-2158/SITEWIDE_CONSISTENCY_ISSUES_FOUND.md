# 🚨 SITEWIDE CONSISTENCY ISSUES - DETAILED AUDIT

**Date:** October 15, 2025, 15:05 UTC  
**Auditor:** Agent-9 (Kaitiaki Whakawhitinga)  
**Pages Sampled:** 30+ pages across all types

---

## 🔴 **CRITICAL ISSUES FOUND:**

### **1. DUPLICATE HEADERS**
**Example:** `curriculum-index.html`
- ❌ Has inline `<header>` HTML (lines 18-32)
- ❌ ALSO tries to load component: `<div id="header-component"></div>` (line 36)
- **Result:** TWO headers rendering or component failing to load
- **Impact:** Navigation broken, visual duplication

### **2. INCONSISTENT NAVIGATION**
**Variations found:**
- Some pages: "Unit Plans, Lessons, Handouts, Teachers"
- Other pages: "Curriculum, Lessons, Handouts, Interactive, Teacher Resources, Units, Resource Hub, Games, Videos"
- Component: Simple version with fewer items
- **Impact:** Users see different navigation on different pages

### **3. BROKEN CSS LINKS**
**Example:** `curriculum-index.html`, `lessons.html`
- ❌ Linking to `/css/ux-professional.css` (DELETED!)
- **Result:** 404 errors, broken styles
- **Impact:** Pages look inconsistent, missing UX enhancements

### **4. INLINE vs COMPONENT HEADERS**
**30 pages using components:**
- ✅ index.html
- ✅ curriculum-index.html (but ALSO has inline - duplicate!)
- ✅ games.html
- ✅ youtube.html
- ... 26 more

**Many pages with INLINE headers:**
- ❌ lessons.html
- ❌ Many unit pages
- ❌ Many lesson pages
- ❌ Many handout pages

### **5. FOOTER INCONSISTENCIES**
- Most pages don't use footer component
- Inline footers with varying content
- Some have no footer at all

---

## 🎯 **SYSTEMATIC FIX PLAN:**

### **Fix 1: Remove Duplicate Headers**
**Script to:**
- Find pages with BOTH inline header AND component div
- Remove inline header
- Keep only component div

### **Fix 2: Standardize CSS Links**
**Replace on ALL pages:**
```html
❌ <link rel="stylesheet" href="/css/ux-professional.css"/>
✅ <link rel="stylesheet" href="/css/ux-professional-enhancements.css"/>
```

### **Fix 3: Inject Component System**
**For pages with inline headers:**
- Replace inline header with: `<div id="header-component"></div>`
- Add component loader JS
- Ensure `components.js` is included

### **Fix 4: Standardize Navigation**
**Decision needed:** Which navigation structure?

**Option A: Simple (component version - 11 items)**
```
Curriculum | Lessons | Handouts | Interactive | Teacher Resources | 
Units | Resource Hub | Games | Videos | Activities | New Resources
```

**Option B: Focused (5 items)**
```
Unit Plans | Lessons | Handouts | Teachers | Login
```

**Recommendation:** Use Option A (comprehensive) for consistency

### **Fix 5: Footer Component Injection**
**Replace inline footers with:**
```html
<div id="footer-component"></div>
```

---

## 📊 **PRIORITY FIXES (In Order):**

1. **🔴 CRITICAL: Fix broken CSS links** (affects 100+ pages)
2. **🔴 CRITICAL: Remove duplicate headers** (affects 10-20 pages)
3. **🟡 HIGH: Standardize header navigation** (affects all pages)
4. **🟡 HIGH: Inject footer components** (affects all pages)
5. **🟢 MEDIUM: Typography consistency**
6. **🟢 MEDIUM: Spacing consistency**
7. **🟢 MEDIUM: Button standardization**

---

## 🛠️ **AUTOMATED FIX SCRIPTS:**

### **Script 1: Fix Broken CSS Links**
```bash
# Replace ux-professional.css with ux-professional-enhancements.css
find public -name "*.html" -type f -exec sed -i '' \
  's|/css/ux-professional\.css|/css/ux-professional-enhancements.css|g' {} \;
```

### **Script 2: Remove Duplicate Headers**
```bash
# Find pages with both inline and component headers
# Manual review and fix each one
```

### **Script 3: Add Missing Component JS**
```bash
# Ensure all pages load components.js
grep -L "components.js" public/*.html
```

---

## ✅ **STARTING FIXES NOW:**

**Phase 1 (Next 30 minutes):**
1. Fix all broken CSS links
2. Remove duplicate headers
3. Test on 10 sample pages
4. Update GraphRAG

**Phase 2 (Next 30 minutes):**
1. Standardize navigation across all pages
2. Inject footer components
3. Test on 20 sample pages

**Phase 3 (Next 30 minutes):**
1. Typography consistency
2. Spacing polish
3. Final testing
4. Deploy to production

---

**Ready to start systematic fixes!** 🔧

— Agent-9 (Kaitiaki Whakawhitinga)  
*Sitewide consistency guardian* 🌉

