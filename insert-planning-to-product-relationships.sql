-- ═══════════════════════════════════════════════════════════════════════════
-- GRAPHRAG PLANNING → PRODUCT RELATIONSHIPS
-- Maps MD planning documents to actual products/features created
-- Purpose: Show WHAT was built FROM each planning document
-- ═══════════════════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 1: INSERT PRODUCTS AS RESOURCES (If not already in GraphRAG)
-- ═══════════════════════════════════════════════════════════════════════════

-- Navigation Products
INSERT INTO resources (title, type, path, description, quality_score, metadata)
VALUES 
  ('Navigation Standard Component',
   'Navigation Component',
   '/public/components/navigation-standard.html',
   'Most-used navigation component: Clean teacher workflow, mobile responsive, professional appearance',
   95,
   '{"product_type": "navigation", "usage": "primary", "features": ["teacher_workflow", "mobile_responsive"]}'::jsonb),
  
  ('Navigation Unified Component',
   'Navigation Component',
   '/public/components/navigation-unified.html',
   'Unified navigation merging 4 systems: Standard + Hegelian + Mega Menu + AI features',
   92,
   '{"product_type": "navigation", "merged_from": 4, "features": ["dropdowns", "year_levels", "graphrag"]}'::jsonb),
  
  ('Navigation Year Dropdown Component',
   'Navigation Component',
   '/public/components/navigation-year-dropdown.html',
   'Year-level organization navigation: Year 7-13 with unit grouping',
   90,
   '{"product_type": "navigation", "organization": "year_level", "supports": "content_hierarchy"}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- Dashboard Products
INSERT INTO resources (title, type, path, description, quality_score, metadata)
VALUES 
  ('Teacher Dashboard Unified',
   'Dashboard Page',
   '/public/teacher-dashboard-unified.html',
   'CRITICAL: Unified teacher dashboard with analytics, resource library, planning tools - implements Teacher Experience Design spec',
   98,
   '{"product_type": "dashboard", "role": "teacher", "features": ["analytics", "resource_library", "planning_tools"], "implements": "teacher_experience_design"}'::jsonb),
  
  ('Teacher Dashboard AI',
   'AI Dashboard',
   '/public/teacher-dashboard-ai.html',
   'AI-powered teacher dashboard: DeepSeek integration, cultural intelligence, GraphRAG recommendations',
   96,
   '{"product_type": "ai_dashboard", "role": "teacher", "ai_features": ["deepseek", "cultural_intelligence", "graphrag"], "implements": "ai_orchestration"}'::jsonb),
  
  ('Teacher AI Intelligence Hub',
   'AI Feature Page',
   '/public/teacher-ai-intelligence-hub.html',
   'CRITICAL: AI orchestration hub with 5 AI agents - Learning Pathfinder, Content Curator, Cultural Guardian, Engagement Optimizer, Assessment Intelligence',
   94,
   '{"product_type": "ai_hub", "agents": 5, "implements": "ai_orchestration_deployment_guide"}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- Auth Products
INSERT INTO resources (title, type, path, description, quality_score, metadata)
VALUES 
  ('Login Page',
   'Authentication Page',
   '/public/login.html',
   'Login interface with Firebase Auth integration (TuiTrader project), role-based authentication',
   93,
   '{"product_type": "auth", "implements": "firebase_migration_aug_2", "roles": ["teacher", "student", "admin"]}'::jsonb),
  
  ('Register Simple Page',
   'Authentication Page',
   '/public/register-simple.html',
   'User registration with role selection (teacher/student), implements Auth System Complete spec',
   95,
   '{"product_type": "auth", "implements": "auth_system_complete_oct_16", "features": ["role_selection", "teacher_signup", "student_signup"]}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 2: PLANNING → NAVIGATION PRODUCT RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Teacher Experience Design → Navigation Components
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  (SELECT id FROM resources WHERE title = 'Navigation Standard Component'),
  'planning_resulted_in_product',
  0.92,
  '{"insight": "Teacher Experience sidebar design influenced Navigation Standard component structure", "feature": "teacher_workflow_navigation", "timeline": "pre_oct_10_to_current"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Navigation Standard Component');

-- Content Hierarchy → Navigation Year Dropdown
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Content Hierarchy Plan%Oct 16%'),
  (SELECT id FROM resources WHERE title = 'Navigation Year Dropdown Component'),
  'planning_resulted_in_product',
  0.94,
  '{"insight": "Content Hierarchy Unit→Lesson→Handout structure required year-level navigation component", "implements": "year_organization", "supports": "nested_structure"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Content Hierarchy Plan%Oct 16%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Navigation Year Dropdown Component');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 3: PLANNING → DASHBOARD PRODUCT RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Teacher Experience Design → Teacher Dashboard Unified
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  (SELECT id FROM resources WHERE title = 'Teacher Dashboard Unified'),
  'planning_resulted_in_product',
  0.98,
  '{"insight": "Teacher Experience Design (Pre-Oct 10) DIRECTLY implemented as Teacher Dashboard Unified (Q98!)", "features_implemented": ["analytics", "resource_library", "planning_tools"], "quality_match": "both_excellent", "critical": "this_is_the_planned_dashboard"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher Dashboard Unified');

