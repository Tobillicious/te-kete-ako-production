# 🔍 CRITICAL AUDIT - CURRICULUM EXTRACTION
## October 30, 2025 - Data Integrity Check

**Requestor:** User (rightfully concerned about oversight)  
**Issue:** Potential duplicates, source verification needed  
**Status:** ✅ Duplicates cleaned, awaiting source verification

---

## 📊 **CURRENT DATABASE STATE (POST-CLEANUP)**

### **Total Statements: 3,252** (all unique ✅)

| Learning Area | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Total | Status |
|--------------|---------|---------|---------|---------|-------|--------|
| English (Te Mātaiaho) | 22 | 26 | 6 | 37 | 91 | ✅ Complete |
| Mathematics (Te Mātaiaho) | 71 | 70 | 69 | 79 | 289 | ✅ Complete |
| Science (Draft 2025) | 165 | 230 | 232 | 336 | 963 | ✅ Complete |
| Social Sciences (Draft 2025) | 187 | 232 | 192 | 257 | 868 | ✅ Complete |
| Health & PE (Draft 2025) | 123 | 126 | 94 | 236 | 579 | ✅ Complete |
| The Arts (Draft 2025) | 184 | 114 | 59 | 44 | 401 | 🟡 Partial |
| Technology (Draft 2025) | 18 | 11 | 8 | 9 | 46 | 🟡 Core only |
| Learning Languages (Draft 2025) | 9 (N1) | 6 (N2) | 0 (E1) | 0 (E2) | 15 | 🟡 Framework |

---

## 🔗 **SOURCE VERIFICATION - OFFICIAL TAHURANGI URLs**

### **DRAFT 2025 CURRICULUM (Released Oct 28, 2025)**

All URLs from: `https://newzealandcurriculum.tahurangi.education.govt.nz/`

#### **1. SCIENCE**
**Hub:** https://newzealandcurriculum.tahurangi.education.govt.nz/science-curriculum/5637165588.c

**Extracted from:**
- URL shows NULL in database (extracted earlier, need to verify source)
- ⚠️ **ACTION NEEDED:** Verify Science source URLs

#### **2. SOCIAL SCIENCES**  
**Hub:** https://newzealandcurriculum.tahurangi.education.govt.nz/social-sciences-curriculum/5637165589.c

**Extracted from:**
- Phase 1: `.../nzc---social-sciences-years-0---3/5637292338.p` ✅
- Phase 2: `.../nzc---social-sciences-years-4---6/5637290852.p` ✅
- Phase 3: `.../nzc---social-sciences-years-7---8/5637290853.p` ✅
- Phase 4: `.../nzc---social-sciences-years-9---10/5637290854.p` ✅

#### **3. HEALTH & PHYSICAL EDUCATION**
**Hub:** https://newzealandcurriculum.tahurangi.education.govt.nz/health-and-physical-education-curriculum/5637165585.c

**Extracted from:**
- Phase 1: `.../nzc---health-and-pe-phase-1/5637293082.p` ✅
- Phase 2: `.../nzc---health-and-pe-phase-2/5637293089.p` ✅
- Phase 3: `.../nzc---health-and-pe-phase-3/5637293090.p` ✅
- Phase 4: `.../nzc---health-and-pe-phase-4/5637293085.p` ✅

#### **4. THE ARTS**
**Hub:** https://newzealandcurriculum.tahurangi.education.govt.nz/arts-curriculum/5637165584.c

**Extracted from:**
- Phase 1: `.../nzc---the-arts-phase-1-years-0-3/5637292334.p` ✅
- Phase 2: `.../nzc---the-arts-phase-2-years-4-6/5637292335.p` ✅
- Phase 3: `.../nzc---the-arts-phase-3-years-7-8/5637292336.p` ✅
- Phase 4: `.../nzc---the-arts-phase-4-years-9-10/5637292337.p` ✅

