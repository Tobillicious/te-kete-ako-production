# 🚀 NEXT.JS MIGRATION PLAN - Most Professional Move

## **Vision: Museum-Quality Educational Platform**

Transform Te Kete Ako from static HTML → **Next.js 14 + React + Framer Motion**

**Result:** Professional SaaS platform with:
- ⚡ Instant page transitions (no white flash!)
- 🎨 Cinematic animations (Framer Motion)
- 📱 Perfect mobile performance
- 🔥 Component-based (maintainable, DRY)
- 🎭 Notion/Linear/Vercel-level polish
- 🌿 BMAD cultural design philosophy intact

---

## 📊 **Current State Analysis**

### **What We Have:**
- 2,230 HTML files (static)
- 71 CSS files (need consolidation)
- 144 JavaScript files
- Tailwind CSS (good!)
- Supabase backend (perfect for Next.js!)
- 25+ serverless functions (convert to Next.js API routes)
- GraphRAG with 1.19M relationships (perfect for data fetching!)

### **What We're Moving To:**
- Next.js 14 App Router
- React Server Components
- Framer Motion animations
- Radix UI primitives
- Tailwind v4
- TypeScript (optional but recommended)

---

## 🎯 **Migration Strategy: 3-Phase Approach**

### **PHASE 1: FOUNDATION (Week 1 - 8 hours)**

#### **Day 1: Setup (2 hours)**
1. Initialize Next.js 14 with App Router
   ```bash
   npx create-next-app@latest te-kete-ako-next --typescript --tailwind --app
   ```

2. Install core dependencies
   ```bash
   npm install framer-motion @radix-ui/react-* @supabase/ssr
   npm install lucide-react class-variance-authority clsx tailwind-merge
   ```

3. Project structure
   ```
   /app
     /(auth)
       /login
       /register
     /(app)
       /dashboard
       /lessons
       /units
       /handouts
     /(marketing)
       /about
       /pricing
   /components
     /ui (Radix primitives)
     /cultural (Māori patterns, koru, etc.)
     /layouts (sidebar, footer, nav)
   /lib
     /supabase (client, server, middleware)
     /graphrag (queries, relationships)
   /public (static assets only)
   ```

#### **Day 2: Design System (3 hours)**
1. Convert BMAD CSS → Tailwind v4 config
2. Create cultural color tokens
3. Build component primitives (Button, Card, etc.)
4. Set up Framer Motion variants library

#### **Day 3: Core Components (3 hours)**
1. Navigation (sidebar with cultural design)
2. Footer
3. Auth layout
4. Dashboard layout
5. Lesson layout

---

### **PHASE 2: MIGRATION (Week 2-3 - 40 hours)**

#### **Migration Priority Order:**

**Week 2 (20 hours):**
1. **Homepage** (4h)
   - Hero with Framer Motion animations
   - Top 10 resources (GraphRAG-powered)
   - Cultural patterns (animated SVG)
   - Professional polish

2. **Auth Flow** (3h)
   - Login/Register pages
   - Supabase SSR integration
   - Protected routes middleware
   - Role-based redirects

3. **Teacher Dashboard** (4h)
   - Real data from GraphRAG
   - Stats with smooth animations
   - Quick actions
   - Recent resources

4. **Subject Hubs** (5h - crucial!)
   - Mathematics Hub
   - Science Hub  
   - English Hub
   - Te Reo Māori Hub
   - Social Studies Hub
   - Digital Tech Hub
   - Dynamic data from GraphRAG

5. **Search** (4h)
   - Semantic search (GraphRAG relationships)
   - Instant results
   - Filters (year, subject, quality)
   - Beautiful results layout

**Week 3 (20 hours):**
6. **Lesson Pages** (8h)
   - Dynamic routes `[slug]`
   - Markdown rendering
   - Beautiful typography
   - Print-friendly
   - Related resources (GraphRAG!)

7. **Unit Pages** (4h)
   - Progress tracking
   - Lesson progression
   - Cultural integration display

8. **Handout Pages** (4h)
   - Download functionality
   - Print optimization
   - Editable exports

