# 🏗️ UNIFIED NAVIGATION ARCHITECTURE PLAN
## Integrating ALL Content into Units → Lessons → Resources Hierarchy

**Date:** October 18, 2025  
**Goal:** Transform scattered 1,500+ resources into organized, navigable learning pathways  
**Strategy:** GraphRAG-powered intelligent content organization

---

## 📊 CURRENT STATE ANALYSIS

### Content Inventory:
```
Total Resources: ~1,500+ files
├─ Units: ~95 files (mostly incomplete)
├─ Lessons: ~850+ standalone files  
├─ Handouts: ~900+ scattered files
├─ Games: 30+ files
├─ Assessments: ~20+ files
└─ Tools: ~10+ generators

Directories:
├─ /public/units/ (36 items, mixed quality)
├─ /public/lessons/ (144 files, mostly standalone)
├─ /public/handouts/ (333 files, unorganized)
├─ /public/generated-resources-alpha/ (47 AI resources)
├─ /y8-systems/ (44 files, GOLD STANDARD ⭐)
├─ /guided-inquiry-unit/ (34 files, complete)
├─ /critical-thinking/ (16 files, complete)
├─ /writers-toolkit/ (46 files, complete)
└─ Many scattered directories...
```

### Quality Tier Assessment:
- **GOLD STANDARD (5 units):** Y8 Systems, Walker Unit, Guided Inquiry, Writers Toolkit, Critical Thinking
- **GOOD (10-15 units):** Partial units with 3-5 lessons
- **FRAGMENTS (70+ units):** Single lesson or incomplete
- **ORPHANS (800+ files):** No unit association

---

## 🎯 TARGET UNIFIED STRUCTURE

### The Hierarchical Vision:

```
📦 SUBJECT AREA
└─ 📘 YEAR LEVEL
   └─ 📚 UNIT (6-8 weeks)
      ├─ 📖 Unit Overview Page
      │  ├─ Learning Objectives
      │  ├─ Cultural Context
      │  ├─ Assessment Framework
      │  └─ Scope & Sequence
      │
      ├─ 📁 LESSONS/ (8-12 lessons)
      │  ├─ 📖 Lesson 1
      │  │  ├─ Lesson Plan (75 min)
      │  │  ├─ 📄 Handout 1
      │  │  ├─ 📄 Handout 2
      │  │  ├─ 📄 Handout 3
      │  │  ├─ 🎮 Related Game
      │  │  ├─ 🎥 Related Video
      │  │  └─ 📊 Formative Assessment
      │  │
      │  ├─ 📖 Lesson 2
      │  │  ├─ Lesson Plan
      │  │  ├─ 📄 Handouts (3-5)
      │  │  ├─ 🎮 Interactive Activity
      │  │  └─ 📊 Assessment
      │  │
      │  └─ ... Lessons 3-12
      │
      ├─ 📁 RESOURCES/
      │  ├─ Supplementary Handouts
      │  ├─ Extension Activities
      │  ├─ Differentiation Materials
      │  └─ Teacher Notes
      │
      ├─ 📊 ASSESSMENTS/
      │  ├─ Formative Checks
      │  ├─ Summative Assessment
      │  ├─ Rubrics
      │  └─ Student Exemplars
      │
      └─ 🔗 PATHWAYS/
         ├─ Related Units (GraphRAG-powered)
         ├─ Prerequisites
         └─ Next Steps
```

---

## 🗺️ PROPOSED SUBJECT → YEAR → UNIT ORGANIZATION

### 1. **SOCIAL STUDIES** (Primary Subject Area)

#### **Year 7: Foundation Units**
```
📦 Y7-SS-01: Te Ao Māori Foundations
├─ 8 lessons
├─ 24 handouts
├─ 4 assessments
└─ Cultural identity, tikanga, basic te reo

📦 Y7-SS-02: Local Community Studies
├─ 6 lessons
├─ 18 handouts
└─ Iwi history, community geography
```

#### **Year 8: Systems & Power** ⭐ GOLD STANDARD
```
📦 Y8-SS-01: Power & Governance Systems
├─ Location: /y8-systems/
├─ Status: COMPLETE (10 lessons, 44 files)
├─ Lessons:
│  ├─ L1: What Makes a Society?
│  ├─ L2: Comparing Governance Systems
│  ├─ L3: Māori vs Pākehā Power
│  ├─ L4-10: Systems thinking, civic participation
├─ 22 resources (handouts, stations, assessments)
└─ Model for other units

📦 Y8-SS-02: Urbanization & Migration
├─ 8 lessons (from existing handouts)
├─ Urban identity, Māori migration, city systems
└─ Resources: unit-2-urban-*.html files

📦 Y8-SS-03: Critical Thinking Toolkit
├─ Location: /critical-thinking/
├─ Status: COMPLETE (10 lessons, 16 files)
├─ Media literacy, source evaluation
└─ Cross-curricular application
```

