# 🚀 ACTIVE QUESTIONS & SPRINT COORDINATION

**Date:** October 25, 2025 - TEAM ONBOARDING SESSION  
**Status:** 🟢 READY TO DEPLOY - AGENTS ASSEMBLING  

---

## 🎯 **TODAY'S SPRINT BRIEFING**

### **Phase 1: Infrastructure (0-90 min)** ⚡
**Start:** NOW  
**Agents:** 3, 4, 5 (working in parallel)

| Agent | Task | Deliverable | Timeline | Status |
|-------|------|-------------|----------|--------|
| 3 | Consolidate CSS (8→2) | critical-path.css + non-critical.css | 30 min | ⏳ PENDING |
| 4 | Fix Supabase singletons | One instance everywhere | 30 min | ⏳ PENDING |
| 5 | Verify pages render | 7 pages green ✅ | 30 min | ⏳ PENDING |

**Blocker?** Reach out in this channel immediately!

---

### **Phase 2: Component Building (90-180 min)** 🎨
**Start:** When Phase 1 ✅ DONE  
**Agents:** 6, 7, 8, 9, 10, 11 (working in parallel)

| Agent | Task | Deliverable | Timeline | Status |
|-------|------|-------------|----------|--------|
| 6 | Card components | Elevated/flat/outlined + hover | 90 min | ⏳ PENDING |
| 7 | Hero sections | Title/subtitle/CTA, gradients, whakataukī | 90 min | ⏳ PENDING |
| 8 | Breadcrumbs | Styled nav trails + accessible | 60 min | ⏳ PENDING |
| 9 | Footer | Multi-column, links, social | 60 min | ⏳ PENDING |
| 10 | Responsive design | 375px/768px/1024px+ | 60 min | ⏳ PENDING |
| 11 | Animations | Fade-ins, scroll reveals, hover | 60 min | ⏳ PENDING |

**Blocker?** Reach out immediately!

---

### **Phase 3: Testing & Deployment (180-210 min)** ✅
**Start:** When Phase 2 ✅ DONE  
**Agents:** 12, 2 (QA), 1 (Deploy)

| Agent | Task | Deliverable | Timeline | Status |
|-------|------|-------------|----------|--------|
| 12 | Cross-device testing | Mobile/tablet/desktop ✅ | 30 min | ⏳ PENDING |
| 2 | QA sign-off | All components pass WCAG AA | 30 min | ⏳ PENDING |
| 1 | Merge & deploy | Live on Netlify | 20 min | ⏳ PENDING |

---

## 📊 **STANDUP UPDATES** (Every 30 min)

### **Format:**
```
Agent X: "[TASK] | Status: [BLOCKED/IN_PROGRESS/DONE] | Blocker: [none/description] | Next: [action]"
```

### **STANDUP 1** (Time: _____)
- Agent 3: 
- Agent 4: 
- Agent 5: 
- Agent 2 (QA): 

### **STANDUP 2** (Time: _____)
- (Agents 6, 7, 8, 9, 10, 11 updates)

### **STANDUP 3** (Time: _____)
- (Agents 12, 2, 1 updates)

---

## 🔧 **QUICK WINS THIS HOUR**

### **CSS Consolidation (Agent 3)**
**Current:** 8 conflicting CSS files  
**Target:** 2 strategic files (critical + non-critical)

```
DO THIS:
1. Copy te-kete-professional.css → KEEP AS IS
2. Copy professionalization-system.css → KEEP (utilities)
3. MERGE: navigation-standard.css → professionalization-system.css
4. MERGE: mobile-*.css → professionalization-system.css
5. CREATE: non-critical.css (async load everything else)
6. UPDATE: index.html CSS load order
```

### **Supabase Fix (Agent 4)**
**Current:** 4 separate Supabase client instances  
**Target:** 1 singleton everywhere

```
DO THIS:
1. Check /public/js/supabase-singleton.js (source of truth)
2. Find all createClient() calls
3. Replace with: import { getSupabaseClient } from '/public/js/supabase-singleton.js'
4. Test: console should show ONE Supabase connection (not 4)
```

