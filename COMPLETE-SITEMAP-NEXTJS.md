# 🗺️ COMPLETE SITEMAP - Next.js Architecture for Teachers

**Data-Driven Design Based on GraphRAG:**
- 11,631 active resources (avg quality 85.96)
- 3,109 Lessons, 2,109 Handouts, 654 Units
- 12 subjects, 24 year levels
- 1,190,295 relationships (intelligence goldmine!)

---

## 📐 **SITE ARCHITECTURE - Teacher-First Design**

```
tekete.co.nz/
│
├── 🌐 PUBLIC (Marketing - Not Logged In)
│   ├── / (Homepage - gorgeous hero + Top 10)
│   ├── /about
│   ├── /pricing (Stripe integration)
│   ├── /demo (Interactive preview for trials)
│   ├── /contact
│   ├── /login
│   ├── /register (role detection: teacher/student)
│   └── /help
│
├── 🧑‍🏫 /app (Teacher Workspace - Auth Required)
│   │
│   ├── /dashboard (Teacher Home)
│   │   ├── Quick Actions (Emergency Lesson, Plan Week, AI Assistant)
│   │   ├── My Classes (from KAMAR or manual)
│   │   ├── Recent Resources
│   │   ├── This Week's Plan
│   │   ├── Student Progress Overview
│   │   └── Recommended For You (GraphRAG!)
│   │
│   ├── /search (Command+K interface, Algolia + GraphRAG)
│   │   ├── Instant results (<50ms)
│   │   ├── Filters: Year, Subject, Type, Quality
│   │   ├── Semantic discovery (relationship-based)
│   │   └── Save searches (persistent)
│   │
│   ├── /discover (GraphRAG Intelligence Hub)
│   │   ├── /pathways (Learning progressions Y7→Y13)
│   │   ├── /related (Relationship explorer)
│   │   ├── /excellence (Top 621 gold-standard)
│   │   └── /cultural (Mātauranga Māori integration)
│   │
│   ├── /browse (Organized Discovery)
│   │   ├── /by-subject (12 canonical subjects)
│   │   ├── /by-year (7-13 + NCEA)
│   │   ├── /by-type (Lessons, Units, Handouts)
│   │   └── /by-topic (cross-curricular themes)
│   │
│   ├── /workspace (Teacher Tools)
│   │   ├── /my-kete (Saved resources - Supabase!)
│   │   ├── /planner (Weekly/term planning)
│   │   ├── /classes (Manage student groups)
│   │   ├── /assignments (Create & track)
│   │   └── /progress (Student tracking)
│   │
│   ├── /ai (AI-Powered Tools - GLM Integration)
│   │   ├── /lesson-planner (GLM-4.6 200K context)
│   │   ├── /image-generator (CogView-4)
│   │   ├── /pronunciation (GLM-4-Voice for te reo)
│   │   ├── /assistant (Chat with AI about teaching)
│   │   └── /content-enhancer (Improve existing lessons)
│   │
│   └── /account
│       ├── /settings (Profile, preferences)
│       ├── /subscription (Billing, upgrade)
│       ├── /kamar (KAMAR integration setup)
│       └── /analytics (Usage stats)
│
├── 👨‍🎓 /student (Student Workspace - Auth Required)
│   ├── /dashboard (Student home - age-appropriate)
│   ├── /my-learning (Current lessons, progress)
│   ├── /achievements (Gamification, badges)
│   ├── /assignments (From teacher)
│   └── /resources (Browse available content)
│
├── 📚 /subjects (Subject Hubs - Public Preview, Full Access Requires Login)
│   ├── /mathematics (1,107 resources)
│   │   ├── Top 50 showcase
│   │   ├── By Year (7-13)
│   │   ├── By Topic (Algebra, Geometry, Statistics, etc.)
│   │   └── Learning Pathways (GraphRAG prerequisite chains)
│   │
│   ├── /science (916 resources)
│   │   ├── Top 50 showcase
│   │   ├── By Year (7-13)
│   │   ├── By Topic (Biology, Chemistry, Physics, etc.)
│   │   └── Cultural Integration (Mātauranga Māori science)
│   │
│   ├── /english (742 resources)
│   ├── /social-studies (538 resources)
│   ├── /digital-technologies (2,344 resources!) 
│   ├── /te-ao-maori (514 resources)
│   ├── /te-reo-maori (2 resources - needs growth!)
│   ├── /health-pe (356 resources)
│   ├── /arts (35 resources)
│   └── /cross-curricular (2,783 resources!)
│
├── 📖 /lessons (Dynamic Content - Auth Required)
│   ├── /[slug] (Individual lesson pages)
│   │   ├── Lesson content (beautiful typography)
│   │   ├── Download PDF
│   │   ├── Print optimized
│   │   ├── Related lessons (GraphRAG!)
│   │   ├── Prerequisites chain
│   │   ├── Assign to class
│   │   └── Save to My Kete
│   │
│   └── /browse
│       ├── All lessons grid (3,109 total)
│       ├── Filters (year, subject, quality)
│       └── Sort (quality, date, cultural%)
│
├── 📦 /units (Unit Plans - Auth Required)
│   ├── /[slug] (Individual unit pages)
│   │   ├── Unit overview
│   │   ├── Lesson sequence (clickable)
│   │   ├── Assessment tools
│   │   ├── Cultural integration
│   │   └── Download complete unit
│   │
│   └── /browse (654 total units)
│
├── 📄 /handouts (Worksheets - Auth Required)
│   ├── /[slug] (Individual handout pages)
│   │   ├── Preview
│   │   ├── Download (PDF, editable DOCX)
│   │   ├── Print
│   │   └── Attach to assignment
│   │
│   └── /browse (2,109 total handouts)
│
├── 🎯 /quick (Emergency & High-Value)
│   ├── /emergency (Print-ready lessons in <2 min)
│   ├── /top-10 (Starter pack)
│   ├── /top-50 (Best resources by subject)
│   └── /new (Recently added)
│
├── 🏫 /school (School Admins - School License Only)
│   ├── /dashboard (School-wide overview)
│   ├── /teachers (Manage teacher accounts)
│   ├── /students (Bulk import from KAMAR)
│   ├── /analytics (School-wide usage)
│   ├── /kamar (Integration dashboard)
│   └── /billing (School subscription)
│
└── 🔧 /admin (Platform Admin - Admin Role Only)
    ├── /graphrag (GraphRAG management)
    ├── /content (Content moderation)
    ├── /users (User management)
    ├── /analytics (Platform metrics)
    └── /system (Health monitoring)
```

