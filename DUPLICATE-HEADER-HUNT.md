# 🔍 DUPLICATE HEADER HUNT - Finding All 4 Headers

**Task:** Find where 4 headers are coming from  
**Agent:** Cursor Sonnet 4.5  
**Method:** Systematic search

---

## 🎯 **WHAT WE KNOW**

**Playwright Testing Found:**
- Homepage has **4 header/nav elements**
- /units/ page has **2 complete headers**

**What We've Checked:**

✅ index.html loads only 1 header: `navigation-standard.html`  
✅ No `header.html` or `header-enhanced.html` loading  
✅ No mega-navigation loading  
❓ But Playwright says there are 4!

---

## 🔍 **POSSIBLE SOURCES:**

### **Source 1:** navigation-standard.html (confirmed)
- Loaded at line 79 of index.html
- Contains `<header class="site-header-synthesis">`

### **Source 2:** Hardcoded breadcrumb (confirmed)  
- Line 407 in index.html
- `<nav aria-label="Breadcrumb" class="breadcrumb-nav">`

### **Source 3 & 4:** ❓ **MYSTERY!**

**Possibilities:**
1. Components loading other components (nested fetch)
2. JavaScript dynamically creating headers
3. CSS pseudo-elements creating visual headers
4. Multiple nav elements being counted as headers

---

## 📋 **SEARCH RESULTS:**

**navigation-standard.html contains:**
- Checking...


