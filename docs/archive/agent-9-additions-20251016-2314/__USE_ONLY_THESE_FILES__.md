# 🚨 MANDATORY: USE ONLY THESE FILES FOR COORDINATION!

**User Order:** "Stop creating new MD files! Use MCP and GraphRAG!"

---

## ✅ THE ONLY FILES AGENTS MAY UPDATE:

### **1. ACTIVE_QUESTIONS.md** - ALL coordination goes here
**Purpose:** Current priorities, decisions needed, agent status  
**Update:** Add your status at top, archive old content  
**DON'T:** Create separate coordination files!

### **2. progress-log.md** - ALL progress goes here  
**Purpose:** Daily achievements, milestones, completions  
**Update:** Add entry at top with date  
**DON'T:** Create separate progress reports!

### **3. README.md** - Project overview ONLY  
**Purpose:** What is Te Kete Ako, how to use  
**Update:** Only if core project info changes  
**DON'T:** Use for status updates!

---

## ✅ PROPER COMMUNICATION CHANNELS:

### **FOR COORDINATION:**
```bash
# Use the coordination tool:
python3 scripts/agent-coordinator.py --check-in agent-[ID]
python3 scripts/agent-coordinator.py --claim agent-[ID] "Task"
python3 scripts/agent-coordinator.py --update agent-[ID] "Progress"
```

### **FOR KNOWLEDGE SHARING:**
```sql
-- Use GraphRAG:
INSERT INTO resources (title, description, path, type, tags) VALUES (
  'Your accomplishment or learning',
  'Detailed description for future agents',
  '/path/to/work',
  'lesson',
  ARRAY['knowledge', 'agent-[ID]', 'date']
);
```

### **FOR QUICK UPDATES:**
- Update ACTIVE_QUESTIONS.md (the ONE file!)
- Post to GraphRAG
- Use coordination tool

---

## ❌ ABSOLUTELY FORBIDDEN:

**DO NOT CREATE:**
- ❌ New MD files for coordination
- ❌ New MD files for progress
- ❌ New MD files for status
- ❌ New MD files for reports
- ❌ New MD files for plans
- ❌ New MD files for hui/celebration
- ❌ New MD files for summaries
- ❌ ANY new MD files in root directory!

**Exception:** Only if creating actual content docs in `/docs/` folder for permanent reference

---

## ✅ WHAT TO DO INSTEAD:

| Want to... | DO THIS | DON'T DO THIS |
|------------|---------|---------------|
| Share progress | Update progress-log.md | Create AGENT_X_PROGRESS.md |
| Coordinate | Use agent-coordinator.py | Create COORDINATION_X.md |
| Log completion | Post to GraphRAG | Create TASK_COMPLETE.md |
| Share status | Update ACTIVE_QUESTIONS.md | Create STATUS_UPDATE.md |
| Document learning | Post to GraphRAG | Create LEARNING_SUMMARY.md |
| Plan work | Update ACTIVE_QUESTIONS.md | Create WORK_PLAN.md |
| Celebrate | Post to GraphRAG | Create HUI_CELEBRATION.md |

---

## 🎯 ENFORCEMENT:

**This is MANDATORY, not optional!**

**All agents:**
- Read this file FIRST
- Follow the protocols
- Use coordination tool
- Use GraphRAG
- Update master files ONLY
- **NO new MD files!**

**If an agent creates new MD files:** They're not following protocol!

---

**Created:** Oct 16, 2025  
**Status:** MANDATORY FOR ALL AGENTS  
**Enforcement:** Immediate

**FOLLOW THIS OR CREATE DIVERGENCE!** 🚨

— Agent-9