9. **Student Dashboard** (4h)
   - Age-appropriate design
   - Progress visualization
   - Achievements (animated!)
   - My Learning path

---

### **PHASE 3: POLISH (Week 4 - 16 hours)**

#### **Professional Excellence:**

1. **Animations** (4h)
   - Page transitions (Framer Motion)
   - Card hover effects
   - Loading states (cultural spinners!)
   - Scroll-triggered animations
   - Gesture interactions

2. **Performance** (4h)
   - Image optimization (Next.js Image)
   - Route prefetching
   - Streaming SSR
   - Edge functions
   - CDN optimization

3. **Cultural Polish** (4h)
   - Koru animations
   - Kōwhaiwhai patterns
   - Māori typography
   - Cultural tooltips
   - Whakataukī daily wisdom

4. **Testing & QA** (4h)
   - Lighthouse 95+ score
   - Mobile testing
   - Auth flows
   - Payment testing
   - Accessibility audit

---

## 💎 **The Next.js Advantage**

### **What You Get:**

#### **1. Server Components = INSTANT**
```tsx
// Lessons load INSTANT (no JavaScript to client!)
async function LessonsPage() {
  const lessons = await getTopLessons() // Server-side!
  return <LessonGrid lessons={lessons} /> // Streams to client
}
```

#### **2. Framer Motion = CINEMATIC**
```tsx
// Beautiful page transitions
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6, ease: "easeOut" }}
>
  <KoruPattern />
</motion.div>
```

#### **3. Radix UI = ACCESSIBLE + BEAUTIFUL**
```tsx
// Professional dropdowns, modals, etc.
<DropdownMenu>
  <DropdownMenuTrigger>Year Level</DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuItem>Year 7</DropdownMenuItem>
    {/* Animated, accessible, keyboard nav built-in! */}
  </DropdownMenuContent>
</DropdownMenu>
```

#### **4. GraphRAG Integration = POWERFUL**
```tsx
// Leverage all 1.19M relationships!
const relatedLessons = await getRelatedByGraphRAG(currentLesson.id)
// Uses related_concept, prerequisite, same_subject relationships
```

---

## 🎨 **Design System Migration**

### **From BMAD CSS → Tailwind v4 Config:**

```js
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        // BMAD Cultural Palette
        pounamu: {
          50: '#f0fdf4',
          500: '#1B7F5A', // Sacred greenstone
          900: '#064e3b',
        },
        kowhai: {
          500: '#F5D915', // Golden bloom
          pure: '#FFD700', // Kehinde Wiley gold
        },
        whenua: {
          100: '#f5f1eb', // Warm earth
          600: '#6B4E3D',
        },
      },
      fontFamily: {
        display: ['Playfair Display', 'serif'], // Regal
        body: ['Inter', 'sans-serif'],
      },
      animation: {
        'koru-unfurl': 'unfurl 0.8s ease-out',
        'fade-in': 'fadeIn 0.6s ease-out',
      },
    },
  },
}
```

### **Cultural Components:**

```tsx
// components/cultural/KoruSpinner.tsx
export function KoruSpinner() {
  return (
    <motion.svg
      animate={{ rotate: 360 }}
      transition={{ repeat: Infinity, duration: 2, ease: "linear" }}
    >
      {/* Koru SVG path */}
    </motion.svg>
  )
}

// components/cultural/WhakataukiCard.tsx
export function WhakataukiCard({ proverb, translation }) {
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="bg-kowhai-100 border-l-4 border-kowhai-500 p-6"
    >
      <p className="font-display italic text-pounamu-800">{proverb}</p>
      <p className="text-whenua-600 mt-2">{translation}</p>
    </motion.div>
  )
}
```

---

## 📦 **Tech Stack Breakdown**

### **Core Framework:**
- **Next.js 14** (App Router, Server Components, Streaming)
- **React 18** (Concurrent features, Suspense)
- **TypeScript** (Type safety, better DX)

### **Styling:**
- **Tailwind CSS v4** (New engine, faster)
- **CVA** (Component variants)
- **tailwind-merge** (Dynamic classes)

