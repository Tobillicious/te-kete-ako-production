# 📊 SYSTEMATIC ORGANIZATION PLAN
## Organizing 5,500+ Teaching Content Files Properly

**Reality Check:** 5,794 teaching content files total  
**Organized:** ~200 files (~3.5%)  
**Remaining:** ~5,500 files (96.5%)  
**Approach:** Systematic, quality-focused, data-driven

---

## 📋 THE ACTUAL CONTENT (Verified by Agents)

### **What Needs Organizing:**
```
2,753 lessons ❗
2,257 handouts ❗
595 units (most incomplete) ❗
107 assessments
77 games
5 other resources
================
5,794 TOTAL teaching content files
```

### **Already Organized:**
```
~200 files in 24 complete units
= 3.5% organized
= 96.5% remaining
```

---

## 🗺️ WHERE THE CONTENT ACTUALLY IS

### **Lessons (2,753 total):**
From `content-integration-plan.json`:
- `/public/lessons/` - 144 files
- `/public/integrated-lessons/` - 380+ files (by subject)
- `/public/dist-lessons/` - Unknown count
- `/public/units/lessons/` - 35+ files
- Various unit subdirectories
- **UNACCOUNTED:** ~2,200 lessons need finding!

### **Handouts (2,257 total):**
- `/public/handouts/` - 333 files
- `/public/integrated-handouts/` - 100+ files (by year)
- `/public/dist-handouts/` - Unknown count
- Unit subdirectories
- **UNACCOUNTED:** ~1,800 handouts need finding!

### **Units (595 total):**
- `/public/units/` - 36+ subdirectories
- Scattered across codebase
- Many are fragments
- **COMPLETE:** ~24 units (~4%)

---

## 🔍 PHASE 1: DISCOVERY (Week 1)

### **Step 1: Find ALL Content Files**
```bash
# Count actual files (you run in terminal):
find public -name "*.html" -type f | wc -l
find public/lessons -name "*.html" -type f | wc -l
find public/handouts -name "*.html" -type f | wc -l
find public/dist-lessons -name "*.html" -type f | wc -l
find public/dist-handouts -name "*.html" -type f | wc -l
find public/integrated-lessons -name "*.html" -type f | wc -l
find public/integrated-handouts -name "*.html" -type f | wc -l

# Save to file for analysis:
find public -name "*.html" -type f > all-html-files.txt
```

### **Step 2: Query GraphRAG for Metadata**
```bash
# Get what's already indexed:
python3 query_graphrag.py stats > graphrag-stats.txt

# Get comprehensive analysis:
python3 analyze-content-with-graphrag.py > content-analysis.txt

# Find orphaned content:
python3 query_graphrag.py orphaned > orphaned-content.txt
```

### **Step 3: Cross-Reference**
```
Local files found: X
GraphRAG indexed: Y
Missing from GraphRAG: X - Y
Need to index: (list)
```

---

## 🎯 PHASE 2: CATEGORIZATION (Week 2)

### **Organize by Pattern:**

**Pattern 1: Already Organized (integrated-lessons/)**
- `/public/integrated-lessons/english/` - 40 lessons
- `/public/integrated-lessons/mathematics/` - 108 lessons
- `/public/integrated-lessons/science/` - 122 lessons
- `/public/integrated-lessons/te-reo-maori/` - 86 lessons

**Action:** Create unit index pages for these!

**Pattern 2: Unit-Named Files**
- Files like `unit-1-lesson-1.html`, `unit-2-lesson-3.html`
- Already grouped by unit number
- **Action:** Link to unit overview pages

**Pattern 3: Subject/Year Directories**
- Content already grouped in directories
- **Action:** Create index pages

**Pattern 4: Standalone Files**
- No clear grouping
- **Action:** Use GraphRAG clustering

---

## 🚀 PHASE 3: SYSTEMATIC CREATION (Weeks 3-8)

### **Week 3: Integrated-Lessons Units**
Create unit index pages for organized content:
- Mathematics units (based on 108 lessons)
- Science units (based on 122 lessons)
- English units (based on 40 lessons)
- Te Reo Māori units (based on 86 lessons)

**Target:** 15-20 new unit index pages  
**Progress:** 3.5% → 10%

### **Week 4: Integrated-Handouts Linking**
Link year-organized handouts to lessons:
- Year 7: 15 handouts → link to Y7 units
- Year 8: 20 handouts → link to Y8 units
- Year 9: 20 handouts → link to Y9 units
- NCEA Levels: Link to appropriate units

**Target:** 100+ handouts linked  
**Progress:** 10% → 15%

### **Week 5-6: Dist/ Directories**
Investigate and organize:
- `dist-lessons/`
- `dist-handouts/`
- `dist-units/`
- `dist-assessments/`

**Target:** Categorize all dist/ content  
**Progress:** 15% → 30%

### **Week 7-8: GraphRAG Clustering**
Use AI to cluster remaining standalone content:
- Run relationship mapper
- Identify natural groupings
- Create units from clusters
- Link orphaned content

**Target:** Organize remaining high-value content  
**Progress:** 30% → 50%

---

## 📊 REALISTIC MILESTONES

### **Month 1 (Weeks 1-4):**
- ✅ Discovery complete
- ✅ Integrated-lessons organized
- ✅ Integrated-handouts linked
- **Progress:** 15% organized (870 files)

### **Month 2 (Weeks 5-8):**
- ✅ Dist/ directories categorized
- ✅ GraphRAG clustering active
- ✅ Major units created
- **Progress:** 40% organized (2,318 files)

### **Month 3 (Weeks 9-12):**
- ✅ Remaining content clustered
- ✅ Quality verification complete
- ✅ Navigation finalized
- **Progress:** 70% organized (4,056 files)

### **Month 4+ (Ongoing):**
- Polish and refine
- User feedback integration
- Continuous improvement
- **Target:** 90%+ organized

---

## 🎯 IMMEDIATE NEXT STEPS

### **For You (Terminal Commands):**
```bash
# 1. Find all content files
find public -name "*.html" -type f > all-content-files.txt
wc -l all-content-files.txt

# 2. Get GraphRAG data
python3 query_graphrag.py stats
python3 analyze-content-with-graphrag.py

# 3. Review what other agents found
cat content-integration-plan.json | jq '.categories'
```

### **For Me (Based on Your Results):**
- Parse the file lists
- Match with GraphRAG data
- Create organization batches
- Build unit index pages systematically
- Track progress accurately

---

## 💡 SUCCESS CRITERIA

**NOT:** "How fast can we finish?"  
**YES:** "Are we organizing systematically with quality?"

**NOT:** "Let's add everything to navigation!"  
**YES:** "Let's organize in verified batches"

**NOT:** "We're almost done!"  
**YES:** "We're making steady, measurable progress"

---

## 🚀 THE HONEST TIMELINE

**Current:** 3.5% (200 files)  
**Month 1:** 15% (870 files)  
**Month 2:** 40% (2,318 files)  
**Month 3:** 70% (4,056 files)  
**Month 4+:** 90% (5,215 files)

**This is a 4-month systematic project!**

---

**Ready to work systematically through the real 5,500+ files?**  
**Share those terminal command results and let's organize properly!** 🎯

