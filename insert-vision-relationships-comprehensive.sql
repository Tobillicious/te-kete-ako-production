-- ═══════════════════════════════════════════════════════════════════════════
-- GRAPHRAG VISION RELATIONSHIP NETWORK - COMPREHENSIVE INSERTION
-- Maps 89-day vision genealogy: July 29 → October 26, 2025
-- Purpose: Enable ALL AI agents to see planning → implementation connections
-- ═══════════════════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 1: INSERT FOUNDATIONAL VISION DOCUMENTS AS RESOURCES
-- ═══════════════════════════════════════════════════════════════════════════

INSERT INTO resources (title, type, path, description, quality_score, created_at, metadata)
VALUES 
  -- JULY 2025: THE GRAND VISION
  ('Te Kete Ako Grand Vision & Strategic Roadmap - July 29 2025', 
   'Strategic Vision', 
   '/docs/archive/md-files-historical/TE_KETE_AKO_GRAND_VISION_STRATEGIC_ROADMAP.md',
   'Original foundational vision: 6-Agent AI team, Teacher/Student differentiation, GraphRAG intelligence, 3-Phase strategic roadmap (National→Global→Revolutionary)',
   100,
   '2025-07-29 00:00:00',
   '{"phase": "vision_foundation", "defines": ["6_agent_team", "teacher_student_roles", "graphrag_system", "3_phase_roadmap"], "status": "foundational_document"}'::jsonb),
  
  -- AUGUST 2025: INFRASTRUCTURE FOUNDATION
  ('GraphRAG Firebase Migration Update - Aug 2 2025',
   'Infrastructure Decision',
   '/docs/GRAPHRAG_FIREBASE_MIGRATION_UPDATE_AUG2.md',
   'Infrastructure foundation: GraphRAG on Supabase, Firebase Auth (TuiTrader), Hybrid architecture, Resolved 12 failed auth attempts',
   95,
   '2025-08-02 00:00:00',
   '{"phase": "infrastructure", "resolves": "authentication_crisis", "establishes": "hybrid_firebase_supabase"}'::jsonb),
  
  ('BMAD Design Revolution - Aug 5 2025',
   'Cultural Design Philosophy',
   '/docs/BMAD_DESIGN_REVOLUTION.md',
   'CRITICAL: Cultural design DNA - Whakapapa navigation, Natural pigment colors (#8B4513, #2F4F2F), Marae spatial organization, Koru/Tukutuku patterns, Cultural principles guide technology',
   100,
   '2025-08-05 00:00:00',
   '{"phase": "design_foundation", "is_older_better_style": true, "colors": ["#8B4513", "#2F4F2F", "#CD853F"], "patterns": ["koru", "tukutuku", "marae"]}'::jsonb),
  
  ('KAMAR Integration Research - Aug 6 2025',
   'Technical Integration Plan',
   '/docs/KAMAR_INTEGRATION_RESEARCH.md',
   'NZ school SMS integration: Webhook listener architecture, Timetable sync design, 2-week MVP timeline, Required for teacher weekly planner',
   90,
   '2025-08-06 00:00:00',
   '{"phase": "integration_planning", "timeline": "2_weeks_mvp", "blocks": "teacher_sidebar_weekly_planner", "status": "researched_not_built"}'::jsonb),
  
  ('Alpha Build Mission Complete - Aug 9 2025',
   'Development Milestone',
   '/docs/ALPHA_BUILD_MISSION_COMPLETE_REPORT.md',
   'Alpha build 80% complete: DeepSeek API integrated, 3 resources deployed, Kaitiaki Aronui active, 750+ resources in GraphRAG',
   92,
   '2025-08-09 00:00:00',
   '{"phase": "alpha_milestone", "completion": "80%", "resources": 750, "ai_system": "kaitiaki_aronui_active"}'::jsonb),
  
  -- PRE-OCTOBER: ARCHITECTURE LAYER
  ('Architecture - Authentication System Design',
   'Technical Architecture',
   '/docs/ARCHITECTURE.md',
   'Technical foundation: 4-layer auth system, student|teacher|admin roles, Database schema (auth.users + profiles), Session management',
   95,
   '2025-10-05 00:00:00',
   '{"phase": "architecture", "defines": ["role_based_auth", "4_layer_system", "database_schema"]}'::jsonb),
  
  ('Teacher Experience Design',
   'UX Specification',
   '/docs/TEACHER_EXPERIENCE_DESIGN.md',
   'CRITICAL: Teacher UX with SIDEBAR NAVIGATION, Daily Dashboard, Lesson Planning Interface, Professional Tools, AI-powered cultural integration',
   98,
   '2025-10-08 00:00:00',
   '{"phase": "ux_design", "defines": "sidebar_navigation", "includes": ["daily_dashboard", "lesson_planner", "ai_suggestions"], "target_role": "teacher"}'::jsonb),
  
  ('Student Experience Design',
   'UX Specification',
   '/docs/STUDENT_EXPERIENCE_DESIGN.md',
   'Student UX: Simplified dashboard, Guided learning pathways, Age-appropriate interface, Minimal distractions vs teacher comprehensive',
   95,
   '2025-10-08 00:00:00',
   '{"phase": "ux_design", "differentiates_from": "teacher_experience", "target_role": "student"}'::jsonb),
  
  ('Mangakotukutuku Production Roadmap',
   'Production Timeline',
   '/docs/MANGAKOTUKUTUKU_PRODUCTION_ROADMAP.md',
   'CRITICAL: 26-week production plan - Phase 1 (0-4w Foundation), Phase 2 (5-12w Alpha), Phase 3 (13-26w Production with sidebar+SaaS)',
   97,
   '2025-10-08 00:00:00',
   '{"phase": "production_timeline", "duration_weeks": 26, "phases": 3, "current_week": 12, "current_phase": "2_to_3_transition"}'::jsonb),
  
  ('Agent Personality System',
   'AI Coordination Framework',
   '/docs/AGENT_PERSONALITY_SYSTEM.md',
   '6 AI Agents with Myers-Briggs: Whaea Claude (ENFJ), Matua DeepSeek (INTJ), Kuia Exa (ENTP), GraphRAG Koro (ISFJ), Tama Code (ISTP), Gemini (ENFP)',
   93,
   '2025-10-08 00:00:00',
   '{"phase": "agent_coordination", "agent_count": 6, "evolved_to": 12, "methodology": "cognitive_diversity"}'::jsonb),
  
  ('AI Orchestration Deployment Guide',
   'AI System Implementation',
   '/docs/AI_ORCHESTRATION_DEPLOYMENT_GUIDE.md',
   '5 AI Agents deployed: Learning Pathfinder, Content Curator, Cultural Guardian, Engagement Optimizer, Assessment Intelligence',
   94,
   '2025-10-09 00:00:00',
   '{"phase": "ai_deployment", "agents": 5, "features": ["teacher_ai_hub", "deepseek_graphrag_bridge", "content_enhancement"]}'::jsonb),
  
  -- OCTOBER 13-16: PHILOSOPHY & STRUCTURE
  ('Unified Vision Fusion - Oct 13 2025',
   'Philosophy Document',
   '/docs/archive/2025-10-16-2158/UNIFIED_VISION_FUSION.md',
   'CRITICAL: Evolutionary Professionalism philosophy - Super Professional + World-Class Cultural (NOT either/or, BOTH!), GraphRAG Meditation, MCP Hive Mind',
   99,
   '2025-10-13 00:00:00',
   '{"phase": "philosophy", "principle": "evolutionary_professionalism", "fusion": "professional_AND_cultural"}'::jsonb),
  
  ('Comprehensive Content Hierarchy Plan - Oct 16 2025',
   'Architecture Document',
   '/docs/archive/2025-10-16-2158/COMPREHENSIVE_CONTENT_HIERARCHY_PLAN.md',
   'CRITICAL: Defines UNIT → LESSONS → HANDOUTS structure, Y8 Systems as gold standard, 1,539 resources to organize, Nested hierarchy for sidebar',
   96,
   '2025-10-16 00:00:00',
   '{"phase": "content_structure", "hierarchy": "unit_lesson_handout", "gold_standard": "y8_systems", "requires": "nested_sidebar_navigation"}'::jsonb),
  
  -- OCTOBER 26: CURRENT IMPLEMENTATION
  ('Professional SaaS Transformation - Oct 26 2025',
   'Implementation Plan',
   '/🚀-PROFESSIONAL-SAAS-TRANSFORMATION.md',
   'Phase 3 implementation: Sidebar navigation (280px), Role-based dashboards, Monetization ($15/month), Professional tools activation',
   98,
   '2025-10-26 00:00:00',
   '{"phase": "phase_3_implementation", "features": ["sidebar", "role_dashboards", "monetization", "professional_tools"], "roadmap_phase": 3}'::jsonb),
  
  ('Navigation Architecture Summary - Oct 26 2025',
   'Technical Documentation',
   '/NAVIGATION-ARCHITECTURE-SUMMARY.md',
   'Three-tier navigation system: Header (global) + Sidebar (role-based) + Breadcrumb+Nested (contextual), GraphRAG-powered intelligence',
   96,
   '2025-10-26 00:00:00',
   '{"phase": "navigation_design", "tiers": 3, "sidebar_width": "280px", "graphrag_powered": true}'::jsonb)

