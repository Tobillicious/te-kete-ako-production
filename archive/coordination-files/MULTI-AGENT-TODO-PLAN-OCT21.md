# 🎯 MULTI-AGENT TODO PLAN - October 21, 2025
## Strategic Execution Plan from Deep GraphRAG Analysis

**Created By:** Kaitiaki Aronui V3.0  
**Source:** Comprehensive GraphRAG & Codebase Analysis  
**Timeline:** Next 7-30 days  
**Status:** Ready for multi-agent execution

---

## 📊 **ANALYSIS SUMMARY**

From deep GraphRAG analysis of 17,196 resources, 240,276 relationships, and 832 MD files:

### **Key Discoveries:**
1. **Prerequisite Desert** - Y7 has ZERO prerequisites! Y9/Y10 < 0.5 density
2. **Cultural Excellence Gap** - 1,231 Q90+ Math/Science resources need cultural enrichment
3. **5 Missing House Leader Units** - Original vision 1/6 complete (Walker done)
4. **Cross-Subject Isolation** - Most subject pairs have <10 bridges
5. **Whakataukī Opportunity** - Can grow from 24.7% → 60% (5,000 resources)

### **Platform Strengths:**
- ✅ 56.8% Q90+ excellence (9,773 resources)
- ✅ 36.7% cultural integration (6,304 resources)
- ✅ 679 relationship types (semantic richness)
- ✅ 25 serverless functions (backend power)
- ✅ Y8 Digital Kaitiakitanga = gold standard (385 pathways!)

---

## 🚀 **TIER 1: CRITICAL (Next 7 Days)**

### **1. Build Year 7 Prerequisite Chains** 🔥
**Current:** 0 prerequisite links  
**Target:** ~25-30 prerequisite links  
**Impact:** Enable Y7 learning progressions

**Actions:**
```sql
-- Connect Y7 Algebra lessons sequentially
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
SELECT 
  '/public/units/y7-maths-algebra/lessons/lesson-' || n || '.html',
  '/public/units/y7-maths-algebra/lessons/lesson-' || (n+1) || '.html',
  'prerequisite_for',
  0.95,
  jsonb_build_object('reason', 'sequential algebra skill building')
FROM generate_series(1, 4) n;

-- Connect Y7 Science Ecosystems lessons
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
SELECT 
  '/public/units/y7-science-ecosystems/lessons/lesson-' || n || '.html',
  '/public/units/y7-science-ecosystems/lessons/lesson-' || (n+1) || '.html',
  'prerequisite_for',
  0.95,
  jsonb_build_object('reason', 'sequential ecosystem understanding')
FROM generate_series(1, 5) n;
```

**Assigned To:** Any agent with GraphRAG write access  
**Estimated Time:** 1 hour  
**Verification:** Query Y7 prerequisite density (should be ~0.5)

---

### **2. Enrich Top 20 Science Q90+ with Whakataukī** 🌿
**Current:** Science whakataukī: 18/83 (21.7%)  
**Target:** 38/83 (45.8%)  
**Impact:** Cultural parity with English/Math

**Priority Targets:**
1. Genetics & Whakapapa (Q95) - Need whakataukī about inheritance/connections
2. Y10 Navigation Teacher Guide (Q94) - Need celestial/wayfinding whakataukī
3. Y9 Ecology Teacher Guide (Q92) - Need kaitiakitanga whakataukī
4. Y7 Ecosystems Lessons (Q90) - Need te taiao whakataukī
5. (Continue for top 20...)

**Method:**
- Read each file
- Add whakataukī banner (follow AI Ethics lesson template)
- Choose culturally appropriate proverb for topic
- Update GraphRAG: `has_whakataukī = true`

**Assigned To:** Cultural content specialist agent  
**Estimated Time:** 3-4 hours  
**Verification:** Query Science whakataukī percentage

---

### **3. Create Science ↔ Math Cross-Subject Bridges** 🔗
**Current:** 0-5 links between Science and Math  
**Target:** +30 new relationships  
**Impact:** Enable STEM integration

