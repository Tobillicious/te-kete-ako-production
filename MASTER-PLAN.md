# 🎯 MASTER PLAN - Te Kete Ako Platform

**Single source of truth. Updated continuously. No more doc chaos.**

**Last Updated:** 2025-10-26 8:00 PM  
**Status:** Active Planning - Awaiting User Decision  
**GraphRAG ID:** 37757

---

## 📊 CURRENT STATE (Verified)

### **What's Broken:**
1. **SaaS Wrapper = Disaster**
   - Homepage: 932 divs, 2,252 lines
   - Navigation: Broken loaders, doesn't work
   - CSS: 5 conflicting systems
   - User verdict: "Worst site I've ever seen"

2. **Teaching Content = Needs Work** (but less critical)
   - User says content "isn't OK"
   - GraphRAG shows 1,680 resources with 90+ quality scores
   - Reality check needed: Are quality scores accurate?

### **What Works:**
- Supabase backend (database functional)
- GraphRAG data (1.19M relationships)
- Deployment pipeline (Netlify works when code doesn't break it)
- Domain purchased: tekete.co.nz

---

## 🎯 THE PROBLEM (User's Actual Experience)

**Navigation:** Can't find anything  
**Quality:** Cluttered, broken, unusable  
**Professional:** Too embarrassing to show colleagues  
**Functional:** Barely works  

**Critical:** User #1 (real teacher) won't use it. No other teachers will try it.

---

## 🔧 THE ACTUAL STRATEGY: Tool-Augmented Rebuild

**Approach:** Use 3rd party tools to amplify AI effectiveness

### **Tools Arsenal:**

1. **Cursor Composer** - Multi-file refactoring
   - Fix navigation across all 269 HTML files
   - Consolidate CSS systems
   - Remove duplicate code

2. **v0.dev** - Generate clean React components
   - Professional homepage
   - Browse page with filters
   - Resource cards
   - Navigation header

3. **Bolt.new** - Rapid Next.js prototyping
   - Full stack app in minutes
   - Test ideas before committing
   - Generate boilerplate fast

4. **GraphRAG + pgvector** - Intelligent content organization
   - Already have 1.19M relationships
   - Use for smart recommendations
   - Semantic search (already installed)

5. **Supabase AI** - Content enhancement
   - Generate embeddings for all resources
   - Vector similarity search
   - AI-powered recommendations

### **The Plan:**

**Phase 1: Prototype (v0.dev + Bolt.new)**
- Generate clean Next.js components in v0.dev
- Prototype full app in Bolt.new
- Test with real data
- Show you for approval

**Phase 2: Build (Cursor Composer)**
- Multi-file refactor of existing codebase
- Or implement v0 components if approved
- Use Composer for consistency

**Phase 3: Intelligence (GraphRAG + Supabase)**
- Generate embeddings for all 1,680 resources
- Enable semantic search
- Add smart recommendations

**Timeline:** 2-3 days with tools vs. weeks manual

---

## ✅ DECISIONS MADE

1. **Subjects:** Year 8 - English, Maths, Social Studies, Te Reo Māori
2. **Approach:** Tool-augmented professional rebuild
3. **Tools:** Cursor Composer + v0.dev + Bolt.new + GraphRAG
4. **Content:** We have GOOD Y8 content (160+ Maths, 119+ Social Studies, 35+ Te Ao Māori)

## 🎯 THE RESTORATION STRATEGY (User Approved!)

**STATUS: ✅ RESTORATION COMPLETE & APPROVED BY USER!**

User verdict: *"OMG I love you! This works so well! Horray! This is gonna be the version we going with!!!"*

### What We Did

1. **Backup Teaching Content** ✅
   - Moved 993 HTML files to `/te-kete-TEACHING-CONTENT-BACKUP/`
   - Content is safe and can be selectively restored

2. **Restore to Clean Version** ✅
   - Git checkout to commit `7b1c43f90` (July 27, 2025)
   - Created new branch: `clean-restoration`
   - Result: Clean, simple, working codebase

3. **Verify It Works** ✅
   - Homepage: 349 lines (down from 2,252!)
   - ONE CSS file: `css/main.css` (89KB)
   - Navigation: Working dropdowns
   - Sidebar: Organized and functional
   - Local server: Running perfectly at localhost:8000

### Restored Version Details

- **File structure**: Root directory (no /public/ chaos)
- **HTML files**: 993 organized content files
- **Design**: Cultural colors (pounamu green, kowhai gold)
- **Navigation**: Header with dropdowns, left sidebar
- **Content**: Unit plans, lessons, handouts, games, curriculum

## 🔥 PHASE 2: POLISH & REBUILD

**NOW WE POLISH THIS CLEAN VERSION!**

### Immediate Polish Tasks

1. **Visual Polish**
   - Fine-tune colors and spacing
   - Improve typography hierarchy
   - Add subtle animations
   - Ensure mobile responsiveness

2. **Content Strategy**
   - Mine GraphRAG for Quality Year 8 content
   - Selectively restore teaching content (Quality 95+ only)
   - Add curriculum integration
   - Link to GraphRAG intelligence

3. **Modern Enhancements**
   - Add search functionality
   - Connect to `browse_resources_api`
   - Filter by subject/year level
   - Quality badges for high-scoring resources

4. **Professional Details**
   - Fix any broken links
   - Improve loading states
   - Add helpful tooltips
   - Polish micro-interactions

### What to Keep

✅ Clean navigation structure
✅ Cultural aesthetic
✅ Organized sidebar
✅ Simple, clear hierarchy
✅ Working functionality

### What to Improve

🔧 Visual refinements
🔧 Content quality and organization
🔧 User experience details
🔧 Integration with GraphRAG data
🔧 Modern component library

**This is our foundation. Now we make it PHENOMENAL.** 🚀

### 📋 FOR USER TO DO:

**v0.dev Prompt (Homepage):**
```
Create a professional educational platform homepage for "Te Kete Ako"

Design Requirements:
- Hero section: Large "Te Kete Ako" heading, subtitle "1,680 quality NZ resources"
- Search bar: Large, centered, placeholder "Search lessons, units, handouts..."
- 3 cards grid: Lessons (1,040), Units (204), Handouts (440)
- Colors: Emerald/pounamu green (#10b981), gold accents
- Typography: Inter font, clean hierarchy
- Mobile responsive Tailwind
- Professional 2025 aesthetic (Stripe/Linear quality)
- Cultural: Māori patterns subtle background

Generate as Next.js 14 TypeScript component with Tailwind.
```

**Bolt.new Prompt (Full App):**
```
Build Next.js 14 educational SaaS platform "Te Kete Ako"

Stack: Next.js 14 App Router, TypeScript, Tailwind, Supabase

Pages needed:
1. Homepage (hero + search + 3 resource type cards)
2. /browse (resource grid with filters: subject, year, type)
3. /resource/[id] (individual resource view)
4. Layout with header nav

Supabase connection:
- URL: https://nlgldaqtubrlcqddppbq.supabase.co
- Use browse_resources_api view
- Columns: id, title, subject, resource_type, year_level, quality_score, file_path

Design: Professional, clean, pounamu green theme, mobile-first

Add: Semantic search placeholder, filter chips, quality badges (90+)
```

---

## 📚 GRAPHRAG API DOCUMENTATION

### **1. Browse Resources API**
```typescript
// Query all high-quality resources with smart metadata
const { data } = await supabase
  .from('browse_resources_api')
  .select('*')
  .eq('subject', 'Mathematics')
  .eq('year_level', '8')
  .order('quality_score', { ascending: false })

// Returns: id, title, subject, resource_type, year_level, quality_score, 
//          file_path, cultural_context, content_preview,
//          connection_count, has_prerequisites, is_excellence
```

### **2. Year 8 Quality Resources (Materialized View)**
```typescript
// Fast access to YOUR subject content
const { data } = await supabase
  .from('year_8_quality_resources')
  .select('*')
  .in('subject', ['English', 'Mathematics', 'Social Studies', 'Te Reo Māori'])

// Pre-filtered: Year 8 only, 90+ quality, your subjects
```

### **3. Smart Recommendations (GraphRAG Function)**
```typescript
// Get related resources using 828K+ semantic relationships
const { data } = await supabase.rpc('get_related_resources', {
  resource_id_input: 12345,
  limit_count: 5
})

// Returns: related resources sorted by relevance
// - Prerequisites (1.0 score)
// - Learning sequences (0.9)
// - Excellence clusters (0.85)
// - Cultural connections (0.8)
```

---

## 🎼 CURSOR COMPOSER IMPLEMENTATION PLAN

### **Phase 1: Setup (Composer Multi-File)**
```
Files to modify simultaneously:
- /app/page.tsx (homepage)
- /app/layout.tsx (header/footer)
- /app/browse/page.tsx (browse grid)
- /app/resource/[id]/page.tsx (resource view)
- /lib/supabase.ts (DB client)
- /tailwind.config.ts (theme)

Composer Prompt:
"Implement the professional Te Kete Ako platform using v0 components.
Use browse_resources_api view from Supabase. Pounamu green theme.
Make it production-ready with proper TypeScript types and error handling."
```

### **Phase 2: Features (Composer Iteration)**
```
Add in order:
1. Search functionality (semantic, uses pgvector)
2. Filters (subject, year, type) with URL params
3. Recommendations (get_related_resources function)
4. Auth (Supabase SSR)
5. Stripe (if time allows)

Each iteration: Composer modifies 3-5 files at once
```

### **Phase 3: Polish (Composer Refinement)**
```
- Mobile responsive fixes
- Loading states
- Error boundaries
- Performance optimization
- Deploy to Netlify
```

---

## 📚 LINKED DOCUMENTATION

**Active Plans:**
- THIS FILE (MASTER-PLAN.md) - Single source of truth
- [GraphRAG API](#-graphrag-api-documentation) - Database functions (above)
- [Composer Plan](#-cursor-composer-implementation-plan) - Implementation strategy (above)

**Context (if needed):**
- [Socratic Interrogation](./SOCRATIC-INTERROGATION.md) - Self-critique
- [The Honest Plan](./THE-HONEST-PLAN.md) - User research approach

**Archive (ignore):**
- All other vision/planning documents

---

## 🎯 NEXT ACTIONS (Waiting on User)

1. Answer 4 questions above
2. I build ONE thing (no more planning)
3. You test it
4. We iterate

**No more documents. Just shipping.**

---

**Updated in GraphRAG:** Yes (ID: 37757)  
**Version:** 1.0  
**Next Update:** After user decision