---

## 🎯 **KEY PAGES - Detailed Specs**

### **1. Homepage `/` (Public)**

**Purpose:** Convert visitors → trial signups in 30 seconds

**Layout:**
```
┌─────────────────────────────────────────────┐
│ HERO (3D Koru Background)                   │
│ "Te Kete Ako"                               │
│ "3,500+ Professional Teaching Resources"    │
│ [Start 14-Day Free Trial] [Browse Demo]     │
└─────────────────────────────────────────────┘
│ TOP 10 STARTER PACK                         │
│ [10 beautiful cards with quality badges]    │
└─────────────────────────────────────────────┘
│ FOR TEACHERS                                │
│ • Emergency Lessons (2-min print)           │
│ • AI Lesson Planner ($500K value!)          │
│ • KAMAR Integration                         │
│ • Cultural Resources (100% integrated)      │
└─────────────────────────────────────────────┘
│ PRICING (Simple)                            │
│ Individual $15/mo | School $499/yr          │
└─────────────────────────────────────────────┘
│ SOCIAL PROOF                                │
│ "1,200+ NZ teachers" testimonials           │
└─────────────────────────────────────────────┘
```

**Features:**
- Framer Motion page entrance
- 3D koru background (Three.js)
- Scroll-triggered animations (GSAP)
- Instant search (Cmd+K anywhere)

---

### **2. Teacher Dashboard `/app/dashboard` (Auth)**

**Purpose:** Everything a teacher needs in one glance

