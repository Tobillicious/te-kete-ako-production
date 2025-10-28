# 🎨 TEMPLATE CREATION PLAN - October 28, 2025

## 🎯 GOAL
Create **3 perfected templates** for all teaching content types, then manually fix all 110 resources against these templates.

---

## 📋 TEMPLATE REQUIREMENTS

### 1️⃣ LESSON TEMPLATE (Perfect)
**File:** `templates/lesson-template-PERFECT.html`  
**Based on:** `units/lessons/unit-2-lesson-1.html` (gold standard)  
**Used for:** 35 existing lessons + future lessons

**Required Elements:**
```html
<div class="main-container">
  <!-- LEFT SIDEBAR -->
  <aside class="left-sidebar no-print">
    <!-- Whakataukī: Auto-injected by daily-whakatauki.js -->
    
    <div class="sidebar-widget">
      <h3 class="sidebar-widget-title">
        <span class="sidebar-icon">📚</span>
        <span>Unit [X] Navigation</span>
      </h3>
      <ul>
        <li><a href="../unit-X.html">← Unit Overview</a></li>
        <li><strong>Lesson [X]: [Current Lesson Name]</strong></li>
        <li><a href="unit-X-lesson-[next].html">Next Lesson →</a></li>
      </ul>
    </div>
  </aside>
  
  <!-- MAIN CONTENT -->
  <main class="content-area">
    <!-- All lesson content here -->
  </main>
</div>
```

**Additional Features:**
- Breadcrumbs: Unit Plans → Unit X → Lesson X
- Unit banner with lesson progression pills
- Save button (ready for auth)
- Print CSS (hides sidebar/header/footer)

---

### 2️⃣ HANDOUT WITH SIDEBAR TEMPLATE (Perfect)
**File:** `templates/handout-with-sidebar-template-PERFECT.html`  
**Based on:** Lessons structure, simplified for standalone handouts  
**Used for:** ~40 handouts (content-rich, meant for screen + print)

**Required Elements:**
```html
<div class="main-container">
  <!-- LEFT SIDEBAR -->
  <aside class="left-sidebar no-print">
    <!-- Whakataukī: Auto-injected by daily-whakatauki.js -->
    
    <div class="sidebar-widget">
      <h3 class="sidebar-widget-title">
        <span class="sidebar-icon">🌟</span>
        <span>Ngā Rauemi Hono / Related Resources</span>
      </h3>
      <ul>
        <li><a href="/handouts.html">📄 All Handouts</a></li>
        <li><a href="/unit-plans.html">📚 Unit Plans</a></li>
        <li><a href="/browse.html">🔍 Browse All</a></li>
      </ul>
    </div>
  </aside>
  
  <!-- MAIN CONTENT -->
  <main class="content-area">
    <!-- All handout content here -->
  </main>
</div>
```

**Key Differences from Lessons:**
- NO unit banner (handouts are standalone)
- NO lesson progression pills
- NO unit-specific navigation
- Simpler breadcrumbs: Handouts → [This Handout]
- Generic related resources links

**Additional Features:**
- Save button
- Print button (prominent)
- Print CSS (hides sidebar/header/footer, prints body only to A4)

---

### 3️⃣ HANDOUT SIMPLE A4 TEMPLATE (Already Exists)
**File:** `templates/handout-simple-a4-template.html`  
**Based on:** `handouts/probability-handout.html` (already correct)  
**Used for:** ~10 handouts (simple worksheets, no sidebar needed)

**Required Elements:**
```html
<!-- NO main-container -->
<!-- NO sidebar -->

<!-- Print Button (above content) -->
<div class="no-print">
  <button onclick="window.print()">Print or Save as PDF</button>
</div>

<!-- Simple A4 Page Container -->
<div class="page">
  <header>
    <h1>[Handout Title]</h1>
  </header>
  
  <!-- Worksheet content -->
  
</div>
```

**Key Features:**
- No sidebar (intentional)
- Clean A4 print layout
- Minimal chrome
- Already prints beautifully

**Status:** ✅ Already correct - just document as template

---

## 🔨 CREATION PROCESS

### Step 1: Create Lesson Template (30 min)
1. Read `units/lessons/unit-2-lesson-1.html` in full
2. Extract structure, remove specific content
3. Add clear comments for future use
4. Add placeholder text: `[REPLACE WITH...]`
5. Save as `templates/lesson-template-PERFECT.html`
6. Deploy to live site
7. Visual review in browser with user

### Step 2: Create Handout Sidebar Template (30 min)
1. Copy lesson template structure
2. Remove unit-specific elements (banner, progression, unit nav)
3. Simplify sidebar (generic related resources)
4. Simplify breadcrumbs
5. Add prominent print button
6. Save as `templates/handout-with-sidebar-template-PERFECT.html`
7. Deploy to live site
8. Visual review in browser with user

### Step 3: Document Simple A4 Template (10 min)
1. Copy `handouts/probability-handout.html` to templates
2. Strip specific content
3. Add comments
4. Save as `templates/handout-simple-a4-template.html`
5. Document when to use this vs sidebar template

---

## 📊 WHICH HANDOUTS USE WHICH TEMPLATE?

### Decision Criteria:

**Use Sidebar Template IF:**
- Content-rich (multiple sections, long text)
- Meant for screen reading first
- Benefits from related resources links
- Still needs to print nicely to A4

**Use Simple A4 Template IF:**
- Simple worksheet (fill-in-the-blank, calculations)
- Primarily meant for printing
- Minimal content (1-2 pages)
- No need for navigation/resources

### Handout Categorization (Manual Audit Needed):

| Handout | Template | Reason |
|---------|----------|--------|
| media-literacy-comprehension-handout.html | Sidebar | Content-rich, screen + print |
| probability-handout.html | Simple A4 | Math worksheet, print-focused |
| treaty-of-waitangi-handout.html | Sidebar | Historical content, screen + print |
| writers-toolkit-peel-argument-handout.html | Sidebar | Writing guide, screen + print |
| bar-graph-handout.html | Simple A4 | Math worksheet |
| ... | ... | ... |

**(Full audit needed for all 67 handouts)**

---

## ✅ SUCCESS CRITERIA

### Template is "Perfect" when:
1. ✅ Visual inspection looks professional
2. ✅ Whakataukī injects correctly
3. ✅ Sidebar is sticky and scrollable (600px max-height)
4. ✅ Print CSS works (prints body only to A4)
5. ✅ Save button in place (ready for auth)
6. ✅ No console errors
7. ✅ Responsive on mobile
8. ✅ User approves: "This is the gold standard"

---

## 🚀 NEXT IMMEDIATE ACTIONS

1. **Create lesson-template-PERFECT.html** from unit-2-lesson-1
2. **Deploy and browse it** at `https://tekete.co.nz/templates/lesson-template-PERFECT.html`
3. **Get user approval** - "Does this look right?"
4. **Create handout-with-sidebar-template-PERFECT.html**
5. **Deploy and browse it**
6. **Get user approval**
7. **Begin manual handout audit** against these standards

---

**Ready to create the first template now?** 🎯