### **UI Components:**
- **Radix UI** (Accessible primitives)
- **Lucide React** (Beautiful icons)
- **Framer Motion** (Cinematic animations)

### **Backend Integration:**
- **Supabase SSR** (Server-side auth)
- **GraphRAG queries** (Server Components!)
- **Next.js API Routes** (Replace serverless functions)

### **Performance:**
- **Next.js Image** (Auto-optimization)
- **Sharp** (Image processing)
- **Edge Runtime** (Global CDN)

### **Developer Experience:**
- **ESLint + Prettier**
- **Husky** (Git hooks)
- **TypeScript** (IntelliSense)

---

## ⏱️ **Timeline & Effort**

### **Conservative Estimate:**
- **Phase 1:** 8 hours (foundation)
- **Phase 2:** 40 hours (migration)  
- **Phase 3:** 16 hours (polish)
- **TOTAL:** 64 hours (~2 weeks full-time OR 4 weeks part-time)

### **Aggressive Estimate:**
- Parallel work with tools/AI assistance
- **TOTAL:** 40 hours (~1 week intensive)

---

## 🎯 **Immediate Next Steps**

### **Option 1: Start Migration Now**
1. Create new Next.js project alongside current
2. Build in `/next-app/` directory
3. Keep current site running during migration
4. Gradual cutover

### **Option 2: Test First**
1. Build ONE page in Next.js (homepage)
2. Compare side-by-side
3. User approves look/feel
4. Then commit to full migration

### **Option 3: Hybrid Approach**
1. Keep static HTML for content (lessons/units)
2. Build Next.js app shell (nav, dashboards, hubs)
3. Embed static content in Next.js routes
4. Best of both worlds

---

## 💰 **Cost-Benefit Analysis**

### **Benefits:**
- 🎨 **Professional:** Notion/Linear-level polish
- ⚡ **Fast:** Instant navigation, <2s loads
- 🔧 **Maintainable:** Component-based, DRY
- 📱 **Mobile:** Perfect responsive design
- 🎭 **Animations:** Cinematic (Framer Motion)
- 💎 **Value:** $100K+ professional frontend

### **Costs:**
- ⏱️ **Time:** 40-64 hours migration
- 🧠 **Learning:** React knowledge needed for maintenance
- 🏗️ **Complexity:** Build process (not just static files)

### **Risk Mitigation:**
- ✅ Keep current site running during migration
- ✅ Build in parallel (`/next-app/`)
- ✅ Gradual cutover (test with beta teachers first)
- ✅ Can always roll back to static

---

## 🌿 **Cultural Design Preserved**

**BMAD Philosophy in Next.js:**

```tsx
// Whakapapa-based navigation (from BMAD doc)
<WhakapapaSidebar>
  <AncestorLevel href="/fundamentals">Year 7 Foundation</AncestorLevel>
  <CurrentLevel href="/current">Year 8 Building</CurrentLevel>
  <DescendantLevel href="/advanced">Year 9 Mastery</DescendantLevel>
</WhakapapaSidebar>

// Marae spatial organization
<MaraeLayout>
  <Wharenui>Main Content</Wharenui>
  <Wharekai>Resources Library</Wharekai>
  <Marae>Community Space</Marae>
</MaraeLayout>

// Natural pigment colors (BMAD + Kehinde Wiley)
className="bg-pounamu-600 text-kowhai-pure border-whenua-500"
```

**All BMAD principles can be implemented in React!**

---

## 🎯 **My Recommendation**

### **Start with Option 2: Build ONE page first**

**This weekend (4 hours):**
1. Initialize Next.js project
2. Build homepage in Next.js
3. Deploy to Vercel preview
4. Compare side-by-side with current

**You decide:**
- If you love it → commit to full migration (3-4 weeks)
- If not → stick with static + enhancements (Alpine + Framer)

**Low risk, high confidence decision.**

---

## 🚀 **Shall I:**
1. **Start Phase 1 now** (initialize Next.js, build sample homepage)?
2. **Create detailed component list** (all pages → React components map)?
3. **Build prototype first** (just homepage, compare quality)?

**What's your preference?**

