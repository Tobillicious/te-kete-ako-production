# 🔍 Cursor Audit: Why Deployed Site Looks Like Fallback

**Date:** October 25, 2025  
**Auditor:** Kaitiaki Aronui V3 (Fresh Eyes Beta Test)  
**For:** All LLMs (DeepSeek, GPT-4o-mini, Claude, etc.)  
**GraphRAG IDs:** 775, 776, 777

---

## 🎯 The Answer (TL;DR)

**Q: Why does the site look like a fallback?**

**A: Because it IS a fallback!**

1. **Component Loading Cascade** - Page loads empty for 2-3 seconds while 14 components fetch sequentially
2. **GraphRAG Features Blocked** - Best features redirect to homepage (users literally sent to fallback)
3. **Production Bloat** - 2,033 backup files, broken service worker, outdated manifest

---

## 🔴 ROOT CAUSE: Component Loading Cascade

### What Happens

```javascript
// Homepage loads like this:
1. HTML loads (empty divs)
2. fetch('/components/hero-unified.html')      // Wait...
3. fetch('/components/featured-carousel.html') // Wait...
4. fetch('/components/perfect-pathways-widget.html') // Wait...
... 11 more fetches ...
14. Page finally looks complete (2-3 seconds later)
```

### User Experience

```
Time 0s:   [Empty page with whakataukī banner]
Time 0.5s: [Hero appears]
Time 1.0s: [Featured content appears]
Time 1.5s: [Widgets pop in]
Time 2.0s: [Footer appears]
Time 2.5s: [Finally looks complete]
```

**This is THE "fallback" look everyone sees!**

### The Numbers

- **74** component files exist
- **2,635** fetch() calls across site
- **1,944** HTML files use component fetching
- **14** components on homepage alone

---

## 🚫 BLOCKED FEATURES (Critical!)

### In `public/_redirects` (Lines 8-16)

```
/graphrag-brain-hub.html / 302
/intelligence-hub.html / 302
/perfect-learning-pathways.html / 302
/cultural-excellence-network.html / 302
/discovery-tools.html / 302
/influence-hubs.html / 302
/graphrag-knowledge-graph-viz.html / 302
/graphrag-visual-graph.html / 302
```

**Impact:** Users trying to access best features get redirected to homepage!

**Fix:** Delete lines 8-16 from `public/_redirects`

---

## 📦 PRODUCTION BLOAT

### Backup Files Everywhere

```bash
$ find public -name "*.bak" | wc -l
2033
```

**2,033 backup files** deployed to production!

**Examples:**
- `students/dashboard.html.bak`
- `signup-teacher.html.bak`
- `lessons-complete.html.bak`
- ... 2,030 more

**Fix:** `find public -name "*.bak" -delete`

---

## 🐛 BROKEN PWA

### Service Worker Issues

**Caches files that don't exist:**
```javascript
// In service-worker.js
'/css/component-library.css',      // ❌ Doesn't exist
'/css/animations-professional.css', // ❌ Doesn't exist
'/css/mobile-optimization.css',     // ❌ Doesn't exist
```

**Result:** Offline mode broken, console errors

### Manifest Outdated

```json
// manifest.json says:
"Browse all 604 lessons"

// Reality:
5,765+ lessons in GraphRAG
```

---

## 🔇 CONSOLE ERROR POLLUTION

**353 console.error/warn calls across 217 files**

```javascript
// Every page shows:
[Hero Component] Load error: ...
[Featured Component] Load error: ...
PWA: Service Worker registration failed: ...
❌ Supabase CDN failed to load!
```

**Impact:** Looks broken to technical users, unprofessional

---

## 📊 MISSING SEO

**No social sharing tags on any page:**

```html
<!-- Missing everywhere: -->
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
<meta name="twitter:card" content="...">
<link rel="canonical" href="...">
```

**Result:** Broken social media previews, poor discoverability

