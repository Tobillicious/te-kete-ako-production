# 🎨 TE KETE AKO STYLING MASTER PLAN
## GraphRAG-Powered Design Evolution Strategy

### 📊 **GRAPHRAG INTELLIGENCE ANALYSIS**

**Key Discoveries from Codebase Analysis:**
- **Current State**: 3 competing CSS systems causing chaos (980-line bloated header)
- **Legacy Gold**: Sidebar navigation, A4 print optimization, cultural color palette
- **Design Evolution**: From inline styles → unified system → professional synthesis
- **Cultural Integration**: Te Ao Māori color palette, respectful pattern integration
- **Teacher Focus**: Clean workflow navigation, print-ready materials, mobile optimization

---

## 🎯 **DIALECTICAL DESIGN SYNTHESIS**

### **THESIS: Legacy Design Excellence**
- ✅ **Sidebar Navigation**: Clean, organized, teacher-friendly
- ✅ **A4 Print Optimization**: Professional classroom materials
- ✅ **Cultural Color Palette**: Pounamu green, Kahurangi blue, earth tones
- ✅ **Template System**: Consistent lesson structure
- ✅ **Mobile-First**: Chromebook optimization

### **ANTITHESIS: Modern Web Standards**
- ✅ **Component Architecture**: Reusable, maintainable
- ✅ **Responsive Design**: Multi-device compatibility
- ✅ **Accessibility**: WCAG compliance, screen readers
- ✅ **Performance**: Fast loading, optimized assets
- ✅ **Interactive Elements**: Dropdowns, animations, micro-interactions

### **SYNTHESIS: Te Kete Ako Design System 2.0** ✨

---

## 🏗️ **MASTER DESIGN SYSTEM ARCHITECTURE**

### **1. CORE DESIGN PRINCIPLES**

```css
/* TE KETE AKO DESIGN PHILOSOPHY */
:root {
  /* Cultural Authenticity */
  --philosophy-cultural: "Respectful integration of Te Ao Māori themes";
  --philosophy-professional: "Clean, modern design for educational environments";
  --philosophy-functional: "Teacher workflow optimization";
  --philosophy-accessible: "Inclusive design for all learners";
}
```

### **2. UNIFIED COLOR SYSTEM**

```css
/* CULTURAL COLOR PALETTE - Te Ao Māori Inspired */
:root {
  /* Primary Colors - Cultural Significance */
  --color-pounamu: #059669;        /* Pounamu Green - Learning & Growth */
  --color-pounamu-light: #d1fae5;  /* Light Pounamu - Backgrounds */
  --color-kahurangi: #0284c7;      /* Kahurangi Blue - Knowledge & Wisdom */
  --color-ocean-light: #e0f2fe;    /* Light Ocean - Subtle backgrounds */
  
  /* Earth Tones - Cultural Grounding */
  --color-whenua: #8b5a2b;         /* Earth Brown - Cultural grounding */
  --color-whenua-light: #f5f1eb;   /* Light Earth - Warm backgrounds */
  --color-sunrise: #fef3c7;        /* Sunrise Yellow - Energy & hope */
  
  /* Functional Colors */
  --color-success: #10b981;        /* Success states */
  --color-warning: #f59e0b;        /* Attention needed */
  --color-error: #ef4444;          /* Critical issues */
  --color-info: #3b82f6;           /* Information */
  
  /* Neutral Palette */
  --color-text-primary: #1f2937;   /* Dark text */
  --color-text-secondary: #6b7280;  /* Muted text */
  --color-background: #ffffff;     /* Clean white */
  --color-surface: #f9fafb;        /* Subtle surfaces */
}
```

### **3. TYPOGRAPHY SYSTEM**

```css
/* FLUID TYPOGRAPHY - Chromebook Optimized */
:root {
  /* Font Families */
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-heading: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  
  /* Fluid Scale - Mobile First */
  --text-xs: clamp(0.75rem, 2vw, 0.875rem);
  --text-sm: clamp(0.875rem, 2.5vw, 1rem);
  --text-base: clamp(1rem, 3vw, 1.125rem);
  --text-lg: clamp(1.125rem, 3.5vw, 1.25rem);
  --text-xl: clamp(1.25rem, 4vw, 1.5rem);
  --text-2xl: clamp(1.5rem, 5vw, 2rem);
  --text-3xl: clamp(1.875rem, 6vw, 2.5rem);
  --text-4xl: clamp(2.25rem, 7vw, 3rem);
  
  /* Line Heights */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
}
```

### **4. SPACING SYSTEM**

```css
/* CONSISTENT SPACING - 8px Grid */
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
}
```

---

## 🧩 **COMPONENT ARCHITECTURE**

### **1. NAVIGATION SYSTEM**

