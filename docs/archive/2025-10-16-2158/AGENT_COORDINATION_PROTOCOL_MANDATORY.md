# 🚨 MANDATORY AGENT COORDINATION PROTOCOL

**Date:** October 16, 2025  
**Priority:** 🔴 CRITICAL - MUST FOLLOW  
**Purpose:** STOP agent divergence permanently  
**Status:** Active enforcement

---

## ⚠️ **THE PROBLEM (USER-IDENTIFIED):**

### **User Feedback:**
> "We continually diverge. It's the only reason our progress isn't 
> flowing nicely. Agents need to ALL be using MCP and GraphRAG and 
> develop another tool to always be working together."

### **Evidence of Divergence:**
- 25 CSS files created by different agents (same purpose!)
- Duplicate navigation systems (3 versions!)
- Demo vs production confusion
- Agents working on same tasks independently
- **Result: Inefficient, conflicting, wasteful**

---

## ✅ **THE SOLUTION: REAL-TIME COORDINATION SYSTEM**

### **NEW DATABASE TABLES (Just Created):**

**1. `agent_coordination`** - Real-time agent status
**2. `agent_tasks`** - Claimable task system  
**3. `agent_messages`** - Agent-to-agent communication
**4. `file_locks`** - Prevent simultaneous edits

**Plus 3 Views:**
- `active_agent_sessions` - Who's working on what NOW
- `available_tasks_view` - What tasks can be claimed
- `recent_agent_messages` - Latest communications

---

## 🚨 **MANDATORY PROTOCOL (ALL AGENTS MUST FOLLOW):**

### **BEFORE Starting ANY Work:**

#### **Step 1: Check Who's Working (MANDATORY)**
```sql
-- Query active agent sessions
SELECT * FROM active_agent_sessions;
```

**Purpose:** See what all other agents are doing RIGHT NOW

#### **Step 2: Register Your Session (MANDATORY)**
```sql
-- Insert or update your status
INSERT INTO agent_coordination (
  agent_id, 
  agent_name, 
  status, 
  current_task, 
  task_started_at,
  estimated_completion,
  files_being_edited
) VALUES (
  'agent-5',
  'Kaiārahi Ako',
  'working',
  'Enriching sidebars with external resources',
  NOW(),
  NOW() + INTERVAL '2 hours',
  ARRAY['/public/units/lessons/unit-3-lesson-3.html']
)
ON CONFLICT (agent_id) DO UPDATE SET
  status = EXCLUDED.status,
  current_task = EXCLUDED.current_task,
  task_started_at = EXCLUDED.task_started_at,
  files_being_edited = EXCLUDED.files_being_edited,
  last_heartbeat = NOW();
```

**Purpose:** Let others know you're working and on what

#### **Step 3: Check Available Tasks (MANDATORY)**
```sql
-- See what tasks are available
SELECT * FROM available_tasks_view;
```

**Purpose:** See if someone already created a task for what you want to do

#### **Step 4: Claim Task or Create New (MANDATORY)**
```sql
-- If task exists, claim it
UPDATE agent_tasks 
SET status = 'claimed',
    claimed_by = 'agent-5',
    claimed_at = NOW()
WHERE task_name = 'Sidebar enrichment'
  AND status = 'available';

-- If no task exists, create and claim it
INSERT INTO agent_tasks (
  task_name,
  task_description,
  priority,
  status,
  claimed_by,
  estimated_hours,
  files_affected,
  tags
) VALUES (
  'Sidebar enrichment',
  'Add external resources to 19 remaining lesson sidebars',
  'medium',
  'claimed',
  'agent-5',
  3,
  ARRAY['/public/units/lessons/unit-3-*.html'],
  ARRAY['content', 'sidebars', 'external-resources']
);
```

**Purpose:** Prevent duplicate work

---

### **DURING Work:**

#### **Heartbeat Every 10 Minutes (MANDATORY)**
```sql
-- Update last_heartbeat
UPDATE agent_coordination
SET last_heartbeat = NOW(),
    updated_at = NOW()
WHERE agent_id = 'agent-5';
```

**Purpose:** Show you're still active

#### **Lock Files You're Editing (RECOMMENDED)**
```sql
-- Lock file before editing
INSERT INTO file_locks (file_path, locked_by, purpose)
VALUES ('/public/index.html', 'agent-5', 'Adding games section')
ON CONFLICT (file_path) DO NOTHING;

-- Check if file locked by someone else
SELECT * FROM file_locks 
WHERE file_path = '/public/index.html'
  AND locked_by != 'agent-5'
  AND lock_expires_at > NOW();
```

**Purpose:** Prevent simultaneous edits

#### **Log Progress in Resources Table (CONTINUE)**
```sql
-- Continue using resources table for knowledge graph
INSERT INTO resources (title, description, ...) 
VALUES (...);
```

**Purpose:** Build knowledge graph

---

### **AFTER Work:**

#### **Update Status (MANDATORY)**
```sql
-- Mark task complete
UPDATE agent_tasks
SET status = 'completed',
    completed_at = NOW(),
    actual_hours = EXTRACT(EPOCH FROM (NOW() - started_at)) / 3600
WHERE id = '[task-uuid]';

-- Update agent status to idle
UPDATE agent_coordination
SET status = 'idle',
    current_task = NULL,
    task_started_at = NULL,
    files_being_edited = NULL,
    last_heartbeat = NOW()
WHERE agent_id = 'agent-5';
```

**Purpose:** Free up for next task

#### **Release File Locks (MANDATORY)**
```sql
-- Release all your locks
DELETE FROM file_locks
WHERE locked_by = 'agent-5';
```

**Purpose:** Let others edit files

---

## 🛠️ **COORDINATION TOOL CREATION:**

### **Creating Helper Functions:**

<function_calls>
<invoke name="mcp_supabase_apply_migration">
<parameter name="name">agent_coordination_helper_functions
