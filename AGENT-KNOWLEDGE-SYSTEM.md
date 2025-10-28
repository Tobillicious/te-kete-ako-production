# 🧠 Agent Knowledge System - Complete Guide

**For:** All AI agents working on Te Kete Ako  
**Created:** October 28, 2025  
**Status:** Production-ready

---

## 🎯 **What This Is:**

GraphRAG now tracks **TWO types of knowledge:**

1. **Teaching Content** (126 resources) - Units, lessons, handouts, games
2. **Agent Documentation** (15 docs) - Handoffs, protocols, status reports

**Purpose:** New agents can understand the system in **2-3 queries** instead of reading 100 files.

---

## 📊 **Current System State:**

```
📚 Teaching Resources: 126
📄 Agent Docs:         15
🔗 Total Relationships: 51
💾 Database Size:      ~1 MB (tiny!)
```

---

## 🚀 **Agent Onboarding (Start Here):**

### **Query 1: What should I know?**
```sql
SELECT * FROM get_agent_onboarding();
```

**Returns (in priority order):**
1. 🎯 **NEXT TASK:** Template Cleanup - Next Task
2. 📊 **STATUS:** Beta Launch Status (99% ready, zero blockers)
3. ✅ **COMPLETED:** Auth System Complete
4. ✅ **COMPLETED:** Backend/GraphRAG Cleanup Complete
5. 📋 **PROTOCOL:** GraphRAG Usage Protocol
6. ... (all relevant docs)

**Translation:** "Templates are next. Beta is ready. Auth and GraphRAG are done. Read the protocol."

---

### **Query 2: What's my next task?**
```sql
SELECT * FROM get_next_task();
```

**Returns:**
- Title: "Template Cleanup - Next Task"
- File: `HANDOFF-TO-NEXT-AGENT-TEMPLATES.md`
- Time: 2 hours
- Priority: HIGH
- Component: templates

**Translation:** "Read this handoff doc, work on templates, should take ~2 hours."

---

### **Query 3: How did we get here?**
```sql
SELECT * FROM get_session_flow();
```

**Returns:**
- Auth System Complete → Template Cleanup (next task)
- GraphRAG Cleanup Complete → Template Cleanup (next task)
- GraphRAG Rebuild → GraphRAG Cleanup Complete (what led to what)

**Translation:** "Auth finished Oct 28. GraphRAG cleaned Oct 28. Templates are next."

---

## 📋 **Common Queries:**

### **Get All Protocols:**
```sql
SELECT * FROM get_protocols();
```

Returns:
- GraphRAG Usage Protocol
- Frontend Integration Guide  
- GraphRAG API Reference

### **Get Docs for Component:**
```sql
-- GraphRAG docs
SELECT * FROM get_component_docs('graphrag');

-- Auth docs
SELECT * FROM get_component_docs('auth');

-- Template docs
SELECT * FROM get_component_docs('templates');
```

### **Check Teaching Resources:**
```sql
-- Get all units
SELECT * FROM graphrag_resources 
WHERE resource_type = 'unit-plan';

-- Get Unit 2 lessons
SELECT * FROM get_unit_lessons('units/unit-2-decolonized-history.html');
```

---

## 🗂️ **Doc Categories:**

### **Current Docs (Read These):**
- **next_task** - What to work on now
- **status_check** - System status (beta readiness, blockers)
- **completion_report** - What was just finished
- **protocol** - How to use systems properly
- **architecture** - How things connect

### **Reference Docs (Read If Needed):**
- **project_overview** - Overall project description
- **api_reference** - API documentation

### **Historical Docs (Context Only):**
- **analysis** - Past analyses (e.g., identified GraphRAG bloat)
- **audit** - Past audits (may be superseded)

---

## 🔗 **Relationship Types:**

### **Session Flow:**
- `leads_to` - Previous work → Next task
- `resulted_in` - Implementation → Summary

### **Documentation:**
- `documented_by` - Implementation → Protocol
- `references` - Doc → API reference
- `depends_on` - Must read together

### **Status:**
- `informs` - Completion → Status update
- `tracks` - Roadmap → Task

### **Historical:**
- `led_to` - Analysis → Action taken
- `superseded_by` - Old audit → New implementation

---

## 📖 **Example Agent Session:**

