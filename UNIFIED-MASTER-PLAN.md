# 🌟 TE KETE AKO - UNIFIED MASTER PLAN

**Created:** October 19, 2025  
**Status:** ACTIVE - Single Source of Truth  
**Vision:** New Zealand's premier Indigenous-centered educational platform - Beautiful beyond belief

---

## 📊 CURRENT STATE (Live from GraphRAG)

**Platform Assets:**
- **19,720 resources** indexed in GraphRAG
- **231,257 relationships** mapped (849 prerequisite chains)
- **662 lessons** (avg quality: 86/100)
- **630 handouts** (avg quality: 83/100)
- **48 units** across all subjects
- **128 interactive games**
- **4,118 resources with Te Reo Māori** (21%)
- **1,556 resources with Whakataukī** (8%)

**Technical Foundation:**
- ✅ Ultimate Beauty System built (Tailwind + Framer Motion + Cultural patterns)
- ✅ GraphRAG 100% indexed for educational content
- ✅ 5 GraphRAG features deployed (widgets, recommendations, pathways)
- ✅ PWA ready (service worker, offline capability)
- ✅ Mobile responsive (100%)

---

## 🎯 MISSION STATEMENT

Transform Te Kete Ako into a world-class educational platform where:
1. **Every lesson is phenomenal** (gold quality or higher)
2. **Navigation is intuitive** (Units → Lessons → Components hierarchy)
3. **Beauty is breathtaking** (professional design sitewide)
4. **Intelligence is embedded** (GraphRAG powers everything)
5. **Culture is authentic** (mātauranga Māori integration)

---

## 🏗️ ARCHITECTURE VISION

### **Hierarchical Content Structure:**

```
UNITS (48 units)
  ↓
  ├── Overview & Context
  ├── Assessments (rubrics, formative tools)
  ├── Curriculum Integration (NZ Curriculum alignment)
  └── LESSONS (662 lessons)
        ↓
        ├── Teaching Sequence
        ├── WALT (We Are Learning To)
        ├── Success Criteria (clear indicators - NOT "WILF")
        ├── WAGOLL (What A Good One Looks Like)
        ├── Handouts/Activities (630 resources)
        ├── GraphRAG Widgets (Next Lesson, Related Resources)
        └── Cultural Context (whakataukī, te reo, tikanga)
```

### **Special Features:**
- **Games Hub** - 128 interactive games beautifully organized
- **Tools Hub** - Teacher generators (crossword, wordsearch, curriculum tagger)
- **Discovery Tools** - 9 GraphRAG-powered exploration features
- **Teacher Dashboard** - AI-powered lesson planning, reflection, analytics

---

## 📅 4-WEEK EXECUTION ROADMAP

### **WEEK 1: Foundation Excellence** (Days 1-7)

#### **Day 1-2: Phenomenal Lesson Template**
**Goal:** Create the gold-standard lesson template

**Build:**
1. **Master Lesson Template** (`/templates/lesson-gold-standard.html`)
   - Beautiful header with cultural pattern
   - Teaching sequence section
   - WALT section (clear learning objectives)
   - WAGOLL section (exemplars and success criteria)
   - Handouts/Activities section (linked via GraphRAG)
   - GraphRAG widgets embedded:
     - "Next Lesson" (prerequisite chain)
     - "Related Resources" (same subject/year)
     - "Download All Handouts" (batch download)
   - Cultural context sidebar (whakataukī, te reo tooltips)
   - Print-optimized (A4 perfect)
   - Framer Motion animations

**Deploy to:** 10 pilot lessons for testing

---

#### **Day 3-4: Unit Pages Completion**
**Goal:** Every unit page has complete structure

**Enhance all 48 unit pages with:**
1. **Unit Overview**
   - Unit whakataukī
   - Learning outcomes
   - Time allocation
   - Year level/Subject tags

2. **Assessments Section**
   - Rubrics (link to assessment library)
   - Formative tools
   - Self-assessment frameworks
   - Cultural assessment protocols

3. **Curriculum Integration**
   - NZ Curriculum achievement objectives
   - NCEA standards (where applicable)
   - Cross-curricular connections
   - Learning progressions

4. **Lessons List**
   - All lessons with status indicators
   - Prerequisite chains visualized
   - Quality scores shown
   - Estimated time per lesson

**Navigation:** Subject Hub → Unit → Lesson → Components

---

