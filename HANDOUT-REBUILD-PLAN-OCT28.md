# 🔧 HANDOUT REBUILD PLAN - 24 FILES

**Date:** October 28, 2025  
**Goal:** Rebuild all 24 non-standard handouts to match site templates  
**Status:** 🚧 IN PROGRESS

---

## 📋 THE 24 HANDOUTS TO REBUILD

### GROUP A: Has main-container, needs sidebar (3 files) ⚡ EASIEST
1. ✅ ai-ethics-and-bias.html
2. ✅ authors-purpose-handout.html
3. ✅ environmental-literacy-framework.html

**Fix:** Add sidebar structure, ensure whakataukī script, verify buttons

---

### GROUP B: Has site header, no main-container (4 files) 🔨 MEDIUM
1. ⬜ arguments-of-tino-rangatiratanga-handout.html
2. ⬜ maori-astronomy-navigation-handout.html
3. ⬜ pre-colonial-innovation.html
4. ⬜ waitangi-tribunal-cases.html

**Fix:** Wrap content in main-container + sidebar + content-area structure

---

### GROUP C: Standalone .page structure (17 files) 🔥 HARDEST
**Writer's Toolkit Series (7 files):**
1. ⬜ writers-toolkit-conclusion-handout.html
2. ⬜ writers-toolkit-diction-handout.html
3. ⬜ writers-toolkit-hook-handout.html
4. ⬜ writers-toolkit-revision-handout.html
5. ⬜ writers-toolkit-rhetorical-devices-handout.html
6. ⬜ writers-toolkit-suspense-handout.html
7. ⬜ writers-toolkit-tone-handout.html

**Comprehension/Analysis (10 files):**
8. ⬜ ai-art-ethics-comprehension-handout.html
9. ⬜ authors-purpose-entertain-handout.html
10. ⬜ authors-purpose-inform-handout.html
11. ⬜ cognitive-biases-comprehension-handout.html
12. ⬜ design-thinking-process-handout.html
13. ⬜ elements-of-art-handout.html
14. ⬜ film-scene-analysis-handout.html
15. ⬜ plate-tectonics-comprehension-handout.html
16. ⬜ political-cartoon-analysis-handout.html
17. ⬜ shakespeare-soliloquy-handout.html

**Fix:** Complete rebuild - extract content, apply handout-with-sidebar-template-PERFECT.html

---

## 🎯 WHAT "CONSISTENT WITH SITE" MEANS

### Must-Have Structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Standard fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Merriweather:ital,wght@0,400;1,300&family=Montserrat:wght@700&display=swap" rel="stylesheet">
    <!-- Main CSS ONLY -->
    <link rel="stylesheet" href="../css/main.css">
    <!-- Print CSS inline -->
    <style>
        @media print {
            .question-block, .analysis-item, .activity-section, section > div {
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }
            h2, h3, h4 {
                page-break-after: avoid !important;
            }
        }
    </style>
</head>
<body data-auto-init="true" data-current-page="handout-page">
    <header class="site-header no-print">
        <!-- Standard site header -->
    </header>
    
    <!-- Save/Print Buttons -->
    <div class="no-print" style="background-color: var(--color-surface)...">
        <button data-save-resource ...>⭐ Save to My Kete</button>
        <button onclick="window.print()">🖨️ Print or Save as PDF</button>
    </div>
    
    <!-- Main Container -->
    <div class="main-container">
        <aside class="left-sidebar no-print">
            <!-- Whakataukī auto-injected -->
            <div class="sidebar-widget">
                <h3>Related Resources</h3>
                <ul>...</ul>
            </div>
        </aside>
        
        <main class="content-area">
            <!-- ALL HANDOUT CONTENT HERE -->
        </main>
    </div>
    
    <footer class="site-footer no-print">
        <!-- Standard site footer -->
    </footer>
    
    <script src="../js/daily-whakatauki.js"></script>
</body>
</html>
```

### Must NOT Have:
- ❌ Tailwind CDN (`<script src="https://cdn.tailwindcss.com"></script>`)
- ❌ Custom inline styles in `<style>` tags (except print CSS)
- ❌ Standalone `.page` divs (210mm width)
- ❌ Custom fonts different from site standard
- ❌ Nested `<main>` inside another `<main>`
- ❌ Hardcoded whakataukī (must be auto-injected)

### Must Have:
- ✅ `../css/main.css` link
- ✅ Standard Google Fonts (Lato, Merriweather, Montserrat)
- ✅ `<div class="main-container">`
- ✅ Single `<aside class="left-sidebar no-print">`
- ✅ `<main class="content-area">`
- ✅ Save button with `data-save-resource` attributes
- ✅ Print button with `onclick="window.print()"`
- ✅ `<script src="../js/daily-whakatauki.js"></script>`
- ✅ Print CSS for page breaks
- ✅ Standard site header & footer
- ✅ `data-auto-init="true"` on body

---

## 🔧 REBUILD PROCESS

### For Each Handout:
1. **Extract content** - Save the actual teaching content (text, questions, exercises)
2. **Copy template** - Use `handout-with-sidebar-template-PERFECT.html`
3. **Insert content** - Place extracted content into `<main class="content-area">`
4. **Update metadata** - Title, data-resource-url, data-resource-title
5. **Add related resources** - Update sidebar widget with relevant links
6. **Test print** - Verify page breaks don't bisect content
7. **Verify save button** - Check data attributes are correct
8. **Visual check** - Compare to fixed handouts for consistency

---

## ⏱️ TIME ESTIMATES

- **Group A (3 files):** 30 min (10 min each)
- **Group B (4 files):** 1 hour (15 min each)
- **Group C (17 files):** 3-4 hours (12-15 min each)

**Total:** ~5 hours for complete rebuild of all 24 handouts

---

## 🎯 SUCCESS CRITERIA

When complete, ALL handouts will:
- ✅ Have identical header/footer to lessons
- ✅ Have single left sidebar with whakataukī
- ✅ Use main.css consistently
- ✅ Print correctly to A4 (no bisected content)
- ✅ Have working save buttons
- ✅ Look professional and unified
- ✅ Be indistinguishable from the 34 we just fixed

---

## 📝 NOTES

- This is NOT just adding sidebars
- This is FULL structural rebuild for consistency
- User explicitly requested: "Do everything to make them consistent. not just sidebar."
- Goal: All 66 handouts should look like they came from the same template
- No more Tailwind, no more custom styles, no more standalone pages
- Everything follows the site standards now

---

**Let's rebuild Te Kete Ako to be consistent and professional! 🚀**

