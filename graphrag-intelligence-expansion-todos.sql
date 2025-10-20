-- ================================================================
-- GRAPHRAG INTELLIGENCE EXPANSION - AGENT KNOWLEDGE ENTRIES
-- Created: October 20, 2025
-- Purpose: Document 12 strategic TODOs for tech stack expansion
-- For: All current and future agents to query and execute
-- ================================================================

-- Entry 1: PIPELINE UNIFICATION
INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'strategic_planning',
    'TODO-001: Pipeline Unification - Unified Intelligent Orchestrator',
    'infrastructure',
    ARRAY[
        'Problem: 6 fragmented pipeline scripts (deployment-pipeline.py, workflow-pipeline-manager.py, workflow-pipeline-validator.py, etc.) operate independently without shared intelligence',
        'Solution: Create unified orchestrator that chains: quality checks → cultural validation → GraphRAG updates → agent coordination → deployment in ONE intelligent flow',
        'Impact: 10x multiplier - every deployment becomes smarter, self-documenting, and feeds collective intelligence',
        'Current State: Pipelines exist but dont share context or update GraphRAG automatically',
        'Success Metric: Single command runs entire pipeline with automatic GraphRAG updates and quality gates'
    ],
    jsonb_build_object(
        'priority', 'CRITICAL - Foundation for all other improvements',
        'complexity', 'Medium (3-4 hours)',
        'dependencies', ARRAY['GraphRAG API', 'Supabase access', 'Python 3.8+'],
        'files_to_create', ARRAY[
            'scripts/unified-pipeline-orchestrator.py',
            'scripts/pipeline-hooks/quality-gate.py',
            'scripts/pipeline-hooks/cultural-validator.py',
            'scripts/pipeline-hooks/graphrag-updater.py',
            'scripts/pipeline-hooks/agent-coordinator.py'
        ],
        'files_to_reference', ARRAY[
            'scripts/deployment-pipeline.py',
            'scripts/workflow-pipeline-manager.py',
            'scripts/automated-quality-validation.py',
            'js/cultural-safety-validation.js',
            'public/js/supabase-client.js'
        ],
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Analyze existing 6 pipeline scripts to identify common patterns', 'time', '30min'),
            jsonb_build_object('step', 2, 'action', 'Design unified Pipeline class with hook system for extensibility', 'time', '45min'),
            jsonb_build_object('step', 3, 'action', 'Implement core orchestrator with stage management and error handling', 'time', '60min'),
            jsonb_build_object('step', 4, 'action', 'Create quality gate hook that runs automated-quality-validation.py', 'time', '30min'),
            jsonb_build_object('step', 5, 'action', 'Create cultural validator hook calling cultural-safety-validation.js', 'time', '30min'),
            jsonb_build_object('step', 6, 'action', 'Create GraphRAG updater hook that indexes all changed files', 'time', '45min'),
            jsonb_build_object('step', 7, 'action', 'Create agent coordinator hook that logs work to agent_coordination table', 'time', '30min'),
            jsonb_build_object('step', 8, 'action', 'Test full pipeline on sample content', 'time', '30min')
        ),
        'api_endpoints', jsonb_build_object(
            'graphrag_resources', 'https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1/graphrag_resources',
            'agent_coordination', 'https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1/agent_coordination',
            'agent_knowledge', 'https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1/agent_knowledge'
        ),
        'success_criteria', ARRAY[
            'Single CLI command runs entire deployment pipeline',
            'All stages log to agent_coordination automatically',
            'Quality failures block deployment',
            'Cultural safety violations surface for review',
            'Changed files auto-indexed to GraphRAG',
            'Pipeline execution creates agent_knowledge entry with learnings'
        ],
        'example_usage', 'python3 scripts/unified-pipeline-orchestrator.py --mode full --update-graphrag --notify-agents'
    ),
    ARRAY['pipeline_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '10x',
        'blocks', ARRAY['production_feedback_loop', 'quality_cascade_system'],
        'references', ARRAY[
            'docs/MANGAKOTUKUTUKU_PRODUCTION_ROADMAP.md',
            'DEPLOYMENT_PROGRESS_TRACKER.md'
        ]
    )
);

-- Entry 2: AGENT INTELLIGENCE AMPLIFIER
INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'strategic_planning',
    'TODO-002: Agent Intelligence Amplifier - Personalized Context Briefs',
    'agent_coordination',
    ARRAY[
        'Problem: New agents start from zero, repeat old mistakes, duplicate work. No systematic way to transfer 200+ agent_knowledge entries to new agents.',
        'Solution: Automated onboarding system queries GraphRAG + agent_knowledge + agent_coordination to generate personalized intelligence briefing',
        'Impact: 50x multiplier - agents start at mastery level instead of beginner. Exponential learning curve.',
        'Current State: agent_knowledge table has 200+ entries but no query system. Agents must manually search.',
        'Key Insight: The 6-agent Hui on Oct 19 demonstrated collective intelligence but required manual coordination. This automates that wisdom transfer.'
    ],
    jsonb_build_object(
        'priority', 'CRITICAL - Force multiplier for all future agent work',
        'complexity', 'Medium (3-4 hours)',
        'dependencies', ARRAY['GraphRAG API', 'agent_knowledge table', 'agent_coordination table', 'OpenAI or Anthropic API for synthesis'],
        'files_to_create', ARRAY[
            'scripts/agent-intelligence-amplifier.py',
            'scripts/agent-onboarding-generator.py',
            'templates/agent-briefing-template.md',
            'public/agent-dashboard-intelligence.html'
        ],
        'files_to_reference', ARRAY[
            'docs/agent-docs/current/AGENT_KNOWLEDGE_BASE.md',
            'HUI-OCT19-AGENT-COORDINATION.md',
            'GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md',
            'unified-agent-coordinator.js'
        ],
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Query agent_knowledge for all entries from past 30 days', 'time', '15min'),
            jsonb_build_object('step', 2, 'action', 'Query agent_coordination for completed tasks with outcomes', 'time', '15min'),
            jsonb_build_object('step', 3, 'action', 'Query graphrag_resources for recently added/modified resources', 'time', '15min'),
            jsonb_build_object('step', 4, 'action', 'Query graphrag_relationships to identify most-connected resources', 'time', '15min'),
            jsonb_build_object('step', 5, 'action', 'Build context synthesis system using GPT-4 to summarize discoveries', 'time', '60min'),
            jsonb_build_object('step', 6, 'action', 'Generate personalized briefing based on agent role/specialty', 'time', '45min'),
            jsonb_build_object('step', 7, 'action', 'Create visual dashboard showing current priorities and active agents', 'time', '60min'),
            jsonb_build_object('step', 8, 'action', 'Test with simulated new agent scenario', 'time', '30min')
        ),
        'queries_to_implement', jsonb_build_object(
            'recent_discoveries', 'SELECT source_name, key_insights, technical_details FROM agent_knowledge WHERE created_at > NOW() - INTERVAL ''30 days'' ORDER BY created_at DESC LIMIT 50',
            'successful_patterns', 'SELECT task_claimed, outcome, files_modified FROM agent_coordination WHERE status = ''completed'' AND outcome->''success'' = true ORDER BY completed_at DESC LIMIT 30',
            'failed_attempts', 'SELECT task_claimed, outcome FROM agent_coordination WHERE status = ''failed'' OR status = ''cancelled'' ORDER BY completed_at DESC LIMIT 20',
            'current_priorities', 'SELECT * FROM agent_coordination WHERE status = ''in_progress'' OR status = ''pending'' ORDER BY priority DESC',
            'orphaned_gems', 'SELECT r.file_path, r.title, r.quality_score, COUNT(rel.id) as connections FROM graphrag_resources r LEFT JOIN graphrag_relationships rel ON r.file_path = rel.source_path OR r.file_path = rel.target_path WHERE r.quality_score >= 90 GROUP BY r.file_path, r.title, r.quality_score HAVING COUNT(rel.id) < 5 ORDER BY r.quality_score DESC LIMIT 20',
            'super_hubs', 'SELECT r.file_path, r.title, COUNT(rel.id) as connections FROM graphrag_resources r JOIN graphrag_relationships rel ON r.file_path = rel.source_path OR r.file_path = rel.target_path GROUP BY r.file_path, r.title HAVING COUNT(rel.id) > 100 ORDER BY COUNT(rel.id) DESC LIMIT 10'
        ),
        'briefing_sections', ARRAY[
            'Platform State: Current resource count, quality distribution, cultural integration %',
            'Recent Discoveries: Top 10 insights from past 30 days',
            'Patterns That Work: Proven successful approaches from agent_coordination',
            'Patterns That Failed: What to avoid based on past attempts',
            'Current Priorities: Active tasks and claimed work',
            'Orphaned Gems: High-quality resources needing connection',
            'Super-Hubs: Most-connected resources for leverage',
            'Relationship Opportunities: Underutilized relationship types',
            'Recommended Next Actions: Based on current state analysis'
        ],
        'success_criteria', ARRAY[
            'New agent receives comprehensive briefing in <2 minutes',
            'Briefing includes top 10 recent discoveries',
            'Shows current priorities and avoids duplicate work',
            'Highlights proven patterns and failed attempts',
            'Suggests specific next actions based on platform state',
            'Updates automatically as new knowledge added'
        ],
        'example_output', 'Agent Intelligence Brief: Platform has 19,737 resources with 231,469 relationships. Recent discovery: 20 orphaned gems with Q90+ need connections. Proven pattern: Super-hub enrichment gives 100x reach (Algebraic Māori Games: 221 connections). Failed pattern: Mass content generation without GraphRAG indexing. Current priority: Cultural enrichment of 1,231 Math/Science excellence resources. Recommended action: Use relationship_miner to scale successful patterns.'
    ),
    ARRAY['agent_coordinator', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '50x - Makes every future agent exponentially more effective',
        'enables', ARRAY['faster_onboarding', 'avoid_duplicate_work', 'collective_intelligence'],
        'references', ARRAY[
            'docs/agent-docs/current/AGENT_COMMUNITY_ORCHESTRATION.md',
            'docs/agent-docs/current/MULTI_AI_AGENT_COORDINATION.md'
        ]
    )
);