---

## ⚡ PERFORMANCE ISSUES

### Large Files

**10 HTML files over 100KB:**
- `handouts-complete.html`
- `index.html`
- `lessons-complete.html`
- `mathematics-hub.html`
- ... 6 more

### Directory Sizes

- CSS: **1.1M**
- JS: **2.0M**
- Components: **1.5M**

### Load Pattern

- 30+ HTTP requests on page load
- No lazy loading
- Sequential component fetches
- Animated counters on mobile (battery drain)

---

## 🚀 FIXES (Prioritized for ANY LLM)

### Priority 1: Unblock Features (5 min) ⚡

**File:** `public/_redirects`  
**Action:** Delete lines 8-16  
**Impact:** Unlock Brain, Intelligence Hub, Perfect Pathways  
**Difficulty:** Trivial

```bash
# Before (lines 8-16):
/graphrag-brain-hub.html / 302
/intelligence-hub.html / 302
...

# After:
# (delete those lines)
```

---

### Priority 2: Remove Backup Files (1 min) ⚡

**Command:**
```bash
find public -name "*.bak" -delete
```

**Impact:** Remove 2,033 files, cleaner production  
**Difficulty:** Trivial

---

### Priority 3: Fix Component Loading (2-4 hours) 🔧

**Problem:** 14 sequential fetches = 2-3 second delay

**Solution Options:**

**A. Bundle Components (Recommended)**
```javascript
// Create components-bundle.json with all components
// Single fetch instead of 14
fetch('/components-bundle.json')
  .then(r => r.json())
  .then(components => {
    // Load all at once
  });
```

**B. Inline Critical Components**
```html
<!-- Don't fetch, just include directly -->
<div class="hero">
  <!-- Hero content here -->
</div>
```

**C. Build Step (Best Long-term)**
```bash
# Pre-render components during build
npm run build  # Inlines all components
```

**Difficulty:** Medium  
**Impact:** Eliminate empty page delay

---

### Priority 4: Update Manifest (5 min) ⚡

**File:** `public/manifest.json`

**Changes:**
```json
{
  "description": "... 5,765+ teaching resources ...",
  "shortcuts": [
    {
      "name": "Browse Lessons",
      "description": "Browse all 5,765 lessons"  // Was 604
    }
  ]
}
```

**Difficulty:** Trivial

---

### Priority 5: Add SEO Tags (1-2 hours) 🔧

**Add to ALL pages:**

```html
<!-- Open Graph -->
<meta property="og:title" content="[Page Title] | Te Kete Ako">
<meta property="og:description" content="[Page Description]">
<meta property="og:image" content="https://tekete.netlify.app/images/og-image.jpg">
<meta property="og:url" content="https://tekete.netlify.app/[page-path]">
<meta property="og:type" content="website">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Page Title]">
<meta name="twitter:description" content="[Page Description]">
<meta name="twitter:image" content="https://tekete.netlify.app/images/twitter-card.jpg">

<!-- Canonical URL -->
<link rel="canonical" href="https://tekete.netlify.app/[page-path]">
```

**Difficulty:** Easy (repetitive)  
**Best for:** DeepSeek, GPT-4o-mini

---

### Priority 6: Clean Console Errors (1 hour) 🔧

**Replace all:**
```javascript
// OLD (353 instances):
.catch(err => console.error('[Component] Load error:', err));

// NEW:
.catch(err => {
  // Log to monitoring (PostHog, Sentry)
  if (window.posthog) {
    posthog.capture('component_error', { error: err.message });
  }
  // Show user-friendly fallback
  // Don't spam console in production
});
```

**Difficulty:** Easy (find/replace)

---

## ✅ Testing Checklist

After fixes, verify:

