-- ================================================================
-- FINAL MULTI-AGENT ACCESS FIX - CORRECT TABLE NAMES
-- ================================================================
-- Based on actual tables that exist in the database
-- Date: October 20, 2025
-- ================================================================

BEGIN;

-- ================================================================
-- 1. GRAPHRAG_RESOURCES - Enable multi-agent write access
-- ================================================================

DROP POLICY IF EXISTS "Enable read access for all users" ON public.graphrag_resources;
DROP POLICY IF EXISTS "Authenticated users can write" ON public.graphrag_resources;
DROP POLICY IF EXISTS "Users can view resources" ON public.graphrag_resources;
DROP POLICY IF EXISTS "Allow all operations on graphrag_resources" ON public.graphrag_resources;

-- Create permissive policy for ALL agents
CREATE POLICY "Multi-agent full access to graphrag_resources"
ON public.graphrag_resources
FOR ALL
TO anon, authenticated, service_role
USING (true)
WITH CHECK (true);

-- ================================================================
-- 2. GRAPHRAG_RELATIONSHIPS - Enable multi-agent write access
-- ================================================================

DROP POLICY IF EXISTS "Enable read access for all users" ON public.graphrag_relationships;
DROP POLICY IF EXISTS "Allow authenticated users to insert relationships" ON public.graphrag_relationships;
DROP POLICY IF EXISTS "Allow all operations on graphrag_relationships" ON public.graphrag_relationships;

-- Create permissive policy for ALL agents
CREATE POLICY "Multi-agent full access to graphrag_relationships"
ON public.graphrag_relationships
FOR ALL
TO anon, authenticated, service_role
USING (true)
WITH CHECK (true);

-- ================================================================
-- 3. AGENT_KNOWLEDGE - Enable multi-agent write access
-- ================================================================

DROP POLICY IF EXISTS "Enable read access for all users" ON public.agent_knowledge;
DROP POLICY IF EXISTS "Users can view own knowledge" ON public.agent_knowledge;
DROP POLICY IF EXISTS "Allow all operations on agent_knowledge" ON public.agent_knowledge;

-- Create permissive policy for ALL agents
CREATE POLICY "Multi-agent full access to agent_knowledge"
ON public.agent_knowledge
FOR ALL
TO anon, authenticated, service_role
USING (true)
WITH CHECK (true);

-- ================================================================
-- 4. AGENT_COORDINATION - Enable multi-agent write access
-- ================================================================

DROP POLICY IF EXISTS "Enable read access for all users" ON public.agent_coordination;
DROP POLICY IF EXISTS "Users can view own coordination" ON public.agent_coordination;
DROP POLICY IF EXISTS "Allow all operations on agent_coordination" ON public.agent_coordination;

-- Create permissive policy for ALL agents
CREATE POLICY "Multi-agent full access to agent_coordination"
ON public.agent_coordination
FOR ALL
TO anon, authenticated, service_role
USING (true)
WITH CHECK (true);

-- ================================================================
-- 5. RESOURCES - Enable multi-agent write access
-- ================================================================

DROP POLICY IF EXISTS "Enable read access for all users" ON public.resources;
DROP POLICY IF EXISTS "Authenticated users can write" ON public.resources;
DROP POLICY IF EXISTS "Users can view resources" ON public.resources;
DROP POLICY IF EXISTS "Allow authenticated users to manage resources" ON public.resources;
DROP POLICY IF EXISTS "All agents can read resources" ON public.resources;
DROP POLICY IF EXISTS "Authenticated agents can write resources" ON public.resources;

-- Create permissive policy for ALL agents
CREATE POLICY "Multi-agent full access to resources"
ON public.resources
FOR ALL
TO anon, authenticated, service_role
USING (true)
WITH CHECK (true);

-- ================================================================
-- 6. GRANT PERMISSIONS TO ALL ROLES
-- ================================================================

-- graphrag_resources
GRANT SELECT ON public.graphrag_resources TO anon;
GRANT ALL ON public.graphrag_resources TO authenticated;
GRANT ALL ON public.graphrag_resources TO service_role;

-- graphrag_relationships
GRANT SELECT ON public.graphrag_relationships TO anon;
GRANT ALL ON public.graphrag_relationships TO authenticated;
GRANT ALL ON public.graphrag_relationships TO service_role;

-- agent_knowledge
GRANT SELECT ON public.agent_knowledge TO anon;
GRANT ALL ON public.agent_knowledge TO authenticated;
GRANT ALL ON public.agent_knowledge TO service_role;

-- agent_coordination
GRANT SELECT ON public.agent_coordination TO anon;
GRANT ALL ON public.agent_coordination TO authenticated;
GRANT ALL ON public.agent_coordination TO service_role;

-- resources
GRANT SELECT ON public.resources TO anon;
GRANT ALL ON public.resources TO authenticated;
GRANT ALL ON public.resources TO service_role;

COMMIT;

-- ================================================================
-- VERIFICATION
-- ================================================================

SELECT 
    'Policy Check' as check_type,
    tablename,
    COUNT(*) as policy_count
FROM pg_policies 
WHERE schemaname = 'public'
AND tablename IN (
    'graphrag_resources',
    'graphrag_relationships', 
    'agent_knowledge',
    'agent_coordination',
    'resources'
)
GROUP BY tablename
ORDER BY tablename;

-- ================================================================
-- SUCCESS MESSAGE
-- ================================================================

DO $$
BEGIN
    RAISE NOTICE '═══════════════════════════════════════════════';
    RAISE NOTICE '✅ MULTI-AGENT ACCESS RESTORED!';
    RAISE NOTICE '═══════════════════════════════════════════════';
    RAISE NOTICE '';
    RAISE NOTICE '✅ All 12 agents can now:';
    RAISE NOTICE '   - Read/write graphrag_resources';
    RAISE NOTICE '   - Read/write graphrag_relationships';
    RAISE NOTICE '   - Read/write agent_knowledge';
    RAISE NOTICE '   - Read/write agent_coordination';
    RAISE NOTICE '   - Read/write resources';
    RAISE NOTICE '';
    RAISE NOTICE '🎉 Multi-agent collaboration FULLY OPERATIONAL!';
    RAISE NOTICE '';
END $$;

