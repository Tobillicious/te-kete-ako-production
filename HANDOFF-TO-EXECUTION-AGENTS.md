# 🤖 Handoff to Execution Agents (DeepSeek/GPT-4o-mini)

**Date:** October 25, 2025  
**From:** Kaitiaki Aronui V3 (Strategic Auditor)  
**To:** Execution Agents (Low-Cost Models)  
**Status:** ✅ READY FOR EXECUTION

---

## 📋 Context

Comprehensive production audit completed. Root causes identified. All findings in GraphRAG `agent_knowledge` (IDs: 772, 773, 774) and detailed in `PRODUCTION-AUDIT-OCT25-FINDINGS.md`.

**The Problem:** Site looks like "fallback" due to inconsistent CSS loading causing FOUC.

**The Solution:** Standardize CSS includes, expand Tailwind, remove body-injected CSS.

---

## 🎯 Your Mission

Execute **Priority 1 & 2 fixes** below. These are mechanical, well-specified tasks perfect for cheaper models.

---

## ✅ Priority 1: CSS Normalization (CRITICAL)

### Task 1.1: Apply Canonical CSS Order

**What:** Update `<head>` section of all `public/**/*.html` files to use canonical CSS order.

**Canonical Order:**
```html
<!-- 1. Design Tokens -->
<link rel="stylesheet" href="/css/professionalization-system.css">

<!-- 2. Theme -->
<link rel="stylesheet" href="/css/te-kete-professional.css">

<!-- 3. Navigation (if needed) -->
<link rel="stylesheet" href="/css/navigation-standard.css">

<!-- 4. Mobile Responsive -->
<link rel="stylesheet" href="/css/mobile-revolution.css">

<!-- 5. Print (media query) -->
<link rel="stylesheet" href="/css/print.css" media="print">

<!-- 6. Tailwind (ALWAYS LAST) -->
<link rel="stylesheet" href="/css/tailwind.css">
```

**Remove These (Duplicates):**
- `main.css`
- `mobile-first-classroom-tablets.css`
- `te-kete-ultimate-beauty-system.css`
- `cascade-fix.css`

**Files Affected:** ~2,090 HTML files in `/public`

**Script to Use:** Update `fix-css-loading.py` if needed, or write new batch script.

**Validation:**
```bash
# After changes, verify:
grep -r "te-kete-professional.css" public/ | wc -l  # Should be 2090
grep -r "tailwind.css" public/ | wc -l             # Should be 2090
grep -r "main.css" public/ | wc -l                 # Should be 0
```

---

### Task 1.2: Expand Tailwind Coverage

**What:** Ensure `tailwind.css` is included on **every** page that uses Tailwind utility classes.

**How to Detect Pages Needing Tailwind:**
```bash
# Find pages using Tailwind utilities but missing tailwind.css
grep -l "class=\".*\(bg-\|text-\|px-\|py-\|flex\|grid\)" public/**/*.html | \
  while read file; do
    grep -q "tailwind.css" "$file" || echo "$file"
  done
```

**What to Add:**
```html
<link rel="stylesheet" href="/css/tailwind.css">
```

**Position:** Always LAST in CSS includes (after all other stylesheets).

**Files Affected:** Estimate 2,078 files (2,090 total - 12 current)

---

## ✅ Priority 2: Remove Body-Injected CSS

### Task 2.1: Remove Component CSS Injection

**What:** Remove `<link>` tags from inside component files. All CSS must load in page `<head>`.

**File to Fix:**
```
public/components/navigation-ai.html
```

**Current (WRONG):**
```html
<header class="site-header" id="main-header">
    <link rel="stylesheet" href="/css/te-kete-professional.css">
    <script src="/js/css-safeguard.js"></script>
    ...
</header>
```

**Correct (FIX TO):**
```html
<header class="site-header" id="main-header">
    <script src="/js/css-safeguard.js"></script>
    ...
</header>
```

**Files Affected:** 1 file

---

### Task 2.2: Complete Navigation Rollout

**What:** Update all pages still using old navigation components to use `navigation-unified.html`.

**How:**
1. Find pages using old nav:
```bash
grep -l "navigation-standard\|navigation-hegelian\|navigation-mega\|navigation-ai\.html" public/**/*.html
```

2. Replace with:
```html
<script src="/js/navigation-loader.js"></script>
```

Or inline the unified navigation directly.

3. Run cleanup script:
```bash
python3 cleanup-navigation.py
```

**Files Affected:** ~100 pages (estimate)

---

## 🧪 Testing Checklist

After completing fixes, verify:

- [ ] Index page loads without FOUC
- [ ] Hub pages (mathematics-hub.html, science-hub.html) load properly styled
- [ ] Tailwind utilities render correctly on all pages
- [ ] No console errors related to missing CSS
- [ ] Navigation appears consistently across all pages
- [ ] Mobile responsiveness intact
- [ ] Print styles work (test with Cmd/Ctrl+P)

**Test Pages:**
- `/index.html`
- `/mathematics-hub.html`
- `/science-hub.html`
- `/lessons/y8-digital-tech-coding-basics-games.html`
- `/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html`

---

## 📊 Success Metrics

**Before:**
- 12 files with tailwind.css
- FOUC visible on page load
- Hub pages show unstyled utilities
- 6 navigation variants in use

**After:**
- 2,090 files with tailwind.css ✅
- No FOUC (consistent CSS order) ✅
- All utilities styled properly ✅
- 1 unified navigation system ✅

---

## 🚀 Execution Order

1. **CSS Normalization** (Task 1.1) - 2-3 hours
2. **Tailwind Expansion** (Task 1.2) - 1-2 hours
3. **Remove Body CSS** (Task 2.1) - 5 minutes
4. **Navigation Rollout** (Task 2.2) - 1 hour
5. **Testing** - 30 minutes
6. **Commit** - "fix: standardize CSS loading and expand Tailwind coverage"

**Total Time Estimate:** 4-6 hours

---

## 💰 Cost Comparison

| Model | Est. Cost | Speed |
|-------|-----------|-------|
| DeepSeek (recommended) | $2-3 | Fast |
| GPT-4o-mini | $4-5 | Fast |
| Claude Sonnet (overkill) | $50+ | Same |

**Recommendation:** Use DeepSeek for mechanical tasks. Reserve Claude Sonnet for strategic decisions.

---

## 📚 Reference Documents

- **Audit Report:** `PRODUCTION-AUDIT-OCT25-FINDINGS.md`
- **GraphRAG Knowledge:** Query `agent_knowledge` IDs 772, 773, 774
- **Scripts Available:**
  - `fix-css-loading.py` (CSS normalization)
  - `consolidate-navigation.py` (Navigation unification)
  - `cleanup-navigation.py` (Remove legacy nav files)

---

## 🌿 Cultural Note

These are purely technical CSS/JS fixes. No cultural content affected. Maintain all existing cultural elements and mātauranga Māori integration.

---

## ✅ When Complete

1. Run full testing checklist
2. Commit with descriptive message
3. Update GraphRAG `agent_knowledge` with results
4. Report back to Kaitiaki Aronui or user

**Questions?** Query GraphRAG or reference audit report.

---

**Kia kaha! Go forth and fix the fallback!** 🚀

---

**Prepared by:** Kaitiaki Aronui V3.0  
**GraphRAG Knowledge:** agent_knowledge.id IN (772, 773, 774)  
**Status:** ✅ EXECUTION READY

