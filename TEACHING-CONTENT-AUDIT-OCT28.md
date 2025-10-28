# 📚 COMPLETE TEACHING CONTENT AUDIT - October 28, 2025

## 🎯 PURPOSE
Manual audit of ALL teaching content to:
1. Identify which resources need which template types
2. Find missing/hidden lessons from units
3. Categorize handouts by layout needs
4. Create fix plan for each resource type

---

## 📊 INVENTORY SUMMARY

**Unit Plans:** 8  
**Lessons:** 35  
**Handouts:** 67  
**Total:** 110 teaching resources

---

## 📚 UNIT PLANS (8 total)

### Units with Complete Lesson Sets
1. ✅ **Unit 1: Te Ao Māori Foundations** (5/5 lessons)
   - unit-1-lesson-1.html → unit-1-lesson-5.html
   
2. ✅ **Unit 2: Decolonized History** (5/5 lessons)
   - unit-2-lesson-1.html → unit-2-lesson-5.html
   
3. ✅ **Unit 3: STEM & Mātauranga** (5/5 lessons)
   - unit-3-lesson-1.html → unit-3-lesson-5.html
   
4. ✅ **Unit 4: Economic Justice** (5/5 lessons)
   - unit-4-lesson-1.html → unit-4-lesson-5.html
   
5. ⚠️ **Unit 5: Globalization & Identity** (4/5 lessons - MISSING LESSON 5)
   - unit-5-lesson-1.html → unit-5-lesson-4.html
   - ❌ unit-5-lesson-5.html NOT FOUND
   
6. ✅ **Unit 6: Hauora & Wellbeing** (5/5 lessons)
   - unit-6-lesson-1.html → unit-6-lesson-5.html
   
7. ⚠️ **Unit 7: Digital Tech & AI** (3/5 lessons - MISSING LESSONS 4-5)
   - unit-7-lesson-1.html → unit-7-lesson-3.html
   - ❌ unit-7-lesson-4.html NOT FOUND
   - ❌ unit-7-lesson-5.html NOT FOUND

8. ⚠️ **Y8 Systems Unit** (3/10 lessons - MISSING 7 LESSONS)
   - systems-lesson-1-1.html (Module 1, Lesson 1)
   - systems-lesson-2-1.html (Module 2, Lesson 1)
   - systems-lesson-5-1.html (Module 5, Lesson 1)
   - ❌ Missing Modules 3, 4, and most lessons from all modules

### Missing Lessons Count: **8 lessons missing** (or not yet created)
- Unit 5: Lesson 5
- Unit 7: Lessons 4-5
- Y8 Systems: ~5 lessons (incomplete module structure)

---

## 📖 LESSON TEMPLATE NEEDS

**Current Status:** All 35 existing lessons have **CORRECT sidebar structure** ✅

**Template Requirements:**
- Single left sidebar with:
  - Whakataukī (auto-injected)
  - Unit Navigation widget
  - Related Resources widget (optional)
- Main content area
- Breadcrumbs with unit context
- Unit overview banner at top
- Save button (when auth works)

**Gold Standard:** `units/lessons/unit-2-lesson-1.html`

**Action Needed:** 
- ✅ Lessons are already correct - NO FIXES NEEDED
- 🆕 Create lesson-template.html based on unit-2-lesson-1.html structure
- 🆕 Create 10 missing lessons (or mark as intentionally omitted)

---

## 📄 HANDOUT TYPES & TEMPLATE NEEDS

### Type A: Content Handouts WITH Sidebar (for screen viewing + print)
**Count:** ~40-50 handouts  
**Purpose:** Rich content pages meant for digital viewing AND printing  
**Layout Needs:**
- Single left sidebar (whakataukī + related resources)
- Main content area
- Save button
- Print CSS hides sidebar/header/footer (prints body only to A4)

**Examples:**
- media-literacy-comprehension-handout.html
- treaty-of-waitangi-handout.html
- ai-ethics-and-bias.html

**Current Status:** 
- ✅ 33 have correct structure OR intentionally no sidebar
- ❌ 34 have **double sidebar bug**

### Type B: Simple A4 Print Worksheets (no sidebar)
**Count:** ~10-15 handouts  
**Purpose:** Clean printable worksheets, no sidebar needed  
**Layout Needs:**
- No sidebar
- Simple A4 page container
- Print button
- Designed to print beautifully as-is

**Examples:**
- probability-handout.html (simple math worksheet)
- Bar graph worksheets
- Fill-in-the-blank activities

**Current Status:** ✅ Already correct - NO FIXES NEEDED