```css
/* HEGELIAN SYNTHESIS NAVIGATION */
.te-kete-navigation {
  /* Clean teacher workflow from legacy */
  display: flex;
  align-items: center;
  gap: var(--space-4);
  
  /* Professional animations from mega-menu */
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  
  /* Accessibility from next-level */
  position: relative;
  z-index: 1000;
}

/* Teacher-Focused Navigation Items */
.nav-item {
  position: relative;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-5);
  color: var(--color-text-primary);
  text-decoration: none;
  font-weight: 500;
  border-radius: var(--space-2);
  transition: all 0.2s ease;
}

.nav-link:hover {
  background: var(--color-pounamu-light);
  color: var(--color-pounamu);
  transform: translateY(-1px);
}

/* Dropdown System */
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  border-radius: var(--space-3);
  box-shadow: 0 10px 40px rgba(0,0,0,0.15);
  padding: var(--space-6);
  min-width: 400px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### **2. TEACHING VARIANTS CARDS**

```css
/* INTERACTIVE TEACHING VARIANTS */
.teaching-variants-container {
  margin: var(--space-8) 0;
  padding: var(--space-8);
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-radius: var(--space-4);
  border: 2px solid rgba(5, 150, 105, 0.1);
}

.variants-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-6);
  max-width: 1200px;
  margin: 0 auto;
}

.variant-card {
  background: white;
  border-radius: var(--space-3);
  padding: var(--space-6);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border: 2px solid transparent;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.variant-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #10b981, #3b82f6, #8b5cf6);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.variant-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  border-color: var(--color-pounamu);
}

.variant-card:hover::before {
  transform: scaleX(1);
}
```

### **3. UNIT LESSON SEQUENCE**

```css
/* UNIT LESSON SEQUENCE - 1/3 Screen Component */
.unit-lesson-sequence {
  width: 33.333%;
  min-height: 400px;
  background: white;
  border-radius: var(--space-3);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  padding: var(--space-6);
  position: sticky;
  top: var(--space-8);
}

.lesson-sequence-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-6);
  padding-bottom: var(--space-4);
  border-bottom: 2px solid var(--color-pounamu-light);
}

.lesson-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-4);
  margin-bottom: var(--space-3);
  background: var(--color-surface);
  border-radius: var(--space-2);
  transition: all 0.2s ease;
  cursor: pointer;
}

.lesson-item:hover {
  background: var(--color-pounamu-light);
  transform: translateX(4px);
}

.lesson-item.active {
  background: var(--color-pounamu);
  color: white;
}

/* Teaching Variants Integration */
.lesson-variants {
  margin-top: var(--space-4);
  padding-top: var(--space-4);
  border-top: 1px solid var(--color-surface);
}

.variants-toggle {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  background: var(--color-kahurangi);
  color: white;
  border: none;
  border-radius: var(--space-2);
  cursor: pointer;
  font-size: var(--text-sm);
  transition: all 0.2s ease;
}

.variants-toggle:hover {
  background: #0369a1;
  transform: translateY(-1px);
}
```

---

## 📱 **RESPONSIVE DESIGN STRATEGY**

### **Mobile-First Breakpoints**

```css
/* MOBILE-FIRST RESPONSIVE DESIGN */
/* Base styles for mobile (320px+) */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-4);
}

/* Tablet (768px+) */
@media (min-width: 768px) {
  .container {
    padding: 0 var(--space-6);
  }
  
  .variants-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .unit-lesson-sequence {
    width: 50%;
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .container {
    padding: 0 var(--space-8);
  }
  
  .variants-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  
  .unit-lesson-sequence {
    width: 33.333%;
  }
}

/* Large Desktop (1280px+) */
@media (min-width: 1280px) {
  .container {
    max-width: 1400px;
  }
}
```

---

## 🖨️ **A4 PRINT OPTIMIZATION**

### **Print-Specific Styles**

```css
/* A4 PRINT OPTIMIZATION - Legacy Excellence */
@media print {
  /* Page Setup */
  @page {
    size: A4;
    margin: 2cm;
  }
  
  /* Hide Navigation */
  .te-kete-navigation,
  .dropdown-menu,
  .teaching-variants-container {
    display: none !important;
  }
  
  /* Optimize Typography */
  body {
    font-size: 12pt;
    line-height: 1.4;
    color: #000;
  }
  
  h1, h2, h3, h4, h5, h6 {
    color: #000;
    page-break-after: avoid;
  }
  
  /* Lesson Structure */
  .lesson-phase {
    page-break-inside: avoid;
    margin-bottom: 1.5em;
  }
  
  .teacher-note {
    background: #f8f9fa;
    border-left: 4px solid var(--color-pounamu);
    padding: 1em;
    margin: 1em 0;
  }
  
  /* Cultural Elements */
  .cultural-opening {
    border: 2px solid var(--color-pounamu);
    padding: 1em;
    margin: 1em 0;
    background: var(--color-pounamu-light);
  }
  
  /* Assessment Rubrics */
  .assessment-rubric {
    border: 1px solid #ccc;
    padding: 1em;
    margin: 1em 0;
  }
  
  /* Hide Interactive Elements */
  .variant-card,
  .dropdown-trigger,
  .interactive-elements {
    display: none !important;
  }
}
```

---

## 🎨 **CULTURAL DESIGN INTEGRATION**

### **Te Ao Māori Visual Elements**

```css
/* CULTURAL PATTERN INTEGRATION */
.cultural-pattern {
  position: relative;
  overflow: hidden;
}

.cultural-pattern::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M50 10 L90 50 L50 90 L10 50 Z" fill="none" stroke="%23059669" stroke-width="0.5" opacity="0.1"/></svg>');
  background-size: 50px 50px;
  pointer-events: none;
}

