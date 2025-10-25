# 📘 **TE KETE AKO AGENT PLAYBOOK**

**Version:** 3.0 (October 25, 2025)  
**For:** All 12 agents working on the sprint  
**Read Time:** 3 minutes  
**Importance:** ⭐⭐⭐ MANDATORY

---

## 🎯 **YOUR MISSION IN 30 SECONDS**

Transform Te Kete Ako from a broken CSS mess into a polished, professional educational platform **TODAY** using this 3-phase sprint:

| Phase | Duration | Focus | Success |
|-------|----------|-------|---------|
| **1️⃣ Infrastructure** | 0-90 min | Fix CSS + Supabase + verify pages | 3 agents, all pass QA ✅ |
| **2️⃣ Components** | 90-180 min | Build cards, heroes, breadcrumbs, etc. | 6 agents, all pass QA ✅ |
| **3️⃣ Deploy** | 180-210 min | Test, approve, deploy to production | 3 agents, live 🚀 |

---

## 🚀 **QUICK START (YOU START HERE)**

### **Step 1: Know Your Role**
```
Find YOUR agent number (1-12):
- Agent 1: Kaitiaki Aronui (Overseer)
- Agent 2: QA Lead (Quality Gatekeeper)
- Agents 3-5: Infrastructure (Foundation)
- Agents 6-11: Components (Beauty)
- Agent 12: Testing & Performance

→ Open: TEAM-ONBOARDING-OCT25.md
→ Find YOUR section
→ Read YOUR task
```

### **Step 2: Understand the Blocker**
```
Current state: 8 CSS files fighting each other → builds are broken
Why it matters: Cards won't style, heroes won't display, pages look terrible
Your job: FIX IT in your phase
```

### **Step 3: Join the Standup**
```
Every 30 minutes, post ONE LINE:
"[TASK] | Status: [IN_PROGRESS/BLOCKED/DONE] | Blocker: [none/description] | Next: [action]"

Example:
"CSS Consolidation | IN_PROGRESS | Blocker: none | Next: merge nav styles into professionalization.css"

Post to: ACTIVE_QUESTIONS.md
```

---

## 📋 **YOUR CHECKLIST (DO BEFORE STARTING)**

- [ ] **Read** TEAM-ONBOARDING-OCT25.md (find YOUR section)
- [ ] **Understand** CRITICAL-SITE-AUDIT-OCT25.md (what we fixed)
- [ ] **Reference** PROFESSIONALIZATION-SPRINT-STATUS.md (design system)
- [ ] **Follow** TEAM-DAILY-STANDUP-OCT25.md (log your progress)
- [ ] **Use** ACTIVE_QUESTIONS.md (post blockers here immediately)

---

## 🔧 **CRITICAL RULE: NO SURPRISES**

### **Before You Code**
✅ Post to ACTIVE_QUESTIONS.md: "Agent X: Starting [TASK]"

### **While You Code**
✅ Post standup every 30 min with status update

### **If You Get Stuck**
✅ Post immediately: "Agent X: [BLOCKED] - [description] - need help from [Agent Y]"

### **When You're Done**
✅ Post: "Agent X: [DONE] - [deliverable summary] - ready for QA"

**Why?** So Kaitiaki knows what to do next and other agents can unblock

---

## 🎨 **DESIGN SYSTEM QUICK REFERENCE**

### **Colors (Use These Variables!)**
```css
--color-primary: #1a4d2e          /* Forest Green - main brand */
--color-primary-hover: #0f3a1e    /* Darker hover state */
--color-success: #10b981          /* Mātauranga Green - positive */
--color-pounamu: #15875d          /* NZ Jade - heritage */
--color-kahurangi: #0066cc        /* NZ Blue - sky */
--color-kupanui: #f4511e          /* Warm Orange - energy */
```

### **Typography**
```css
--font-heading: 'Playfair Display', serif   /* Elegant headers */
--font-body: 'Inter', -apple-system, sans-serif  /* Clean body text */
--font-mono: 'Fira Code', monospace             /* Code snippets */
```

### **Spacing (Use These Increments!)**
```
4px (--space-1)  | 8px (--space-2)  | 12px (--space-3) 
16px (--space-4) | 20px (--space-5) | 32px (--space-8)
```

### **Breakpoints (Mobile-First!)**
```
Mobile (375px default)
Tablet (768px minimum)
Desktop (1024px minimum)
Large Desktop (1280px minimum)
```

---

## ⚡ **PHASE 1 AGENTS (Agents 3-5-4):** Your Mission

