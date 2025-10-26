# ✅ THE REAL FIX - Data-Driven Reality

**Problem diagnosed: Teaching content is OK. SaaS wrapper is broken garbage.**

---

## 📊 THE ACTUAL DATA

### **What's Good (Keep):**
```
Content in GraphRAG:
- 523 Lessons (522 high quality = 99.8%)
- 517 lessons (517 high quality = 100%)
- 440 handouts (440 high quality = 100%)  
- 204 Units (204 high quality = 100%)

Total usable content: ~1,680 resources
Average quality: 94+ (actually validated in GraphRAG)
All with cultural integration marked
Organized by: Subject, Year Level, Resource Type
```

### **What's Broken (Delete):**
```
Homepage: 932 divs/sections (2,252 lines total)
- 5 different badge systems
- "AI Features - 28 Functions!"
- "GraphRAG - 14 Tools!"
- "7,391 Cultural Resources!" (false - it's 1,680)
- Multiple duplicate sections
- Broken component loaders
- Empty CSS files with comments only

Navigation: Completely broken
- Multiple conflicting loaders
- Sidebar doesn't load
- Duplicate meta tags everywhere

Current file count: 269 HTML files
Actual content files: ~1,040
Garbage/duplicate/broken: 229 files
```

---

## 🎯 THE FIX (Simple & Fast)

### **Phase 1: Clean Rebuild (3 days)**

**Step 1: New Next.js App (Day 1)**
```bash
# Fresh directory
mkdir te-kete-clean
cd te-kete-clean
npx create-next-app@latest . --typescript --tailwind --app

# Install only what we need
npm install @supabase/ssr lucide-react

# 6 files total:
1. app/page.tsx              # Homepage (clean)
2. app/browse/page.tsx       # Browse all resources
3. app/resource/[id]/page.tsx # Individual resource
4. app/layout.tsx            # Nav + Footer
5. lib/supabase.ts           # DB connection
6. components/ResourceCard.tsx # Reusable card
```

**Step 2: Connect to Existing Data (Day 2)**
```typescript
// lib/supabase.ts
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)

// Fetch from EXISTING graphrag_resources table
export async function getResources(filters = {}) {
  const { data } = await supabase
    .from('graphrag_resources')
    .select('*')
    .eq('archive_status', 'active')
    .in('resource_type', ['lesson', 'Lesson', 'unit', 'Unit', 'handout', 'Handout'])
    .gte('quality_score', 90) // Only show high quality
    .order('quality_score', { ascending: false })
  
  return data
}

// That's it. Data is already there.
```

**Step 3: Build Clean UI (Day 3)**
```typescript
// app/page.tsx - ENTIRE HOMEPAGE
export default function Home() {
  return (
    <main className="min-h-screen">
      {/* Hero */}
      <section className="bg-gradient-to-b from-emerald-50 to-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-5xl font-bold text-emerald-900 mb-4">
            Te Kete Ako
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            1,680 quality NZ teaching resources
          </p>
          
          {/* Search */}
          <SearchBar />
          
          {/* Quick Links */}
          <div className="grid md:grid-cols-3 gap-6 mt-12 max-w-3xl mx-auto">
            <Link href="/browse?type=lessons">
              <Card>
                <h3 className="text-2xl font-bold">📚 Lessons</h3>
                <p>1,040 ready to use</p>
              </Card>
            </Link>
            
            <Link href="/browse?type=units">
              <Card>
                <h3 className="text-2xl font-bold">📦 Units</h3>
                <p>204 complete units</p>
              </Card>
            </Link>
            
            <Link href="/browse?type=handouts">
              <Card>
                <h3 className="text-2xl font-bold">📄 Handouts</h3>
                <p>440 printable</p>
              </Card>
            </Link>
          </div>
        </div>
      </section>
    </main>
  )
}

// ~60 lines. Done. Clean. Fast. Works.
```

---

## 🗂️ THE MIGRATION STRATEGY

### **Content Files (Keep & Serve):**
```
Current location: /public/lessons/*.html
                 /public/units/*.html
                 /public/handouts/*.html

New strategy:
1. Keep files exactly where they are
2. Serve them statically from Next.js /public folder
3. GraphRAG table already has all metadata
4. No need to move or convert files

How it works:
- Browse page shows cards (from GraphRAG)
- Click card → redirects to /lessons/y8-algebra.html (static file)
- File already exists, works perfectly
- Zero migration needed for content
```