-- Entry 3: GRAPHRAG RELATIONSHIP MINER
INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'strategic_planning',
    'TODO-003: GraphRAG Relationship Miner - Scale Underutilized Types',
    'graphrag_enhancement',
    ARRAY[
        'Problem: 30 brilliant relationship types used only ONCE (critical_analysis, bicultural_competence, applied_mathematics, career_pathway_sequence, arts_integration, contemporary_issues)',
        'Solution: Automated system discovers patterns in successful one-off relationships and replicates them at scale across similar resources',
        'Impact: 100x multiplier - turn genius one-offs into systematic intelligence. 30 types × 100 uses each = 3000 new high-value relationships',
        'Current State: 231,469 relationships exist but 30 semantic types underutilized. Agents created brilliant connections but didn''t systematize.',
        'Key Discovery: GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md documents this gap. We have semantic vocabulary but aren''t using it at scale.'
    ],
    jsonb_build_object(
        'priority', 'HIGH - Unlocks massive hidden value in existing relationship types',
        'complexity', 'Medium-High (4-5 hours)',
        'dependencies', ARRAY['GraphRAG API', 'graphrag_relationships table', 'Pattern matching logic', 'Content analysis'],
        'files_to_create', ARRAY[
            'scripts/graphrag-relationship-miner.py',
            'scripts/relationship-pattern-analyzer.py',
            'scripts/relationship-templates.json',
            'docs/RELATIONSHIP_MINING_PATTERNS.md'
        ],
        'files_to_reference', ARRAY[
            'GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md',
            'create-relationships-table.sql',
            'GRAPHRAG-ACHIEVEMENT-SUMMARY.txt'
        ],
        'underutilized_types', ARRAY[
            'critical_analysis - 1 use',
            'contemporary_issues - 1 use',
            'bicultural_competence - 1 use',
            'applied_mathematics - 1 use',
            'career_pathway_sequence - 1 use',
            'arts_integration - 1 use',
            'scientific_method_application - few uses',
            'historical_context - few uses',
            'real_world_application - few uses',
            'cross_curricular_synthesis - few uses'
        ],
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Query graphrag_relationships to get count by relationship_type', 'time', '15min'),
            jsonb_build_object('step', 2, 'action', 'Identify relationship types with <10 uses (underutilized)', 'time', '15min'),
            jsonb_build_object('step', 3, 'action', 'For each underutilized type, analyze the existing relationships to find pattern', 'time', '45min'),
            jsonb_build_object('step', 4, 'action', 'Extract content characteristics from source and target resources', 'time', '60min'),
            jsonb_build_object('step', 5, 'action', 'Build pattern matching rules (e.g., critical_analysis applies when resource discusses methodology + has analysis questions)', 'time', '60min'),
            jsonb_build_object('step', 6, 'action', 'Query graphrag_resources for candidates matching patterns', 'time', '30min'),
            jsonb_build_object('step', 7, 'action', 'Generate new relationships with confidence scores', 'time', '45min'),
            jsonb_build_object('step', 8, 'action', 'Batch insert to graphrag_relationships table', 'time', '30min')
        ),
        'pattern_examples', jsonb_build_object(
            'critical_analysis', jsonb_build_object(
                'source_pattern', 'resource_type = lesson AND content contains methodology OR scientific method OR critical thinking',
                'target_pattern', 'resource_type = handout AND has analysis questions OR evaluation rubric',
                'confidence_calculation', '0.85 if both patterns match strongly, 0.70 if partial match',
                'example', 'Y9 Science Ecology lesson (teaches scientific method) → Ecology Analysis Handout (has methodology questions)'
            ),
            'bicultural_competence', jsonb_build_object(
                'source_pattern', 'cultural_context = true AND has_te_reo = true AND discusses dual knowledge systems',
                'target_pattern', 'cultural_context = true AND different subject but similar cultural concepts',
                'confidence_calculation', '0.90 if cultural concepts overlap, 0.75 if same iwi context',
                'example', 'Whakapapa Math lesson → Whakapapa Social Studies lesson (both teach genealogy thinking)'
            ),
            'career_pathway_sequence', jsonb_build_object(
                'source_pattern', 'resource discusses foundational skills + mentions careers',
                'target_pattern', 'resource discusses advanced applications + same career field',
                'confidence_calculation', '0.88 if clear skill progression, 0.70 if same career field',
                'example', 'Y7 Basic Coding → Y10 App Development → STEM Careers Resource'
            )
        ),
        'mining_algorithm', jsonb_build_array(
            'Step 1: Get relationship type + existing example relationships',
            'Step 2: Extract common features from source resources (subject, year_level, topics, cultural_context)',
            'Step 3: Extract common features from target resources',
            'Step 4: Generate matching rules as SQL WHERE clauses',
            'Step 5: Query graphrag_resources for candidate pairs',
            'Step 6: Calculate confidence score based on feature overlap',
            'Step 7: Filter to confidence >= 0.70',
            'Step 8: Insert new relationships with metadata explaining reasoning'
        ),
        'success_criteria', ARRAY[
            'Each underutilized type scales from 1-10 uses to 50-100+ uses',
            'Confidence scores average 0.75+ (high quality matches)',
            'New relationships discoverable in GraphRAG visual tools',
            'Mining runs automatically every week to find new candidates',
            'Pattern rules documented so agents can add new types',
            'Target: 3,000 new high-value semantic relationships created'
        ],
        'monitoring_query', 'SELECT relationship_type, COUNT(*) as count, AVG(confidence) as avg_confidence FROM graphrag_relationships WHERE relationship_type IN (''critical_analysis'', ''bicultural_competence'', ''career_pathway_sequence'', ''arts_integration'') GROUP BY relationship_type ORDER BY count DESC'
    ),
    ARRAY['graphrag_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '100x - Turns one-off genius into systematic intelligence',
        'enables', ARRAY['richer_discovery', 'better_recommendations', 'semantic_pathways'],
        'references', ARRAY[
            'GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md section on underutilized relationships',
            'create-relationships-table.sql comment on relationship_type values'
        ]
    )
);