#### **Day 5-6: Games Hub + Beauty Rollout**
**Goal:** Make everything gorgeous

**Build:**
1. **Games Hub** (`/public/games/index.html`)
   - Beautiful grid layout
   - Categories: Language | Math | Culture | Science | Thinking
   - 128 games organized
   - "Game of the Week" feature
   - Cultural pattern background (pattern-koru-subtle)
   - Framer Motion card hover effects
   - Search and filter

2. **Beauty System Deployment:**
   - All 48 unit pages
   - All subject hubs (Math, Science, English, Te Ao Māori, etc.)
   - Games Hub
   - Tools Hub (create if not exists)
   - Homepage refinement

**Apply to all pages:**
   - Tailwind CSS classes
   - Cultural pattern backgrounds
   - Typography system (4-size scale: h1/h2/body/small)
   - Framer Motion interactions
   - Consistent spacing/shadows

---

#### **Day 7: Navigation Integration**
**Goal:** Perfect navigation hierarchy

**Update main navigation:**
```
HOME

SUBJECTS ▼
  └─ Mathematics Hub
  └─ Science Hub
  └─ English Hub
  └─ Te Ao Māori Hub
  └─ Digital Technologies Hub
  └─ Social Sciences Hub

UNITS ▼
  └─ Year 7 Units (8 units)
  └─ Year 8 Units (12 units)
  └─ Year 9 Units (14 units)
  └─ Year 10 Units (14 units)

RESOURCES ▼
  └─ 🎮 Games (128 games)
  └─ 🎯 Tools (generators, planners)
  └─ 📄 Handouts (630 resources)
  └─ 📊 Assessments (rubrics, frameworks)

DISCOVERY ▼
  └─ 🔍 Discovery Tools (9 tools)
  └─ 🧠 Intelligence Hub
  └─ 📈 Learning Pathways

TEACHERS ▼
  └─ Teacher Dashboard
  └─ Lesson Planner
  └─ Professional Development
  └─ Community
```

**Add breadcrumbs to all pages:**
`Home > Mathematics > Year 8 Algebra > Lesson 3: Building with Algebra`

---

### **WEEK 2: Intelligence & Interactivity** (Days 8-14)

#### **Day 8-9: GraphRAG Widgets Everywhere**
**Deploy to all 662 lessons:**
1. Next Lesson Widget (uses prerequisite relationships)
2. Related Resources Sidebar (same_subject + related_content)
3. Cultural Connections (shared_cultural_element)
4. Handout Quick Access (lesson_handout_pair)

**Build new widgets:**
5. "Students Also Viewed" (collaborative filtering)
6. "Learning Pathway Visualizer" (D3.js tree of prerequisites)
7. "Unit Progress Tracker" (how far through unit)

---

#### **Day 10-11: Professional Polish**
**Stripe Integration:**
- Teacher Pro: $15/month (unlimited downloads, premium tools)
- School License: $99/month (whole school access)
- Subscription management dashboard

**OAuth Integration:**
- Google Sign-In (one-click teacher signup)
- Microsoft Sign-In (school integration)
- 5x easier onboarding

**PostHog Analytics:**
- Page view tracking
- Feature usage analytics
- A/B testing capability
- User journey funnels
- Teacher dashboard with insights

---

#### **Day 12-13: Enhanced Interactions**
**Framer Motion Deployment:**
- Hover states on all cards/links
- Smooth page transitions
- Loading states (skeleton screens)
- Error states with art direction
- Scroll-triggered animations
- Cultural gesture system (karakia fade-in, whakairo patterns)

**Typography Refinement:**
- Inter for UI/body text
- Noto Sans Māori for te reo
- Perfect scale and rhythm
- Line height optimization
- Responsive typography

---

#### **Day 14: Cultural Authenticity**
**Deploy sitewide:**
1. **Cultural Tooltips** - Hover over te reo terms for pronunciation + meaning
2. **Whakataukī Integration** - Add to pages missing them (target: 50%+)
3. **Pronunciation Guides** - Audio files for key te reo terms
4. **Cultural Context Cards** - Expand tikanga explanations
5. **Dual Knowledge System** - Toggle between Western/Māori perspectives

---

### **WEEK 3: Content Excellence** (Days 15-21)

#### **Day 15-17: Lesson Quality Uplift**
**Goal:** All 662 lessons → Gold quality (90+)

