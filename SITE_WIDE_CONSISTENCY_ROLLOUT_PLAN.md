# 🎯 SITE-WIDE CONSISTENCY ROLLOUT PLAN

**Created:** October 19, 2025  
**For:** All agents working on Te Kete Ako  
**Goal:** Professional, consistent experience across ALL 1,585 pages

---

## **📊 CURRENT STATE (Verified via MCP GraphRAG queries):**

```
Total HTML pages: 1,585
✅ Pages with professional CSS: 1,721 (108% - some have multiple)
⚠️ Pages with navigation: 784 (49%)
⚠️ Pages with footer: 235 (15%)
```

**GAP:** 801 pages need navigation, 1,350 pages need footer

---

## **🎯 THE STANDARD: What Every Page Must Have**

### **Required Components (in order):**

```html
1. <div id="nav-container"></div>
   <script>
     fetch('/components/navigation-standard.html')
       .then(r => r.text())
       .then(html => document.getElementById('nav-container').innerHTML = html);
   </script>

2. [PAGE CONTENT HERE]

3. <div id="footer-container"></div>
   <script>
     fetch('/components/footer.html')
       .then(r=>r.text())
       .then(html=>document.getElementById('footer-container').innerHTML=html);
   </script>

4. <div id="mobile-nav-bottom"></div>
   <script>
     fetch('/components/mobile-bottom-nav.html')
       .then(r=>r.text())
       .then(html=>document.getElementById('mobile-nav-bottom').innerHTML=html);
   </script>

5. <div id="fab-quick-actions"></div>
   <script>
     fetch('/components/quick-actions-fab.html')
       .then(r=>r.text())
       .then(html=>document.getElementById('fab-quick-actions').innerHTML=html);
   </script>
```

---

## **✅ VERIFIED WORKING COMPONENTS:**

All these files EXIST and are production-ready:

- ✅ `/public/components/navigation-standard.html` (1,098 lines)
- ✅ `/public/components/footer.html` (exists)
- ✅ `/public/components/mobile-bottom-nav.html` (exists)
- ✅ `/public/components/quick-actions-fab.html` (exists)

---

## **📋 PRIORITY CATEGORIES:**

### **Category A: Hub Pages (CRITICAL - High Traffic)**
**Status:** ✅ COMPLETE (all major hubs now have nav/footer)

- ✅ index.html
- ✅ science-hub.html
- ✅ english-hub.html
- ✅ mathematics-hub.html
- ✅ social-studies-hub.html (NEW!)
- ✅ digital-technologies-hub.html (NEW!)
- ✅ te-reo-maori-hub.html (NEW!)
- ✅ te-ao-maori-hub.html

---

### **Category B: Complete Learning Units (HIGH PRIORITY)**
**Impact:** Teachers need complete units for planning

**Target directories:**
- `/public/units/y8-digital-kaitiakitanga/lessons/` (18 lessons)
- `/public/units/y7-maths-algebra/lessons/` 
- `/public/units/y9-science-ecology/lessons/`
- `/public/units/walker-unit/lessons/`
- `/public/units/y7-foundational-reading/`
- All other `/public/units/*/lessons/` directories

**Estimated:** ~250 lesson pages

---

### **Category C: Generated Excellence Resources (MEDIUM PRIORITY)**
**Impact:** These are high-quality (90+) but in orphaned directory

**Target:** `/public/generated-resources-alpha/`
- 47 handouts
- 30+ lessons
- All quality 90+

**Estimated:** ~80 pages

---

### **Category D: Standalone Lessons & Handouts (MEDIUM PRIORITY)**
**Target:** 
- `/public/lessons/` (not in units)
- `/public/handouts/` (not in units)
- `/public/integrated-lessons/`

**Estimated:** ~400 pages

---

### **Category E: Tools & Interactive Pages (LOW PRIORITY)**
**These already have custom navigation, just need footer**

**Target:**
- GraphRAG tools (discovery, search, etc.)
- Games
- Interactive widgets

**Estimated:** ~70 pages

---

## **🚀 RECOMMENDED EXECUTION APPROACH:**

### **Option 1: Manual (Agent-Intensive)**
- Each agent takes 50 pages
- Copy/paste standard snippets
- Slow but thorough
- **Time:** ~20 hours total (split across agents)

### **Option 2: Script-Based (Fast but Risky)**
- Python script to inject components
- Match `</body>` tag and insert before it
- Test on 10 pages first
- **Time:** ~2 hours (1 agent)
- **Risk:** Could break pages with unusual structure

### **Option 3: Hybrid (RECOMMENDED)**
- Start with Category B (complete units) - manual
- Test with 5 lessons
- If pattern is consistent, automate Category C & D
- **Time:** ~5 hours (2-3 agents)

---

## **🧩 THE INJECTION PATTERN:**

### **For pages that have BODY but no nav:**