### **What Gets Deleted:**
```
/public/index.html → Replaced by Next.js app/page.tsx
/public/browse-*.html → Replaced by app/browse/page.tsx
/public/teacher-dashboard.html → Replaced by app/dashboard/page.tsx
/public/*-hub.html → Delete (47 hub pages = bloat)
/public/*-showcase.html → Delete (AI feature spam)
/public/navigation-*.js → Delete (broken loaders)
/css/archive/ → Delete (old CSS systems)

Keep:
/public/lessons/ → Serve statically
/public/units/ → Serve statically
/public/handouts/ → Serve statically
/public/css/te-kete-bmad-authentic.css → Maybe keep for lesson pages
```

---

## 🎨 THE CLEAN DESIGN

### **Design System (One, not five):**
```
Tailwind v4 config with custom tokens:

colors:
  pounamu: { 50-900 green scale }
  kowhai: { 50-900 gold scale }
  
fonts:
  heading: Inter
  body: Inter
  
That's it. Clean, modern, 2025.
```

### **Navigation (Simple):**
```
Header:
┌─────────────────────────────────────────────┐
│ Te Kete Ako    Browse  About    [Search] 🔍  │
└─────────────────────────────────────────────┘

Browse dropdown:
- Lessons
- Units
- Handouts
- By Subject
- By Year Level

That's it. 5 links. Simple.
```

### **Browse Page (Clean Grid):**
```
Filters:
[Type: All ▾] [Subject: All ▾] [Year: All ▾] [Quality: 90+ ✓]

Grid:
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│ Y8   │ │ Y9   │ │ Y7   │ │ Y10  │
│Algeb │ │Ecolo │ │Digit │ │Stat  │
│Math  │ │Scien │ │Tech  │ │Math  │
│🌟94  │ │🌟95  │ │🌟94  │ │🌟96  │
│      │ │      │ │      │ │      │
│[View]│ │[View]│ │[View]│ │[View]│
└──────┘ └──────┘ └──────┘ └──────┘

Load 20 per page, infinite scroll OR pagination
```

---

## ⚡ THE TIMELINE

### **Day 1: Setup**
- Create Next.js app
- Connect to Supabase (existing tables)
- Test data fetch (verify 1,680 resources load)

### **Day 2: Core Pages**
- Homepage (60 lines)
- Browse page (120 lines)
- Layout + Nav (40 lines)
Total code: ~220 lines

### **Day 3: Polish**
- Tailwind design system
- Search functionality (pgvector semantic search)
- Mobile responsive (Tailwind = automatic)

### **Day 4: Test & Deploy**
- YOU test it
- Fix what's broken
- Deploy to Netlify
- Point tekete.co.nz at it

### **Day 5: Feedback**
- Is it better than current?
- What's still broken?
- What's missing?

**Total: 5 days to functional, clean site**

---

## ✅ WHAT THIS FIXES

**Current Problems:**
- ❌ Can't find content → ✅ Clean browse page with filters
- ❌ Navigation broken → ✅ Simple header nav that works
- ❌ Visual chaos → ✅ One design system, clean UI
- ❌ 932 divs on homepage → ✅ 60 lines, semantic HTML
- ❌ Embarrassing to show colleagues → ✅ Professional 2025 design
- ❌ Can't use on mobile → ✅ Tailwind responsive

**What Stays Good:**
- ✅ 1,680 quality teaching resources (no changes needed)
- ✅ GraphRAG metadata (subject, year, quality all there)
- ✅ Supabase backend (works fine)
- ✅ Content files (lessons/*.html already perfect)

---

## 🚫 WHAT WE DON'T BUILD

**Not building (unless you ask):**
- ❌ AI features showcase
- ❌ 47 different hub pages
- ❌ GraphRAG visualization tools
- ❌ Teacher dashboard with 20 widgets
- ❌ Gamification badges
- ❌ Social features
- ❌ Progress tracking
- ❌ Any of the "vision" docs

**Just building:**
- ✅ Clean homepage
- ✅ Working browse page
- ✅ Simple navigation
- ✅ Search that works
- ✅ Access to existing content

---

## 🎯 THE DECISION POINT

**Current site:** "Worst I've ever seen"  
**New site:** "Actually usable"

**3 questions:**

1. **Does this fix the problem?** (Can you find lessons now?)

2. **Can I start building this today?** (Or more planning?)

3. **What subjects do YOU teach?** (I'll make sure those resources work first in the new browse page)

**This is the data-driven, reality-based plan. Ready?**

