# 🚀 **TE KETE AKO: 12-AGENT TEAM ONBOARDING**

**Date:** October 25, 2025  
**Status:** 🟢 READY TO DEPLOY  
**Overseer:** Kaitiaki Aronui V3.0  

---

## 📋 **QUICK START (5 MINUTES)**

### **What We're Building**
Te Kete Ako is an AI-powered educational platform integrating mātauranga Māori with 19,298+ resources, serving NZ teachers and students across all age groups.

### **Current Status (October 25)**
- ✅ Frontend CSS fixed (navigation, heroes, styling conflicts resolved)
- ✅ Backend 95% indexed (19,298 resources)
- ✅ 621 gold standard resources (Q90+)
- ⏳ **NOW:** Professionalization sprint (Card components, Heroes, Breadcrumbs)

### **Mission Today**
- **Team:** Fix 10 highest-priority items
- **Output:** Professional, polished frontend ready for teacher beta
- **Deployment:** Continuous (as agents complete work)

---

## 👥 **12-AGENT ROLE ASSIGNMENTS**

### **TIER 1: Leadership** (Oversee all work)
**Agent 1 (Kaitiaki Aronui):** Strategic Oversight
- Manages dependencies between agents
- Reviews deliverables for cultural alignment
- Coordinates cross-agent communication
- **This session:** Onboarding + Priority assignment

**Agent 2 (QA Lead - Agent 9a4dd0d0):** Quality Standards
- Sets QA standards (WCAG AA, 60fps, mobile-first)
- Reviews all PR-like changes
- Validates cultural integration
- Approves deployments

---

### **TIER 2: Infrastructure** (Foundation)
**Agent 3 (CSS & Styling):** Visual System
- **Task:** Consolidate CSS files (8 → 2 strategic files)
- **Deliverable:** critical-path.css + non-critical.css
- **Timeline:** 1 hour
- **Files to touch:**
  - `/public/css/te-kete-professional.css` (3,409 lines - **KEEP**)
  - `/public/css/professionalization-system.css` (2,100 lines - **MERGE**)
  - `/public/css/navigation-standard.css` (700 lines - **MERGE**)
  - `/public/css/te-kete-ultimate-beauty-system.css` (1,000+ lines - **REVIEW**)
  - Others → `/public/css/non-critical.css` (async load)

**Agent 4 (Backend & Database):** Data Pipeline
- **Task:** Fix Supabase client duplications
- **Deliverable:** One singleton instance everywhere
- **Timeline:** 30 min
- **Files to fix:**
  - `/public/js/graphrag-connection-counter.js` (Line 27-28)
  - `/public/js/my-kete-database.js` (constructor auto-init)
  - `/public/js/supabase-singleton.js` (the source of truth)

**Agent 5 (Navigation & Structure):** Site Architecture
- **Task:** Verify all major pages render correctly
- **Deliverable:** Green status on 7+ key pages
- **Timeline:** 30 min
- **Pages to test:**
  - / (homepage)
  - /units/
  - /teachers/
  - /lessons/
  - /handouts/
  - /games/
  - /curriculum-index.html

---

### **TIER 3: Components** (Visual Polish - 6 Agents)
**Agent 6 (Cards):** Card Component System
- **Task:** Build consistent card styles
- **Deliverable:** Card variants (elevated/flat/outlined) with hover effects
- **Timeline:** 1-2 hours
- **Output:** Add to `professionalization-system.css`:
  ```css
  .card { border: 1px solid var(--color-border); border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: all 150ms ease-in-out; }
  .card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.15); transform: translateY(-2px); }
  .card.outlined { border: 2px solid var(--color-primary); background: transparent; }
  ```
- **Where to use:** Lesson cards, resource cards, unit cards

**Agent 7 (Heroes):** Hero Section System
- **Task:** Build responsive hero templates
- **Deliverable:** Hero with title/subtitle/CTA, Hero with gradient, Hero with whakataukī
- **Timeline:** 2-3 hours
- **Components:**
  - Base hero (title + subtitle + CTA button)
  - Hero with gradient overlay
  - Hero with background image
  - Hero with Māori proverb (whakataukī)
  - All responsive (stack on mobile)

**Agent 8 (Breadcrumbs):** Navigation Breadcrumbs
- **Task:** Implement breadcrumb trails
- **Deliverable:** Styled, accessible breadcrumbs on all pages
- **Timeline:** 1 hour
- **Markup pattern:**
  ```html
  <nav class="breadcrumbs" aria-label="Breadcrumb">
    <ol>
      <li><a href="/">Home</a></li>
      <li><a href="/units">Units</a></li>
      <li aria-current="page">Y7 Algebra</li>
    </ol>
  </nav>
  ```

**Agent 9 (Footer):** Footer System
- **Task:** Build unified footer component
- **Deliverable:** Multi-column footer with links, social, legal
- **Timeline:** 1-2 hours
- **Sections:**
  - Learning Links (by subject)
  - About Te Kete Ako
  - Social Media
  - Legal (Privacy, Terms, etc.)
  - Copyright

