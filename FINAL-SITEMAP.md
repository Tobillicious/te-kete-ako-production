# 🎯 FINAL SITEMAP - Clean, Professional, Teacher-Focused

---

## 🎨 **HOMEPAGE - Gorgeous, Dynamic, Minimal Text**

```
┌──────────────────────────────────────────────────────────────┐
│ HEADER (Clean, professional)                                 │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TE KETE AKO                                              │ │
│ │                                                          │ │
│ │ [Resources ▾] [Curriculum ▾] [Games] [AI Generator]     │ │
│ │ [Other ▾] [Third Party ▾]                   [Login]     │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
│                                                              │
│ HERO (Changes weekly - gorgeous image)                      │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │                                                          │ │
│ │        Featured Resource This Week                       │ │
│ │        or Educational News from NZ                       │ │
│ │        or New Resource Spotlight                         │ │
│ │                                                          │ │
│ │        (Beautiful, minimal text, Kehinde Wiley style)    │ │
│ │                                                          │ │
│ └──────────────────────────────────────────────────────────┘ │
│                                                              │
│ CONTENT (Clean sections - no bloat)                         │
│ Maybe 3-4 featured resources or trending or nothing         │
│ Homepage is GORGEOUS first, informative second               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Key:** Homepage is beautiful and changes. Brings teachers back regularly.

---

## 🎯 **HEADER DROPDOWNS - Detailed**

### **1. Resources ▾**
```
RESOURCES ▾
├─ Units     →  (Arrow icon showing connection)
├─ Lessons   →
└─ Handouts  →
```

**On hover:** Shows visual arrow/line connecting items (fancy component!)

**On click:** 
- `/units` → Browse all units (beautiful grid)
- `/lessons` → Browse all lessons (beautiful grid)
- `/handouts` → Browse all handouts (beautiful grid)

---

### **2. Curriculum ▾**
```
CURRICULUM ▾
├─ NZ Curriculum Overview
├─ Mathematics
├─ Science
├─ English
├─ Social Sciences
├─ Digital Technologies
├─ Te Reo Māori
├─ Arts
└─ Health & PE
```

**Links to:**
- `/curriculum` → Overview page
- `/curriculum/mathematics` → Math curriculum document (updated as MoE updates!)
- `/curriculum/science` → Science curriculum document
- etc.

**These are static pages** with official curriculum content, kept up-to-date.

---

### **3. Games** (Single link, no dropdown)
```
GAMES → /games
```

Educational games collection page

---

### **4. AI Generator** (Single link, no dropdown)
```
AI GENERATOR → /ai-generator
```

Lesson planner tool (GLM-4.6 integration)

---

### **5. Other ▾**
```
OTHER ▾
├─ Assessments
├─ Professional Development
├─ Worksheets
├─ Activities
└─ Templates
```

**Links to:**
- `/assessments` → Assessment resources
- `/professional-development` → PD resources
- `/worksheets` → Worksheet library
- etc.

---

### **6. Third Party ▾**
```
THIRD PARTY ▾
├─ Education NZ ↗
├─ NZQA ↗
├─ TKI - Te Kete Ipurangi ↗
├─ Kahoot! ↗
├─ Quizlet ↗
├─ Educreations ↗
└─ Google Classroom ↗
```

**External links** (open in new tab) to useful teacher sites

---

### **7. Login / User Avatar**

**Before login:**
```
[Login] → Clean button
```

**After login:**
```
[👤 Avatar ▾]
├─ Dashboard
├─ Saved Resources
├─ Account Settings
└─ Logout
```

---

## 📐 **BROWSE PAGES - Clean & Simple**

### **Units Page `/units`**

```
┌─────────────────────────────────────────────┐
│ UNITS                                       │
│ 654 complete unit plans                     │
└─────────────────────────────────────────────┘
│ FILTERS                                     │
│ [All Years ▾] [All Subjects ▾]             │
└─────────────────────────────────────────────┘
│                                             │
│ GRID (Masonry, beautiful cards)             │
│ ┌──────┐ ┌──────┐ ┌──────┐                │
│ │ Y8   │ │ Y9   │ │ Y7   │                │
│ │Digita│ │Ecolog│ │Algebr│                │
│ │🌟🌟🌟│ │🌟🌟🌟│ │🌟🌟🌟│                │
│ └──────┘ └──────┘ └──────┘                │
│                                             │
│ [Showing 654 units]                         │
│ NO INFINITE SCROLL                          │
│ ALL visible with filters                    │
│                                             │
└─────────────────────────────────────────────┘
```

**Same pattern for:**
- `/lessons` (3,109 lessons)
- `/handouts` (2,109 handouts)

**Filters narrow it down.** All results visible. Simple.

---

## 🎯 **INDIVIDUAL RESOURCE PAGE**

### **Lesson Page `/lessons/[slug]`**

```
┌─────────────────────────────────────────────┐
│ Y8 Geometry & Kōwhaiwhai Patterns          │
│ Mathematics | Year 8 | Quality: 🌟🌟🌟🌟🌟│
│                                             │
│ [💾 Save] [🖨️ Print] [📥 Download PDF]    │
└─────────────────────────────────────────────┘
│                                             │
│ CONTENT                                     │
│ (Beautiful typography)                      │
│ (Let the lesson content shine)              │
│                                             │
│ • Learning objectives                       │
│ • Cultural context                          │
│ • Activities                                │
│ • Assessment                                │
│                                             │
└─────────────────────────────────────────────┘
│ RELATED (GraphRAG - 3 max)                  │
│ • Y7 Patterns (prerequisite)                │
│ • Y9 Transformations (next)                 │
│ • Kōwhaiwhai Handout (companion)           │
└─────────────────────────────────────────────┘
```

Clean. Focused. Let the content be the star.

---

## 🔐 **SAAS FLOW - Login-First**

```
VISITOR
└─> Homepage (gorgeous, minimal)
    └─> Click "Login" or any resource link
        └─> Redirected to /login
            └─> "Don't have an account? Start free trial"
                └─> /register
                    └─> 14-day trial starts
                        └─> /dashboard (full access!)
                            └─> Day 14: Soft prompt to subscribe
                                └─> /pricing → Stripe
                                    └─> Subscribed (seamless!)
