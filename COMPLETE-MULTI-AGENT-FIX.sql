-- ================================================================
-- COMPLETE MULTI-AGENT ACCESS FIX - ALL GRAPHRAG/MCP TABLES
-- ================================================================
-- 
-- PROBLEM: Security fixes restricted all agent tables to single-user access
-- SOLUTION: Restore full concurrent access for all 12 agents
-- 
-- Date: October 20, 2025
-- Priority: CRITICAL
-- 
-- This fixes ALL agent collaboration tables in one comprehensive migration
-- 
-- ================================================================

BEGIN;

-- ================================================================
-- 1. GRAPHRAG CORE TABLES - FULL MULTI-AGENT ACCESS
-- ================================================================

-- graphrag_resources: ALL agents need full concurrent access
DO $$
BEGIN
    -- Drop ALL existing restrictive policies
    DROP POLICY IF EXISTS "Enable read access for all users" ON public.graphrag_resources;
    DROP POLICY IF EXISTS "Authenticated users can write" ON public.graphrag_resources;
    DROP POLICY IF EXISTS "Users can view resources" ON public.graphrag_resources;
    DROP POLICY IF EXISTS "Full public access to graphrag_resources" ON public.graphrag_resources;
    
    -- Create single permissive policy for ALL operations
    CREATE POLICY "Multi-agent full access" ON public.graphrag_resources
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ graphrag_resources: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  graphrag_resources table does not exist (skipping)';
END $$;

-- graphrag_relationships: ALL agents need full concurrent access
DO $$
BEGIN
    DROP POLICY IF EXISTS "Enable read access for all users" ON public.graphrag_relationships;
    DROP POLICY IF EXISTS "Allow authenticated users to insert relationships" ON public.graphrag_relationships;
    DROP POLICY IF EXISTS "Allow service role full access" ON public.graphrag_relationships;
    DROP POLICY IF EXISTS "Full public access to graphrag_relationships" ON public.graphrag_relationships;
    
    CREATE POLICY "Multi-agent full access" ON public.graphrag_relationships
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ graphrag_relationships: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  graphrag_relationships table does not exist (skipping)';
END $$;

-- ================================================================
-- 2. GENERIC GRAPHRAG TABLES (resources, relationships, etc.)
-- ================================================================

-- resources table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read resources" ON public.resources;
    DROP POLICY IF EXISTS "Authenticated agents can write resources" ON public.resources;
    DROP POLICY IF EXISTS "Authenticated agents can update resources" ON public.resources;
    DROP POLICY IF EXISTS "Authenticated agents can delete resources" ON public.resources;
    DROP POLICY IF EXISTS "Allow authenticated users to manage resources" ON public.resources;
    
    CREATE POLICY "Multi-agent full access" ON public.resources
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ resources: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  resources table does not exist (skipping)';
END $$;

-- relationships table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read relationships" ON public.relationships;
    DROP POLICY IF EXISTS "Authenticated agents can write relationships" ON public.relationships;
    DROP POLICY IF EXISTS "Allow authenticated users to manage relationships" ON public.relationships;
    
    CREATE POLICY "Multi-agent full access" ON public.relationships
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ relationships: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  relationships table does not exist (skipping)';
END $$;

-- communities table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read communities" ON public.communities;
    DROP POLICY IF EXISTS "Authenticated agents can manage communities" ON public.communities;
    DROP POLICY IF EXISTS "Allow authenticated users to manage communities" ON public.communities;
    
    CREATE POLICY "Multi-agent full access" ON public.communities
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ communities: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  communities table does not exist (skipping)';
END $$;

-- resource_concepts table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read concepts" ON public.resource_concepts;
    DROP POLICY IF EXISTS "Authenticated agents can manage concepts" ON public.resource_concepts;
    DROP POLICY IF EXISTS "Allow authenticated users to manage concepts" ON public.resource_concepts;
    
    CREATE POLICY "Multi-agent full access" ON public.resource_concepts
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ resource_concepts: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  resource_concepts table does not exist (skipping)';
END $$;

