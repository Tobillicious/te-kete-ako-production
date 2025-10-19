# 📚 Te Kete Ako: Literacy Restructure Plan
**Date:** October 19, 2025  
**Agent:** GraphRAG Integration Specialist  
**Status:** PLANNING → IMPLEMENTATION

---

## 🎯 **THE MOE FRAMEWORK**

### **New Zealand Ministry of Education Guidelines:**
- **1 hour daily** of Reading
- **1 hour daily** of Writing  
- **1 hour daily** of Mathematics

### **Subject Structure:**

#### **LITERACY (Years 7-8, Foundation for All)**
1. **READING**
   - Comprehension
   - Fluency
   - Vocabulary development
   - Can include Te Reo texts

2. **WRITING**
   - Composition
   - Mechanics
   - Expression
   - Can include Te Reo writing

**Note:** Reading and Writing are SEPARATE subjects until Year 9, but deeply intertwined and can be linked in lessons.

#### **ENGLISH (Years 9-13)**
- Text analysis
- Literary devices
- Critical interpretation
- Essay writing
- Formal discourse

---

## 📊 **GRAPHRAG CURRENT STATE**

### **Resource Breakdown (from 2,212 "English" resources):**
```
✍️ Writing:          204 resources
📖 Reading:          187 resources
📚 General Literacy: 197 resources
🎓 English Analysis:  58 resources
🛠️ Writers Toolkit:  935 resources (!!!)
❓ Uncategorized:   1,566 resources (need better tagging)
```

### **Key Discovery:**
The **Writers Toolkit** has **935 resources** - this is a MASSIVE collection that should be the centerpiece of the Writing Hub!

---

## 🏗️ **PROPOSED STRUCTURE**

### **1. READING HUB** (New)
**Target:** Years 7-8 + foundation for all levels  
**Resources:** 187+ GraphRAG resources

**Sections:**
- 📖 Comprehension Strategies
- 🔤 Vocabulary Building
- 🗣️ Te Reo Reading Materials
- 📚 Guided Reading Resources
- 🎯 Reading Assessment Tools

**GraphRAG Query:**
```sql
WHERE (title ILIKE '%reading%' OR title ILIKE '%comprehension%')
AND year_level IN ('Year 7', 'Year 8', 'Years 7-8')
```

---

### **2. WRITING HUB** (New)
**Target:** Years 7-8 + foundation for all levels  
**Resources:** 935 (Writers Toolkit) + 204 = **1,139+ resources**

**Centerpiece:** 🛠️ **Writers Toolkit** (935 resources, 18-step learning pathway!)

**Sections:**
- ✍️ **Writers Toolkit** (18 comprehensive lessons)
- 📝 Composition Skills
- 🎨 Creative Writing
- 📋 Writing Mechanics
- 🗣️ Te Reo Writing
- 🎯 Writing Assessment

**GraphRAG Query:**
```sql
WHERE (file_path LIKE '%writers-toolkit%' 
   OR title ILIKE '%writing%' 
   OR title ILIKE '%composition%')
```

---

### **3. ENGLISH HUB** (Restructured)
**Target:** Years 9-13 (Higher-level analysis)  
**Resources:** 58 analysis + higher-level content

**NEW FOCUS:**
- 📖 Literary Analysis
- 🎭 Text Interpretation
- ✍️ Essay Writing (formal)
- 📚 Literature Studies
- 🎓 NCEA Preparation (Levels 1-3)
- 🗣️ Oral Language & Debate

**GraphRAG Query:**
```sql
WHERE (title ILIKE '%analysis%' 
   OR title ILIKE '%essay%' 
   OR title ILIKE '%literature%')
AND year_level IN ('Year 9', 'Year 10', 'Year 11', 'Year 12', 'Year 13', 'Years 9-13')
```

---

## 🔗 **LEARNING PROGRESSION PATHWAYS**

### **The Literacy → English Journey:**

```
YEAR 7-8: LITERACY FOUNDATION
├── READING (1 hr/day)
│   ├── Comprehension strategies
│   ├── Vocabulary development
│   └── Fluency practice
│
└── WRITING (1 hr/day)
    ├── Writers Toolkit (18 steps)
    ├── Composition basics
    └── Mechanics & expression

         ↓ BUILDS TO ↓

YEAR 9-13: ENGLISH (Analysis)
├── Text analysis
├── Literary interpretation
├── Essay writing
├── Critical thinking
└── NCEA assessment
```

---

## 🎯 **IMPLEMENTATION PLAN**

### **Phase 1: Create New Hubs** ✅ READY
1. ✅ Create `reading-hub.html`
   - Query GraphRAG for reading resources
   - MOE daily reading emphasis
   - Y7-8 focus + foundation skills
   
