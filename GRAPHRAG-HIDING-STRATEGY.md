# 🎯 GraphRAG Hiding Strategy - Surgical Fix

**Problem:** Homepage (index.html) shows GraphRAG visualizer sections to END USERS
**Goal:** Hide AI/dev tools while keeping educational content visible
**Constraint:** GraphRAG must still access pages for indexing

---

## 🔍 **WHAT I FOUND IN INDEX.HTML**

From grep analysis, these sections mention GraphRAG:

### **Line 153-157: Discovery Tools Callout**
```html
<!-- Quick Callouts: Generated Resources + Discovery Tools -->
<span>16 Discovery Tools (Q97!)</span>
```
**STATUS:** ❌ HIDE - This is AI tooling

### **Line 248: Cultural Excellence Network Button**
```html
<a href="/cultural-excellence-network.html" ...>
```
**STATUS:** ❌ HIDE - AI visualizer page

### **Line 772-785: DISCOVERY TOOLS SECTION** (Already has comment "HIDDEN FOR END USERS")
```html
<!-- 🔍 DISCOVERY TOOLS SECTION - GraphRAG Intelligence (HIDDEN FOR END USERS) -->
<section style="display: none; ...">
    Discovery Tools
    <a href="/discovery-tools.html">View All Discovery Tools →</a>
</section>
```
**STATUS:** ✅ ALREADY HIDDEN with `display: none;`

### **Line 948: GraphRAG Orphaned Excellence Component**
```html
fetch('/components/graphrag-orphaned-excellence.html')
```
**STATUS:** ❌ HIDE - Loading AI component

### **Line 1113, 1138: GraphRAG Stats in Teaching Library**
```html
10,117 gold-quality resources! GraphRAG-powered discovery with 231,237 connections.
...
GraphRAG Connections
```
**STATUS:** ⚠️ KEEP but change wording - Just say "AI-powered" not "GraphRAG"

### **Line 1435-1441: GRAPHRAG PLATFORM CHAMPIONS** (Already has comment "HIDDEN FOR END USERS")
```html
<!-- 🧠 GRAPHRAG PLATFORM CHAMPIONS - Most Connected Resources (HIDDEN FOR END USERS) -->
<section style="display: none; ...">
    🧠 GRAPHRAG INTELLIGENCE
</section>
```
**STATUS:** ✅ ALREADY HIDDEN with `display: none;`

### **Line 2146: GraphRAG Search Link**
```html
<a href="/graphrag-search.html" ...>
```
**STATUS:** ❌ HIDE - AI search tool

---

## ✅ **SURGICAL FIX PLAN**

### **Strategy: Hide by ID/Class, Not Broad CSS**

Instead of hiding ALL `a[href*="graphrag"]`, hide SPECIFIC sections:

```css
/* Hide specific GraphRAG sections on homepage */
#discovery-tools-callout,
#cultural-excellence-cta,
#graphrag-orphaned-section,
#graphrag-platform-champions,
a[href*="cultural-excellence-network"],
a[href*="/graphrag-search.html"],
a[href*="/discovery-tools.html"],
script[src*="graphrag-orphaned-excellence"] {
    display: none !important;
}
```

### **HTML Changes Needed:**

1. **Line 248** - Hide Cultural Excellence Network button
2. **Line 948** - Comment out graphrag-orphaned-excellence fetch
3. **Line 1113** - Change "GraphRAG-powered" to "AI-powered"
4. **Line 1138** - Change "GraphRAG Connections" to "AI Connections"
5. **Line 2146** - Hide graphrag-search.html link

---

## 🎯 **WHY THIS WORKS**

**CSS hiding alone won't work because:**
- Inline `<section style="display: none;">` can be overridden
- JavaScript might re-show hidden elements
- Users can inspect and unhide CSS

**Better approach:**
1. **Remove/comment out the HTML** that loads AI components
2. **Change text** from "GraphRAG" to "AI" (less technical)
3. **Keep CSS as backup** for any links that slip through

---

## 📋 **IMPLEMENTATION STEPS**

1. ✅ Edit index.html - remove GraphRAG component loads
2. ✅ Change "GraphRAG" text to "AI-powered" (user-friendly)
3. ✅ Keep CSS hiding rules as safety net
4. ✅ Test: Users should only see lessons, games, subject hubs

---

**This is a SURGICAL fix, not nuclear option. GraphRAG pages still exist and are accessible via direct URL (for agents), but users won't see links to them.**

