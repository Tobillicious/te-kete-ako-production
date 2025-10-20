-- ==============================
-- SECURITY DISCOVERY & LOGGING
-- ==============================

-- Discovery: find resources discussing RLS or SECURITY DEFINER
-- Run this in Supabase SQL Editor
SELECT id, title, file_path
FROM graphrag_resources
WHERE lower(content) LIKE '%row level security%'
   OR lower(content) LIKE '%rls%'
   OR lower(content) LIKE '%security definer%'
ORDER BY id DESC
LIMIT 50;

-- Log: record our fixes to agent_knowledge for team visibility
-- Ensure agent_knowledge exists with columns: agent_id, knowledge_type, knowledge_content, confidence, verified
INSERT INTO agent_knowledge (agent_id, knowledge_type, knowledge_content, confidence, verified)
VALUES (
  'GPT-5-Cursor',
  'security_fix',
  'Applied idempotent security fixes: set security_invoker=true on views (featured_resources, user_kete_view, graphrag_summary). Enabled RLS and created idempotent permissive policies on teacher_lesson_plans, teacher_favorites, beta_feedback, bmad_deployment_queue, content_audit_results, deployment_summary. Next: tighten policies with per-user and role constraints.',
  0.95,
  true
);
-- =============================================================
-- GRAPHRAG LIVE QUERIES AND ACTION TEMPLATES (Oct 20, 2025)
-- Use with MCP Supabase executor. Do not run in local terminal.
-- =============================================================

-- 1) SUPER-HUBS (>= 100 connections)
-- Purpose: Build FROM these for 100x impact
-- Output: Top 20 hubs with connection counts
SELECT r.file_path,
       r.title,
       r.subject,
       r.quality_score,
       COUNT(rel.id) AS connections
FROM graphrag_resources r
JOIN graphrag_relationships rel
  ON r.file_path = rel.source_path OR r.file_path = rel.target_path
GROUP BY r.file_path, r.title, r.subject, r.quality_score
HAVING COUNT(rel.id) >= 100
ORDER BY connections DESC
LIMIT 20;

-- 2) ORPHANED GEMS (Q90+ with < 5 connections)
-- Purpose: Low effort, high impact linking
-- Output: Top 50 highest-quality under-connected resources
SELECT r.file_path,
       r.title,
       r.subject,
       r.year_level,
       r.quality_score,
       COALESCE(COUNT(rel.id), 0) AS connections
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel
  ON r.file_path = rel.source_path OR r.file_path = rel.target_path
WHERE r.quality_score >= 90
GROUP BY r.file_path, r.title, r.subject, r.year_level, r.quality_score
HAVING COALESCE(COUNT(rel.id), 0) < 5
ORDER BY r.quality_score DESC, connections ASC
LIMIT 50;

-- 3) YEAR BRIDGE COVERAGE (prerequisite_for across year levels)
-- Purpose: Identify weak bridges (e.g., Y11→Y12→Y13)
SELECT source_year_level,
       target_year_level,
       COUNT(*) AS bridge_count,
       ROUND(AVG(confidence)::numeric, 3) AS avg_confidence
FROM graphrag_relationships
WHERE relationship_type = 'prerequisite_for'
  AND source_year_level IS NOT NULL
  AND target_year_level IS NOT NULL
  AND source_year_level <> target_year_level
GROUP BY source_year_level, target_year_level
ORDER BY bridge_count ASC;

-- 4) UNDERUTILIZED RELATIONSHIP TYPES
-- Purpose: Scale one-off successes (target >= 100 uses)
SELECT relationship_type,
       COUNT(*) AS usage_count,
       ROUND(AVG(confidence)::numeric, 3) AS avg_confidence
FROM graphrag_relationships
GROUP BY relationship_type
HAVING COUNT(*) < 10
ORDER BY usage_count ASC, avg_confidence DESC;

