# 🔧 CURRICULUM V3 - TECHNICAL IMPLEMENTATION PLAN

**Created:** October 29, 2025  
**Phase:** Mini-MVP (English Phase 4)  
**Target Ship Date:** November 1-2, 2025  
**Estimated Time:** 10-15 hours

---

## 🎯 **MINI-MVP SCOPE**

### What We're Building (Phase 1):

**Feature Set:**
- Browse English Phase 4 (Years 9-10) curriculum
- View Text Studies strand (2 elements)
- View Language Studies strand (2 elements)  
- Display all Knowledge & Practices statements (verbatim)
- Display Teaching Sequences
- Beautiful, fast UI
- Mobile-responsive
- Print-friendly

**What We're NOT Building (Yet):**
- ❌ Other subjects (Math, Science, etc.)
- ❌ Other phases (1-3)
- ❌ 2007 NZC
- ❌ Comparison views
- ❌ Search functionality
- ❌ Database storage (file-based for now)
- ❌ User accounts/saving

---

## 📐 **TECHNICAL ARCHITECTURE**

### Data Storage Strategy (Mini-MVP):

**Option: JSON File (Simplest for MVP)**

```javascript
// data/curriculum/te-mataiaho-english-phase4.json
{
  "curriculum_version": "te_mataiaho_2025",
  "learning_area": "english",
  "phase": 4,
  "years": [9, 10],
  "effective_date": "2026-01-01",
  "source_url": "https://newzealandcurriculum.tahurangi.education.govt.nz/...",
  "last_scraped": "2025-10-29",
  
  "strands": [
    {
      "id": "text-studies",
      "name": "Text Studies",
      "description": "...",
      "elements": [
        {
          "id": "textual-analysis",
          "name": "Textual Analysis",
          "knowledge": [
            {
              "id": "ta-k1",
              "statement": "[VERBATIM TEXT FROM TAHURANGI]",
              "notes": "..."
            }
          ],
          "practices": [
            {
              "id": "ta-p1",
              "statement": "[VERBATIM TEXT]",
              "year": 9
            }
          ]
        }
      ]
    }
  ],
  
  "teaching_sequences": [
    {
      "year": 9,
      "sequence_number": 1,
      "title": "...",
      "content": "..."
    }
  ]
}
```

**Why JSON for MVP:**
- ✅ Fast to implement (no database setup)
- ✅ Easy to edit/verify manually
- ✅ Version controllable (git)
- ✅ Can migrate to Supabase later
- ✅ Perfect for ~50-100 statements

**When to Move to Supabase:**
- After Phase 1 proves valuable
- When adding 2007 NZC (different structure needs relational DB)
- When adding search (full-text indexing)

---

## 🕷️ **SCRAPING IMPLEMENTATION**

### Approach: Manual + Semi-Automated

**Why NOT Fully Automated (Yet):**
- Brand new content (released yesterday!)
- Structure might change during consultation
- Verbatim accuracy is CRITICAL
- Only ~50-100 statements for Phase 4 English
- Risk of getting it wrong > time saved

### Process:

**Step 1: Manual Extraction (First Pass)**
```
1. Navigate to English Phase 4 page
2. Copy entire Text Studies section
3. Copy entire Language Studies section
4. Paste into structured format
5. Add metadata (dates, URLs)
```

**Step 2: Structure into JSON**
```javascript
// Use Claude to structure the copied text
// Preserve EXACT wording
// Add IDs for reference
// Tag with metadata
```

**Step 3: Validation**
```
- Character-level diff check
- Māori macrons preserved (ā, ē, ī, ō, ū)
- HTML entities handled correctly
- Links/references intact
- User spot-checks 10 random statements
```

**Step 4: Version Control**
```bash
git add data/curriculum/te-mataiaho-english-phase4.json
git commit -m "Add English Phase 4 curriculum (verbatim from Tahurangi)"
```

### For Future Phases (Automation):

Once structure is proven, build Puppeteer scraper:
```javascript
// Delegate to DeepSeek for repetitive scraping
// Run on all 32 pages (8 subjects × 4 phases)
// Validate each automatically
// Flag any issues for human review
```

