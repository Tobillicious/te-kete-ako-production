# 📚 CURRICULUM V3 - MASTER PLAN

**Created:** October 29, 2025  
**Status:** Planning Phase  
**Complexity:** 🔴 EXTREMELY HIGH - Multi-week project

---

## 🎯 **THE PROBLEM**

### What Teachers Are Facing:
- NZ Government constantly updating curriculum (Phase 1, Phase 2, Phase 3, Phase 4...)
- New versions aren't always improvements
- Teachers cherry-picking Achievement Objectives (AOs) from **multiple curriculum versions**
- Hard to find and compare official curriculum statements
- Current gov site (Tahurangi) is slow, poorly organized

### Real-World Impact:
> "Teachers are struggling to keep up. They're mixing AOs from 2007 NZC, 2024 refresh, Phase 4 updates... it's chaos but necessary because the new stuff isn't always better."

**Unofficial Reality:** ALL curriculum versions are currently "valid" for planning

---

## 🌟 **OUR SOLUTION: CURRICULUM V3**

### Vision Statement:
**"One beautiful, fast platform to browse ALL official NZ Curriculum statements across ALL versions, subjects, year levels, and phases"**

### Core Features:
1. **Multi-Version Browser** - Switch between 2007 NZC, 2024 Refresh, Phase 1-4, etc.
2. **Subject Navigator** - All 8 learning areas (English, Math, Science, etc.)
3. **Year/Level Filter** - Years 1-13, Curriculum Levels 1-8
4. **Phase Selector** - Phase 1 (Years 1-2) through Phase 4 (Years 9-10)
5. **Comparison View** - See how AOs changed across versions
6. **Search Everything** - Fast, semantic search across ALL curriculum docs
7. **Gorgeous UI** - Makes complex information feel simple

---

## 📊 **RESEARCH PHASE - COMPLETED**

### Step 1: Map All Curriculum Versions ✅

**CRITICAL DISCOVERY:** This is WAY more complex than initially thought!

#### **Te Mātaiaho (2025 - THE BIG REFRESH)**
**Official Name:** "The New Zealand Curriculum | Te Mātaiaho"  
**Status:** Draft released October 28, 2025 (YES YESTERDAY!)  
**Consultation:** Open until April 24, 2026  
**Implementation Timeline:**
- **Jan 1, 2026:** English & Math Years 0-10 (ALREADY MANDATORY!)
- **Term 1, 2027:** Science, Social Sciences, Health/PE (Years 0-8) + ALL subjects (Years 9-10)  
- **Term 1, 2028:** Arts, Technology, Learning Languages (Years 0-8)

**Structure:** PHASE-BASED (completely different!)
- **Phase 1:** Years 0-3 (not 1-2!)
- **Phase 2:** Years 4-6
- **Phase 3:** Years 7-8
- **Phase 4:** Years 9-10
- **NO PHASE 5 YET** - Years 11-13 still separate

**Key Differences from Old NZC:**
- OLD: Organized by "Curriculum Levels" (1-8)
- NEW: Organized by "Phases" (Years 0-10) + "Teaching Sequences"
- OLD: Strands like "Reading, Writing, Speaking, Listening"
- NEW: Strands like "Text Studies, Language Studies" (totally restructured!)

#### **2007 NZC (Still Active!)**
**Official Name:** "The New Zealand Curriculum"  
**Status:** Still in effect until Jan 1, 2027 for Framework  
**Structure:** Curriculum Levels 1-8
**Why Teachers Still Use It:** More flexible, familiar, "better quality"

#### **Draft Learning Areas (Released Oct 28, 2025) 🔥**
**What's New:**
- Science (Years 0-10) - DRAFT
- Social Sciences (Years 0-10) - DRAFT  
- Health & PE (Years 0-10) - DRAFT
- The Arts (Years 0-10) - DRAFT
- Learning Languages (Years 0-10) - DRAFT
- Technology (Years 0-10) - DRAFT

