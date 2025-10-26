# 📚 Te Kete Ako Templates

**Source of Truth:** These templates are extracted from the ACTUAL working clean version (July 27, 2025 commit `7b1c43f90`)

**NOT from GraphRAG documentation. NOT from AI-generated "ideal" systems. From REAL, WORKING, USER-APPROVED code.**

---

## 🎯 What Are These Templates?

These are **copy-and-fill** templates for creating new teaching resources. They include:
- ✅ Correct HTML structure
- ✅ Proper CSS links (`css/main.css` - the ONE design system)
- ✅ Cultural elements (whakataukī, Te Reo, tikanga)
- ✅ Print-friendly styles
- ✅ Accessibility features
- ✅ Working navigation

**User verdict on this design:** *"OMG I love you! This works so well!"*

---

## 📋 Available Templates

### 1. **lesson-template.html**
**Based on:** Original `lesson-template.html` from root directory  
**Use for:** Individual lesson plans (single 45-60 minute lessons)  
**Features:**
- Cultural opening (Whakatūwhera)
- Learning intentions (Ngā Whāinga Ako)
- Activity sections
- Assessment guidance
- Sidebar navigation

**When to use:** Creating a standalone lesson or adding to an existing unit

---

### 2. **handout-template.html**
**Based on:** `handouts/writers-toolkit-peel-argument-handout.html`  
**Use for:** Student handouts, worksheets, reference materials  
**Features:**
- Clean, printable layout
- Example boxes and technique boxes
- Practice activities
- Reflection questions
- NZ Curriculum alignment section

**When to use:** Creating materials students will print and use

---

### 3. **unit-template.html**
**Based on:** `y8-systems-unit.html`  
**Use for:** Multi-week teaching units (complete unit plans)  
**Features:**
- Unit context bar (shows unit info prominently)
- Week-by-week lesson organization
- Resources section
- Assessment framework
- Complete curriculum alignment

**When to use:** Creating a full 3-6 week unit plan

---

### 4. **game-template.html**
**Based on:** `games/te-reo-wordle.html`  
**Use for:** Interactive educational games  
**Features:**
- Game container layout
- Stats tracking (localStorage)
- Instructions section
- Cultural connection box
- Inline CSS for game-specific styles

**When to use:** Creating an interactive game or activity

---

## 🚀 How to Use These Templates

### Method 1: Copy & Fill (Recommended)

```bash
# 1. Copy the template
cp templates/lesson-template.html lessons/my-new-lesson.html

# 2. Edit the file
# - Replace [placeholders] with actual content
# - Update CSS path if needed (see note below)
# - Fill in cultural elements
# - Add your content

# 3. Test locally
open http://localhost:8000/lessons/my-new-lesson.html

# 4. Done!
```

### Method 2: Use as Reference

Open the template and copy the structure you need into your existing file.

---

## ⚠️ IMPORTANT: CSS Path Adjustments

The templates use `css/main.css` but you need to adjust the path based on file location:

```html
<!-- From root directory -->
<link rel="stylesheet" href="css/main.css">

<!-- From /lessons/ directory -->
<link rel="stylesheet" href="../css/main.css">

<!-- From /handouts/ directory -->
<link rel="stylesheet" href="../css/main.css">

<!-- From /units/lessons/ directory -->
<link rel="stylesheet" href="../../css/main.css">
```

**Rule:** Count how many directories deep you are, add that many `../`

---

## 🎨 Design System Reference

All templates use **ONE CSS file**: `css/main.css`

**DO NOT:**
- ❌ Add Tailwind
- ❌ Add "Ultimate Beauty System"
- ❌ Add multiple CSS files
- ❌ Follow GraphRAG design documentation

**DO:**
- ✅ Use existing CSS classes from `main.css`
- ✅ Use CSS variables (see below)
- ✅ Keep it simple
- ✅ Trust what works

### Key CSS Variables

```css
--color-primary: #1a1a1a;           /* Deep Charcoal */
--color-secondary: #00b0b9;          /* Turquoise Blue */
--color-accent: #f5a623;             /* Golden Yellow */
--color-forest: #2C5F41;             /* Pounamu Green */
--color-text-primary: #1a1a1a;
--color-text-secondary: #6c757d;
```

