# 🚨 GRAPHRAG CRITICAL GAPS - ACTION PLAN
**Created:** October 18, 2025  
**Priority:** URGENT - 534 resources unmapped  
**Impact:** 60% of core educational content is invisible

---

## 📊 THE PROBLEM

### **Discovery:**
GraphRAG audit revealed massive indexing gaps:

- **534 educational HTML files** NOT in GraphRAG (60% missing!)
- **2,582 MD files** NOT in GraphRAG (74% missing!)
- **251 root-level coordination MDs** bloating the codebase

### **Breakdown:**
| Type | Filesystem | GraphRAG | Missing | Coverage |
|------|------------|----------|---------|----------|
| Lessons (public/lessons/) | 124 | 27 | 97 | 22% |
| Handouts (public/handouts/) | 366 | 175 | 191 | 48% |
| Units (public/units/) | 393 | 147 | 246 | 37% |
| **Educational Total** | **883** | **349** | **534** | **40%** |
| MD files (all) | 3,500 | 918 | 2,582 | 26% |

---

## 🎯 PHASE 1: DELETE COORDINATION BLOAT (30 min)

### **Target: ~96 coordination MDs**

**Pattern Match & Delete:**
```bash
# Session summaries
*SESSION*.md
*SUMMARY*.md  
*COMPLETE*.md

# Agent coordination
*AGENT*.md (except AGENT_KNOWLEDGE_BASE.md)
*HUI*.md
*COORDINATION*.md

# Status reports
*STATUS*.md
*PROGRESS*.md
*VICTORY*.md
*REPORT*.md (except technical reports)

# Redundant planning
*PLAN*.md (keep deployment/architecture plans only)
```

### **KEEP These Critical MDs:**
1. `README.md` - Essential
2. `README-PRODUCTION.md` - Deployment guide
3. `DEPLOY-INSTRUCTIONS.md` - Critical
4. `GRAPHRAG-INTELLIGENCE-REPORT.md` - Just created, valuable
5. `GRAPHRAG-EXPLAINED.md` - Educational
6. `AUTH-FIX-INSTRUCTIONS.md` - Technical guide
7. `SUPABASE_SETUP_REQUIRED.md` - Setup guide
8. `ACTIVE_QUESTIONS.md` - Per repo rules
9. `BROWSER_DEBUG_STEPS.md` - Troubleshooting
10. `CACHE_FIX_INSTRUCTIONS.md` - Technical

**DELETE Everything Else in Root** (coordination noise)

---

## 🎯 PHASE 2: INDEX MISSING CORE CONTENT (2-3 hours)

### **Priority 1: Public Directory Educational Content**

#### **A. Index Missing Lessons (97 files)**
```bash
# Find unmapped lessons
find public/lessons -name "*.html" > all_lessons.txt
# Compare with GraphRAG
# Index the 97 missing files
```

**High-Value Targets:**
- Writers toolkit lessons
- Subject-specific lessons
- Interactive literacy lessons
- Curriculum-aligned lessons

#### **B. Index Missing Handouts (191 files)**
```bash
# Find unmapped handouts
find public/handouts -name "*.html" > all_handouts.txt
# Index the 191 missing files
```

**High-Value Targets:**
- Subject handouts
- Assessment rubrics
- Writers toolkit handouts
- Curriculum resources

#### **C. Index Missing Units (246 files)**
```bash
# Find unmapped units
find public/units -name "*.html" > all_units.txt
# Index the 246 missing files
```

**High-Value Targets:**
- Complete unit plans (Units 1-7 discovered earlier)
- Subject-specific units
- Cross-curricular units
- Y8 Systems resources (already partially indexed)

### **Priority 2: Important MD Documentation**

**Index These MD Categories:**
- `/docs/` - Technical documentation
- `/public/curriculum-documents/` - Curriculum guides
- Unit READMEs with learning objectives
- Assessment framework docs

**Skip These:**
- Agent coordination logs
- Session summaries
- Status reports
- Temporary planning docs

---

## 🎯 PHASE 3: BUILD INDEXING SCRIPT (1 hour)

### **Create: `index-missing-resources.py`**

```python
#!/usr/bin/env python3
"""
Index missing educational resources into GraphRAG
"""

import os
from pathlib import Path
from supabase import create_client
import re

PRIORITY_PATHS = [
    'public/lessons/',
    'public/handouts/',
    'public/units/',
    'public/games/',
    'public/activities/',
    'public/assessments/',
]

def extract_metadata(html_path):
    """Extract title, subject, level from HTML"""
    # Parse HTML for meta tags, title, content
    pass

def should_index(file_path):
    """Determine if file should be indexed"""
    # Skip backups, temp files, duplicates
    if '/backups/' in file_path:
        return False
    if '/temp/' in file_path:
        return False
    if '.backup.' in file_path:
        return False
    return True

def index_file(supabase, file_path, metadata):
    """Insert into resources table"""
    # Check if already exists
    # Extract metadata
    # Insert with proper tags
    pass

def main():
    # 1. Connect to Supabase
    # 2. For each priority path:
    #    - Find all HTML files
    #    - Check if in GraphRAG
    #    - Index if missing
    # 3. Report results
    pass
```

