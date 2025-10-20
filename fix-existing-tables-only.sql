-- ================================================================
-- FIX MULTI-AGENT ACCESS - EXISTING TABLES ONLY
-- ================================================================
-- 
-- This version checks which tables exist first, then fixes only those
-- 
-- ================================================================

-- ================================================================
-- 1. FIX GRAPHRAG_RESOURCES TABLE (if exists)
-- ================================================================

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='graphrag_resources') THEN
        RAISE NOTICE '✅ Found graphrag_resources table - fixing...';
        
        -- Enable RLS
        EXECUTE 'ALTER TABLE public.graphrag_resources ENABLE ROW LEVEL SECURITY';
        
        -- Drop any restrictive policies
        EXECUTE 'DROP POLICY IF EXISTS "Enable read access for authenticated users" ON public.graphrag_resources';
        EXECUTE 'DROP POLICY IF EXISTS "Restrict write to authenticated" ON public.graphrag_resources';
        
        -- Create open access policies
        EXECUTE 'CREATE POLICY "All can view graphrag resources" ON public.graphrag_resources FOR SELECT USING (true)';
        EXECUTE 'CREATE POLICY "All can insert graphrag resources" ON public.graphrag_resources FOR INSERT WITH CHECK (true)';
        EXECUTE 'CREATE POLICY "All can update graphrag resources" ON public.graphrag_resources FOR UPDATE USING (true)';
        EXECUTE 'CREATE POLICY "All can delete graphrag resources" ON public.graphrag_resources FOR DELETE USING (true)';
        
        -- Grant to anon and authenticated
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.graphrag_resources TO anon';
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.graphrag_resources TO authenticated';
        
        RAISE NOTICE '✅ graphrag_resources fixed!';
    ELSE
        RAISE NOTICE '⚠️  graphrag_resources table not found - skipping';
    END IF;
END $$;

-- ================================================================
-- 2. FIX GRAPHRAG_RELATIONSHIPS TABLE (if exists)
-- ================================================================

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='graphrag_relationships') THEN
        RAISE NOTICE '✅ Found graphrag_relationships table - fixing...';
        
        -- Enable RLS
        EXECUTE 'ALTER TABLE public.graphrag_relationships ENABLE ROW LEVEL SECURITY';
        
        -- Drop any restrictive policies
        EXECUTE 'DROP POLICY IF EXISTS "Enable read access for authenticated users" ON public.graphrag_relationships';
        EXECUTE 'DROP POLICY IF EXISTS "Restrict write to authenticated" ON public.graphrag_relationships';
        
        -- Create open access policies
        EXECUTE 'CREATE POLICY "All can view graphrag relationships" ON public.graphrag_relationships FOR SELECT USING (true)';
        EXECUTE 'CREATE POLICY "All can insert graphrag relationships" ON public.graphrag_relationships FOR INSERT WITH CHECK (true)';
        EXECUTE 'CREATE POLICY "All can update graphrag relationships" ON public.graphrag_relationships FOR UPDATE USING (true)';
        EXECUTE 'CREATE POLICY "All can delete graphrag relationships" ON public.graphrag_relationships FOR DELETE USING (true)';
        
        -- Grant to anon and authenticated
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.graphrag_relationships TO anon';
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.graphrag_relationships TO authenticated';
        
        RAISE NOTICE '✅ graphrag_relationships fixed!';
    ELSE
        RAISE NOTICE '⚠️  graphrag_relationships table not found - skipping';
    END IF;
END $$;

-- ================================================================
-- 3. FIX AGENT_KNOWLEDGE TABLE (if exists)
-- ================================================================

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='agent_knowledge') THEN
        RAISE NOTICE '✅ Found agent_knowledge table - fixing...';
        
        -- Enable RLS
        EXECUTE 'ALTER TABLE public.agent_knowledge ENABLE ROW LEVEL SECURITY';
        
        -- Drop any restrictive policies
        EXECUTE 'DROP POLICY IF EXISTS "Agents can view own knowledge" ON public.agent_knowledge';
        EXECUTE 'DROP POLICY IF EXISTS "Enable read access for authenticated users" ON public.agent_knowledge';
        
        -- Create open access policies
        EXECUTE 'CREATE POLICY "All can view agent knowledge" ON public.agent_knowledge FOR SELECT USING (true)';
        EXECUTE 'CREATE POLICY "All can insert agent knowledge" ON public.agent_knowledge FOR INSERT WITH CHECK (true)';
        EXECUTE 'CREATE POLICY "All can update agent knowledge" ON public.agent_knowledge FOR UPDATE USING (true)';
        EXECUTE 'CREATE POLICY "All can delete agent knowledge" ON public.agent_knowledge FOR DELETE USING (true)';
        
        -- Grant to anon and authenticated
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.agent_knowledge TO anon';
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.agent_knowledge TO authenticated';
        
        RAISE NOTICE '✅ agent_knowledge fixed!';
    ELSE
        RAISE NOTICE '⚠️  agent_knowledge table not found - skipping';
    END IF;
END $$;

-- ================================================================
-- 4. FIX AGENT_COORDINATION TABLE (if exists)
-- ================================================================

DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='agent_coordination') THEN
        RAISE NOTICE '✅ Found agent_coordination table - fixing...';
        
        -- Enable RLS
        EXECUTE 'ALTER TABLE public.agent_coordination ENABLE ROW LEVEL SECURITY';
        
        -- Drop any restrictive policies
        EXECUTE 'DROP POLICY IF EXISTS "Agents can view own coordination" ON public.agent_coordination';
        
        -- Create open access policies
        EXECUTE 'CREATE POLICY "All can view coordination" ON public.agent_coordination FOR SELECT USING (true)';
        EXECUTE 'CREATE POLICY "All can insert coordination" ON public.agent_coordination FOR INSERT WITH CHECK (true)';
        EXECUTE 'CREATE POLICY "All can update coordination" ON public.agent_coordination FOR UPDATE USING (true)';
        EXECUTE 'CREATE POLICY "All can delete coordination" ON public.agent_coordination FOR DELETE USING (true)';
        
        -- Grant to anon and authenticated
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.agent_coordination TO anon';
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON public.agent_coordination TO authenticated';
        
        RAISE NOTICE '✅ agent_coordination fixed!';
    ELSE
        RAISE NOTICE '⚠️  agent_coordination table not found - skipping';
    END IF;
END $$;

-- ================================================================
-- 5. CHECK WHAT TABLES EXIST
-- ================================================================

SELECT 
    tablename,
    CASE WHEN rowsecurity THEN '🔒 RLS ENABLED' ELSE '🔓 RLS DISABLED' END as security_status
FROM pg_tables
WHERE schemaname = 'public'
AND tablename LIKE '%graphrag%' 
   OR tablename LIKE '%agent%'
ORDER BY tablename;

-- ================================================================
-- 6. VERIFY POLICIES
-- ================================================================

SELECT 
    tablename,
    policyname,
    cmd,
    CASE WHEN 'anon' = ANY(roles) THEN '✅ ANON ACCESS' ELSE '❌ NO ANON' END as anon_access
FROM pg_policies
WHERE schemaname = 'public'
AND (tablename LIKE '%graphrag%' OR tablename LIKE '%agent%')
ORDER BY tablename, policyname;

-- ================================================================
-- 7. TEST QUERIES (to verify access works)
-- ================================================================

-- Test graphrag_resources
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='graphrag_resources') THEN
        EXECUTE 'SELECT COUNT(*) FROM public.graphrag_resources';
        RAISE NOTICE '✅ Can query graphrag_resources';
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE '❌ Cannot query graphrag_resources: %', SQLERRM;
END $$;

-- Test graphrag_relationships  
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='graphrag_relationships') THEN
        EXECUTE 'SELECT COUNT(*) FROM public.graphrag_relationships';
        RAISE NOTICE '✅ Can query graphrag_relationships';
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE '❌ Cannot query graphrag_relationships: %', SQLERRM;
END $$;

-- Test agent_knowledge
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='agent_knowledge') THEN
        EXECUTE 'SELECT COUNT(*) FROM public.agent_knowledge';
        RAISE NOTICE '✅ Can query agent_knowledge';
    END IF;
EXCEPTION WHEN OTHERS THEN
    RAISE NOTICE '❌ Cannot query agent_knowledge: %', SQLERRM;
END $$;

-- ================================================================
-- SUMMARY
-- ================================================================

DO $$
DECLARE
    graphrag_exists boolean;
    relationships_exists boolean;
    knowledge_exists boolean;
BEGIN
    -- Check what exists
    SELECT EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='graphrag_resources') INTO graphrag_exists;
    SELECT EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='graphrag_relationships') INTO relationships_exists;
    SELECT EXISTS (SELECT 1 FROM pg_tables WHERE schemaname='public' AND tablename='agent_knowledge') INTO knowledge_exists;
    
    RAISE NOTICE '';
    RAISE NOTICE '═══════════════════════════════════════════════════';
    RAISE NOTICE '🎯 MULTI-AGENT ACCESS FIX - SUMMARY';
    RAISE NOTICE '═══════════════════════════════════════════════════';
    RAISE NOTICE '';
    
    IF graphrag_exists THEN
        RAISE NOTICE '✅ graphrag_resources: FIXED - all agents can access';
    ELSE
        RAISE NOTICE '⚠️  graphrag_resources: TABLE NOT FOUND';
    END IF;
    
    IF relationships_exists THEN
        RAISE NOTICE '✅ graphrag_relationships: FIXED - all agents can access';
    ELSE
        RAISE NOTICE '⚠️  graphrag_relationships: TABLE NOT FOUND';
    END IF;
    
    IF knowledge_exists THEN
        RAISE NOTICE '✅ agent_knowledge: FIXED - all agents can access';
    ELSE
        RAISE NOTICE '⚠️  agent_knowledge: TABLE NOT FOUND';
    END IF;
    
    RAISE NOTICE '';
    RAISE NOTICE '🚀 All existing GraphRAG tables now support multi-agent access!';
    RAISE NOTICE '🔓 Permissions granted to: anon, authenticated';
    RAISE NOTICE '';
    RAISE NOTICE '💡 TIP: If tables are missing, agents will create them';
    RAISE NOTICE '    automatically when they first try to store data.';
    RAISE NOTICE '═══════════════════════════════════════════════════';
END $$;