### Common CSS Classes

```css
.page-title              /* Main page heading */
.page-subtitle           /* Subtitle */
.section-title           /* Section headings */
.breadcrumb              /* Back navigation */
.sidebar-widget          /* Sidebar boxes */
.sidebar-widget-title    /* Sidebar heading */
.cultural-opening-section /* Cultural context section */
.example-box             /* Example/demo boxes */
.technique-box           /* Key concept boxes */
.mb-4                    /* Margin bottom */
```

---

## 📝 Content Guidelines

### Cultural Elements (Required)

Every resource should include:
1. **Whakataukī** - Relevant Māori proverb
2. **Te Reo terms** - Use Māori language naturally
3. **Cultural connection** - How does this honor Te Ao Māori?

### Structure (Recommended)

1. **Clear title** - What is this about?
2. **Introduction** - Why does this matter?
3. **Main content** - The teaching/learning material
4. **Practice/Activity** - Students apply knowledge
5. **Reflection** - Think deeper
6. **Curriculum alignment** - NZ Curriculum links

---

## 🔧 Required Scripts

All templates include these scripts (in this order):

```html
<script src="../js/supabase-client.js"></script>
<script src="../js/auth-ui.js"></script>
<script src="../js/simple-bookmarks.js"></script>
<script src="../js/main.js"></script>
<script src="../js/shared-components.js"></script>
<script src="../js/footer.js"></script>
```

**Note:** Disabled analytics and accessibility scripts (they had bugs)

---

## ✅ Quality Checklist

Before publishing your new resource:

- [ ] Replaced all `[placeholders]` with actual content
- [ ] CSS path is correct for file location
- [ ] Cultural elements included (whakataukī, Te Reo)
- [ ] NZ Curriculum alignment added
- [ ] Tested in browser locally
- [ ] Print preview works (Cmd+P)
- [ ] Links work (no 404s)
- [ ] File name is descriptive and kebab-case

---

## 🚨 What NOT to Do

### DON'T Follow GraphRAG Design Docs

GraphRAG has documentation marked "Quality 100" that references:
- "Ultimate Design System"
- "Kehinde Wiley aesthetic" (failed system)
- "BMAD Authentic" (caused CSS crisis)
- "Hegelian synthesis" (AI nonsense)

**These are AI-generated docs about FAILED systems.**

**Trust these templates instead. They're from the version users actually love.**

### DON'T Add Complexity

- No Tailwind
- No Framer Motion
- No "gesture systems"
- No additional CSS files
- No fancy frameworks

**Keep it simple. Simple works. Users love simple.**

---

## 💡 Tips for Success

### 1. Start Small
Don't try to create the perfect resource. Copy a template, fill it in, test it, improve it.

### 2. Look at Examples
Check existing resources in the same category:
- `/lessons/` - See how other lessons are structured
- `/handouts/` - See handout patterns
- `/units/` - See unit organization

### 3. Keep Cultural Elements Authentic
Don't just add whakataukī as decoration. Make sure:
- The proverb relates to the content
- Te Reo is used correctly
- Cultural connections are meaningful

### 4. Test Print Styles
Teachers will print these. Press `Cmd+P` (or `Ctrl+P`) and check:
- Does it look good printed?
- Are sidebars hidden? (they should be)
- Is text readable?

---

## 📚 Further Reading

- `docs/CSS-REFERENCE.md` - All CSS classes explained (coming soon)
- `docs/FILE-STRUCTURE.md` - Where files go (coming soon)
- `CRITICAL-THINKING-GRAPHRAG.md` - Why we don't follow GraphRAG design docs

---

## 🎯 Remember

**These templates represent what ACTUALLY WORKS.**

Not what AI thinks should work.  
Not what's "theoretically better."  
Not what's in GraphRAG documentation.

**What users love. What's clean. What's simple. What's beautiful.**

**Trust the templates. Build on success.**

---

*Last updated: October 26, 2025*  
*Based on commit: 7b1c43f90 (July 27, 2025)*  
*User feedback: "OMG I love you! This works so well!"*