-- 5) ACTION TEMPLATE: CREATE Y11→Y13 PREREQUISITE BRIDGES
-- Replace :SUBJECT with a canonical subject (e.g., 'Science' or 'Mathematics')
-- Replace :LIMIT with desired number to create (e.g., 30)
-- NOTE: Review candidates before executing the INSERT
WITH candidates AS (
  SELECT s.file_path AS source_path,
         t.file_path AS target_path,
         0.92::float AS confidence,
         jsonb_build_object(
           'reason', 'Year progression bridge',
           'source_title', s.title,
           'target_title', t.title,
           'builder', 'automated-template',
           'created_at', NOW()
         ) AS metadata
  FROM graphrag_resources s
  JOIN graphrag_resources t
    ON s.subject = t.subject
   AND s.year_level = 'Y11'
   AND t.year_level IN ('Y12','Y13')
   AND s.subject = :SUBJECT
  WHERE s.quality_score >= 80
    AND t.quality_score >= 80
    AND s.file_path <> t.file_path
    AND NOT EXISTS (
      SELECT 1 FROM graphrag_relationships r
      WHERE r.source_path = s.file_path
        AND r.target_path = t.file_path
        AND r.relationship_type = 'prerequisite_for'
    )
  ORDER BY t.year_level ASC, t.quality_score DESC
  LIMIT :LIMIT
)
-- Preview
SELECT * FROM candidates;

-- Execute (uncomment to insert)
-- INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
-- SELECT source_path, target_path, 'prerequisite_for', confidence, metadata
-- FROM candidates;

-- 6) ACTION TEMPLATE: LINK ORPHANED Q90+ TO SUPER-HUBS
-- Purpose: Fast rescue by linking each orphan to 2 nearest hubs by subject
WITH hubs AS (
  SELECT r.file_path, r.subject
  FROM graphrag_resources r
  JOIN graphrag_relationships rel
    ON r.file_path = rel.source_path OR r.file_path = rel.target_path
  GROUP BY r.file_path, r.subject
  HAVING COUNT(rel.id) >= 100
),
orphans AS (
  SELECT r.file_path, r.subject
  FROM graphrag_resources r
  LEFT JOIN graphrag_relationships rel
    ON r.file_path = rel.source_path OR r.file_path = rel.target_path
  WHERE r.quality_score >= 90
  GROUP BY r.file_path, r.subject
  HAVING COALESCE(COUNT(rel.id), 0) < 5
),
pairings AS (
  SELECT o.file_path AS orphan_path,
         h.file_path AS hub_path,
         0.94::float AS confidence,
         jsonb_build_object('reason','orphan→hub link','created_at',NOW()) AS metadata,
         ROW_NUMBER() OVER (PARTITION BY o.file_path ORDER BY h.file_path) AS rn
  FROM orphans o
  JOIN hubs h ON h.subject = o.subject
)
-- Preview top 2 hub links per orphan
SELECT * FROM pairings WHERE rn <= 2;

-- Execute (uncomment to insert)
-- INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
-- SELECT orphan_path, hub_path, 'related_topic', confidence, metadata
-- FROM pairings
-- WHERE rn <= 2
-- ON CONFLICT DO NOTHING;

-- 7) ACTION TEMPLATE: SCALE UNDERUSED RELATIONSHIP TYPES (EXAMPLE)
-- Example shown for `critical_analysis` across Science lessons to analysis handouts
-- Adjust patterns to your repo schema/content paths
WITH lessons AS (
  SELECT file_path, title FROM graphrag_resources
  WHERE resource_type = 'lesson' AND subject = 'Science'
),
handouts AS (
  SELECT file_path, title FROM graphrag_resources
  WHERE resource_type = 'handout' AND title ILIKE '%analysis%'
),
matches AS (
  SELECT l.file_path AS source_path,
         h.file_path AS target_path,
         0.88::float AS confidence,
         jsonb_build_object('reason','scale critical_analysis','created_at',NOW()) AS metadata
  FROM lessons l
  JOIN handouts h ON TRUE
  WHERE NOT EXISTS (
    SELECT 1 FROM graphrag_relationships r
    WHERE r.source_path = l.file_path
      AND r.target_path = h.file_path
      AND r.relationship_type = 'critical_analysis'
  )
  LIMIT 100
)
-- Preview
SELECT * FROM matches;

-- Execute (uncomment to insert)
-- INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
-- SELECT source_path, target_path, 'critical_analysis', confidence, metadata
-- FROM matches
-- ON CONFLICT DO NOTHING;

-- End of file