-- AI Orchestration → Teacher AI Intelligence Hub
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%AI Orchestration Deployment Guide%'),
  (SELECT id FROM resources WHERE title = 'Teacher AI Intelligence Hub'),
  'planning_resulted_in_product',
  0.96,
  '{"insight": "AI Orchestration Guide planned 5 AI agents, Teacher AI Hub is the PRODUCT - deployed and working!", "agents_deployed": 5, "features": ["deepseek_integration", "cultural_guardian", "assessment_intelligence"], "status": "built_needs_visibility_in_sidebar"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%AI Orchestration Deployment Guide%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher AI Intelligence Hub');

-- AI Orchestration → Teacher Dashboard AI
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%AI Orchestration Deployment Guide%'),
  (SELECT id FROM resources WHERE title = 'Teacher Dashboard AI'),
  'planning_resulted_in_product',
  0.95,
  '{"insight": "AI Orchestration enabled Teacher Dashboard AI with DeepSeek + GraphRAG intelligence", "ai_features": ["deepseek_powered", "cultural_intelligence", "graphrag_recommendations"]}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%AI Orchestration Deployment Guide%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher Dashboard AI');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 4: PLANNING → AUTH PRODUCT RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- GraphRAG Firebase Migration → Login Page
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%GraphRAG Firebase Migration%Aug 2%'),
  (SELECT id FROM resources WHERE title = 'Login Page'),
  'planning_resulted_in_product',
  0.94,
  '{"insight": "Aug 2 Firebase migration decision (TuiTrader project) implemented in Login Page", "auth_provider": "firebase", "project": "tuitrader", "hybrid": "firebase_auth_supabase_data"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%GraphRAG Firebase Migration%Aug 2%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Login Page');

-- Architecture → Register Simple Page
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Architecture - Authentication System%'),
  (SELECT id FROM resources WHERE title = 'Register Simple Page'),
  'planning_resulted_in_product',
  0.96,
  '{"insight": "Architecture student|teacher|admin roles implemented in Register Simple with role selection", "roles": ["teacher", "student"], "features": ["role_based_signup", "profile_creation"]}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Architecture - Authentication System%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Register Simple Page');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 5: CONTENT HIERARCHY → ACTUAL UNITS/LESSONS (Products!)
-- ═══════════════════════════════════════════════════════════════════════════

-- We need to find actual unit pages and connect them
-- First, let's create entries for gold standard units

