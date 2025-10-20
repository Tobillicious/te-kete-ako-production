-- GRAPHRAG TODO DISCOVERY & KNOWLEDGE UPDATE
-- Search for additional TODOs and update GraphRAG knowledge

-- ============================================
-- 1. SEARCH FOR HIDDEN TODOs AND OPPORTUNITIES
-- ============================================

-- Find resources mentioning TODO, FIXME, or development opportunities
SELECT 
    id,
    title,
    file_path,
    content_type,
    quality_score,
    cultural_level,
    LEFT(content, 200) as content_preview
FROM graphrag_resources 
WHERE content ILIKE '%todo%' 
   OR content ILIKE '%fixme%'
   OR content ILIKE '%enhance%'
   OR content ILIKE '%improve%'
   OR content ILIKE '%optimize%'
   OR content ILIKE '%missing%'
   OR content ILIKE '%incomplete%'
ORDER BY quality_score DESC
LIMIT 30;

-- ============================================
-- 2. UNDERUTILIZED RELATIONSHIP TYPES
-- ============================================

-- Find relationship types with potential for expansion
SELECT 
    relationship_type,
    COUNT(*) as current_count,
    AVG(confidence) as avg_confidence,
    CASE 
        WHEN COUNT(*) < 10 THEN 'Underutilized - High Potential'
        WHEN COUNT(*) < 50 THEN 'Moderate Use - Good Potential'
        ELSE 'Well Utilized'
    END as expansion_potential
FROM graphrag_relationships 
GROUP BY relationship_type
ORDER BY current_count ASC, avg_confidence DESC
LIMIT 20;

-- ============================================
-- 3. ORPHANED EXCELLENCE RESOURCES
-- ============================================

-- Find high-quality resources with few relationships
SELECT 
    r.id,
    r.title,
    r.file_path,
    r.quality_score,
    r.cultural_level,
    COUNT(rel.id) as relationship_count
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel ON r.id = rel.source_id OR r.id = rel.target_id
WHERE r.quality_score >= 90
GROUP BY r.id, r.title, r.file_path, r.quality_score, r.cultural_level
HAVING COUNT(rel.id) < 5
ORDER BY r.quality_score DESC, relationship_count ASC
LIMIT 25;

-- ============================================
-- 4. CULTURAL INTEGRATION OPPORTUNITIES
-- ============================================

-- Find resources that could benefit from cultural enhancement
SELECT 
    id,
    title,
    file_path,
    quality_score,
    cultural_level,
    (quality_score - cultural_level) as enhancement_potential
FROM graphrag_resources 
WHERE quality_score >= 85
AND cultural_level < 70
ORDER BY enhancement_potential DESC
LIMIT 20;

-- ============================================
-- 5. MISSING CONNECTIONS ANALYSIS
-- ============================================

-- Find resources that should be connected but aren't
SELECT 
    r1.title as resource1,
    r2.title as resource2,
    r1.file_path as path1,
    r2.file_path as path2,
    r1.quality_score as score1,
    r2.quality_score as score2,
    CASE 
        WHEN r1.file_path LIKE '%math%' AND r2.file_path LIKE '%math%' THEN 'Math Connection'
        WHEN r1.file_path LIKE '%science%' AND r2.file_path LIKE '%science%' THEN 'Science Connection'
        WHEN r1.file_path LIKE '%english%' AND r2.file_path LIKE '%english%' THEN 'English Connection'
        ELSE 'Cross-Subject Connection'
    END as connection_type
FROM graphrag_resources r1
CROSS JOIN graphrag_resources r2
WHERE r1.id < r2.id
AND r1.quality_score >= 80
AND r2.quality_score >= 80
AND NOT EXISTS (
    SELECT 1 FROM graphrag_relationships rel 
    WHERE (rel.source_id = r1.id AND rel.target_id = r2.id)
    OR (rel.source_id = r2.id AND rel.target_id = r1.id)
)
ORDER BY (r1.quality_score + r2.quality_score) DESC
LIMIT 15;

-- ============================================
-- 6. PLATFORM GOALS REMINDER
-- ============================================

