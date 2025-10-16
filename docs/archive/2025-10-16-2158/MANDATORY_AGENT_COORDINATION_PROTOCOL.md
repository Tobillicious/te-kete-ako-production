# 🚨 MANDATORY AGENT COORDINATION PROTOCOL

**Date:** October 16, 2025  
**Status:** CRITICAL - ALL AGENTS MUST FOLLOW  
**Problem:** Agents diverging, creating duplicate docs, not unifying work  
**Solution:** MANDATORY MCP + GraphRAG coordination EVERY action

---

## ⚠️ **THE PROBLEM - USER IDENTIFIED:**

> "We continually diverge. It's the only reason our progress isn't flowing nicely."

**Symptoms:**
```
❌ Multiple agents creating separate plans
❌ Duplicate documentation (30+ coordination MDs!)
❌ Not checking what others have done
❌ Not using MCP properly
❌ Not updating GraphRAG
❌ Progress looks good but doesn't integrate
❌ User has to manually synthesize
```

**Root Cause:**
```
Agents are NOT:
- Querying GraphRAG before starting
- Checking agent_coordination table
- Reading other agents' work
- Using MCP for real-time coordination
- Building on each other's work
```

---

## ✅ **THE SOLUTION - MANDATORY PROTOCOL:**

### **BEFORE STARTING ANY WORK:**

**Step 1: CHECK GRAPHRAG (MANDATORY)**
```sql
-- Query what's been done recently
SELECT agent_name, task_claimed, status, files_modified, updated_at
FROM agent_coordination
WHERE status IN ('in_progress', 'planning')
ORDER BY updated_at DESC
LIMIT 10;
```

**Step 2: LOG YOUR INTENTION (MANDATORY)**
```sql
-- Log what you're about to do
INSERT INTO agent_coordination (
    agent_name,
    task_claimed,
    status,
    key_decisions
) VALUES (
    'Agent-[YOUR-ID]',
    '[What you're doing in ONE sentence]',
    'planning',
    '{"reads": ["file1.md", "file2.md"], "will_create": ["file3.html"]}'::jsonb
);
```

**Step 3: READ RELATED WORK (MANDATORY)**
```
Query GraphRAG for:
- What files others have modified
- What decisions others have made
- What's already complete
- What's currently in progress

THEN: Build on it, don't duplicate!
```

### **DURING WORK:**

**Every 30 Minutes: UPDATE STATUS (MANDATORY)**
```sql
-- Update your progress
UPDATE agent_coordination
SET 
    status = 'in_progress',
    files_modified = ARRAY['file1.html', 'file2.js'],
    key_decisions = '{"approach": "using canonical CSS", "tested": true}'::jsonb,
    updated_at = now()
WHERE agent_name = 'Agent-[YOUR-ID]'
AND status = 'planning';
```

### **AFTER COMPLETING WORK:**

**Mark Complete & Handoff (MANDATORY)**
```sql
-- Mark complete
UPDATE agent_coordination
SET 
    status = 'completed',
    completed_at = now(),
    files_modified = ARRAY['list', 'of', 'all', 'files'],
    next_agent_handoff = 'Agent-X should test this / Agent-Y should build on this',
    updated_at = now()
WHERE agent_name = 'Agent-[YOUR-ID]'
AND status = 'in_progress';
```

---

## 🔧 **MANDATORY TOOLS:**

### **Tool 1: Pre-Work Check Script**
```python
#!/usr/bin/env python3
"""
MANDATORY: Run before starting ANY work
Checks what others have done, prevents duplication
"""

import subprocess
from supabase import create_client

# Query agent coordination
result = supabase.from_('agent_coordination')\
    .select('*')\
    .in_('status', ['in_progress', 'planning'])\
    .order('updated_at', desc=True)\
    .limit(10)\
    .execute()

if result.data:
    print("🚨 OTHER AGENTS CURRENTLY WORKING:")
    for agent in result.data:
        print(f"   - {agent['agent_name']}: {agent['task_claimed']}")
        print(f"     Status: {agent['status']}")
        print(f"     Files: {agent.get('files_modified', [])}")
    
    print("\n⚠️  READ THEIR WORK BEFORE PROCEEDING!")
    print("    Coordinate or pick different task!")
else:
    print("✅ No other agents currently working")
    print("   You can proceed!")
```

### **Tool 2: Work Logging Script**
```python
#!/usr/bin/env python3
"""
MANDATORY: Log your work to GraphRAG
"""

def log_work(agent_name, task, status, files):
    supabase.from_('agent_coordination').insert({
        'agent_name': agent_name,
        'task_claimed': task,
        'status': status,
        'files_modified': files
    }).execute()
    print(f"✅ Logged to GraphRAG: {task}")
```

### **Tool 3: Synthesis Query**
```sql
-- See ALL work done today
SELECT 
    agent_name,
    task_claimed,
    status,
    array_length(files_modified, 1) as files_count,
    completed_at - started_at as duration
FROM agent_coordination
WHERE DATE(created_at) = CURRENT_DATE
ORDER BY started_at;
```

