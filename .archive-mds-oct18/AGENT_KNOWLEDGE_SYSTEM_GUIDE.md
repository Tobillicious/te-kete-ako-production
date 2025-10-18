# 🧠 AGENT KNOWLEDGE SYSTEM GUIDE

**Quick Reference:** How to access preserved knowledge without creating new MD files

---

## 🎯 **THREE-LAYER KNOWLEDGE SYSTEM:**

### **Layer 1: MCP Export** (Real-time coordination)
**File:** `MCP_KNOWLEDGE_EXPORT.json`  
**Use for:** Agent coordination, current tasks, live status

```bash
# View coordination knowledge
cat MCP_KNOWLEDGE_EXPORT.json | jq '.knowledge_categories.coordination'

# View technical knowledge
cat MCP_KNOWLEDGE_EXPORT.json | jq '.knowledge_categories.technical'
```

### **Layer 2: GraphRAG Export** (Knowledge graph)
**File:** `GRAPHRAG_KNOWLEDGE_EXPORT.json`  
**Use for:** Finding relationships, semantic search

```bash
# View all knowledge nodes
cat GRAPHRAG_KNOWLEDGE_EXPORT.json | jq '.nodes[] | {id, category, importance_score}'

# View relationships
cat GRAPHRAG_KNOWLEDGE_EXPORT.json | jq '.edges[] | {source, target, relationship}'
```

### **Layer 3: SQLite Database** (Structured queries)
**File:** `knowledge_preservation.db`  
**Use for:** Fast specific queries, filtering by importance

```bash
# High importance coordination
sqlite3 knowledge_preservation.db "SELECT * FROM coordination_knowledge WHERE importance_score >= 70;"

# Technical knowledge
sqlite3 knowledge_preservation.db "SELECT * FROM technical_knowledge;"

# Search by content
sqlite3 knowledge_preservation.db "SELECT * FROM status_knowledge WHERE content LIKE '%auth%';"
```

---

## 📋 **MASTER FILES (Human-readable):**

1. **`ACTIVE_QUESTIONS.md`** - Coordination & task tracking
2. **`README.md`** - Project overview
3. **`progress-log.md`** - Historical timeline
4. **`__USE_ONLY_THESE_FILES__.md`** - File usage rules

---

## 🚀 **QUICK COMMANDS:**

### **Test the knowledge system:**
```bash
python3 scripts/test-knowledge-queries.py
```

### **Query preserved knowledge:**
```bash
# All coordination items
sqlite3 knowledge_preservation.db "SELECT COUNT(*) FROM coordination_knowledge;"

# High importance across all categories
for table in coordination technical content progress documentation status; do
    echo "=== ${table}_knowledge ==="
    sqlite3 knowledge_preservation.db "SELECT COUNT(*) FROM ${table}_knowledge WHERE importance_score >= 70;"
done
```

### **Access specific knowledge:**
```python
import sqlite3
import json

# SQLite query
conn = sqlite3.connect('knowledge_preservation.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM technical_knowledge WHERE importance_score >= 60")
results = cursor.fetchall()

# MCP query
with open('MCP_KNOWLEDGE_EXPORT.json') as f:
    mcp = json.load(f)
    coordination = mcp['knowledge_categories']['coordination']
    
# GraphRAG query
with open('GRAPHRAG_KNOWLEDGE_EXPORT.json') as f:
    graph = json.load(f)
    nodes = [n for n in graph['nodes'] if n['importance_score'] >= 70]
```

---

## ✅ **RULES:**

1. **DO NOT** create new MD files
2. **DO** update `ACTIVE_QUESTIONS.md` for coordination
3. **DO** query the knowledge system for information
4. **DO** use MCP for real-time coordination
5. **DO** use GraphRAG for knowledge discovery
6. **DO** use SQLite for specific queries

---

## 🎯 **PRESERVED KNOWLEDGE CATEGORIES:**

- **Coordination (59 items)** - Agent coordination, team status, tasks
- **Technical (9 items)** - CSS, JS, HTML, code architecture
- **Content (25 items)** - Educational resources, curriculum
- **Progress (32 items)** - Development milestones, achievements
- **Documentation (20 items)** - Guides, manuals, specs
- **Status (55 items)** - Current state, readiness, issues

---

**Total: 200 items of preserved knowledge, zero information lost!** 🎉