### **Agent Starts:**
```sql
-- 1. Get overview
SELECT * FROM get_agent_onboarding();
-- Sees: Templates next, beta ready, auth/graphrag done

-- 2. Get next task details
SELECT * FROM get_next_task();
-- Sees: Read HANDOFF-TO-NEXT-AGENT-TEMPLATES.md

-- 3. Read that file
-- (use file read tool)

-- 4. Check related context
SELECT * FROM get_component_docs('templates');
-- Sees: Template audit exists

-- 5. Start work!
```

**Time to onboard:** ~2 minutes (vs 20 minutes reading docs manually)

---

## 🔧 **Maintaining This System:**

### **When You Complete Work:**

1. **Update handoff doc:**
```sql
UPDATE graphrag_resources 
SET archive_status = 'superseded'
WHERE file_path = 'HANDOFF-TO-NEXT-AGENT-TEMPLATES.md';
```

2. **Create new handoff (if needed):**
```sql
INSERT INTO graphrag_resources (file_path, resource_type, title, archive_status, metadata)
VALUES ('HANDOFF-TO-NEXT-AGENT-FEATURE-X.md', 'agent_doc', 'Feature X - Next Task', 'current', 
  '{"purpose": "next_task", "date": "2025-10-29", "component": "feature_x"}'::jsonb);
```

3. **Add relationship:**
```sql
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence)
VALUES ('YOUR-SIGNOFF.md', 'HANDOFF-TO-NEXT-AGENT-FEATURE-X.md', 'leads_to', 1.0);
```

### **Or Just Ask Next Agent to Update It!**
Most agents will scan filesystem and update GraphRAG as needed.

---

## 📊 **System Stats:**

```sql
-- Total resources
SELECT COUNT(*) FROM graphrag_resources;
-- Result: 141 (126 teaching + 15 agent docs)

-- Total relationships
SELECT COUNT(*) FROM graphrag_relationships;
-- Result: 51 (38 teaching + 13 agent)

-- Current agent docs
SELECT COUNT(*) FROM graphrag_resources 
WHERE resource_type = 'agent_doc' AND archive_status = 'current';
-- Result: 12

-- Database size
SELECT pg_size_pretty(pg_total_relation_size('graphrag_resources')) as resources,
       pg_size_pretty(pg_total_relation_size('graphrag_relationships')) as relationships;
-- Result: ~500 kB total (tiny!)
```

---

## ✅ **Success Criteria:**

Agent knowledge system is working if:
- ✅ New agents onboard in < 5 minutes
- ✅ "What should I work on?" has clear answer
- ✅ No reading 50 outdated docs
- ✅ Session flow is obvious (what led to what)
- ✅ Protocols are easy to find

---

## 🎯 **Quick Reference:**

| Query | Purpose | Returns |
|-------|---------|---------|
| `get_agent_onboarding()` | Overview | All current docs, prioritized |
| `get_next_task()` | What to work on | Single handoff doc |
| `get_session_flow()` | History | What led to what |
| `get_protocols()` | How-to guides | All protocols |
| `get_component_docs(name)` | Component info | Docs for specific component |

---

## 📚 **Files to Read:**

**First Time:**
1. This doc (`AGENT-KNOWLEDGE-SYSTEM.md`)
2. `AGENT-GRAPHRAG-PROTOCOL.md` - How to use GraphRAG
3. Output of `get_next_task()` - Your actual task

**As Needed:**
- `FRONTEND-BACKEND-INTEGRATION.md` - If touching frontend
- `GRAPHRAG-API-GUIDE.md` - If querying teaching resources
- Component-specific docs via `get_component_docs()`

---

## 🎉 **What This Gives You:**

### **Before:**
- 😰 100+ MD files in root
- 😰 Which are current? Which are outdated?
- 😰 What should I work on?
- 😰 20 minutes to figure out context

### **After:**
- ✅ 2-3 queries
- ✅ Clear "next task"
- ✅ Obvious what's done, what's not
- ✅ 2 minutes to onboard

---

## 💡 **Pro Tips:**

1. **Always start with `get_agent_onboarding()`** - It's your dashboard
2. **Check `get_session_flow()`** - Understand the story
3. **Use `get_component_docs()`** - Deep dive when needed
4. **Don't read historical docs** - Unless you need context
5. **Update when you finish** - Help the next agent!

---

**Created:** October 28, 2025  
**Agent:** Kaitiaki Aronui  
**Next:** Use this system to onboard faster!

🧺 ✨ 🧠

