# ⚡ GRAPHRAG QUICK REFERENCE CARD
**Keep this open while working!**

---

## 🎯 INSTANT INTELLIGENCE (Copy & Run)

### Get Platform Stats:
```bash
python3 query_graphrag.py stats
```

### Get Your Intelligence Brief:
```bash
python3 scripts/agent-intelligence-amplifier.py
```

### Search for Content:
```bash
python3 query_graphrag.py search "kaitiakitanga"
python3 query_graphrag.py search "mathematics"
python3 query_graphrag.py search "year 8"
```

### Find High-Cultural Resources:
```bash
python3 query_graphrag.py high
```

### Find Orphaned Gems:
```bash
python3 query_graphrag.py orphaned
```

---

## 📊 PLATFORM STATE (Current)

- **1,640 resources** total
- **231,679 relationships** mapped
- **621 gold standard** (Q90+)
- **627 culturally integrated**

**Excellence by Subject:**
- Social Studies: 100% cultural ✅
- Digital Tech: 100% cultural ✅
- Science: 47% cultural ⚠️
- Math: 34% cultural ⚠️

---

## 🌟 SUPER-HUBS (Build FROM These!)

1. **Algebraic Thinking Māori Games**: 221 connections
2. Biotechnology Ethics Māori: 129 connections
3. Data Visualization Cultural: 120 connections
4. Cultural Safety Checklists: 111 connections
5. Media Literacy Māori: 98 connections

**Strategy:** Connect TO/FROM these for 100x reach

---

## 🔗 PROVEN RELATIONSHIP TYPES

1. **unit_contains_lesson** (0.972 confidence) ⭐
2. **prerequisite_for** (0.950 confidence) ⭐
3. **shared_cultural_wisdom** (0.920 confidence) ⭐

**Use these for highest success rate!**

---

## 💎 UNDERUTILIZED GEMS (Scale These!)

30 relationship types used only ONCE:
- critical_analysis
- bicultural_competence
- applied_mathematics
- career_pathway_sequence
- arts_integration

**Opportunity:** 30 types × 100 uses = 3,000 new connections!

---

## 🎯 GOLD STANDARD MODEL

**Y8 Digital Kaitiakitanga:**
- 18 sequential lessons
- 385 complete pathways
- 0.958 average confidence
- 100% cultural integration
- Quality 90.5

**Pattern:** Replicate for other units!

---

## 🔥 CRITICAL GAPS

**Year Bridges (Need Building!):**
- Y7→Y8: Only 4 bridges 🔴
- Y9→Y10: Only 3 bridges 🔴
- Y11→Y12: ~0 bridges 🔥
- Y12→Y13: ~0 bridges 🔥

**Cultural Enrichment Needed:**
- Science excellence: 639 resources
- Math excellence: 592 resources
Total: 1,231 Q90+ resources need cultural context!

---

## 🚀 TOP 5 HIGH-IMPACT ACTIONS

### 1. Connect Orphaned Gems
**What:** 47 alpha resources (Q90+) need linking  
**Time:** 30 minutes  
**Impact:** Unlock hidden excellence

### 2. Build Y11→Y13 Bridges
**What:** Create 20-30 senior secondary prerequisites  
**Time:** 2-3 hours  
**Impact:** Complete NCEA pathways

### 3. Replicate Y8 Digital Model
**What:** Pick 1 unit, build 18-lesson chain  
**Time:** 60 minutes  
**Impact:** 385 new pathways

### 4. Scale Underutilized Relationships
**What:** Pattern-match & replicate 1-use types  
**Time:** 4-5 hours  
**Impact:** 3,000 new semantic connections

### 5. Cultural Enrichment Sprint
**What:** Add cultural context to 50 Q90+ resources  
**Time:** 2-3 hours  
**Impact:** Excellence → Transcendence

---

## 🧠 BEFORE YOU BUILD

✅ Query GraphRAG for existing work  
✅ Check agent_knowledge for recent discoveries  
✅ Identify super-hubs to leverage  
✅ Use proven relationship types  
✅ Add cultural frameworks  

---

## 💡 QUICK QUERIES (SQL)

### Find Super-Hubs:
```sql
SELECT r.title, COUNT(*) as connections
FROM graphrag_resources r
JOIN graphrag_relationships rel 
  ON r.file_path = rel.source_path OR r.file_path = rel.target_path
GROUP BY r.title
HAVING COUNT(*) >= 100
ORDER BY COUNT(*) DESC;
```

### Find Orphans:
```sql
SELECT r.title, r.quality_score, COUNT(rel.id) as connections
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel 
  ON r.file_path = rel.source_path OR r.file_path = rel.target_path
WHERE r.quality_score >= 90
GROUP BY r.title, r.quality_score
HAVING COUNT(rel.id) < 5
ORDER BY r.quality_score DESC;
```

### Recent Agent Work:
```sql
SELECT source_name, key_insights[1:2]
FROM agent_knowledge
WHERE created_at > NOW() - INTERVAL '7 days'
ORDER BY created_at DESC;
```

---

## 🌿 CULTURAL FRAMEWORKS

**Proven to boost quality:**
- Digital Kaitiakitanga (0.958 confidence)
- Kaitiakitanga Progression (0.96 confidence)
- Te Whare Tapa Whā (0.93 confidence)
- Tino Rangatiratanga (0.94 confidence)
- Toi Māori (0.92-0.93 confidence)

**Apply to:** Any content for cultural + quality boost!

---

## 🔧 TOOLS AVAILABLE

### Working Tools ✅:
- `mcp_supabase_execute_sql` - SQL queries (USE THIS!)
- `query_graphrag.py` - Quick stats
- `scripts/agent-intelligence-amplifier.py` - Intelligence briefs
- File operations (read, write, grep, etc.)

### BROKEN (Don't Use!) ❌:
- `run_terminal_cmd` - HANGS FOREVER!

**Always use MCP Supabase for database queries!**

---

## 📚 KEY DOCUMENTS

Must-read before building:
1. `START_HERE_NEW_AGENTS.md` (60 seconds)
2. `GRAPHRAG-MASTER-INTELLIGENCE-GUIDE.md` (this guide's big brother)
3. `GRAPHRAG-INTELLIGENCE-ALL-AGENTS.md` (agent-specific playbooks)
4. `graphrag-intelligence-expansion-todos.sql` (12 strategic TODOs)

---

## ⚡ ONE-LINER POWER COMMANDS

```bash
# Complete intelligence package
python3 scripts/agent-intelligence-amplifier.py && python3 query_graphrag.py stats

# Search everything
python3 query_graphrag.py search "your_topic"

# Find work opportunities
python3 query_graphrag.py orphaned && python3 query_graphrag.py high
```

---

## 🎯 SUCCESS FORMULA

1. **Query first** (don't guess!)
2. **Build FROM super-hubs** (leverage network)
3. **Use proven patterns** (Y8 Digital model)
4. **Add cultural context** (boosts quality)
5. **Share discoveries** (agent_knowledge table)

---

## 💚 REMEMBER

*"Ehara taku toa i te toa takitahi, engari he toa takitini"*

Your strength comes from the collective. Query GraphRAG, learn from others, build amazing things, share your discoveries!

---

**Keep this card open. Reference it constantly. Get exponentially smarter!** 🚀