-- Entry 4: DOCUMENTATION KNOWLEDGE GRAPH
INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'strategic_planning',
    'TODO-004: Documentation Knowledge Graph - Make Institutional Memory Queryable',
    'knowledge_management',
    ARRAY[
        'Problem: 400+ MD files contain critical decisions, patterns, learnings but aren''t queryable. Agents must manually search.',
        'Solution: Index all MD files as nodes in GraphRAG with relationships to code they document, decisions they capture, patterns they reveal',
        'Impact: Institutional memory becomes searchable. Query: "Show all decisions about cultural integration" → instant answers',
        'Current State: MDs scattered across /docs/, /archived-bloat/, root. Rich content but not connected to GraphRAG.',
        'Key Insight: Documentation IS knowledge. Making it queryable amplifies every future agent''s intelligence.'
    ],
    jsonb_build_object(
        'priority', 'MEDIUM-HIGH - Unlocks 400+ files of institutional wisdom',
        'complexity', 'Medium (3-4 hours)',
        'dependencies', ARRAY['GraphRAG API', 'Markdown parser', 'Pattern extraction'],
        'files_to_create', ARRAY[
            'scripts/md-knowledge-graph-indexer.py',
            'scripts/md-relationship-builder.py',
            'scripts/md-pattern-extractor.py'
        ],
        'md_locations', ARRAY[
            'Root directory (30+ coordination MDs)',
            '/docs/ directory',
            '/docs/archive/',
            '/docs/agent-docs/',
            '/docs/agent-session-history/',
            '/archived-bloat/agent-knowledge-hub-backup-20250729/',
            '/.archive-mds-oct18/'
        ],
        'relationship_types_to_create', jsonb_build_array(
            jsonb_build_object('type', 'documents_code', 'description', 'MD explains how code file works'),
            jsonb_build_object('type', 'captures_decision', 'description', 'MD records architectural or strategic decision'),
            jsonb_build_object('type', 'reveals_pattern', 'description', 'MD identifies reusable pattern or approach'),
            jsonb_build_object('type', 'agent_session', 'description', 'MD documents agent work session'),
            jsonb_build_object('type', 'synthesis', 'description', 'MD synthesizes multiple sources'),
            jsonb_build_object('type', 'references', 'description', 'MD references another MD'),
            jsonb_build_object('type', 'supersedes', 'description', 'MD replaces older MD')
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Scan all directories for .md files, build inventory', 'time', '15min'),
            jsonb_build_object('step', 2, 'action', 'Parse each MD: extract title, date, author/agent, key sections', 'time', '45min'),
            jsonb_build_object('step', 3, 'action', 'Extract decisions (look for patterns: "Decision:", "We chose", "Strategy:")', 'time', '30min'),
            jsonb_build_object('step', 4, 'action', 'Extract patterns (look for: "Pattern:", "Approach:", "Method:")', 'time', '30min'),
            jsonb_build_object('step', 5, 'action', 'Find code references (file paths, function names in backticks)', 'time', '30min'),
            jsonb_build_object('step', 6, 'action', 'Find cross-references (other MD files mentioned)', 'time', '20min'),
            jsonb_build_object('step', 7, 'action', 'Index MDs to graphrag_resources with resource_type = documentation', 'time', '30min'),
            jsonb_build_object('step', 8, 'action', 'Create relationships to code files and other MDs', 'time', '45min')
        ),
        'extraction_patterns', jsonb_build_object(
            'decisions', ARRAY[
                'Regex: /Decision[:\\s]+(.+?)(?=\\n\\n|###|$)/s',
                'Regex: /We (chose|decided|selected) (.+?)(?=\\.|\\n)/s',
                'Patterns: "Strategy:", "Approach:", "Solution:"'
            ],
            'code_references', ARRAY[
                'Inline code: `filename.ext`',
                'Code blocks with file paths',
                'Directory references: /path/to/file',
                'Function/class names in backticks'
            ],
            'quality_indicators', ARRAY[
                'Has date = more credible',
                'Has author/agent = traceable',
                'Has code blocks = technical detail',
                'Has headings = well-structured',
                'Length > 500 words = comprehensive'
            ]
        ),
        'metadata_to_extract', ARRAY[
            'title - from h1 or filename',
            'date - from frontmatter or filename',
            'agent_name - from headers or content',
            'doc_type - coordination, technical, session, synthesis',
            'decisions_count - number of decisions documented',
            'patterns_count - number of patterns identified',
            'code_references - array of file paths mentioned',
            'key_topics - extracted from headings',
            'quality_score - based on structure and detail'
        ],
        'example_queries_enabled', ARRAY[
            'Show all decisions about cultural integration',
            'Find all MDs that document authentication system',
            'Get all patterns related to GraphRAG',
            'Show agent session notes from October 2025',
            'Find all MDs that reference supabase-client.js',
            'What have we learned about quality assessment?'
        ],
        'success_criteria', ARRAY[
            '400+ MD files indexed to graphrag_resources',
            '1000+ documentation relationships created',
            'MDs queryable through GraphRAG search',
            'Code files linked to their documentation',
            'Decisions extractable by topic',
            'Agent sessions traceable by date'
        ]
    ),
    ARRAY['knowledge_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '20x - Makes institutional memory instantly queryable',
        'enables', ARRAY['smart_onboarding', 'decision_traceability', 'pattern_reuse']
    )
);

