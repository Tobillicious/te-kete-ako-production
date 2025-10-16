# 🧠 Agent Knowledge Access Guide

**Last Updated:** 2025-10-16  
**For:** All Te Kete Ako AI Agents

---

## 📚 WHERE TO FIND INFORMATION

### 1. **TE_KETE_KNOWLEDGE_BASE.json** (Complete Backup)
- **What:** ALL content from MD files, searchable JSON
- **When to use:** Need to find specific content from old MDs
- **How to search:** `grep "your search term" TE_KETE_KNOWLEDGE_BASE.json`

### 2. **MASTER_*.md Files** (Organized by Topic)
- `MASTER_TECHNICAL_SPECS.md` - Auth, database, PWA, CSS, infrastructure
- `MASTER_AGENT_COORDINATION.md` - How agents work together
- `MASTER_PROGRESS_LOGS.md` - What's been done, when, by whom
- **When to use:** Need comprehensive info on a specific domain
- **How to use:** Read the relevant master file directly

### 3. **GraphRAG** (Semantic Knowledge Graph - via MCP Supabase)
```bash
# Query GraphRAG for resources
python3 -c "import mcp_supabase; mcp_supabase.query('your search')"
```
- **What:** Structured knowledge about resources, lessons, relationships
- **When to use:** Finding curriculum content, lesson plans, resources
- **Status:** Connected via MCP

### 4. **ACTIVE_QUESTIONS.md** (For Questions Only!)
- **What:** Questions agents need answered (NOT a knowledge dump)
- **When to use:** You have a question for other agents or the user
- **Format:**
```markdown
## [Agent-ID] Question Title (Date)
- **Context:** Why asking
- **Question:** What you need to know
- **Status:** OPEN/ANSWERED
```

### 5. **agent-coordinator.py** (Real-time Task Coordination)
```bash
# Check what others are doing
python3 scripts/agent-coordinator.py --status

# Claim a task
python3 scripts/agent-coordinator.py --claim agent-ID "Task description"

# Update progress
python3 scripts/agent-coordinator.py --update agent-ID "What I did"

# Complete task
python3 scripts/agent-coordinator.py --complete agent-ID
```

---

## 🚫 WHAT NOT TO DO

1. **DON'T create new MD files** (except master ones above)
2. **DON'T duplicate information** across multiple locations
3. **DON'T store knowledge in terminal output** - use the systems above

---

## ✅ WORKFLOW FOR ANY AGENT

```
1. Check in: agent-coordinator.py --check-in agent-ID
2. Check status: agent-coordinator.py --status
3. Need info? 
   → Search TE_KETE_KNOWLEDGE_BASE.json
   → Read relevant MASTER_*.md
   → Query GraphRAG if needed
4. Have question? Add to ACTIVE_QUESTIONS.md
5. Claim task: agent-coordinator.py --claim
6. Do work, update every 30 mins
7. Complete: agent-coordinator.py --complete
```

---

## 📖 QUICK REFERENCE

| Need to... | Use this... |
|-----------|------------|
| Find old MD content | `TE_KETE_KNOWLEDGE_BASE.json` |
| Learn about auth system | `MASTER_TECHNICAL_SPECS.md` |
| See what others did | `MASTER_PROGRESS_LOGS.md` |
| Understand agent workflow | `MASTER_AGENT_COORDINATION.md` |
| Ask a question | `ACTIVE_QUESTIONS.md` |
| Coordinate tasks | `agent-coordinator.py` |
| Find curriculum resources | GraphRAG (MCP Supabase) |

---

**🎯 GOLDEN RULE: One source of truth per domain. Query, don't duplicate.**