### **Agent 3: CSS Consolidation**
```
FROM: 8 conflicting CSS files
TO: 2 strategic files

ACTION:
1. Keep: te-kete-professional.css (primary system - 3,409 lines)
2. Keep: professionalization-system.css (utilities - 2,100 lines)
3. Merge INTO professionalization-system.css:
   - navigation-standard.css
   - mobile-*.css files
4. Create: non-critical.css (everything else, loaded async)
5. Update: index.html <link> tags (new order)

DONE WHEN: index.html loads with no CSS warnings, cascade is clean
```

### **Agent 4: Supabase Singleton**
```
FROM: 4 different Supabase client instances (memory leak!)
TO: 1 shared singleton

ACTION:
1. Open: /public/js/supabase-singleton.js (source of truth)
2. Find all files with: window.supabase.createClient()
3. Replace with: import { getSupabaseClient } from '/supabase-singleton.js'
4. Delete duplicate client initialization code
5. Test: Console should show 1 Supabase connection (not 4)

DONE WHEN: Console shows clean Supabase initialization, no errors
```

### **Agent 5: Page Verification**
```
TEST THESE 7 PAGES (in your browser):
- http://localhost:3000/ (homepage)
- http://localhost:3000/units/
- http://localhost:3000/teachers/
- http://localhost:3000/lessons/
- http://localhost:3000/handouts/
- http://localhost:3000/games/
- http://localhost:3000/curriculum-index.html

LOOK FOR:
✅ Header is 80px tall (not 8,442px!)
✅ Navigation visible
✅ No layout shift
✅ No console errors
✅ Content renders smoothly

DONE WHEN: All 7 pages pass inspection
```

---

## 🎨 **PHASE 2 AGENTS (Agents 6-11):** Your Mission

**→ START ONLY AFTER Phase 1 ✅ DONE**

### **Agent 6: Card Components**
```
BUILD: Reusable card component system

DELIVERABLE: Add to professionalization-system.css
.card { base styles }
.card:hover { smooth hover effects }
.card-elevated { shadow elevation }
.card-flat { minimal styling }
.card-outlined { border-only style }

DONE WHEN: Cards render beautifully on lesson/resource pages
```

### **Agent 7: Hero Sections**
```
BUILD: Responsive hero templates

DELIVERABLE: HTML templates + CSS
- Hero with title + subtitle + CTA button
- Hero with gradient overlay
- Hero with background image
- Hero with whakataukī (Māori proverb)
- All responsive (stack on mobile)

DONE WHEN: Homepage hero looks stunning, mobile-friendly
```

### **Agent 8: Breadcrumbs**
```
BUILD: Navigation breadcrumb trails

DELIVERABLE: HTML markup + CSS styling
<nav class="breadcrumbs">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/units">Units</a></li>
    <li aria-current="page">Y7 Algebra</li>
  </ol>
</nav>

DONE WHEN: Breadcrumbs visible on all pages, keyboard accessible
```

### **Agent 9: Footer**
```
BUILD: Unified footer component

DELIVERABLE: Multi-column footer with:
- Learning links (by subject)
- About Te Kete Ako
- Social media icons
- Legal (Privacy, Terms)
- Copyright notice

DONE WHEN: Footer displays on all pages consistently
```

### **Agent 10: Responsive Design**
```
BUILD: Mobile-first responsive system

DELIVERABLE: Media queries for 3 breakpoints:
@media (min-width: 768px) { /* Tablet styles */ }
@media (min-width: 1024px) { /* Desktop styles */ }
@media (min-width: 1280px) { /* Large desktop */ }

DONE WHEN: Works perfectly on 375px (iPhone SE) to 1920px
```

### **Agent 11: Animations**
```
BUILD: Smooth 60fps animations

DELIVERABLE:
- Fade-in on page load
- Scroll-reveal for cards
- Button hover animations (150ms ease-in-out)
- Link transitions
- Page transitions

DONE WHEN: All animations smooth, no jank, 60fps stable
```

---

## 📊 **QUALITY STANDARDS (EVERYONE MUST PASS)**

Before Agent 2 (QA Lead) approves your work:

- ✅ **No CSS warnings** - cascade is clean
- ✅ **No JavaScript errors** - console is quiet
- ✅ **Mobile-first** - works on 375px (iPhone SE)
- ✅ **Accessible** - WCAG AA (color contrast 4.5:1, keyboard nav)
- ✅ **60fps** - animations are smooth, no jank
- ✅ **Professional** - looks polished, no rough edges
- ✅ **Cultural** - incorporates mātauranga Māori where relevant

**If any of these fail → QA Lead rejects → back to you for fixes**

---

## 🚨 **IF YOU GET STUCK**

### **Blocker? DO THIS:**
1. **Post immediately** to ACTIVE_QUESTIONS.md with [BLOCKED] tag
2. **Be specific:** "Agent X: [BLOCKED] - Need CSS variable value from Agent 3"
3. **Tag the agent** who might help: "cc: Agent 3"
4. **Wait max 10 min** for response

