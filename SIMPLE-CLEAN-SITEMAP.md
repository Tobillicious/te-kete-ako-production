# 🎯 SIMPLE CLEAN SITEMAP - Essential Only

**Philosophy:** Less is more. Quality over quantity. Clear over clever.

---

## 📐 **COMPLETE SITE STRUCTURE**

```
tekete.co.nz/

PUBLIC (Not Logged In)
├── /                    → Landing page (hero + login CTA)
├── /pricing             → Simple pricing (Individual $15, School $499)
├── /login               → Clean login form
└── /register            → Clean signup (teacher/student toggle)

AUTHENTICATED (Logged In)
├── /dashboard           → Personal home (role-based: teacher or student)
│
├── /browse              → THE MAIN CONTENT BROWSER
│   ├── Default view: All resources, beautiful grid
│   ├── Filters: Year (7-13), Subject (12), Type (Lesson/Unit/Handout)
│   └── That's it. Simple.
│
├── /lessons/[slug]      → Individual lesson page
├── /units/[slug]        → Individual unit page  
├── /handouts/[slug]     → Individual handout page
│
├── /saved               → My saved resources (simple list)
│
└── /account             → Settings + subscription
```

**TOTAL:** 10 routes. That's it.

---

## 🎯 **PAGE BREAKDOWN**

### **1. Homepage `/` (Public)**

**One Purpose:** Get teachers to click "Start Free Trial"

```
┌─────────────────────────────────────┐
│                                     │
│        TE KETE AKO                  │
│   3,500+ Teaching Resources         │
│   For Aotearoa Educators            │
│                                     │
│   [Start 14-Day Free Trial]         │
│   [Login]                           │
│                                     │
└─────────────────────────────────────┘
```

**That's it.** No bloat, no feature lists, no testimonials. Just beautiful and clear.

---

### **2. Pricing `/pricing` (Public)**

**One Purpose:** Show pricing, start trial

```
┌─────────────────────────────────────┐
│                                     │
│   Individual Teacher                │
│   $15 NZD/month                     │
│   14-day free trial                 │
│   [Start Trial]                     │
│                                     │
│   School License                    │
│   $499 NZD/year                     │
│   Up to 50 teachers                 │
│   30-day free trial                 │
│   [Contact Us]                      │
│                                     │
└─────────────────────────────────────┘
```

Simple. Professional. Clear.

---

### **3. Dashboard `/dashboard` (Auth)**

**Teacher View:**
```
┌──────────┬──────────────────────────┐
│ SIDEBAR  │  DASHBOARD               │
│          │                          │
│ 🏠 Home  │  Kia ora, [Name]        │
│ 🔍 Browse│                          │
│ 💾 Saved │  This Week:             │
│ ⚙️ Account│  Monday 9am: Y9 Math    │
│          │  Tuesday 1pm: Y8 Science │
│          │  [+ Add lesson]          │
│          │                          │
│          │  Recent:                 │
│          │  • Y8 Geometry (Oct 24)  │
│          │  • Y9 Ecology (Oct 23)   │
│          │                          │
│          │  Recommended: (GraphRAG!)│
│          │  [3 lesson cards]        │
│          │                          │
└──────────┴──────────────────────────┘
```

**Student View:**
```
┌──────────┬──────────────────────────┐
│ SIDEBAR  │  DASHBOARD               │
│          │                          │
│ 🏠 Home  │  Kia ora, [Name]        │
│ 📚 Learn │                          │
│ 🎯 Tasks │  Your Assignments:       │
│ 🏆 Badges│  • Algebra worksheet     │
│          │  • Science project       │
│          │                          │
│          │  Progress:               │
│          │  Math: ████░░ 60%        │
│          │  Science: ██████░ 80%    │
│          │                          │
└──────────┴──────────────────────────┘
```

Clean. Age-appropriate. Focused.

---

### **4. Browse `/browse` (Auth - THE MAIN PAGE)**

**One Purpose:** Find any resource quickly

```
┌─────────────────────────────────────────────┐
│ 🔍 Search...                                │
│ [Year ▾] [Subject ▾] [Type ▾] [Quality ▾]  │
└─────────────────────────────────────────────┘
│                                             │
│ RESOURCES (Beautiful masonry grid)          │
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐       │
│ │ Y8   │ │ Y9   │ │ Y7   │ │ Y10  │       │
│ │Geom  │ │Stats │ │Algeb │ │Ecol  │       │
│ │🌟🌟🌟│ │🌟🌟🌟│ │🌟🌟🌟│ │🌟🌟🌟│       │
│ │Math  │ │Math  │ │Math  │ │Sci   │       │
│ └──────┘ └──────┘ └──────┘ └──────┘       │
│                                             │
│ [... beautiful grid of all resources]       │
│ [Load more as you scroll]                   │
│                                             │
└─────────────────────────────────────────────┘
```

**Features:**
- Instant client-side filtering
- Search (Cmd+K overlay)
- Save from grid
- Quality badges
- That's it!