2. ✅ Create `writing-hub.html`
   - Showcase Writers Toolkit (935 resources!)
   - Query GraphRAG for writing resources
   - MOE daily writing emphasis
   - Y7-8 focus + foundation skills

3. ✅ Restructure `english-hub.html`
   - Shift to Y9-13 analysis focus
   - Literary & critical thinking
   - Higher-level skills

### **Phase 2: GraphRAG Enhancement** 🔄 IN PROGRESS
1. Update resource tagging in GraphRAG
2. Add MOE category metadata:
   - `literacy_strand: 'reading'`
   - `literacy_strand: 'writing'`
   - `literacy_strand: 'english_analysis'`
3. Improve categorization of 1,566 uncategorized resources

### **Phase 3: Navigation Updates** 📋 PENDING
1. Update main navigation:
   ```
   OLD: English Hub
   NEW: Reading | Writing | English
   ```
2. Update subject hub page
3. Add "MOE Framework" badge/indicator

### **Phase 4: Learning Pathways** 🧠 PENDING
1. GraphRAG-powered progression mapping
2. Show Reading → Writing → English journey
3. Prerequisite relationships
4. Cross-linking between hubs

---

## 📈 **EXPECTED OUTCOMES**

### **Benefits:**
1. ✅ **MOE Compliance** - Aligns with daily 1-hour structure
2. ✅ **Clarity** - Teachers know exactly where to find resources
3. ✅ **Progression** - Clear pathway from Y7-8 literacy → Y9-13 analysis
4. ✅ **Discovery** - Writers Toolkit (935 resources) gets proper visibility
5. ✅ **Cultural Integration** - Te Reo can be properly integrated across all three

### **GraphRAG Power:**
- Real-time resource counts
- Quality scoring
- Cultural integration metrics
- Semantic learning pathways
- Relationship mapping (231,469 connections!)

---

## 🛠️ **TECHNICAL NOTES**

### **GraphRAG Queries to Run:**

```javascript
// Reading Resources
const readingResources = await supabase
  .from('graphrag_resources')
  .select('*')
  .or('title.ilike.%reading%,title.ilike.%comprehension%')
  .order('quality_score', { ascending: false });

// Writing Resources (including Writers Toolkit)
const writingResources = await supabase
  .from('graphrag_resources')
  .select('*')
  .or('file_path.like.%writers-toolkit%,title.ilike.%writing%')
  .order('quality_score', { ascending: false });

// English Analysis (Y9-13)
const englishResources = await supabase
  .from('graphrag_resources')
  .select('*')
  .or('title.ilike.%analysis%,title.ilike.%essay%,title.ilike.%literature%')
  .in('year_level', ['Year 9', 'Year 10', 'Year 11', 'Year 12', 'Year 13'])
  .order('quality_score', { ascending: false });
```

---

## 🎨 **VISUAL IDENTITY**

### **Color Coding:**
- 📖 **Reading Hub**: Blue (#3b82f6)
- ✍️ **Writing Hub**: Red (#dc2626) - current English color
- 🎓 **English Hub**: Purple (#7c3aed) - higher-level analysis

### **Icons:**
- Reading: 📖 🔤 👀
- Writing: ✍️ 📝 🖊️
- English: 🎓 📚 🎭

---

## ✅ **SUCCESS CRITERIA**

1. ✅ Three distinct hubs (Reading, Writing, English)
2. ✅ GraphRAG-powered resource discovery
3. ✅ MOE framework compliance
4. ✅ Clear Y7-8 → Y9-13 progression
5. ✅ Writers Toolkit properly showcased
6. ✅ Cultural integration across all three
7. ✅ Updated navigation
8. ✅ Learning pathway visualization

---

## 🚀 **NEXT ACTIONS**

**IMMEDIATE:**
1. Create `reading-hub.html` with GraphRAG integration
2. Create `writing-hub.html` with Writers Toolkit showcase
3. Restructure `english-hub.html` for Y9-13 analysis

**THEN:**
4. Update main navigation
5. Add MOE framework indicators
6. Create cross-linking pathways

**FINALLY:**
7. Commit all changes
8. Update documentation
9. Celebrate the MOE-aligned structure! 🎉

---

**This restructure honors:**
- ✅ NZ Ministry of Education guidelines
- ✅ GraphRAG intelligence (19,737 resources, 231,469 relationships)
- ✅ Te Ao Māori integration
- ✅ Teacher workflow (1 hour daily structure)
- ✅ Student learning progression (Y7-8 → Y9-13)

**Nā te GraphRAG, nā te MOE, nā te ako!** 🌟