**Systematic enrichment:**
1. Apply gold template to all lessons
2. Ensure every lesson has:
   - Clear WALT
   - Concrete WAGOLL
   - Linked handouts (via GraphRAG)
   - Cultural context
   - Assessment criteria
3. Add missing components (WALT/WAGOLL) where needed
4. Enrich with GraphRAG metadata
5. Quality check each lesson

**Batch processing:**
- 50 lessons/day
- Use template system
- GraphRAG auto-tags

---

#### **Day 18-19: Handout Integration**
**Goal:** All 630 handouts linked to lessons

**Process:**
1. Run GraphRAG relationship builder (lesson_handout_pair)
2. Link orphaned handouts to appropriate lessons
3. Add "Download Handout" buttons to lesson pages
4. Create "All Handouts" page with filters
5. Print optimization (A4 perfect)

**Handout categories:**
- Worksheets
- Assessment rubrics
- Reference sheets
- Activities/Games
- Cultural resources

---

#### **Day 20-21: Custom Illustrations & Art Direction**
**Goal:** Unique visual identity

**Create:**
1. **Custom Illustration System**
   - Cultural motifs (koru, mangopare, tukutuku)
   - SVG icon library
   - Illustrations for each subject
   - Hero graphics for units

2. **Motion Design Language**
   - Purposeful animations (not decorative)
   - Cultural gestures (e.g., karakia rhythm)
   - Loading patterns (koru spiral)
   - Transition choreography

3. **Sophisticated Color Grading**
   - Depth and richness
   - Cultural color palette
   - Subject-specific color schemes
   - Accessibility-first (WCAG AAA)

---

### **WEEK 4: Polish & Launch** (Days 22-28)

#### **Day 22-23: Performance Optimization**
**Goal:** Lighthouse 95+ on all pages

**Optimize:**
1. Image optimization (WebP, lazy loading)
2. Code splitting (critical CSS inline)
3. Database query optimization
4. CDN setup for static assets
5. Minification pipeline
6. Bundle size reduction
7. Service worker caching strategy

**Metrics:**
- Load time <2 seconds
- Time to Interactive <3 seconds
- Cumulative Layout Shift <0.1
- First Contentful Paint <1 second

---

#### **Day 24-25: Accessibility Excellence**
**Goal:** WCAG 2.1 AAA compliance

**Audit & Fix:**
1. Screen reader optimization (all pages)
2. Keyboard navigation (focus states)
3. Color contrast (all text readable)
4. Alt text (all images)
5. ARIA labels (interactive elements)
6. Caption support (videos when added)
7. Dyslexia-friendly font option
8. Text scaling (up to 200%)

---

#### **Day 26-27: QA Testing**
**Comprehensive testing:**

**Functional Tests:**
- Auth flows (signup, login, password reset)
- All 48 units navigation
- All 662 lessons load correctly
- GraphRAG widgets function
- Games work on mobile
- Tools generate correctly
- Handout downloads work

**Cross-Browser:**
- Chrome, Safari, Firefox, Edge
- iOS Safari, Android Chrome

**Mobile:**
- Responsive breakpoints
- Touch interactions
- Performance on slow connections
- Chromebook compatibility

**Accessibility:**
- VoiceOver (iOS)
- NVDA (Windows)
- Keyboard-only navigation
- Color blindness simulation

**Create:**
- QA Test Report
- Bug fix list (prioritized)
- Performance metrics
- User flow videos

---

#### **Day 28: Launch Preparation**
**Final polish:**

1. **Homepage perfection**
   - Hero with cultural animation
   - Featured units (best 6)
   - Games showcase
   - Teacher testimonials
   - GraphRAG stats (live)

2. **Documentation**
   - Teacher Quick Start Guide
   - Student Guide
   - FAQ page
   - Video walkthrough

3. **Marketing Assets**
   - Screenshots (all major pages)
   - Feature list
   - Press release draft
   - Social media graphics

4. **Deployment Checklist**
   - All 662 lessons gold quality ✓
   - All 48 units complete ✓
   - Navigation perfect ✓
   - Beauty sitewide ✓
   - Performance optimized ✓
   - Accessibility AAA ✓
   - QA passed ✓

---

## 🎯 SUCCESS METRICS

### **Week 1 Goals:**
- ✅ Phenomenal lesson template created
- ✅ All 48 unit pages complete
- ✅ Games Hub live
- ✅ Beauty system deployed sitewide
- ✅ Navigation hierarchy perfect