**Example Bridges:**
```sql
-- Connect data analysis resources
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
VALUES 
  ('/public/units/y9-science-ecology/resources/conservation-data.html',
   '/public/units/y8-statistics/lessons/lesson-3-graphing.html',
   'applies_math_to',
   0.88,
   '{"reason": "ecological data visualization uses statistics"}'::jsonb),
   
  ('/public/handouts/mathematical-modeling-ecosystems.html',
   '/public/units/y9-science-ecology/unit-overview.html',
   'provides_math_for',
   0.90,
   '{"reason": "mathematical models explain population dynamics"}'::jsonb);
```

**Pattern:** Find Science resources using data/measurement → Link to Math statistics/graphing

**Assigned To:** Cross-curricular integration agent  
**Estimated Time:** 2 hours  
**Verification:** Query cross-subject bridge count

---

## 🏆 **TIER 2: HIGH PRIORITY (Next 14 Days)**

### **4. Build Te Puea Hērangi Unit** 👑
**Current:** 0/6 house leader units complete  
**Target:** 2/6 complete (Walker + Hērangi)  
**Impact:** Complete original curriculum vision

**Structure (Following Walker Template):**
- Lesson 1: Who Was Te Puea Hērangi?
- Lesson 2: The Legacy of Raupatu (Waikato War)
- Lesson 3: A Stand for Peace (Anti-conscription)
- Lesson 4: Tūrangawaewae - A Place to Stand
- Lesson 5: The Politics of Mana

**Requirements:**
- Quality 90+ (match Walker standard)
- 100% cultural integration
- 5+ connections each lesson
- Teacher guide (Q95+)
- Assessment materials
- Whakataukī for each lesson

**Assigned To:** Curriculum development specialist  
**Estimated Time:** 6-8 hours  
**Verification:** Check GraphRAG for "Hērangi" resources

---

### **5. Build Y9 & Y10 Prerequisite Chains** 📚
**Current:** Y9: 0.41 density, Y10: 1.00 density  
**Target:** Both ~1.0-1.5 density  
**Impact:** Complete Y7-10 learning progressions

**Focus Units:**
- Y9 Science Ecology (6 lessons) - Sequential chains
- Y9 Maths Geometry (8 lessons) - Tukutuku pattern progression
- Y10 Physics Navigation (5+ lessons) - Complexity building
- Y10 Physics Forces (lessons) - Conceptual scaffolding

**Method:** Same as Y7 - sequential lesson linking with 0.95 confidence

**Assigned To:** Any agent, can be parallelized  
**Estimated Time:** 2-3 hours  
**Verification:** Query Y9/Y10 prerequisite density

---

### **6. Enrich Top 50 Math Q90+ with Cultural Context** 🔢
**Current:** Math excellence 42.6% cultural  
**Target:** 60% cultural  
**Impact:** +100 culturally-enriched math resources

**Priority Targets:**
- Algebra units (pure math → cultural connections)
- Statistics units (real-world Māori data)
- Geometry units (whakairo, tukutuku patterns)

**Cultural Elements to Add:**
- Whakataukī (mathematical thinking)
- Māori measurement systems (ancient mathematics)
- Traditional games with mathematical principles
- Cultural data applications (treaty settlements, demographics)

**Assigned To:** Math + Cultural specialist agent  
**Estimated Time:** 6-8 hours  
**Verification:** Query Math cultural percentage

---

## 💎 **TIER 3: STRATEGIC (Next 30 Days)**

### **7. Build Remaining 4 House Leader Units** 🏛️
**Units to Build:**
- Ngata Unit - "The Politics of Culture" (5 lessons)
- Hopa Unit - "The Scholar and the People" (5 lessons)
- Rickard Unit - "The Price of Protest" (5 lessons)
- Māhuta Unit - "The Future of Rangatiratanga" (5 lessons)

**Total:** ~25 new lessons, Q90+, 100% cultural

**Assigned To:** Curriculum team (can parallelize)  
**Estimated Time:** 20-30 hours total  
**Verification:** All 6 house leader units complete

---

### **8. Whakataukī Saturation Campaign** 🌿
**Current:** 4,250 (24.7%)  
**Target:** 10,300 (60%)  
**Impact:** +6,050 resources with whakataukī

**Phase 1 (Priority):**
- All Q90+ resources (9,773 candidates)
- All Q90+ Science (639 resources)
- All Q90+ Math (592 resources)
- All Q90+ Digital Tech (910 resources)

**Phase 2 (Expansion):**
- Q80-89 resources with cultural context
- Hub pages and discovery tools
- Components and templates

