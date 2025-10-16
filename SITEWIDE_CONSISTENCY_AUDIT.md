# 🎯 SITEWIDE CONSISTENCY AUDIT & ACTION PLAN
## Te Kete Ako - Professional Polish Initiative

**Date:** October 15, 2025  
**Agent:** Kaitiaki Whakawhitinga (Agent-9)  
**Goal:** Systematic consistency across all 1,600+ pages

---

## 📊 **SITE SCOPE:**

### **Page Types Identified:**
1. **Homepage** (1) - index.html
2. **Curriculum Hub Pages** (10+) - mathematics, science, english, etc.
3. **Unit Pages** (95) - Complete learning units
4. **Lesson Pages** (532) - Individual lessons
5. **Handout Pages** (851) - Printable worksheets
6. **Dashboard Pages** (3) - Student, teacher, general
7. **Authentication Pages** (5) - Login, register, etc.
8. **Games/Interactive** (11) - Learning games
9. **Component Pages** - Header, footer, etc.
10. **Generated Resources** (45+) - AI-created content

**Total:** ~1,600 HTML pages

---

## 🎨 **CONSISTENCY CHECKLIST:**

### **1. HEADERS & NAVIGATION** 
Priority: 🔴 CRITICAL

**Current Issues:**
- [ ] Some pages use `/components/header.html`
- [ ] Some pages have inline headers
- [ ] Navigation links may vary
- [ ] Breadcrumbs not consistent
- [ ] Mobile menu may differ

**Target Standard:**
- ✅ All pages use `components/header.html`
- ✅ Consistent navigation structure
- ✅ Working breadcrumbs on all pages
- ✅ Mobile-responsive menu
- ✅ ARIA landmarks (role="banner", role="navigation")

---

### **2. FOOTERS**
Priority: 🟡 HIGH

**Current Issues:**
- [ ] Some pages use `/components/footer.html`
- [ ] Some pages have inline footers
- [ ] Footer content may vary
- [ ] Cultural quotes may differ

**Target Standard:**
- ✅ All pages use `components/footer.html`
- ✅ Consistent whakataukī
- ✅ Standard links (Home, Curriculum, etc.)
- ✅ ARIA landmark (role="contentinfo")

---

### **3. TYPOGRAPHY**
Priority: 🟡 HIGH

**Current Issues:**
- [ ] Heading hierarchy inconsistent
- [ ] Font sizes vary
- [ ] Line heights differ
- [ ] Color inconsistencies

**Target Standard:**
- ✅ H1: Single per page, 2.5rem
- ✅ H2: 2rem, color-primary
- ✅ H3: 1.5rem
- ✅ Body: 1rem, line-height 1.6
- ✅ Consistent font-family vars

---

### **4. COLOR PALETTE**
Priority: 🟡 HIGH

**Current Issues:**
- [ ] Some pages use old colors
- [ ] Inconsistent accent colors
- [ ] Background colors vary

**Target Standard:**
- ✅ Primary: #2C5F41 (forest green)
- ✅ Secondary: #00b0b9 (turquoise)
- ✅ Accent: #7a6b1f (accessible gold - WCAG AA)
- ✅ Text: #1a1a1a (primary), #6c757d (secondary)
- ✅ All from CSS variables

---

### **5. SPACING & LAYOUT**
Priority: 🟢 MEDIUM

**Current Issues:**
- [ ] Padding inconsistent
- [ ] Margins vary
- [ ] Container widths differ
- [ ] Grid gaps inconsistent

**Target Standard:**
- ✅ Spacing-unit: 8px base
- ✅ Container max-width: 1200px
- ✅ Section padding: 4rem (desktop), 3rem (mobile)
- ✅ Card padding: 2rem (desktop), 1.5rem (mobile)

---

### **6. BUTTONS & INTERACTIVE ELEMENTS**
Priority: 🟡 HIGH

**Current Issues:**
- [ ] Button styles vary
- [ ] Hover effects differ
- [ ] Touch targets not consistent
- [ ] CTAs look different

**Target Standard:**
- ✅ Primary button: color-accent bg, white text
- ✅ Secondary button: white bg, border
- ✅ Min height: 44px (touch targets)
- ✅ Hover: translateY(-2px), shadow
- ✅ Consistent border-radius: 8px