ON CONFLICT (title) DO NOTHING;

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 2: CREATE RELATIONSHIPS - VISION FOUNDATION
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 1: Grand Vision → Agent Personality System
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%'),
  (SELECT id FROM resources WHERE title LIKE '%Agent Personality System%'),
  'defines_team_architecture',
  0.98,
  '{"insight": "Grand Vision July 29 defined 6-Agent AI team, Agent Personality System implements same 6 agents with Myers-Briggs", "validation": "exact_match", "evolution": "6_to_12_agents"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Agent Personality System%');

-- Relationship 2: Grand Vision → Teacher Experience Design
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%'),
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  'defines_role_differentiation',
  0.97,
  '{"insight": "Grand Vision defined Teacher/Student differentiation, Teacher Experience implements teacher-specific UX with sidebar", "feature": "sidebar_navigation", "role": "teacher"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%');

-- Relationship 3: Grand Vision → GraphRAG Infrastructure
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%'),
  (SELECT id FROM resources WHERE title LIKE '%GraphRAG Firebase Migration%Aug 2%'),
  'defines_intelligence_system',
  0.96,
  '{"insight": "Grand Vision defined GraphRAG intelligence system, Aug 2 migration implemented infrastructure foundation", "implementation": "supabase_graphrag", "timeline": "4_days_after_vision"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%GraphRAG Firebase Migration%Aug 2%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 3: BMAD DESIGN PHILOSOPHY RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 4: BMAD → Teacher Experience (Design Philosophy)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%'),
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  'cultural_design_philosophy_for',
  0.99,
  '{"insight": "BMAD (Aug 5) defined Māori cultural design DNA that should guide Teacher Experience sidebar aesthetics", "critical": "this_is_older_better_style", "colors": "#8B4513, #2F4F2F", "patterns": "koru, tukutuku, marae"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%');