- [ ] Homepage loads without 2-3 second empty state
- [ ] GraphRAG Brain accessible at `/graphrag-brain-hub.html`
- [ ] Intelligence Hub accessible at `/intelligence-hub.html`
- [ ] Perfect Pathways accessible at `/perfect-learning-pathways.html`
- [ ] No console errors on page load
- [ ] Social sharing preview works (test on Twitter/Facebook)
- [ ] PWA installs correctly
- [ ] Offline mode works
- [ ] No .bak files in production
- [ ] Manifest shows correct lesson count

---

## 📊 Success Metrics

### Before (Current)
- Time to content: 2-3 seconds
- Console errors: 5-10 per page
- Backup files: 2,033
- GraphRAG features: Blocked
- Social sharing: Broken
- PWA offline: Broken

### After (Target)
- Time to content: <0.5 seconds
- Console errors: 0
- Backup files: 0
- GraphRAG features: Accessible
- Social sharing: Working
- PWA offline: Working

---

## 💰 Cost Estimate

### By Model

| Task | DeepSeek | GPT-4o-mini | Claude Sonnet |
|------|----------|-------------|---------------|
| Unblock features | $0.01 | $0.02 | $0.50 |
| Remove backups | $0.01 | $0.02 | $0.50 |
| Update manifest | $0.05 | $0.10 | $1.00 |
| Add SEO tags | $1.00 | $2.00 | $20.00 |
| Clean console | $0.50 | $1.00 | $10.00 |
| Bundle components | $2.00 | $3.00 | $30.00 |
| **TOTAL** | **$3.57** | **$6.14** | **$62.00** |

**Recommendation:** Use DeepSeek for P1-P5, reserve Claude for strategy only

---

## 🤖 LLM-Specific Notes

### For DeepSeek
- Perfect for: P1, P2, P4, P5 (find/replace, batch edits)
- Use simple commands, clear file paths
- Test each change before moving to next

### For GPT-4o-mini
- Perfect for: P3, P6 (logic, bundling)
- Can handle component bundling
- Good at pattern recognition for SEO tags

### For Claude Sonnet
- Reserve for: Strategic decisions, complex refactoring
- Don't waste on trivial find/replace
- Use for architecture decisions only

---

## 📚 Reference Documents

1. **PROFESSIONALIZATION-ROADMAP-OCT25.md** - 7-phase roadmap
2. **FRESH-EYES-AUDIT-CONTINUED-OCT25.md** - Detailed findings
3. **HANDOFF-TO-EXECUTION-AGENTS.md** - Execution specs

### GraphRAG Queries

```sql
-- Get all audit findings
SELECT * FROM agent_knowledge 
WHERE id IN (775, 776, 777)
ORDER BY created_at DESC;

-- Get professionalization roadmap
SELECT * FROM agent_knowledge 
WHERE source_name = 'oct25_comprehensive_beta_test';
```

---

## 🌿 Cultural Note

**All fixes are purely technical - no cultural content affected.**

Maintain:
- ✅ Whakataukī placement and prominence
- ✅ Māori language integration
- ✅ Cultural authenticity
- ✅ Te Ao Māori perspectives

---

## 🎯 Quick Start (For Any LLM)

```bash
# 1. Unblock features (5 min)
nano public/_redirects  # Delete lines 8-16

# 2. Remove backups (1 min)
find public -name "*.bak" -delete

# 3. Update manifest (5 min)
nano public/manifest.json  # Change 604 to 5765

# 4. Test
open http://localhost:8000/graphrag-brain-hub.html
# Should work now (not redirect)!

# 5. Deploy
git add -A
git commit -m "fix: unblock GraphRAG features and clean production"
git push
```

**Total time for quick wins: 11 minutes**  
**Impact: Massive improvement in user experience**

---

**Prepared by:** Kaitiaki Aronui V3  
**Audit Method:** Fresh eyes, actual user testing  
**Status:** ✅ Ready for execution by any LLM  
**GraphRAG:** IDs 775, 776, 777

**Kia kaha! Let's make it professional!** 🚀

