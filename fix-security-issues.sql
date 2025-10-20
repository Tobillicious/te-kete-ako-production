-- Fix Database Security Issues
-- Addresses all security linting issues identified

-- ============================================
-- 1. FIX SECURITY DEFINER VIEWS
-- ============================================

-- DO NOT drop and recreate; simply set security_invoker flag on existing views
-- This avoids breaking dependencies and preserves definitions

-- Make flagged views run with caller's permissions (Postgres 15+)
DO $$
BEGIN
    BEGIN
        EXECUTE 'ALTER VIEW public.featured_resources SET (security_invoker = true)';
    EXCEPTION WHEN others THEN
        RAISE NOTICE 'featured_resources: %', SQLERRM;
    END;

    BEGIN
        EXECUTE 'ALTER VIEW public.user_kete_view SET (security_invoker = true)';
    EXCEPTION WHEN others THEN
        RAISE NOTICE 'user_kete_view: %', SQLERRM;
    END;

    BEGIN
        EXECUTE 'ALTER VIEW public.graphrag_summary SET (security_invoker = true)';
    EXCEPTION WHEN others THEN
        RAISE NOTICE 'graphrag_summary: %', SQLERRM;
    END;
END $$;

-- ============================================
-- 2. ENABLE RLS ON PUBLIC TABLES
-- ============================================

-- Enable Row Level Security on all identified tables
DO $$
BEGIN
    PERFORM 1 FROM pg_tables WHERE schemaname='public' AND tablename='teacher_lesson_plans' AND rowsecurity;
    IF NOT FOUND THEN
        EXECUTE 'ALTER TABLE public.teacher_lesson_plans ENABLE ROW LEVEL SECURITY';
    END IF;

    PERFORM 1 FROM pg_tables WHERE schemaname='public' AND tablename='teacher_favorites' AND rowsecurity;
    IF NOT FOUND THEN
        EXECUTE 'ALTER TABLE public.teacher_favorites ENABLE ROW LEVEL SECURITY';
    END IF;

    PERFORM 1 FROM pg_tables WHERE schemaname='public' AND tablename='beta_feedback' AND rowsecurity;
    IF NOT FOUND THEN
        EXECUTE 'ALTER TABLE public.beta_feedback ENABLE ROW LEVEL SECURITY';
    END IF;

    PERFORM 1 FROM pg_tables WHERE schemaname='public' AND tablename='bmad_deployment_queue' AND rowsecurity;
    IF NOT FOUND THEN
        EXECUTE 'ALTER TABLE public.bmad_deployment_queue ENABLE ROW LEVEL SECURITY';
    END IF;

    PERFORM 1 FROM pg_tables WHERE schemaname='public' AND tablename='content_audit_results' AND rowsecurity;
    IF NOT FOUND THEN
        EXECUTE 'ALTER TABLE public.content_audit_results ENABLE ROW LEVEL SECURITY';
    END IF;

    PERFORM 1 FROM pg_tables WHERE schemaname='public' AND tablename='deployment_summary' AND rowsecurity;
    IF NOT FOUND THEN
        EXECUTE 'ALTER TABLE public.deployment_summary ENABLE ROW LEVEL SECURITY';
    END IF;
END $$;

-- ============================================
-- 3. CREATE BASIC RLS POLICIES
-- ============================================

-- Create permissive policies for now (can be refined later)
-- These allow all operations - you should customize based on your security needs

-- Teacher lesson plans - allow all for authenticated users
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE schemaname='public' AND tablename='teacher_lesson_plans' AND policyname='Allow all operations on teacher_lesson_plans'
    ) THEN
        EXECUTE $$CREATE POLICY "Allow all operations on teacher_lesson_plans" ON public.teacher_lesson_plans FOR ALL TO authenticated USING (true) WITH CHECK (true)$$;
    END IF;
END $$;

-- Teacher favorites - allow all for authenticated users  
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE schemaname='public' AND tablename='teacher_favorites' AND policyname='Allow all operations on teacher_favorites'
    ) THEN
        EXECUTE $$CREATE POLICY "Allow all operations on teacher_favorites" ON public.teacher_favorites FOR ALL TO authenticated USING (true) WITH CHECK (true)$$;
    END IF;
END $$;

-- Beta feedback - allow all for authenticated users
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE schemaname='public' AND tablename='beta_feedback' AND policyname='Allow all operations on beta_feedback'
    ) THEN
        EXECUTE $$CREATE POLICY "Allow all operations on beta_feedback" ON public.beta_feedback FOR ALL TO authenticated USING (true) WITH CHECK (true)$$;
    END IF;
END $$;

-- BMAD deployment queue - allow all for authenticated users
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE schemaname='public' AND tablename='bmad_deployment_queue' AND policyname='Allow all operations on bmad_deployment_queue'
    ) THEN
        EXECUTE $$CREATE POLICY "Allow all operations on bmad_deployment_queue" ON public.bmad_deployment_queue FOR ALL TO authenticated USING (true) WITH CHECK (true)$$;
    END IF;
END $$;

-- Content audit results - allow all for authenticated users
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE schemaname='public' AND tablename='content_audit_results' AND policyname='Allow all operations on content_audit_results'
    ) THEN
        EXECUTE $$CREATE POLICY "Allow all operations on content_audit_results" ON public.content_audit_results FOR ALL TO authenticated USING (true) WITH CHECK (true)$$;
    END IF;
END $$;

-- Deployment summary - allow all for authenticated users
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE schemaname='public' AND tablename='deployment_summary' AND policyname='Allow all operations on deployment_summary'
    ) THEN
        EXECUTE $$CREATE POLICY "Allow all operations on deployment_summary" ON public.deployment_summary FOR ALL TO authenticated USING (true) WITH CHECK (true)$$;
    END IF;
END $$;

-- ============================================
-- 4. VERIFICATION QUERIES
-- ============================================

-- Check that views have security_invoker set
SELECT 
  n.nspname AS schema,
  c.relname AS view,
  c.relkind,
  c.reloptions
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
  AND c.relkind IN ('v','m')
  AND c.relname IN ('featured_resources', 'user_kete_view', 'graphrag_summary');

-- Check that RLS is enabled on tables
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
);

-- Check RLS policies exist
SELECT 
    schemaname,
    tablename,
    policyname,
    permissive,
    roles,
    cmd,
    qual
FROM pg_policies 
WHERE schemaname = 'public'
AND tablename IN (
    'teacher_lesson_plans',
    'teacher_favorites', 
    'beta_feedback',
    'bmad_deployment_queue',
    'content_audit_results',
    'deployment_summary'
)
ORDER BY tablename, policyname;
