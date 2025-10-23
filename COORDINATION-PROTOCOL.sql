-- 🤝 REAL-TIME AGENT COORDINATION PROTOCOL
-- Use these queries to coordinate work between Cursor AI Agent & Claude Code

-- ========================================
-- 1️⃣ REGISTER YOUR PRESENCE (Claude Code: Run this first!)
-- ========================================
INSERT INTO agent_status (
  agent_id,
  agent_name,
  status,
  current_task,
  started_at,
  last_heartbeat
) VALUES (
  'claude-code-41259',  -- Your PID!
  'Claude Code',
  'working',
  'Running initial verification queries',  -- Update this to what you're doing
  NOW(),
  NOW()
)
ON CONFLICT (agent_id) 
DO UPDATE SET 
  status = 'working',
  current_task = 'Running initial verification queries',
  last_heartbeat = NOW()
RETURNING agent_id, agent_name, status, current_task, last_heartbeat;

-- ========================================
-- 2️⃣ CHECK WHO ELSE IS ACTIVE (Both agents: Run anytime)
-- ========================================
SELECT 
  agent_id,
  agent_name,
  status,
  current_task,
  files_editing,
  started_at,
  last_heartbeat,
  NOW() - last_heartbeat as idle_time
FROM agent_status 
WHERE last_heartbeat > NOW() - INTERVAL '10 minutes'
ORDER BY last_heartbeat DESC;

-- ========================================
-- 3️⃣ SEND A MESSAGE (Both agents: Use to communicate)
-- ========================================
-- Example from Claude Code to Cursor Agent:
INSERT INTO agent_messages (from_agent, to_agent, message, priority)
VALUES (
  'Claude Code',
  'Cursor AI Agent',
  'Started working! Running verification queries from CLAUDE-CODE-QUICKSTART.sql',
  'medium'
)
RETURNING id, message, created_at;

-- Example from Cursor Agent to Claude Code:
INSERT INTO agent_messages (from_agent, to_agent, message, priority)
VALUES (
  'Cursor AI Agent',
  'Claude Code',
  'Welcome! I can help with GraphRAG queries or task coordination. What are you working on?',
  'medium'
)
RETURNING id, message, created_at;

-- ========================================
-- 4️⃣ READ YOUR MESSAGES (Both agents: Check frequently)
-- ========================================
SELECT 
  id,
  from_agent,
  message,
  priority,
  created_at,
  NOW() - created_at as age
FROM agent_messages 
WHERE to_agent = 'Claude Code'  -- Or 'Cursor AI Agent'
  AND read = false
  AND created_at > NOW() - INTERVAL '1 hour'
ORDER BY priority ASC, created_at DESC;

-- Mark message as read:
-- UPDATE agent_messages SET read = true WHERE id = 'message-id';

-- ========================================
-- 5️⃣ UPDATE YOUR STATUS (Both agents: Run every 2-5 minutes)
-- ========================================
-- When starting a new task:
UPDATE agent_status 
SET status = 'working',
    current_task = 'Fixing orphaned pages in generated-resources-alpha',
    files_editing = ARRAY['/public/generated-resources-alpha/handouts/example.html'],
    last_heartbeat = NOW()
WHERE agent_id = 'claude-code-41259';  -- Or 'cursor-agent'

-- When idle/waiting:
UPDATE agent_status 
SET status = 'idle',
    current_task = NULL,
    files_editing = NULL,
    last_heartbeat = NOW()
WHERE agent_id = 'claude-code-41259';

-- When blocked:
UPDATE agent_status 
SET status = 'blocked',
    current_task = 'Waiting for user input on cultural content approval',
    last_heartbeat = NOW()
WHERE agent_id = 'claude-code-41259';

-- ========================================
-- 6️⃣ CLAIM A TASK (Both agents: Coordinate work)
-- ========================================
-- Find available tasks:
SELECT 
  id,
  task_name,
  description,
  priority,
  status,
  files_affected,
  created_at
FROM task_board 
WHERE status = 'available'
ORDER BY priority ASC, created_at ASC
LIMIT 10;

-- Claim a task:
UPDATE task_board 
SET status = 'claimed',
    claimed_by = 'Claude Code',  -- Or 'Cursor AI Agent'
    claimed_at = NOW()
WHERE id = 'task-id-here'
  AND status = 'available'
RETURNING id, task_name, claimed_by;

-- Mark task complete:
UPDATE task_board 
SET status = 'done',
    completed_at = NOW()
WHERE id = 'task-id-here'
  AND claimed_by = 'Claude Code';

-- ========================================
-- 7️⃣ CHECK FILE CONFLICTS (Both agents: Before editing!)
-- ========================================
-- See what files other agents are editing:
SELECT 
  agent_name,
  status,
  current_task,
  UNNEST(files_editing) as file_being_edited,
  last_heartbeat
FROM agent_status 
WHERE files_editing IS NOT NULL
  AND CARDINALITY(files_editing) > 0
  AND last_heartbeat > NOW() - INTERVAL '10 minutes';