**Method:**
- Batch processing by subject
- Subject-appropriate whakataukī selection
- Culturally vetted proverbs
- Update GraphRAG metadata

**Assigned To:** Cultural enrichment team  
**Estimated Time:** 30-40 hours  
**Verification:** Platform whakataukī percentage

---

### **9. Build Year 8, 9, 10 Hub Pages** 🎓
**Current:** Only Y7 hub exists  
**Target:** All 4 year-level hubs (Y7-10)  
**Impact:** Complete year-based navigation

**Template:** Use Y7 hub as base

**Features Each Hub:**
- GraphRAG-powered resource counts
- Subject navigation grid
- Featured units for that year
- Whakataukī appropriate for age
- "All Year X Resources" links

**Assigned To:** Frontend/navigation specialist  
**Estimated Time:** 3-4 hours  
**Verification:** All 4 hubs accessible + linked in nav

---

### **10. Cross-Subject Bridge Building** 🌉
**Target:** +500 cross-subject relationships

**Priority Bridges:**
- Science ↔ Math: +100 (data, modeling, measurement)
- English ↔ Social Studies: +100 (historical analysis, narratives)
- Health & PE ↔ Science: +50 (biology, physiology)
- Te Ao Māori ↔ ALL: +200 (cultural threading)
- Digital Tech ↔ Science: +50 (modeling, simulations)

**Method:**
- Identify thematic overlaps
- Build relationships with context
- Set appropriate confidence (0.80-0.90)
- Document reasoning in metadata

**Assigned To:** Multiple agents (parallelizable)  
**Estimated Time:** 15-20 hours  
**Verification:** Query cross-subject link counts

---

## 🧠 **BACKEND SYSTEM OVERVIEW (25 Netlify Functions)**

### **Discovered Serverless Functions:**

**Authentication (5 functions):**
1. `auth-register.js` - User registration
2. `auth-login.js` - Login flow
3. `auth-forgot-password.js` - Password recovery
4. `auth-update-password.js` - Password changes
5. `admin-password-reset.js` - Admin controls

**AI & Intelligence (5 functions):**
6. `ai-learning-orchestrator.js` - Multi-AI coordination
7. `ai-companion.js` - Student AI assistant
8. `deepseek-agent.js` - DeepSeek integration
9. `deepseek-graphrag-bridge.js` - DeepSeek + GraphRAG
10. `deepseek-agent-simple.js` - Lightweight variant

**GraphRAG & Search (4 functions):**
11. `fetch-graphrag.js` - GraphRAG queries
12. `find-similar-resources.js` - Semantic search
13. `neo4j-bridge.js` - Graph database integration
14. `exa-search.js` - External research API

**Content & Learning (5 functions):**
15. `adaptive-learning-paths.js` - Personalized pathways
16. `get-resources.js` - Resource retrieval
17. `youtube-library-api.js` - Video content
18. `get-student-projects.js` - Project management
19. `project-submit.js` - Project submissions

**Platform Management (6 functions):**
20. `progress-tracker.js` - Learning analytics
21. `professional-compliance-reporter.js` - Quality monitoring
22. `kaitiaki-reality-check.js` - System validation
23. `apply-schema-migration.js` - Database updates
24. `manual-schema-fix.js` - Database repairs
25. `db-test.js` - Connection testing

**Key Insight:** We have a COMPLETE backend API layer with AI orchestration, GraphRAG integration, and adaptive learning!

---

## 🎯 **EXECUTION PROTOCOL**

### **How to Use This Plan:**

1. **Choose Your Mission:**
   - Pick 1-2 TODOs that match your specialization
   - Mark them as `in_progress` in agent_knowledge
   - Execute systematically

2. **Use GraphRAG:**
   - Query BEFORE building (check if it exists)
   - Build (create actual code/content)
   - Teach (update agent_knowledge with learnings)

3. **Coordinate via ACTIVE_QUESTIONS.md:**
   - Ask questions before duplicating work
   - Share discoveries
   - Update progress

4. **Quality Standards:**
   - All new resources: Q90+ minimum
   - All new lessons: Whakataukī required
   - All relationships: 0.85+ confidence
   - All code: Follow existing patterns

5. **Verification:**
   - Every TODO has a verification query
   - Check GraphRAG stats after completion
   - Document results in agent_knowledge

---

## 📈 **SUCCESS METRICS**

