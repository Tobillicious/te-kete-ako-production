-- ============================================================================
-- SCIENCE CURRICULUM URL FIX
-- Date: October 30, 2025
-- Issue: 963 Science statements have NULL source URLs
-- Solution: Update with correct Tahurangi URLs based on pattern analysis
-- ============================================================================

-- Science Hub URL (confirmed from search)
-- https://newzealandcurriculum.tahurangi.education.govt.nz/new-zealand-curriculum-online/new-zealand-curriculum/learning-areas/science-curriculum/5637165588.c

-- Phase URLs (following pattern from other learning areas)
-- Pattern: .../nzc---[learning-area]-phase-[number]-years-[range]/[ID].p

-- PHASE 1: Update Science Phase 1 statements (Years 0-3)
UPDATE curriculum_statements 
SET tahurangi_url = 'https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---science-phase-1-years-0-3/[NEEDS_RESEARCH].p'
WHERE learning_area = 'Science' 
  AND phase = 'Phase 1' 
  AND tahurangi_url IS NULL;

-- PHASE 2: Update Science Phase 2 statements (Years 4-6)  
UPDATE curriculum_statements 
SET tahurangi_url = 'https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---science-phase-2-years-4-6/[NEEDS_RESEARCH].p'
WHERE learning_area = 'Science' 
  AND phase = 'Phase 2' 
  AND tahuranagi_url IS NULL;

-- PHASE 3: Update Science Phase 3 statements (Years 7-8)
UPDATE curriculum_statements 
SET tahurangi_url = 'https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---science-phase-3-years-7-8/[NEEDS_RESEARCH].p'
WHERE learning_area = 'Science' 
  AND phase = 'Phase 3' 
  AND tahurangi_url IS NULL;

-- PHASE 4: Update Science Phase 4 statements (Years 9-10)
UPDATE curriculum_statements 
SET tahurangi_url = 'https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---science-phase-4-years-9-10/[NEEDS_RESEARCH].p'
WHERE learning_area = 'Science' 
  AND phase = 'Phase 4' 
  AND tahurangi_url IS NULL;

-- ============================================================================
-- VERIFICATION QUERIES
-- ============================================================================

-- Check how many Science statements still have NULL URLs
SELECT 
    phase,
    COUNT(*) as statements_with_null_urls
FROM curriculum_statements 
WHERE learning_area = 'Science' 
  AND tahurangi_url IS NULL
GROUP BY phase
ORDER BY phase;

-- Check the URL pattern worked
SELECT 
    phase,
    tahurangi_url,
    COUNT(*) as statement_count
FROM curriculum_statements 
WHERE learning_area = 'Science' 
  AND tahurangi_url IS NOT NULL
GROUP BY phase, tahurangi_url
ORDER BY phase;

-- ============================================================================
-- NOTES
-- ============================================================================

/*
NEXT STEPS REQUIRED:
1. Research the actual Phase page IDs (currently marked as [NEEDS_RESEARCH])
2. Test URLs manually to ensure they work
3. Run these UPDATE statements with correct IDs
4. Verify all 963 Science statements now have proper URLs

URL PATTERN ANALYSIS:
- Health & PE Phase 4: .../nzc---health-and-pe-phase-4/5637293085.p
- The Arts Phase 1: .../nzc---the-arts-phase-1-years-0-3/5637292334.p
- Technology Phase 1: .../technology-phase-1/5637296077.p

Science should follow: .../nzc---science-phase-[1-4]-years-[range]/[ID].p

VERIFICATION STATUS:
- Science Hub found: ✅ 5637165588.c
- Phase 1 ID: ❌ Needs research
- Phase 2 ID: ❌ Needs research  
- Phase 3 ID: ❌ Needs research
- Phase 4 ID: ❌ Needs research

This fix addresses the critical metadata gap for 963 Science statements.
*/