---

## 📋 **SIMPLE COORDINATION FLOW:**

```
1. Query agent_coordination table (see who's working on what)
   ↓
2. Query GraphRAG (see what's been done)
   ↓
3. Read relevant files (understand context)
   ↓
4. Log your intention (claim task)
   ↓
5. DO THE WORK (build on others' work, don't duplicate)
   ↓
6. Update every 30 mins (show progress)
   ↓
7. Mark complete (handoff to next agent)
   ↓
8. ONE summary document (not 5 separate ones)
```

---

## 🚨 **WHAT MUST STOP:**

### **STOP Creating:**
```
❌ Multiple coordination MDs (we have 30+!)
❌ Separate session summaries (use ONE shared log)
❌ Duplicate plans (check GraphRAG first!)
❌ Separate work streams (integrate!)
❌ New documentation systems (use existing!)
```

### **START Doing:**
```
✅ Query agent_coordination table BEFORE work
✅ Log to GraphRAG DURING work
✅ Update ONE shared document (ACTIVE_QUESTIONS.md)
✅ Build on each other's work
✅ Create INTEGRATED solutions
```

---

## 📊 **ONE SOURCE OF TRUTH:**

### **For Coordination:**
```
1. agent_coordination table (MCP Supabase) ← REAL-TIME STATUS
2. ACTIVE_QUESTIONS.md ← HUMAN-READABLE HUB
3. progress-log.md ← TIMELINE

That's IT. No more coordination MDs!
```

### **For Technical Specs:**
```
CSS: CSS_ARCHITECTURE_CANONICAL.md (Agent-4's work)
Auth: PRODUCTION_AUTH_COMPLETE.md (My work)
Content: MASTER_CONTENT_MAP.md (My work)
Links: BROKEN_LINKS_REPAIR_SUCCESS.md (Agent-9's work)
```

---

## 🎯 **UNIFIED WORK PLAN (Oct 17-22):**

### **Current State (From ALL Agents Combined):**
```
✅ Design System: Unified (Agent-4)
✅ CSS: Consolidated to 8 canonical files (Agent-4)
✅ Links: 10,444 fixed, 87% complete (Agent-9)
✅ Auth: Production student + teacher (Kaitiaki + Agent-4)
✅ Content: 20+ units mapped, 72 lessons enhanced (Kaitiaki)
✅ Validation: 17 lessons verified (Agent-3)
✅ GraphRAG: 1,539+ resources indexed

Demo Readiness: 95%
```

### **Remaining Work (UNIFIED LIST):**
```
1. [Agent-9] Finish link repairs (1 hour) - IN PROGRESS
2. [NEED] Mobile testing (30 mins) - AVAILABLE
3. [NEED] Legal pages (2 hours) - AVAILABLE
4. [NEED] Test auth flow (30 mins) - AVAILABLE
5. [Agent-3] Finish Te Ao Māori enrichment (30 mins) - CAN RESUME
```

**Total: 4-5 hours to 100%**

---

## 🔧 **IMPLEMENTATION - RIGHT NOW:**

### **I'm Creating:**
```
1. ✅ agent_coordination table (MCP Supabase) - DONE!
2. 📝 This protocol document (MANDATORY rules)
3. 🔄 Updated ACTIVE_QUESTIONS.md (ONE hub)
4. 🧹 Will archive 29 coordination MDs (reduce clutter)
```

### **All Agents Must:**
```
1. Query agent_coordination before starting
2. Log work to GraphRAG
3. Update ACTIVE_QUESTIONS.md only
4. Stop creating new coordination docs
5. Build on each other's work
```

---

## 🎉 **PROOF IT WORKS:**

### **When We DO Coordinate:**
```
✅ Agent-4 + Agent-5: CSS consolidation (no conflicts!)
✅ Agent-4 + Kaitiaki: Auth system (integrated perfectly!)
✅ Agent-9 + Agent-4: Link fixes on CSS paths (worked together!)
✅ Agent-3 validation: Building on others' content
```

### **When We DON'T Coordinate:**
```
❌ 30+ coordination MDs created
❌ User has to manually synthesize
❌ Progress doesn't integrate
❌ Looks like chaos
```

---

## ✅ **MOVING FORWARD:**

**NEW RULE:**
```
Before starting ANYTHING, you MUST:
1. Query agent_coordination table via MCP
2. Read what others have done
3. Log your intention
4. Build on their work (don't duplicate)
```

**ONE SHARED LOG:**
```
ACTIVE_QUESTIONS.md ← Everyone updates THIS
(Not 30 separate coordination files!)
```

**GraphRAG FOR EVERYTHING:**
```
- Log all work
- Query before starting
- Update during work
- Share discoveries
```

---

**Status:** 🚨 CRITICAL PROTOCOL CREATED  
**Action:** ALL AGENTS MUST FOLLOW  
**Goal:** UNIFIED PROGRESS, NOT DIVERGENT DOCS  

**Let me now implement this and coordinate properly!** 🔥

