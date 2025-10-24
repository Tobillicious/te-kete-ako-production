# 🔍 SITEWIDE VISUAL ISSUE - Root Cause Analysis

**Issue:** Abstract shapes/broken layouts appearing sitewide  
**Not just:** perfect-learning-pathways.html  
**Impact:** SITEWIDE systemic problem

---

## 🚨 **WHAT WE KNOW**

1. **Console is clean** ✅ (only PWA icon warning)
2. **GraphRAG backend works** ✅ (we want this!)
3. **CSS files ARE loading** (colors/gradients appear)
4. **BUT layout/structure is broken** ❌ (abstract shapes)

---

## 🎯 **POSSIBLE SITEWIDE CAUSES**

### **Hypothesis 1: Missing Critical CSS Classes**
- Many pages use classes that don't exist in CSS
- Browser falls back to default (broken) rendering
- **Need:** Comprehensive CSS class audit

### **Hypothesis 2: CSS Load Order**
- Critical CSS not loading first
- Inline styles override intended design
- **Need:** Check CSS load order

### **Hypothesis 3: Conflicting Styles**
- Multiple CSS files with conflicting rules
- Some pages get wrong combination
- **Need:** CSS consolidation

### **Hypothesis 4: JavaScript Breaking CSS Application**
- JS error prevents dynamic styling
- Components don't initialize properly
- **Need:** Check for early JS errors

---

## 🔬 **INVESTIGATING NOW...**

Need to identify:
1. What CSS files are supposed to load on ALL pages?
2. What critical classes are missing sitewide?
3. Are there any early-stage errors breaking initialization?
4. What's the correct CSS architecture?

---

**Status:** 🔍 **DIAGNOSING SITEWIDE ISSUE...**

