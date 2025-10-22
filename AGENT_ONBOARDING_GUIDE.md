# 🚀 Agent Onboarding Guide

**Last Updated:** October 22, 2025  
**Purpose:** Step-by-step guide to join the Te Kete Ako agent coordination system

---

## 📚 **Table of Contents**

1. [Prerequisites](#prerequisites)
2. [Step 1: Register Your Agent](#step-1-register-your-agent)
3. [Step 2: Understand the System](#step-2-understand-the-system)
4. [Step 3: Query Existing Work](#step-3-query-existing-work)
5. [Step 4: Claim Your First Task](#step-4-claim-your-first-task)
6. [Step 5: Update Your Status](#step-5-update-your-status)
7. [Step 6: Document Your Work](#step-6-document-your-work)
8. [Ongoing Coordination](#ongoing-coordination)
9. [Agent Roles Available](#agent-roles-available)
10. [Troubleshooting](#troubleshooting)

---

## ✅ **Prerequisites**

Before joining the system, ensure you have:

- [x] Access to Supabase MCP (project: nlgldaqtubrlcqddppbq)
- [x] Read `START_HERE_NEW_AGENTS.md` (60 seconds)
- [x] Read `ACTIVE_QUESTIONS.md` (current priorities)
- [x] Understand GraphRAG-first workflow
- [x] Know the terminal command bug (use MCP only!)

---

## 🎯 **Step 1: Register Your Agent**

### **1.1 Choose Your Agent ID**

Pick a unique identifier:
- Format: `agent-{role}-{date}` or `{unique-name}`
- Examples: `agent-9a4dd0d0`, `assistant-oct22-sprint2`, `kaitiaki-aronui-v3`

### **1.2 Choose Your Agent Name**

Pick a descriptive Māori or English name:
- **Māori examples:** Kaitiaki Aronui, Kaiārahi Mātauranga, Kaituhi Ako
- **English examples:** Sprint Deployer, Quality Validator, Content Creator

### **1.3 Register in agent_status Table**

```sql
-- Register yourself
INSERT INTO agent_status (
  agent_id, 
  agent_name, 
  status, 
  current_task,
  files_editing,
  last_heartbeat
) VALUES (
  'your-unique-agent-id',           -- e.g., 'agent-discovery-specialist'
  'Your Descriptive Agent Name',    -- e.g., 'Kaiārahi Discovery (Discovery Specialist)'
  'idle',                           -- Start as 'idle'
  NULL,                             -- No task yet
  ARRAY[]::text[],                  -- No files yet
  NOW()                             -- Current timestamp
);

-- Verify registration
SELECT * FROM agent_status WHERE agent_id = 'your-unique-agent-id';
```

### **1.4 Register in agent_coordination Table**

```sql
-- Create your coordination record
INSERT INTO agent_coordination (
  agent_name,
  task_claimed,
  status,
  started_at,
  files_modified,
  key_decisions
) VALUES (
  'Your Agent Name',
  'Onboarding - Getting Started',
  'planning',
  NOW(),
  ARRAY[]::text[],
  '{"role": "your_role", "specialty": "your_specialty"}'::jsonb
);
```

---

## 📖 **Step 2: Understand the System**

### **2.1 The Three-Layer Architecture**

**Layer 1: GraphRAG Knowledge Base**
- `agent_knowledge` - Discoveries & learnings (531 entries)
- `agent_coordination` - Task tracking & handoffs (33 records)
- `agent_status` - Real-time "who's doing what" (12 active)
- `agent_messages` - Urgent communications (130 messages)
- `task_board` - Centralized task queue (4 active)

**Layer 2: ACTIVE_QUESTIONS.md**
- Single coordination markdown file
- Updated by all agents in real-time
- Contains priorities, achievements, handoffs

**Layer 3: GraphRAG Resources**
- `graphrag_resources` - 17,379 educational resources
- `graphrag_relationships` - 242,217 connections
- Core platform intelligence

### **2.2 Coordination Rules**

✅ **DO:**
- Query GraphRAG BEFORE building anything
- Update `agent_status` heartbeat every 30 minutes
- Add discoveries to `agent_knowledge`
- Update `ACTIVE_QUESTIONS.md` with major progress
- Use MCP Supabase exclusively (terminal hangs!)

❌ **DON'T:**
- Create new coordination MD files
- Duplicate work others are doing
- Use `run_terminal_cmd` (it hangs forever!)
- Skip querying GraphRAG for existing work

### **2.3 The Critical Bug**

⚠️ **TERMINAL COMMANDS HANG FOREVER!**
- ❌ Never use: `run_terminal_cmd`
- ✅ Always use: `mcp_supabase_execute_sql`
- ✅ Works perfectly for all data operations

---

## 🔍 **Step 3: Query Existing Work**

### **3.1 Check Active Agents**

```sql
-- Who is working right now?
SELECT 
  agent_id,
  agent_name,
  status,
  current_task,
  last_heartbeat,
  EXTRACT(EPOCH FROM (NOW() - last_heartbeat))/60 as minutes_idle
FROM agent_status
WHERE last_heartbeat > NOW() - INTERVAL '2 hours'
ORDER BY last_heartbeat DESC;
```

### **3.2 Check Recent Discoveries**

```sql
-- What has been discovered in the last 24 hours?
SELECT 
  source_name,
  doc_type,
  key_insights[1:3] as top_insights,
  agents_involved,
  created_at
FROM agent_knowledge
WHERE created_at > NOW() - INTERVAL '24 hours'
ORDER BY created_at DESC;
```

### **3.3 Check Available Tasks**

```sql
-- What tasks are unclaimed?
SELECT 
  id,
  task_name,
  priority,
  description,
  created_at
FROM task_board
WHERE status = 'available'
ORDER BY 
  CASE priority 
    WHEN 'urgent' THEN 1 
    WHEN 'high' THEN 2 
    WHEN 'medium' THEN 3 
    ELSE 4 
  END,
  created_at;
```

### **3.4 Check Current Priorities**

```sql
-- What are the top priorities?
SELECT 
  task_name,
  priority,
  status,
  claimed_by
FROM task_board
WHERE status IN ('available', 'claimed')
ORDER BY 
  CASE priority 
    WHEN 'urgent' THEN 1 
    WHEN 'high' THEN 2 
    WHEN 'medium' THEN 3 
    ELSE 4 
  END
LIMIT 5;
```

---

## 🎯 **Step 4: Claim Your First Task**

### **4.1 Choose a Task**

Based on your specialty:
- **Cultural:** Cultural integration, te reo, whakataukī
- **Technical:** GraphRAG, components, infrastructure
- **Content:** Lessons, handouts, quality validation
- **Design:** CSS, UI/UX, responsiveness
- **Data:** Analytics, reporting, intelligence

### **4.2 Claim the Task**

```sql
-- Claim a task from task_board
UPDATE task_board 
SET 
  status = 'claimed',
  claimed_by = 'your-agent-id',
  claimed_at = NOW()
WHERE id = 'task-uuid-here'
RETURNING task_name, priority;
```

### **4.3 Update Your Status**

```sql
-- Update agent_status to show you're working
UPDATE agent_status 
SET 
  status = 'working',
  current_task = 'Task Name from task_board',
  started_at = NOW(),
  last_heartbeat = NOW()
WHERE agent_id = 'your-agent-id';
```

### **4.4 Add to agent_coordination**

```sql
-- Update your coordination record
UPDATE agent_coordination
SET
  task_claimed = 'Specific Task Description',
  status = 'in_progress',
  started_at = NOW(),
  key_decisions = jsonb_build_object(
    'approach', 'your_approach',
    'estimated_time', 'X hours',
    'dependencies', ARRAY[]::text[]
  )
WHERE agent_name = 'Your Agent Name'
  AND completed_at IS NULL;
```

---

## 🔄 **Step 5: Update Your Status**

### **5.1 Heartbeat Updates (Every 30 Minutes)**

```sql
-- Update heartbeat to show you're still alive
UPDATE agent_status
SET 
  last_heartbeat = NOW(),
  files_editing = ARRAY['/public/file1.html', '/public/file2.html']
WHERE agent_id = 'your-agent-id';
```

### **5.2 Progress Updates**

```sql
-- Add progress notes to agent_coordination
UPDATE agent_coordination
SET
  key_decisions = key_decisions || jsonb_build_object(
    'progress_' || to_char(NOW(), 'HH24MI'), 
    'Description of what you just accomplished'
  ),
  updated_at = NOW()
WHERE agent_name = 'Your Agent Name'
  AND completed_at IS NULL;
```

### **5.3 File Tracking**

```sql
-- Track which files you're editing
UPDATE agent_coordination
SET
  files_modified = array_append(
    COALESCE(files_modified, ARRAY[]::text[]),
    '/public/new-file.html'
  ),
  updated_at = NOW()
WHERE agent_name = 'Your Agent Name'
  AND completed_at IS NULL;
```

---

## 📝 **Step 6: Document Your Work**

### **6.1 Add Discovery to agent_knowledge**

```sql
-- Document what you learned/built
INSERT INTO agent_knowledge (
  source_type,
  source_name,
  doc_type,
  key_insights,
  technical_details,
  agents_involved
) VALUES (
  'synthesis',                           -- or 'session', 'discovery'
  'Your Discovery Title',                -- Clear, searchable name
  'deployment_success',                  -- See doc_type list below
  ARRAY[
    'Key insight 1: What you discovered',
    'Key insight 2: Why it matters',
    'Key insight 3: What changed'
  ],
  jsonb_build_object(                    -- Technical implementation details
    'files_created', ARRAY['/public/file1.html'],
    'approach', 'Description of your approach',
    'challenges', 'Any blockers you hit',
    'solutions', 'How you solved them'
  ),
  ARRAY['your-agent-id']                 -- Your agent ID
);
```

**Common doc_types:**
- `deployment_success` - Feature/component deployed
- `code-change` - Code modifications made
- `discovery` - New insight or pattern found
- `bug_fix` - Issue resolved
- `cultural_transformation` - Cultural integration work
- `milestone` - Major achievement
- `reference_guide` - Reusable patterns/solutions
- `coordination_log` - Agent coordination notes

### **6.2 Update ACTIVE_QUESTIONS.md**

For major achievements, update the coordination file:

```markdown
## 🎊 **LATEST: Your Achievement Title** (Oct 22, 2025)

**Agent:** Your Agent Name  
**Status:** ✅ COMPLETE

### **Achievements:**
- ✅ Thing 1 accomplished
- ✅ Thing 2 built
- ✅ Thing 3 deployed

### **Key Discoveries:**
1. Discovery 1
2. Discovery 2
3. Discovery 3

### **Files Modified:**
- `/public/file1.html`
- `/public/file2.html`

### **Handoff to Next Agent:**
- Ready for X to do Y
- Blockers: None
- Documentation: See agent_knowledge entry #XXX
```

### **6.3 Complete Your Task**

```sql
-- Mark task as done in task_board
UPDATE task_board
SET
  status = 'done',
  completed_at = NOW()
WHERE id = 'your-task-id';

-- Mark yourself as idle
UPDATE agent_status
SET
  status = 'idle',
  current_task = NULL,
  files_editing = ARRAY[]::text[]
WHERE agent_id = 'your-agent-id';

-- Complete coordination record
UPDATE agent_coordination
SET
  status = 'completed',
  completed_at = NOW(),
  next_agent_handoff = 'Optional: Who should pick this up next'
WHERE agent_name = 'Your Agent Name'
  AND completed_at IS NULL;
```

---

## 🔁 **Ongoing Coordination**

### **Daily Workflow**

**Morning:**
```sql
-- 1. Check what happened overnight
SELECT source_name, key_insights[1] 
FROM agent_knowledge 
WHERE created_at > NOW() - INTERVAL '12 hours'
ORDER BY created_at DESC;

-- 2. Check active agents
SELECT agent_name, current_task 
FROM agent_status 
WHERE status = 'working';

-- 3. Find available tasks
SELECT task_name, priority 
FROM task_board 
WHERE status = 'available'
ORDER BY priority;
```

**Every 30 Minutes:**
```sql
-- Update heartbeat
UPDATE agent_status 
SET last_heartbeat = NOW() 
WHERE agent_id = 'your-agent-id';
```

**Evening:**
```sql
-- Document your discoveries
INSERT INTO agent_knowledge (...) VALUES (...);

-- Mark yourself idle
UPDATE agent_status SET status = 'idle' WHERE agent_id = 'your-agent-id';

-- Update ACTIVE_QUESTIONS.md with summary
```

### **Communication**

**Urgent Messages:**
```sql
-- Send urgent message to another agent
INSERT INTO agent_messages (
  from_agent,
  to_agent,
  message,
  priority
) VALUES (
  'your-agent-id',
  'target-agent-id',  -- or NULL for broadcast
  'Urgent: I noticed X. Can you check Y?',
  'urgent'
);

-- Check your messages
SELECT * FROM agent_messages 
WHERE to_agent = 'your-agent-id' AND read = false
ORDER BY created_at DESC;
```

---

## 🎭 **Agent Roles Available**

Choose a role that fits your specialty:

| Role | Māori Name | Focus |
|------|------------|-------|
| **Strategic Overseer** | Kaitiaki Aronui | Overall platform strategy, priorities |
| **Cultural Validator** | Kaitiaki Ahurea | Te Ao Māori integration, cultural accuracy |
| **Quality Validator** | Kaiārahi Kounga | Content quality, standards enforcement |
| **Content Creator** | Kaituhi Ako | Lessons, handouts, teaching resources |
| **Curriculum Agent** | Kaihanga Rauemi | Subject organization, year levels |
| **Pathways Agent** | Kaiārahi Tūhono | Learning progressions, prerequisites |
| **Styling Agent** | Kaiako CSS | CSS, design system, UI/UX |
| **Data Analyst** | Kaitātari Raraunga | Analytics, reporting, intelligence |
| **Documentation** | Kaituhi Tuhinga | Guides, documentation, knowledge |
| **Auth & Security** | Kaitiaki Whakamana | Authentication, security, access |
| **Component Builder** | Kaiwhakawhanake | Components, widgets, interactions |
| **GraphRAG Specialist** | Kaiārahi GraphRAG | Knowledge graph, relationships |

**Current Active Agents:**
- Kaitiaki Aronui (Strategic Overseer)
- Kaihanga Rauemi (Curriculum Agent)
- Kaiārahi Tūhono (Pathways Agent)
- Kaitiaki Ahurea (Cultural Validator)
- Kaiārahi Kounga (Quality Validator)
- Kaituhi Ako (Content Creator)
- Kaiako CSS (Styling Agent)
- Kaitātari Raraunga (Data Analyst)
- Kaituhi Tuhinga (Documentation)
- Kaitiaki Whakamana (Auth & Security)

**Roles Needed:**
- Component Builder
- Mobile Specialist
- Accessibility Specialist
- Performance Optimizer

---

## 🔧 **Troubleshooting**

### **Issue: "Agent ID already exists"**

```sql
-- Check if your ID is taken
SELECT * FROM agent_status WHERE agent_id = 'your-agent-id';

-- Choose a different ID or update existing record
UPDATE agent_status 
SET agent_name = 'Your New Name', last_heartbeat = NOW()
WHERE agent_id = 'your-agent-id';
```

### **Issue: "Task already claimed"**

```sql
-- Check who claimed it
SELECT claimed_by, claimed_at FROM task_board WHERE id = 'task-id';

-- Find other available tasks
SELECT * FROM task_board WHERE status = 'available';
```

### **Issue: "Terminal commands hanging"**

This is expected! See `.cursorrules`:
- ❌ Never use `run_terminal_cmd`
- ✅ Always use MCP Supabase queries

### **Issue: "Can't find recent work"**

```sql
-- Query by time period
SELECT source_name, created_at 
FROM agent_knowledge 
WHERE created_at > '2025-10-22'::date
ORDER BY created_at DESC;

-- Query by keyword
SELECT source_name FROM agent_knowledge 
WHERE source_name ILIKE '%keyword%';
```

### **Issue: "Don't know what to work on"**

1. Check `ACTIVE_QUESTIONS.md` - Top priorities
2. Query `task_board` - Available tasks
3. Query `agent_knowledge` - Recent discoveries
4. Ask in `agent_messages` - Broadcast a question

---

## 📊 **System Stats**

**Current State (Oct 22, 2025):**
- **Agents Registered:** 12 active
- **Knowledge Entries:** 531 discoveries
- **Tasks Completed:** 29 (88% success rate)
- **Resources in GraphRAG:** 17,379
- **Relationships Mapped:** 242,217
- **Platform Readiness:** 85-90% production-ready

---

## ✅ **Onboarding Checklist**

Complete this checklist:

- [ ] Read `START_HERE_NEW_AGENTS.md`
- [ ] Read `ACTIVE_QUESTIONS.md`
- [ ] Choose agent ID and name
- [ ] Register in `agent_status` table
- [ ] Register in `agent_coordination` table
- [ ] Query recent discoveries (last 24 hours)
- [ ] Check active agents (avoid conflicts)
- [ ] Find and claim first task
- [ ] Update heartbeat
- [ ] Complete first task
- [ ] Document discovery in `agent_knowledge`
- [ ] Update `ACTIVE_QUESTIONS.md`
- [ ] Mark task complete

---

## 🚀 **Welcome to the Team!**

You're now part of a **world-class multi-agent coordination system**. 

**Key Principles:**
1. 🧠 **Query first, build second** - GraphRAG is your institutional memory
2. 🤝 **Coordinate constantly** - Update heartbeat every 30 min
3. 📝 **Document everything** - Future agents will thank you
4. 🌿 **Cultural excellence** - Te Ao Māori integration is the standard
5. 💎 **Quality over quantity** - Build for real humans, not metrics

**Kia kaha! Let's build something extraordinary! 🚀**

---

**Next:** Read `AGENT_QUERY_GUIDE.md` for advanced query patterns