**Layout:**
```
┌─────────────┬───────────────────────────────┐
│  SIDEBAR    │  MAIN DASHBOARD               │
│             │                               │
│ 👤 Profile  │  🌿 Kia ora, [Name]!         │
│             │                               │
│ ⚡ Quick    │  📊 THIS WEEK                │
│ • Emergency │  ┌─────┬─────┬─────┬─────┐  │
│ • Top 10    │  │ Mon │ Tue │ Wed │ Thu │  │
│             │  │ 3 P │ 2 P │ 4 P │ 3 P │  │
│ 📚 Browse   │  └─────┴─────┴─────┴─────┘  │
│ • Lessons   │                               │
│ • Units     │  🎯 QUICK ACTIONS            │
│ • Handouts  │  [🚨 Emergency] [📝 Plan]    │
│             │  [🤖 AI Help] [👥 Classes]   │
│ 🎓 Subjects │                               │
│ • Math      │  📈 MY STATS                 │
│ • Science   │  • 42 students active        │
│ • English   │  • 18 lessons this month     │
│ • +9 more   │  • 156 resources saved       │
│             │                               │
│ 🌺 Cultural │  💡 RECOMMENDED FOR YOU      │
│ • Te Reo    │  (GraphRAG-powered cards!)   │
│ • Māori     │                               │
│             │  📅 UPCOMING                 │
│ 🤖 AI Tools │  • Y9 Science tomorrow 9am   │
│ • Planner   │  • Y8 Math Friday P3         │
│ • Images    │                               │
│             │  🎓 MY CLASSES               │
│ 👤 Account  │  • 9MAT (24 students)        │
│ • Settings  │  • 10SCI (28 students)       │
│ • Billing   │  [View all →]                │
└─────────────┴───────────────────────────────┘
```

**Features:**
- Real-time data (Supabase Realtime!)
- Smooth animations (every stat counts up!)
- GraphRAG recommendations
- KAMAR timetable integration
- One-click to any resource

---

### **3. Subject Hub `/subjects/mathematics` (Hybrid)**

**Purpose:** Browse 1,107 math resources with intelligent discovery

**Layout:**
```
┌─────────────────────────────────────────────┐
│ HERO                                        │
│ "📐 Mathematics" (Kehinde Wiley gold!)     │
│ "1,107 culturally integrated resources"    │
└─────────────────────────────────────────────┘
│ FILTERS (Sticky)                            │
│ [Year: All ▾] [Topic: All ▾] [Quality: 90+]│
└─────────────────────────────────────────────┘
│ TOP 50 EXCELLENCE (Masonry grid)            │
│ ┌─────┐ ┌─────┐ ┌─────┐                   │
│ │ Y7  │ │ Y8  │ │ Y9  │ (Quality badges) │
│ │Algeb│ │Geom │ │Stats│  🌟🌟🌟🌟🌟       │
│ │ ra  │ │ etry│ │     │                   │
│ └─────┘ └─────┘ └─────┘                   │
│ [... 47 more cards, beautifully laid out]  │
└─────────────────────────────────────────────┘
│ LEARNING PATHWAYS (GraphRAG!)               │
│ Y7 Foundation → Y8 Building → Y9 Mastery   │
│ (Visual prerequisite chains)                │
└─────────────────────────────────────────────┘
│ BROWSE ALL (Infinite scroll)                │
│ Remaining 1,057 resources                   │
└─────────────────────────────────────────────┘
```

**Features:**
- Instant filtering (client-side after SSR)
- Masonry layout (Pinterest-style)
- GraphRAG relationship visualization
- Save directly from hub
- Print multiple selections

---

### **4. Lesson Page `/lessons/[slug]` (Auth)**

**Purpose:** Beautiful, printable, useful lesson with intelligent discovery

**Layout:**
```
┌─────────────────────────────────────────────┐
│ HERO IMAGE (Parallax)                       │
│ "Y8 Geometry & Kōwhaiwhai Patterns"        │
│ 🌟🌟🌟🌟🌟 Excellence | 🌿 100% Cultural  │
└─────────────────────────────────────────────┘
│ ACTIONS                                     │
│ [💾 Save] [🖨️ Print] [📥 Download] [➡️ Assign]│
└─────────────────────────────────────────────┘
│ WHAKATAUKĪ (Animated card)                 │
│ "Ko te manu e kai ana i te miro..."        │
└─────────────────────────────────────────────┘
│ LESSON CONTENT (Beautiful typography)       │
│ • Learning Objectives                       │
│ • Success Criteria                          │
│ • Cultural Context                          │
│ • Activities (interactive where possible!)  │
│ • Assessment Tools                          │
│ • Teacher Notes                             │
└─────────────────────────────────────────────┘
│ PREREQUISITES (GraphRAG chain!)             │
│ Start here ← Y7 Patterns ← Y8 Geometry     │
└─────────────────────────────────────────────┘
│ RELATED RESOURCES (828K relationships!)     │
│ • Similar lessons (same_subject)            │
│ • Cross-curricular (cross_curricular_bridge)│
│ • Next in sequence (learning_sequence)      │
│ • Cultural connections (shared_cultural)    │
└─────────────────────────────────────────────┘
│ COMMENTS & SHARING (Teacher community)      │
│ • Teacher notes (shared with school)        │
│ • Modifications (teaching variants!)        │
│ • Ratings & feedback                        │
└─────────────────────────────────────────────┘
```

