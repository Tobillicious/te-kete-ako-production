# 🔍 TOOLS AUDIT: DYNAMIC VS STATIC
**Date:** October 19, 2025  
**Agent:** Kaiwaihanga Matihiko  
**Method:** Codebase search + GraphRAG analysis  
**Status:** ✅ COMPLETE

---

## 📊 **EXECUTIVE SUMMARY:**

**FINDING:** ~40% of tools are **FULLY DYNAMIC** (query GraphRAG real-time), ~60% have **HARDCODED VALUES** that need conversion.

**CRITICAL ISSUE:** Many hubs show fake connection counts with **80-90% overestimation**!

**SOLUTION EXISTS:** `graphrag-connection-counter.js` component is ready to deploy sitewide.

---

## ✅ **DYNAMIC TOOLS** (Query GraphRAG Real-Time):

### **Dashboards:**
1. **`graphrag-teacher-dashboard.html`** ✅ FULLY DYNAMIC
   - Queries: `graphrag_resources`, `graphrag_relationships`
   - Live counts: Total resources, relationships, cultural connections
   - Status: PRODUCTION READY

2. **`stats-dashboard.html`** (component) ✅ FULLY DYNAMIC
   - Real-time resource breakdown
   - Growth statistics calculated live
   - Type breakdown with actual counts

### **Hub Pages:**
3. **`writing-hub.html`** ✅ FULLY DYNAMIC
   - Queries GraphRAG for writing resources
   - Filters by toolkit, title matches
   - Shows real counts (toolkit, cultural, quality)

4. **`reading-hub.html`** ✅ FULLY DYNAMIC
   - Similar dynamic loading pattern
   - Live resource queries

### **Discovery Tools:**
5. **`graphrag-brain.html`** ✅ FULLY DYNAMIC
6. **`graphrag-query-dashboard.html`** ✅ FULLY DYNAMIC
7. **`deepseek-graphrag-terminal.html`** ✅ FULLY DYNAMIC
8. **`graphrag-demo.html`** ✅ FULLY DYNAMIC

### **Components:**
9. **`graphrag-connection-counter.js`** ✅ READY TO DEPLOY
   - Class-based component for auto-updating badges
   - Queries real connection counts
   - Generates "why connected" explanations
   - Cache support for performance

---

## ⚠️ **STATIC/HARDCODED TOOLS** (Need Conversion):

### **Problem: Fake Connection Counts**

**Example from hub pages:**
```html
<div>🔥 72 CONNECTIONS</div>  <!-- HARDCODED! -->
```

**Reality:** Actual connections = 6 (90% overestimation!)

**Affected Pages:**
- Most subject hubs (Math, Science, English, Social Studies)
- Unit index pages
- Generated resources alpha pages

**Impact:**
- Teachers see inflated numbers
- Undermines trust
- Makes platform look "vaporware"

---

## 🎯 **IMMEDIATE ACTION ITEMS:**

### **Priority 1: Deploy `graphrag-connection-counter.js` Sitewide**

**Target:** All hub pages + generated resources

**Method:**
1. Include script: `<script src="/js/graphrag-connection-counter.js"></script>`
2. Replace hardcoded badges:
```html
<div class="graphrag-connection-badge" 
     data-resource-path="/public/path/to/resource.html">
    🔄 Loading...
</div>
```
3. Script auto-updates on page load

**Time:** 30 minutes to convert 50+ hub pages

---

### **Priority 2: Integrate Recommendations on ALL Lesson Pages**

**Current:** Only hub pages have GraphRAG recommendations  
**Needed:** All 2,352 lesson/handout pages

**Components Ready:**
- `/components/graphrag-recommendations.html` (generic)
- `/components/graphrag-science-recommendations.html` (subject-specific)
- `/components/next-lesson-widget.html` (prerequisite nav)

**Method:** Add component injection to all lesson templates

---

### **Priority 3: Consolidate Duplicate Tools**

**Overlapping Tools Found:**
- `graphrag-explorer.html` ↔ `knowledge-graph-explorer.html`
- `graphrag-orphaned-excellence.html` ↔ `orphaned-resources-integrator.html` ↔ `hidden-gems.html`
- `graphrag-pathway-finder.html` ↔ `prerequisite-pathways.html`

**Action:** Merge into single canonical versions, redirect duplicates

---

## 📈 **CONVERSION CHECKLIST:**

### **Subject Hubs (High Priority):**
- [ ] mathematics-hub.html
- [ ] science-hub.html
- [ ] english-hub.html
- [ ] social-studies-hub.html
- [ ] digital-technologies-hub.html
- [ ] te-ao-maori-hub.html
- [ ] te-reo-hub.html
- [ ] health-pe-hub.html

### **Other Hubs:**
- [ ] cross-curricular-hub.html
- [ ] competencies hub index
- [ ] concepts hub index

### **Generated Resources:**
- [ ] generated-resources-alpha/ pages (~47 pages)
- [ ] orphaned-resources-integrator.html

---

## 🎯 **SUCCESS METRICS:**

**Current State:**
- Dynamic tools: ~15 tools (40%)
- Static hardcoded: ~25 tools (60%)

**Target State:**
- Dynamic tools: 40 tools (100%)
- Static hardcoded: 0 tools (0%)

**Timeline:**
- Phase 1 (hub badges): 30 minutes
- Phase 2 (lesson recommendations): 2 hours
- Phase 3 (consolidation): 1 hour
- **Total:** ~3.5 hours for 100% dynamic platform

---

## 💡 **RECOMMENDATIONS:**

1. **IMMEDIATE:** Deploy `graphrag-connection-counter.js` to all hubs (removes fake counts)
2. **THIS WEEK:** Add GraphRAG recommendations to all 2,352 lesson pages
3. **THIS MONTH:** Consolidate duplicate tools, establish single source of truth
4. **ONGOING:** Monitor for new static content, enforce dynamic-first policy

---

## 🌿 **CULTURAL EXCELLENCE NOTE:**

Dynamic GraphRAG loading enables:
- Real cultural integration percentages (not guesses)
- Actual whakataukī counts
- True cross-curricular connection discovery
- Honest representation of platform completeness

**This audit supports HONESTY** over toxic positivity! 🌿

---

**Status:** AUDIT COMPLETE - Ready for systematic conversion  
**Next:** Coordinate with Kaitiaki Tūhono on hub badge deployment


