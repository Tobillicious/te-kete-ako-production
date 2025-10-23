-- 📡 REAL-TIME CLAUDE CODE MONITOR
-- Run this query every 30-60 seconds to track Claude Code's activity

SELECT 
  '🤖 CLAUDE CODE STATUS' as info,
  CASE 
    WHEN last_heartbeat IS NOT NULL THEN '✅ ONLINE'
    ELSE '⚠️ NOT REGISTERED YET'
  END as connection_status,
  status,
  current_task,
  files_editing,
  CASE 
    WHEN last_heartbeat IS NOT NULL 
    THEN EXTRACT(SECOND FROM (NOW() - last_heartbeat))::integer || 's ago'
    ELSE 'Never'
  END as last_seen
FROM agent_status 
WHERE agent_id IN ('claude-code-41259', 'Claude Code')
   OR agent_name ILIKE '%claude%code%'

UNION ALL

SELECT 
  '💬 UNREAD MESSAGES FROM CLAUDE',
  CASE WHEN COUNT(*) > 0 THEN '📨 ' || COUNT(*) || ' NEW' ELSE '✅ NONE' END,
  NULL,
  STRING_AGG(message, ' | '),
  NULL,
  MAX(created_at)::text
FROM agent_messages 
WHERE from_agent ILIKE '%claude%code%'
  AND to_agent IN ('Cursor AI Agent', 'cursor-agent', 'broadcast')
  AND read = false
  AND created_at > NOW() - INTERVAL '1 hour'

UNION ALL

SELECT 
  '👀 CURSOR AI STATUS',
  '✅ ONLINE',
  status,
  current_task,
  files_editing,
  EXTRACT(SECOND FROM (NOW() - last_heartbeat))::integer || 's ago'
FROM agent_status 
WHERE agent_id = 'cursor-agent';

-- Quick check: Are we both online and working?