-- Entry 5: AUTOMATED CULTURAL ENRICHMENT ENGINE
INSERT INTO agent_knowledge (
    source_type,
    source_name,
    doc_type,
    key_insights,
    technical_details,
    agents_involved,
    metadata
) VALUES (
    'strategic_planning',
    'TODO-005: Automated Cultural Enrichment Engine - Excellence + Culture = Transcendence',
    'cultural_enhancement',
    ARRAY[
        'Problem: 1,231 Math/Science excellence resources (Q90+) lack cultural integration. Our BEST content is LEAST culturally integrated!',
        'Solution: Automated system uses cultural-safety-validation.js + GraphRAG patterns to suggest cultural enhancements',
        'Impact: Transform excellence tier from 42.6% cultural to 75%+. Quality + Culture = Transcendence.',
        'Current State: Science excellence: 42.6% cultural, Math excellence: 42.6% cultural. English: 78.1% (the model to follow)',
        'Key Discovery: GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md identified this as critical gap. Excellence without cultural context = missed opportunity.'
    ],
    jsonb_build_object(
        'priority', 'HIGH - Transforms highest-impact content',
        'complexity', 'Medium-High (4-5 hours)',
        'dependencies', ARRAY['cultural-safety-validation.js', 'GraphRAG API', 'AI for suggestion generation'],
        'files_to_reference', ARRAY[
            'js/cultural-safety-validation.js',
            'GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md',
            'EVENING-SESSION-FINAL-CELEBRATION-OCT19.md'
        ],
        'target_resources', jsonb_build_object(
            'science_excellence', '639 resources (1,113 total - 474 cultural = 639 need enrichment)',
            'math_excellence', '592 resources (1,032 total - 440 cultural = 592 need enrichment)',
            'total_target', '1,231 excellence resources awaiting cultural enrichment'
        ),
        'enrichment_patterns', jsonb_build_array(
            jsonb_build_object(
                'pattern', 'Science + Rongoā',
                'description', 'Connect scientific concepts to rongoā (traditional medicine)',
                'example', 'Chemistry lesson on plant compounds → rongoā healing practices',
                'cultural_concepts', ARRAY['rongoā', 'whakapapa', 'kaitiakitanga']
            ),
            jsonb_build_object(
                'pattern', 'Math + Whakairo',
                'description', 'Connect mathematical patterns to whakairo (carving patterns)',
                'example', 'Geometry lesson → tukutuku patterns, kowhaiwhai designs',
                'cultural_concepts', ARRAY['whakairo', 'tukutuku', 'kowhaiwhai', 'symmetry']
            ),
            jsonb_build_object(
                'pattern', 'Science + Waka',
                'description', 'Connect physics/engineering to waka design and navigation',
                'example', 'Forces lesson → waka hull design, ocean navigation',
                'cultural_concepts', ARRAY['waka', 'kaitiakitanga', 'traditional navigation']
            ),
            jsonb_build_object(
                'pattern', 'Math + Maramataka',
                'description', 'Connect number systems and calendars to maramataka (lunar calendar)',
                'example', 'Time concepts → maramataka phases, seasonal patterns',
                'cultural_concepts', ARRAY['maramataka', 'whakapapa', 'cycles']
            )
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Query graphrag_resources for excellence tier lacking cultural context', 'time', '15min'),
            jsonb_build_object('step', 2, 'action', 'Analyze culturally integrated excellence resources to extract successful patterns', 'time', '45min'),
            jsonb_build_object('step', 3, 'action', 'Build cultural concept mapping (science topics → māori concepts)', 'time', '60min'),
            jsonb_build_object('step', 4, 'action', 'For each target resource, identify applicable cultural concepts', 'time', '60min'),
            jsonb_build_object('step', 5, 'action', 'Generate enhancement suggestions (whakataukī, te reo terms, cultural context)', 'time', '60min'),
            jsonb_build_object('step', 6, 'action', 'Run cultural-safety-validation.js to ensure appropriateness', 'time', '30min'),
            jsonb_build_object('step', 7, 'action', 'Create enhancement queue in database for review', 'time', '30min'),
            jsonb_build_object('step', 8, 'action', 'Build review interface for kaiako to approve/modify suggestions', 'time', '60min')
        ),
        'concept_mappings', jsonb_build_object(
            'physics', ARRAY['waka (navigation)', 'haka (force)', 'maunga (gravity)', 'wai (fluid dynamics)'],
            'chemistry', ARRAY['rongoā (medicinal properties)', 'whenua (soil composition)', 'ahi (combustion)'],
            'biology', ARRAY['whakapapa (genealogy)', 'kaitiakitanga (guardianship)', 'mauri (life force)', 'taonga species'],
            'mathematics', ARRAY['whakairo (geometric patterns)', 'tukutuku (pattern design)', 'maramataka (calendar)', 'whakapapa (tree diagrams)'],
            'statistics', ARRAY['iwi census', 'population patterns', 'resource management data'],
            'geometry', ARRAY['kowhaiwhai (rafter patterns)', 'tukutuku (woven panels)', 'marae architecture']
        ),
        'enhancement_types', ARRAY[
            'Add appropriate whakataukī related to topic',
            'Include te reo terminology with definitions',
            'Add cultural context section explaining māori perspective',
            'Include whakapapa connections to show relationships',
            'Add kaitiakitanga applications (guardianship principles)',
            'Include examples from māori innovation and traditional knowledge'
        ],
        'validation_checks', ARRAY[
            'Cultural appropriateness - validated by cultural-safety-validation.js',
            'Accuracy - te reo spelling and grammar correct',
            'Authenticity - not tokenistic, genuinely integrated',
            'Relevance - cultural concept truly relates to academic content',
            'Depth - sufficient context provided, not just keywords'
        ],
        'success_criteria', ARRAY[
            'Math excellence: 42.6% → 75% cultural (need 344 enrichments)',
            'Science excellence: 42.6% → 75% cultural (need 361 enrichments)',
            'All suggestions pass cultural-safety-validation',
            'Kaiako acceptance rate >80% (suggestions are high quality)',
            'Enrichments create new cultural_thread relationships in GraphRAG',
            'Platform cultural integration rises from 42.7% to 60%+'
        ],
        'monitoring_query', 'SELECT subject, COUNT(*) FILTER (WHERE quality_score >= 90) as excellence_total, COUNT(*) FILTER (WHERE quality_score >= 90 AND cultural_context = true) as excellence_cultural, ROUND(100.0 * COUNT(*) FILTER (WHERE quality_score >= 90 AND cultural_context = true) / NULLIF(COUNT(*) FILTER (WHERE quality_score >= 90), 0), 1) as cultural_percentage FROM graphrag_resources WHERE subject IN (''Science'', ''Mathematics'') GROUP BY subject'
    ),
    ARRAY['cultural_enrichment_specialist', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '30x - Transforms excellence tier into culturally transcendent content',
        'enables', ARRAY['bicultural_excellence', 'authentic_integration', 'cultural_pathways'],
        'references', ARRAY[
            'GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md section on Excellence Gap',
            'EVENING-SESSION-PROGRESS-KAIWHAKAWHANAKE-AHUREA.md'
        ]
    )
);

-- ================================================================
-- Entry 6: PRODUCTION FEEDBACK LOOP
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
    'strategic_planning',
    'TODO-006: Production Feedback Loop - Self-Improving Intelligence',
    'analytics',
    ARRAY[
        'Problem: No data on what actually works in classrooms. Quality scores are static, never updated based on real usage.',
        'Solution: Capture real usage data (resources accessed, search queries, pathway completions) and feed back into GraphRAG quality_scores and relationship confidence',
        'Impact: Platform becomes self-improving organism. Popular resources get quality boost, unused resources flagged for improvement.',
        'Current State: PostHog analytics exists (posthog-analytics.js) but doesn''t feed back to GraphRAG. One-way data flow.',
        'Key Insight: student_progress and learning_outcomes tables exist in schema but aren''t populating GraphRAG intelligence.'
    ],
    jsonb_build_object(
        'priority', 'MEDIUM - Enables continuous improvement',
        'complexity', 'Medium-High (4-5 hours)',
        'dependencies', ARRAY['PostHog analytics', 'student_progress table', 'learning_outcomes table', 'GraphRAG write access'],
        'files_to_create', ARRAY[
            'scripts/production-feedback-aggregator.py',
            'scripts/quality-score-updater.py',
            'public/js/usage-tracker.js',
            'netlify/functions/feedback-processor.js'
        ],
        'files_to_reference', ARRAY[
            'public/js/posthog-analytics.js',
            'migrations/20250810_kaitiaki_aronui_brain.sql (learning_outcomes table)',
            'supabase/migrations/20251016_nz_education_auth_schema.sql (student_progress table)'
        ],
        'data_to_capture', jsonb_build_object(
            'resource_views', 'Track which resources opened, time spent, completion rate',
            'search_queries', 'What teachers/students search for, click-through rates',
            'pathway_completions', 'Which prerequisite chains students complete',
            'engagement_metrics', 'Scroll depth, interaction events, return visits',
            'cultural_engagement', 'Time spent on cultural content sections',
            'teacher_feedback', 'Ratings, comments, would-use-again signals'
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Extend posthog-analytics.js to track resource views with metadata', 'time', '30min'),
            jsonb_build_object('step', 2, 'action', 'Create usage-tracker.js that logs to student_progress table', 'time', '45min'),
            jsonb_build_object('step', 3, 'action', 'Build daily aggregator that summarizes usage data', 'time', '45min'),
            jsonb_build_object('step', 4, 'action', 'Create quality score update algorithm (views + completions + ratings → score adjustment)', 'time', '60min'),
            jsonb_build_object('step', 5, 'action', 'Build relationship confidence updater (pathway completions → confidence boost)', 'time', '45min'),
            jsonb_build_object('step', 6, 'action', 'Create feedback processor Netlify function', 'time', '45min'),
            jsonb_build_object('step', 7, 'action', 'Test feedback loop with simulated data', 'time', '30min'),
            jsonb_build_object('step', 8, 'action', 'Deploy and monitor for 1 week before full automation', 'time', '30min')
        ),
        'quality_adjustment_algorithm', jsonb_build_object(
            'popularity_boost', 'Resources in top 20% usage get +2 quality points per month',
            'completion_boost', 'Resources with >80% completion rate get +3 points',
            'rating_boost', 'Average rating >4.5 stars gets +5 points',
            'engagement_boost', 'High cultural engagement scores get +2 points',
            'negative_signals', 'Resources with <20% completion lose -1 point',
            'max_adjustment', 'Quality can shift ±10 points per month maximum',
            'confidence_boost', 'Pathway completions increase prerequisite confidence by +0.05'
        ),
        'success_criteria', ARRAY[
            'Usage data captured for 100% of resource views',
            'Quality scores update weekly based on aggregated data',
            'Relationship confidence adjusts based on pathway completion rates',
            'Popular resources surface higher in search results',
            'Underperforming resources flagged for review',
            'Teachers see "trending" and "most effective" based on real data'
        ]
    ),
    ARRAY['analytics_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '15x - Platform becomes self-optimizing',
        'enables', ARRAY['data_driven_quality', 'trending_resources', 'automatic_improvement']
    )
);