### **Common Blockers & Solutions:**
```
❌ "CSS isn't applying"
→ Wait for Agent 3 CSS consolidation, then Hard refresh (Cmd+Shift+R)

❌ "Database connection error"
→ Wait for Agent 4 Supabase fix, restart dev server

❌ "Page layout is broken"
→ Agent 5 is verifying pages - post your findings to ACTIVE_QUESTIONS.md

❌ "I don't understand the design system"
→ Read PROFESSIONALIZATION-SPRINT-STATUS.md section "CSS Classes to Use"
```

---

## 🎯 **SUCCESS CHECKLIST FOR EACH AGENT**

### **Phase 1 Checkpoint (Agent 2 will verify):**
- [ ] Agent 3: CSS consolidation complete → No CSS warnings in console
- [ ] Agent 4: Supabase singleton → Only 1 client instance in console
- [ ] Agent 5: Page verification → All 7 pages render perfectly
- [ ] All agents: Ready for Phase 2

### **Phase 2 Checkpoint (Agent 2 will verify):**
- [ ] Agent 6: Cards working → Hover effects smooth, all variants visible
- [ ] Agent 7: Heroes ready → Responsive, beautiful, whakataukī included
- [ ] Agent 8: Breadcrumbs live → Visible on all pages, accessible
- [ ] Agent 9: Footer complete → Multi-column, all links work
- [ ] Agent 10: Responsive ✅ → Perfect on 375px/768px/1024px
- [ ] Agent 11: Animations smooth → 60fps, no jank anywhere
- [ ] All agents: Ready for Phase 3

### **Phase 3 Final (Agent 2 will sign off):**
- [ ] Agent 12: Testing passed → Cross-device ✅, Performance ✅
- [ ] Agent 2: QA approved → All standards met ✅
- [ ] Agent 1: Deployed live 🚀 → Production shows new design

---

## 📈 **HOW TO COMMIT YOUR WORK**

```bash
# Stage your changes
git add public/css/...
git add public/js/...
git add components/...

# Commit with clear message (Agent name + what you did)
git commit -m "Agent 6: Add card component system with hover effects

- Added .card, .card-outlined, .card-elevated styles
- Implemented smooth 150ms hover transitions
- Responsive grid support (2-4 columns)
- WCAG AA contrast verified (4.5:1 minimum)
- Mobile-first, no JavaScript required"

# WAIT for Kaitiaki (Agent 1) to review
# Then: git push (when Kaitiaki says OK)
```

---

## 💬 **COMMUNICATION PROTOCOL**

| Channel | Use For | Format |
|---------|---------|--------|
| ACTIVE_QUESTIONS.md | Status updates, blockers, questions | "Agent X: [MESSAGE]" |
| TEAM-DAILY-STANDUP-OCT25.md | Log every 30 min | Brief update with status |
| Git commits | Track work, create audit trail | Clear message with Agent name |
| This playbook | Quick reference | You're reading it! |

---

## ✨ **WHAT AMAZING LOOKS LIKE**

After today's sprint, the user will see:

```
🟢 Homepage renders beautifully with professional styling
🟢 Navigation is clean, breadcrumbs work everywhere
🟢 Cards have elegant hover effects
🟢 Hero sections look stunning with whakataukī
🟢 Mobile view (375px) is perfect
🟢 Animations are smooth (60fps, no jank)
🟢 WCAG AA accessibility passing
🟢 Zero console errors
🟢 Teachers ready to beta test
🟢 Cultural integration visible throughout
```

---

## 🚀 **FINAL REMINDERS**

1. **Don't Surprise Kaitiaki** → Update ACTIVE_QUESTIONS.md every 30 min
2. **One Standup Format** → Keep messages consistent for clarity
3. **Quality Over Speed** → Agent 2 (QA) will reject rushed work
4. **No Cowboy Coding** → Ask questions, use ACTIVE_QUESTIONS.md
5. **Test Before Declaring Done** → "Looks good locally" ≠ "Deployed"
6. **Be Specific in Commits** → Include what changed, why, and which files
7. **Cultural Alignment Matters** → Te Kete Ako is built on mātauranga Māori

---

## 🎊 **LET'S BUILD SOMETHING AMAZING**

**Time:** October 25, 2025  
**Status:** 🟢 READY  
**Energy:** 🔋 FULL  
**Team:** 🙌 ASSEMBLED

**You've got this! 🚀**

---

*Questions? Check ACTIVE_QUESTIONS.md*  
*Need design guidance? Read PROFESSIONALIZATION-SPRINT-STATUS.md*  
*Not sure what to do? Read TEAM-ONBOARDING-OCT25.md*
