# 🎓 LESSON ENRICHMENT SYNTHESIS - Research Complete

**Date:** October 19, 2025  
**Research Phase:** COMPLETE - Ready for intelligent enrichment  
**Based on:** GraphRAG intelligence + Enhancement docs + Gold lesson analysis

---

## ✅ WHAT I NOW UNDERSTAND

### 1. **TEACHING VARIANTS STRATEGY** ✓

**The System:**
- Duplicates are INTENTIONAL, not mistakes
- Each lesson → synthesize to 2-3 DISTINCT pedagogical variants
- Variants based on cultural principles:
  - **Inquiry-Based** (Rangatiratanga - self-determination)
  - **Collaborative** (Whanaungatanga - relationships)
  - **Guided Learning** (Ako - reciprocal teaching)
  - **Project-Based** (Kotahitanga - unity)
  - **Experiential** (Manaakitanga - generosity of experience)

**Why This Matters:**
- Teachers choose which approach fits their ākonga
- Different classes need different approaches
- Cultural principles embedded in pedagogy
- Maximum 3 variants = choice without overwhelm

**Files Built:**
- `teaching-variant-generator.js` ✅
- `teaching-variants-synthesizer.js` ✅
- `teaching-variants-card.html` component ✅

---

### 2. **MULTI-PASS ENRICHMENT PROTOCOL** ✓

**The 7 Passes (Systematic Enhancement):**

1. **Pass 1: Technical Foundation** ✅ COMPLETE
   - CSS/JS/navigation infrastructure

2. **Pass 2: Navigation & Discovery** ✅ COMPLETE
   - Breadcrumbs, hub links

3. **Pass 3: Learning Structure** 🔄 4% COMPLETE (current)
   - WALT, Success Criteria, DO NOW, timing

4. **Pass 4: Teacher Resources** ⏭️ PENDING
   - Answer keys, rubrics, implementation guides

5. **Pass 5: Cultural Enhancement** ⏭️ PENDING
   - Whakataukī, te reo verification, house values

6. **Pass 6: Assessment Tools** ⏭️ PENDING
   - Formative checkpoints, exit tickets, reflection

7. **Pass 7: Professional Polish** ⏭️ PENDING
   - Visual consistency, accessibility, mobile

**Current Status:** 662 lessons need Passes 3-7

---

### 3. **GOLD STANDARD (10/10 Quality)** ✓

**Required Components (6-Level Nested Completeness):**

**MUST HAVE:**
1. ✅ **DO NOW Activity** (5-10 mins, hook ākonga immediately)
2. ✅ **Cultural Opening** (karakia, whakataukī, tikanga)
3. ✅ **Learning Intentions (WALT)** - Clear "We Are Learning To..."
4. ✅ **Success Criteria (SC)** - Clear indicators of success (NOT "WILF" - inappropriate for teenagers!)
5. ✅ **Explicit Teaching** (main content, minute-by-minute)
6. ✅ **Guided Practice (WAGOLL)** - "What A Good One Looks Like"
7. ✅ **Independent Practice** - Mahi for ākonga (tasks, activities)
8. ✅ **Assessment Checkpoints** - Formative + summative
9. ✅ **Extension Activities** - For advanced learners
10. ✅ **Reflection & Consolidation** - Synthesis, exit ticket
11. ✅ **Teacher Resources** - Answer keys, rubrics, implementation guide
12. ✅ **Student Materials** - Handouts, worksheets, readings
13. ✅ **Supporting Materials** - PowerPoint, audio, interactive

**MUST SOUND LIKE:**
- Written by experienced NZ kaiako (teachers)
- Uses NZ educational jargon: "ākonga" (students), "kaiako" (teacher), "mahi" (work)
- References NZ Curriculum Achievement Objectives VERBATIM
- Uses phrases like: "WALT", "Success Criteria", "DO NOW", "exit ticket", "tuakana-teina"
- Cultural safety language: "whānau", "iwi", "kaumātua", "cultural protocols"

---

### 4. **NZ CURRICULUM INTEGRATION** ✓

**MUST BE VERBATIM:**
- Pull from `/public/data/nzc.json` (NZ Curriculum achievement objectives)
- Example: "Understand how people participate individually and collectively in response to community challenges." (NZC-SS-4-1)
- Not paraphrased - EXACT curriculum language

**House Leader Values (Mangakōtukutuku College):**
- **Whaimana:** Integrity - standing firm in truth
- **Whaiora:** Wellbeing - holistic health
- **Whaiara:** Rising up - aspiration and excellence

