-- MAP ALL HEGELIAN SYNTHESIS MD RELATIONSHIPS
-- Based on 51 synthesis documents + complete MD analysis

-- TIER 1: FOUNDATIONAL SYNTHESES
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
VALUES
-- Core Dialectic Syntheses
('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-01-CORE-PARADOXES.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'contributes_foundational_law', 0.99, 
 '{"laws_contributed": ["Law #1: Reality ≠ Documentation", "Law #6: Built ≠ Integrated"], "paradoxes_resolved": 5}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-02-WORKFLOW-PATTERNS.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'contributes_foundational_law', 0.99, 
 '{"laws_contributed": ["Law #2: Value > Effort", "Law #3: Automate > Manual"], "patterns_found": 5}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-03-STRATEGIC-EVOLUTION.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'contributes_foundational_law', 0.99, 
 '{"laws_contributed": ["Law #4: Ship > Plan"], "evolution_patterns": 5}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-04-COLLABORATION-PATTERNS.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'contributes_foundational_law', 0.99, 
 '{"laws_contributed": ["Law #5: Coordinate Smart", "Law #10: Boundaries"], "coordination_insights": 5}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-05-ERROR-RECOVERY.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'contributes_foundational_law', 0.99, 
 '{"laws_contributed": ["Law #8: Root Cause > Symptoms"], "error_patterns": 6, "key_insight": "Built for AI, broken for humans"}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-06-QUALITY-CONTENT.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'contributes_foundational_law', 0.99, 
 '{"laws_contributed": ["Law #7: Discovery > Creation"], "hidden_value": "$250K+", "content_patterns": 6}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-07-AUTONOMOUS-DEPLOYMENT.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'contributes_foundational_law', 0.99, 
 '{"laws_contributed": ["Law #9: Autonomy > Instruction"], "deployment_patterns": 6}'),

-- Meta Syntheses
('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-META-FINAL-WISDOM.md', 
 'docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'synthesizes_into', 0.98, 
 '{"synthesis_level": "meta", "principles_discovered": 5}'),

('docs/hegelian_synthesis/META-META-SYNTHESIS-COMPLETE-JOURNEY.md', 
 'docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-META-FINAL-WISDOM.md', 
 'recursive_synthesis_of', 1.0, 
 '{"synthesis_level": "meta-meta", "recursive_depth": 3, "validates_itself": true}'),

-- Ultimate Synthesis
('docs/hegelian_synthesis/ULTIMATE-SYNTHESIS-SIMULATION-DRIVEN.md', 
 'docs/hegelian_synthesis/META-META-SYNTHESIS-COMPLETE-JOURNEY.md', 
 'evolved_into', 0.99, 
 '{"added_component": "simulation_framework", "sessions_simulated": 2500}'),

-- TIER 2: IMPLEMENTATION PLANS
('docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'docs/hegelian_synthesis/IMPLEMENTATION-PLAN-01-IMMEDIATE-ACTIONS.md', 
 'informs_implementation', 0.95, 
 '{"timeline": "24 hours", "actions": "Ship to beta, unblock features"}'),

('docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'docs/hegelian_synthesis/IMPLEMENTATION-PLAN-02-DOCUMENTATION-CONSOLIDATION.md', 
 'informs_implementation', 0.95, 
 '{"timeline": "2-3 hours", "actions": "Consolidate 1,313 → 20 files"}'),

('docs/hegelian_synthesis/MASTER-WISDOM-CONSOLIDATION-FINAL.md', 
 'docs/hegelian_synthesis/IMPLEMENTATION-PLAN-03-FRONTEND-INTEGRATION.md', 
 'informs_implementation', 0.95, 
 '{"timeline": "4-6 hours", "actions": "Close 35% integration gap"}'),