```

**Key:** Everything is gated. Homepage is beautiful but you need to login to access content.

---

## 📊 **COMPLETE ROUTE MAP**

```
PUBLIC (No auth)
├── /                        Homepage (gorgeous, dynamic)
├── /login                   Login form
├── /register                Signup form
└── /pricing                 Pricing page

CONTENT (Auth required)
├── /units                   Browse all units (grid + filters)
├── /units/[slug]            Individual unit
├── /lessons                 Browse all lessons
├── /lessons/[slug]          Individual lesson
├── /handouts                Browse all handouts
└── /handouts/[slug]         Individual handout

CURRICULUM (Public or auth - TBD)
├── /curriculum              Overview
└── /curriculum/[subject]    Subject-specific curriculum doc

TOOLS (Auth required)
├── /games                   Educational games
├── /ai-generator            AI lesson planner
├── /assessments             Assessment resources
├── /professional-development PD resources
├── /worksheets              Worksheet library
├── /activities              Activity resources
└── /templates               Template resources

THIRD PARTY (Public)
└── /resources/third-party   Curated external links

USER (Auth required)
├── /dashboard               Personal dashboard (role-based)
├── /saved                   Saved resources list
└── /account                 Settings + subscription
```

**TOTAL: ~20 unique routes** (rest are dynamic `[slug]` variations)

---

## ✅ **THIS IS IT - Final Vision**

**Simple:**
- Clean header navigation (dropdowns with fancy hover effects)
- Gorgeous homepage (changes weekly, minimal text)
- Browse pages (beautiful grids with simple filters)
- Resource pages (content shines, 3 actions max)
- Login-first SaaS model

**Professional:**
- Next.js 14 (instant transitions)
- Framer Motion (smooth animations)
- Kehinde Wiley design (regal, gorgeous)
- GraphRAG intelligence (subtle, helpful)

**NO:**
- ❌ Infinite scroll
- ❌ 15 different dashboards  
- ❌ Complex workspace features
- ❌ Overwhelming options
- ❌ Sidebars competing with content

**Approve this and I'll start building the Next.js prototype?**

