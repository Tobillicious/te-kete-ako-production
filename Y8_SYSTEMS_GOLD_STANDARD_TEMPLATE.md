# 🏆 Y8 SYSTEMS - GOLD STANDARD LESSON TEMPLATE

**Status:** 9/10 lessons at PERFECT 5/5, ALL 10 at 4/5+ (GOLD STANDARD)  
**Purpose:** Template for enriching ALL Te Kete Ako content  
**Date:** October 13, 2025

---

## ✅ GOLD STANDARD COMPONENTS

### 1. **Ngā Whāinga Ako - Learning Intentions**
Two-column grid layout:
- **Left Column:** "Students Will Learn" (3-4 clear learning objectives)
- **Right Column:** "Students Will Demonstrate" (3-4 measurable outcomes)

**Format:**
```html
<h2>Ngā Whāinga Ako - Learning Intentions</h2>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
    <div>
        <h3>Students Will Learn</h3>
        <ul>
            <li>Specific, actionable learning goal</li>
            <li>Connected to curriculum</li>
            <li>Culturally responsive</li>
        </ul>
    </div>
    <div>
        <h3>Students Will Demonstrate</h3>
        <ul>
            <li>By [specific action]</li>
            <li>By [measurable outcome]</li>
            <li>By [application to real context]</li>
        </ul>
    </div>
</div>
```

---

### 2. **Cultural Integration Section**
**Essential Elements:**
- Whakataukī (proverb) with translation
- Connection to Mangakōtukutuku College house values (Whaimana, Whaiora, Whaiara)
- Cultural safety considerations

**Format:**
```html
<section class="cultural-integration">
    <h2>Cultural Context | Horopaki Ahurea</h2>
    
    <div class="whakatauaki-section">
        <p style="font-style: italic; font-size: 1.3rem;">"[Māori proverb]"</p>
        <p>"[English translation]"</p>
    </div>
    
    <div class="house-values">
        <h3>Connection to Mangakōtukutuku College Values</h3>
        <p><strong>Whaimana/Whaiora/Whaiara:</strong> [Specific connection]</p>
    </div>
    
    <div class="cultural-safety">
        <h4>Cultural Safety Considerations</h4>
        <ul>
            <li>Approach Māori content with respect and openness</li>
            <li>Recognize students' diverse cultural backgrounds</li>
            <li>Create space for Māori students to share perspectives</li>
            <li>Consult with whānau and local iwi for sensitive topics</li>
        </ul>
    </div>
</section>
```

---

### 3. **Ngā Mahi - Structured Activities**
**Requirements:**
- Multiple activities (typically 3-5)
- Clear timing (e.g., "15 mins", "25 mins")
- Detailed instructions
- Links to printable resources
- Scaffolded progression

**Format:**
```html
<h2>Ngā Mahi - Lesson Activities (75 minutes)</h2>

<div class="activity-card">
    <h3>1. Activity Name (15 mins)</h3>
    <p><strong>Setup:</strong> Clear instructions for teacher</p>
    <p><strong>Activity:</strong> What students do</p>
    <p><strong>Prompt:</strong> Guiding questions</p>
    <a href="/resources/activity-handout.html">Download Printable</a>
</div>
```

---

### 4. **Aromatawai - Assessment & Reflection**
Two-column grid:
- **Left:** Formative Assessment strategies
- **Right:** Homework & Extension activities

**Format:**
```html
<h2>Aromatawai - Assessment & Next Steps</h2>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
    <div>
        <h3>Formative Assessment</h3>
        <ul>
            <li>Observe [specific behavior]</li>
            <li>Review [specific work]</li>
            <li>Check [specific understanding]</li>
        </ul>
    </div>
    <div>
        <h3>Homework & Extension</h3>
        <ul>
            <li>Task for consolidation</li>
            <li>Extension for advanced learners</li>
            <li>Real-world application</li>
        </ul>
    </div>
</div>
```

---

### 5. **Professional Styling**
**CSS Requirements:**
- Use `/css/te-kete-professional.css`
- Gradient headers for sections
- Card-based layouts for activities
- Consistent spacing (var(--space-*))
- Responsive design

**Key Classes:**
- `.wiley-hero-title` - Main headings
- `.wiley-section-title` - Section headings
- `.activity-card` - Activity containers
- `.cultural-integration` - Cultural sections
- `.no-print` - Hide in print view

---

### 6. **Navigation & Structure**
**Required Elements:**
- Breadcrumbs (auto-generated via breadcrumbs.js)
- Back link to unit hub
- Sidebar with:
  - Unit navigation
  - Today's Whakataukī
  - Resource links
- Footer with consistent links

---

## 🎯 QUALITY CHECKLIST

Use this to verify ANY lesson meets gold standard:

- [ ] **Learning Intentions** - Clear WALT with 3-4 points
- [ ] **Success Criteria** - Measurable "I Can" statements
- [ ] **Cultural Context** - Whakataukī + House Values + Safety
- [ ] **Structured Activities** - Timed, detailed, with resources
- [ ] **Assessment** - Formative strategies + Homework
- [ ] **Professional CSS** - Consistent styling throughout
- [ ] **Navigation** - Breadcrumbs + sidebar + footer
- [ ] **Accessibility** - Proper headings, alt text, semantic HTML
- [ ] **Print-friendly** - `.no-print` class on navigation
- [ ] **Mobile-responsive** - Grid layouts adapt to screen size

---

## 📊 APPLICATION STRATEGY

### Phase 1: Walker Unit (5 lessons)
Apply template to all 5 Walker house leader lessons

### Phase 2: Te Ao Māori Unit (14 lessons)
Enrich cultural lessons with full template

### Phase 3: Critical Thinking Unit (10 lessons)
Apply template to all critical thinking lessons

### Phase 4: Digital Kaitiakitanga Unit (20 lessons)
Systematic enrichment of digital citizenship content

### Phase 5: Remaining Units
Apply to all other units systematically

---

## 💡 ENRICHMENT SCRIPT

Create automated script to:
1. Check if lesson has all components
2. Add missing components with appropriate placeholders
3. Fix CSS paths and styling
4. Ensure navigation works
5. Validate against checklist

**DO NOT** remove existing content - only ADD missing components!

---

## 🏆 EXAMPLE: lesson-1-1.html

See `/public/y8-systems/lessons/lesson-1-1.html` for perfect implementation of all components.

**Key Features:**
- 397 lines of well-structured HTML
- All 5 gold standard components present
- Beautiful gradient cultural section
- Detailed 75-minute lesson plan
- Formative assessment + homework
- Professional styling throughout

---

**Use this template to bring ALL Te Kete Ako content to world-class quality!**