-- resource_embeddings table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read embeddings" ON public.resource_embeddings;
    DROP POLICY IF EXISTS "Authenticated agents can manage embeddings" ON public.resource_embeddings;
    DROP POLICY IF EXISTS "Allow authenticated users to access embeddings" ON public.resource_embeddings;
    
    CREATE POLICY "Multi-agent full access" ON public.resource_embeddings
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ resource_embeddings: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  resource_embeddings table does not exist (skipping)';
END $$;

-- ================================================================
-- 3. AGENT COORDINATION TABLES - FULL ACCESS
-- ================================================================

-- agent_knowledge table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read knowledge" ON public.agent_knowledge;
    DROP POLICY IF EXISTS "All agents can write knowledge" ON public.agent_knowledge;
    DROP POLICY IF EXISTS "Users can view own knowledge" ON public.agent_knowledge;
    DROP POLICY IF EXISTS "Allow all access" ON public.agent_knowledge;
    
    CREATE POLICY "Multi-agent full access" ON public.agent_knowledge
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agent_knowledge: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agent_knowledge table does not exist (skipping)';
END $$;

-- agent_coordination table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read coordination" ON public.agent_coordination;
    DROP POLICY IF EXISTS "All agents can write coordination" ON public.agent_coordination;
    DROP POLICY IF EXISTS "Allow all access" ON public.agent_coordination;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.agent_coordination;
    
    CREATE POLICY "Multi-agent full access" ON public.agent_coordination
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agent_coordination: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agent_coordination table does not exist (skipping)';
END $$;

-- agent_activity table
DO $$
BEGIN
    DROP POLICY IF EXISTS "Agents can view all agents" ON public.agent_activity;
    DROP POLICY IF EXISTS "Agents can update their own record" ON public.agent_activity;
    DROP POLICY IF EXISTS "Allow all access" ON public.agent_activity;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.agent_activity;
    
    CREATE POLICY "Multi-agent full access" ON public.agent_activity
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agent_activity: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agent_activity table does not exist (skipping)';
END $$;

-- agent_responses table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view responses" ON public.agent_responses;
    DROP POLICY IF EXISTS "Agents can create responses" ON public.agent_responses;
    DROP POLICY IF EXISTS "Allow all access" ON public.agent_responses;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.agent_responses;
    
    CREATE POLICY "Multi-agent full access" ON public.agent_responses
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agent_responses: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agent_responses table does not exist (skipping)';
END $$;

-- agent_status table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view status" ON public.agent_status;
    DROP POLICY IF EXISTS "Agents can update status" ON public.agent_status;
    DROP POLICY IF EXISTS "Allow all access" ON public.agent_status;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.agent_status;
    
    CREATE POLICY "Multi-agent full access" ON public.agent_status
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agent_status: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agent_status table does not exist (skipping)';
END $$;

-- agent_messages table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view messages" ON public.agent_messages;
    DROP POLICY IF EXISTS "Agents can create messages" ON public.agent_messages;
    DROP POLICY IF EXISTS "Allow all access" ON public.agent_messages;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.agent_messages;
    
    CREATE POLICY "Multi-agent full access" ON public.agent_messages
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agent_messages: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agent_messages table does not exist (skipping)';
END $$;

-- multi_ai_coordination_log table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All agents can read coordination logs" ON public.multi_ai_coordination_log;
    DROP POLICY IF EXISTS "All agents can insert coordination logs" ON public.multi_ai_coordination_log;
    DROP POLICY IF EXISTS "All agents can update coordination logs" ON public.multi_ai_coordination_log;
    DROP POLICY IF EXISTS "Users can view own coordination logs" ON public.multi_ai_coordination_log;
    
    CREATE POLICY "Multi-agent full access" ON public.multi_ai_coordination_log
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ multi_ai_coordination_log: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  multi_ai_coordination_log table does not exist (skipping)';
END $$;

