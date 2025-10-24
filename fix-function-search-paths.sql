-- ================================================================
-- FIX SPECIFIC FUNCTION SEARCH PATH MUTABLE WARNINGS
-- ================================================================
-- 
-- Based on database linter results from Oct 24, 2025
-- Fixes 4 specific functions identified with mutable search paths
-- 
-- ================================================================

-- 1. Fix get_orphaned_resources function
ALTER FUNCTION public.get_orphaned_resources() SET search_path = public, pg_temp;

-- 2. Fix complete_task function  
ALTER FUNCTION public.complete_task(task_id UUID) SET search_path = public, pg_temp;

-- 3. Fix assign_task function
ALTER FUNCTION public.assign_task(task_data JSONB) SET search_path = public, pg_temp;

-- 4. Fix record_validation function
ALTER FUNCTION public.record_validation(resource_id UUID, validation_status TEXT, validator_id UUID) SET search_path = public, pg_temp;

-- ================================================================
-- VERIFICATION QUERIES
-- ================================================================
-- 
-- Run these to verify the fixes were applied:
-- 
-- SELECT proname, prosrc FROM pg_proc WHERE proname IN (
--     'get_orphaned_resources', 
--     'complete_task', 
--     'assign_task', 
--     'record_validation'
-- ) AND pronamespace = 'public'::regnamespace;
-- 
-- ================================================================

-- Success! These 4 function search path warnings should now be resolved.