**House Leaders:**
- Walker, Hērangi, Ngata, Hopa, Rickard, Wētere

---

### 5. **WHAT ĀKONGA NEED (Activities/Mahi)** ✓

**Students MUST HAVE things to DO:**
- Tasks to complete (on Chromebook)
- Questions to answer
- Worksheets to fill out
- Mahi to work on
- Discussions to have
- Projects to create
- Reflections to write

**NOT:** Just reading passively - they need ACTIVE ENGAGEMENT

**Examples from Gold Lessons:**
- "Write a 200-word reflection addressing..."
- "In small groups, brainstorm..."
- "Create your own digital story using..."
- "Analyze a traditional pūrākau and identify..."
- "Complete the My Digital Rangatiratanga Statement handout"

---

## 🎯 WHAT I'VE LEARNED FROM GOLD LESSONS

**Lesson 15: Digital Rangatiratanga (95/100):**
- Four kaiako voices (Tikanga, Hauora, Pūtaiao, Toi)
- Lesson phases with timing: Whakatūwhera (15 mins), Main Learning (40 mins), etc.
- Multiple assessment types: formative, self, peer, portfolio
- External resources from NZ government sites (teara.govt.nz, netsafe.org.nz)
- "The Leader in the Mirror" - evocative activity names
- Silent reflective writing workshop
- Volunteer sharing (optional, respects ākonga autonomy)

**Key Insight:** Gold lessons TELL A STORY, not just list activities

---

## 🚀 HIGH-LEVEL RECOMMENDATIONS FOR TODAY

### **PRIORITY 1: BUILD GRAPHRAG ENRICHMENT ENGINE**

**Problem:** 662 lessons need enrichment across Passes 3-7  
**Solution:** Build AI-powered enrichment system that LEARNS from gold lessons

**Create:**
```
/scripts/intelligent-lesson-enricher.py
```

**What it does:**
1. **Learn from Gold** - Analyze all 95+ quality lessons
   - Extract patterns (DO NOW structures, WALT formats, assessment types)
   - Build templates from actual excellence
   - Store patterns in GraphRAG

2. **Enrich with Intelligence**
   - Read lesson content
   - Identify which Pass (3-7) needed
   - Apply appropriate enrichment based on learned patterns
   - Use NZ curriculum data from `/public/data/nzc.json`
   - Pull whakataukī from cultural database
   - Generate ākonga-focused activities (not generic)

3. **Create Variants**
   - Use `teaching-variant-generator.js` system
   - Generate 2-3 pedagogical approaches
   - Tag each variant properly
   - Store all in GraphRAG

4. **Quality Validate**
   - Score using quality rubric
   - Ensure 90+ target met
   - Flag for human review if needed

---

### **PRIORITY 2: GRAPHRAG AS LEARNING SYSTEM**

**Insight:** GraphRAG should GET SMARTER as we enrich

**Build into GraphRAG:**

**A) Pattern Library Table:**
```sql
CREATE TABLE enrichment_patterns (
  pattern_id SERIAL PRIMARY KEY,
  pattern_type TEXT, -- 'do_now', 'walt', 'wagoll', 'assessment'
  source_lesson TEXT, -- Which gold lesson taught us this
  pattern_structure JSONB, -- Actual pattern
  quality_score INT, -- How good is this pattern
  usage_count INT, -- How often used successfully
  nz_specific BOOLEAN -- Is this NZ-specific pedagogy
);
```

**B) Enrichment Log Table:**
```sql
CREATE TABLE enrichment_history (
  enrichment_id SERIAL PRIMARY KEY,
  lesson_path TEXT,
  pass_number INT, -- Which pass (3-7)
  before_quality INT,
  after_quality INT,
  patterns_applied JSONB,
  agent_id TEXT,
  timestamp TIMESTAMPTZ,
  human_reviewed BOOLEAN
);
```

**C) Teaching Variant Decisions Table:**
```sql
CREATE TABLE teaching_variants (
  variant_id SERIAL PRIMARY KEY,
  lesson_base_path TEXT, -- Original lesson
  variant_type TEXT, -- 'inquiry', 'collaborative', 'guided', 'project'
  cultural_principle TEXT, -- 'rangatiratanga', 'whanaungatanga', etc
  variant_path TEXT, -- Path to this variant
  recommended_for JSONB, -- Class types, scenarios
  quality_score INT,
  teacher_usage_count INT -- Track which variants teachers actually use
);
```

---

### **PRIORITY 3: AGENT PROTOCOL FOR ENRICHMENT**