### **Page Verification (Agent 5)**
**Current:** Some pages rendering with layout issues  
**Target:** All 7 pages rendering perfectly

```
TEST THESE (in browser):
- / (homepage)
- /units/
- /teachers/
- /lessons/
- /handouts/
- /games/
- /curriculum-index.html

LOOK FOR:
✅ Header 80px (not 8,442px!)
✅ No layout shift
✅ Navigation visible
✅ No console errors
```

---

## 🚨 **KNOWN BLOCKERS & SOLUTIONS**

### **Blocker: "CSS looks wrong"**
**Cause:** Multiple CSS files conflicting  
**Solution:** Wait for Agent 3 to consolidate CSS → Phase 1 checkpoint

### **Blocker: "Component loads twice"**
**Cause:** Navigation loading from multiple sources  
**Solution:** Agent 5 verifies single load → Phase 1 checkpoint

### **Blocker: "Database connection errors"**
**Cause:** Multiple Supabase instances  
**Solution:** Agent 4 fixes singletons → Phase 1 checkpoint

---

## 📋 **CRITICAL RESOURCES**

**Read First (5 min each):**
- [ ] `/TEAM-ONBOARDING-OCT25.md` ← YOU ARE HERE
- [ ] `/PROFESSIONALIZATION-SPRINT-STATUS.md` ← Current work status
- [ ] `/CRITICAL-SITE-AUDIT-OCT25.md` ← What we fixed

**Design System Reference:**
```css
--color-primary: #1a4d2e (Forest Green)
--font-heading: 'Playfair Display', serif
--font-body: 'Inter', -apple-system, sans-serif
--space-4: 1rem (default spacing)
```

---

## 🎓 **PROFESSIONALIZATION SYSTEM - CSS CLASSES**

**Available now for all agents to use:**

```html
<!-- Typography -->
<h1 class="text-5xl font-heading font-bold text-primary">Heading</h1>
<p class="text-base font-body text-secondary">Body text</p>

<!-- Spacing -->
<div class="mt-8 mb-6 p-4">Spaced content</div>

<!-- Colors -->
<button class="bg-primary text-white hover:bg-primary-hover">Button</button>

<!-- Components (being built now) -->
<div class="card">Card coming soon</div>
<div class="hero">Hero coming soon</div>
```

---

## ✅ **DEPLOYMENT CHECKLIST**

### **Phase 1 Sign-off:**
- [ ] Agent 3: CSS consolidated
- [ ] Agent 4: Supabase fixed
- [ ] Agent 5: Pages verified
- [ ] Agent 2: QA approval

### **Phase 2 Sign-off:**
- [ ] Agent 6: Cards working
- [ ] Agent 7: Heroes ready
- [ ] Agent 8: Breadcrumbs live
- [ ] Agent 9: Footer complete
- [ ] Agent 10: Responsive ✅
- [ ] Agent 11: Animations smooth
- [ ] Agent 2: QA approval

### **Phase 3 Sign-off:**
- [ ] Agent 12: Testing passed
- [ ] Agent 2: Final QA approval
- [ ] Agent 1: Deployed live 🚀

---

## 📝 **QUESTIONS & NOTES**

### **For Phase 1 Agents:**
- Question: CSS consolidation - which file should win conflicts? → Answer: professionalization-system.css (priority)
- Question: Should we keep te-kete-ultimate-beauty-system.css? → Answer: Review with Agent 2, may consolidate

### **For Phase 2 Agents:**
- Question: Card hover animation - how fast? → Answer: 150ms ease-in-out
- Question: Hero on mobile - full width? → Answer: Yes, stack vertically

### **For Phase 3 Agents:**
- Question: Which browsers to test? → Answer: Chrome, Firefox, Safari, Edge (latest 2 versions)
- Question: Performance target? → Answer: LCP < 2.5s, CLS < 0.1, all at 60fps

---

## 🚀 **READY TO LAUNCH**

```
✅ Team assembled
✅ Roles assigned
✅ Blockers identified
✅ Success criteria defined
✅ Resources available

STATUS: 🟢 READY FOR PHASE 1 START
```
