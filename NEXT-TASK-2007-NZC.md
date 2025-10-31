# 📚 NEXT TASK: 2007 NZC Curriculum Extraction

**Assigned To:** Kaiārahi Tūhono  
**Assigned By:** Kaitiaki Aronui  
**Date:** October 31, 2025  
**Priority:** HIGH  
**Complexity:** MAJOR PROJECT  
**Estimated Time:** 2-3 hours

---

## 🎯 MISSION

Extract the **entire 2007 New Zealand Curriculum** (legacy system) and load it into our database.

**Current Status:** We have ZERO 2007 NZC data in database  
**Target:** ~800-1000 curriculum objectives across all learning areas  
**Impact:** Teachers transitioning from 2007 → 2025 curriculum need this reference

---

## 📊 SCOPE

### Learning Areas to Extract:

1. **English** (~100 objectives, Levels 1-8)
2. **Mathematics** (~100 objectives, Levels 1-8)  
3. **Science** (~100 objectives, Levels 1-8)
4. **Social Sciences** (~100 objectives, Levels 1-8)
5. **The Arts** (~100 objectives, Levels 1-8)
6. **Health & Physical Education** (~100 objectives, Levels 1-8)
7. **Technology** (~100 objectives, Levels 1-8)
8. **Learning Languages** (~100 objectives, Levels 1-8)

**Total Estimate:** 800-1000 objectives

---

## 🔍 DATA SOURCE

**Primary:** https://nzcurriculum.tki.org.nz/  
(This is the official 2007 NZC archive)

**Structure:**
- Each learning area has 8 curriculum levels
- Each level has multiple achievement objectives
- Organized by strands (varies by subject)

---

## 🛠️ YOUR APPROACH (Recommended)

### Phase 1: Research & Planning (30 mins)

1. **Browse the 2007 NZC site:**
   - Understand the structure
   - Identify all learning areas
   - Map out strand organization
   - Document URL patterns

2. **Design extraction strategy:**
   - Manual vs automated scraping?
   - Data format decisions
   - Database schema alignment

### Phase 2: Build Scraper (60 mins)

1. **Create new scraper script:**
   ```bash
   scripts/curriculum-scraper/scrape_2007_nzc.py
   ```

2. **Requirements:**
   - Extract all achievement objectives
   - Capture: Learning Area, Level, Strand, Objective Text
   - Map to our database schema format
   - Generate SQL INSERT statements

3. **Test thoroughly:**
   - Start with ONE learning area (English)
   - Verify data quality
   - Check database compatibility

### Phase 3: Full Extraction (60 mins)

1. **Run scraper for all 8 learning areas**
2. **Generate complete SQL file**
3. **Validate data quality**
4. **Load into database**

### Phase 4: Verification (30 mins)

1. **Quality checks:**
   - Correct count (~800-1000 objectives)
   - No duplicates
   - All fields populated correctly
   - Proper curriculum_version tagging

2. **Test in curriculum-v3.html:**
   - Switch to "2007 NZC (Legacy)"
   - Verify filters work
   - Test search functionality

---

## 📋 DATABASE SCHEMA MAPPING

Map 2007 structure to our schema:

```sql
INSERT INTO curriculum_statements (
  curriculum_version,     -- 'nzc_2007'
  learning_area,          -- e.g., 'English', 'Mathematics'
  phase,                  -- NULL (2007 uses levels not phases)
  year_levels,            -- Array mapping from level (e.g., Level 1 = [1,2])
  strand,                 -- e.g., 'Reading', 'Number'
  sub_strand,             -- NULL or specific sub-category
  element,                -- 'Achievement Objective' (all are AOs in 2007)
  statement_text,         -- The actual objective text
  statement_order,        -- Sequential ordering
  curriculum_level        -- 1-8 (2007 specific field)
) VALUES (...);
```

### Level → Year Mapping:

- Level 1 → Years 1-2
- Level 2 → Years 3-4
- Level 3 → Years 5-6  
- Level 4 → Years 7-8
- Level 5 → Years 9-10
- Level 6 → Years 11-12
- Level 7 → Years 12-13
- Level 8 → Years 13+

---

## 🎯 SUCCESS CRITERIA

**You're done when:**

✅ All 8 learning areas extracted  
✅ ~800-1000 objectives loaded into database  
✅ Data quality verified (no duplicates, all fields populated)  
✅ curriculum-v3.html shows "2007 NZC (Legacy)" option working  
✅ Search/filter functionality working for legacy curriculum  
✅ SQL migration file created and documented  
✅ Audit report delivered to Kaitiaki

---

## 📡 COMMUNICATION PROTOCOL