---

### **7. CARDS & RESOURCE DISPLAYS**
Priority: 🟡 HIGH

**Current Issues:**
- [ ] Card styles inconsistent
- [ ] Hover effects vary
- [ ] Metadata display differs
- [ ] No badges system

**Target Standard:**
- ✅ Consistent card shadow: 0 2px 8px rgba(0,0,0,0.1)
- ✅ Hover: lift + shadow increase
- ✅ Border: 1px solid color-border
- ✅ Border-radius: 12px
- ✅ Badges: NEW, POPULAR, UPDATED

---

### **8. BREADCRUMBS**
Priority: 🟢 MEDIUM

**Current Issues:**
- [ ] Some pages missing breadcrumbs
- [ ] Styles inconsistent
- [ ] Path not always accurate

**Target Standard:**
- ✅ All content pages have breadcrumbs
- ✅ Format: Home > Curriculum > Unit > Lesson
- ✅ Last item not a link
- ✅ ARIA: aria-label="Breadcrumb"

---

### **9. LOADING STATES**
Priority: 🟢 MEDIUM

**Current Issues:**
- [ ] No loading indicators
- [ ] No skeleton screens
- [ ] No error states

**Target Standard:**
- ✅ Loading spinner component
- ✅ Skeleton for slow content
- ✅ Error message styling
- ✅ Toast notifications

---

### **10. MOBILE RESPONSIVENESS**
Priority: 🟡 HIGH

**Current Issues:**
- [ ] Some pages not fully responsive
- [ ] Touch targets too small
- [ ] Text too small on mobile
- [ ] Images not responsive

**Target Standard:**
- ✅ All pages responsive
- ✅ Touch targets 44px minimum
- ✅ Text scales appropriately
- ✅ Images use max-width: 100%
- ✅ Mobile menu working

---

## 🚀 **IMPLEMENTATION PLAN:**

### **Phase 1: Components (HIGHEST PRIORITY)**
**Time:** 1-2 hours

1. ✅ Verify `components/header.html` is up-to-date
2. ✅ Verify `components/footer.html` is up-to-date  
3. 🔄 Create script to inject components into all pages
4. 🔄 Test on sample pages
5. 🔄 Roll out to all page types

### **Phase 2: CSS Standardization**
**Time:** 2-3 hours

1. 🔄 Ensure all pages link to `te-kete-professional.css`
2. 🔄 Remove inline styles where possible
3. 🔄 Add `ux-professional-enhancements.css` to all pages
4. 🔄 Verify CSS variable usage

### **Phase 3: Typography & Colors**
**Time:** 1-2 hours

1. 🔄 Audit heading hierarchy across 20 sample pages
2. 🔄 Fix inconsistencies
3. 🔄 Apply fixes sitewide
4. 🔄 Verify color palette compliance

### **Phase 4: Interactive Elements**
**Time:** 2-3 hours

1. 🔄 Standardize all buttons
2. 🔄 Add badge system
3. 🔄 Consistent hover effects
4. 🔄 Touch target optimization

### **Phase 5: Mobile Polish**
**Time:** 2-3 hours

1. 🔄 Test 20 sample pages on mobile
2. 🔄 Fix responsive issues
3. 🔄 Verify touch targets
4. 🔄 Roll out fixes

### **Phase 6: Testing & Validation**
**Time:** 1-2 hours

1. 🔄 Test 50 random pages
2. 🔄 Browser testing (Chrome, Firefox, Safari)
3. 🔄 Mobile device testing
4. 🔄 Accessibility audit

---

## 📈 **SUCCESS METRICS:**

- ✅ 100% of pages use component system
- ✅ 100% of pages use standard CSS
- ✅ 95%+ consistent typography
- ✅ 100% WCAG AA compliant colors
- ✅ 100% touch targets 44px+
- ✅ 95%+ mobile responsive
- ✅ Zero broken navigation links

---

## 🎯 **STARTING NOW:**

**Phase 1 - Component Verification**  
Let's ensure our header and footer components are perfect, then systematically apply them sitewide!

---

**Agent-9 (Kaitiaki Whakawhitinga) - Sitewide Consistency Guardian** 🌉