**Agent 10 (Responsive):** Mobile/Tablet Design
- **Task:** Mobile-first responsive system
- **Deliverable:** Works seamlessly on 375px, 768px, 1024px+
- **Timeline:** 2-3 hours
- **Breakpoints:**
  ```css
  /* Mobile first (375px) */
  @media (min-width: 768px) { /* Tablet */ }
  @media (min-width: 1024px) { /* Desktop */ }
  @media (min-width: 1280px) { /* Large desktop */ }
  ```

**Agent 11 (Animations):** Smooth Interactions
- **Task:** Add 60fps animations and transitions
- **Deliverable:** Fade-ins, scroll reveals, button interactions
- **Timeline:** 2-3 hours
- **Effects:**
  - On-load fade-in for components
  - Scroll-reveal for cards
  - Hover animations for buttons/links
  - Page transitions

---

### **TIER 4: Quality & Deployment** (2 Agents)
**Agent 12 (Testing & Performance):** QA Sprint
- **Task:** Cross-device testing + performance audit
- **Deliverable:** 
  - Tests on mobile/tablet/desktop
  - Core Web Vitals passing (LCP < 2.5s, CLS < 0.1)
  - Zero accessibility violations
- **Timeline:** 1-2 hours

**Agent 1 (Deployment):** Release Coordination
- **Task:** Prepare for production deployment
- **Deliverable:** All changes merged, tested, deployed to Netlify
- **Timeline:** 30 min after all agents finish

---

## 🎯 **TODAY'S SPRINT ROADMAP**

### **Phase 1: Infrastructure (0-90 min)** ⚡
**Goal:** Fix broken foundations so styling works everywhere

1. **Agents 3-4-5 work in parallel:**
   - Agent 3: Consolidate CSS (30 min)
   - Agent 4: Fix Supabase singletons (30 min)
   - Agent 5: Verify pages (30 min)

2. **Checkpoint:** All agents report "DONE" before Phase 2 starts
3. **Sign-off:** Agent 2 (QA Lead) validates fixes

### **Phase 2: Component Building (90-180 min)** 🎨
**Goal:** Build beautiful, reusable components using professionalization system

1. **Agents 6-11 work in parallel:**
   - Agent 6: Card components (90 min)
   - Agent 7: Hero sections (90 min)
   - Agent 8: Breadcrumbs (60 min)
   - Agent 9: Footer (60 min)
   - Agent 10: Responsive breakpoints (60 min)
   - Agent 11: Animations (60 min)

2. **Checkpoint:** Each agent shows their work in pull request format
3. **Sign-off:** Agent 2 (QA Lead) validates styling + accessibility

### **Phase 3: Testing & Deployment (180-210 min)** ✅
**Goal:** Production-ready release

1. **Agent 12:**
   - Cross-device testing (30 min)
   - Performance audit (30 min)

2. **Agent 1:**
   - Merge all changes (10 min)
   - Deploy to Netlify (10 min)

3. **Final Status:** 🚀 LIVE

---

## 📊 **DAILY STANDUP FORMAT**

**When:** Every 30 minutes  
**Format:** 1-minute updates from each agent

```
Agent X: "[TASK] | Status: [BLOCKED/IN_PROGRESS/DONE] | Blocker: [none/description] | Next: [specific action]"

Example:
Agent 6: "Card Components | IN_PROGRESS | Blocker: waiting for CSS consolidation from Agent 3 | Next: add hover effects"
```

**Log to:** ACTIVE_QUESTIONS.md (append each standup)

---

## 🔧 **CRITICAL TOOLS & RESOURCES**

### **Supabase (Database & GraphRAG)**
```javascript
// ALWAYS use this singleton:
import { getSupabaseClient } from '/public/js/supabase-singleton.js';
const supabase = getSupabaseClient();

// ❌ NEVER do this:
// const supabase = window.supabase.createClient(url, key);
```

### **CSS Architecture**
```
/public/css/
  ├── te-kete-professional.css    (3,409 lines - PRIMARY SYSTEM)
  ├── professionalization-system.css (2,100 lines - UTILITIES)
  ├── navigation-standard.css      (700 lines - DEPRECATED, merge into primary)
  ├── critical-path.css            (NEW - above-fold critical CSS)
  └── non-critical.css             (NEW - lazy-loaded async)
```

### **Design System Colors**
```css
/* Use these CSS variables (not hardcoded hex!) */
--color-primary: #1a4d2e (Forest Green)
--color-primary-hover: #0f3a1e
--color-success: #10b981 (Mātauranga Green)
--color-pounamu: #15875d (NZ Jade)
--color-kahurangi: #0066cc (NZ Blue)
--color-kupanui: #f4511e (Warm Orange)
```

### **Typography**
```css
--font-heading: 'Playfair Display', serif (headers)
--font-body: 'Inter', -apple-system, sans-serif (body)
--font-mono: 'Fira Code', monospace (code)
```

### **Spacing Scale**
```
--space-1: 0.25rem (4px)
--space-2: 0.5rem (8px)
--space-3: 0.75rem (12px)
--space-4: 1rem (16px) ← DEFAULT
--space-5: 1.25rem (20px)
--space-8: 2rem (32px)
```

---

