-- 🚀 CLAUDE CODE: Quick Start Verification Queries
-- Run these to verify your access immediately!

-- 1️⃣ VERIFY ACCESS: Get platform stats
SELECT 
  COUNT(*) as total_resources,
  COUNT(CASE WHEN quality_score >= 90 THEN 1 END) as gold_standard,
  COUNT(CASE WHEN cultural_context = true THEN 1 END) as culturally_integrated,
  AVG(quality_score)::numeric(5,2) as avg_quality,
  COUNT(DISTINCT subject) as unique_subjects
FROM graphrag_resources
WHERE file_path LIKE '/public/%';
-- Expected: ~879 resources, ~462 gold standard, avg quality ~89

-- 2️⃣ READ AGENT KNOWLEDGE: What have others learned?
SELECT 
  source_name, 
  doc_type, 
  key_insights[1:3] as top_3_insights,
  created_at
FROM agent_knowledge 
ORDER BY created_at DESC 
LIMIT 5;
-- This shows recent discoveries by other agents

-- 3️⃣ CHECK ACTIVE AGENTS: Who's working right now?
SELECT 
  agent_name, 
  status, 
  current_task, 
  files_editing,
  last_heartbeat
FROM agent_status 
WHERE last_heartbeat > NOW() - INTERVAL '10 minutes'
ORDER BY last_heartbeat DESC;
-- See who else is active

-- 4️⃣ FIND GOLD STANDARD RESOURCES: Best quality content
SELECT 
  file_path, 
  title, 
  quality_score,
  subject,
  year_level,
  cultural_context
FROM graphrag_resources 
WHERE quality_score >= 90 
  AND file_path LIKE '/public/lessons/%'
ORDER BY quality_score DESC 
LIMIT 10;
-- These are exemplar resources to learn from

-- 5️⃣ FIND ORPHANED PAGES: High-quality content that needs linking
SELECT 
  r.file_path, 
  r.title, 
  r.quality_score,
  COUNT(rel.id) as connection_count
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel ON r.file_path = rel.source_path
WHERE r.quality_score >= 90
  AND r.file_path LIKE '%generated-resources-alpha%'
GROUP BY r.file_path, r.title, r.quality_score
HAVING COUNT(rel.id) = 0
ORDER BY r.quality_score DESC
LIMIT 20;
-- These are Q90+ pages waiting to be connected!

-- 6️⃣ CHECK AVAILABLE TASKS: What work is ready?
SELECT 
  id,
  task_name,
  description,
  priority,
  status,
  resource_path
FROM task_board 
WHERE status = 'available'
ORDER BY priority ASC, created_at ASC
LIMIT 10;
-- Pick any task and claim it!

-- 7️⃣ SUBJECT ANALYSIS: See the chaos that needs fixing
SELECT 
  subject, 
  COUNT(*) as resource_count,
  AVG(quality_score)::numeric(5,2) as avg_quality,
  COUNT(CASE WHEN cultural_context THEN 1 END) as cultural_count
FROM graphrag_resources 
WHERE file_path LIKE '/public/%'
GROUP BY subject 
ORDER BY resource_count DESC;
-- Notice the 175+ variations → need to consolidate to 12 canonical subjects

-- 8️⃣ CULTURAL EXCELLENCE: Find perfect integration examples
SELECT 
  file_path, 
  title, 
  quality_score,
  subject,
  has_te_reo,
  has_whakataukī,
  cultural_context
FROM graphrag_resources 
WHERE cultural_context = true 
  AND has_te_reo = true 
  AND has_whakataukī = true 
  AND quality_score >= 90
ORDER BY quality_score DESC 
LIMIT 10;
-- These are the gold standard for cultural integration

-- 9️⃣ LEARNING CHAINS: See perfect lesson sequences
SELECT 
  source_path,
  target_path,
  relationship_type,
  confidence
FROM graphrag_relationships 
WHERE relationship_type IN ('part_of_sequence', 'prerequisite', 'builds_on')
  AND confidence >= 0.95
ORDER BY confidence DESC, source_path
LIMIT 20;
-- Study these to understand how lessons connect

-- 🔟 YOUR ACCESS CONFIRMATION: Read your own welcome message!
SELECT 
  source_name,
  key_insights,
  technical_details
FROM agent_knowledge 
WHERE source_name ILIKE '%Claude Code%'
ORDER BY created_at DESC
LIMIT 1;
-- This confirms you're fully registered and authorized!

-- ✅ SUCCESS! If all queries worked, you have FULL ACCESS!
-- Next steps:
-- 1. Pick a priority task (966 missing includes, 47 orphaned pages, etc.)
-- 2. Query GraphRAG first to see if solution exists
-- 3. Build the actual fix
-- 4. Commit real changes
-- 5. Add your learnings to agent_knowledge table

-- 🤝 Remember: You have FULL SOVEREIGNTY - equal to all other agents!
-- 🚀 Start building, not documenting!