**Features:**
- Server Component (instant load!)
- Markdown rendering (beautiful!)
- Print CSS perfection
- GraphRAG-powered discovery sidebar
- Save with notes (Supabase)
- Assign to class (one click!)

---

### **5. Search `/app/search` (Auth)**

**Purpose:** Find anything in <2 seconds, discover related

**Layout:**
```
┌─────────────────────────────────────────────┐
│ COMMAND PALETTE (Cmd+K from anywhere!)      │
│ 🔍 Search 3,500+ resources...              │
└─────────────────────────────────────────────┘
│ INSTANT RESULTS (Algolia <50ms)             │
│ ┌─────────────────────────────────────────┐ │
│ │ Y8 Geometry & Kōwhaiwhai 🌟🌟🌟🌟🌟     │ │
│ │ Mathematics • Year 8 • Lesson            │ │
│ │ "Explore geometric patterns in Māori..." │ │
│ └─────────────────────────────────────────┘ │
│ [... 20 more instant results]               │
└─────────────────────────────────────────────┘
│ SMART FILTERS                               │
│ [Year ▾] [Subject ▾] [Type ▾] [Quality ▾]  │
└─────────────────────────────────────────────┘
│ RELATED SEARCHES (GraphRAG)                 │
│ • "Māori patterns in math"                  │
│ • "Cultural geometry lessons"               │
│ • "Year 7-8 progression"                    │
└─────────────────────────────────────────────┘
│ DISCOVERY (If no exact match)               │
│ "Did you mean...?" (semantic suggestions)   │
│ "Teachers also searched for..."             │
└─────────────────────────────────────────────┘
```

**Features:**
- Algolia InstantSearch
- GraphRAG semantic layer
- Keyboard shortcuts (↑↓ navigate, Enter select)
- Recent searches (persisted)
- Save search (for repeating needs)

---

### **6. AI Lesson Planner `/app/ai/lesson-planner` (Auth)**

**Purpose:** Generate complete lesson plan in 60 seconds

**Layout:**
```
┌─────────────────────────────────────────────┐
│ 🤖 AI LESSON PLANNER                       │
│ Powered by GLM-4.6 (200K context)           │
└─────────────────────────────────────────────┘
│ INPUT FORM (Beautiful, step-by-step)        │
│ ┌─────────────────────────────────────────┐ │
│ │ Step 1: What are you teaching?          │ │
│ │ Subject: [Mathematics ▾]                 │ │
│ │ Year: [8 ▾]                              │ │
│ │ Topic: [Geometry & Patterns]             │ │
│ │                                          │ │
│ │ Step 2: Cultural integration level       │ │
│ │ ○ Light  ● Deep  ○ Complete             │ │
│ │                                          │ │
│ │ Step 3: Your class context (optional)    │ │
│ │ Class size: [24]                         │ │
│ │ Ability: [Mixed ▾]                       │ │
│ │ Special needs: [...]                     │ │
│ │                                          │ │
│ │ [✨ Generate Lesson Plan]               │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
│ GENERATED PLAN (Streaming!)                 │
│ Watch it generate in real-time...           │
│ • Learning objectives ✓                     │
│ • Cultural connections (appearing...)       │
│ • Activities (generating...)                │
│ • Assessment tools (pending...)             │
└─────────────────────────────────────────────┘
│ ACTIONS                                     │
│ [💾 Save to My Kete] [📝 Edit] [🖨️ Print] │
└─────────────────────────────────────────────┘
```

**Features:**
- GLM-4.6 streaming (watch it write!)
- Uses GraphRAG for context (pulls related resources!)
- Beautiful markdown output
- Save directly to My Kete
- Edit before saving

---

### **7. Weekly Planner `/app/workspace/planner` (Auth)**

**Purpose:** Plan entire week in 10 minutes

