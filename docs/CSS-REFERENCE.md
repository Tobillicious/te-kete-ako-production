# 🎨 CSS Reference - Te Kete Ako Design System

**Source:** `css/main.css` - The ONLY CSS file (89KB, 3,974 lines)  
**Design System:** V5 - "Beautiful, Minimalist, Print-First, Modern"  
**Based on:** Clean version from July 27, 2025 (commit `7b1c43f90`)

**User feedback:** *"OMG I love you! This works so well!"*

---

## ⚠️ CRITICAL: ONE CSS FILE ONLY

**DO NOT:**
- ❌ Add Tailwind
- ❌ Add "Ultimate Design System"
- ❌ Add BMAD Authentic
- ❌ Add Kehinde Wiley styles
- ❌ Add ANY additional CSS files

**This file has EVERYTHING you need. Adding more CSS = breaking what works.**

---

## 🎨 CSS Variables (Design Tokens)

### Colors - Cultural Palette

```css
/* Primary Colors */
--color-primary: #1a1a1a;        /* Deep Charcoal - main text, headings */
--color-secondary: #00b0b9;      /* Turquoise Blue (Ocean) - links, accents */
--color-accent: #f5a623;         /* Golden Yellow (Sun) - highlights */

/* Cultural Colors */
--color-maori-red: #d83c3e;      /* Traditional Māori Red */
--color-earth: #8b6f47;          /* Earth Brown (Whenua) */
--color-forest: #2C5F41;         /* Deep Forest Green (Ngahere/Pounamu) */
--color-cultural-teal: #40E0D0;  /* Cultural Teal */

/* Background Colors */
--color-cultural-light: #f0f8f0; /* Light green backgrounds */
--color-cultural-accent: #e8f4f8;/* Light teal backgrounds */
--color-warmth: #fef7ed;         /* Warm cream */
--color-nature: #ecfdf5;         /* Nature green */

/* Neutrals */
--color-background: #ffffff;     /* Page background */
--color-surface: #ffffff;        /* Card/surface color */
--color-card-hover: #f8f9fa;     /* Hover states */
--color-text-primary: #1a1a1a;   /* Body text */
--color-text-secondary: #6c757d; /* Secondary text */
--color-text-muted: #9ca3af;     /* Muted/disabled text */
--color-border: #e5e7eb;         /* Borders */
--color-border-light: #f3f4f6;   /* Light borders */
```

**Usage:**
```css
.my-element {
    color: var(--color-secondary);
    background: var(--color-cultural-light);
}
```

### Typography

```css
--font-headings: 'Montserrat', 'Helvetica', 'Arial', sans-serif;
--font-body: 'Lato', 'Helvetica', 'Arial', sans-serif;
--font-special: 'Merriweather', 'Georgia', serif;
```

**When to use:**
- `--font-headings`: All h1-h6 tags
- `--font-body`: Body text, paragraphs
- `--font-special`: Quotes, whakataukī, special text

### Spacing & Layout

```css
--spacing-unit: 8px;          /* Base spacing (multiply for consistency) */
--content-width: 1200px;      /* Max content width */
--sidebar-width: 300px;       /* Sidebar width */
--header-height: 72px;        /* Header height */
```

### Effects

```css
/* Shadows */
--shadow-light: 0 1px 3px rgba(0,0,0,0.08);
--shadow-medium: 0 4px 12px rgba(0,0,0,0.08);
--shadow-strong: 0 8px 24px rgba(0,0,0,0.12);

/* Border Radius */
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;

/* Transitions */
--transition-fast: 0.15s ease;
--transition-medium: 0.25s ease;
--transition-slow: 0.35s ease;
```

---

## 📐 Layout Classes

### Main Container System

```html
<div class="main-container">
    <aside class="left-sidebar">...</aside>
    <main class="content-area">...</main>
</div>
```

**Classes:**
- `.main-container` - Flexbox container for sidebar + content
- `.left-sidebar` - 300px sidebar (hidden on mobile, hidden when printing)
- `.content-area` - Main content area (flexible width)

### Typography Classes