INSERT INTO resources (title, type, path, description, quality_score, metadata)
VALUES 
  ('Y8 Systems Unit - Gold Standard',
   'Unit',
   '/public/y8-systems/',
   'GOLD STANDARD unit: Decolonizing Power Structures - 10 lessons over 5 weeks, 30+ resources, exemplifies Content Hierarchy Plan',
   100,
   '{"unit_type": "gold_standard", "lessons": 10, "weeks": 5, "resources": 30, "subject": "social_studies", "year": 8, "exemplifies": "content_hierarchy_oct_16"}'::jsonb),
  
  ('Y8 Digital Kaitiakitanga Unit',
   'Unit',
   '/public/units/y8-digital-kaitiakitanga/',
   'Digital Technologies unit with cultural integration: 18 lessons, Quality 100, Perfect learning chain',
   100,
   '{"lessons": 18, "confidence": 1.0, "cultural_integration": 100, "subject": "digital_technologies", "year": 8}'::jsonb),
  
  ('Y9 Ecology & Whakapapa Unit',
   'Unit',
   '/public/units/y9-ecology/',
   'Ecology unit with whakapapa connections: 6 lessons, Quality 98, Cultural integration excellent',
   98,
   '{"lessons": 6, "confidence": 1.0, "cultural_integration": 95, "subject": "science", "year": 9}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- Content Hierarchy Plan → Y8 Systems (Gold Standard!)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Content Hierarchy Plan%Oct 16%'),
  (SELECT id FROM resources WHERE title = 'Y8 Systems Unit - Gold Standard'),
  'planning_resulted_in_product',
  0.99,
  '{"insight": "Content Hierarchy Plan (Oct 16) used Y8 Systems as GOLD STANDARD example - this unit IS the template!", "exemplifies": "unit_lesson_handout_structure", "quality": "5/5", "critical": "this_is_the_model_for_all_units"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Content Hierarchy Plan%Oct 16%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Y8 Systems Unit - Gold Standard');

-- Y8 Systems → Other Units (Sets Standard)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title = 'Y8 Systems Unit - Gold Standard'),
  (SELECT id FROM resources WHERE title = 'Y8 Digital Kaitiakitanga Unit'),
  'sets_standard_for',
  0.92,
  '{"insight": "Y8 Systems gold standard structure (10 lessons, 5 weeks) influenced other units like Digital Kaitiakitanga (18 lessons)", "influence": "unit_structure_template"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title = 'Y8 Systems Unit - Gold Standard')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Y8 Digital Kaitiakitanga Unit');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 6: BMAD DESIGN → CSS PRODUCTS
-- ═══════════════════════════════════════════════════════════════════════════

INSERT INTO resources (title, type, path, description, quality_score, metadata)
VALUES 
  ('Professionalization System CSS',
   'CSS File',
   '/public/css/professionalization-system.css',
   'Primary design system CSS - should implement BMAD cultural design but may have gone generic',
   85,
   '{"file_type": "css", "status": "may_have_erased_bmad", "should_contain": "bmad_cultural_tokens"}'::jsonb),
  
  ('Te Kete Professional CSS',
   'CSS File',
   '/public/css/te-kete-professional.css',
   'Professional styling CSS - supplementary to professionalization system',
   88,
   '{"file_type": "css", "role": "supplementary", "lines": 3409}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- BMAD → CSS Files (Should Have Implemented)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%'),
  (SELECT id FROM resources WHERE title = 'Professionalization System CSS'),
  'should_be_implemented_in',
  0.90,
  '{"insight": "BMAD cultural design (Aug 5) SHOULD be implemented in Professionalization CSS, but may have been erased by generic corporate styling", "critical": "user_says_older_better", "action_required": "restore_bmad_tokens", "bmad_colors": "#8B4513, #2F4F2F, #CD853F"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Professionalization System CSS');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 7: AI ORCHESTRATION → AI PRODUCTS
-- ═══════════════════════════════════════════════════════════════════════════