## 🚨 **CRITICAL BLOCKERS & HOW TO UNBLOCK**

### **Blocker #1: CSS Cascade Conflicts**
**Who can unblock:** Agent 3  
**What to do:** Merge CSS files into strategic order
```
1. professionalization-system.css (WINS - has final say)
2. te-kete-professional.css
3. navigation-standard.css
4. others async-loaded (non-critical.css)
```

### **Blocker #2: Supabase Multiple Instances**
**Who can unblock:** Agent 4  
**What to do:** Replace all `createClient()` calls with singleton
```javascript
// ✅ DO THIS:
import { getSupabaseClient } from '/public/js/supabase-singleton.js';

// ❌ NOT THIS:
const supabase = window.supabase.createClient(URL, KEY);
```

### **Blocker #3: Component Loading Race Conditions**
**Who can unblock:** Agent 5  
**What to do:** Verify page load order (nav → hero → content → polish)

---

## 📚 **QUALITY STANDARDS (MUST PASS)**

Every deliverable must meet:
- ✅ **Accessibility:** WCAG AA (color contrast 4.5:1, keyboard nav, screen reader)
- ✅ **Performance:** 60fps animations, no jank
- ✅ **Mobile-First:** Works perfectly on 375px (iPhone SE)
- ✅ **Cultural Alignment:** Incorporates mātauranga Māori perspectives
- ✅ **Code Quality:** No console errors, clean CSS, semantic HTML
- ✅ **Browser Support:** Works on Chrome, Firefox, Safari, Edge (latest 2 versions)

---

## 🎓 **QUICK REFERENCE: PROFESSIONALIZATION SYSTEM**

### **CSS Classes to Use**

**Typography:**
```html
<h1 class="text-5xl font-heading font-bold text-primary">Page Title</h1>
<p class="text-base font-body text-secondary">Body text with secondary color</p>
<code class="text-sm font-mono bg-neutral-100">Code snippet</code>
```

**Spacing:**
```html
<section class="py-8 px-4 md:py-12 md:px-8">
  <div class="mb-6 p-4">Content with margin-bottom-6 and padding-4</div>
</section>
```

**Colors:**
```html
<button class="bg-primary text-white hover:bg-primary-hover">Primary Button</button>
<div class="border border-primary rounded-lg p-4">Card with primary border</div>
<span class="text-success">Success message</span>
```

**Components:**
```html
<!-- Card -->
<div class="card">Content</div>

<!-- Button -->
<button class="btn btn-primary btn-lg">Click Me</button>

<!-- Form Group -->
<div class="form-group">
  <label for="email">Email</label>
  <input type="email" id="email" class="input" />
</div>
```

---

## 📋 **DEPLOYMENT CHECKLIST**

Before moving to next phase:

**Phase 1 (Infrastructure):**
- [ ] CSS files consolidated → Agent 3
- [ ] Supabase singleton fixed → Agent 4
- [ ] All pages rendering → Agent 5
- [ ] QA Lead approves → Agent 2

**Phase 2 (Components):**
- [ ] Card components built → Agent 6
- [ ] Hero sections built → Agent 7
- [ ] Breadcrumbs added → Agent 8
- [ ] Footer built → Agent 9
- [ ] Responsive breakpoints tested → Agent 10
- [ ] Animations working → Agent 11
- [ ] QA Lead approves → Agent 2

**Phase 3 (Deployment):**
- [ ] Cross-device tested → Agent 12
- [ ] Performance audit passed → Agent 12
- [ ] All changes merged → Agent 1
- [ ] Deployed to production → Agent 1
- [ ] QA Lead sign-off → Agent 2
- [ ] Deployed live ✅

---

## 🚀 **HOW TO COMMIT WORK**

```bash
# Stage your changes
git add public/css/...
git add public/js/...

# Commit with clear message
git commit -m "Agent 6: Add card component system with hover effects

- Added .card, .card-outlined, .card-elevated styles
- Added smooth hover animations (150ms transition)
- Responsive grid support for 2-4 column layouts
- WCAG AA accessible with proper contrast"

# Wait for Kaitiaki to merge all agent work
# Then: git push
```

---

## 💬 **COMMUNICATION CHANNELS**

- **Standup Updates:** ACTIVE_QUESTIONS.md (append every 30 min)
- **Blockers:** Update ACTIVE_QUESTIONS.md with [BLOCKED] tag
- **Questions:** Use ACTIVE_QUESTIONS.md section at bottom
- **Final Status:** Update PROFESSIONALIZATION-SPRINT-STATUS.md

---

## ✨ **SUCCESS LOOKS LIKE**

After today's sprint:
```
🟢 Homepage renders beautifully with professional styling
🟢 Navigation, cards, heroes all use professionalization system
🟢 Mobile users see perfect 375px layout
🟢 Animations are smooth (60fps, no jank)
🟢 WCAG AA accessibility passing
🟢 Teachers are ready to start beta testing
🟢 Cultural integration is visible throughout
🟢 Zero console errors
```

---

## 🎊 **LET'S BUILD EXCELLENCE**

**Status:** Ready for deployment!  
**Energy:** 🔋 Full  
**Let's go team! 🚀**