**Layout:**
```
┌─────────────────────────────────────────────┐
│ 📅 WEEK OF OCT 28, 2025                    │
│ [← Prev Week] [Today] [Next Week →]        │
└─────────────────────────────────────────────┘
│ TIMETABLE (Drag & Drop!)                    │
│ ┌──────┬──────┬──────┬──────┬──────┐       │
│ │ MON  │ TUE  │ WED  │ THU  │ FRI  │       │
│ ├──────┼──────┼──────┼──────┼──────┤       │
│ │ P1   │ P1   │ P1   │ P1   │ P1   │       │
│ │ 9MAT │ 10SCI│ 9MAT │ 10SCI│ 9MAT │       │
│ │[Drop]│[Drop]│[Drop]│[Drop]│[Drop]│       │
│ ├──────┼──────┼──────┼──────┼──────┤       │
│ │ P2   │ P2   │ ...  │ ...  │ ...  │       │
│ └──────┴──────┴──────┴──────┴──────┘       │
└─────────────────────────────────────────────┘
│ RESOURCE BANK (Drag from here!)             │
│ 📚 Saved Lessons | 🔍 Search | ⭐ Top 50   │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│ │ Algebra │ │Geometry │ │ Stats   │ DRAG  │
│ │ Y9 Q:95 │ │ Y8 Q:92 │ │ Y9 Q:90 │  →    │
│ └─────────┘ └─────────┘ └─────────┘       │
└─────────────────────────────────────────────┘
│ PREP STATUS                                 │
│ ✅ Monday fully planned (4/4 periods)      │
│ ⚠️ Tuesday needs 1 lesson (P3)             │
│ 📝 Wednesday needs planning                 │
└─────────────────────────────────────────────┘
```

**Features:**
- KAMAR auto-import (timetable syncs!)
- Drag & drop lessons
- Auto-saves (Supabase Realtime)
- Print week view
- Share with colleagues (collaboration!)

---

### **8. My Kete `/app/workspace/my-kete` (Auth)**

**Purpose:** Personal resource library (like Notion!)

**Layout:**
```
┌─────────────────────────────────────────────┐
│ 📚 MY KETE                                  │
│ 156 saved resources                         │
└─────────────────────────────────────────────┘
│ FOLDERS (Drag to organize!)                 │
│ 📁 This Week (12)                           │
│ 📁 Algebra Unit (8)                         │
│ 📁 Emergency Backups (15)                   │
│ 📁 Cultural Excellence (23)                 │
│ 📁 To Try Next Term (42)                    │
│ + New Folder                                │
└─────────────────────────────────────────────┘
│ RESOURCES (Grid or List view)               │
│ ┌─────────────────────────────────────────┐ │
│ │ 🌟🌟🌟🌟🌟 Y8 Geometry               │ │
│ │ Saved: Oct 24 | Used: 3 times            │ │
│ │ Notes: "Students loved the koru part!" │ │
│ │ Tags: #cultural #geometry #year8         │ │
│ │ [Open] [Edit Notes] [Print] [Remove]     │ │
│ └─────────────────────────────────────────┘ │
│ [... more saved resources]                  │
└─────────────────────────────────────────────┘
│ SMART COLLECTIONS (Auto-generated!)         │
│ • Recently Used (last 7 days)               │
│ • Highly Rated (you gave 5★)               │
│ • Never Used (maybe try these?)            │
│ • Similar to X (GraphRAG!)                  │
└─────────────────────────────────────────────┘
```

**Features:**
- Supabase database (not localStorage!)
- Folders (organize however you want)
- Notes per resource
- Tags (auto + custom)
- Search within kete
- Export collection (PDF of all!)

---

## 🎨 **DESIGN SYSTEM - Complete Spec**

### **Color Palette (Kehinde Wiley + BMAD Synthesis):**

```typescript
colors: {
  // Kehinde Wiley Regal
  royal: {
    blue: '#003366',
    purple: '#4B0082',
    gold: '#FFD700',
    crimson: '#DC143C',
    emerald: '#006A4E',
  },
  
  // BMAD Cultural (Māori authentic)
  pounamu: '#1B6B42',  // Greenstone
  kowhai: '#F5D915',   // Golden bloom
  moana: '#006994',    // Ocean
  whenua: '#8B4513',   // Earth
  kumara: '#FF6B35',   // Fire
  
  // Neutrals (Warm, not cold!)
  neutral: {
    50: '#fafaf9',     // Warm white
    100: '#f5f1eb',    // Earth cream (BMAD default background!)
    500: '#78716c',    // Warm gray
    900: '#292524',    // Warm black
  },
}
```

