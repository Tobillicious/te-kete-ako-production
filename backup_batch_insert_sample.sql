-- BACKUP MIGRATION: BATCH INSERT SAMPLE
-- ============================================================================
-- This demonstrates the structure for batch-loading extracted backup files
-- Generated from: extract_backup_and_index.py output
-- 
-- PROCESS:
-- 1. Python script extracts 1,580 files → JSON catalog
-- 2. This SQL loads the catalog → graphrag_resources table
-- 3. Additional SQL steps build relationships & boost quality
-- 
-- EXPECTED: ~1,500 successfully inserted resources (some may be duplicates)
-- ============================================================================

-- SAMPLE BATCH: Lessons Directory (Representative sample)
INSERT INTO graphrag_resources (
    file_path,
    resource_type,
    title,
    quality_score,
    cultural_context,
    year_level,
    subject,
    canonical_subject,
    has_te_reo,
    has_whakataukī,
    content_preview,
    metadata,
    archive_status,
    is_backup,
    backup_type,
    created_at,
    updated_at
) VALUES
-- Mathematics Lessons
('/backup_before_css_migration/lessons/mathematics/algebra-fundamentals-y7.html', 'lesson', 'Algebra Fundamentals - Year 7', 78, true, 'Year 7', 'Mathematics', 'Mathematics', false, false, 'Introduce students to basic algebraic concepts including variables, expressions...', '{"subject":"Mathematics","year_level":"Year 7","content_type":"lesson","has_structure":true}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- Science Lessons with Cultural Integration
('/backup_before_css_migration/lessons/science/ecology-and-kaitiakitanga-y8.html', 'lesson', 'Ecology and Kaitiakitanga - Year 8', 85, true, 'Year 8', 'Science', 'Science', true, true, 'Explore ecological systems through the lens of mātauranga Māori and kaitiakitanga principles..', '{"subject":"Science","year_level":"Year 8","has_te_reo":true,"has_whakataukī":true,"cultural_integration":"kaitiakitanga"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- English Literacy
('/backup_before_css_migration/lessons/english/writing-for-purpose-y9.html', 'lesson', 'Writing for Purpose - Year 9', 82, true, 'Year 9', 'English', 'English', false, false, 'Develop writing skills for different audiences and purposes including narrative, persuasive, informative..', '{"subject":"English","year_level":"Year 9","content_type":"lesson","academic_level":"intermediate"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- Social Studies
('/backup_before_css_migration/lessons/social-studies/nz-history-treaty-y10.html', 'lesson', 'New Zealand History: Treaty of Waitangi - Year 10', 88, true, 'Year 10', 'Social Studies', 'Social Studies', true, true, 'Comprehensive exploration of the Treaty of Waitangi, its significance in NZ history, and contemporary implications..', '{"subject":"Social Studies","year_level":"Year 10","has_te_reo":true,"historical_focus":"treaty_of_waitangi"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- Digital Technologies
('/backup_before_css_migration/lessons/digital-tech/coding-fundamentals-python-y7.html', 'lesson', 'Coding Fundamentals with Python - Year 7', 80, true, 'Year 7', 'Digital Technologies', 'Digital Technologies', false, false, 'Introduction to programming concepts using Python: variables, loops, functions, debugging..', '{"subject":"Digital Technologies","year_level":"Year 7","programming_language":"python","content_type":"lesson"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- Te Reo Māori
('/backup_before_css_migration/lessons/te-reo/whakapapa-basics-y8.html', 'lesson', 'Whakapapa Basics - Year 8', 87, true, 'Year 8', 'Te Reo Māori', 'Te Reo Māori', true, true, 'Understand the concept of whakapapa - genealogy, genealogical connections, and their importance in Māori culture..', '{"subject":"Te Reo Māori","year_level":"Year 8","has_te_reo":true,"cultural_concept":"whakapapa"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- Arts
('/backup_before_css_migration/lessons/arts/visual-composition-y9.html', 'lesson', 'Visual Composition and Design - Year 9', 75, true, 'Year 9', 'Arts', 'Arts', false, false, 'Develop visual literacy skills: color theory, composition principles, design elements, critique..', '{"subject":"Arts","year_level":"Year 9","art_form":"visual","content_type":"lesson"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- Health & PE
('/backup_before_css_migration/lessons/health-pe/nutrition-wellness-y10.html', 'lesson', 'Nutrition and Wellness - Year 10', 79, true, 'Year 10', 'Health & PE', 'Health & PE', false, false, 'Explore healthy nutrition choices, dietary guidelines, relationship between health and lifestyle decisions..', '{"subject":"Health & PE","year_level":"Year 10","focus_area":"nutrition_wellness"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- SAMPLE HANDOUTS
('/backup_before_css_migration/handouts/mathematics/algebraic-expressions-worksheet.html', 'handout', 'Algebraic Expressions Worksheet', 72, true, 'Year 7', 'Mathematics', 'Mathematics', false, false, 'Practice worksheet for algebraic expression simplification with scaffolded difficulty levels..', '{"resource_type":"handout","content_type":"worksheet","difficulty":"scaffolded"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- SAMPLE UNITS
('/backup_before_css_migration/units/y8-ecosystem-unit.html', 'unit-plan', 'Year 8 Ecosystem Unit - Complete Learning Sequence', 90, true, 'Year 8', 'Science', 'Science', true, true, 'Comprehensive unit covering ecosystems, biodiversity, food webs, conservation, with cultural perspectives on land stewardship..', '{"unit_type":"full_sequence","duration_weeks":6,"has_assessments":true,"has_te_reo":true,"cultural_integration":"kaitiakitanga"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- SAMPLE GAMES
('/backup_before_css_migration/games/math-equation-quest.html', 'game', 'Equation Quest - Interactive Math Game', 76, true, 'Year 7', 'Mathematics', 'Mathematics', false, false, 'Gamified learning for equation solving with progressive difficulty and immediate feedback..', '{"game_type":"educational","subject":"Mathematics","mechanics":"solve_equations","engagement":"high"}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- SAMPLE ASSESSMENTS
('/backup_before_css_migration/assessments/algebra-formative-quiz.html', 'assessment', 'Algebra Fundamentals - Formative Quiz', 74, true, 'Year 7', 'Mathematics', 'Mathematics', false, false, 'Formative assessment for algebra basics: 15 questions covering variables, expressions, simple equations..', '{"assessment_type":"formative","num_questions":15,"time_limit_minutes":20,"auto_scoring":true}', 'active', true, 'pre_css_migration', NOW(), NOW()),

-- SAMPLE ACTIVITIES
('/backup_before_css_migration/activities/poetry-writing-workshop.html', 'activity', 'Poetry Writing Workshop', 81, true, 'Year 8', 'English', 'English', true, true, 'Structured creative writing activity: haiku and traditional Māori poetry forms combined..', '{"activity_type":"creative_writing","formats":["haiku","māori_poetry"],"collaborative":true,"duration_minutes":90}', 'active', true, 'pre_css_migration', NOW(), NOW())

ON CONFLICT (file_path) DO NOTHING;

-- ============================================================================
-- QUALITY VERIFICATION AFTER INSERT
-- ============================================================================

-- Check insert results
SELECT 
    'Backup Resources Indexed' as check_name,
    COUNT(*) as resource_count,
    COUNT(CASE WHEN quality_score >= 90 THEN 1 END) as gold_standard,
    COUNT(CASE WHEN quality_score >= 80 THEN 1 END) as high_quality,
    ROUND(AVG(quality_score), 1) as avg_quality,
    COUNT(DISTINCT subject) as subjects_covered,
    COUNT(DISTINCT year_level) as year_levels_covered
FROM graphrag_resources
WHERE is_backup = true;

-- ============================================================================
-- PROFILE BY CONTENT TYPE
-- ============================================================================

SELECT 
    resource_type,
    COUNT(*) as count,
    ROUND(AVG(quality_score), 1) as avg_quality,
    COUNT(CASE WHEN has_te_reo = true THEN 1 END) as with_te_reo,
    COUNT(CASE WHEN has_whakataukī = true THEN 1 END) as with_whakataukī
FROM graphrag_resources
WHERE is_backup = true
GROUP BY resource_type
ORDER BY count DESC;

-- ============================================================================
-- PROFILE BY SUBJECT
-- ============================================================================

SELECT 
    subject,
    COUNT(*) as resource_count,
    COUNT(DISTINCT year_level) as year_levels,
    ROUND(AVG(quality_score), 1) as avg_quality,
    COUNT(CASE WHEN quality_score >= 90 THEN 1 END) as gold_standard
FROM graphrag_resources
WHERE is_backup = true
GROUP BY subject
ORDER BY resource_count DESC;

-- ============================================================================
-- YEAR LEVEL PROGRESSION CHECK
-- Find subjects with complete Y7-Y13 coverage (complete learning pathways)
-- ============================================================================

WITH subject_year_coverage AS (
    SELECT 
        subject,
        COUNT(DISTINCT year_level) as unique_years,
        STRING_AGG(DISTINCT year_level, ', ' ORDER BY year_level) as years_covered,
        COUNT(DISTINCT file_path) as total_resources
    FROM graphrag_resources
    WHERE is_backup = true
    GROUP BY subject
)
SELECT 
    subject,
    unique_years,
    years_covered,
    total_resources,
    CASE 
        WHEN unique_years >= 5 THEN 'Complete pathway potential'
        WHEN unique_years >= 3 THEN 'Partial pathway'
        ELSE 'Limited coverage'
    END as pathway_status
FROM subject_year_coverage
ORDER BY unique_years DESC;

-- ============================================================================
-- CULTURAL INTEGRATION SUMMARY
-- ============================================================================

SELECT 
    'Cultural Integration Status' as metric,
    COUNT(*) as total_backup_resources,
    COUNT(CASE WHEN has_te_reo = true THEN 1 END) as with_te_reo,
    ROUND(100.0 * COUNT(CASE WHEN has_te_reo = true THEN 1 END) / COUNT(*), 1) as pct_te_reo,
    COUNT(CASE WHEN has_whakataukī = true THEN 1 END) as with_whakataukī,
    ROUND(100.0 * COUNT(CASE WHEN has_whakataukī = true THEN 1 END) / COUNT(*), 1) as pct_whakataukī
FROM graphrag_resources
WHERE is_backup = true;

-- ============================================================================
-- QUALITY SCORE DISTRIBUTION
-- ============================================================================

SELECT 
    CASE 
        WHEN quality_score >= 90 THEN '90-100 (Gold Standard)'
        WHEN quality_score >= 80 THEN '80-89 (High Quality)'
        WHEN quality_score >= 70 THEN '70-79 (Good Quality)'
        ELSE '< 70 (Fair Quality)'
    END as quality_band,
    COUNT(*) as resource_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 1) as percentage
FROM graphrag_resources
WHERE is_backup = true
GROUP BY quality_band
ORDER BY quality_band DESC;
