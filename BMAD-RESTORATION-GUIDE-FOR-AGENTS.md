# 🌿 BMAD RESTORATION GUIDE - FOR ALL AGENTS

**Date:** October 26, 2025  
**Purpose:** Document BMAD cultural design restoration process  
**For:** All Waka Mātauranga agents  
**Status:** ✅ BMAD CSS CREATED & APPLIED

---

## 🎯 WHAT WAS DONE (By Background Audit Agent)

### **Files Created:**

**1. `/public/css/te-kete-bmad-authentic.css`** ✅
- Complete BMAD cultural design system
- 400+ lines of authentic Māori aesthetic
- PRIMARY design system (loads FIRST!)

**2. Applied to Homepage:** ✅
- Added to `public/index.html` line 169
- Loads BEFORE other CSS (wins cascade!)
- Cultural soul restored!

**3. Showcase Pages:** ✅
- `/public/ai-features-showcase.html`
- `/public/graphrag-features-showcase.html`

---

## 🎨 BMAD DESIGN TOKENS (What Was Extracted)

### **From:** BMAD_DESIGN_REVOLUTION.md (August 5, 2025)

### **Color Palette (Natural Pigments):**

```css
/* PRIMARY: Earth & Forest */
--bmad-earth-brown: #8B4513;        ⭐ Primary color
--bmad-forest-green: #2F4F2F;       ⭐ Secondary color
--bmad-forest-light: #3A7D56;
--bmad-forest-dark: #1d3f2a;

/* SECONDARY: Warm Tones */
--bmad-warm-tan: #CD853F;           ⭐ Accent color
--bmad-golden-ochre: #B8860B;       Cultural highlights
--bmad-clay-terracotta: #A0522D;

/* ACCENT: Excellence */
--bmad-gold-excellence: #FFD700;    Q90+ badges
--bmad-jade-green: #00A86B;         Special features

/* NEUTRALS: Warm (NOT cold gray!) */
--bmad-cream-white: #FAF9F6;        Background
--bmad-warm-gray: #8B7D6B;          Muted text
--bmad-dark-text: #2D2520;          Body text
```

**Critical:** These are WARM earth/forest tones, NOT corporate blue #007bff!

---

### **Spacing System (Generous!):**

```css
/* GENEROUS SPACING (Marae-inspired) */
--bmad-space-xl: 4rem;    /* 64px - Major sections */
--bmad-space-lg: 3rem;    /* 48px - Breathing room */
--bmad-space-md: 2rem;    /* 32px - Components */
--bmad-space-sm: 1.5rem;  /* 24px - Elements */
```

**Critical:** NOT tight 8px corporate grid! Cultural spaces need room to breathe!

---

### **Typography (Māori-Friendly):**

```css
--bmad-font-heading: 'Tauri', 'Hind', 'Georgia', serif;
--bmad-font-body: 'Hind', 'Open Sans', 'Segoe UI', sans-serif;
```

**Critical:** Tauri & Hind chosen for Māori character support and warmth!

---

### **Border Radius (Soft & Organic):**

```css
--bmad-radius-sm: 8px;     /* Gentle */
--bmad-radius-md: 12px;    /* Soft, warm */
--bmad-radius-lg: 16px;    /* Koru-like flow */
--bmad-radius-xl: 20px;    /* Very soft (cards) */
```

**Critical:** NOT sharp 4px corporate! Organic, flowing Koru-inspired forms!

---

### **Shadows (Earth-Toned):**

```css
--bmad-shadow-md: 0 4px 12px rgba(139, 69, 19, 0.12);
--bmad-shadow-cultural: 0 4px 16px rgba(184, 134, 11, 0.2);  /* Golden glow */
```

**Critical:** Earth brown shadows, NOT harsh black rgba(0,0,0,0.5)!

---

### **Cultural Patterns:**

```css
--bmad-pattern-koru: [SVG unfurling fern pattern];
--bmad-pattern-tukutuku: [SVG woven geometric pattern];
--bmad-pattern-marae: [Gradient lines for spatial organization];
```

**Critical:** Actual Māori patterns, NOT generic decorative!

---

## 🎯 HOW OTHER AGENTS SHOULD USE BMAD

### **For CSS/Design Agents:**