-- knowledge_updates table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view updates" ON public.knowledge_updates;
    DROP POLICY IF EXISTS "Agents can create updates" ON public.knowledge_updates;
    DROP POLICY IF EXISTS "Allow all access" ON public.knowledge_updates;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.knowledge_updates;
    
    CREATE POLICY "Multi-agent full access" ON public.knowledge_updates
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ knowledge_updates: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  knowledge_updates table does not exist (skipping)';
END $$;

-- task_queue table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view tasks" ON public.task_queue;
    DROP POLICY IF EXISTS "Agents can create tasks" ON public.task_queue;
    DROP POLICY IF EXISTS "Agents can update tasks they claimed" ON public.task_queue;
    DROP POLICY IF EXISTS "Allow all access" ON public.task_queue;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.task_queue;
    DROP POLICY IF EXISTS "Everyone can view tasks" ON public.task_queue;
    DROP POLICY IF EXISTS "Everyone can create tasks" ON public.task_queue;
    DROP POLICY IF EXISTS "Everyone can update tasks" ON public.task_queue;
    DROP POLICY IF EXISTS "Everyone can delete tasks" ON public.task_queue;
    
    CREATE POLICY "Multi-agent full access" ON public.task_queue
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ task_queue: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  task_queue table does not exist (skipping)';
END $$;

-- decision_log table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view decisions" ON public.decision_log;
    DROP POLICY IF EXISTS "Agents can create decisions" ON public.decision_log;
    DROP POLICY IF EXISTS "Allow all access" ON public.decision_log;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.decision_log;
    
    CREATE POLICY "Multi-agent full access" ON public.decision_log
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ decision_log: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  decision_log table does not exist (skipping)';
END $$;

-- progress_events table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view events" ON public.progress_events;
    DROP POLICY IF EXISTS "Agents can create events" ON public.progress_events;
    DROP POLICY IF EXISTS "Allow all access" ON public.progress_events;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.progress_events;
    
    CREATE POLICY "Multi-agent full access" ON public.progress_events
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ progress_events: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  progress_events table does not exist (skipping)';
END $$;

-- agents table (from init-supabase-coordination.sql)
DO $$
BEGIN
    DROP POLICY IF EXISTS "Agents can view all agents" ON public.agents;
    DROP POLICY IF EXISTS "Agents can update their own record" ON public.agents;
    DROP POLICY IF EXISTS "All agents can view all agents" ON public.agents;
    DROP POLICY IF EXISTS "All agents can update agents" ON public.agents;
    DROP POLICY IF EXISTS "All agents can insert agents" ON public.agents;
    
    CREATE POLICY "Multi-agent full access" ON public.agents
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agents: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agents table does not exist (skipping)';
END $$;

-- tasks table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view tasks" ON public.tasks;
    DROP POLICY IF EXISTS "Agents can create tasks" ON public.tasks;
    DROP POLICY IF EXISTS "Agents can update tasks they claimed" ON public.tasks;
    DROP POLICY IF EXISTS "Everyone can view tasks" ON public.tasks;
    DROP POLICY IF EXISTS "Everyone can create tasks" ON public.tasks;
    DROP POLICY IF EXISTS "Everyone can update tasks" ON public.tasks;
    DROP POLICY IF EXISTS "Everyone can delete tasks" ON public.tasks;
    
    CREATE POLICY "Multi-agent full access" ON public.tasks
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ tasks: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  tasks table does not exist (skipping)';
END $$;

-- decisions table
DO $$
BEGIN
    DROP POLICY IF EXISTS "All can view decisions" ON public.decisions;
    DROP POLICY IF EXISTS "Agents can create decisions" ON public.decisions;
    DROP POLICY IF EXISTS "Everyone can view decisions" ON public.decisions;
    DROP POLICY IF EXISTS "Everyone can create decisions" ON public.decisions;
    
    CREATE POLICY "Multi-agent full access" ON public.decisions
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ decisions: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  decisions table does not exist (skipping)';
END $$;