**Key Features:**
- ✅ Skip already-indexed files
- ✅ Extract metadata from HTML
- ✅ Batch insert for speed
- ✅ Tag with source directory
- ✅ Build relationships automatically
- ✅ Progress reporting

---

## 🎯 PHASE 4: VALIDATE & OPTIMIZE (30 min)

### **After Indexing:**

1. **Verify Count:**
   ```sql
   SELECT COUNT(*) FROM resources WHERE path LIKE '/public/lessons/%';
   SELECT COUNT(*) FROM resources WHERE path LIKE '/public/handouts/%';
   SELECT COUNT(*) FROM resources WHERE path LIKE '/public/units/%';
   ```

2. **Build Missing Relationships:**
   ```sql
   -- Find lessons without handouts
   -- Find units without lessons
   -- Find orphaned resources
   ```

3. **Tag Properly:**
   - Subject tags
   - Year level tags
   - Cultural integration tags
   - Resource type tags

4. **Test Queries:**
   - Subject hub queries
   - Search functionality
   - Relationship queries
   - Discovery features

---

## 📊 EXPECTED OUTCOMES

### **Before:**
- Resources in GraphRAG: 25,861
- Educational content coverage: 40%
- Coordination MDs: 251
- Usable docs: ~155

### **After Phase 1 (Delete):**
- Root MDs: ~60 (deleted ~190 coordination docs)
- Clean, professional repo
- Follows "BUILD DON'T DOCUMENT" rule

### **After Phase 2 (Index):**
- Resources in GraphRAG: ~26,400
- Educational content coverage: **100%** ✅
- Lessons: 124/124 (100%)
- Handouts: 366/366 (100%)
- Units: 393/393 (100%)

### **After Phase 3 (Build Relationships):**
- Relationships: ~8,000 (up from 5,324)
- Fully connected knowledge graph
- Discovery features work perfectly
- Search returns complete results

---

## ⏰ TIME ESTIMATES

| Phase | Task | Time | Cumulative |
|-------|------|------|------------|
| 1 | Delete coordination MDs | 30 min | 0:30 |
| 2A | Index missing lessons (97) | 45 min | 1:15 |
| 2B | Index missing handouts (191) | 1 hour | 2:15 |
| 2C | Index missing units (246) | 1.5 hours | 3:45 |
| 3 | Build indexing script | 1 hour | 4:45 |
| 4 | Validate & optimize | 30 min | 5:15 |

**Total Estimated Time: ~5-6 hours**

---

## 🚀 IMMEDIATE NEXT STEPS

### **Right Now:**
1. Delete ~190 coordination MDs
2. Keep only the 10-15 critical docs
3. Commit the cleanup

### **Today:**
4. Run indexing script on `/public/lessons/`
5. Run indexing script on `/public/handouts/`
6. Verify GraphRAG coverage improved

### **This Weekend:**
7. Index remaining units
8. Build missing relationships
9. Test all discovery features
10. Performance audit

---

## 💡 WHY THIS MATTERS

### **Current State:**
Teachers searching for "Year 8 Math" might get:
- 27 lessons (only 22% of what exists!)
- 175 handouts (missing 48%!)
- 147 units (missing 63%!)

### **After Indexing:**
Same search returns:
- **124 lessons** (100% coverage)
- **366 handouts** (100% coverage)
- **393 units** (100% coverage)

**Impact: Teachers find 2.5X more content!**

### **Platform Credibility:**
- "We have 25,861 resources" → TRUE  
- "All content is searchable" → **CURRENTLY FALSE** (only 40%!)
- "GraphRAG powers discovery" → **PARTIALLY** (60% missing!)

**After fixing: All claims become 100% TRUE ✅**

---

## 📋 SUCCESS METRICS

### **Phase 1 Success:**
- [ ] Root directory has <60 MDs
- [ ] All coordination docs deleted
- [ ] Only technical/essential docs remain

### **Phase 2 Success:**
- [ ] All 124 lessons in GraphRAG
- [ ] All 366 handouts in GraphRAG
- [ ] All 393 units in GraphRAG
- [ ] GraphRAG coverage: 100%

### **Phase 3 Success:**
- [ ] Relationships: 8,000+
- [ ] All lessons have handout links
- [ ] All units have lesson links
- [ ] Prerequisite chains complete

### **Phase 4 Success:**
- [ ] Subject hub queries return complete results
- [ ] Search finds all relevant content
- [ ] No "orphaned" resources
- [ ] Performance: <500ms query time

---

## 🎯 THIS IS THE FOUNDATION

**Everything else depends on this:**
- Teaching Variants Library → Needs complete index
- Y8 Systems showcase → Needs all unit pages indexed
- Homepage features → Needs accurate counts
- Discovery tools → Need complete relationship graph

**Fix the foundation first. Then build the features.**

---

*This is not coordination - this is CRITICAL INFRASTRUCTURE WORK*