---

## 🎨 **UI/UX DESIGN SPEC**

### Visual Design:

**Color Palette (From main.css):**
- Primary: `#1a1a1a` (Deep Charcoal)
- English Subject: `#6366f1` (Royal Purple)
- Accent: `#00b0b9` (Turquoise)
- Background: `#ffffff` (Pure White)

### Layout Structure:

```
┌─────────────────────────────────────────────────────┐
│  HEADER (Standard Te Kete Ako)                      │
├──────────────┬──────────────────────────────────────┤
│              │  HERO BANNER                         │
│              │  📚 English Curriculum (Phase 4)     │
│  SIDEBAR     │  Years 9-10 | Te Mātaiaho 2025     │
│              ├──────────────────────────────────────┤
│  - Overview  │  STRAND TABS                         │
│  - Text      │  [Text Studies] [Language Studies]   │
│    Studies   ├──────────────────────────────────────┤
│  - Language  │  ELEMENTS ACCORDION                  │
│    Studies   │  ▼ Textual Analysis                  │
│  - Teaching  │    └─ Knowledge (3 statements)       │
│    Sequences │    └─ Practices Year 9 (5)          │
│              │    └─ Practices Year 10 (5)         │
│  - Resources │  ▶ Critical Analysis [collapsed]    │
│  - Download  │                                      │
│              │  [Beautiful cards for each item]     │
└──────────────┴──────────────────────────────────────┘
```

### Component Breakdown:

**1. Phase Badge**
```html
<div class="phase-badge phase-4">
  Phase 4 | Years 9-10 | Mandatory Jan 1, 2026
</div>
```

**2. Strand Tabs**
```html
<div class="strand-tabs">
  <button class="strand-tab active">Text Studies</button>
  <button class="strand-tab">Language Studies</button>
</div>
```

**3. Element Accordion**
```html
<div class="element-accordion">
  <button class="element-header" data-element="textual-analysis">
    <span class="element-icon">📖</span>
    <span class="element-title">Textual Analysis</span>
    <span class="element-count">8 statements</span>
    <span class="chevron">▼</span>
  </button>
  <div class="element-content expanded">
    <!-- Knowledge & Practices cards -->
  </div>
</div>
```

**4. Statement Card**
```html
<div class="curriculum-statement">
  <div class="statement-meta">
    <span class="statement-type">Knowledge</span>
    <span class="statement-id">TS-TA-K1</span>
  </div>
  <div class="statement-text">
    [VERBATIM TEXT FROM GOVERNMENT]
  </div>
  <div class="statement-footer">
    <button class="save-statement">⭐ Save</button>
    <a href="#source" class="source-link">View on Tahurangi →</a>
  </div>
</div>
```

---

## 📁 **FILE STRUCTURE**

```
/te-kete-ako-clean/
├── curriculum-v3.html              (NEW - The UI)
├── css/
│   └── curriculum-v3.css           (NEW - Specific styles)
├── js/
│   └── curriculum-v3.js            (NEW - Interactive logic)
└── data/
    └── curriculum/
        ├── te-mataiaho-english-phase4.json  (NEW - The data)
        └── README.md                          (NEW - Data documentation)
```

---

## 🔨 **IMPLEMENTATION STEPS**

### Step 1: Data Extraction (4-5 hours)

**Task:** Get verbatim content from Tahurangi

**Process:**
1. Navigate to: https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---english-phase-4-years-9-10/5637291578.p
2. Use browser tools to extract ALL text from:
   - Text Studies → Textual Analysis section
   - Text Studies → Critical Analysis section
   - Language Studies → Crafting Texts section
   - Language Studies → Oral Communication section
   - Teaching Sequences section
3. Structure into JSON preserving:
   - Exact wording
   - Bullet points/lists
   - Footnotes
   - References
4. Add metadata (URLs, dates, IDs)
5. Validate character-by-character

