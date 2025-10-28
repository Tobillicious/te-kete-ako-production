# 🔍 HANDOUT SIDEBAR AUDIT - October 28, 2025

## 📊 SUMMARY

**Total Handouts:** 67  
**With Double Sidebar Bug:** 34 (51%)  
**Correct Structure:** 33 (49%)

## ✅ CORRECT SIDEBAR STRUCTURE (Gold Standard)

**Example:** `units/lessons/unit-2-lesson-1.html`

```html
<div class="main-container">
  <aside class="left-sidebar no-print">
    <!-- Whakataukī: Auto-injected by daily-whakatauki.js -->
    
    <div class="sidebar-widget">
      <h3 class="sidebar-widget-title">
        <span class="sidebar-icon">📚</span>
        <span>Unit Navigation</span>
      </h3>
      <ul>
        <li><a href="../unit-overview.html">← Unit Overview</a></li>
        <li><strong>Current Page</strong></li>
        <li><a href="next-page.html">Next →</a></li>
      </ul>
    </div>
  </aside>
  
  <main class="content-area">
    <!-- ALL CONTENT HERE -->
    <section>...</section>
    <section>...</section>
  </main>
</div>
```

**Key Points:**
- ONE `<aside class="left-sidebar no-print">` 
- Whakataukī auto-injected by JavaScript
- Navigation/resources in sidebar-widget divs
- `<main class="content-area">` contains ALL content
- NO duplicate sidebars inside main

## ❌ DOUBLE SIDEBAR BUG (What's Wrong)

**Example:** `handouts/media-literacy-comprehension-handout.html`

```html
<div class="main-container">
  <aside class="left-sidebar no-print">  <!-- CORRECT -->
    <!-- Whakataukī auto-injected -->
    <div class="sidebar-widget">
      Related Resources
    </div>
  </aside>
  
  <main class="content-area">
    <aside class="left-sidebar no-print">  <!-- BUG! DUPLICATE INSIDE MAIN! -->
      <div class="sidebar-widget">
        More content...
      </div>
      <div class="sidebar-widget">
        Whakataukī (hardcoded) <!-- DUPLICATE! -->
      </div>
    </aside>
    
    <main class="content-area">  <!-- NESTED MAIN! -->
      <!-- Actual content buried here -->
    </main>
  </main>
</div>
```

**Problems:**
1. DUPLICATE `<aside class="left-sidebar">` INSIDE `<main>`
2. Often has hardcoded duplicate whakataukī
3. Content is nested too deep
4. Confusing structure for maintenance

## 📋 HANDOUTS WITH DOUBLE SIDEBAR BUG (34 files)

```
youth-vaping-comprehension-handout.html
writers-toolkit-show-dont-tell-handout.html
writers-toolkit-peel-argument-handout.html
writers-toolkit-inform-structure-handout.html
writers-toolkit-fluency-handout.html
writers-toolkit-analogy-handout.html
treaty-of-waitangi-handout.html
traditional-navigation-mathematics-handout.html
traditional-ecological-indicators-handout.html
sustainable-technology-design-challenge.html
statistical-investigation-handout.html
speech-analysis-handout.html
scientific-method-handout.html
science-of-sleep-comprehension-handout.html
misleading-graphs-comprehension-handout.html
microplastics-comprehension-handout.html
media-literacy-comprehension-handout.html
maori-geometric-patterns-handout.html
maori-battalion-legacy.html
land-wars-strategy.html
haka-comprehension-handout.html
gig-economy-comprehension-handout.html
figurative-language-handout.html
environmental-text-analysis-handout.html
digital-citizenship-handout.html
data-sovereignty-maori.html
colonisation-impact-handout.html
climate-crisis-generation-comprehension-handout.html
biodiversity-handout.html
ai-impact-comprehension-handout.html
ai-ethics-and-bias.html
ai-art-ethics-comprehension-handout.html
(+ 2 more)
```

## ✅ HANDOUTS WITH CORRECT STRUCTURE (33 files)

These either have:
- ONE sidebar (correct)
- NO sidebar (intentional, e.g., simple A4 print worksheets)

**Examples:**
- `probability-handout.html` - Simple A4, no sidebar (intentional)
- `introduction-to-llms.html` - Single sidebar (correct)
- `prompt-engineering-101.html` - Single sidebar (correct)
- `urban-maori-identity.html` - Single sidebar (correct)

## 🎯 FIX PLAN

### Phase 1: Perfect the Template (NOW)
1. Use `units/lessons/unit-2-lesson-1.html` as gold standard
2. Create perfected `handout-template.html`
3. Visual review with user

### Phase 2: Audit All Handouts
1. Categorize each of 67 handouts:
   - ✅ Correct (0-1 sidebar)
   - ❌ Double sidebar bug (2 sidebars)
   - 📄 Intentional no-sidebar (A4 print)

### Phase 3: Fix Double Sidebar Bugs (34 files)
For each file:
1. Remove SECOND `<aside class="left-sidebar">` inside `<main>`
2. Remove any hardcoded duplicate whakataukī
3. Ensure single `<main class="content-area">` with all content
4. Keep FIRST sidebar with proper structure

### Phase 4: Verify All
1. Test whakataukī injection works
2. Test sidebar sticky behavior
3. Visual review sample from each category

## 📝 NOTES

**From Sidebar Docs:**
- All 48 lessons already have CORRECT structure ✅
- Video activities have 3-column layout (left sidebar, main, right sidebar) ✅
- Handouts are MIXED - this audit identifies which need fixing

**GraphRAG Updated:**
- Sidebar specification added as agent doc
- Links to gold standard example
- Documents bug pattern for future agents

## 🚀 NEXT STEP

User wants to start by **perfecting the handout template** using the lesson as a guide, then fix all existing handouts against that perfected template.

**Question for user:** Want me to create the perfected handout template now based on `unit-2-lesson-1.html` structure?