### **Week 1 Targets:**
- [ ] Y7 prerequisite density: 0.00 → 0.50
- [ ] Science whakataukī: 21.7% → 40%
- [ ] Science ↔ Math bridges: 0 → 30
- [ ] Hērangi unit lessons: 0 → 5

### **Month 1 Targets:**
- [ ] Y9/Y10 prerequisite density: 0.41 → 1.0
- [ ] Math cultural excellence: 42.6% → 60%
- [ ] Cross-subject bridges: +200 total
- [ ] House leader units: 1/6 → 3/6
- [ ] Whakataukī saturation: 24.7% → 35%

### **Quarter 1 Targets (3 months):**
- [ ] All year levels: 1.0+ prerequisite density
- [ ] All subjects: 80%+ cultural integration
- [ ] All 6 house leader units complete
- [ ] Whakataukī: 60% platform-wide
- [ ] Pilot program: 10 schools engaged

---

## 🤝 **AGENT COORDINATION**

### **Recommended Agent Assignments:**

**Cultural Guardian Agent:**
- TODOs #2, #6, #8 (Whakataukī enrichment)
- Verify cultural authenticity
- Ensure appropriate proverb selection

**Curriculum Developer Agent:**
- TODOs #4, #7 (House leader units)
- Follow Walker unit template
- Maintain Q90+ quality

**GraphRAG Specialist Agent:**
- TODOs #1, #5, #10 (Prerequisite chains, bridges)
- Build relationship SQL
- Monitor confidence scores

**Frontend/UX Agent:**
- TODO #9 (Year-level hubs)
- Test mobile responsiveness
- Verify component loading

**Cross-Curricular Agent:**
- TODO #3, #10 (Cross-subject bridges)
- Identify thematic connections
- Build interdisciplinary links

---

## 🎊 **CELEBRATION MILESTONES**

### **When We Hit These, CELEBRATE! 🎉**

**Milestone 1:** Y7 Gets First Prerequisite Chain
- Significance: Youngest learners can now follow progressions!

**Milestone 2:** Science Reaches 50% Whakataukī
- Significance: Cultural parity with top subjects!

**Milestone 3:** 2nd House Leader Unit Complete
- Significance: 1/3 of original curriculum vision done!

**Milestone 4:** 1,000th Cross-Subject Bridge
- Significance: True interdisciplinary platform!

**Milestone 5:** All Year Levels Have 1.0+ Density
- Significance: Complete Y7-10 learning pathway system!

**Milestone 6:** 10,000th Resource Gets Whakataukī
- Significance: Majority of platform culturally enriched!

---

## 📊 **TRACKING & REPORTING**

### **How to Update Progress:**

**For Each Completed TODO:**
```sql
INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
VALUES (
  'todo_completion',
  'TODO #X: [Name]',
  'execution_summary',
  ARRAY[
    'Completed [action]',
    'Created [X] new relationships',
    'Updated [Y] resources',
    'Result: [metric improved]'
  ],
  jsonb_build_object(
    'todo_id', 'X',
    'start_date', 'YYYY-MM-DD',
    'completion_date', 'YYYY-MM-DD',
    'resources_affected', X,
    'relationships_created', Y
  ),
  ARRAY['your_agent_id']
);
```

**Weekly Check-In:**
- Query agent_knowledge for last 7 days
- Calculate metric improvements
- Update ACTIVE_QUESTIONS.md with progress
- Celebrate wins!

---

## 🌟 **VISION ALIGNMENT**

This plan directly executes on:

✅ **Original Vision (July 2025):** "World's first AI-powered, culturally responsive learning ecosystem"  
✅ **October 18 Super Plan:** "Deploy full tech stack" (backend exists, now enrich content)  
✅ **House Leader Curriculum:** Complete the 6-unit vision (1/6 → 6/6)  
✅ **18-Month Roadmap Phase 1:** Build to 2,000 resources with gold standard (we're at 17,196!)

**We're not just maintaining - we're EVOLVING toward the original grand vision!**

---

**Plan Created:** October 21, 2025  
**Based On:** Comprehensive GraphRAG analysis  
**Timeline:** Next 7-30 days  
**Expected Impact:** +1,500 relationships, +100 cultural resources, +35 new lessons

**Kia mau ki te tokanga nui a noho!**  
*Hold fast to your noble aspirations!*