#### **Year 9-10: Advanced Social Sciences**
```
📦 Y9-SS-01: Guided Inquiry - Design Your Society
├─ Location: /guided-inquiry-unit/
├─ Status: COMPLETE (6 lessons, 34 files)
├─ Interdisciplinary project
└─ Economics, politics, culture design

📦 Y10-SS-01: Historical Analysis & Te Tiriti
├─ 8-10 lessons
├─ Walker Unit lessons (Te Puea Hērangi)
├─ Treaty settlements, colonial impacts
└─ 25+ handouts
```

---

### 2. **ENGLISH / LITERACY**

#### **Year 8: Writing Excellence**
```
📦 Y8-EN-01: Writer's Toolkit
├─ Location: /writers-toolkit/
├─ Status: COMPLETE (11 lessons, 46 files)
├─ Narrative, persuasive, descriptive writing
└─ Cultural story structures

📦 Y8-EN-02: Interactive Literacy Workbook
├─ Location: /interactive-literacy/
├─ Digital-first, Chromebook-optimized
├─ Reading comprehension, vocabulary
└─ Self-paced learning
```

#### **Year 9-13: Advanced Literacy**
```
📦 Y9-EN-01: Creative Writing & Whakataukī
├─ From generated-resources-alpha
├─ 5 lessons on narrative structures
├─ Poetry analysis through Māori traditions
└─ 10+ handouts

📦 Y11-13-EN-01: NCEA Level 1 Literacy
├─ Standards-aligned lessons
├─ Must-knows handout
├─ Practice assessments
└─ 15+ resources
```

---

### 3. **MATHEMATICS**

#### **Year 7-8: Foundation Maths**
```
📦 Y7-MA-01: Algebra Foundations
├─ Location: /units/y7-maths-algebra/
├─ 6 lessons
├─ Algebraic thinking in Māori games
└─ 12+ handouts

📦 Y8-MA-01: Statistics & Probability
├─ Location: /units/y8-statistics/
├─ 8 lessons
├─ Māori games probability
├─ Sports performance analysis
└─ Treaty data analysis
```

#### **Year 9-10: Applied Maths**
```
📦 Y9-MA-01: Geometry & Māori Patterns
├─ Location: /units/y9-mathematics-geometry-maori-patterns/
├─ Tukutuku patterns, kōwhaiwhai
├─ Symmetry, tessellations
└─ 8 lessons + 20 handouts

📦 Y10-MA-01: Mathematical Modeling
├─ Environmental modeling (calculus)
├─ Ecological systems
└─ From generated-resources-alpha
```

---

### 4. **SCIENCE & TECHNOLOGY**

#### **Year 7-8: Foundation Science**
```
📦 Y7-SC-01: Ecosystems & Kaitiakitanga
├─ Location: /units/y7-science-ecosystems/
├─ 6 lessons
├─ Traditional ecological knowledge
└─ 15 handouts

📦 Y8-DT-01: Digital Kaitiakitanga
├─ Location: /units/y8-digital-kaitiakitanga/
├─ Digital citizenship, AI ethics
├─ 8 lessons
└─ 18 resources
```

#### **Year 9-13: Advanced Science**
```
📦 Y9-SC-01: Physics & Traditional Instruments
├─ Sound waves, vibration
├─ Taonga pūoro physics
└─ 6 lessons from generated-resources

📦 Y10-SC-01: Genetics & Whakapapa
├─ DNA science + cultural identity
├─ 8 lessons
├─ Ethics through Māori lens
└─ 12 handouts

📦 Y11-13-SC-01: Renewable Energy & Innovation
├─ Traditional knowledge + modern tech
├─ Climate change through te taiao
└─ From generated-resources-alpha
```

---

### 5. **DIGITAL TECHNOLOGIES**

```
📦 Y7-DT-01: Digital Foundations
├─ Location: /units/y7-digital-technology/
├─ Chromebook skills
├─ Digital literacy basics
└─ 6 lessons

📦 Y8-DT-02: Coding with Cultural Patterns
├─ From generated-resources-alpha
├─ Tukutuku pattern coding
├─ 6 lessons
└─ Computational thinking

📦 Y9-13-DT-01: AI Ethics & Data Sovereignty
├─ Māori data sovereignty
├─ AI bias and ethics
├─ 8 lessons + game development
└─ 15+ resources
```

---

### 6. **CROSS-CURRICULAR / GAMES**