**When enriching lessons, agents must:**

**BEFORE enriching:**
1. Query GraphRAG for enrichment patterns
2. Find similar gold lessons (same subject/year)
3. Check which pass (3-7) needed
4. Read NZ curriculum objectives for this topic

**DURING enrichment:**
1. Use patterns from gold lessons (don't invent)
2. Write in NZ kaiako voice
3. Create ACTUAL mahi for ākonga (not placeholders)
4. Link to actual handouts in GraphRAG
5. Pull verbatim curriculum objectives

**AFTER enrichment:**
1. Score using quality rubric
2. Log to enrichment_history table
3. Update lesson quality_score in graphrag_resources
4. Create GraphRAG relationships to patterns used

---

### **PRIORITY 4: BUILD "ENRICHMENT INTELLIGENCE DASHBOARD"**

**Create:** `/public/enrichment-dashboard.html`

**Shows agents:**
- Which lessons need which passes
- Quality scores before/after enrichment
- Patterns available to use
- Success rate by pattern
- Which gold lessons to study for each topic
- Real-time enrichment progress

**Makes enrichment:** Data-driven, not guesswork

---

### **PRIORITY 5: VARIANT SYNTHESIS AUTOMATION**

**Tool:** `/scripts/synthesize-variants-to-3.py`

**What it does:**
1. Find all duplicate lessons (same content, different paths)
2. Analyze differences (CSS system, cultural depth, pedagogy)
3. Score each variant
4. Select best 3 variants:
   - Variant 1: Highest quality (recommended)
   - Variant 2: Alternative pedagogical approach
   - Variant 3: Different cultural integration level OR time allocation
5. Archive remaining duplicates
6. Update GraphRAG with variant relationships

---

## 🧠 GRAPHRAG WORKFLOW IMPROVEMENTS

### **Current Workflow:** Agent reads docs → enriches lesson
### **Improved Workflow:** Agent queries GraphRAG → learns → enriches

**Enable agents to query:**

```sql
-- What patterns work for Year 8 Science DO NOW activities?
SELECT ep.pattern_structure, ep.usage_count
FROM enrichment_patterns ep
JOIN graphrag_resources r ON r.file_path = ep.source_lesson
WHERE r.year_level = 'Year 8' 
  AND r.subject = 'Science'
  AND ep.pattern_type = 'do_now'
  AND ep.quality_score >= 90
ORDER BY ep.usage_count DESC, ep.quality_score DESC;

-- Which whakataukī work for mathematics lessons?
SELECT DISTINCT metadata->>'whakatauki' as whakatauki
FROM graphrag_resources
WHERE subject = 'Mathematics'
  AND has_whakataukī = true
  AND quality_score >= 90;

-- Show me gold lessons I should study before enriching this topic
SELECT file_path, title, quality_score
FROM graphrag_resources
WHERE resource_type = 'Lesson'
  AND subject = $CURRENT_SUBJECT
  AND quality_score >= 93
ORDER BY quality_score DESC
LIMIT 5;
```

---

## 🎯 HIGH-LEVEL PLAN FOR TODAY

### **MORNING: Build Intelligence Infrastructure**

**Task 1: Extract Patterns from Gold Lessons (2-3 hours)**
```
python3 scripts/extract-patterns-from-gold.py
```
- Analyzes all 95+ quality lessons
- Extracts DO NOW patterns, WALT formats, assessment structures
- Stores in GraphRAG enrichment_patterns table
- Creates pattern library for reuse

**Task 2: Create Enrichment Intelligence Dashboard (1-2 hours)**
- Build visual dashboard showing enrichment progress
- Shows which lessons need which passes
- Displays available patterns to use
- Real-time quality tracking

---

### **AFTERNOON: Pilot Enrichment with Intelligence**

**Task 3: Enrich 10 Pilot Lessons Using Patterns (3-4 hours)**
- Select 10 lessons needing Pass 3
- Use extracted patterns (not invented content)
- Apply NZ curriculum objectives (verbatim)
- Create actual ākonga mahi (worksheets, questions, tasks)
- Log everything to GraphRAG enrichment_history

**Task 4: Build Variant Synthesizer (2 hours)**
```
python3 scripts/synthesize-variants-to-3.py
```
- Find duplicate lesson sets
- Analyze differences
- Select best 3 variants per lesson
- Tag with variant_type and recommended_for

---

### **EVENING: Review & Iterate**

**Task 5: Quality Review**
- Score pilot lessons using rubric
- Compare to gold standards
- Identify what worked / what didn't
- Refine patterns

**Task 6: Plan Next Batch**
- Based on learnings
- Scale to next 50 lessons
- Continuous improvement

---

## 💡 SUGGESTED GRAPHRAG IMPROVEMENTS

### **1. Add "Learning From Enrichment" Loop**
```javascript
// After each enrichment, learn what worked
async learnFromEnrichment(lessonPath, beforeScore, afterScore, patternsUsed) {
    const improvement = afterScore - beforeScore;
    
    // If improvement > 10 points, this pattern worked!
    if (improvement >= 10) {
        patternsUsed.forEach(pattern => {
            // Increment usage_count for successful patterns
            // Increase quality_score for this pattern
        });
    }
    
    // Store in enrichment_history for future agents to learn from
}
```

### **2. Add "Variant Decision Intelligence"**
```javascript
// When teacher views lesson, track which variant they choose
trackVariantUsage(lessonBase, variantChosen, teacherContext) {
    // Store: Which variant did teachers with Y8 low-decile classes prefer?
    // Learn: Inquiry-based works better for advanced classes
    // Adapt: Recommend variants based on teacher's class profile
}
```

### **3. Add "Quality Prediction"**
```javascript
// Before enriching, predict likely quality outcome
predictEnrichmentQuality(lesson, patterns, pass) {
    // Based on historical enrichments:
    // - Similar lessons that improved 15+ points
    // - Patterns that succeeded in this subject/year
    // - Agent's historical success rate
    // Helps prioritize which lessons to enrich first
}
```

### **4. Add "Cultural Authenticity Validator"**
```javascript
// Before storing enrichment, validate cultural content
validateCulturalContent(enrichedLesson) {
    // Check: Whakataukī used correctly?
    // Check: Te reo macrons present?
    // Check: Cultural safety language appropriate?
    // Check: House leader values connected authentically?
    // Flag for cultural expert review if unsure
}
```

---

## 🚀 TODAY'S EXECUTION PLAN

### **OPTION A: Build the Infrastructure (Recommended)**
**Time:** Full day (8 hours)  
**Impact:** Makes ALL future enrichment smarter and faster

**Build:**
1. Pattern extraction system
2. Enrichment history tracking
3. Variant synthesis tool
4. Intelligence dashboard

**Why:** One day investment = 10x faster enrichment forever

---

### **OPTION B: Manual Enrichment Learning**
**Time:** Full day  
**Impact:** 10-20 lessons enriched, patterns learned manually

**Process:**
1. Read 10 gold lessons completely
2. Extract patterns manually
3. Enrich 10 pilot lessons
4. Document learnings

**Why:** Hands-on learning, slower but educational

---

### **OPTION C: Hybrid Approach**
**Time:** Full day  
**Impact:** Some infrastructure + some enrichment

**Morning:**
1. Extract patterns from 10 gold lessons (manual)
2. Store in GraphRAG enrichment_patterns table
3. Build simple pattern query tool

**Afternoon:**
4. Use patterns to enrich 5 pilot lessons
5. Track quality improvements
6. Iterate

---

## 🎯 MY RECOMMENDATION: OPTION A

**Why?**
- 662 lessons need enrichment (not just 10)
- Building intelligence makes future work 10x faster
- GraphRAG becomes self-improving system
- Agents can query patterns instead of guessing
- Quality is consistent (learned from gold, not invented)

**After today:**
- Future agents can enrich 50+ lessons/day (vs 10)
- Every enrichment makes GraphRAG smarter
- Patterns proven to work at gold level
- Cultural authenticity validated systematically

---

## ✅ WHAT TO BUILD TODAY

**1. `/scripts/extract-gold-patterns.py`**
- Analyze all 95+ quality lessons
- Extract: DO NOW formats, WALT structures, assessment types, cultural openings
- Store in enrichment_patterns table

**2. `/scripts/intelligent-lesson-enricher.py`**
- Query patterns from GraphRAG
- Apply to lessons needing enrichment
- Log results for learning loop

**3. `/public/enrichment-dashboard.html`**
- Visual progress tracking
- Pattern library browser
- Quality improvement graphs

**4. `/scripts/synthesize-variants-to-3.py`**
- Find duplicates
- Synthesize to best 3 variants
- Clean up GraphRAG

---

**Ready to build this infrastructure?**

This transforms enrichment from:
- ❌ Slow, manual, inconsistent
- ✅ Fast, intelligent, systematic

🌟 **The GraphRAG learns, agents get smarter, quality compounds!**

