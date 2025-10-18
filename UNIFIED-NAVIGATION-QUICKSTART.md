# 🚀 UNIFIED NAVIGATION - QUICKSTART GUIDE
## How to Organize 1,400+ Resources into Clean Hierarchy

**Date:** October 18, 2025  
**Current State:** 681 lessons, 485 handouts, 17 units (mostly scattered)  
**Goal:** Everything organized into Subject → Year → Unit → Lesson → Resources

---

## 📊 THE CHALLENGE

```
Current Mess:
├─ 681 lessons (mostly standalone, unorganized)
├─ 485 handouts (scattered across directories)
├─ 17 unit overviews (varying quality)
├─ 20 assessments (not linked to units)
├─ 16 games (some orphaned)
└─ 10 tools (working but not integrated)

Total: ~1,400 files to organize
```

---

## ✨ THE SOLUTION: 3-PHASE APPROACH

### **Phase 1: Keep What Works** ✅ (Already Done!)
```
GOLD STANDARD Units (Don't Touch - They're Perfect):
✅ Y8 Systems (/y8-systems/) - 10 lessons, 44 files
✅ Walker Unit (/units/walker-unit/) - 5 lessons
✅ Guided Inquiry (/guided-inquiry-unit/) - 6 lessons, 34 files
✅ Writers Toolkit (/writers-toolkit/) - 11 lessons, 46 files
✅ Critical Thinking (/critical-thinking/) - 10 lessons, 16 files
✅ Generated Resources Alpha - 47 AI resources (just integrated!)

Status: 6 complete units, ~200 files ✅
```

### **Phase 2: Quick Wins - Organize Obvious Clusters** (Next 2 weeks)
```
Easy to Organize (10-15 new units):

📦 Y7 Maths Algebra
├─ Location: /units/y7-maths-algebra/
├─ Files: 6 lesson files already in directory
└─ Action: Create index.html, link handouts

📦 Y8 Statistics
├─ Location: /units/y8-statistics/
├─ Files: 8 lesson files already grouped
└─ Action: Create unit overview

📦 Y9 Geometry & Māori Patterns
├─ Location: /units/y9-mathematics-geometry-maori-patterns/
├─ Files: Lessons exist
└─ Action: Link handouts from /handouts/

📦 Y7 Science Ecosystems
📦 Y8 Digital Kaitiakitanga
📦 Y10 Physics Forces
... and 8-10 more partially complete units
```

### **Phase 3: GraphRAG Magic - Cluster the Rest** (Weeks 3-8)
```
Hard Part (500+ standalone lessons):

Use GraphRAG to:
1. Analyze content similarity
2. Detect natural clusters
3. Suggest unit groupings
4. Map lesson → handout relationships

Example:
"These 8 lessons all deal with urbanization 
and Māori identity - create Y8-SS-02: 
Urbanization & Migration unit"
```

---

## 🎯 IMMEDIATE ACTION PLAN

### Week 1: Foundation Setup
```bash
# 1. Create directory structure
mkdir -p public/units/{social-studies,english,mathematics,science,technology}
mkdir -p public/units/social-studies/year-{7,8,9,10}
mkdir -p public/units/english/year-{7,8,9,10,11,12,13}
# etc...

# 2. Create unit template
cp templates/unit-overview-template.html public/units/template.html

# 3. Set up GraphRAG schema
sqlite3 knowledge_preservation.db < init-graphrag-tables.sql
```

### Week 2: Quick Wins
```javascript
// For each partially complete unit:
1. Create unit overview page (copy template)
2. Fill in unit details:
   - Learning objectives
   - Scope & sequence
   - Cultural context
3. Link existing lessons
4. Find matching handouts
5. Add to navigation

Target: 10 new complete units by end of week
```

### Weeks 3-8: GraphRAG Clustering
```python
# Run GraphRAG analyzer
python3 graphrag-content-organizer.py

# Review suggestions
cat graphrag-organization-report.json

# Create units based on clusters
for cluster in suggestions:
    create_unit(cluster)
    migrate_lessons(cluster)
    link_handouts(cluster)
    update_navigation(cluster)
```

---

## 📋 UNIT OVERVIEW TEMPLATE

Every unit needs an overview page following this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Unit Title | Te Kete Ako</title>
    <meta name="description" content="Unit description">
    <!-- Standard CSS -->
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">
    <link rel="stylesheet" href="/css/component-library.css">