-- Relationship 5: BMAD → Unified Vision Fusion (Philosophy Evolution)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%'),
  (SELECT id FROM resources WHERE title LIKE '%Unified Vision Fusion%Oct 13%'),
  'evolved_into_philosophy',
  0.95,
  '{"insight": "BMAD cultural principles (Aug 5) evolved into Evolutionary Professionalism (Oct 13): Super Professional + World-Class Cultural", "synthesis": "professional_AND_cultural_not_OR"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Unified Vision Fusion%Oct 13%');

-- Relationship 6: BMAD → Current User Concern (Explains Issue)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%'),
  (SELECT id FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%'),
  'explains_user_concern',
  0.99,
  '{"insight": "BMAD is the older better style user referenced - warm Māori aesthetics vs recent generic professionalization", "user_feedback": "older_style_is_better", "solution": "restore_bmad_design_dna", "critical": "professionalization_erased_cultural_soul"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%BMAD Design Revolution%Aug 5%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 4: PRODUCTION ROADMAP & TIMELINE RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 7: Roadmap → KAMAR Integration (Requires Feature)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Mangakotukutuku Production Roadmap%'),
  (SELECT id FROM resources WHERE title LIKE '%KAMAR Integration Research%Aug 6%'),
  'requires_integration',
  0.93,
  '{"insight": "Roadmap Phase 1 requires basic KAMAR, Phase 2 requires advanced KAMAR for teacher weekly planner", "blocker": "sidebar_weekly_planner_needs_kamar_data", "timeline": "2_week_mvp", "status": "researched_not_built"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Mangakotukutuku Production Roadmap%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%KAMAR Integration Research%Aug 6%');