**URL Pattern:**
```
https://newzealandcurriculum.tahurangi.education.govt.nz/
  /new-zealand-curriculum-online/
  /nzc---[subject]-phase-[N]-years-[X-Y]/
  /[ID].p
```

**Example URLs Found:**
- English Phase 4: `/nzc---english-phase-4-years-9-10/5637291578.p`
- Learning Areas Hub: `/learning-areas/5637165582.c`

### Step 2: Map Learning Area Structure ✅

**8 Learning Areas:**
1. English / Literacy
2. Mathematics & Statistics / Pāngarau
3. Science / Pūtaiao
4. Social Sciences / Tikanga-ā-Iwi
5. Te Reo Māori
6. The Arts / Ngā Toi
7. Health & Physical Education / Hauora
8. Technology / Hangarau
9. **Learning Languages** (13 languages including NZSL!)

**MAJOR STRUCTURAL DIFFERENCES:**

#### OLD NZC 2007 Structure:
```
Learning Area
 └─ Curriculum Level (1-8)
     └─ Strand (e.g. "Reading", "Writing")
         └─ Achievement Objective
```

#### NEW Te Mātaiaho Structure:
```
Learning Area
 └─ Phase (1-4, based on Years not Levels)
     └─ Strand (COMPLETELY DIFFERENT names!)
         └─ Element (new concept!)
             └─ Knowledge & Practices (not just "AOs")
                 └─ Teaching Sequences (prescriptive guidance)
```

**Example - English:**
- **OLD Strands:** Reading, Writing, Speaking, Listening, Presenting
- **NEW Strands (Phase 4):** Text Studies, Language Studies
- **NEW Elements:** Textual Analysis, Critical Analysis, Crafting Texts, Oral Communication

**This is NOT just a refresh - it's a COMPLETE RESTRUCTURE!**

### Step 3: Analyze Government Site Structure

**Tahurangi Site Analysis:**
```
Base: https://newzealandcurriculum.tahurangi.education.govt.nz
Structure: /[learning-area]-phase-[N]-years-[X-Y]/[id].p
Example: /nzc---english-phase-4-years-9-10/5637291578.p
```

**What We Need:**
- [ ] Complete URL list for ALL curriculum pages
- [ ] Understand the ID system (e.g. "5637291578")
- [ ] Check if there's an API or sitemap
- [ ] Identify downloadable PDFs
- [ ] Test rate limits for scraping

---

## 🗄️ **DATA ARCHITECTURE**

### Option 1: Supabase Tables (Recommended)

**Table: `curriculum_versions`**
```sql
CREATE TABLE curriculum_versions (
  id UUID PRIMARY KEY,
  version_code TEXT UNIQUE, -- "nzc_2007", "nzc_2024", "phase_4_2024"
  version_name TEXT, -- "New Zealand Curriculum 2007"
  effective_date DATE,
  status TEXT, -- "current", "archived", "draft"
  description TEXT,
  official_url TEXT,
  created_at TIMESTAMP
);
```

**Table: `learning_areas`**
```sql
CREATE TABLE learning_areas (
  id UUID PRIMARY KEY,
  code TEXT UNIQUE, -- "english", "math", "social_studies"
  name_en TEXT, -- "English"
  name_mi TEXT, -- "Reo Pākehā"
  description TEXT,
  color_hex TEXT -- For UI styling
);
```

**Table: `curriculum_strands`**
```sql
CREATE TABLE curriculum_strands (
  id UUID PRIMARY KEY,
  learning_area_id UUID REFERENCES learning_areas(id),
  version_id UUID REFERENCES curriculum_versions(id),
  name TEXT, -- "Reading and Viewing"
  description TEXT,
  sort_order INTEGER
);
```