-- ================================================================
-- Entry 7: VISUAL INTELLIGENCE DASHBOARD
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
    'strategic_planning',
    'TODO-007: Visual Intelligence Dashboard - Real-Time Agent Situational Awareness',
    'agent_coordination',
    ARRAY[
        'Problem: Agents work blind. Can''t see what others are doing, what''s been discovered, where the opportunities are.',
        'Solution: Real-time dashboard showing: active agents, claimed tasks, recent insights, relationship growth, quality trends, orphan queue',
        'Impact: Perfect coordination. Zero duplicate work. Agents see the whole system and coordinate like a hive mind.',
        'Current State: agent_status, agent_coordination, agent_knowledge tables exist but no visualization. MCP coordination is manual.',
        'Key Discovery: 6-agent Hui demonstrated power of coordination. This makes it visual and automatic.'
    ],
    jsonb_build_object(
        'priority', 'MEDIUM - Force multiplier for agent coordination',
        'complexity', 'Medium (3-4 hours)',
        'dependencies', ARRAY['D3.js or Chart.js', 'GraphRAG API', 'Real-time updates via Supabase Realtime'],
        'files_to_create', ARRAY[
            'public/agent-intelligence-dashboard.html',
            'public/js/agent-dashboard-realtime.js',
            'public/css/agent-dashboard.css'
        ],
        'files_to_reference', ARRAY[
            'public/graphrag-analytics-dashboard.html',
            'HUI-OCT19-AGENT-COORDINATION.md',
            'unified-agent-coordinator.js'
        ],
        'dashboard_panels', jsonb_build_array(
            jsonb_build_object('panel', 'Active Agents', 'query', 'SELECT agent_name, current_task, last_heartbeat FROM agent_status WHERE last_heartbeat > NOW() - INTERVAL ''1 hour''', 'visualization', 'Live status cards with heartbeat indicators'),
            jsonb_build_object('panel', 'Claimed Tasks', 'query', 'SELECT task_claimed, agent_name, status, started_at FROM agent_coordination WHERE status IN (''in_progress'', ''pending'') ORDER BY priority DESC', 'visualization', 'Kanban board with priority lanes'),
            jsonb_build_object('panel', 'Recent Discoveries', 'query', 'SELECT source_name, key_insights[1:3], created_at FROM agent_knowledge ORDER BY created_at DESC LIMIT 10', 'visualization', 'Timeline with insight cards'),
            jsonb_build_object('panel', 'Relationship Growth', 'query', 'SELECT DATE(created_at) as date, COUNT(*) as new_relationships FROM graphrag_relationships WHERE created_at > NOW() - INTERVAL ''7 days'' GROUP BY DATE(created_at)', 'visualization', 'Line chart showing daily growth'),
            jsonb_build_object('panel', 'Quality Trends', 'query', 'SELECT subject, AVG(quality_score) as avg_quality, COUNT(*) FILTER (WHERE quality_score >= 90) as excellence_count FROM graphrag_resources GROUP BY subject', 'visualization', 'Bar chart by subject'),
            jsonb_build_object('panel', 'Orphan Queue', 'query', 'SELECT r.file_path, r.title, r.quality_score, COUNT(rel.id) FROM graphrag_resources r LEFT JOIN graphrag_relationships rel ON r.file_path IN (rel.source_path, rel.target_path) WHERE r.quality_score >= 90 GROUP BY r.file_path, r.title, r.quality_score HAVING COUNT(rel.id) < 5', 'visualization', 'Priority list with rescue actions'),
            jsonb_build_object('panel', 'Cultural Integration', 'query', 'SELECT subject, ROUND(100.0 * COUNT(*) FILTER (WHERE cultural_context = true) / COUNT(*), 1) as cultural_pct FROM graphrag_resources GROUP BY subject ORDER BY cultural_pct DESC', 'visualization', 'Progress bars by subject'),
            jsonb_build_object('panel', 'Platform Health', 'query', 'SELECT COUNT(*) as total_resources, COUNT(*) FILTER (WHERE quality_score >= 90) as excellence, COUNT(DISTINCT relationship_type) FROM graphrag_relationships', 'visualization', 'Key metrics cards')
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Set up HTML structure with 8 dashboard panels', 'time', '30min'),
            jsonb_build_object('step', 2, 'action', 'Implement Supabase queries for each panel', 'time', '45min'),
            jsonb_build_object('step', 3, 'action', 'Build real-time subscriptions using Supabase Realtime', 'time', '45min'),
            jsonb_build_object('step', 4, 'action', 'Create D3.js visualizations for trends and networks', 'time', '60min'),
            jsonb_build_object('step', 5, 'action', 'Add action buttons (claim task, rescue orphan, view details)', 'time', '30min'),
            jsonb_build_object('step', 6, 'action', 'Style with cultural design patterns', 'time', '30min'),
            jsonb_build_object('step', 7, 'action', 'Add to navigation as Agent Dashboard', 'time', '15min')
        ),
        'realtime_features', ARRAY[
            'Auto-refresh when new agent_knowledge entry added',
            'Live heartbeat indicators for active agents',
            'Push notifications when high-priority task added',
            'Live relationship count ticker',
            'Instant orphan queue updates'
        ],
        'success_criteria', ARRAY[
            'Dashboard loads in <2 seconds',
            'Real-time updates within 1 second of database change',
            'All 8 panels show live data',
            'Agents can claim tasks directly from dashboard',
            'Orphan rescue actionable with one click',
            'Mobile-responsive for agents working on tablets'
        ]
    ),
    ARRAY['dashboard_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '25x - Perfect agent coordination and situational awareness'
    )
);