-- AI Orchestration → Kaitiaki-Generated Content
INSERT INTO resources (title, type, path, description, quality_score, metadata)
VALUES 
  ('Kaitiaki Generated Cultural Mathematics Rubric',
   'Assessment Tool',
   '/public/assessments/kaitiaki-generated-cultural-mathematics-rubric.html',
   'AI-generated assessment rubric with cultural integration - demonstrates Kaitiaki AI system capabilities',
   93,
   '{"product_type": "ai_generated", "ai_agent": "kaitiaki", "subject": "mathematics", "cultural_integration": true}'::jsonb),
  
  ('Kaitiaki Generated Y10 Math Cultural Geometry Unit',
   'Unit Plan',
   '/public/unit-plans/kaitiaki-generated-y10-math-cultural-geometry.html',
   'AI-generated unit plan connecting geometry to Māori cultural patterns - demonstrates AI content generation',
   91,
   '{"product_type": "ai_generated_unit", "ai_agent": "kaitiaki", "year": 10, "subject": "mathematics", "cultural": "geometry_patterns"}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- Grand Vision AI → Kaitiaki Products
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%'),
  (SELECT id FROM resources WHERE title = 'Kaitiaki Generated Cultural Mathematics Rubric'),
  'vision_resulted_in_ai_product',
  0.88,
  '{"insight": "July 29 Grand Vision AI-powered culturally responsive ecosystem resulted in Kaitiaki-generated content", "ai_system": "kaitiaki_aronui", "cultural_validation": true}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Kaitiaki Generated Cultural Mathematics Rubric');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 8: CROSS-PRODUCT RELATIONSHIPS (Products to Products)
-- ═══════════════════════════════════════════════════════════════════════════

-- Teacher Dashboard → Navigation Component (Uses)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title = 'Teacher Dashboard Unified'),
  (SELECT id FROM resources WHERE title = 'Navigation Standard Component'),
  'product_uses_product',
  0.95,
  '{"insight": "Teacher Dashboard Unified loads Navigation Standard component for teacher workflow", "integration_type": "component_injection", "method": "javascript_fetch"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher Dashboard Unified')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Navigation Standard Component');

-- Teacher Dashboard Unified → Teacher AI Hub (Links To)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title = 'Teacher Dashboard Unified'),
  (SELECT id FROM resources WHERE title = 'Teacher AI Intelligence Hub'),
  'product_links_to_product',
  0.93,
  '{"insight": "Teacher Dashboard should link to AI Intelligence Hub for AI-powered features", "status": "link_may_not_be_prominent", "action": "make_visible_in_sidebar"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher Dashboard Unified')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher AI Intelligence Hub');

-- Login Page → Dashboard Products (Redirects After Auth)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title = 'Login Page'),
  (SELECT id FROM resources WHERE title = 'Teacher Dashboard Unified'),
  'auth_redirects_to',
  0.94,
  '{"insight": "Login Page redirects teachers to Teacher Dashboard Unified after successful authentication", "role": "teacher", "flow": "login_to_dashboard"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title = 'Login Page')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher Dashboard Unified');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 9: MISSING PRODUCTS (Planned but Not Built)
-- ═══════════════════════════════════════════════════════════════════════════

-- These are PLANNED in MDs but don't exist as products yet