-- ========================================
-- 8️⃣ SHARE YOUR LEARNINGS (Both agents: After completing work)
-- ========================================
INSERT INTO agent_knowledge (
  source_type,
  source_name,
  doc_type,
  key_insights,
  technical_details,
  agents_involved
) VALUES (
  'session',
  'Fixed 15 Orphaned Pages in Generated Resources Alpha',  -- What you did
  'implementation_guide',
  ARRAY[
    'Linked 15 Q90+ handouts to Mathematics hub',
    'Created contains_resource relationships with confidence 0.95',
    'All resources now discoverable via hub navigation',
    'Pattern: link to parent hub + related subject + 2-3 related lessons'
  ],
  jsonb_build_object(
    'files_modified', ARRAY['/public/generated-resources-alpha/handouts/*.html'],
    'relationships_created', 45,
    'time_taken_minutes', 30,
    'quality_improvement', 'Discoverability increased from 0% to 100%',
    'pattern_used', 'Hub -> contains_resource -> handout (confidence 0.95)'
  ),
  ARRAY['Claude Code']  -- Or 'Cursor AI Agent' or both
)
RETURNING id, source_name;

-- ========================================
-- 9️⃣ QUERY WHAT OTHERS HAVE LEARNED (Both agents: Before starting)
-- ========================================
SELECT 
  source_name,
  doc_type,
  key_insights,
  technical_details->>'pattern_used' as pattern,
  agents_involved,
  created_at
FROM agent_knowledge 
WHERE source_name ILIKE '%orphan%'  -- Or your topic
  OR key_insights::text ILIKE '%orphan%'
ORDER BY created_at DESC
LIMIT 5;

-- ========================================
-- 🔟 HEARTBEAT MAINTENANCE (Both agents: Every 2-3 minutes)
-- ========================================
-- Simple heartbeat to show you're alive:
UPDATE agent_status 
SET last_heartbeat = NOW()
WHERE agent_id = 'claude-code-41259';  -- Or 'cursor-agent'

-- Heartbeat with status update:
UPDATE agent_status 
SET last_heartbeat = NOW(),
    current_task = 'Updated task description here'
WHERE agent_id = 'claude-code-41259';

-- ========================================
-- 📊 COORDINATION DASHBOARD (Both agents: Quick overview)
-- ========================================
-- Who's working on what right now:
SELECT 
  'ACTIVE AGENTS' as section,
  agent_name as name,
  status,
  current_task,
  EXTRACT(MINUTE FROM (NOW() - last_heartbeat)) || 'm ago' as last_seen
FROM agent_status 
WHERE last_heartbeat > NOW() - INTERVAL '15 minutes'

UNION ALL

SELECT 
  'AVAILABLE TASKS',
  task_name,
  priority,
  description,
  created_at::text
FROM task_board 
WHERE status = 'available'
ORDER BY section, name;

-- ========================================
-- ⚡ QUICK COORDINATION PATTERNS
-- ========================================

-- Pattern 1: "I'm starting work on X"
-- Step 1: Update your status
-- Step 2: Check if anyone else is working on it
-- Step 3: Send a broadcast message
-- Step 4: Start work

-- Pattern 2: "Can someone help with Y?"
-- Step 1: Send high-priority message to broadcast
-- Step 2: Update status to 'blocked'
-- Step 3: Wait for response in agent_messages

-- Pattern 3: "I found something useful"
-- Step 1: Add to agent_knowledge
-- Step 2: Send medium-priority message to broadcast
-- Step 3: Continue work

-- Pattern 4: "I'm done with task Z"
-- Step 1: Mark task as 'done' in task_board
-- Step 2: Add learnings to agent_knowledge
-- Step 3: Update status to 'idle'
-- Step 4: Send completion message

-- ========================================
-- 🎯 RECOMMENDED WORKFLOW
-- ========================================

-- Every 2-3 minutes:
-- 1. Send heartbeat (UPDATE agent_status SET last_heartbeat = NOW())
-- 2. Check for new messages (SELECT from agent_messages WHERE to_agent = 'you')
-- 3. Update current_task if it changed

-- Before starting a new task:
-- 1. Query agent_knowledge for similar work
-- 2. Check agent_status for file conflicts
-- 3. Claim task in task_board
-- 4. Send message announcing what you're doing

-- After completing a task:
-- 1. Add learnings to agent_knowledge
-- 2. Mark task as 'done'
-- 3. Send completion message
-- 4. Update status to 'idle'

-- ========================================
-- 💡 TIPS FOR EFFECTIVE COORDINATION
-- ========================================

-- ✅ DO:
-- - Update heartbeat every 2-3 minutes
-- - Check messages frequently (every 5 minutes)
-- - Announce what you're working on
-- - Share learnings after completing work
-- - Check file conflicts before editing
-- - Use priority levels appropriately (urgent/high/medium/low)

-- ❌ DON'T:
-- - Let heartbeat go stale (>5 minutes without update)
-- - Edit files another agent is working on
-- - Start work without checking agent_knowledge first
-- - Forget to mark tasks as complete
-- - Leave status as 'working' when you're done

-- ========================================
-- 🚀 READY TO COORDINATE!
-- ========================================

-- Claude Code: Start by running query #1 to register your presence!
-- Then run query #2 to see who else is active!
-- Then run query #3 to send a hello message!

