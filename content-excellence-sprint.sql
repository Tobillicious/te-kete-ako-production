-- CONTENT EXCELLENCE SPRINT - PHASE 1: DISCOVERY
-- Identify top-quality resources for cultural enhancement

-- ============================================
-- 1. IDENTIFY TARGET RESOURCES
-- ============================================

-- Find high-quality resources (90+ score) with cultural integration potential
SELECT 
    id,
    title,
    file_path,
    content_type,
    quality_score,
    cultural_level,
    (quality_score + cultural_level) as combined_score
FROM graphrag_resources 
WHERE quality_score >= 90 
AND cultural_level < 80  -- Need cultural enhancement
ORDER BY quality_score DESC, cultural_level ASC
LIMIT 25;

-- ============================================
-- 2. CULTURAL INTEGRATION OPPORTUNITIES
-- ============================================

-- Find resources with high quality but low cultural integration
SELECT 
    content_type,
    COUNT(*) as resource_count,
    AVG(quality_score) as avg_quality,
    AVG(cultural_level) as avg_cultural,
    AVG(quality_score - cultural_level) as enhancement_potential
FROM graphrag_resources 
WHERE quality_score >= 85
GROUP BY content_type
ORDER BY enhancement_potential DESC;

-- ============================================
-- 3. EXISTING CULTURAL EXCELLENCE PATTERNS
-- ============================================

-- Find resources that already have high cultural integration for pattern analysis
SELECT 
    title,
    file_path,
    cultural_level,
    quality_score,
    LEFT(content, 200) as content_preview
FROM graphrag_resources 
WHERE cultural_level >= 90 
AND quality_score >= 90
ORDER BY cultural_level DESC, quality_score DESC
LIMIT 15;

-- ============================================
-- 4. SUBJECT-SPECIFIC OPPORTUNITIES
-- ============================================

-- Identify subjects with high quality but low cultural integration
SELECT 
    CASE 
        WHEN file_path LIKE '%math%' OR title ILIKE '%math%' THEN 'Mathematics'
        WHEN file_path LIKE '%science%' OR title ILIKE '%science%' THEN 'Science'
        WHEN file_path LIKE '%english%' OR title ILIKE '%english%' THEN 'English'
        WHEN file_path LIKE '%social%' OR title ILIKE '%social%' THEN 'Social Studies'
        WHEN file_path LIKE '%digital%' OR title ILIKE '%digital%' THEN 'Digital Technologies'
        ELSE 'Other'
    END as subject_area,
    COUNT(*) as resource_count,
    AVG(quality_score) as avg_quality,
    AVG(cultural_level) as avg_cultural,
    AVG(quality_score - cultural_level) as enhancement_potential
FROM graphrag_resources 
WHERE quality_score >= 85
GROUP BY subject_area
ORDER BY enhancement_potential DESC;

-- ============================================
-- 5. RELATIONSHIP OPPORTUNITIES
-- ============================================

-- Find relationship types that could connect cultural concepts
SELECT 
    relationship_type,
    COUNT(*) as relationship_count,
    AVG(confidence) as avg_confidence
FROM graphrag_relationships 
WHERE relationship_type ILIKE '%cultural%' 
   OR relationship_type ILIKE '%māori%'
   OR relationship_type ILIKE '%indigenous%'
   OR relationship_type ILIKE '%traditional%'
GROUP BY relationship_type
ORDER BY relationship_count DESC;

-- ============================================
-- 6. LOG SPRINT INITIATION
-- ============================================

-- Log our Content Excellence Sprint start
INSERT INTO agent_coordination (
    agent_id,
    agent_name,
    status,
    current_task,
    task_started_at,
    estimated_completion,
    files_being_edited
) VALUES (
    'content-excellence-specialist',
    'Content Excellence Specialist',
    'working',
    'Content Excellence Sprint: Enhance 20+ high-quality resources with cultural integration',
    NOW(),
    NOW() + INTERVAL '3 hours',
    ARRAY['content-excellence-sprint.sql', 'SPRINT-KICKOFF-EXECUTION.md']
);

-- Log our approach to agent_knowledge
INSERT INTO agent_knowledge (
    agent_id,
    knowledge_type,
    knowledge_content,
    confidence,
    verified
) VALUES (
    'content-excellence-specialist',
    'sprint_execution',
    'Content Excellence Sprint initiated: Targeting 20+ resources with 90+ quality scores but <80 cultural integration. Focus on Mathematics, Science, English, Social Studies, and Digital Technologies. Goal: Transform excellence into culturally rich learning experiences.',
    0.95,
    true
);

-- ============================================
-- 7. SPRINT READINESS CHECK
-- ============================================

-- Verify we have the data needed for the sprint
SELECT 
    'Content Excellence Sprint Ready' as status,
    COUNT(*) as high_quality_resources,
    AVG(quality_score) as avg_quality,
    AVG(cultural_level) as avg_cultural,
    NOW() as sprint_started;
