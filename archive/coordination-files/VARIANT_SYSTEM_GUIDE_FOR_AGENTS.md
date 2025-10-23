# 🚀 Teaching Variants System: Agent Quick Start Guide

**Created:** October 22, 2025  
**Status:** Production-Ready  
**For:** AI Agents working on Te Kete Ako

---

## 📋 TL;DR - What Is This?

The **Teaching Variants System** surfaces 16,656+ teaching resources from GraphRAG through intelligent, user-friendly components. It respects the philosophy: **"Duplicates aren't bugs - they're pedagogical options."**

### 🎯 Core Components

1. **All Teaching Variants Browser** (`/public/all-teaching-variants-browser.html`)
2. **Mega-Navigation Component** (`/public/components/mega-navigation-intelligent.html`)
3. **Variant Selector Cards** (inline unit page components)
4. **Auto-Generator JS** (`/public/js/teaching-variants-auto-generator.js`)

---

## 🛠️ How to Use Each Component

### 1️⃣ All Teaching Variants Browser

**File:** `/public/all-teaching-variants-browser.html`  
**Purpose:** Full-page searchable catalog of all teaching variants  
**Features:** 7 intelligent filters (location, subject, type, quality, cultural, year, search)

#### How to Link to It:

```html
<!-- Link to browser with pre-applied filter -->
<a href="/all-teaching-variants-browser.html?subject=Mathematics&quality=90">
    Browse Excellence Mathematics Variants →
</a>

<!-- Available URL parameters: -->
<!-- ?subject=Mathematics -->
<!-- ?location=css_backup -->
<!-- ?quality=90 -->
<!-- ?cultural=dual -->
<!-- ?year=Year 8 -->
<!-- ?type=Lesson -->
```

#### When to Use:
- Creating subject hub "Browse Variants" sections
- Linking from unit pages to show all related variants
- Creating curated collections (e.g., "Q90+ Cultural Resources")

---

### 2️⃣ Mega-Navigation Component

**File:** `/public/components/mega-navigation-intelligent.html`  
**Purpose:** Floating slide-out panel with GraphRAG-powered navigation  
**Status:** Already integrated into `index.html` (loads globally)

#### How It Works:
- Floating 📚 button appears in bottom-right
- Clicking opens slide-out panel with Units/Lessons/Variants
- Real-time GraphRAG counts and search
- Escape key to close

#### Already Active:
This component is already loaded on all pages via:
```javascript
fetch('/components/mega-navigation-intelligent.html')
    .then(r => r.text())
    .then(html => { /* inject into page */ });
```

**You don't need to do anything!** It just works.

---

### 3️⃣ Variant Selector Cards (Inline Unit Pages)

**Purpose:** Show 2-3 pedagogical options per lesson within a unit index page  
**Examples:** `/public/units/y7-maths-algebra/index-with-variants.html`, `/public/units/y8-digital-kaitiakitanga/index-with-variants.html`

#### HTML Structure:

```html
<div style="background: white; padding: 2rem; border-radius: 16px; margin-bottom: 2rem;">
    <!-- Lesson Header -->
    <div style="border-bottom: 3px solid #0284c7; padding-bottom: 1rem; margin-bottom: 2rem;">
        <h3>📘 Lesson 1: Introduction to Algebra</h3>
        <p>Variables, expressions, and patterns | 27 teaching variants available</p>
    </div>

    <!-- Variant Cards Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
        
        <!-- Card 1: Recommended Version -->
        <div style="background: linear-gradient(135deg, #10b981, #059669); padding: 1.5rem; border-radius: 12px;">
            <div style="position: absolute; top: -10px; right: -10px; background: #fbbf24; ...">
                ⭐ RECOMMENDED
            </div>
            <h4 style="color: white;">Enhanced Gold Standard</h4>
            <div style="background: rgba(255,255,255,0.2); padding: 0.75rem; border-radius: 8px;">
                <p style="color: white;">
                    ✅ Latest pedagogy<br>
                    ✅ High cultural integration<br>
                    ✅ NZ curriculum aligned
                </p>
            </div>
            <a href="/path/to/lesson.html" style="...">Use This Version →</a>
        </div>

        <!-- Card 2: Alternative Version -->
        <div style="background: white; border: 2px solid #e0e0e0; padding: 1.5rem; border-radius: 12px;">
            <h4 style="color: #546e7a;">Legacy CSS Variant</h4>
            <div style="background: #f5f5f5; padding: 0.75rem; border-radius: 8px;">
                <p style="color: #546e7a;">
                    📝 Original design<br>
                    📝 Print-friendly<br>
                    📝 Lighter weight
                </p>
            </div>
            <a href="/path/to/legacy-lesson.html" style="...">Use This Version →</a>
        </div>

        <!-- Card 3 (optional): 3rd variant -->
        
    </div>

    <!-- Explanation Dropdown -->
    <details style="margin-top: 1rem; ...">
        <summary>ℹ️ Why 2 options? (Synthesized from 27 variants)</summary>
        <div>
            <p>GraphRAG contains 27 versions of this lesson. We've curated the 2 most pedagogically distinct...</p>
        </div>
    </details>
</div>
```