-- Relationship 8: Roadmap → Teacher Experience (Defines Requirements)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Mangakotukutuku Production Roadmap%'),
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  'defines_feature_requirements',
  0.97,
  '{"insight": "Roadmap Phase 1-2 defines weekly planner, teacher analytics, AI assessment - all require sidebar navigation from Teacher Experience design", "features": ["weekly_planner", "analytics", "ai_assessment"], "requires": "sidebar_navigation"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Mangakotukutuku Production Roadmap%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%');

-- Relationship 9: Roadmap → SaaS Transformation (Timeline Validation)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Mangakotukutuku Production Roadmap%'),
  (SELECT id FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%'),
  'timeline_validates',
  0.96,
  '{"insight": "Roadmap Phase 3 (Week 13+) aligns with Oct 26 user request = Week 12.3 = perfect timing for Phase 3 implementation!", "current_week": 12, "phase_transition": "2_to_3", "features_requested": ["sidebar", "saas", "monetization"], "validation": "exactly_on_schedule"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Mangakotukutuku Production Roadmap%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 5: ARCHITECTURE → UX DESIGN RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 10: Architecture → Teacher Experience (Technical Foundation)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Architecture - Authentication System%'),
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  'technical_foundation_for',
  0.98,
  '{"insight": "Architecture defines role-based auth (teacher|student|admin), Teacher Experience implements teacher-specific dashboard and sidebar", "technical": "role_based_authentication", "ux": "sidebar_navigation_professional_tools"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Architecture - Authentication System%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%');

-- Relationship 11: Architecture → Student Experience (Technical Foundation)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Architecture - Authentication System%'),
  (SELECT id FROM resources WHERE title LIKE '%Student Experience Design%'),
  'technical_foundation_for',
  0.98,
  '{"insight": "Architecture defines student role, Student Experience implements simplified dashboard and guided pathways", "technical": "student_role_authentication", "ux": "simplified_guided_interface"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Architecture - Authentication System%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Student Experience Design%');

-- Relationship 12: Teacher Experience ↔ Student Experience (Differentiation)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  (SELECT id FROM resources WHERE title LIKE '%Student Experience Design%'),
  'differentiates_from',
  0.97,
  '{"insight": "Teacher = comprehensive sidebar with professional tools, Student = simplified guided pathways", "difference": "complexity_and_features", "same_foundation": "architecture_roles"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Student Experience Design%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 6: CONTENT HIERARCHY → NAVIGATION RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 13: Content Hierarchy → Navigation Architecture (Requires Structure)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Comprehensive Content Hierarchy Plan%Oct 16%'),
  (SELECT id FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%'),
  'architecture_requires',
  0.98,
  '{"insight": "Oct 16 Unit→Lesson→Handout hierarchy requires Oct 26 nested sidebar navigation with collapsible sections", "structure": "nested_details_elements", "match": "exact_hierarchy_implementation"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Comprehensive Content Hierarchy Plan%Oct 16%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%');