INSERT INTO resources (title, type, path, description, quality_score, metadata)
VALUES 
  ('Teacher Sidebar Component - PLANNED NOT BUILT',
   'Planned Component',
   '/public/components/teacher-sidebar.html',
   'PLANNED: 280px persistent sidebar with nested teaching content, professional tools, GraphRAG-powered - Designed Pre-Oct 10, NOT BUILT YET',
   0,
   '{"status": "planned_not_built", "planned_in": "teacher_experience_design", "requested": "oct_26_user", "priority": "p2_after_bmad_and_kamar"}'::jsonb),
  
  ('KAMAR Webhook Listener - PLANNED NOT BUILT',
   'Planned Backend Service',
   '/netlify/functions/kamar-webhook-listener.js',
   'CRITICAL BLOCKER: KAMAR integration webhook listener - Researched Aug 6, Designed, NOT BUILT - Required for teacher weekly planner!',
   0,
   '{"status": "planned_not_built", "planned_in": "kamar_integration_research_aug_6", "timeline": "2_week_mvp", "blocks": "teacher_sidebar_weekly_planner", "priority": "p1_critical_blocker"}'::jsonb),
  
  ('Student Dashboard - PLANNED NOT BUILT',
   'Planned Dashboard',
   '/public/students/dashboard.html',
   'PLANNED: Student dashboard with learning overview, personalized paths, achievements - Detailed spec Oct 16, NOT BUILT YET',
   0,
   '{"status": "planned_not_built", "planned_in": "student_dashboard_spec_oct_16", "spec_complete": true, "ready_to_build": true, "priority": "p2_after_teacher_sidebar"}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- KAMAR Research → Missing Webhook (Critical Gap!)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%KAMAR Integration Research%Aug 6%'),
  (SELECT id FROM resources WHERE title = 'KAMAR Webhook Listener - PLANNED NOT BUILT'),
  'planning_NOT_YET_implemented',
  0.93,
  '{"insight": "KAMAR webhook planned Aug 6 with 2-week MVP timeline, STILL NOT BUILT after 81 days!", "critical_blocker": true, "blocks": "teacher_sidebar_weekly_planner", "urgency": "high", "timeline_original": "2_weeks", "timeline_actual": "81_days_not_started"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%KAMAR Integration Research%Aug 6%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'KAMAR Webhook Listener - PLANNED NOT BUILT');

-- Teacher Experience → Missing Sidebar (Gap!)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  (SELECT id FROM resources WHERE title = 'Teacher Sidebar Component - PLANNED NOT BUILT'),
  'planning_NOT_YET_implemented',
  0.96,
  '{"insight": "Teacher Experience Design (Pre-Oct 10) explicitly designed sidebar, STILL NOT BUILT - This is what user requested Oct 26!", "designed_days_ago": "16+", "user_requested": "oct_26", "priority": "implement_now_phase_3"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Teacher Sidebar Component - PLANNED NOT BUILT');

-- Student Dashboard Spec → Missing Dashboard (Gap!)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%TASK_3_STUDENT_DASHBOARD%'),
  (SELECT id FROM resources WHERE title = 'Student Dashboard - PLANNED NOT BUILT'),
  'planning_NOT_YET_implemented',
  0.94,
  '{"insight": "Student Dashboard spec complete Oct 16, ready to build, NOT BUILT YET", "spec_quality": "production_ready", "ready": true, "waiting_for": "teacher_sidebar_first"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%TASK_3_STUDENT_DASHBOARD%')
  AND EXISTS (SELECT 1 FROM resources WHERE title = 'Student Dashboard - PLANNED NOT BUILT');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 10: VERIFY COMPLETE NETWORK
-- ═══════════════════════════════════════════════════════════════════════════

-- Count all relationship types
SELECT 
  relationship_type,
  COUNT(*) as count,
  AVG(confidence_score) as avg_confidence
FROM graphrag_relationships 
WHERE created_at > NOW() - INTERVAL '2 minutes'
GROUP BY relationship_type
ORDER BY count DESC;

-- Show complete planning → product chain
SELECT 
  r1.title as planning_doc,
  rel.relationship_type,
  r2.title as product,
  rel.confidence_score,
  rel.metadata->>'insight' as insight
FROM graphrag_relationships rel
JOIN resources r1 ON r1.id = rel.source_resource_id
JOIN resources r2 ON r2.id = rel.target_resource_id
WHERE rel.relationship_type LIKE '%resulted_in%'
   OR rel.relationship_type LIKE '%NOT_YET%'
ORDER BY rel.confidence_score DESC;

