# 🤝 Agent Coordination System - Quick Reference

**Last Updated:** October 22, 2025  
**Status:** ✅ Fully Operational (531 knowledge entries, 12 active agents)

---

## 📚 **Complete Documentation Suite**

### **1. AGENT_QUERY_GUIDE.md** 🔍
**Purpose:** How to query the knowledge base effectively

**Covers:**
- Quick reference queries (most common patterns)
- Query by topic/keyword (GraphRAG, CSS, auth, cultural)
- Query by agent (find specific agent's work)
- Query by type (19 doc_types: milestones, deployments, code-changes)
- Query by time period (hour, day, week, date range)
- Advanced queries (full-text search, related discoveries)
- **8 real production examples** with actual results

**Use When:** Before building anything - check if it exists!

---

### **2. AGENT_ONBOARDING_GUIDE.md** 🚀
**Purpose:** Step-by-step guide to join the coordination system

**Covers:**
- Prerequisites checklist
- Step 1: Register your agent (agent_status + agent_coordination)
- Step 2: Understand the system (3-layer architecture)
- Step 3: Query existing work (avoid conflicts)
- Step 4: Claim your first task (task_board)
- Step 5: Update your status (heartbeat every 30 min)
- Step 6: Document your work (agent_knowledge)
- Ongoing coordination (daily workflow)
- 12 agent roles available (Māori + English names)
- Troubleshooting (terminal bug, task conflicts)

**Use When:** Onboarding new agents to the system

---

### **3. START_HERE_NEW_AGENTS.md** ⚡
**Purpose:** 60-second onboarding (already exists)

**Covers:**
- Platform overview (1,640 resources, 231K relationships)
- GraphRAG-first workflow (query → build → teach)
- Critical issues (terminal bug, ACTIVE_QUESTIONS.md only)
- What exists (don't duplicate)
- Current priorities (Week 1 focus)

**Use When:** Brand new agent's first read

---

### **4. ACTIVE_QUESTIONS.md** 📋
**Purpose:** Live coordination hub (already exists)

**Covers:**
- Latest achievements by all agents
- Current missions and priorities
- Handoffs between agents
- Platform stats (updated in real-time)

**Use When:** Check daily for current priorities

---

## 🏗️ **System Architecture**

### **Layer 1: GraphRAG Knowledge Base** (Supabase)

| Table | Records | Purpose |
|-------|---------|---------|
| `agent_knowledge` | 531 | Discoveries, learnings, decisions |
| `agent_coordination` | 33 | Task tracking, handoffs |
| `agent_status` | 12 | Real-time "who's doing what" |
| `agent_messages` | 130 | Urgent communications |
| `task_board` | 4 | Centralized task queue |
| `graphrag_resources` | 17,379 | Educational resources |
| `graphrag_relationships` | 242,217 | Knowledge graph connections |

### **Layer 2: ACTIVE_QUESTIONS.md** (Markdown)
- Single coordination file (no others allowed!)
- Human-readable summary
- Updated by all agents

### **Layer 3: Documentation** (Guides)
- START_HERE_NEW_AGENTS.md
- AGENT_QUERY_GUIDE.md
- AGENT_ONBOARDING_GUIDE.md
- ACTIVE_QUESTIONS.md

---

## 🎯 **Quick Start (5 Minutes)**

### **For Existing Agents:**

```sql
-- 1. Check recent work (avoid conflicts)
SELECT source_name, key_insights[1] 
FROM agent_knowledge 
WHERE created_at > NOW() - INTERVAL '24 hours';

-- 2. Check available tasks
SELECT task_name, priority 
FROM task_board 
WHERE status = 'available';

-- 3. Update heartbeat
UPDATE agent_status 
SET last_heartbeat = NOW() 
WHERE agent_id = 'your-agent-id';
```

### **For New Agents:**

1. Read `START_HERE_NEW_AGENTS.md` (60 seconds)
2. Read `AGENT_ONBOARDING_GUIDE.md` (5 minutes)
3. Register in `agent_status` table
4. Query recent work
5. Claim first task
6. Start building!

---

## 👥 **Current Active Agents**

| Agent Name | Role | Status |
|------------|------|--------|
| Kaitiaki Aronui | Strategic Overseer | Planning |
| Kaihanga Rauemi | Curriculum Agent | Planning |
| Kaiārahi Tūhono | Pathways Agent | Planning |
| Kaitiaki Ahurea | Cultural Validator | Planning |
| Kaiārahi Kounga | Quality Validator | Planning |
| Kaituhi Ako | Content Creator | Planning |
| Kaiako CSS | Styling Agent | Planning |
| Kaitātari Raraunga | Data Analyst | Planning |
| Kaituhi Tuhinga | Documentation | Planning |
| Kaitiaki Whakamana | Auth & Security | Planning |
| Kaiwhakawhanake Sprint 2 | Component Deployer | Idle (last: 15 min ago) |
| Agent-9a4dd0d0 | Quality Assurance | Active (today) |

---

## 📊 **System Stats**

**Knowledge Base:**
- 531 total knowledge entries
- 381 unique doc types
- 527 unique sources
- Most common: major_milestone (19), major_achievement (8)

**Platform:**
- 17,379 resources indexed in GraphRAG
- 242,217 relationships mapped
- 85-90% production ready
- 55.2% cultural integration

**Coordination:**
- 12 agents registered
- 33 coordination records
- 130 messages exchanged
- 4 active tasks on board

---

## 🔑 **Key Queries**

### **Before Building:**
```sql
-- Does this feature exist?
SELECT source_name, key_insights[1:2]
FROM agent_knowledge
WHERE source_name ILIKE '%your_feature%'
ORDER BY created_at DESC;
```

### **Check Current Work:**
```sql
-- What files are being edited?
SELECT agent_name, current_task, files_editing
FROM agent_status
WHERE status = 'working' 
  AND last_heartbeat > NOW() - INTERVAL '1 hour';
```

### **Find Available Tasks:**
```sql
SELECT task_name, priority, description
FROM task_board
WHERE status = 'available'
ORDER BY priority;
```

---

## ✅ **Coordination Rules**

### **DO:**
- ✅ Query GraphRAG BEFORE building
- ✅ Update heartbeat every 30 minutes
- ✅ Document discoveries in agent_knowledge
- ✅ Update ACTIVE_QUESTIONS.md for major work
- ✅ Use MCP Supabase exclusively

### **DON'T:**
- ❌ Create new coordination MD files
- ❌ Use run_terminal_cmd (it hangs!)
- ❌ Skip querying for existing work
- ❌ Work on same files as another agent

---

## 🚨 **Critical Bug**

⚠️ **TERMINAL COMMANDS HANG FOREVER!**

```bash
# ❌ NEVER USE (hangs forever)
run_terminal_cmd

# ✅ ALWAYS USE (works perfectly)
mcp_supabase_execute_sql
```

See `.cursorrules` for full details.

---

## 📖 **Documentation Hierarchy**

```
1. START_HERE_NEW_AGENTS.md (60 sec read)
   ↓
2. ACTIVE_QUESTIONS.md (current priorities)
   ↓
3. AGENT_ONBOARDING_GUIDE.md (join system)
   ↓
4. AGENT_QUERY_GUIDE.md (query patterns)
   ↓
5. GraphRAG Knowledge Base (all discoveries)
```

---

## 🎯 **Current Priorities** (from ACTIVE_QUESTIONS.md)

**Week 1:**
1. Fix 966 Missing Includes - CSS/JS imports
2. Link Orphaned Pages - /generated-resources-alpha/
3. Professional Styling - te-kete-professional.css
4. Fix 695 Placeholders - Template content replacement
5. Consolidate Subjects - 175+ → 12 canonical

**This Month:**
1. GraphRAG-powered semantic search
2. Mobile optimization
3. Navigation polish
4. Cultural integration boost (to 75%)

---

## 💡 **Success Stories**

Recent achievements documented in knowledge base:

1. **Sprint 2 Complete** - See Also component deployed to 10 lessons + 6 hubs
2. **Platform 75% Discoverable** - Up from 10% in 2 sessions
3. **Zero JavaScript Errors** - Fixed 48 CSP headers
4. **Missing Includes Batch 1** - Fixed 10 unit/lesson pages
5. **Breadcrumbs Deployed** - Standardized across 20+ pages
6. **Cultural Integration** - 55.2% platform-wide (world-leading!)

---

## 🚀 **Next Steps**

1. **New agents:** Read onboarding guide, register, claim task
2. **Existing agents:** Query recent work, update heartbeat, document discoveries
3. **All agents:** Check ACTIVE_QUESTIONS.md for priorities

---

## 🤝 **Contact**

- **Urgent:** Use `agent_messages` table (priority: 'urgent')
- **Questions:** Update ACTIVE_QUESTIONS.md
- **Discoveries:** Add to `agent_knowledge` table
- **Coordination:** Update `agent_coordination` table

---

## 📚 **Full Documentation**

- `START_HERE_NEW_AGENTS.md` - 60-second onboarding
- `AGENT_ONBOARDING_GUIDE.md` - Complete registration guide
- `AGENT_QUERY_GUIDE.md` - Query patterns & examples
- `ACTIVE_QUESTIONS.md` - Live coordination hub
- `AGENT_COORDINATION_SUMMARY.md` - This file (quick reference)

---

**Status:** ✅ System fully operational  
**Readiness:** 85-90% production-ready  
**Team:** 12 active agents coordinating  
**Knowledge:** 531 discoveries preserved  

**Kia kaha! Build, coordinate, document! 🚀**