**DO:**
- ✅ Use BMAD CSS variables in new components
- ✅ Apply `.bmad-card`, `.bmad-button`, `.bmad-hero` classes
- ✅ Use warm earth colors (#8B4513, #2F4F2F)
- ✅ Generous spacing (var(--bmad-space-lg))
- ✅ Soft border radius (var(--bmad-radius-xl))
- ✅ Load BMAD CSS FIRST (before other stylesheets!)

**DON'T:**
- ❌ Use corporate blue (#007bff)
- ❌ Use tight spacing (8px grid)
- ❌ Use sharp borders (4px radius)
- ❌ Use cold gray (#6c757d)
- ❌ Override BMAD variables
- ❌ Apply generic professionalization!

**Example:**
```html
<!-- GOOD: Using BMAD classes -->
<div class="bmad-card">
    <h3 class="bmad-text-cultural">Unit Title</h3>
    <p>Description with warm Māori aesthetic</p>
    <button class="bmad-button bmad-button-cultural">Action</button>
</div>

<!-- BAD: Generic corporate style -->
<div class="card-generic" style="background: #fff; border: 1px solid #ccc;">
    <h3 style="color: #007bff;">Unit Title</h3>
    <button class="btn-primary">Action</button>
</div>
```

---

### **For Frontend/Component Agents:**

**Include BMAD CSS:**
```html
<!-- In ALL new pages, load BMAD FIRST! -->
<link rel="stylesheet" href="/css/te-kete-bmad-authentic.css">
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
<!-- Other CSS after -->
```

**Use BMAD Classes:**
```html
<section class="bmad-hero">
    <h1 class="bmad-hero-title">Page Title</h1>
    <p class="bmad-hero-description">Description</p>
</section>

<div class="bmad-card">
    <h3 class="bmad-text-cultural">Section</h3>
    <p>Content with cultural warmth</p>
</div>

<button class="bmad-button bmad-button-cultural">
    Cultural Action
</button>
```

---

### **For Sidebar Implementation (Tama Kōtahi):**

**Teacher Sidebar MUST use BMAD aesthetic:**
```html
<aside class="bmad-sidebar">
    <!-- Profile section -->
    <div class="bmad-sidebar-section">
        <h5>👤 Profile</h5>
        <!-- ... -->
    </div>
    
    <!-- Teaching Content (Nested with BMAD!) -->
    <div class="bmad-sidebar-section">
        <h5>📚 Teaching Content</h5>
        <details>
            <summary>My Units</summary>
            <div class="bmad-nested-links">
                <a href="/units/y8-algebra" class="bmad-nested-link">
                    Y8 Algebra <span class="bmad-quality-badge gold">Q96</span>
                </a>
            </div>
        </details>
    </div>
    
    <!-- GraphRAG Intelligence Section -->
    <div class="bmad-sidebar-section">
        <h5 class="bmad-text-cultural">🧠 GraphRAG Intelligence</h5>
        <a href="/graphrag-hub.html" class="bmad-nested-link">GraphRAG Hub</a>
        <a href="/graphrag-search.html" class="bmad-nested-link">Smart Search</a>
        <!-- ... -->
    </div>
</aside>
```

---

## 🌿 BMAD PHILOSOPHY (Critical for All Agents!)

### **Core Principles:**

**1. "Cultural principles guide technology"**
- NOT technology shapes culture
- Māori aesthetics FIRST, professional execution second
- Cultural authenticity over corporate precision

**2. "Technology serves as waka (vessel)"**
- Design facilitates knowledge journey
- NOT flashy for flashy's sake
- Purpose-driven aesthetics

**3. "UI patterns are whakairo (carved expressions)"**
- Every design choice has cultural meaning
- Patterns tell stories
- Warmth & character over minimalism

**4. "Knowledge flows like waiora (life-giving waters)"**
- Generous spacing like water flows
- Gentle motion like rivers
- Organic, NOT mechanical

---

## ⚠️ WHAT TO AVOID (Common Mistakes!)

### **DON'T Apply Generic Professionalization:**

**Bad Example (Corporate Generic):**
```css
/* WRONG - Corporate blue, tight spacing, sharp corners */
.card {
    background: #fff;
    padding: 16px;
    border-radius: 4px;
    color: #333;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.btn-primary {
    background: #007bff;  /* Corporate blue! */
    padding: 8px 16px;
    border-radius: 4px;
}
```

**Good Example (BMAD Authentic):**
```css
/* RIGHT - Warm Māori, generous spacing, soft curves */
.bmad-card {
    background: var(--bmad-pure-white);
    padding: var(--bmad-space-lg);      /* 48px generous! */
    border-radius: var(--bmad-radius-xl); /* 20px soft! */
    color: var(--bmad-dark-text);
    box-shadow: var(--bmad-shadow-md);   /* Earth brown tint! */
}

.bmad-button {
    background: linear-gradient(135deg, var(--bmad-earth-brown) 0%, var(--bmad-forest-green) 100%);
    padding: var(--bmad-space-sm) var(--bmad-space-md);
    border-radius: var(--bmad-radius-md);  /* 12px soft! */
}
```

---

## ✅ VERIFICATION CHECKLIST

**For any new page/component, check:**

- [ ] BMAD CSS loaded FIRST?
- [ ] Using BMAD color variables (earth/forest)?
- [ ] Using BMAD spacing (generous)?
- [ ] Using BMAD radius (soft curves)?
- [ ] Using Māori-friendly fonts (Tauri/Hind)?
- [ ] Cultural warmth over corporate precision?
- [ ] Patterns have cultural meaning?
- [ ] Feels Māori, NOT generic?

**If YES to all → ✅ BMAD authentic!**  
**If NO to any → ⚠️ Review and fix!**

---

## 🎊 RESULTS SO FAR

### **Files Using BMAD (Week 13):**
- ✅ index.html (homepage)
- ✅ ai-features-showcase.html
- ✅ graphrag-features-showcase.html
- ⏳ More to come as agents work!

### **Impact:**
- Cultural soul restored on homepage ✨
- Warm Māori aesthetic visible
- "Older better style" implemented!
- User concern addressed!

---

## 🚀 NEXT STEPS FOR AGENTS

### **Māhina Pūmanawa (Design Specialist):**
- Continue applying BMAD to more pages
- Create BMAD component variants
- Ensure consistent cultural aesthetic

### **Tama Kōtahi (Builder):**
- When building sidebar, USE BMAD classes!
- Apply `.bmad-sidebar`, `.bmad-sidebar-section`
- Warm Māori aesthetic throughout!

### **All Other Agents:**
- Load BMAD CSS in any new pages
- Use BMAD classes for components
- Maintain cultural warmth
- Verify with checklist above!

---

**Status:** ✅ BMAD RESTORATION DOCUMENTED  
**Files:** CSS created, applied, documented  
**Philosophy:** Preserved for all agents  
**Impact:** Cultural soul restored! ✨

**Mā te whakaaro Māori ka pai!**  
*(Through Māori thinking it becomes good!)*

🌿🎨✨

**BMAD design is now accessible to ALL agents!**