-- TIER 3: NAVIGATION & DESIGN INSIGHTS
('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-05-ERROR-RECOVERY.md', 
 '🧠-HEGELIAN-NAVIGATION-ANALYSIS.md', 
 'identifies_design_problem', 0.98, 
 '{"problem": "Built for AI, broken for humans", "solution": "Human-first design, remove AI elements"}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-01-CORE-PARADOXES.md', 
 '🧠-HEGELIAN-NAVIGATION-ANALYSIS.md', 
 'identifies_css_problem', 0.98, 
 '{"problem": "CSS 95% built, 60% integrated", "solution": "Revert to older/simpler CSS"}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-06-QUALITY-CONTENT.md', 
 '🧠-HEGELIAN-NAVIGATION-ANALYSIS.md', 
 'validates_curation_strategy', 0.97, 
 '{"principle": "Discovery > Creation", "action": "Hide 90%, show Top 50"}'),

-- TIER 4: SIMULATION FINDINGS
('docs/hegelian_synthesis/ULTIMATE-SYNTHESIS-SIMULATION-DRIVEN.md', 
 'COMPREHENSIVE-BETA-SIMULATION-REPORT.md', 
 'led_to_simulation', 0.99, 
 '{"sessions": 2500, "findings": "Download ≠ Use problem, Decision paralysis"}'),

('COMPREHENSIVE-BETA-SIMULATION-REPORT.md', 
 '🎯-SIMULATION-KEY-FINDINGS.md', 
 'analyzes_into', 0.98, 
 '{"critical_finding": "44% classroom use - need Quick Start guides"}'),

('🎯-SIMULATION-KEY-FINDINGS.md', 
 '🔮-FUTURE-IMPROVEMENTS-ROADMAP.md', 
 'creates_roadmap_from', 0.97, 
 '{"large_issues": 6, "quick_wins": 12, "total_scope": "1500+ hours"}'),

-- TIER 5: EXECUTION & DEPLOYMENT
('docs/hegelian_synthesis/IMPLEMENTATION-PLAN-01-IMMEDIATE-ACTIONS.md', 
 'docs/hegelian_synthesis/P0-EXECUTION-PROGRESS.md', 
 'executed_as', 0.99, 
 '{"tasks_complete": "12/12", "status": "100% execution"}'),

('docs/hegelian_synthesis/P0-EXECUTION-PROGRESS.md', 
 '🎊-COMPLETE-SESSION-DEPLOYMENT-READY.md', 
 'resulted_in_deployment', 1.0, 
 '{"deployment_status": "LIVE", "url": "https://tekete.netlify.app"}'),

-- TIER 6: NAVIGATION SPECIFIC RELATIONSHIPS
('🧠-HEGELIAN-NAVIGATION-ANALYSIS.md', 
 'public/index.html', 
 'recommends_changes_to', 0.95, 
 '{"changes": ["Teaching dropdown", "Simplify hero", "Hide 90% resources", "Remove AI elements"]}'),

('docs/hegelian_synthesis/DIALECTIC-SYNTHESIS-05-ERROR-RECOVERY.md', 
 'public/components/teaching-content-dropdown.html', 
 'informs_creation_of', 0.90, 
 '{"principle": "Simple navigation for humans, not AI"}'),

-- CROSS-SYNTHESIS RELATIONSHIPS
('docs/hegelian_synthesis/SYNTHESIS-EXECUTIVE-SUMMARY.md', 
 'docs/hegelian_synthesis/README.md', 
 'summarizes_for', 0.95, 
 '{"purpose": "Quick navigation to all syntheses"}'),

('docs/hegelian_synthesis/INDEX-AND-NAVIGATION.md', 
 'docs/hegelian_synthesis/QUICK-START-FROM-SYNTHESIS.md', 
 'provides_fast_path_to', 0.93, 
 '{"read_time": "5 minutes", "key_laws": 5}');

-- Count relationships created
SELECT COUNT(*) as relationships_mapped FROM graphrag_relationships
WHERE source_path LIKE '%hegelian%' OR target_path LIKE '%hegelian%';