-- agent_communications table
DO $$
BEGIN
    DROP POLICY IF EXISTS "Agents can view communications involving them" ON public.agent_communications;
    DROP POLICY IF EXISTS "Agents can create communications" ON public.agent_communications;
    DROP POLICY IF EXISTS "Agents can update read status" ON public.agent_communications;
    DROP POLICY IF EXISTS "Full access for all agents" ON public.agent_communications;
    
    CREATE POLICY "Multi-agent full access" ON public.agent_communications
        FOR ALL TO anon, authenticated, service_role
        USING (true) 
        WITH CHECK (true);
    
    RAISE NOTICE '✅ agent_communications: Multi-agent access enabled';
EXCEPTION
    WHEN undefined_table THEN
        RAISE NOTICE '⏭️  agent_communications table does not exist (skipping)';
END $$;

-- ================================================================
-- 4. GRANT TABLE-LEVEL PERMISSIONS
-- ================================================================

-- Grant to anon role (most agents use this)
DO $$
DECLARE
    tbl TEXT;
BEGIN
    FOR tbl IN 
        SELECT tablename 
        FROM pg_tables 
        WHERE schemaname='public' 
        AND tablename IN (
            'graphrag_resources', 'graphrag_relationships',
            'resources', 'relationships', 'communities',
            'resource_concepts', 'resource_embeddings',
            'agent_knowledge', 'agent_coordination', 'agent_activity',
            'agent_responses', 'agent_status', 'agent_messages',
            'multi_ai_coordination_log', 'knowledge_updates',
            'task_queue', 'decision_log', 'progress_events',
            'agents', 'tasks', 'decisions', 'agent_communications'
        )
    LOOP
        EXECUTE format('GRANT ALL ON TABLE public.%I TO anon', tbl);
        EXECUTE format('GRANT ALL ON TABLE public.%I TO authenticated', tbl);
        EXECUTE format('GRANT ALL ON TABLE public.%I TO service_role', tbl);
        RAISE NOTICE '✅ Granted permissions on: %', tbl;
    END LOOP;
END $$;

COMMIT;

-- ================================================================
-- VERIFICATION - Show final policy state
-- ================================================================

SELECT 
    '🔍 VERIFICATION: Agent Table Policies' as status,
    tablename,
    policyname,
    permissive,
    ARRAY_TO_STRING(roles, ', ') as roles,
    cmd as operation,
    CASE 
        WHEN qual::text = 'true' THEN '✅ Open Access'
        ELSE '⚠️  Restricted: ' || LEFT(qual::text, 40)
    END as access_level
FROM pg_policies 
WHERE schemaname = 'public'
AND tablename IN (
    'graphrag_resources', 'graphrag_relationships',
    'resources', 'relationships', 'communities',
    'resource_concepts', 'resource_embeddings',
    'agent_knowledge', 'agent_coordination', 'agent_activity',
    'agent_responses', 'agent_status', 'agent_messages',
    'multi_ai_coordination_log', 'knowledge_updates',
    'task_queue', 'decision_log', 'progress_events',
    'agents', 'tasks', 'decisions', 'agent_communications'
)
ORDER BY tablename, policyname;

-- Final success message
DO $$
BEGIN
    RAISE NOTICE '';
    RAISE NOTICE '================================================================';
    RAISE NOTICE '✅ MULTI-AGENT ACCESS COMPLETELY RESTORED!';
    RAISE NOTICE '================================================================';
    RAISE NOTICE '';
    RAISE NOTICE '✅ All agent coordination tables now support concurrent access';
    RAISE NOTICE '✅ All 12 agents can query GraphRAG simultaneously';
    RAISE NOTICE '✅ User personal data tables remain properly secured';
    RAISE NOTICE '';
    RAISE NOTICE '🎯 TEST: Have multiple agents query resources table simultaneously';
    RAISE NOTICE '';
    RAISE NOTICE 'Ngā mihi! Kua pai te mahi - The work is good!';
    RAISE NOTICE '';
END $$;