/* Whakataukī Styling */
.whakataukī {
  background: linear-gradient(135deg, var(--color-pounamu-light), var(--color-ocean-light));
  border-left: 4px solid var(--color-pounamu);
  padding: var(--space-6);
  margin: var(--space-6) 0;
  border-radius: var(--space-2);
  font-style: italic;
  position: relative;
}

.whakataukī::before {
  content: '🌿';
  position: absolute;
  top: var(--space-2);
  right: var(--space-4);
  font-size: var(--text-lg);
}

/* Cultural Section Headers */
.cultural-section {
  background: var(--color-whenua-light);
  border: 2px solid var(--color-whenua);
  border-radius: var(--space-3);
  padding: var(--space-6);
  margin: var(--space-8) 0;
}

.cultural-section h2 {
  color: var(--color-whenua);
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.cultural-section h2::before {
  content: '🌿';
  font-size: var(--text-xl);
}
```

---

## ⚡ **PERFORMANCE OPTIMIZATION**

### **Critical CSS Strategy**

```css
/* CRITICAL CSS - Above the Fold */
.te-kete-navigation,
.te-kete-header,
.hero-section {
  /* Critical styles loaded immediately */
  display: block;
  position: relative;
  z-index: 1000;
}

/* Lazy Load Non-Critical Styles */
.variant-card,
.dropdown-menu,
.animations {
  /* Load after initial render */
  opacity: 0;
  animation: fadeIn 0.3s ease forwards;
}

@keyframes fadeIn {
  to { opacity: 1; }
}

/* CSS Custom Properties for Theming */
:root {
  --theme-primary: var(--color-pounamu);
  --theme-secondary: var(--color-kahurangi);
  --theme-background: var(--color-background);
  --theme-surface: var(--color-surface);
}
```

---

## 🧪 **COMPONENT TESTING STRATEGY**

### **Design System Validation**

```css
/* COMPONENT TESTING UTILITIES */
.test-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-4);
  padding: var(--space-8);
  background: var(--color-surface);
}

.test-card {
  background: white;
  border: 2px dashed var(--color-text-secondary);
  border-radius: var(--space-2);
  padding: var(--space-4);
  text-align: center;
}

/* Accessibility Testing */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Focus Indicators */
.focus-visible {
  outline: 2px solid var(--color-pounamu);
  outline-offset: 2px;
}
```

---

## 🚀 **IMPLEMENTATION ROADMAP**

### **Phase 1: Foundation (Week 1-2)**
- [ ] Deploy unified color system
- [ ] Implement fluid typography
- [ ] Create component architecture
- [ ] Test mobile responsiveness

### **Phase 2: Components (Week 3-4)**
- [ ] Build navigation system
- [ ] Create teaching variants cards
- [ ] Develop unit lesson sequence
- [ ] Implement dropdown menus

### **Phase 3: Integration (Week 5-6)**
- [ ] A4 print optimization
- [ ] Cultural pattern integration
- [ ] Performance optimization
- [ ] Accessibility compliance

### **Phase 4: Polish (Week 7-8)**
- [ ] Animation refinement
- [ ] Cross-browser testing
- [ ] Teacher feedback integration
- [ ] Documentation completion

---

## 📊 **SUCCESS METRICS**

### **Design System KPIs**
- **Consistency**: 95% component reuse across site
- **Performance**: <2s load time, >90 Lighthouse score
- **Accessibility**: WCAG AA compliance
- **Teacher Satisfaction**: 4.5/5 usability rating
- **Print Quality**: 100% A4 compatibility

### **Cultural Integration Metrics**
- **Authentic Usage**: 90% culturally appropriate content
- **Teacher Adoption**: 80% use cultural features
- **Student Engagement**: 15% increase in cultural activities
- **Community Feedback**: Positive whānau response

---

## 🎯 **FUTURE EVOLUTION**

### **Advanced Features**
- **Theme Customization**: Teacher-selectable color schemes
- **Seasonal Themes**: Maramataka-based design variations
- **Accessibility Modes**: High contrast, large text options
- **Cultural Variants**: Iwi-specific design elements

### **Technology Integration**
- **CSS Grid Advanced**: Complex layout systems
- **CSS Custom Properties**: Dynamic theming
- **CSS Container Queries**: Component-based responsive design
- **CSS Houdini**: Custom paint and layout APIs

---

*This master plan synthesizes the best of legacy design excellence with modern web standards, creating a beautiful, functional, and culturally authentic design system for Te Kete Ako.* 🌿✨