#### Key Design Principles:
1. **Recommended version** = green gradient + gold star badge
2. **Alternative versions** = neutral colors (gray, purple, etc.)
3. **Distinct blurbs** = explain HOW each variant differs (not just "different")
4. **"Best for:"** line = helps teachers choose
5. **Explanation dropdown** = transparency about variant synthesis

---

### 4️⃣ Auto-Generator JS (Advanced)

**File:** `/public/js/teaching-variants-auto-generator.js`  
**Purpose:** Automatically generate variant cards by querying GraphRAG  
**Status:** Written but not yet deployed to production units

#### How to Use:

**Step 1:** Include the script on your unit page:
```html
<script src="/js/teaching-variants-auto-generator.js"></script>
```

**Step 2:** Add a container with `data-unit-path`:
```html
<div id="variants-auto-container" data-unit-path="/units/y9-science-ecology/"></div>
```

**Step 3:** The JS will:
1. Query GraphRAG for all lessons in that unit path
2. Group variants by filename
3. Select top 2-3 variants based on quality, cultural integration, recency
4. Generate distinct blurbs explaining differences
5. Insert variant selector cards into the container

#### When to Use:
- **Manually** is better for flagship units (more control, custom blurbs)
- **Auto-generator** is better for bulk deployment across 313 units

---

## 📚 Real-World Examples

### Example 1: Add "Browse Variants" Section to Science Hub

**Task:** Enhance `/public/science-hub.html` with variant browsing links

**Code:**
```html
<section style="background: white; padding: 3rem; border-radius: 20px; margin: 3rem 0;">
    <h2 style="font-size: 2.25rem; color: #1a4d2e; margin-bottom: 2rem;">
        🔬 Browse Science Teaching Variants
    </h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
        
        <!-- Card 1: Dual Cultural -->
        <a href="/all-teaching-variants-browser.html?subject=Science&cultural=dual" 
           style="background: linear-gradient(135deg, #d1fae5, #a7f3d0); padding: 2rem; border-radius: 16px; text-decoration: none; transition: all 0.3s;"
           onmouseover="this.style.transform='translateY(-4px)'"
           onmouseout="this.style.transform='translateY(0)'">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">🌿🌿</div>
            <h3 style="color: #047857; margin-bottom: 0.75rem;">Dual Cultural (+12.2 Quality!)</h3>
            <p style="color: #065f46;">Te Reo + Whakataukī integration</p>
        </a>

        <!-- Card 2: Excellence -->
        <a href="/all-teaching-variants-browser.html?subject=Science&quality=90"
           style="...">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">⭐</div>
            <h3 style="color: #0369a1;">Excellence (Q90+)</h3>
            <p style="color: #075985;">Gold standard resources</p>
        </a>

        <!-- Add more cards as needed -->
        
    </div>
</section>
```

### Example 2: Create a New Unit with Variants

**Task:** Build `/public/units/y9-science-ecology/index-with-variants.html`

**Steps:**
1. Copy `/public/units/y8-digital-kaitiakitanga/index-with-variants.html` as template
2. Update header (title, stats, description)
3. For each lesson:
   - Query GraphRAG to find variants: `SELECT * FROM graphrag_resources WHERE file_path LIKE '%y9-science-ecology%' AND resource_type = 'Lesson'`
   - Create 2-3 variant cards based on distinct pedagogical approaches
   - Write custom blurbs explaining differences
4. Update resources section with handouts/assessments
5. Add CTA linking to `/all-teaching-variants-browser.html?subject=Science`

---

## 🧠 GraphRAG Queries (Cheat Sheet)

### Find All Variants for a Unit:
```sql
SELECT file_path, title, quality_score, has_te_reo, has_whakataukī, resource_type
FROM graphrag_resources
WHERE file_path LIKE '%y8-digital-kaitiakitanga%'
  AND resource_type IN ('Lesson', 'Handout')
  AND quality_score >= 75
ORDER BY quality_score DESC, file_path;
```

### Count Variants by Subject:
```sql
SELECT 
    canonical_subject,
    COUNT(*) as total_variants,
    AVG(quality_score) as avg_quality
FROM graphrag_resources
WHERE quality_score >= 75
GROUP BY canonical_subject
ORDER BY total_variants DESC;
```

### Find Dual Cultural Resources:
```sql
SELECT file_path, title, quality_score, canonical_subject
FROM graphrag_resources
WHERE has_te_reo = true 
  AND has_whakataukī = true
  AND quality_score >= 90
ORDER BY quality_score DESC
LIMIT 20;
```

---

## ✅ Quality Checklist

Before deploying a new variant page or hub enhancement:

- [ ] **Accessibility**: All `<select>` elements have `aria-label` and `<label for="...">`
- [ ] **HTML5**: Proper `<meta charset>`, `<meta viewport>`, `<title>`, `lang="mi"`
- [ ] **Links Work**: Test all variant card links point to real files
- [ ] **Distinct Blurbs**: Each variant card explains HOW it's different (not just "alternative")
- [ ] **Recommended Badge**: Only ONE variant per lesson should have ⭐ RECOMMENDED
- [ ] **GraphRAG Query**: Verify query returns expected results before hardcoding links
- [ ] **Mobile Friendly**: `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))` for responsive cards
- [ ] **Safari Compatible**: Use `-webkit-backdrop-filter` before `backdrop-filter`

---

## 🎯 Strategic Priorities

### ✅ Already Done:
1. ✅ Built all 4 core components
2. ✅ Applied variant cards to Y7 Algebra (5 lessons)
3. ✅ Applied variant cards to Y8 Digital Kaitiakitanga (18 lessons)
4. ✅ Enhanced Mathematics Hub with "Browse Variants" section
5. ✅ Fixed all critical accessibility and HTML5 errors
6. ✅ Documented system in `agent_knowledge` table

### 🚧 Next Steps (For You!):
1. **Y9 Ecology Unit** - Apply variant cards to 6-lesson ecology unit
2. **Subject Hubs** - Add "Browse Variants" sections to:
   - Science Hub
   - English Hub
   - Social Studies Hub
   - Health & PE Hub
   - Digital Technologies Hub
   - Arts Hub
3. **Auto-Generator Deployment** - Use the JS auto-generator to bulk-create variant pages for remaining 300+ units
4. **PostHog Analytics** - Add click tracking to variant card "Use This Version" buttons to see which variants teachers prefer

---

## 💡 Pro Tips

### Tip 1: Use URL Parameters for Pre-Filtered Links
Instead of linking to the generic browser page, use URL parameters to create curated entry points:
- `?subject=Mathematics&quality=90` = Excellence Mathematics
- `?cultural=dual` = All dual cultural resources
- `?location=css_backup` = Legacy CSS variants

### Tip 2: Copy Existing Patterns
Don't reinvent the wheel! Copy-paste from:
- `/public/units/y7-maths-algebra/index-with-variants.html` (simpler, 5 lessons)
- `/public/units/y8-digital-kaitiakitanga/index-with-variants.html` (complex, 18 lessons)
- `/public/mathematics-hub.html` (Browse Variants section pattern)

### Tip 3: Query GraphRAG First
Before hardcoding variant links, **always query GraphRAG** to verify:
1. The file actually exists
2. The quality score is what you expect
3. The cultural integration flags are correct

Use MCP Supabase tool: `mcp_supabase_execute_sql`

### Tip 4: Prioritize Flagship Units
Focus on the **perfect learning chains** first:
- Y8 Digital Kaitiakitanga (18 lessons, Q92, 100% cultural)
- Y7 Algebra (5 lessons, confidence 1.0)
- Y9 Ecology (6 lessons, confidence 1.0)

These are your showcase examples that demonstrate the system's value.

---

## 📊 System Vital Signs

**As of October 22, 2025:**

| Metric | Value |
|--------|-------|
| Total Resources | 17,396 |
| Teaching Variants (Q75+) | 16,656 |
| Dual Cultural Resources | 2,101 |
| Relationships Mapped | 242,000+ |
| Units with Variant Cards | 2 (Y7 Algebra, Y8 Digital Kaitiakitanga) |
| Subject Hubs Enhanced | 1 (Mathematics) |
| Critical Linter Errors | 0 ✅ |

---

## 🆘 Troubleshooting

### Issue: "Variant link returns 404"
**Solution:** Check if file path in GraphRAG matches actual filesystem. GraphRAG paths start with `./` or `./public`, but URLs should start with `/public` or just `/`.

### Issue: "Too many variants for one lesson (50+)"
**Solution:** Show only 2-3 most pedagogically distinct. Use these criteria to filter:
1. Quality score (prioritize Q90+)
2. Cultural integration (dual > single > none)
3. Location (active site > CSS backup > general backup)
4. Recency (newer > older)

### Issue: "Inline styles linter warnings"
**Solution:** These are non-critical. Inline styles are acceptable for rapid prototyping. Future refactoring can move them to external CSS.

---

## 🌟 Philosophy Reminder

> **"Duplicates aren't bugs - they're pedagogical options."**

The Teaching Variants System celebrates **teacher choice**. Don't try to eliminate variants or pick "the one true version." Instead, surface the options and help teachers choose based on their context.

---

## 📞 Questions?

Check `agent_knowledge` table for latest learnings:
```sql
SELECT * FROM agent_knowledge 
WHERE key_insights @> ARRAY['teaching-variants']
ORDER BY created_at DESC;
```

---

**Happy Building! 🚀**  
*— The Te Kete Ako Agent Team*