**Table: `achievement_objectives`**
```sql
CREATE TABLE achievement_objectives (
  id UUID PRIMARY KEY,
  version_id UUID REFERENCES curriculum_versions(id),
  learning_area_id UUID REFERENCES learning_areas(id),
  strand_id UUID REFERENCES curriculum_strands(id),
  
  -- Identification
  code TEXT, -- "NZC-EN-4-RV-1" (custom code we create)
  official_code TEXT, -- If gov provides codes
  
  -- Content (VERBATIM FROM GOVERNMENT)
  statement TEXT NOT NULL, -- The actual AO text
  elaboration TEXT, -- Supporting text/examples
  
  -- Classification
  curriculum_level INTEGER, -- 1-8
  year_levels INTEGER[], -- [9, 10]
  phase TEXT, -- "phase_4"
  
  -- Metadata
  source_url TEXT,
  last_verified DATE,
  created_at TIMESTAMP,
  
  -- Full-text search
  search_vector TSVECTOR
);

-- Full-text search index
CREATE INDEX ao_search_idx ON achievement_objectives 
USING GIN(search_vector);
```

**Table: `curriculum_relationships`**
```sql
CREATE TABLE curriculum_relationships (
  id UUID PRIMARY KEY,
  ao_id_from UUID REFERENCES achievement_objectives(id),
  ao_id_to UUID REFERENCES achievement_objectives(id),
  relationship_type TEXT, -- "replaces", "updates", "equivalent", "related"
  notes TEXT,
  created_at TIMESTAMP
);
```

### Option 2: JSON Files + GraphRAG (Backup)

If Supabase gets too large, we can store in JSON files:
- `data/curriculum/nzc_2007.json`
- `data/curriculum/phase_4_2024.json`

Then use GraphRAG for relationships only.

---

## 🕷️ **SCRAPING STRATEGY**

### Ethical & Legal Considerations:
✅ **We CAN scrape because:**
- Content is public government information
- We're not republishing commercially
- We're making it MORE accessible for teachers
- We'll attribute source properly

### Technical Approach:

**Option A: Puppeteer + Cheerio (Recommended)**
```javascript
// Pseudo-code
const pages = await getAllCurriculumURLs();
for (const page of pages) {
  const content = await scrapeVerbatim(page.url);
  await validateContent(content); // Check no corruption
  await saveToDatabase(content);
  await delay(2000); // Respectful rate limiting
}
```

**Option B: Exa.ai API**
- User mentioned this might help
- Can search and extract web content
- Worth exploring for automation

**Option C: Manual + PDF Parsing**
- Download official PDFs
- Use pdf-parse or similar
- More reliable but slower

### Validation Requirements:
- [ ] Character-level comparison with source
- [ ] HTML entity handling (quotes, apostrophes)
- [ ] Māori macrons preserved (ā, ē, ī, ō, ū)
- [ ] Formatting preserved (bold, italic, lists)
- [ ] No AI interpretation - VERBATIM ONLY

---

## 🎨 **UI/UX DESIGN**

### Design Principles:
1. **Speed First** - Teachers don't have time. Sub-second interactions.
2. **Visual Hierarchy** - Complex info made simple through design
3. **Cultural Respect** - Te Reo Māori equal prominence
4. **Mobile-Ready** - Teachers browse on phones
5. **Print-Friendly** - Easy to save AOs for planning docs

### Component Breakdown:

#### 1. **Top Filter Bar**
```
[Version Selector ▼] [Subject ▼] [Year Level ▼] [Phase ▼] [🔍 Search...]
```

**Version Selector:**
- Dropdown or tab switcher
- Icons for visual distinction
- Shows count: "NZC 2007 (186 AOs)"

#### 2. **Subject Cards Grid**
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ 📝 English  │ │ 🔢 Math     │ │ 🔬 Science  │
│ 42 AOs      │ │ 38 AOs      │ │ 35 AOs      │
└─────────────┘ └─────────────┘ └─────────────┘
```

#### 3. **Strand Accordion**
```
📖 Reading and Viewing [EXPANDED]
  ├─ Level 1: [3 AOs]
  ├─ Level 2: [3 AOs]
  └─ Level 3: [4 AOs]

