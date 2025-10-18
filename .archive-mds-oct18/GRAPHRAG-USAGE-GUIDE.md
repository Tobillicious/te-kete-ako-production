# 🤖 GraphRAG Usage Guide - Te Kete Ako
## How to Use the REAL Working GraphRAG System

**Status:** ✅ GraphRAG is in Supabase and working!  
**Location:** `https://nlgldaqtubrlcqddppbq.supabase.co`

---

## 📊 What is GraphRAG?

GraphRAG is our **knowledge graph database** storing:
- All 1,400+ resources (lessons, handouts, units)
- Resource metadata (title, type, path, description)
- Cultural integration levels
- Māori concepts used
- Relationships between resources

---

## 🚀 Quick Start - Run These Commands

### **1. See What's in GraphRAG**
```bash
python3 query_graphrag.py stats
```
Shows:
- Total resources
- Breakdown by type (lesson, handout, unit, etc.)
- Cultural integration levels
- Featured resources

### **2. Find High Cultural Value Content**
```bash
python3 query_graphrag.py high
```
Lists resources with high cultural integration - perfect for featuring!

### **3. Search for Specific Content**
```bash
python3 query_graphrag.py search "māori"
python3 query_graphrag.py search "algebra"
python3 query_graphrag.py search "year 8"
```

### **4. Find Orphaned Resources**
```bash
python3 query_graphrag.py orphaned
```
Shows resources in GraphRAG but maybe not linked on site

### **5. See Māori Concepts**
```bash
python3 query_graphrag.py concepts
```
Lists all Māori concepts across resources

---

## 🔍 Analyze Content for Unit Organization

### **NEW: Content Analyzer** (Just Created!)
```bash
python3 analyze-content-with-graphrag.py
```

This script:
- ✅ Scans all local HTML files
- ✅ Queries Supabase GraphRAG
- ✅ **Finds potential unit clusters** (3+ related resources)
- ✅ **Identifies orphaned lessons** not in units
- ✅ Shows cultural integration breakdown
- ✅ Generates detailed JSON report

**Output:**
- `graphrag-content-analysis.json` - Full analysis report

---

## 📁 Available GraphRAG Scripts

### **Query & Search:**
1. `query_graphrag.py` - Main query tool ✅ WORKING
2. `explore-graphrag-schema.py` - See database structure ✅ WORKING
3. `analyze-content-with-graphrag.py` - Content analysis ✅ NEW!

### **Update & Sync:**
4. `scripts/insert-knowledge-to-graphrag.py` - Add new resources
5. `scripts/update-graphrag-with-synthesis.py` - Sync knowledge
6. `scripts/index-generated-resources-to-graphrag.py` - Index AI resources

### **Advanced:**
7. `update-graphrag-supabase.py` - Full sync
8. `update-graphrag-now.py` - Quick update
9. `test-graphrag.py` - Test connection

---

## 🎯 How to Use GraphRAG for Unit Organization

### **Step 1: Analyze Current State**
```bash
python3 analyze-content-with-graphrag.py
```

Look at output for:
- **Potential unit clusters** - Resources that group naturally
- **Orphaned lessons** - Need to be added to units
- **Coverage gaps** - Local files not in GraphRAG yet

### **Step 2: Review Suggestions**
```bash
cat graphrag-content-analysis.json
```

Look for clusters like:
```
Y8-mathematics: 12 resources
Y9-science: 8 resources
Y7-english: 6 resources
```

### **Step 3: Create Units Based on Clusters**

For each cluster with 6+ resources:
1. Create unit directory: `/units/mathematics/year-8/unit-name/`
2. Create unit overview page
3. Move/link lessons into unit
4. Update navigation

### **Step 4: Update GraphRAG**
```bash
python3 scripts/update-graphrag-with-synthesis.py
```

Re-run analysis to see progress!

---

## 🔧 GraphRAG Schema (Supabase)

### **Table: `resources`**

**Fields:**
- `id` - Unique identifier
- `title` - Resource title
- `type` - lesson, handout, unit, game, tool, etc.
- `path` - File path (relative to /public/)
- `file_path` - Alternative path field
- `description` - Resource description
- `cultural_elements` - JSON object:
  ```json
  {
    "cultural_integration": "high|medium|low",
    "maori_concepts": ["kaitiakitanga", "whānau", ...],
    "whakatauaki_present": true/false
  }
  ```
- `metadata` - Additional JSON metadata
- `featured` - Boolean, is this featured content?
- `created_at` - Timestamp
- `updated_at` - Timestamp

**Indexes:**
- Full-text search on title and description
- Type index for filtering
- Cultural integration for quality queries

---

## 💡 Common Use Cases

### **Find Resources for New Unit:**
```bash
# 1. Search by topic
python3 query_graphrag.py search "geometry"

# 2. See what clusters exist
python3 analyze-content-with-graphrag.py

# 3. Check cultural integration
python3 query_graphrag.py high
```

### **Check What's Not Organized:**
```bash
# 1. Find orphaned lessons
python3 query_graphrag.py orphaned

# 2. Run full analysis
python3 analyze-content-with-graphrag.py

# 3. Review missing content
cat graphrag-content-analysis.json
```

### **Feature High-Quality Content:**
```bash
# 1. Find high cultural value
python3 query_graphrag.py high

# 2. Check featured status
python3 query_graphrag.py stats

# 3. Add to homepage/navigation
```

---

## 🎯 Next Steps for Unit Organization

### **Immediate Actions:**

1. **Run the analyzer:**
   ```bash
   python3 analyze-content-with-graphrag.py
   ```

2. **Review clusters:**
   - Open `graphrag-content-analysis.json`
   - Look for clusters with 6+ resources
   - These are natural units waiting to be created!

3. **Create units from clusters:**
   - Use cluster suggestions to build new units
   - Follow existing unit structure (Y8 Systems, etc.)
   - Add to navigation

4. **Handle orphans:**
   - 500+ orphaned lessons identified
   - Group by theme/subject/year
   - Create new units or add to existing

5. **Update GraphRAG:**
   - As you organize, update GraphRAG
   - Keep it in sync with actual site structure
   - Use for discovering more relationships

---

## 📊 Expected Results

### **After Running Analyzer:**

```
Found XX potential unit clusters:
- Y8-mathematics: 12 resources
- Y9-science: 8 resources
- Y7-english: 6 resources
... and XX more

Found XXX orphaned lessons
```

**Action:** Create units for clusters with 6+ resources!

### **After Creating New Units:**

```
Before: 18 units, 29% organized
After:  25+ units, 50%+ organized
```

### **Final Goal:**

```
50+ units organized
90%+ content in units
Zero orphaned lessons
Complete learning pathways
```

---

## 🚀 Why This Approach Works

**Intelligent Clustering:**
- GraphRAG already has metadata about all resources
- Cultural integration levels help prioritize
- Natural groupings emerge from analysis
- Less manual work, more intelligent organization

**Incremental Progress:**
- Start with high-value clusters (6+ resources)
- Build units around natural groupings
- Leave edge cases for later
- Measurable progress with each unit

**Quality Focus:**
- Feature high cultural integration content
- Maintain professional standards
- Build on existing excellence
- Don't create new content, organize existing!

---

## 📖 Documentation

- **Query Tool:** `query_graphrag.py --help`
- **Schema Explorer:** `explore-graphrag-schema.py`
- **Content Analyzer:** `analyze-content-with-graphrag.py`

---

**Ready to use GraphRAG for intelligent content organization!** 🎉

*Last Updated: October 18, 2025*