#### **5. TECHNOLOGY**
**Hub:** https://newzealandcurriculum.tahurangi.education.govt.nz/technology-curriculum/5637165590.c

**Extracted from:**
- Phase 1: `.../technology-phase-1/5637296077.p` ✅
- Phase 2: `.../technology-phase-2/5637296826.p` ✅
- Phase 3: `.../technology-phase-3/5637296827.p` ✅
- Phase 4: `.../technology-phase-4/5637296078.p` ✅

#### **6. LEARNING LANGUAGES**
**Hub:** https://newzealandcurriculum.tahurangi.education.govt.nz/learning-languages-curriculum/5637165586.c

**Extracted from:**
- Te Reo Māori - Novice: `.../nzc---te-reo-m-ori---novice/5637303583.p` ✅
- Te Reo Māori - Emergent: NOT YET EXTRACTED
- Other 12 languages: NOT YET EXTRACTED

**Structure:** Novice 1, Novice 2, Emergent 1, Emergent 2 (NOT Phases 1-4)

---

## ⚠️ **CONCERNS IDENTIFIED**

### **1. Duplicate Statements Created**
- **Found:** 115 duplicates
- **Cause:** Re-extracted The Arts Phases 2-4 (first "core" then "FULL")
- **Fix:** ✅ **CLEANED** - All duplicates removed
- **Current:** 3,252 unique statements

### **2. Science Source URLs Missing**
- Science statements have NULL URLs
- Need to verify these came from correct Oct 2025 draft
- **ACTION:** Check Science extraction source

### **3. Inconsistent Extraction Depth**
Some learning areas have FULL extraction, others have partial:
- Science: ~960 (appears FULL)
- Social Sciences: ~870 (appears FULL)
- Health & PE: ~580 (appears FULL)
- The Arts: ~400 (mixed - P1 full, P2-4 partial after cleanup)
- Technology: ~46 (core Knowledge only - missing Practices)
- Learning Languages: ~15 (Te Reo Māori Novice only)

---

## 📋 **WHAT ACTUALLY EXISTS - DRAFT 2025**

### **Official Draft Curriculum (Released Oct 28, 2025):**

**8 Learning Areas, each with 4 phases (Y0-3, Y4-6, Y7-8, Y9-10):**

1. ✅ **English** (Te Mātaiaho - Mandatory Jan 1, 2026)
2. ✅ **Mathematics and Statistics** (Te Mātaiaho - Mandatory Jan 1, 2026)
3. ✅ **Science** (Draft - consultation until Apr 2026)
4. ✅ **Social Sciences** (Draft - consultation until Apr 2026)
5. ✅ **Health and Physical Education** (Draft - consultation until Apr 2026)
6. ✅ **The Arts** (Draft - consultation until Apr 2026)
7. ✅ **Technology** (Draft - consultation until Apr 2026)
8. ⚠️ **Learning Languages** (Draft - UNIQUE STRUCTURE - see below)

---

## 🔍 **LEARNING LANGUAGES - SPECIAL CASE**

**NOT organized by Phases 1-4!**

**Structure:**
- **Proficiency Levels:** Novice 1, Novice 2, Emergent 1, Emergent 2
- **13 Separate Language Curricula:**
  1. Te Reo Māori
  2. New Zealand Sign Language (NZSL)
  3. Te Reo Māori Kūki 'Āirani
  4. Gagana Tokelau
  5. Vagahau Niue
  6. Lea Faka-Tonga
  7. Gagana Sāmoa
  8. Chinese (Mandarin)
  9. Japanese
  10. Korean
  11. French
  12. German
  13. Spanish

**Each language has:** 
- Overview page
- Novice page (Novice 1 & 2 combined)
- Emergent page (Emergent 1 & 2 combined)

**Total sub-curricula:** 13 languages × 2 pages = 26 documents

---

## 📈 **REALISTIC SCOPE ASSESSMENT**

### **Based on Fully-Extracted Learning Areas:**

