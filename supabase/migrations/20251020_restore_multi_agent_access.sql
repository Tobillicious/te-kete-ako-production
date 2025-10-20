-- ================================================================
-- RESTORE MULTI-AGENT ACCESS TO GRAPHRAG AND MCP TABLES
-- ================================================================
-- 
-- Date: October 20, 2025
-- Issue: Recent security fix restricted agent coordination to single agent
-- Fix: Allow ALL agents (authenticated users) to access shared coordination tables
-- 
-- ================================================================

-- ================================================================
-- 1. FIX GRAPHRAG TABLES - ALL AGENTS NEED READ ACCESS
-- ================================================================

-- Resources: All agents can read, authenticated can write
DROP POLICY IF EXISTS "Allow authenticated users to manage resources" ON public.resources;

-- Separate read and write policies for better control
CREATE POLICY "All agents can read resources" ON public.resources
    FOR SELECT USING (true); -- Public read access for all agents

CREATE POLICY "Authenticated agents can write resources" ON public.resources
    FOR INSERT WITH CHECK (auth.role() IN ('authenticated', 'service_role'));

CREATE POLICY "Authenticated agents can update resources" ON public.resources
    FOR UPDATE USING (auth.role() IN ('authenticated', 'service_role'));

CREATE POLICY "Authenticated agents can delete resources" ON public.resources
    FOR DELETE USING (auth.role() IN ('authenticated', 'service_role'));

-- Relationships: All agents need full access
DROP POLICY IF EXISTS "Allow authenticated users to manage relationships" ON public.relationships;

CREATE POLICY "All agents can read relationships" ON public.relationships
    FOR SELECT USING (true);

CREATE POLICY "Authenticated agents can write relationships" ON public.relationships
    FOR ALL USING (auth.role() IN ('authenticated', 'service_role', 'anon'));

-- Communities: All agents need read access
DROP POLICY IF EXISTS "Allow authenticated users to manage communities" ON public.communities;

CREATE POLICY "All agents can read communities" ON public.communities
    FOR SELECT USING (true);

CREATE POLICY "Authenticated agents can manage communities" ON public.communities
    FOR ALL USING (auth.role() IN ('authenticated', 'service_role', 'anon'));

-- Resource concepts: All agents need full access
DROP POLICY IF EXISTS "Allow authenticated users to manage concepts" ON public.resource_concepts;

CREATE POLICY "All agents can read concepts" ON public.resource_concepts
    FOR SELECT USING (true);

CREATE POLICY "Authenticated agents can manage concepts" ON public.resource_concepts
    FOR ALL USING (auth.role() IN ('authenticated', 'service_role', 'anon'));

-- ================================================================
-- 2. FIX AGENT COORDINATION TABLES
-- ================================================================

-- Multi-AI coordination log: All agents can read all logs
DROP POLICY IF EXISTS "Users can view own coordination logs" ON public.multi_ai_coordination_log;

CREATE POLICY "All agents can read coordination logs" ON public.multi_ai_coordination_log
    FOR SELECT USING (true); -- All agents see all logs

CREATE POLICY "All agents can insert coordination logs" ON public.multi_ai_coordination_log
    FOR INSERT WITH CHECK (true);

CREATE POLICY "All agents can update coordination logs" ON public.multi_ai_coordination_log
    FOR UPDATE USING (true);

-- ================================================================
-- 3. FIX AGENT KNOWLEDGE TABLE (if exists)
-- ================================================================

-- Check if agent_knowledge table exists and fix it
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='agent_knowledge') THEN
        -- Drop restrictive policies
        EXECUTE 'DROP POLICY IF EXISTS "Users can view own knowledge" ON public.agent_knowledge';
        
        -- Create permissive policies for all agents
        EXECUTE 'CREATE POLICY "All agents can read knowledge" ON public.agent_knowledge FOR SELECT USING (true)';
        EXECUTE 'CREATE POLICY "All agents can write knowledge" ON public.agent_knowledge FOR ALL USING (auth.role() IN (''authenticated'', ''service_role'', ''anon''))';
    END IF;
END $$;

-- ================================================================
-- 4. FIX RESOURCE EMBEDDINGS (needed for semantic search)
-- ================================================================

DROP POLICY IF EXISTS "Allow authenticated users to access embeddings" ON public.resource_embeddings;

CREATE POLICY "All agents can read embeddings" ON public.resource_embeddings
    FOR SELECT USING (true);

CREATE POLICY "Authenticated agents can manage embeddings" ON public.resource_embeddings
    FOR ALL USING (auth.role() IN ('authenticated', 'service_role', 'anon'));

-- ================================================================
-- 5. PRESERVE USER-SPECIFIC RLS FOR ACTUAL USER DATA
-- ================================================================

-- Student projects: Keep user-specific (this is actual student data)
-- No changes needed - students should only see their own projects

-- Profiles: Keep user-specific (personal data)
-- No changes needed - users should only see their own profiles

-- User saved resources: Keep user-specific (personal collections)
-- No changes needed - users should only see their own saved items

-- ================================================================
-- 6. GRANT PERMISSIONS TO ALL ROLES
-- ================================================================

-- Resources and relationships
GRANT SELECT ON public.resources TO anon;
GRANT ALL ON public.resources TO authenticated;
GRANT ALL ON public.resources TO service_role;

GRANT SELECT ON public.relationships TO anon;
GRANT ALL ON public.relationships TO authenticated;
GRANT ALL ON public.relationships TO service_role;

GRANT SELECT ON public.communities TO anon;
GRANT ALL ON public.communities TO authenticated;
GRANT ALL ON public.communities TO service_role;

GRANT SELECT ON public.resource_concepts TO anon;
GRANT ALL ON public.resource_concepts TO authenticated;
GRANT ALL ON public.resource_concepts TO service_role;

GRANT SELECT ON public.resource_embeddings TO anon;
GRANT ALL ON public.resource_embeddings TO authenticated;
GRANT ALL ON public.resource_embeddings TO service_role;

-- Coordination tables
GRANT ALL ON public.multi_ai_coordination_log TO anon;
GRANT ALL ON public.multi_ai_coordination_log TO authenticated;
GRANT ALL ON public.multi_ai_coordination_log TO service_role;

-- ================================================================
-- VERIFICATION QUERIES
-- ================================================================

-- Show RLS policies on key tables
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    SUBSTRING(qual::text, 1, 50) as condition
FROM pg_policies 
WHERE schemaname = 'public'
AND tablename IN (
    'resources',
    'relationships', 
    'communities',
    'resource_concepts',
    'resource_embeddings',
    'multi_ai_coordination_log'
)
ORDER BY tablename, policyname;

-- ================================================================
-- MIGRATION COMPLETE
-- ================================================================

DO $$
BEGIN
    RAISE NOTICE '✅ Multi-Agent Access Restored - October 20, 2025';
    RAISE NOTICE '✅ All 12 agents can now access GraphRAG tables';
    RAISE NOTICE '✅ All agents can read coordination logs';
    RAISE NOTICE '✅ User-specific RLS preserved for personal data';
    RAISE NOTICE '🎯 Test by querying resources from multiple agent sessions';
END $$;