### **Typography (Museum-Quality):**

```typescript
fontFamily: {
  display: ['Freight Display Pro', 'Playfair Display', 'serif'],
  heading: ['Söhne', 'Inter', 'sans-serif'],
  body: ['Inter Variable', 'system-ui', 'sans-serif'],
  cultural: ['Tauri', 'Georgia', 'serif'], // Māori characters
  code: ['Berkeley Mono', 'Consolas', 'monospace'],
}

fontSize: {
  'hero': ['4.5rem', { lineHeight: '1', letterSpacing: '-0.02em' }],
  '4xl': ['3.5rem', { lineHeight: '1.1' }],
  '3xl': ['2.5rem', { lineHeight: '1.2' }],
  // ... Kehinde Wiley bold scale
}
```

### **Spacing (Marae-inspired - GENEROUS):**

```typescript
spacing: {
  'marae-xs': '1rem',    // 16px
  'marae-sm': '2rem',    // 32px  
  'marae-md': '4rem',    // 64px - section breathing
  'marae-lg': '6rem',    // 96px - major sections
  'marae-xl': '10rem',   // 160px - hero spacing
}
```

---

## 🔐 **AUTHENTICATION FLOW**

### **Simplified Journey:**

```
┌─────────────────────────────────────────────┐
│ VISITOR                                     │
│ └→ Homepage (public, gorgeous)              │
│    └→ [Start Free Trial] button             │
│       └→ Register page                      │
│          ├→ "I'm a Teacher" → Role: teacher │
│          └→ "I'm a Student" → Role: student │
│             └→ Supabase signup              │
│                └→ Email verification        │
│                   └→ AUTHENTICATED          │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ TEACHER (authenticated)                     │
│ ├→ /app/dashboard (default landing)         │
│ ├→ Sidebar always visible                   │
│ ├→ All content unlocked during trial        │
│ ├→ After 14 days → Stripe checkout          │
│ └→ Subscription active → Full access        │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ STUDENT (authenticated)                     │
│ ├→ /student/dashboard (age-appropriate)     │
│ ├→ Assignments from teacher                 │
│ ├→ Progress tracking                        │
│ ├→ Achievements & badges                    │
│ └→ Simplified UI (no pricing!)              │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│ SCHOOL ADMIN (school license)               │
│ ├→ /school/dashboard                        │
│ ├→ Manage 50 teacher accounts               │
│ ├→ Bulk student import (KAMAR!)             │
│ ├→ School-wide analytics                    │
│ └→ Billing management                       │
└─────────────────────────────────────────────┘
```

### **Middleware (Next.js 14):**

```typescript
// middleware.ts - Handle all auth routing
export async function middleware(request: NextRequest) {
  const { data: { session } } = await supabase.auth.getSession()
  
  // Public routes (no auth needed)
  if (isPublicRoute(request)) {
    return NextResponse.next()
  }
  
  // Protected routes (require auth)
  if (!session) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  
  // Role-based routing
  const { role } = session.user.user_metadata
  
  if (request.nextUrl.pathname === '/app') {
    // Default dashboard based on role
    if (role === 'teacher') {
      return NextResponse.rewrite(new URL('/app/dashboard', request.url))
    } else if (role === 'student') {
      return NextResponse.rewrite(new URL('/student/dashboard', request.url))
    } else if (role === 'school_admin') {
      return NextResponse.rewrite(new URL('/school/dashboard', request.url))
    }
  }
  
  // Check subscription status for premium features
  if (isPremiumRoute(request)) {
    const hasActiveSubscription = await checkSubscription(session.user.id)
    
    if (!hasActiveSubscription) {
      return NextResponse.redirect(new URL('/pricing?upgrade=required', request.url))
    }
  }
  
  return NextResponse.next()
}
```

---

## 📱 **RESPONSIVE STRATEGY**

### **Breakpoints:**
```typescript
screens: {
  'phone': '375px',     // iPhone SE
  'tablet': '768px',    // iPad portrait
  'laptop': '1024px',   // Small laptop
  'desktop': '1280px',  // Desktop
  'wide': '1536px',     // Wide monitor
  'classroom': '1920px', // Classroom projector!
}
```