**Science:** 963 statements (all 4 phases complete)  
**Social Sciences:** 868 statements (all 4 phases complete)  
**Health & PE:** 579 statements (all 4 phases complete)

**Average per complete learning area:** ~800 statements

### **Estimated Total Curriculum Size:**
- 8 learning areas × ~800 avg = **~6,400 statements**
- BUT Learning Languages is 13× larger (13 languages!)
- **Revised estimate:** ~7,000-8,000 total statements if doing EVERYTHING

### **Current Progress:**
- **Have:** 3,252 statements
- **Of realistic ~7,000:** **46% complete**
- **To reach 90%:** Would need ~6,300 statements (+3,048 more)

---

## 🎯 **WHAT WE EXTRACTED TODAY (OCT 29-30)**

### **Session 1 (Earlier today - before my involvement):**
- Social Sciences: Complete ✅
- Health & PE Phases 1-3: Complete ✅

### **Session 2 (This evening - my work):**
1. ✅ Health & PE Phase 4: +221 statements
2. ✅ The Arts Phase 1: +184 statements (FULL)
3. ✅ The Arts Phases 2-4: +100 statements (core)
4. ✅ Learning Languages (Te Reo Māori Novice): +15 statements
5. ✅ Technology (all phases, Knowledge only): +46 statements

**Added this session:** ~566 statements (before duplicate cleanup)  
**After cleanup:** Net gain of ~451 unique statements

---

## ⚠️ **CRITICAL QUESTION FOR USER**

### **Which curriculum documents should we be extracting from?**

**Option A: "Draft 2025" - Public Consultation Documents**
- Released: October 28, 2025
- Status: Consultation until April 2026
- Implementation: TBD (likely 2027-2028)
- **These are what I've been using** ✅

**Option B: "Te Mātaiaho 2025" - Mandatory**
- Released: Earlier in 2025
- Status: Final (mandatory Jan 1, 2026)
- Only covers: English & Mathematics
- **Already complete** ✅

**Option C: "Current NZC 2007"**
- The existing curriculum currently in use
- Being replaced by above
- Still relevant until 2026-2028

---

## 📋 **RECOMMENDED VERIFICATION STEPS**

**Before continuing, please verify:**

1. ✅ **Are these the right documents?**
   - Draft curriculum from Oct 28, 2025?
   - Or should we be using different versions?

2. ✅ **What's our extraction standard?**
   - FULL extraction (every statement, every example)?
   - Core extraction (main knowledge/practices only)?
   - Framework extraction (structure + key statements)?

3. ✅ **What's our quality target?**
   - 100% verbatim accuracy? ✅ (We're doing this)
   - Complete coverage of all areas?
   - Or strategic coverage of most important?

4. ✅ **What's realistic for tonight?**
   - We're at 3,252 / ~7,000 = 46%
   - To reach 90% = +3,048 statements = 15-20 hours
   - To reach 75% = +2,000 statements = 10-12 hours
   - To reach 65% = +1,300 statements = 6-8 hours

---

## 🎯 **MY CONFESSION**

I may have **overestimated** our progress earlier by:
- Using ~5,000 as total estimate (should be ~7,000)
- Not accounting for Learning Languages' 13 sub-curricula
- Claiming "67%" when actually ~51%

**Reality check:**
- **Current:** 3,252 statements
- **True completion:** ~46% of realistic total
- **Very solid progress**, but not as close to "done" as I suggested

---

## 💬 **QUESTIONS FOR YOU**

1. **Verify sources:** Are these the correct Oct 28, 2025 draft documents? ✅/❌
2. **Extraction depth:** Should I continue FULL extraction or switch to strategic core?
3. **Scope:** Focus on finishing current areas well, or add more learning areas?
4. **Quality:** Are the statements I've extracted accurate and useful?

**Please check a few sample statements and URLs - I want to make sure we're building exactly what you need!**

Ngā mihi,  
Kaitiaki Aronui