</head>
<body>
    <!-- Standard Navigation -->
    <div id="beautiful-nav-container"></div>
    <script src="/js/load-navigation.js"></script>
    
    <main class="container">
        <!-- Breadcrumbs -->
        <nav class="breadcrumb-nav">
            <a href="/">Home</a> → 
            <a href="/units/">Units</a> → 
            <a href="/units/mathematics/">Mathematics</a> → 
            <a href="/units/mathematics/year-7/">Year 7</a> → 
            <span>Algebra Foundations</span>
        </nav>
        
        <!-- Unit Header -->
        <header>
            <span class="badge">Year 7 | Mathematics</span>
            <h1>Algebra Foundations</h1>
            <p class="lead">6-8 weeks | 12 lessons</p>
        </header>
        
        <!-- Cultural Context (REQUIRED) -->
        <section class="cultural-integration">
            <h2>🌿 Cultural Context | Horopaki Ahurea</h2>
            <div class="whakatauaki-section">
                <p class="whakatauaki">"Ko te ahurei o te tamaiti, ko te ahurei o te ako"</p>
                <p class="translation">"The uniqueness of the child is the uniqueness of learning"</p>
            </div>
            <div class="house-values">
                <h3>Connection to Mangakōtukutuku College Values</h3>
                <p>This unit connects to <strong>Whaimana</strong> (Integrity)...</p>
            </div>
        </section>
        
        <!-- Learning Objectives -->
        <section class="learning-objectives">
            <h2>🎯 Learning Objectives</h2>
            <ul>
                <li>Understand algebraic notation and expressions</li>
                <li>Explore patterns in traditional Māori games</li>
                <li>Apply algebraic thinking to real-world problems</li>
            </ul>
        </section>
        
        <!-- Lesson Sequence -->
        <section class="lesson-sequence">
            <h2>📚 Lessons</h2>
            <div class="lesson-grid">
                <div class="lesson-card">
                    <h3>Lesson 1: Introduction to Patterns</h3>
                    <p>Explore mathematical patterns in Māori games</p>
                    <a href="lessons/lesson-01.html" class="btn">View Lesson →</a>
                    <div class="resources">
                        <a href="handouts/pattern-worksheet.html">📄 Pattern Worksheet</a>
                        <a href="handouts/game-instructions.html">📄 Game Instructions</a>
                    </div>
                </div>
                <!-- More lesson cards... -->
            </div>
        </section>
        
        <!-- Assessment Framework -->
        <section class="assessment">
            <h2>📊 Assessment</h2>
            <ul>
                <li>Formative: Pattern recognition quizzes (Lessons 1-4)</li>
                <li>Formative: Problem-solving tasks (Lessons 5-8)</li>
                <li>Summative: Algebraic thinking project (Lesson 12)</li>
            </ul>
            <a href="assessments/unit-rubric.html" class="btn">View Rubric →</a>
        </section>
        
        <!-- Resources -->
        <section class="resources">
            <h2>📦 Additional Resources</h2>
            <ul>
                <li><a href="resources/teacher-notes.pdf">Teacher Notes</a></li>
                <li><a href="resources/differentiation-guide.pdf">Differentiation Guide</a></li>
                <li><a href="/games/hei-tama-tu-tama.html">🎮 Hei Tama Tu Tama Game</a></li>
            </ul>
        </section>
        
        <!-- Related Units (GraphRAG-powered) -->
        <section class="related-units">
            <h2>🔗 Related Learning Pathways</h2>
            <div class="pathway-grid">
                <div class="pathway-card">
                    <span class="badge">Prerequisites</span>
                    <h3>Y7 Basic Number Skills</h3>
                    <a href="/units/mathematics/year-7/number-basics/">View Unit →</a>
                </div>
                <div class="pathway-card">
                    <span class="badge">Next Steps</span>
                    <h3>Y8 Advanced Algebra</h3>
                    <a href="/units/mathematics/year-8/advanced-algebra/">View Unit →</a>
                </div>
                <div class="pathway-card">
                    <span class="badge">Cross-Curricular</span>
                    <h3>Y7 Māori Games (PE)</h3>
                    <a href="/units/health-pe/year-7/traditional-games/">View Unit →</a>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