### **Week 2 Goals:**
- ✅ GraphRAG widgets on all 662 lessons
- ✅ Stripe + OAuth integrated
- ✅ PostHog analytics live
- ✅ Framer Motion sitewide
- ✅ Cultural tooltips active

### **Week 3 Goals:**
- ✅ All 662 lessons gold quality (90+)
- ✅ All 630 handouts linked
- ✅ Custom illustrations deployed
- ✅ Art direction complete

### **Week 4 Goals:**
- ✅ Lighthouse 95+ all pages
- ✅ WCAG AAA compliance
- ✅ QA testing complete
- ✅ Launch-ready

---

## 💡 CORE PRINCIPLES

1. **Quality Over Quantity**
   - Every lesson phenomenal (not just good)
   - No placeholder content
   - GraphRAG ensures nothing orphaned

2. **Beauty Is Function**
   - Professional design = trust
   - Cultural authenticity = differentiation
   - Smooth interactions = delight

3. **Intelligence Embedded**
   - GraphRAG powers every feature
   - Personalized recommendations
   - Adaptive pathways

4. **Hierarchical Navigation**
   - Units → Lessons → Components
   - Breadcrumbs everywhere
   - No hidden content

5. **Cultural Leadership**
   - Mātauranga Māori integrated
   - Te reo throughout
   - Whakataukī wisdom
   - Tikanga protocols

---

## 🚀 IMMEDIATE NEXT ACTIONS

**TODAY (Day 1):**
1. Create phenomenal lesson template
2. Test on 10 pilot lessons
3. Start unit page enrichment (first 10 units)

**TOMORROW (Day 2):**
1. Refine template based on feedback
2. Complete all 48 unit pages
3. Start Games Hub build

**THIS WEEK:**
1. Complete Week 1 roadmap
2. Test everything
3. User feedback

---

## 📊 TRACKING PROGRESS

**Store in GraphRAG:**
- Each completed lesson (track quality score improvement)
- Each unit enrichment (components added)
- Each widget deployment (usage metrics)
- Each beauty system application (page count)

**Weekly Review:**
- What shipped?
- What quality improved?
- What blockers emerged?
- What user feedback received?

---

## 🎨 DESIGN SYSTEM

**Typography:**
- H1: 3rem (48px) - Inter Bold
- H2: 2rem (32px) - Inter Semibold  
- Body: 1rem (16px) - Inter Regular
- Small: 0.875rem (14px) - Inter Regular
- Te Reo: Noto Sans Māori

**Cultural Patterns:**
- Koru (spiral growth)
- Tukutuku (woven panels)
- Kowhaiwhai (painted rafters)
- Whakairo (carving patterns)

**Color Palette:**
- Pounamu Green: #059669
- Kahurangi Blue: #0284c7
- Whenua Light: #f5f1eb
- Ocean Light: #e0f2fe
- Sunrise Yellow: #fef3c7

**Spacing System:**
- xs: 0.5rem (8px)
- sm: 1rem (16px)
- md: 1.5rem (24px)
- lg: 2rem (32px)
- xl: 3rem (48px)

---

## 🎯 LONG-TERM VISION (Months 2-6)

**Month 2:** Teacher community launch (500+ teachers)
**Month 3:** KAMAR integration (10 schools piloting)
**Month 4:** Video lessons (50 units with video)
**Month 5:** Student dashboards (progress tracking)
**Month 6:** Full Y7-13 curriculum complete

**Success = 100,000 active users across Aotearoa**

---

## ✅ COMPLETION CRITERIA

**Platform is "complete" when:**
- ✅ All 662 lessons are phenomenal (90+ quality)
- ✅ All 48 units have complete structure
- ✅ Navigation is intuitive (3 clicks to any resource)
- ✅ Beauty is breathtaking (professional sitewide)
- ✅ GraphRAG powers everything (personalized)
- ✅ Cultural integration is authentic (50%+ with whakataukī)
- ✅ Performance is excellent (Lighthouse 95+)
- ✅ Accessibility is exemplary (WCAG AAA)
- ✅ Teachers love it (4.8/5 rating)
- ✅ Students engage (weekly usage)

---

**This is the SINGLE unified plan. All agents execute from this document.**

**Status:** ACTIVE  
**Next Review:** End of Week 1  
**Owner:** All agents working on Te Kete Ako

🌟 **Mā te mōhio ka ora, mā te ora ka mōhio** 🌟

