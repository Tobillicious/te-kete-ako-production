-- ================================================================
-- AGENT DISCOVERY SESSION - October 20, 2025
-- Agent: New Claude Instance (Exploration & Intelligence Gathering)
-- Purpose: Document exploration findings and discoveries for GraphRAG
-- ================================================================

-- ================================================================
-- DISCOVERY #1: COMPREHENSIVE GRAPHRAG EXPLORATION COMPLETE
-- ================================================================

INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'agent_session',
    'GraphRAG Intelligence Layer Exploration - Oct 20, 2025',
    'system_discovery',
    ARRAY[
        '11,224 resources indexed with 153,184 AI-powered connections mapped',
        '738 prerequisite learning pathways exist (longest: 18-step Writers Toolkit sequence!)',
        '13,042 teaching variant options available (10.8 options per lesson) - pedagogical gold!',
        '90% cultural integration platform-wide with Y8 Digital Kaitiakitanga at 97.2% (the template for excellence)',
        'Recent victory: Digital Tech ↔ Te Ao Māori bridge grew 710 → 1,210 connections (+70% in Oct 19 sprint)',
        'Most connected resources: Adaptive Learning Pathways (1,617), Teacher Insights Dashboard (1,388), Homepage (986)',
        'Science × Math cross-curricular bridge: 2,284 connections (STRONGEST bridge on platform)',
        'Subject taxonomy cleaned: 242 → 12 canonical subjects (99.97% cleanup!)',
        'Intelligence Hub dashboard shows real-time stats and 10 specialized discovery tools available'
    ],
    jsonb_build_object(
        'exploration_method', 'Systematic file reading + codebase search + documentation analysis',
        'dashboards_discovered', ARRAY[
            '/public/intelligence-hub.html (master hub)',
            '/public/graphrag-teacher-dashboard.html (updated Oct 19)',
            '/public/graphrag-analytics-dashboard.html',
            '/public/graphrag-optimization-dashboard.html',
            '/public/graphrag-science-dashboard.html',
            '/public/graphrag-query-dashboard.html'
        ],
        'tools_available', jsonb_build_object(
            'python_scripts', 184,
            'scripts_directory', '/scripts/',
            'key_query_scripts', ARRAY[
                'query-graphrag-quick.py',
                'explore-graphrag-detailed.py',
                'query-graphrag-knowledge.py',
                'surface-all-resources-to-graphrag.py'
            ]
        ),
        'platform_stats', jsonb_build_object(
            'total_resources', 11224,
            'total_connections', 153184,
            'learning_pathways', 738,
            'teaching_variants', 13042,
            'cultural_integration', '90%',
            'relationship_types', 22,
            'subject_count', 12
        ),
        'super_hubs_identified', ARRAY[
            'Adaptive Learning Pathways: 1,617 connections',
            'Teacher Insights Dashboard: 1,388 connections',
            'Complete Assessments Library: 4,676 connections (TRUE hub!)',
            'Te Kete Ako Homepage: 986 connections',
            'Science × Math Bridge: 2,284 connections'
        ],
        'api_documentation_found', 'GRAPHRAG-API-DOCUMENTATION.md provides complete query patterns',
        'dynamic_connection_system', 'graphrag-connection-counter.js enables real-time connection counts on pages'
    ),
    ARRAY['new_claude_agent_oct20'],
    jsonb_build_object(
        'session_start', '2025-10-20',
        'exploration_duration', '~30 minutes',
        'files_analyzed', 15,
        'docs_read', ARRAY[
            'START_HERE_NEW_AGENTS.md',
            'ACTIVE_QUESTIONS.md',
            'GRAPHRAG-API-DOCUMENTATION.md',
            'GRAPHRAG-DYNAMIC-CONNECTIONS-GUIDE.md',
            '/public/intelligence-hub.html',
            '/public/graphrag-teacher-dashboard.html'
        ],
        'status', 'exploration_complete',
        'readiness_level', 'fully_intelligent_and_ready_to_build'
    )
);

-- ================================================================
-- DISCOVERY #2: 12 STRATEGIC TODOS FOUND IN GRAPHRAG
-- ================================================================

INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'agent_session',
    'Strategic TODOs Discovery - 12 Major Initiatives Found in GraphRAG - Oct 20, 2025',
    'coordination_discovery',
    ARRAY[
        'Found 12 strategic TODOs documented in graphrag-intelligence-expansion-todos.sql with FULL implementation plans',
        'These represent 45-55 hours of strategic work to evolve platform from good → self-improving AI organism',
        'All TODOs have: priority level, complexity estimate, implementation steps (8 steps each), success criteria, impact multipliers',
        'TODOs organized in 4 tiers: Foundation (001-003), Intelligence (004-005, 008), Self-Improving (006, 010-011), Ecosystem (007, 009, 012)',
        '8-AGENT-COORDINATION-OCT20.sql shows these TODOs are intended for parallel multi-agent execution',
        'Estimated total impact: 400x+ multiplier across all initiatives',
        'All TODOs queryable via: SELECT * FROM agent_knowledge WHERE source_type = ''strategic_planning'' AND source_name LIKE ''TODO-%''',
        'Each TODO includes API endpoints, file references, example queries, and monitoring queries for progress tracking'
    ],
    jsonb_build_object(
        'todos_discovered', jsonb_build_array(
            jsonb_build_object('id', 'TODO-001', 'name', 'Pipeline Unification', 'priority', 'CRITICAL', 'time', '3-4h', 'impact', '10x'),
            jsonb_build_object('id', 'TODO-002', 'name', 'Agent Intelligence Amplifier', 'priority', 'CRITICAL', 'time', '3-4h', 'impact', '50x'),
            jsonb_build_object('id', 'TODO-003', 'name', 'GraphRAG Relationship Miner', 'priority', 'HIGH', 'time', '4-5h', 'impact', '100x'),
            jsonb_build_object('id', 'TODO-004', 'name', 'Documentation Knowledge Graph', 'priority', 'MEDIUM-HIGH', 'time', '3-4h', 'impact', '20x'),
            jsonb_build_object('id', 'TODO-005', 'name', 'Automated Cultural Enrichment', 'priority', 'HIGH', 'time', '4-5h', 'impact', '30x'),
            jsonb_build_object('id', 'TODO-006', 'name', 'Production Feedback Loop', 'priority', 'MEDIUM', 'time', '4-5h', 'impact', '15x'),
            jsonb_build_object('id', 'TODO-007', 'name', 'Visual Intelligence Dashboard', 'priority', 'MEDIUM', 'time', '3-4h', 'impact', '25x'),
            jsonb_build_object('id', 'TODO-008', 'name', 'Semantic Relationship Engine', 'priority', 'MEDIUM-HIGH', 'time', '5-6h', 'impact', '40x'),
            jsonb_build_object('id', 'TODO-009', 'name', 'Agent Collaboration Protocol 2.0', 'priority', 'HIGH', 'time', '3-4h', 'impact', '30x'),
            jsonb_build_object('id', 'TODO-010', 'name', 'Quality Cascade System', 'priority', 'MEDIUM', 'time', '4-5h', 'impact', '60x'),
            jsonb_build_object('id', 'TODO-011', 'name', 'Orphan Rescue Automation', 'priority', 'MEDIUM', 'time', '3-4h', 'impact', '20x'),
            jsonb_build_object('id', 'TODO-012', 'name', 'Prerequisite Chain Builder', 'priority', 'MEDIUM-HIGH', 'time', '5-6h', 'impact', '35x')
        ),
        'tier_1_foundation', ARRAY['TODO-001: Pipeline Unification', 'TODO-002: Agent Intelligence Amplifier', 'TODO-003: GraphRAG Relationship Miner'],
        'tier_2_intelligence', ARRAY['TODO-004: Documentation Knowledge Graph', 'TODO-005: Cultural Enrichment Engine', 'TODO-008: Semantic Relationship Engine'],
        'tier_3_self_improving', ARRAY['TODO-006: Production Feedback Loop', 'TODO-010: Quality Cascade System', 'TODO-011: Orphan Rescue Automation'],
        'tier_4_ecosystem', ARRAY['TODO-009: Agent Collaboration Protocol 2.0', 'TODO-007: Visual Intelligence Dashboard', 'TODO-012: Prerequisite Chain Builder'],
        'recommended_agent_distribution', jsonb_build_object(
            'agents_1_3', 'Tier 1 Foundation (critical)',
            'agents_4_6', 'Tier 2 Intelligence Expansion',
            'agents_7_8', 'Tier 3 + Tier 4 (quick wins + support)'
        ),
        'coordination_method', 'Query agent_coordination table before claiming to avoid conflicts',
        'source_files', ARRAY[
            'graphrag-intelligence-expansion-todos.sql (1,190 lines - complete implementation plans)',
            '8-AGENT-COORDINATION-OCT20.sql (coordination protocol for 8-agent sprint)'
        ]
    ),
    ARRAY['new_claude_agent_oct20'],
    jsonb_build_object(
        'discovery_method', 'SQL file analysis + grep search',
        'strategic_importance', 'CRITICAL - These TODOs represent the roadmap for platform evolution',
        'readiness', 'All TODOs ready to implement with full specs',
        'recommendation', 'Prioritize Tier 1 (Foundation) first, then expand to other tiers',
        'coordination_ready', true
    )
);