```
📦 GAMES-01: Language Learning Games
├─ Te Reo Wordle (5 & 6 letter)
├─ English Wordle
├─ Spelling Bee
├─ Countdown Letters
└─ 11 interactive games

📦 TOOLS-01: Teacher Resource Generators
├─ Crossword Generator
├─ Word Search Generator
├─ Quiz Makers
└─ 10+ tools
```

---

## 🤖 GRAPHRAG-POWERED ORGANIZATION

### How GraphRAG Will Help:

#### 1. **Automatic Content Clustering**
```sql
-- GraphRAG query to find related content
SELECT 
  resource_title,
  resource_type,
  subject_area,
  year_level,
  cultural_connection,
  similarity_score
FROM agent_knowledge
WHERE subject_area = 'Social Studies'
  AND year_level = 8
  AND category = 'lessons'
ORDER BY similarity_score DESC;
```

#### 2. **Relationship Mapping**
```javascript
// GraphRAG discovers:
- Which handouts belong to which lessons
- Which lessons form a logical sequence
- Which resources share cultural themes
- Which content fills curriculum gaps
```

#### 3. **Intelligent Suggestions**
```
GraphRAG can suggest:
✅ "Lesson X would fit well in Unit Y8-SS-01"
✅ "Handout Z supports Lesson 3 learning objectives"
✅ "This unit needs 2 more formative assessments"
✅ "Similar content exists in different format"
```

---

## 🔧 IMPLEMENTATION STRATEGY

### Phase 1: Audit & Categorize (Week 1)
```bash
# Use GraphRAG to analyze all content
1. Scan all 1,500+ files
2. Extract metadata:
   - Subject area
   - Year level
   - Content type
   - Cultural elements
   - Learning objectives
3. Store in GraphRAG database
4. Generate similarity scores
```

### Phase 2: Cluster into Units (Week 2-3)
```javascript
// Automated clustering algorithm:
1. Start with GOLD STANDARD units (already done)
2. Find "homeless" lessons
3. Match to existing units OR create new units
4. Group by:
   - Subject + Year + Theme
   - Cultural context
   - Learning progression
   - Curriculum standards
```

### Phase 3: Build Unit Pages (Week 4-5)
```
For each identified unit:
1. Create unit overview page
2. Link lessons in logical sequence
3. Attach handouts to relevant lessons
4. Add assessments
5. Insert cultural context
6. Create navigation breadcrumbs
```

### Phase 4: Update Navigation (Week 6)
```
Update navigation-standard.html:
- Subject dropdowns
  ├─ Year level sub-menus
  └─ Unit listings
- Dynamic loading of unit content
- Search by year/subject/theme
```

### Phase 5: Cross-Linking (Week 7-8)
```
GraphRAG-powered connections:
- "Students who studied this also studied..."
- "Related units across subjects"
- "Prerequisites" and "Next steps"
- "Cultural themes" linking
```

---

## 📁 FILE ORGANIZATION STRUCTURE

### Proposed Directory Structure:
```
/public/
├─ units/
│  ├─ social-studies/
│  │  ├─ year-7/
│  │  │  ├─ te-ao-maori-foundations/
│  │  │  │  ├─ index.html (unit overview)
│  │  │  │  ├─ lessons/
│  │  │  │  │  ├─ lesson-01-whakapapa.html
│  │  │  │  │  ├─ lesson-02-tikanga.html
│  │  │  │  │  └─ ...
│  │  │  │  ├─ handouts/
│  │  │  │  │  ├─ whakapapa-reflection.html
│  │  │  │  │  └─ ...
│  │  │  │  └─ assessments/
│  │  │  └─ ...
│  │  ├─ year-8/
│  │  │  ├─ power-governance/ → SYMLINK to /y8-systems/
│  │  │  ├─ urbanization/
│  │  │  └─ critical-thinking/ → SYMLINK
│  │  └─ ...
│  │
│  ├─ english/
│  │  ├─ year-8/
│  │  │  ├─ writers-toolkit/ → SYMLINK
│  │  │  └─ ...
│  │  └─ ...
│  │
│  ├─ mathematics/
│  ├─ science/
│  └─ technology/
│
├─ legacy/ (for backward compatibility)
│  ├─ lessons/ → redirects to new structure
│  ├─ handouts/ → redirects to new structure
│  └─ ...
│
└─ index.html (updated with new navigation)
```

---

## 🎯 GRAPHRAG DATABASE SCHEMA