-- Relationship 14: Navigation Architecture → Content Hierarchy (Fulfills Plan)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%'),
  (SELECT id FROM resources WHERE title LIKE '%Comprehensive Content Hierarchy Plan%Oct 16%'),
  'fulfills_plan',
  0.97,
  '{"insight": "Oct 26 sidebar navigation implements Oct 16 content hierarchy plan - nested Unit dropdown shows Lessons shows Handouts", "implementation": "collapsible_nested_structure", "timeline": "10_days_plan_to_implementation"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Comprehensive Content Hierarchy Plan%Oct 16%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 7: PHILOSOPHY → IMPLEMENTATION RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 15: Unified Vision → SaaS Transformation (Philosophy Guides)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Unified Vision Fusion%Oct 13%'),
  (SELECT id FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%'),
  'philosophy_guides_implementation',
  0.94,
  '{"insight": "Oct 13 Evolutionary Professionalism (Super Professional + World-Class Cultural) guides Oct 26 SaaS implementation with BMAD aesthetics", "principle": "professional_execution_with_maori_character"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Unified Vision Fusion%Oct 13%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 8: CURRENT IMPLEMENTATION → GRAND VISION (FULFILLS)
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 16: SaaS Transformation → Grand Vision (Fulfills 89-Day Plan!)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%'),
  (SELECT id FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%'),
  'fulfills_original_vision',
  0.98,
  '{"insight": "Oct 26 sidebar+SaaS request fulfills July 29 Grand Vision - NOT a pivot, but COMPLETION of 89-day plan!", "timeline": "89_days_consistent", "validation": "teacher_student_roles_sidebar_navigation_all_planned_july", "critical": "this_was_always_the_plan"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%');

-- Relationship 17: Navigation Architecture → Grand Vision (Fulfills Vision)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%'),
  (SELECT id FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%'),
  'fulfills_original_vision',
  0.96,
  '{"insight": "Oct 26 three-tier navigation (header+sidebar+nested) implements July 29 vision of intelligent, culturally responsive platform", "features": "graphrag_powered_navigation", "timeline": "89_days_vision_to_implementation"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Navigation Architecture Summary%Oct 26%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Grand Vision%Strategic Roadmap%July%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 9: KAMAR INTEGRATION DEPENDENCY CHAIN
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 18: KAMAR → Teacher Experience (Critical Blocker!)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%KAMAR Integration Research%Aug 6%'),
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  'critical_dependency_for',
  0.93,
  '{"insight": "KAMAR timetable sync is CRITICAL BLOCKER for teacher sidebar weekly planner feature", "blocker": "weekly_planner_needs_timetable_data", "status": "researched_aug_6_not_built", "timeline": "2_week_mvp", "urgency": "high"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%KAMAR Integration Research%Aug 6%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%');

-- Relationship 19: Teacher Experience → SaaS Transformation (Requires KAMAR)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  (SELECT id FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%'),
  'requires_for_full_implementation',
  0.95,
  '{"insight": "Teacher sidebar in SaaS Transformation requires KAMAR integration for weekly planner to function", "dependency_chain": "KAMAR_webhook → timetable_sync → weekly_planner → sidebar_display", "action": "build_kamar_integration_first"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Professional SaaS Transformation%Oct 26%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 10: AI ORCHESTRATION RELATIONSHIPS
-- ═══════════════════════════════════════════════════════════════════════════

-- Relationship 20: AI Orchestration → Teacher Experience (Enables Features)
INSERT INTO graphrag_relationships (source_resource_id, target_resource_id, relationship_type, confidence_score, metadata)
SELECT 
  (SELECT id FROM resources WHERE title LIKE '%AI Orchestration Deployment Guide%'),
  (SELECT id FROM resources WHERE title LIKE '%Teacher Experience Design%'),
  'enables_ai_features_in',
  0.94,
  '{"insight": "AI Orchestration deploys 5 AI agents (Assessment Intelligence, Cultural Guardian, etc) that power Teacher Experience AI suggestions", "features": ["ai_cultural_integration_suggestions", "assessment_intelligence", "content_curation"], "status": "built_not_visible_in_ui"}'::jsonb
WHERE EXISTS (SELECT 1 FROM resources WHERE title LIKE '%AI Orchestration Deployment Guide%')
  AND EXISTS (SELECT 1 FROM resources WHERE title LIKE '%Teacher Experience Design%');

-- ═══════════════════════════════════════════════════════════════════════════
-- STEP 11: VERIFY RELATIONSHIPS CREATED
-- ═══════════════════════════════════════════════════════════════════════════

SELECT 
  'Vision Relationships Inserted' as status,
  COUNT(*) as relationship_count,
  AVG(confidence_score) as avg_confidence
FROM graphrag_relationships 
WHERE relationship_type IN (
  'defines_team_architecture',
  'defines_role_differentiation',
  'defines_intelligence_system',
  'cultural_design_philosophy_for',
  'evolved_into_philosophy',
  'explains_user_concern',
  'requires_integration',
  'defines_feature_requirements',
  'timeline_validates',
  'technical_foundation_for',
  'differentiates_from',
  'architecture_requires',
  'fulfills_plan',
  'philosophy_guides_implementation',
  'fulfills_original_vision',
  'critical_dependency_for',
  'requires_for_full_implementation',
  'enables_ai_features_in'
)
AND created_at > NOW() - INTERVAL '1 minute';