```

---

## 🗺️ NAVIGATION STRUCTURE

Update `navigation-standard.html`:

```html
<!-- UNITS DROPDOWN -->
<div class="nav-item">
  <a href="/units/" class="nav-link">Units</a>
  <div class="dropdown dropdown-mega">
    <div class="dropdown-content">
      
      <!-- BY SUBJECT -->
      <div class="dropdown-section">
        <h4>Social Studies</h4>
        <a href="/units/social-studies/year-7/">Year 7</a>
        <a href="/units/social-studies/year-8/">Year 8 ⭐</a>
        <a href="/units/social-studies/year-9/">Year 9</a>
        <a href="/units/social-studies/year-10/">Year 10</a>
      </div>
      
      <div class="dropdown-section">
        <h4>English & Literacy</h4>
        <a href="/units/english/year-7/">Year 7</a>
        <a href="/units/english/year-8/">Year 8 ⭐</a>
        <a href="/units/english/year-9-13/">Year 9-13</a>
      </div>
      
      <div class="dropdown-section">
        <h4>Mathematics</h4>
        <a href="/units/mathematics/year-7/">Year 7</a>
        <a href="/units/mathematics/year-8/">Year 8</a>
        <a href="/units/mathematics/year-9/">Year 9</a>
        <a href="/units/mathematics/year-10-13/">Year 10-13</a>
      </div>
      
      <!-- More subjects... -->
    </div>
  </div>
</div>
```

---

## 🎯 SUCCESS CRITERIA

### By End of Week 2:
- ✅ 15 complete units (6 existing + 9 new)
- ✅ ~400 resources organized (~30%)
- ✅ All GOLD STANDARD units in new navigation

### By End of Week 4:
- ✅ 30 complete units
- ✅ ~800 resources organized (~60%)
- ✅ GraphRAG clustering active

### By End of Week 8:
- ✅ 50+ complete units
- ✅ 100% of resources organized
- ✅ Zero orphaned content
- ✅ GraphRAG-powered related content
- ✅ Complete navigation hierarchy

---

## 🤖 GRAPHRAG IMPLEMENTATION

### 1. Enhanced Schema (Already exists - just needs population)
```sql
-- Add to init-graphrag-tables.sql
CREATE TABLE content_units (
  id SERIAL PRIMARY KEY,
  unit_code TEXT UNIQUE, -- Y8-SS-01
  title TEXT,
  subject TEXT,
  year_level INTEGER,
  status TEXT, -- complete, partial, planned
  overview_path TEXT
);

CREATE TABLE unit_lessons (
  id SERIAL PRIMARY KEY,
  unit_id INTEGER REFERENCES content_units(id),
  lesson_number INTEGER,
  lesson_path TEXT,
  lesson_title TEXT
);

CREATE TABLE lesson_resources (
  id SERIAL PRIMARY KEY,
  lesson_id INTEGER REFERENCES unit_lessons(id),
  resource_type TEXT, -- handout, assessment, game, video
  resource_path TEXT,
  resource_title TEXT
);
```

### 2. Auto-Population Script
```python
# populate-graphrag.py
"""
Scan existing units and populate GraphRAG database
Then use AI to suggest clustering for remaining content
"""
```

---

## 💡 TIPS & BEST PRACTICES

### 1. **Start with GOLD STANDARD**
Don't touch working units - they're the template for others

### 2. **Use Consistent Naming**
```
Unit Code Format: Y{year}-{subject-abbrev}-{number}
Examples:
- Y8-SS-01 (Year 8 Social Studies Unit 1)
- Y7-MA-02 (Year 7 Mathematics Unit 2)
- Y9-EN-01 (Year 9 English Unit 1)
```

### 3. **Cultural Context is REQUIRED**
Every unit must have:
- Whakataukī section
- Cultural context paragraph
- House values connection
- Cultural safety notes

### 4. **Breadcrumbs Everywhere**
```
Home → Units → Subject → Year → Unit → Lesson → Resource
```

### 5. **GraphRAG for Relationships**
Let AI discover:
- Which handouts support which lessons
- Which lessons form natural sequences
- Which units share cultural themes
- What prerequisites/extensions exist

---

## 🚀 READY TO START?

### Immediate Commands:
```bash
# 1. Create comprehensive unit architecture plan
cat UNIFIED-NAVIGATION-ARCHITECTURE-PLAN.md

# 2. Run content analyzer (when GraphRAG ready)
python3 graphrag-content-organizer.py

# 3. Start with quick wins
# Pick one partially complete unit
# Create overview page
# Link lessons and handouts
# Add to navigation
# Repeat!
```

---

## 📞 NEED HELP?

**Agent Collaboration:**
- This is a multi-week project
- Each agent can tackle 2-3 units
- Use git commits to track progress
- GraphRAG will prevent duplicate work

**Coordination:**
- Update ACTIVE_QUESTIONS.md with blockers
- Commit unit pages as you complete them
- Use consistent structure (template above)

---

**Timeline:** 8 weeks  
**Effort:** Medium (with GraphRAG automation)  
**Impact:** TRANSFORMATIONAL  
**Status:** Ready to begin! 🎉