**Progress Updates (every 60 mins):**
```bash
curl -X POST http://localhost:3002/messages/send \
  -H "Content-Type: application/json" \
  -d '{
    "from": "Kaiārahi Tūhono",
    "to": "Kaitiaki Aronui",
    "message": "Progress: Phase 2 complete. English extraction working. 127 objectives extracted. Moving to Mathematics next.",
    "priority": "normal",
    "metadata": {
      "phase": "2_scraper_build",
      "progress": 40,
      "objectives_extracted": 127
    }
  }'
```

**When Blocked:**
```bash
# HIGH priority message asking for help
```

**When Complete:**
```bash
curl -X POST http://localhost:3002/messages/send \
  -H "Content-Type: application/json" \
  -d '{
    "from": "Kaiārahi Tūhono",
    "to": "Kaitiaki Aronui",
    "message": "2007 NZC EXTRACTION COMPLETE ✅ Total: 847 objectives across 8 learning areas. All loaded and verified. Deliverables ready.",
    "priority": "high",
    "metadata": {
      "status": "complete",
      "objectives_extracted": 847,
      "learning_areas": 8
    }
  }'
```

---

## 📦 DELIVERABLES

1. **Scraper Script:**  
   `scripts/curriculum-scraper/scrape_2007_nzc.py`

2. **SQL Migration:**  
   `supabase/migrations/20251031_nzc_2007_curriculum.sql`

3. **Audit Report:**  
   `/tmp/2007-nzc-extraction-report.txt`

4. **Data Summary:**  
   `/tmp/2007-nzc-data-summary.txt`  
   (Counts by learning area, strand, level)

---

## 💡 TIPS FOR SUCCESS

**1. Start Small:**  
Begin with ONE learning area (English). Get it perfect. Then scale.

**2. Be Methodical:**  
Document URL patterns, test data quality, verify at each step.

**3. Ask for Help:**  
If the 2007 site structure is confusing, send HIGH priority message.

**4. Quality > Speed:**  
Take your time. This is legacy data—accuracy is critical for teacher trust.

**5. Test Everything:**  
After loading, test in curriculum-v3.html to ensure it works.

---

## 🚀 AUTONOMY LEVEL: FULL

You have **complete autonomy** on:
- How to extract the data (manual, automated, hybrid)
- Technical approach (scraping library choices)
- Order of learning areas to process
- Time management

**Just deliver:**
- High-quality data
- ~800-1000 objectives
- Working integration with UI
- Professional audit report

---

## ⏰ TIMELINE FLEXIBILITY

**Estimated:** 2-3 hours  
**But:** Take as long as you need!

Quality > Speed. If it takes 4-5 hours to do it right, that's fine.

Check in every 60 minutes so I know you're not stuck.

---

## 🌟 WHY THIS MATTERS

Teachers at Mangakōtukutuku College are **transitioning** from 2007 NZC to Te Mātaiaho 2025.

Without 2007 data, they can't:
- Compare old vs new curriculum
- Map existing lessons to new standards
- Understand what changed
- Plan transition strategy

**This extraction makes Te Kete Ako the ONLY platform in NZ with both legacy and new curriculum searchable in one place!**

---

## 📚 RESOURCES

**2007 NZC Official Site:**  
https://nzcurriculum.tki.org.nz/

**Your Existing Scraping System:**  
`scripts/curriculum-scraper/` (33 files - reference these!)

**Database Schema:**  
`supabase/migrations/20251029_curriculum_v3_schema.sql`

**Testing Framework:**  
`scripts/test_semantic_search.py`

---

## ✅ PRE-FLIGHT CHECKLIST

Before starting:

- [ ] Read this entire brief
- [ ] Browse 2007 NZC site to understand structure
- [ ] Review existing scraper code for patterns
- [ ] Check database schema for field requirements
- [ ] Confirm Supabase access working
- [ ] Send "STARTING 2007 NZC EXTRACTION" message
- [ ] Begin Phase 1: Research

---

## 🎓 KAIĀRAHI TŪHONO - THIS IS YOUR TIME TO SHINE!

Your first audit was **EXCELLENT**.

This extraction is **BIGGER**, **HARDER**, and **MORE IMPORTANT**.

But I trust you completely.

**Take your time. Do it right. Ask for help if needed.**

When you're done, we'll have built something **NO OTHER NZ EDUCATION PLATFORM HAS**.

---

**Kia kaha, Kaiārahi Tūhono!**  
**E kore au e ngaro, he kākano i ruia mai i Rangiātea**  
*I will never be lost, for I am a seed sown from Rangiātea*

🚀 **START WHEN READY!**

---

*Awaiting your "STARTING" confirmation message...*

📡 MCP Server: http://localhost:3002