-- ================================================================
-- DISCOVERY #3: IMMEDIATE ACTIONABLE TODOS FROM ALL-TODOS-EXECUTION-LOG
-- ================================================================

INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'agent_session',
    'Immediate TODOs from ALL-TODOS-EXECUTION-LOG.md - Oct 20, 2025',
    'task_discovery',
    ARRAY[
        'Found 5 immediate tactical TODOs in ALL-TODOS-EXECUTION-LOG.md (15% complete, 5 tasks remaining)',
        'These are shorter-term tasks (10-30 min each) vs strategic TODOs (3-6 hours)',
        'Task #1 completed: Linked 14 orphaned resources (30→24 orphans)',
        'Remaining: surface resources script, nav injection, auth routing fix, placeholder fix, tools audit',
        'Key script ready: surface-all-resources-to-graphrag.py (167 lines, configured, READY TO RUN)',
        'Impact: Index ~18K missing resources to make platform fully discoverable'
    ],
    jsonb_build_object(
        'completed_tasks', ARRAY[
            'Link orphaned high-quality resources (14 linked, orphans 30→24)'
        ],
        'pending_tasks', jsonb_build_array(
            jsonb_build_object('id', 2, 'task', 'Run surface-all-resources-to-graphrag.py', 'goal', 'Index ~18K missing resources', 'time', '5-10 min', 'status', 'READY TO RUN'),
            jsonb_build_object('id', 3, 'task', 'Inject nav/footer to Y8 Digital Kaitiakitanga lessons', 'goal', 'Verify/inject navigation in 20 lessons', 'time', '15 min', 'status', 'VERIFYING'),
            jsonb_build_object('id', 4, 'task', 'Fix auth routing - role-based dashboards', 'goal', 'Teacher→teacher-dashboard, Student→student-dashboard', 'time', '10 min', 'status', 'URGENT'),
            jsonb_build_object('id', 5, 'task', 'Run fix-all-placeholders-sitewide.py', 'goal', 'Fix 359 placeholder instances', 'time', '3-5 min', 'status', 'READY TO RUN'),
            jsonb_build_object('id', 6, 'task', 'Audit 150+ existing tools', 'goal', 'Classify dynamic vs static', 'time', '20 min', 'status', 'PENDING')
        ),
        'highest_impact_next', 'surface-all-resources-to-graphrag.py - Makes 18K resources discoverable',
        'most_urgent', 'Fix auth routing (task #4) - Critical user flow',
        'scripts_ready', ARRAY[
            'surface-all-resources-to-graphrag.py',
            'fix-all-placeholders-sitewide.py'
        ],
        'estimated_remaining_time', '~70 minutes total'
    ),
    ARRAY['new_claude_agent_oct20'],
    jsonb_build_object(
        'source_file', 'ALL-TODOS-EXECUTION-LOG.md',
        'agent_who_started', 'Kaiwaihanga Matihiko',
        'progress_status', '15% complete (1/6 tasks done)',
        'recommendation', 'Run surface-all-resources script first for maximum discovery impact'
    )
);

-- ================================================================
-- DISCOVERY #4: MCP SUPABASE COORDINATION PROTOCOL
-- ================================================================

INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'agent_session',
    'MCP Supabase Coordination Protocol Understanding - Oct 20, 2025',
    'protocol_learning',
    ARRAY[
        'CRITICAL: Terminal commands hang forever - must use MCP Supabase exclusively',
        'START_HERE_NEW_AGENTS.md documents GraphRAG-first workflow: Query → Build → Teach',
        'agent_knowledge table stores discoveries, agent_coordination tracks tasks, agent_status shows heartbeats',
        'Mandatory 3-step protocol: Pre-work query → Mid-work heartbeat → Post-work synthesis',
        'Query patterns documented: Recent work (7 days), current priorities, active agents, orphaned resources',
        'Teaching GraphRAG: INSERT INTO agent_knowledge with source_type, key_insights, technical_details, agents_involved',
        'Coordination check: SELECT from agent_coordination WHERE status = in_progress to avoid duplicate work',
        'Cultural protocols: 85+ quality threshold, validate against 627 cultural resources, check has_te_reo/has_whakataukī'
    ],
    jsonb_build_object(
        'mcp_tools_that_work', ARRAY[
            'mcp_supabase_execute_sql',
            'mcp_supabase_list_tables',
            'mcp_supabase_apply_migration'
        ],
        'tools_that_fail', ARRAY[
            'run_terminal_cmd (HANGS FOREVER - NEVER USE)'
        ],
        'key_tables', jsonb_build_object(
            'graphrag_resources', '19,737 rows - all platform resources',
            'graphrag_relationships', '231,469 rows - connection graph',
            'agent_knowledge', '200+ entries - collective agent wisdom',
            'agent_coordination', 'Task claiming and progress tracking',
            'agent_status', 'Real-time agent heartbeats',
            'agent_messages', 'Inter-agent communication'
        ),
        'query_examples', jsonb_build_object(
            'recent_discoveries', 'SELECT source_name, key_insights[1:3] FROM agent_knowledge WHERE created_at >= NOW() - INTERVAL ''7 days'' ORDER BY created_at DESC',
            'current_priorities', 'SELECT task_claimed, status, agent_name FROM agent_coordination WHERE status = ''in_progress'' ORDER BY priority DESC',
            'orphaned_excellence', 'SELECT r.file_path, r.quality_score FROM graphrag_resources r LEFT JOIN graphrag_relationships rel ON r.file_path IN (rel.source_path, rel.target_path) WHERE r.quality_score >= 90 GROUP BY r.file_path HAVING COUNT(rel.id) < 5',
            'platform_stats', 'SELECT COUNT(*) FROM graphrag_resources WHERE file_path LIKE ''/public/%'''
        ),
        'success_checklist', jsonb_build_array(
            'Before starting: Query GraphRAG for existing work',
            'Before starting: Read ACTIVE_QUESTIONS.md',
            'Before starting: Check for similar existing features',
            'While building: Use MCP Supabase (not terminal)',
            'While building: Create relationships in graphrag_relationships',
            'After completing: Add knowledge to agent_knowledge',
            'After completing: Update ACTIVE_QUESTIONS.md if needed',
            'After completing: Create 3+ relationships for discoverability'
        )
    ),
    ARRAY['new_claude_agent_oct20'],
    jsonb_build_object(
        'learning_source', 'START_HERE_NEW_AGENTS.md + codebase search',
        'protocol_understood', true,
        'ready_to_coordinate', true,
        'terminal_bug_acknowledged', 'NEVER use run_terminal_cmd - it hangs forever'
    )
);

-- ================================================================
-- QUERY HELPERS FOR THIS DISCOVERY SESSION
-- ================================================================

-- View all discoveries from this session:
-- SELECT source_name, key_insights[1:5] 
-- FROM agent_knowledge 
-- WHERE agents_involved @> ARRAY['new_claude_agent_oct20']
-- ORDER BY created_at DESC;

-- Get all strategic TODOs:
-- SELECT source_name, technical_details->>'priority', technical_details->>'complexity', metadata->>'estimated_impact'
-- FROM agent_knowledge 
-- WHERE source_type = 'strategic_planning' 
-- AND source_name LIKE 'TODO-%'
-- ORDER BY source_name;

-- Check what agents are currently active:
-- SELECT agent_name, current_task, status, last_heartbeat 
-- FROM agent_status 
-- WHERE last_heartbeat > NOW() - INTERVAL '1 hour';

-- See what tasks are claimed:
-- SELECT task_claimed, agent_name, status, started_at 
-- FROM agent_coordination 
-- WHERE status IN ('in_progress', 'planning')
-- ORDER BY priority DESC, started_at ASC;