### Type C: Enhanced/Experimental Handouts
**Count:** 4 handouts in `/handouts/enhanced/`  
**Purpose:** Advanced integrations, possibly different layout  
**Files:**
- climate-science-traditional-knowledge.html
- microplastics-matauranga-integration.html
- probability-matauranga-integration.html
- whakapapa-mathematical-thinking.html

**Action Needed:** Review individually to determine template needs

---

## 🔧 TEMPLATE REQUIREMENTS

### 1. **lesson-template.html** (for 35+ lessons)
- ✅ Based on: `units/lessons/unit-2-lesson-1.html`
- Single left sidebar (whakataukī + navigation)
- Breadcrumbs with unit context
- Unit banner with lesson progression
- Save button
- **Status:** NEEDS TO BE CREATED FROM GOLD STANDARD

### 2. **handout-with-sidebar-template.html** (for ~40 handouts)
- Based on: lessons structure BUT simpler
- Single left sidebar (whakataukī + related resources)
- No unit banner (handouts are standalone)
- Save button + Print button
- Print CSS hides sidebar
- **Status:** NEEDS TO BE CREATED

### 3. **handout-simple-a4-template.html** (for ~10 handouts)
- No sidebar
- Simple page container
- Print button only
- Clean A4 print layout
- **Status:** ALREADY EXISTS (probability-handout.html is good example)

### 4. **unit-template.html** (for 8 unit plans)
- Existing template seems okay
- **Status:** NEEDS REVIEW

---

## 🎯 FIX PRIORITY

### Phase 1: Perfect Templates (1-2 hours)
1. ✅ Identify gold standard (unit-2-lesson-1.html)
2. 🔨 Create `lesson-template-PERFECT.html` from gold standard
3. 🔨 Create `handout-with-sidebar-template-PERFECT.html`
4. 👀 Visual review with user in browser

### Phase 2: Audit All Handouts Manually (2-3 hours)
Create spreadsheet/document categorizing each of 67 handouts:
- Which template does it need? (sidebar vs simple A4)
- What's its current status? (correct, double sidebar bug, needs sidebar)
- What subject/year level? (for GraphRAG)
- Which unit does it belong to? (for relationships)

### Phase 3: Fix 34 Handouts with Double Sidebar Bug (3-4 hours)
Manually for each:
1. Remove duplicate sidebar inside `<main>`
2. Remove duplicate whakataukī
3. Ensure single main.content-area
4. Verify print CSS works
5. Test in browser

### Phase 4: Create Missing Lessons (TBD - may not be needed)
- 10 lessons missing from units
- Determine if intentionally omitted or need to be created

### Phase 5: Update GraphRAG (30 min)
- Index all fixed content
- Add structural relationships (unit → lessons, lessons → handouts)
- Add metadata (subjects, year levels, resource types)

---

## 📝 HANDOUT CATEGORIZATION (To Be Completed)

### Needs Manual Review - Each of 67 Handouts:

| Handout File | Template Needed | Current Status | Unit Link | Priority |
|-------------|-----------------|----------------|-----------|----------|
| media-literacy-comprehension-handout.html | Sidebar | Double Bug ❌ | Unit 5 | High |
| probability-handout.html | Simple A4 | Correct ✅ | Unit 5 | None |
| treaty-of-waitangi-handout.html | Sidebar | Double Bug ❌ | Unit 2 | High |
| ... | ... | ... | ... | ... |

**(This will be a separate detailed spreadsheet)**

---

## 🚀 NEXT IMMEDIATE ACTIONS

1. **Create perfected lesson template** from unit-2-lesson-1.html
2. **Create perfected handout-with-sidebar template** 
3. **Visual review both templates** in browser with user
4. **Begin manual handout audit** with spreadsheet
5. **Fix handouts one-by-one** (no batch scripts - too risky)

---

## 💡 KEY INSIGHTS

**Why Manual?**
- 67 handouts × different purposes = can't safely automate
- Need human judgment: Does this need a sidebar? 
- Risk of breaking working content with scripts
- Better to be slow and surgical

**Why Multiple Templates?**
- Lessons have unit context (breadcrumbs, banners, navigation)
- Handouts are standalone (simpler)
- Print worksheets need minimal chrome
- One template doesn't fit all use cases

**Print Behavior:**
- ALL handouts (with or without sidebar) should print nicely to A4
- Print CSS hides header, footer, sidebar, buttons
- Only body content prints
- Already working for most handouts ✅

---

**Created:** October 28, 2025  
**Next Step:** Create perfected templates for user review