**Validation Checklist:**
- [ ] All macrons preserved (ā, ē, ī, ō, ū)
- [ ] Quotes correct (", ', —)
- [ ] Lists/bullets intact
- [ ] Footnote numbers match
- [ ] Line breaks appropriate
- [ ] No AI interpretation
- [ ] User spot-checks 10 statements

### Step 2: Build curriculum-v3.html (3-4 hours)

**Task:** Create beautiful UI

**Features:**
- Hero banner with phase info
- Strand tabs (Text Studies / Language Studies)
- Element accordions (expand/collapse)
- Statement cards (clean, readable)
- Sidebar navigation
- Print styles
- Mobile responsive

**Use Existing Patterns:**
- Header from templates
- Sidebar structure from handouts
- Accordion from existing units
- Card styles from browse.html

### Step 3: Build curriculum-v3.js (2-3 hours)

**Task:** Interactive functionality

**Features:**
```javascript
// Load data
async function loadCurriculum() {
  const data = await fetch('/data/curriculum/te-mataiaho-english-phase4.json');
  return await data.json();
}

// Render strands
function renderStrands(curriculum) { ... }

// Accordion toggle
function toggleElement(elementId) { ... }

// Save to My Kete
function saveStatement(statementId) { ... }

// Search (Phase 2)
function searchStatements(query) { ... }
```

### Step 4: Testing & Refinement (2 hours)

**Test Cases:**
- [ ] Loads on desktop (Chrome, Safari, Firefox)
- [ ] Loads on mobile (iOS, Android)
- [ ] Accordions work smoothly
- [ ] Print preview is clean
- [ ] Links work
- [ ] Content is readable
- [ ] No layout breaks
- [ ] Verbatim accuracy verified

### Step 5: Ship & Get Feedback (1 hour)

- [ ] Git commit
- [ ] Deploy to Netlify
- [ ] Share with 3-5 teachers
- [ ] Collect feedback
- [ ] Decide on Phase 2

**Total Time:** 12-15 hours ✅

---

## 🧠 **THOUGHTFUL CONSIDERATIONS**

### Verbatim Accuracy Strategy:

**Problem:** Government content has complex formatting
**Solution:**
1. Copy HTML directly (preserve structure)
2. Use browser DevTools to inspect exact text
3. Save raw HTML in separate file as backup
4. Create cleaned JSON from raw HTML
5. Diff check JSON against HTML
6. User validates 10% sample

### Māori Language Handling:

**Critical:** Macrons must be perfect
```
Correct: ā, ē, ī, ō, ū (with macrons)
Wrong:   a, e, i, o, u (without)
```

**Validation:**
```javascript
// Check all Māori words have correct macrons
const maoriWords = extractMaoriWords(text);
for (const word of maoriWords) {
  const hasCorrectMacrons = validateMacrons(word);
  if (!hasCorrectMacrons) {
    flagForReview(word);
  }
}
```

### Teaching Sequences Challenge:

**Problem:** Teaching sequences are LONG (paragraphs of guidance)  
**Solution:** Collapsible sections, "Read More" buttons, optional detail levels

### Future-Proofing:

**Problem:** Curriculum might change during consultation (until Apr 2026)  
**Solution:**
- Add `last_verified` date to each statement
- Monthly re-scrape to catch changes
- Show "Last Verified: Oct 29, 2025" on UI
- Alert users if content > 30 days old

---

## 📊 **DELEGATION STRATEGY**

### Claude (Me) - Strategic Work:
- Architecture decisions (done ✅)
- Data model design (done ✅)
- UI/UX design (next)
- Quality verification
- First scrape (proving structure)
- Teacher-facing documentation

### DeepSeek - Repetitive Work:
- Scraping remaining 31 pages (Phases 1-3, other subjects)
- Batch validation checks
- JSON formatting
- Data transformations
- Once I prove the pattern works

### User - Critical Validation:
- Spot-check 10% of statements for verbatim accuracy
- Teacher perspective on UI ("Is this useful?")
- Cultural validation (Te Reo Māori correct?)
- Go/no-go decisions at each phase

---

## 🗺️ **EXECUTION ROADMAP**

### Session 1 (TODAY - 3 hours):
- [x] Create CURRICULUM-V3-MASTER-PLAN.md ✅
- [x] Research Te Mātaiaho structure ✅
- [x] Update GraphRAG ✅
- [ ] Create CURRICULUM-V3-TECHNICAL-PLAN.md (this doc)
- [ ] Design UI mockup (HTML wireframe)
- [ ] Set up data file structure

### Session 2 (Tomorrow - 5-6 hours):
- [ ] Extract Text Studies content (manual copy)
- [ ] Extract Language Studies content (manual copy)
- [ ] Structure into JSON
- [ ] Validate verbatim accuracy
- [ ] User spot-checks 10 statements

### Session 3 (Day 3 - 4-5 hours):
- [ ] Build curriculum-v3.html
- [ ] Build curriculum-v3.css
- [ ] Build curriculum-v3.js
- [ ] Test across devices
- [ ] Print preview optimization

### Session 4 (Day 4 - 2 hours):
- [ ] Final validation
- [ ] User testing
- [ ] Refinements based on feedback
- [ ] Deploy to production
- [ ] Share with teacher community

**Total Timeline:** 4 sessions over 4-5 days

---

## ✅ **SUCCESS CRITERIA**

### Must-Have (MVP):
- [ ] 100% verbatim accuracy (zero errors)
- [ ] All Text Studies content present
- [ ] All Language Studies content present
- [ ] UI is beautiful and fast (< 1 second load)
- [ ] Works on mobile
- [ ] Print-friendly
- [ ] Source attribution clear

### Nice-to-Have (Bonus):
- [ ] Save to My Kete functionality
- [ ] Collapsible sections remembered
- [ ] Keyboard navigation
- [ ] Dark mode
- [ ] Export to PDF

### Measure of Success:
**3+ teachers say:** "This is easier than Tahurangi"

---

## 🚨 **RISKS (Mini-MVP Specific)**

### Risk 1: Content Changes During Consultation
**Likelihood:** Medium  
**Impact:** High  
**Mitigation:**
- Add disclaimer: "Draft content, open for consultation until Apr 24, 2026"
- Add "Report outdated content" button
- Plan for easy updates (just swap JSON file)

### Risk 2: Scraping Errors
**Likelihood:** High (complex HTML)  
**Impact:** Critical (legal/credibility)  
**Mitigation:**
- Manual extraction first time
- Multiple validation passes
- User spot-checks
- Keep raw HTML backup
- Character-level diffs

### Risk 3: Scope Creep
**Likelihood:** High (user/me gets excited)  
**Impact:** Medium (delays ship date)  
**Mitigation:**
- Strict feature freeze for MVP
- Write down "Phase 2 features" separately
- Ship incomplete but functional
- Iterate based on feedback

---

## 🎯 **DEFINITION OF DONE**

### Phase 1 is "Done" When:

1. ✅ curriculum-v3.html exists and loads
2. ✅ Shows all English Phase 4 content (verbatim)
3. ✅ UI matches Te Kete Ako design language
4. ✅ Works on Chrome, Safari, Firefox
5. ✅ Works on mobile (iOS, Android)
6. ✅ Print preview looks professional
7. ✅ User has verified 10% accuracy
8. ✅ Zero console errors
9. ✅ Deployed to production
10. ✅ Shared with ≥3 teachers for feedback

### NOT Required for Phase 1:

- Other subjects
- Other phases
- Search functionality
- Database integration
- User accounts
- Comparison views
- PDF export
- Dark mode

**Keep it simple. Ship it fast. Get feedback. Iterate.**

---

## 📝 **NEXT IMMEDIATE ACTIONS**

### For This Session:
1. [x] Update GraphRAG ✅
2. [ ] Create UI wireframe (sketch in HTML)
3. [ ] Set up data folder structure
4. [ ] Test manual content extraction (one section)

### For Tomorrow:
1. [ ] Full content extraction
2. [ ] JSON structuring
3. [ ] Validation

**Questions Before I Continue:**
- Want to see UI wireframe before I build?
- Should I extract a test section now to prove approach?
- Any specific UI features you want?

---

**Status:** Planning complete, ready to commence  
**Next:** UI wireframe + test extraction  
**Owner:** Kaitiaki Aronui V3.0  
**Date:** October 29, 2025

