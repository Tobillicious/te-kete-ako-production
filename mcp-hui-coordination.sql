-- MCP HUI COORDINATION - DISCOVERY QUERIES
-- Run these in Supabase SQL Editor to assess current state

-- ============================================
-- PHASE 1: INTELLIGENCE GATHERING
-- ============================================

-- 1. Check what other agents have learned about security, coordination, and platform state
SELECT 
    agent_id,
    knowledge_type,
    LEFT(knowledge_content, 100) as content_preview,
    confidence,
    created_at
FROM agent_knowledge 
WHERE knowledge_type IN ('security_fix', 'system_implementation', 'coordination', 'sprint_discovery')
ORDER BY created_at DESC 
LIMIT 20;

-- 2. Check who's currently working and what they're doing
SELECT 
    agent_name,
    status,
    current_task,
    task_started_at,
    files_being_edited
FROM agent_coordination 
WHERE status IN ('working', 'planning')
ORDER BY task_started_at DESC;

-- 3. Get latest platform insights from GraphRAG
SELECT 
    title,
    file_path,
    content_type,
    cultural_level,
    quality_score
FROM graphrag_resources 
WHERE quality_score >= 90 
AND cultural_level >= 80
ORDER BY quality_score DESC, cultural_level DESC
LIMIT 15;

-- 4. Check for any security issues remaining
SELECT 
    schemaname,
    tablename,
    rowsecurity as rls_enabled
FROM pg_tables 
WHERE schemaname = 'public' 
AND tablename IN (
    'teacher_lesson_plans', 
    'teacher_favorites', 
    'beta_feedback',
    'bmad_deployment_queue', 
    'content_audit_results', 
    'deployment_summary'
)
ORDER BY tablename;

-- 5. Check view security settings
SELECT 
    n.nspname AS schema,
    c.relname AS view,
    c.reloptions
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
  AND c.relname IN ('featured_resources', 'user_kete_view', 'graphrag_summary')
ORDER BY c.relname;

-- ============================================
-- PHASE 2: SPRINT PLANNING
-- ============================================

-- 6. Log our MCP HUI coordination session
INSERT INTO agent_coordination (
    agent_id,
    agent_name,
    status,
    current_task,
    task_started_at,
    estimated_completion,
    files_being_edited
) VALUES (
    'mcp-hui-coordinator',
    'MCP HUI Coordinator',
    'planning',
    'Multi-agent coordination sprint planning and execution',
    NOW(),
    NOW() + INTERVAL '4 hours',
    ARRAY['COLLABORATIVE-MCP-HUI-SPRINT.md', 'mcp-hui-coordination.sql']
);

-- 7. Log our coordination approach to agent_knowledge
INSERT INTO agent_knowledge (
    agent_id,
    knowledge_type,
    knowledge_content,
    confidence,
    verified
) VALUES (
    'mcp-hui-coordinator',
    'coordination',
    'MCP HUI Coordination Framework: 4-phase process using agent_coordination, agent_knowledge, agent_messages tables. Includes discovery queries, sprint planning, real-time coordination, and knowledge sharing. Ready for immediate multi-agent collaboration.',
    0.95,
    true
);

-- ============================================
-- PHASE 3: SPRINT OPTIONS ASSESSMENT
-- ============================================

-- 8. Assess security sprint readiness
SELECT 
    COUNT(*) as total_tables,
    COUNT(CASE WHEN rowsecurity THEN 1 END) as rls_enabled_tables,
    COUNT(CASE WHEN NOT rowsecurity THEN 1 END) as rls_disabled_tables
FROM pg_tables 
WHERE schemaname = 'public' 
AND tablename IN (
    'teacher_lesson_plans', 'teacher_favorites', 'beta_feedback',
    'bmad_deployment_queue', 'content_audit_results', 'deployment_summary'
);

-- 9. Assess content excellence opportunities
SELECT 
    COUNT(*) as high_quality_resources,
    AVG(cultural_level) as avg_cultural_level,
    AVG(quality_score) as avg_quality_score
FROM graphrag_resources 
WHERE quality_score >= 90 
AND cultural_level >= 80;

-- 10. Check for platform optimization opportunities
SELECT 
    file_path,
    content_type,
    quality_score,
    cultural_level
FROM graphrag_resources 
WHERE file_path LIKE '%.css' 
OR file_path LIKE '%.js'
OR file_path LIKE '%navigation%'
ORDER BY quality_score DESC
LIMIT 10;

-- ============================================
-- PHASE 4: COLLABORATION READINESS
-- ============================================

-- 11. Check if coordination tables exist and are populated
SELECT 
    'agent_coordination' as table_name,
    COUNT(*) as record_count,
    MAX(updated_at) as last_update
FROM agent_coordination
UNION ALL
SELECT 
    'agent_knowledge' as table_name,
    COUNT(*) as record_count,
    MAX(created_at) as last_update
FROM agent_knowledge
UNION ALL
SELECT 
    'graphrag_resources' as table_name,
    COUNT(*) as record_count,
    MAX(created_at) as last_update
FROM graphrag_resources;

-- 12. Ready for sprint execution
SELECT 
    'MCP HUI Coordination Ready' as status,
    NOW() as coordination_started,
    'Run discovery queries above, then choose sprint option' as next_steps;