---

### **5. Lesson Page `/lessons/[slug]` (Auth)**

**One Purpose:** Read lesson, print it, save it

```
┌─────────────────────────────────────────────┐
│ Y8 Geometry & Kōwhaiwhai Patterns          │
│ 🌟🌟🌟🌟🌟 | Mathematics | Year 8         │
│ [💾 Save] [🖨️ Print] [📥 PDF]             │
└─────────────────────────────────────────────┘
│                                             │
│ LESSON CONTENT                              │
│ (Beautiful typography, the content shines)  │
│                                             │
│ [All the lesson content here]               │
│                                             │
└─────────────────────────────────────────────┘
│ RELATED (GraphRAG - 3-5 cards max)          │
│ • Y7 Patterns (prerequisite)                │
│ • Y9 Transformations (next level)           │
│ • Cultural Patterns handout                 │
└─────────────────────────────────────────────┘
```

Simple. Let the content shine. No clutter.

---

## 🔐 **SAAS MODEL - Login-First**

### **The Flow:**

**1. Visitor Arrives**
```
Homepage → Beautiful but simple
          → One CTA: "Start Free Trial"
          → Everything else requires login
```

**2. Registers (14-day trial starts)**
```
Register → Choose role (teacher/student)
        → Email verification
        → Redirects to /dashboard
        → FULL ACCESS during trial
```

**3. Trial Period**
```
Days 1-14: Full access to everything
Day 7: Gentle email reminder
Day 12: "Trial ending soon" notice
Day 14: Redirect to /pricing on login
```

**4. Conversion**
```
Click subscribe → Stripe checkout
               → Payment success
               → Full access continues
               → No interruption
```

**5. Active Subscriber**
```
Full access → Everything unlocked
           → Clean dashboard
           → Professional tools
           → Support access
```

---

## 🗺️ **SIMPLIFIED STRUCTURE - FINAL**

```
/ (public)
  - Hero + CTA
  - No content previews
  - Login-first model

/pricing (public)
  - Two plans
  - Clear benefits
  - Start trial CTA

/login (public)
/register (public)

/dashboard (auth)
  - Teacher: This week + recommended
  - Student: Assignments + progress
  
/browse (auth) ← THE CORE APP
  - All 11,631 resources
  - Filters: Year, Subject, Type
  - Search: Instant
  - Grid: Beautiful
  
/lessons/[slug] (auth)
/units/[slug] (auth)
/handouts/[slug] (auth)
  - Just show the content
  - Print button
  - Save button
  - Related resources (3-5 max)

/saved (auth)
  - List of saved resources
  - Simple, clean
  
/account (auth)
  - Profile
  - Subscription
  - Settings
```

**TOTAL:** 10 routes, maximum clarity.

---

## 🎨 **DESIGN PRINCIPLE**

**Every page has ONE job:**
- Homepage: Get signup
- Pricing: Show value
- Dashboard: Quick access to what's needed today
- Browse: Find resources fast
- Lesson: Read/print/save
- Saved: Access saved resources
- Account: Manage subscription

**No page tries to do everything.**

---

## 💎 **WHY THIS WORKS FOR TEACHERS**

**Teacher Journey:**
1. Lands on homepage (beautiful, simple)
2. Starts trial (2-minute signup)
3. Goes to dashboard (sees recommended)
4. Browses resources (finds what they need)
5. Saves favorites (builds their collection)
6. Uses resources (prints, downloads)
7. Subscribes (after trial, seamless)

**Student Journey:**
1. Teacher gives login
2. Sees assignments
3. Completes work
4. Tracks progress
5. Done. (No complexity!)

---

## 🚀 **NEXT.JS ROUTING - CLEAN**

```typescript
/app
├── (public)
│   ├── page.tsx              // Homepage
│   ├── pricing/page.tsx
│   ├── login/page.tsx
│   └── register/page.tsx
│
├── (app)                      // Protected group
│   ├── dashboard/page.tsx     // Role-based
│   ├── browse/page.tsx        // Main browser
│   ├── saved/page.tsx         // Saved resources
│   ├── account/page.tsx       // Settings + billing
│   └── layout.tsx             // Sidebar layout
│
└── [type]/[slug]/page.tsx     // Dynamic: lessons/units/handouts
```

**That's it. Clean. Simple. Professional.**

---

## ✅ **APPROVAL NEEDED**

Is THIS the right level of simplicity?

**Keep:**
- ✅ Beautiful design (Kehinde Wiley + BMAD)
- ✅ Next.js + React + Framer Motion
- ✅ GraphRAG intelligence (subtle, not overwhelming)
- ✅ Simple navigation (5 sidebar links max)
- ✅ Login-first SaaS model

**Remove:**
- ❌ 15 different dashboards
- ❌ Complex workspace tools
- ❌ AI feature showcase pages
- ❌ Multiple browse interfaces
- ❌ Everything that isn't essential

**YES or need more simplification?**