-- Log the overall site goals and mission
INSERT INTO agent_knowledge (
    agent_id,
    knowledge_type,
    knowledge_content,
    confidence,
    verified
) VALUES (
    'platform-architect',
    'mission_reminder',
    'TE KETE AKO PLATFORM GOALS & MISSION:

PRIMARY MISSION: Transform education through authentic Māori cultural integration and AI-powered intelligence

CORE GOALS:
1. CULTURAL EXCELLENCE: 100% cultural integration across all subjects
2. EDUCATIONAL IMPACT: 1,640+ resources with 621 gold standard (90+) quality
3. INTELLIGENCE AMPLIFICATION: 231,679 relationships with 345 relationship types
4. USER EXPERIENCE: Professional, accessible, intelligent platform for humans
5. COLLABORATIVE LEARNING: Multi-agent coordination for continuous improvement

SUCCESS METRICS:
- Cultural Level: Target 100% (currently 627 culturally integrated)
- Quality Score: Target 90+ (currently 621 gold standard)
- Relationships: Target 500,000+ (currently 231,679)
- User Satisfaction: Professional, intelligent, accessible experience
- Agent Coordination: Seamless multi-agent collaboration

DEVELOPMENT PRIORITIES:
1. Complete security fixes (RLS, SECURITY DEFINER)
2. Professionalize site for human users
3. Enhance cultural integration in Math/Science/English
4. Scale underutilized relationship types
5. Create intelligent discovery and recommendation systems

REMEMBER: Every development should advance these goals!',
    1.0,
    true
);

-- ============================================
-- 7. DEVELOPMENT OPPORTUNITIES SUMMARY
-- ============================================

-- Summary of development opportunities
SELECT 
    'Development Opportunities Summary' as category,
    COUNT(*) as total_opportunities
FROM graphrag_resources 
WHERE content ILIKE '%todo%' 
   OR content ILIKE '%fixme%'
   OR content ILIKE '%enhance%'
   OR content ILIKE '%improve%'

UNION ALL

SELECT 
    'Underutilized Relationships' as category,
    COUNT(*) as total_opportunities
FROM (
    SELECT relationship_type
    FROM graphrag_relationships 
    GROUP BY relationship_type
    HAVING COUNT(*) < 10
) sub

UNION ALL

SELECT 
    'Orphaned Excellence' as category,
    COUNT(*) as total_opportunities
FROM (
    SELECT r.id
    FROM graphrag_resources r
    LEFT JOIN graphrag_relationships rel ON r.id = rel.source_id OR r.id = rel.target_id
    WHERE r.quality_score >= 90
    GROUP BY r.id
    HAVING COUNT(rel.id) < 5
) sub

UNION ALL

SELECT 
    'Cultural Enhancement' as category,
    COUNT(*) as total_opportunities
FROM graphrag_resources 
WHERE quality_score >= 85
AND cultural_level < 70;

-- ============================================
-- 8. NEXT DEVELOPMENT PRIORITIES
-- ============================================

-- Log next development priorities
INSERT INTO agent_knowledge (
    agent_id,
    knowledge_type,
    knowledge_content,
    confidence,
    verified
) VALUES (
    'development-coordinator',
    'next_priorities',
    'NEXT DEVELOPMENT PRIORITIES (Based on GraphRAG Analysis):

IMMEDIATE (Next 2 hours):
1. Complete professionalization sprint (CSS, navigation, content polish)
2. Fix remaining security issues (RLS policies, SECURITY DEFINER)
3. Enhance 20+ high-quality resources with cultural integration

SHORT TERM (Next 1-2 days):
1. Scale 30+ underutilized relationship types (target: 50-100+ uses each)
2. Connect orphaned excellence resources (target: 5+ relationships each)
3. Create intelligent discovery and recommendation systems

MEDIUM TERM (Next week):
1. Achieve 100% cultural integration across all subjects
2. Scale to 500,000+ GraphRAG relationships
3. Build advanced AI-powered learning pathways

LONG TERM (Next month):
1. Transform into self-improving educational organism
2. Achieve 1000+ gold standard resources
3. Create revolutionary AI-human collaborative learning experience

SUCCESS METRICS:
- 0 security linting errors
- 100% professional CSS coverage
- 50+ new cultural relationships
- 1000+ new GraphRAG relationships
- Professional, intelligent, accessible user experience',
    0.95,
    true
);