```html
<body>
  <!-- ADD THIS AT TOP -->
  <div id="nav-container"></div>
  <script>
    fetch('/components/navigation-standard.html')
      .then(r => r.text())
      .then(html => document.getElementById('nav-container').innerHTML = html);
  </script>
  
  [EXISTING CONTENT]
  
  <!-- ADD THIS AT BOTTOM, BEFORE </body> -->
  <div id="footer-container"></div>
  <script>
    fetch('/components/footer.html').then(r=>r.text()).then(html=>{
      document.getElementById('footer-container').innerHTML=html;
    });
  </script>
  
  <div id="mobile-nav-bottom"></div>
  <script>
    fetch('/components/mobile-bottom-nav.html').then(r=>r.text()).then(html=>{
      document.getElementById('mobile-nav-bottom').innerHTML=html;
    });
  </script>
  
  <div id="fab-quick-actions"></div>
  <script>
    fetch('/components/quick-actions-fab.html').then(r=>r.text()).then(html=>{
      document.getElementById('fab-quick-actions').innerHTML=html;
    });
  </script>
</body>
```

---

## **⚠️ EDGE CASES TO HANDLE:**

1. **Pages that already have OLD navigation** (not navigation-standard.html)
   - Replace old nav with standard
   
2. **Pages with custom styling** (tools, games)
   - Keep custom styling, just add footer
   
3. **Component pages** (navigation-standard.html itself!)
   - Don't add nav to nav! Skip these.
   
4. **Error pages** (404.html)
   - May need custom nav (no dropdowns on error page)

---

## **📈 SUCCESS METRICS:**

**When complete:**
- ✅ 100% of hub pages have nav + footer
- ✅ 100% of lesson pages have nav + footer
- ✅ 95%+ of all pages have consistent navigation
- ✅ Every page can reach Help, About, Contact
- ✅ Every page has Login/Signup access
- ✅ Mobile users have bottom nav on all pages

---

## **🧠 GRAPHRAG-POWERED NAVIGATION STRATEGY:**

### **Traditional Breadcrumbs REPLACED by GraphRAG:**

Instead of static:
```
Home > Science > Y9 > Lesson 1
```

We use dynamic GraphRAG:
- **Similar Resources** sidebar (5-10 related lessons)
- **Prerequisite Chain** links (what comes before/after)
- **Cross-Subject Connections** (Math in Science lesson)
- **Hidden Gems** recommendations

### **Why GraphRAG is Better:**

1. **Dynamic:** Updates as knowledge graph grows
2. **Intelligent:** Finds non-obvious connections
3. **Cultural:** Highlights shared cultural elements
4. **Personalized:** Based on user's journey

### **When to Use Traditional Breadcrumbs:**

- SEO (search engines expect them)
- Quick vertical navigation (back to hub)
- User orientation ("where am I?")

**VERDICT:** Use BOTH! Breadcrumbs for hierarchy, GraphRAG for discovery

---

## **🔧 COMPONENTS TO USE:**

### **Navigation Components:**
- `/components/navigation-standard.html` - Main nav (USE EVERYWHERE)
- `/components/mobile-bottom-nav.html` - Mobile UX
- `/components/quick-actions-fab.html` - Floating help button

### **Discovery Components:**
- `/components/graphrag-recommendations.html` - Similar resources widget
- `/components/related-resources-widget.html` - Related content
- `/components/graphrag-semantic-search.html` - Semantic search

### **Footer Components:**
- `/components/footer.html` - Standard footer (About, Contact, Help, Legal)

---

## **💡 QUICK START FOR AGENTS:**

### **To add nav/footer to ONE lesson page:**

1. Open the lesson file
2. After `<body>` tag, add nav container + script
3. Before `</body>` tag, add footer + mobile nav + fab
4. Test: Load page, check nav dropdown works, footer links work
5. Move to next page

### **To batch process 50 pages:**

Use search_replace tool with pattern matching, or create a Python script (but test on 5 pages first!)

---

## **📊 TRACKING PROGRESS:**

**Update agent_knowledge after each batch:**

```sql
INSERT INTO agent_knowledge (
  source_name,
  key_insights,
  technical_details
) VALUES (
  'Navigation Rollout Batch 1',
  ARRAY['Added nav/footer to 50 Y8 Digital Kaitiakitanga lessons'],
  jsonb_build_object('pages_updated', 50, 'directory', '/units/y8-digital-kaitiakitanga/')
);
```

---

## **⚡ ESTIMATED TIMELINE:**

- **Category B (250 unit lessons):** 5 hours (2 agents)
- **Category C (80 generated resources):** 2 hours (1 agent)
- **Category D (400 standalone):** 8 hours (3 agents)
- **Category E (70 tools):** 2 hours (1 agent)

**TOTAL:** ~17 hours across 3-4 agents = **~1 day of work**

**After completion:** Site will feel 100% professional and consistent! 🎯

---

**Kia kaha! (Be strong!) Let's make this happen!** 🚀