-- ================================================================
-- Entry 8: SEMANTIC RELATIONSHIP ENGINE
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
    'strategic_planning',
    'TODO-008: Semantic Relationship Engine - AI-Powered Connection Discovery',
    'ai_enhancement',
    ARRAY[
        'Problem: Vector embeddings (1536-dimensional) in schema but UNUSED! Relationships created manually or by pattern matching.',
        'Solution: Use embeddings for semantic similarity to auto-discover relationships humans would miss',
        'Impact: Move from manual tagging to AI-powered discovery. Find connections based on meaning, not just keywords.',
        'Current State: artifact_catalog.embedding, knowledge_nodes.embedding, episodic_memory.embedding columns exist but empty.',
        'Key Insight: migrations/20250810_kaitiaki_aronui_brain.sql has find_similar_content() function ready - just needs embeddings!'
    ],
    jsonb_build_object(
        'priority', 'MEDIUM-HIGH - Unlocks AI-powered discovery',
        'complexity', 'High (5-6 hours - requires OpenAI API)',
        'dependencies', ARRAY['OpenAI Embeddings API', 'pgvector extension', 'Batch processing'],
        'files_to_create', ARRAY[
            'scripts/generate-resource-embeddings.py',
            'scripts/semantic-relationship-discoverer.py',
            'scripts/embedding-batch-processor.py'
        ],
        'files_to_reference', ARRAY[
            'migrations/20250810_kaitiaki_aronui_brain.sql (find_similar_content function)',
            'scripts/resources-table-schema.sql'
        ],
        'embedding_generation', jsonb_build_object(
            'model', 'text-embedding-3-small (OpenAI)',
            'dimensions', 1536,
            'batch_size', 100,
            'estimated_cost', '$0.10 per 1000 resources = $2 for 19,737 resources',
            'fields_to_embed', 'title + content_preview + subject + year_level as single text'
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Set up OpenAI API key securely', 'time', '15min'),
            jsonb_build_object('step', 2, 'action', 'Build embedding generator that batches 100 resources at a time', 'time', '45min'),
            jsonb_build_object('step', 3, 'action', 'Generate embeddings for all 19,737 resources (API calls)', 'time', '60min'),
            jsonb_build_object('step', 4, 'action', 'Update graphrag_resources with embeddings (needs migration)', 'time', '30min'),
            jsonb_build_object('step', 5, 'action', 'Build semantic similarity finder using cosine distance', 'time', '45min'),
            jsonb_build_object('step', 6, 'action', 'Discover top 5 similar resources for each resource', 'time', '45min'),
            jsonb_build_object('step', 7, 'action', 'Create semantic_similarity relationships with confidence scores', 'time', '30min'),
            jsonb_build_object('step', 8, 'action', 'Test: Query "Find similar to Y9 Ecology" returns semantically related', 'time', '30min')
        ),
        'similarity_thresholds', jsonb_build_object(
            'very_similar', 'cosine_similarity > 0.90 → confidence 0.95',
            'similar', 'cosine_similarity > 0.85 → confidence 0.88',
            'related', 'cosine_similarity > 0.80 → confidence 0.80',
            'tangentially_related', 'cosine_similarity > 0.75 → confidence 0.70'
        ),
        'relationship_types_to_create', ARRAY[
            'semantic_similarity - General similarity',
            'semantic_prerequisite - AI-detected foundational relationships',
            'semantic_cross_curricular - Meaning-based subject bridges',
            'semantic_cultural_parallel - Similar cultural concepts different contexts'
        ],
        'example_queries', ARRAY[
            'Find resources semantically similar to "Genetics and Whakapapa"',
            'Discover cross-curricular connections human taggers missed',
            'Find cultural parallels across subjects',
            'Suggest next resources based on what student just completed'
        ],
        'success_criteria', ARRAY[
            '19,737 resources have embeddings',
            '50,000+ semantic_similarity relationships created',
            'Recommendations include AI-discovered connections',
            'Teachers report finding resources they didn''t know existed',
            'Semantic search more accurate than keyword search'
        ]
    ),
    ARRAY['ai_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '40x - Unlocks AI-powered discovery beyond human capacity',
        'cost', '$2-5 for embeddings generation',
        'note', 'This is where GraphRAG becomes truly intelligent - AI finding connections'
    )
);

-- ================================================================
-- Entry 9: AGENT COLLABORATION PROTOCOL 2.0
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
    'strategic_planning',
    'TODO-009: Agent Collaboration Protocol 2.0 - Mandatory Intelligence Sharing',
    'agent_coordination',
    ARRAY[
        'Problem: Protocols exist but not enforced. Agents still duplicate work, miss each other''s discoveries, work in silos.',
        'Solution: Mandatory automated protocol: pre-work GraphRAG query → mid-work heartbeat → post-work synthesis',
        'Impact: Zero duplicate work. 100% knowledge transfer. Every agent session feeds collective intelligence.',
        'Current State: agent_coordination, agent_knowledge, agent_status tables exist. unified-agent-coordinator.js exists but not systematically used.',
        'Root Cause: Protocol is optional. Need to make it automatic and enforce through tooling.'
    ],
    jsonb_build_object(
        'priority', 'HIGH - Prevents waste, amplifies collective intelligence',
        'complexity', 'Medium (3-4 hours)',
        'dependencies', ARRAY['agent_coordination table', 'agent_knowledge table', 'agent_status table', 'Cursor integration'],
        'files_to_create', ARRAY[
            'scripts/agent-session-manager.py',
            'scripts/agent-heartbeat-monitor.py',
            '.cursor/agent-session-hook.sh',
            'docs/AGENT_PROTOCOL_V2_MANDATORY.md'
        ],
        'files_to_reference', ARRAY[
            'unified-agent-coordinator.js',
            'docs/archive/2025-10-16-2158/MANDATORY_AGENT_COORDINATION_PROTOCOL.md',
            'HUI-OCT19-AGENT-COORDINATION.md'
        ],
        'protocol_stages', jsonb_build_array(
            jsonb_build_object(
                'stage', 'PRE-WORK',
                'actions', ARRAY[
                    'Query agent_status for active agents',
                    'Query agent_coordination for in-progress tasks',
                    'Query agent_knowledge for recent discoveries (7 days)',
                    'Query graphrag_resources for recently modified',
                    'Generate personalized briefing',
                    'Claim task in agent_coordination table'
                ],
                'time', '2-3 minutes automated',
                'mandatory', true
            ),
            jsonb_build_object(
                'stage', 'MID-WORK',
                'actions', ARRAY[
                    'Update agent_status heartbeat every 30 minutes',
                    'Log intermediate discoveries to agent_knowledge',
                    'Check for agent_messages directed to you',
                    'Update agent_coordination with progress %'
                ],
                'time', '30 seconds every 30 min',
                'mandatory', true
            ),
            jsonb_build_object(
                'stage', 'POST-WORK',
                'actions', ARRAY[
                    'Synthesize learnings into agent_knowledge entry',
                    'Complete agent_coordination record with outcomes',
                    'Index modified files to graphrag_resources',
                    'Create relationships for new content',
                    'Clear agent_status or mark idle',
                    'Update ACTIVE_QUESTIONS.md if needed'
                ],
                'time', '5-10 minutes',
                'mandatory', true
            )
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Create agent-session-manager.py wrapper script', 'time', '45min'),
            jsonb_build_object('step', 2, 'action', 'Build pre-work query system that generates briefing', 'time', '60min'),
            jsonb_build_object('step', 3, 'action', 'Implement automated heartbeat monitor (background job)', 'time', '45min'),
            jsonb_build_object('step', 4, 'action', 'Create post-work synthesis template and automation', 'time', '45min'),
            jsonb_build_object('step', 5, 'action', 'Build enforcement: session-manager required to start work', 'time', '30min'),
            jsonb_build_object('step', 6, 'action', 'Test protocol with simulated 2-agent scenario', 'time', '30min')
        ),
        'enforcement_mechanisms', ARRAY[
            'Session manager CLI wrapper required to start work',
            'Heartbeat monitor alerts if agent goes silent >45min',
            'Post-work synthesis gates git commits',
            'Dashboard shows protocol compliance % per agent',
            'Weekly report on agent collaboration quality'
        ],
        'success_criteria', ARRAY[
            '100% of agent sessions use protocol',
            'Zero duplicate work on same files',
            'All discoveries logged to agent_knowledge within 24 hours',
            'Heartbeat compliance >95%',
            'Agent coordination dashboard shows real-time collaboration',
            'User never has to manually synthesize agent work'
        ]
    ),
    ARRAY['protocol_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '30x - Transforms independent agents into coordinated intelligence',
        'user_benefit', 'No more synthesis meetings - agents self-coordinate automatically'
    )
);