### **Layout Adaptations:**

**Desktop (1280px+):**
- Fixed left sidebar (280px)
- Main content (fluid)
- Discovery sidebar (320px right)
- Three-column layout

**Tablet (768-1024px):**
- Collapsible sidebar (drawer)
- Main content (full width)
- Discovery inline (below content)
- Two-column layout

**Mobile (<768px):**
- Bottom nav bar (5 icons)
- Full-width content
- Swipe gestures (cultural!)
- Single-column layout

---

## 🎯 **NAVIGATION HIERARCHY**

### **Primary Navigation (Sidebar):**
```
1. 🏠 Dashboard
2. 🔍 Search (Cmd+K)
3. 📚 Browse
   └─ Lessons
   └─ Units
   └─ Handouts
4. 🎓 Subjects (12 canonical)
5. 🌺 Cultural Hub
6. 🤖 AI Tools
7. 📅 My Workspace
   └─ My Kete
   └─ Planner
   └─ Classes
8. 👤 Account
```

### **Contextual Navigation (Per Page):**
- **Breadcrumbs** (hierarchical path)
- **Related Resources** (GraphRAG sidebar)
- **Prerequisites** (below content)
- **Quick Actions** (floating action button on mobile)

---

## 🚀 **TECHNICAL ROUTING**

### **Next.js App Router Structure:**

```
/app
├── (marketing)          # Public group
│   ├── page.tsx         # Homepage
│   ├── about/page.tsx
│   ├── pricing/page.tsx
│   └── layout.tsx       # Marketing layout
│
├── (auth)               # Auth group
│   ├── login/page.tsx
│   ├── register/page.tsx
│   └── layout.tsx       # Minimal layout
│
├── (app)                # Teacher app (protected)
│   ├── dashboard/page.tsx
│   ├── search/page.tsx
│   ├── workspace/
│   │   ├── my-kete/page.tsx
│   │   ├── planner/page.tsx
│   │   └── classes/page.tsx
│   ├── ai/
│   │   ├── lesson-planner/page.tsx
│   │   ├── image-generator/page.tsx
│   │   └── pronunciation/page.tsx
│   └── layout.tsx       # App layout (sidebar!)
│
├── subjects/
│   └── [subject]/page.tsx    # Dynamic subject hubs
│
├── lessons/
│   ├── page.tsx              # Browse all
│   └── [slug]/page.tsx       # Individual lesson
│
├── units/
│   └── [slug]/page.tsx
│
├── handouts/
│   └── [slug]/page.tsx
│
├── student/             # Student app (protected)
│   ├── dashboard/page.tsx
│   ├── my-learning/page.tsx
│   └── achievements/page.tsx
│
└── school/              # School admin (protected)
    ├── dashboard/page.tsx
    ├── teachers/page.tsx
    └── kamar/page.tsx
```

---

## 💎 **WHAT MAKES THIS PHENOMENAL**

### **For Teachers:**
1. **INSTANT** - No loading, no waiting, no frustration
2. **BEAUTIFUL** - Museum-quality design, gorgeous typography
3. **INTELLIGENT** - GraphRAG shows what you need when you need it
4. **ORGANIZED** - Everything has a logical place
5. **MOBILE-PERFECT** - Plan lessons on phone in staffroom
6. **PRINT-PERFECT** - One click → professional printout
7. **COLLABORATIVE** - Share with department, see what works
8. **AI-POWERED** - Generate lessons in 60 seconds
9. **CULTURALLY RICH** - Mātauranga Māori throughout
10. **PROFESSIONAL** - Stripe, SSO, real dashboards

### **Technical Excellence:**
- Server Components (instant page loads!)
- Edge runtime (global <50ms responses)
- Vercel Analytics (real user monitoring)
- Sentry (catch every error)
- LogRocket (see exactly what teachers see!)
- Algolia (search in <50ms)
- GraphRAG (intelligent relationships)

---

## 🎯 **NEXT STEPS**

Want me to:
1. **Start building the prototype** (initialize Next.js, build homepage)?
2. **Design more detailed wireframes** (specific page mockups)?
3. **Plan the migration strategy** (how to preserve 11,631 resources)?

**This sitemap is the foundation. Once you approve it, we build the most beautiful educational platform in the world.** 🎨✨

Ready?