### Enhanced Schema for Content Organization:
```sql
CREATE TABLE content_hierarchy (
  id SERIAL PRIMARY KEY,
  
  -- Identity
  file_path TEXT,
  content_type TEXT, -- unit, lesson, handout, assessment, game
  title TEXT,
  
  -- Hierarchy
  subject_area TEXT, -- Social Studies, English, Maths, Science
  year_level INTEGER, -- 7-13
  unit_id INTEGER REFERENCES units(id),
  lesson_id INTEGER REFERENCES lessons(id),
  
  -- Content
  learning_objectives TEXT[],
  cultural_elements TEXT[],
  curriculum_links TEXT[],
  
  -- Relationships (GraphRAG magic)
  related_content INTEGER[], -- IDs of related resources
  prerequisite_content INTEGER[],
  extension_content INTEGER[],
  
  -- Quality
  completion_status TEXT, -- complete, partial, fragment
  quality_tier TEXT, -- gold, good, needs-work
  
  -- Metadata
  created_date DATE,
  last_updated DATE,
  author TEXT
);

CREATE TABLE units (
  id SERIAL PRIMARY KEY,
  code TEXT, -- Y8-SS-01
  title TEXT,
  subject_area TEXT,
  year_level INTEGER,
  duration_weeks INTEGER,
  status TEXT,
  overview_page TEXT -- file path
);

CREATE TABLE lessons (
  id SERIAL PRIMARY KEY,
  unit_id INTEGER REFERENCES units(id),
  sequence_number INTEGER,
  title TEXT,
  duration_minutes INTEGER,
  file_path TEXT
);
```

---

## 🚀 IMMEDIATE NEXT STEPS

### 1. GraphRAG Content Scan (1-2 days)
```python
# Script: scan-all-content-graphrag.py
"""
Scan all HTML files
Extract metadata
Store in GraphRAG
Generate similarity matrix
Output clustering recommendations
"""
```

### 2. Create Unit Templates (1 day)
```html
<!-- Template: unit-overview-template.html -->
Standard structure for all unit overview pages
- Cultural context section
- Lesson sequence
- Resources list
- Assessment framework
```

### 3. Migration Scripts (2-3 days)
```bash
# Scripts to:
1. Move files to new structure
2. Update internal links
3. Create redirects
4. Generate breadcrumbs
5. Update navigation
```

### 4. Quality Tiers (1 week)
```
Focus migration by quality:
1. GOLD STANDARD: Already done ✅
2. GOOD units: Quick migration
3. FRAGMENTS: Consolidate or archive
4. ORPHANS: GraphRAG clustering
```

---

## 📊 SUCCESS METRICS

### Target Outcomes:
- ✅ **100% of content** organized into units
- ✅ **Zero orphaned** lessons/handouts
- ✅ **3-click max** to any resource from homepage
- ✅ **GraphRAG-powered** related content suggestions
- ✅ **Clear learning pathways** across year levels
- ✅ **Cultural integration** in every unit

### User Experience:
```
Teacher Journey:
Homepage → Subject → Year Level → Unit → Lesson → Handout
(5 clicks max, with breadcrumbs at every step)

Student Journey:
Dashboard → My Units → Current Lesson → Today's Handout
(3 clicks max)
```

---

## 🎓 CULTURAL INTEGRATION

Every unit must include:
- **Whakataukī** - Guiding proverb
- **Cultural Context** - Te Ao Māori lens
- **House Values** - Whaimana, Whaiora, Whaiara
- **Cultural Safety** - Consultation points
- **Local Iwi** - Connections where relevant

---

## 💡 EXAMPLE: BEFORE → AFTER

### BEFORE (Current Chaos):
```
/public/handouts/algebraic-thinking-in-traditional-māori-games.html
❌ Orphaned
❌ No unit association
❌ Hard to discover
❌ No learning progression
```

### AFTER (Unified System):
```
/public/units/mathematics/year-7/algebra-foundations/
├─ index.html (Unit Overview)
├─ lessons/
│  ├─ lesson-03-patterns-in-games.html
│  │   └─ Links to:
│  │       ├─ handout-algebraic-thinking-games.html ✅
│  │       ├─ activity-hei-tama-tu-tama.html
│  │       └─ assessment-pattern-recognition.html
│  └─ ...
└─ resources/

Teacher finds it:
Homepage → Maths → Year 7 → Algebra Unit → Lesson 3 → Handout ✅
```

---

## 🎯 CONCLUSION

This unified navigation architecture will transform Te Kete Ako from a scattered collection of excellent resources into a **world-class, organized learning platform** where:

1. **Every resource has a home** (unit → lesson → resource)
2. **Clear learning pathways** guide teachers and students
3. **GraphRAG intelligence** suggests related content
4. **Cultural integration** is consistent and authentic
5. **Navigation is intuitive** (subject → year → unit → lesson)

**Timeline:** 8 weeks with GraphRAG automation  
**Effort:** Medium (GraphRAG does heavy lifting)  
**Impact:** **TRANSFORMATIONAL** 🚀

---

*Next Step: Run GraphRAG content scan to begin automated clustering*