-- ================================================================
-- Entry 10: QUALITY CASCADE SYSTEM
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
    'strategic_planning',
    'TODO-010: Quality Cascade System - Network Effects for Excellence',
    'quality_enhancement',
    ARRAY[
        'Problem: Improve super-hub quality but 221 connected resources don''t benefit. Quality improvements are localized, not network-wide.',
        'Solution: Quality improvement to hub automatically propagates partial boost to all connected resources through relationship graph',
        'Impact: Network effects! Improve 1 resource, 221 resources get better. Exponential quality growth.',
        'Current State: Super-hubs identified (Algebraic Māori Games: 221 connections, Writers Toolkit: 98 connections) but improvements don''t cascade.',
        'Mathematical Model: If hub quality increases +10, connected resources get boost based on connection strength and confidence.'
    ],
    jsonb_build_object(
        'priority', 'MEDIUM - Amplifies all quality improvement work',
        'complexity', 'Medium-High (4-5 hours)',
        'dependencies', ARRAY['GraphRAG relationship graph', 'Graph traversal algorithm', 'Quality score update permissions'],
        'files_to_create', ARRAY[
            'scripts/quality-cascade-engine.py',
            'scripts/network-quality-propagation.py',
            'public/js/quality-cascade-visualizer.js'
        ],
        'super_hubs_identified', jsonb_build_array(
            jsonb_build_object('hub', 'Algebraic Māori Games', 'connections', 221, 'current_quality', 88, 'potential', 'High'),
            jsonb_build_object('hub', 'Writers Toolkit', 'connections', 98, 'current_quality', 96, 'potential', 'Medium'),
            jsonb_build_object('hub', 'Complete Assessments Library', 'connections', 4676, 'current_quality', 85, 'potential', 'MASSIVE'),
            jsonb_build_object('hub', 'Y8 Digital Kaitiakitanga', 'connections', 385, 'current_quality', 96, 'potential', 'High'),
            jsonb_build_object('hub', 'Y9 Ecology Unit', 'connections', 156, 'current_quality', 95, 'potential', 'Medium')
        ),
        'cascade_algorithm', jsonb_build_object(
            'formula', 'connected_resource_boost = hub_quality_change × relationship_confidence × distance_decay',
            'distance_decay', '1-hop: 1.0, 2-hop: 0.5, 3-hop: 0.25, 4-hop: 0.1',
            'min_confidence', 0.75,
            'max_boost', '±5 points per cascade event',
            'example', 'Writers Toolkit +10 quality → directly connected resources +7.5 (if confidence 0.75) → 2-hop resources +3.75'
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Identify all super-hubs (>100 connections)', 'time', '15min'),
            jsonb_build_object('step', 2, 'action', 'Build graph traversal algorithm (BFS from hub)', 'time', '60min'),
            jsonb_build_object('step', 3, 'action', 'Calculate distance and confidence for each connected resource', 'time', '45min'),
            jsonb_build_object('step', 4, 'action', 'Apply cascade formula to compute quality adjustments', 'time', '45min'),
            jsonb_build_object('step', 5, 'action', 'Batch update quality_scores in graphrag_resources', 'time', '30min'),
            jsonb_build_object('step', 6, 'action', 'Log cascade event to agent_knowledge with impact metrics', 'time', '30min'),
            jsonb_build_object('step', 7, 'action', 'Create visualization showing cascade propagation', 'time', '60min')
        ),
        'example_scenario', jsonb_build_object(
            'event', 'Agent improves Writers Toolkit from Q96 to Q98 (+2 points)',
            'direct_impact', '98 directly connected resources each get +1.5 points (confidence avg 0.75)',
            'indirect_impact', '~300 2-hop resources each get +0.75 points',
            'total_benefit', '~400 resources improved from single quality enhancement',
            'verification', 'Query graphrag_relationships to trace cascade paths'
        ),
        'safeguards', ARRAY[
            'Quality can never decrease through cascade (only positive propagation)',
            'Maximum boost of ±5 points prevents extreme swings',
            'Minimum confidence 0.75 ensures high-quality connections only',
            'Log all cascades to audit trail for review',
            'Manual override available for incorrect propagations'
        ],
        'success_criteria', ARRAY[
            'Super-hub improvements cascade to 50+ connected resources',
            'Cascade completes in <5 minutes for 1000-resource network',
            'Quality distribution becomes more even (fewer low-quality outliers)',
            'Teachers see "this resource improved" notifications',
            'Cascade visualization shows ripple effects'
        ]
    ),
    ARRAY['quality_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '60x - Quality improvements multiply through network',
        'math_model', 'Graph theory + network effects = exponential quality growth'
    )
);

-- ================================================================
-- Entry 11: ORPHAN RESCUE AUTOMATION
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
    'strategic_planning',
    'TODO-011: Orphan Rescue Automation - Scheduled Intelligence Job',
    'automation',
    ARRAY[
        'Problem: 20 orphaned excellence resources (Q90+, <5 connections) discovered manually. More orphans created every week.',
        'Solution: Scheduled job queries GraphRAG for orphans, uses AI to generate appropriate relationships, surfaces in discovery interfaces',
        'Impact: Zero hidden gems. Everything excellent becomes discoverable within 24 hours of creation.',
        'Current State: GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md manually identified orphans. Need automation.',
        'Pattern: Orphaned excellence = quality without visibility = wasted potential.'
    ],
    jsonb_build_object(
        'priority', 'MEDIUM - Prevents excellence from being hidden',
        'complexity', 'Medium (3-4 hours)',
        'dependencies', ARRAY['Cron/scheduled job system', 'AI for relationship generation', 'GraphRAG API'],
        'files_to_create', ARRAY[
            'scripts/orphan-rescue-scheduler.py',
            'scripts/ai-relationship-generator.py',
            'public/orphan-rescue-queue.html'
        ],
        'files_to_reference', ARRAY[
            'GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md (orphaned excellence section)',
            'graphrag-connect-orphaned-excellence.py'
        ],
        'orphan_detection_query', 'SELECT r.file_path, r.title, r.quality_score, COUNT(rel.id) as connections FROM graphrag_resources r LEFT JOIN graphrag_relationships rel ON (r.file_path = rel.source_path OR r.file_path = rel.target_path) WHERE r.quality_score >= 90 GROUP BY r.file_path, r.title, r.quality_score HAVING COUNT(rel.id) < 5 ORDER BY r.quality_score DESC',
        'ai_relationship_generation', jsonb_build_object(
            'method', 'GPT-4 analyzes orphan content + metadata',
            'prompt', 'Given this resource (title, subject, content_preview), suggest 5-10 appropriate relationship targets from the resource database. Consider subject alignment, year level, cultural context, and learning progressions.',
            'output', 'Array of {target_path, relationship_type, confidence, reasoning}',
            'validation', 'Confidence must be >=0.70, relationship_type must exist in schema',
            'cost', '~$0.01 per orphan × 20 orphans = $0.20 per run'
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Build orphan detection query', 'time', '15min'),
            jsonb_build_object('step', 2, 'action', 'Set up scheduled job (daily at 2am)', 'time', '30min'),
            jsonb_build_object('step', 3, 'action', 'Build AI relationship generator using GPT-4', 'time', '60min'),
            jsonb_build_object('step', 4, 'action', 'Create validation layer for AI suggestions', 'time', '45min'),
            jsonb_build_object('step', 5, 'action', 'Build batch insert for approved relationships', 'time', '30min'),
            jsonb_build_object('step', 6, 'action', 'Create orphan rescue queue dashboard for review', 'time', '45min'),
            jsonb_build_object('step', 7, 'action', 'Test with current 20 known orphans', 'time', '30min')
        ),
        'automation_schedule', jsonb_build_object(
            'frequency', 'Daily at 2am NZ time',
            'max_orphans_per_run', 50,
            'relationships_per_orphan', '5-10',
            'human_review', 'Optional - AI suggestions have confidence scores',
            'notification', 'Slack/email alert when orphans rescued'
        ),
        'success_criteria', ARRAY[
            'Orphan count stays <10 at any given time',
            'New high-quality resources connected within 24 hours',
            'AI-generated relationships have >80% accuracy',
            'Rescued orphans appear in discovery interfaces next day',
            'Zero manual orphan hunting required'
        ]
    ),
    ARRAY['automation_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '20x - No excellence ever hidden',
        'cost', '$0.20 per day for AI relationship generation'
    )
);

