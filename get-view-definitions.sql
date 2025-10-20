-- Get current view metadata and security flags
-- This will help confirm security_invoker settings

-- Get view definitions for the problematic views
-- In Postgres 15+, security_invoker is stored in reloptions
SELECT 
  n.nspname   AS schema,
  c.relname   AS view,
  c.relkind,
  c.reloptions
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public'
  AND c.relkind IN ('v','m')
  AND c.relname IN ('featured_resources', 'user_kete_view', 'graphrag_summary')
ORDER BY c.relname;

-- Also check if these views exist and their current structure
SELECT 
    table_name,
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns 
WHERE table_schema = 'public' 
AND table_name IN ('featured_resources', 'user_kete_view', 'graphrag_summary')
ORDER BY table_name, ordinal_position;

-- Check current RLS status on tables
SELECT 
    schemaname,
    tablename,
    rowsecurity as rls_enabled,
    hasindexes,
    hasrules,
    hastriggers
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