✍️ Writing [COLLAPSED]
```

#### 4. **Achievement Objective Card**
```
┌────────────────────────────────────────────────────┐
│ 📋 NZC-EN-4-RV-1                        [⭐ Save]  │
├────────────────────────────────────────────────────┤
│ Level 4 | Years 9-10 | Phase 4                     │
│                                                     │
│ "Students will use their knowledge of text         │
│  structures and language features to make          │
│  meaning from texts..."                            │
│                                                     │
│ 🔗 Source: Tahurangi NZC Phase 4                  │
│ 📅 Last Verified: Oct 29, 2025                    │
└────────────────────────────────────────────────────┘
```

#### 5. **Comparison View** (Advanced Feature)
```
Split screen:
┌──────────────────┬──────────────────┐
│   NZC 2007       │  Phase 4 2024    │
├──────────────────┼──────────────────┤
│ [AO Statement]   │ [Updated AO]     │
│                  │                  │
│ Changes: [Highlight diff]           │
└─────────────────────────────────────┘
```

### Color System (From main.css):
- **English**: Purple/Royal Blue (#6366f1)
- **Math**: Teal (#00b0b9)
- **Science**: Forest Green (#2c5f41)
- **Social Studies**: Earth Brown (#8b6f47)
- **Te Reo**: Cultural Teal (#40e0d0)
- **Arts**: Golden Yellow (#f5a623)
- **Health**: Vibrant Green (#10b981)
- **Technology**: Modern Blue (#3b82f6)

---

## 🛠️ **IMPLEMENTATION PHASES**

### Phase 1: Foundation (Week 1-2)
**Goal:** Get ONE curriculum version working perfectly

**Tasks:**
- [x] Research complete (map versions, structures, URLs)
- [ ] Create Supabase tables
- [ ] Scrape NZC 2007 English Level 4 (test sample)
- [ ] Validate data quality (verbatim check)
- [ ] Build basic UI for ONE subject
- [ ] Test with real teachers

**Success Criteria:**
- 100% verbatim accuracy for test sample
- Teachers can browse English Level 4 easily
- Performance: < 500ms page load

### Phase 2: Scale Up (Week 3-4)
**Goal:** Complete ONE full curriculum version

**Tasks:**
- [ ] Scrape all 8 learning areas for NZC 2007
- [ ] Build full subject switcher
- [ ] Add year level filtering
- [ ] Implement search (full-text)
- [ ] Add "Save to My Kete" functionality
- [ ] Create print styles

**Success Criteria:**
- All NZC 2007 content indexed
- Teachers report it's faster than Tahurangi
- Zero accuracy errors

### Phase 3: Multi-Version (Week 5-6)
**Goal:** Add Phase 4 (2024) curriculum

**Tasks:**
- [ ] Scrape Phase 4 curriculum docs
- [ ] Build version switcher UI
- [ ] Create comparison view
- [ ] Map relationships (which AOs replace which)
- [ ] Add "What's Changed?" summaries

**Success Criteria:**
- Can toggle between 2007 and 2024
- Relationships mapped for ALL AOs
- Teachers love the comparison feature

### Phase 4: Complete & Polish (Week 7-8)
**Goal:** Production-ready with ALL versions

**Tasks:**
- [ ] Add remaining versions (Phase 1, 2, 3)
- [ ] Advanced search (semantic, cross-version)
- [ ] Export functionality (PDF, Word)
- [ ] Mobile optimization
- [ ] User testing with 10+ teachers
- [ ] Documentation & guides

**Success Criteria:**
- ALL official curriculum versions indexed
- 95%+ teacher satisfaction
- Becomes Te Kete Ako's killer feature

---

## 😱 **THE BRUTAL REALITY CHECK**

### What This ACTUALLY Means:

**Scope Multiplier:** We're not building ONE curriculum browser. We're building:
- 2007 NZC (8 learning areas × 8 levels × ~3-5 strands each = **~200-300 AOs**)
- Te Mātaiaho 2025 (8 learning areas × 4 phases × multiple elements = **~400-600 statements**)
- **PLUS** they're COMPLETELY DIFFERENT structures (can't just copy structure!)
- **PLUS** draft versions are being updated constantly
- **PLUS** consultation feedback might change things before April 2026

### Why This is a Nightmare:

1. **TWO ENTIRELY DIFFERENT TAXONOMIES** - Can't reuse data model
2. **RELEASED YESTERDAY** - Means ZERO existing tools/parsers
3. **STILL IN DRAFT** - Content might change
4. **VERBATIM REQUIREMENT** - One typo = legal/credibility issue
5. **NO API** - Must scrape + validate manually
6. **Teachers Need It NOW** - English & Math mandatory from Jan 1, 2026 (62 days!)

### Estimated Work:

| Task | Hours | Complexity |
|------|-------|------------|
| Scrape Te Mātaiaho (all 8 areas × 4 phases) | 40-60 | 🔴🔴🔴 |
| Scrape 2007 NZC (all 8 areas × 8 levels) | 30-40 | 🔴🔴 |
| Build dual data model (2 structures) | 15-20 | 🔴🔴🔴 |
| Validate verbatim accuracy (critical!) | 20-30 | 🔴🔴🔴 |
| Build UI that handles BOTH structures | 25-35 | 🔴🔴🔴 |
| Testing + refinement | 15-20 | 🔴🔴 |
| **TOTAL:** | **145-205 hours** | 🔴🔴🔴🔴🔴 |

**Translation:** This is a **3-5 WEEK FULL-TIME PROJECT** minimum.

---

## 💡 **RECOMMENDED APPROACH**

### Option A: PHASED MVP (Recommended)

**Phase 1 (This Week - 10-15 hours):**
- Scrape English Phase 4 ONLY (mandatory Jan 1)
- Scrape Math Phase 4 ONLY (mandatory Jan 1)
- Build basic UI for THESE TWO subjects
- Ship to teachers IMMEDIATELY

**Phase 2 (Next Week - 15-20 hours):**
- Add remaining Te Mātaiaho subjects (Phases 1-4)
- Build phase switcher
- Add search

**Phase 3 (Week 3 - 20-25 hours):**
- Add 2007 NZC (all subjects)
- Build version comparison view
- Full feature set

### Option B: PERFECT FIRST (Not Recommended)

- Do ALL research upfront
- Build complete data model
- Scrape everything
- Launch when 100% done
- **Risk:** Takes 2+ months, teachers suffer meanwhile

### Option C: PARTNERSHIP APPROACH

- You manually grab some PDFs/docs
- I build scraper for structure
- We split the work
- Ship faster together

---

## 🚨 **RISKS & MITIGATION**

### Risk 1: Government Site Changes
**Risk:** Tahurangi changes URL structure or content  
**Mitigation:** 
- Store source URLs with each AO
- Set up automated weekly verification
- Build flexible scraper that adapts

### Risk 2: Copyright/Legal Issues
**Risk:** Ministry contacts us about content use  
**Mitigation:**
- Prominent attribution on every page
- Link back to official sources
- Reach out proactively for permission
- Frame as "educational tool" not commercial

### Risk 3: Data Quality (Verbatim Requirement)
**Risk:** Scraping introduces errors  
**Mitigation:**
- Manual verification for 10% sample
- Character-level diff checks
- Teacher feedback loop
- "Report an error" button

### Risk 4: Scope Creep
**Risk:** Trying to do too much, project never finishes  
**Mitigation:**
- Ship Phase 1 fast (2 weeks)
- Get teacher feedback early
- Iterate based on actual use
- OK to launch with ONE version first

---

## 📈 **SUCCESS METRICS**

### Quantitative:
- [ ] 100% curriculum coverage (all official AOs indexed)
- [ ] < 1 second average page load
- [ ] 0 verbatim errors detected
- [ ] 500+ AOs searchable
- [ ] 50+ teachers using weekly (first month)

### Qualitative:
- [ ] Teachers report it's "faster than Tahurangi"
- [ ] Teachers report it's "easier to find what I need"
- [ ] Teachers report "finally! I can compare versions"
- [ ] Becomes known as THE place for curriculum reference

---

## 🎯 **IMMEDIATE NEXT STEPS**

### This Session:
1. ✅ Create this master plan
2. [ ] Research complete URL list from Tahurangi
3. [ ] Test scraping ONE page (verbatim validation)
4. [ ] Design Supabase schema
5. [ ] Sketch UI mockup

### Next Session:
1. [ ] Set up Supabase tables
2. [ ] Build scraping script (Phase 4 English first)
3. [ ] Create basic curriculum-v3.html page
4. [ ] Test with sample data

---

## 💡 **INSPIRATION & REFERENCES**

**Good Curriculum Browsers:**
- UK National Curriculum Browser
- Australian Curriculum Portal
- Common Core State Standards (USA)

**What Makes Them Good:**
- Clean, minimal design
- Fast filtering
- Clear hierarchies
- Mobile-friendly

**What We'll Do Better:**
- Multi-version support (they don't have this)
- Comparison views
- Integration with our teaching resources
- Mātauranga Māori prominence

---

## 📞 **DECISION POINTS NEEDED**

**For User to Decide:**
1. Start with NZC 2007 or Phase 4 (2024)?
2. Build scraper ourselves or pay for Exa.ai?
3. GraphRAG or pure Supabase for storage?
4. Ship Phase 1 fast (2 weeks) or perfect everything first?
5. Manual verification sample size (10%? 25%?)?

---

---

## 🎯 **MY RECOMMENDATION AS OVERSEER**

### START IMMEDIATELY with Mini-MVP

**What:** English Phase 4 (Years 9-10) ONLY  
**Why:** Mandatory from Jan 1, 2026 (62 days away!)  
**How Long:** 8-12 hours  
**Ship Date:** This weekend (Nov 1-2)

**Deliverable:**
```
curriculum-v3.html
├─ Filter: Phase 4 only (hardcoded for now)
├─ Subject: English only
├─ Strands: Text Studies + Language Studies
├─ Elements: All 4 (Textual Analysis, Critical Analysis, Crafting Texts, Oral Comm)
└─ UI: Simple accordion, beautiful design, fast
```

**Then Get Teacher Feedback IMMEDIATELY:**
- Does this solve your problem?
- Is the verbatim accurate?
- What else do you need?

### Delegation Strategy:

**Use DeepSeek/Cheaper Models For:**  
[[memory:5721304]] - User prefers delegating monotonous tasks to cheaper models
- Scraping repetitive pages (once structure is proven)
- Data validation (character-level checks)
- CSV/JSON formatting
- Batch processing

**Use Claude (Me) For:**
- Architecture decisions
- UI/UX design
- Complex data modeling
- Quality verification
- Teacher-facing content

**Use Exa.ai For:**
- Automated web scraping (if you have API access)
- Bulk content extraction
- URL discovery

### Alternative: Start with What We Have

**If This is Too Ambitious Right Now:**
1. Improve curriculum-v2.html with better UI
2. Add Phase 4 English manually (type it in, just Phase 4)
3. See if teachers find it useful
4. Then decide if full automation worth it

---

## ⚡ **URGENT CONTEXT**

**TEACHERS NEED THIS BY JANUARY 1, 2026** (62 days!)

English & Math Phase 4 become **MANDATORY**. Every teacher in NZ will be scrambling to understand the new structure during summer break (Dec-Jan).

If we can ship English Phase 4 by early November:
- Teachers have 2 months to familiarize
- Te Kete Ako becomes THE reference tool
- We prove value before tackling full scope

**This could be HUGE for platform adoption.**

---

## 🤔 **DECISIONS NEEDED FROM YOU:**

1. **Do we tackle this now** or put it on backlog?
2. **If now:** Start with Mini-MVP (English Phase 4) or full build?
3. **Delegation:** Should I hand off scraping to DeepSeek once structure is proven?
4. **Quality bar:** 100% verbatim required or 95% good enough for MVP?
5. **Your time:** Can you help spot-check accuracy of scraped content?

---

**Next Update:** Awaiting your decisions  
**Owner:** Kaitiaki Aronui V3.0 (Claude Sonnet 4.5)  
**Priority:** 🔴 URGENT - 62 days until English/Math mandatory  
**Status:** Planned, awaiting go/no-go decision