```css
.page-title          /* Main page heading (h1 style) */
.page-subtitle       /* Subtitle under main heading */
.section-title       /* Section headings (h2/h3 style) */
.section-title-main  /* Larger section title */
.text-italic         /* Italic text */
.text-bold           /* Bold text */
.text-sm             /* Small text */
.text-secondary      /* Secondary color text */
```

**Example:**
```html
<h1 class="page-title">Lesson Title</h1>
<p class="page-subtitle">Learn about X, Y, Z</p>
<h2 class="section-title">Introduction</h2>
```

### Navigation

```css
.breadcrumb          /* Back navigation link */
.nav-brand           /* Site logo/title in header */
.main-nav            /* Main navigation ul */
.nav-icon            /* Icon in navigation (emoji) */
.nav-dropdown        /* Dropdown menu */
```

### Sidebar Widgets

```css
.sidebar-widget       /* Widget container */
.sidebar-widget-title /* Widget heading */
```

**Example:**
```html
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">Whakataukī</h3>
    <p class="text-italic">"Quote here"</p>
</div>
```

### Content Boxes

```css
.technique-box       /* Key concept/technique box */
.example-box         /* Example/demo box */
.activity-box        /* Activity/task box */
.cultural-opening-section /* Cultural context section */
.whakatauki-container     /* Whakataukī box */
```

**Example:**
```html
<div class="technique-box">
    <h4>PEEL Method</h4>
    <p>Point, Evidence, Explanation, Link</p>
</div>
```

### Spacing Utilities

```css
.mb-2    /* Margin bottom: 16px */
.mb-4    /* Margin bottom: 32px */
.mt-2    /* Margin top: 16px */
.mt-4    /* Margin top: 32px */
```

**Pattern:** Multiply spacing-unit (8px) by number
- `.mb-2` = 2 × 8px = 16px
- `.mb-4` = 4 × 8px = 32px

### Print Control

```css
.no-print    /* Hide when printing (sidebars, nav, etc.) */
```

**Always add to:** Headers, footers, sidebars, navigation

---

## 🖨️ Print Styles

**Automatic print optimization:**
- A4 page size
- 2cm margins
- Hides: `.no-print`, `.site-header`, `.site-footer`, `.left-sidebar`
- Optimizes: Font sizes, spacing for readability
- Page breaks: Avoids breaking headings from content

**No extra work needed!** Just add `.no-print` to elements you don't want printed.

---

## 🎯 Common Patterns

### Pattern 1: Standard Page Layout

```html
<div class="main-container">
    <aside class="left-sidebar no-print">
        <div class="sidebar-widget">
            <h3 class="sidebar-widget-title">Related Resources</h3>
            <ul>
                <li><a href="#">Link 1</a></li>
            </ul>
        </div>
    </aside>
    
    <main class="content-area">
        <h1 class="page-title">Page Title</h1>
        <p class="page-subtitle">Subtitle</p>
        
        <section class="mb-4">
            <h2 class="section-title">Section</h2>
            <p>Content...</p>
        </section>
    </main>
</div>
```

### Pattern 2: Cultural Element

```html
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">Whakataukī</h3>
    <p class="text-italic text-secondary">"Māori proverb"</p>
    <p class="text-sm">English translation</p>
</div>
```

### Pattern 3: Content Box

```html
<div class="technique-box">
    <h4><strong>Key Concept</strong></h4>
    <p class="text-italic">Explanation</p>
    <div class="example-box">
        <strong>Example:</strong> Concrete example here
    </div>
</div>
```

### Pattern 4: Curriculum Alignment

```html
<section class="curriculum-alignment mb-4">
    <h3 class="section-title">NZ Curriculum Alignment</h3>
    <p><strong>Learning Area:</strong> English</p>
    <p><strong>Year Level:</strong> Year 8</p>
    <p><strong>Achievement Objective:</strong> [Code and description]</p>
</section>
```

---

## 🎨 Color Usage Guide

### When to Use Each Color