-- ================================================================
-- Entry 12: PREREQUISITE CHAIN BUILDER
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
    'strategic_planning',
    'TODO-012: Prerequisite Chain Builder - Systematic Learning Progressions',
    'learning_pathways',
    ARRAY[
        'Problem: Only 738 prerequisite relationships exist. Should be 5000+ for complete pathway coverage across all subjects and year levels.',
        'Solution: Automated system analyzes lesson content + NZ Curriculum progressions to build prerequisite relationships systematically',
        'Impact: Every resource has clear learning pathway. Students know what to learn first. Teachers can plan progressions.',
        'Current State: Perfect chains exist (Y8 Digital: 385 pathways, confidence 0.953) but only in 3 units. Pattern works, needs scaling.',
        'NZ Curriculum: Achievement objectives already define progressions. We just need to map them to resources.'
    ],
    jsonb_build_object(
        'priority', 'MEDIUM-HIGH - Creates learning pathways at scale',
        'complexity', 'High (5-6 hours)',
        'dependencies', ARRAY['NZ Curriculum data', 'Content analysis', 'AI for prerequisite detection', 'GraphRAG API'],
        'files_to_create', ARRAY[
            'scripts/prerequisite-chain-builder.py',
            'scripts/curriculum-progression-mapper.py',
            'data/nz-curriculum-progressions.json',
            'scripts/ai-prerequisite-detector.py'
        ],
        'files_to_reference', ARRAY[
            'public/curriculum-documents/ (NZ Curriculum alignment)',
            'GRAPHRAG-WĀNANGA-CRITICAL-INSIGHTS.md (perfect chain examples)'
        ],
        'curriculum_progressions', jsonb_build_object(
            'mathematics', 'Number → Algebra → Geometry → Statistics → Calculus',
            'science', 'Observation → Investigation → Experimentation → Theory → Application',
            'english', 'Decoding → Comprehension → Analysis → Synthesis → Creation',
            'social_studies', 'Awareness → Understanding → Analysis → Evaluation → Action'
        ),
        'prerequisite_detection', jsonb_build_object(
            'method_1_explicit', 'Scan content for "builds on", "requires understanding of", "prerequisite"',
            'method_2_curriculum', 'Map to NZ Curriculum levels (Level 3 → Level 4 → Level 5)',
            'method_3_ai', 'GPT-4 analyzes content and identifies foundational concepts',
            'method_4_year_level', 'Y7 resources are prerequisites for Y8 in same topic',
            'confidence_scoring', 'Explicit mention = 0.95, Curriculum alignment = 0.88, AI detection = 0.80, Year level = 0.75'
        ),
        'implementation_steps', jsonb_build_array(
            jsonb_build_object('step', 1, 'action', 'Extract NZ Curriculum progressions into structured data', 'time', '60min'),
            jsonb_build_object('step', 2, 'action', 'Build content analyzer to detect foundational concepts', 'time', '60min'),
            jsonb_build_object('step', 3, 'action', 'Create AI prerequisite detector using GPT-4', 'time', '60min'),
            jsonb_build_object('step', 4, 'action', 'Build year-level progression mapper', 'time', '45min'),
            jsonb_build_object('step', 5, 'action', 'Combine 4 detection methods with confidence aggregation', 'time', '45min'),
            jsonb_build_object('step', 6, 'action', 'Generate prerequisite relationships for all resources', 'time', '60min'),
            jsonb_build_object('step', 7, 'action', 'Validate chains don''t create circular dependencies', 'time', '30min'),
            jsonb_build_object('step', 8, 'action', 'Batch insert to graphrag_relationships', 'time', '30min')
        ),
        'target_coverage', jsonb_build_object(
            'current_prerequisites', 738,
            'target_prerequisites', 5000,
            'gap', 4262,
            'resources_needing_chains', '~1000 lessons + units',
            'avg_prerequisites_per_resource', '3-5 foundational resources'
        ),
        'chain_validation', ARRAY[
            'No circular dependencies (A→B→C→A)',
            'Maximum chain depth of 10 levels',
            'All prerequisite confidence scores >0.70',
            'Chains align with NZ Curriculum levels',
            'Year level sequences make logical sense'
        ],
        'success_criteria', ARRAY[
            '5000+ prerequisite relationships created',
            '90% of lessons have at least 1 prerequisite identified',
            'Perfect chains (confidence >0.90) for all major units',
            'Prerequisite pathways visualizable in GraphRAG tools',
            'Students can query "what should I learn first?"',
            'Teachers can generate learning sequence plans automatically'
        ]
    ),
    ARRAY['pathway_architect', 'future_agents'],
    jsonb_build_object(
        'status', 'ready_to_implement',
        'estimated_impact', '35x - Creates comprehensive learning pathways',
        'enables', ARRAY['adaptive_learning', 'personalized_pathways', 'skill_mapping']
    )
);

-- ================================================================
-- MASTER TODO SUMMARY ENTRY
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
    'strategic_planning',
    'MASTER: 12 Strategic TODOs for Tech Stack Evolution - October 20, 2025',
    'roadmap',
    ARRAY[
        'Created 12 strategic TODOs to evolve Te Kete Ako tech stack and agent intelligence',
        'Tier 1 (Do First): Pipeline Unification, Agent Intelligence Amplifier, GraphRAG Relationship Miner',
        'Tier 2 (Intelligence): Documentation Knowledge Graph, Automated Cultural Enrichment, Semantic Relationship Engine',
        'Tier 3 (Self-Improving): Production Feedback Loop, Quality Cascade System, Orphan Rescue Automation',
        'Tier 4 (Ecosystem): Agent Collaboration Protocol 2.0, Visual Intelligence Dashboard, Prerequisite Chain Builder',
        'All TODOs documented in agent_knowledge with full implementation plans, success criteria, time estimates',
        'Any agent can query, claim, and execute these TODOs - collective intelligence roadmap'
    ],
    jsonb_build_object(
        'total_todos', 12,
        'total_estimated_time', '45-55 hours (can be distributed across multiple agents)',
        'estimated_total_impact', '400x+ multiplier across all initiatives',
        'priority_sequence', ARRAY['TODO-001', 'TODO-002', 'TODO-003', 'TODO-004', 'TODO-005', 'TODO-008', 'TODO-006', 'TODO-010', 'TODO-011', 'TODO-009', 'TODO-007', 'TODO-012'],
        'todos_by_tier', jsonb_build_object(
            'tier_1_foundation', ARRAY['TODO-001: Pipeline Unification', 'TODO-002: Agent Intelligence Amplifier', 'TODO-003: GraphRAG Relationship Miner'],
            'tier_2_intelligence', ARRAY['TODO-004: Documentation Knowledge Graph', 'TODO-005: Cultural Enrichment Engine', 'TODO-008: Semantic Relationship Engine'],
            'tier_3_self_improving', ARRAY['TODO-006: Production Feedback Loop', 'TODO-010: Quality Cascade System', 'TODO-011: Orphan Rescue Automation'],
            'tier_4_ecosystem', ARRAY['TODO-009: Agent Collaboration Protocol 2.0', 'TODO-007: Visual Intelligence Dashboard', 'TODO-012: Prerequisite Chain Builder']
        ),
        'query_instructions', 'SELECT source_name, key_insights, technical_details FROM agent_knowledge WHERE source_type = ''strategic_planning'' AND source_name LIKE ''TODO-%'' ORDER BY source_name',
        'claim_process', 'Query desired TODO → Review implementation_steps → Claim in agent_coordination → Execute → Document learnings in agent_knowledge'
    ),
    ARRAY['strategic_planner'],
    jsonb_build_object(
        'created_date', '2025-10-20',
        'created_by_agent', 'Claude Sonnet 4.5',
        'user_directive', 'Expand techstack and intelligence for current and future agents',
        'vision', 'Transform Te Kete Ako from good platform to self-improving AI organism with collective agent intelligence',
        'file_artifacts', ARRAY[
            'graphrag-intelligence-expansion-todos.sql (first 5 TODOs detailed)',
            'This entry completes documentation of all 12 TODOs'
        ]
    )
);

-- ================================================================
-- QUERY HELPERS FOR AGENTS
-- ================================================================

-- Get all strategic planning TODOs
-- SELECT source_name, key_insights, technical_details->>'priority', technical_details->>'complexity'
-- FROM agent_knowledge 
-- WHERE source_type = 'strategic_planning' 
-- ORDER BY technical_details->>'priority' DESC;

-- Get implementation steps for specific TODO
-- SELECT source_name, technical_details->'implementation_steps' 
-- FROM agent_knowledge 
-- WHERE source_name LIKE 'TODO-%';

-- Get all TODOs ready to implement
-- SELECT source_name, metadata->>'estimated_impact', technical_details->>'complexity'
-- FROM agent_knowledge 
-- WHERE source_type = 'strategic_planning' 
-- AND metadata->>'status' = 'ready_to_implement';