**Primary (#1a1a1a - Deep Charcoal)**
- Body text
- Headings
- Main content
- Dark elements

**Secondary (#00b0b9 - Turquoise Blue)**
- Links
- Interactive elements
- Call-to-action buttons
- Highlights

**Accent (#f5a623 - Golden Yellow)**
- Important highlights
- Badges
- Special callouts
- Attention-grabbing elements

**Forest Green (#2C5F41 - Pounamu)**
- Cultural elements
- Te Ao Māori content
- Special navigation states
- Theme color (PWA)

**Cultural Light (#f0f8f0)**
- Background for cultural sections
- Subtle highlighting
- Content boxes

---

## 📱 Responsive Behavior

**Breakpoints:**
```css
@media (max-width: 768px) {
    /* Mobile: Sidebar hidden, single column */
}

@media (min-width: 769px) {
    /* Desktop: Sidebar visible, two columns */
}
```

**Mobile optimizations:**
- Sidebar auto-hides
- Navigation becomes hamburger menu (if implemented)
- Font sizes scale down
- Spacing adjusts
- Touch-friendly targets

---

## ✅ Best Practices

### DO:

```css
/* ✓ Use CSS variables */
color: var(--color-secondary);

/* ✓ Use existing classes */
<h1 class="page-title">

/* ✓ Add no-print to non-content elements */
<header class="site-header no-print">

/* ✓ Use spacing utilities */
<section class="mb-4">
```

### DON'T:

```css
/* ✗ Hardcode colors */
color: #00b0b9;  /* Use var(--color-secondary) instead */

/* ✗ Create new CSS files */
/* We have ONE file. Keep it that way. */

/* ✗ Override with !important */
/* Fix the root cause instead */

/* ✗ Add inline styles (except games) */
/* Use existing classes */
```

---

## 🔧 Adding New Styles

**If you MUST add new styles:**

1. **Check if it exists first** - Search main.css
2. **Use existing patterns** - Copy similar styles
3. **Use CSS variables** - Don't hardcode values
4. **Add to main.css** - Don't create new files
5. **Document here** - Update this guide

**Example:**
```css
/* Add to main.css, following existing patterns */
.my-new-component {
    background: var(--color-cultural-light);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    padding: calc(var(--spacing-unit) * 2);
    margin-bottom: calc(var(--spacing-unit) * 4);
}
```

---

## 📋 Quick Reference Card

### Most Used Classes

```
Layout:
  .main-container, .left-sidebar, .content-area

Typography:
  .page-title, .page-subtitle, .section-title
  .text-italic, .text-bold, .text-sm, .text-secondary

Spacing:
  .mb-2, .mb-4, .mt-2, .mt-4

Boxes:
  .technique-box, .example-box, .activity-box
  .sidebar-widget, .sidebar-widget-title

Cultural:
  .cultural-opening-section, .whakatauki-container

Print:
  .no-print

Navigation:
  .breadcrumb, .nav-brand, .main-nav
```

### Most Used Variables

```
Colors:
  var(--color-primary)     /* Charcoal */
  var(--color-secondary)   /* Turquoise */
  var(--color-accent)      /* Golden */
  var(--color-forest)      /* Pounamu */

Spacing:
  var(--spacing-unit)      /* 8px */
  var(--content-width)     /* 1200px */

Effects:
  var(--shadow-medium)
  var(--radius-md)
  var(--transition-medium)
```

---

## 🚨 Troubleshooting

### "My styles aren't working!"

1. **Check CSS path** - Is it correct for your file location?
2. **Check class spelling** - `.page-title` not `.pageTitle`
3. **Check browser cache** - Hard refresh (Cmd+Shift+R)
4. **Check element inspector** - Are styles being applied?

### "It looks different on mobile!"

That's expected! The design is responsive. Test on actual devices or use browser dev tools.

### "Print layout is broken!"

- Did you add `.no-print` to navigation/sidebars?
- Are you using the standard `.content-area` structure?
- Check print preview (Cmd+P)

---

## 📚 Related Documentation

- `templates/README.md` - How to use templates
- `CRITICAL-THINKING-GRAPHRAG.md` - Why we don't add more CSS
- `DEVELOPMENT-FOUNDATION.md` - Overall dev guide

---

**Remember: This CSS file represents what WORKS. Don't "improve" it by adding complexity. Simple is beautiful. Beautiful is what users love.**

*Last updated: October 26, 2025*  
*Based on: css/main.css (3,974 lines, 89KB)*  
*User feedback: "OMG I love you! This works so well!"*

