#!/usr/bin/env python3
"""
🎓 AGENT ONBOARDING GENERATOR
Generates personalized intelligence briefs for agents based on specialty

Usage:
    python3 scripts/agent-onboarding-generator.py --specialty cultural-enrichment
    python3 scripts/agent-onboarding-generator.py --specialty graphrag-relationships
    python3 scripts/agent-onboarding-generator.py --specialty content-creation
    python3 scripts/agent-onboarding-generator.py --name "Kaitiaki-Aronui" --specialty cultural

Dependencies: agent-intelligence-amplifier.py, templates/agent-briefing-template.md
"""

import sys
import os
import argparse
from datetime import datetime
from pathlib import Path

def load_template():
    """Load the briefing template"""
    template_path = Path(__file__).parent.parent / 'templates' / 'agent-briefing-template.md'
    
    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        sys.exit(1)
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def get_specialty_focus(specialty):
    """Get recommended focus areas based on specialty"""
    specialty_map = {
        'cultural-enrichment': {
            'mission': 'Boost cultural integration across Math, Science, and English subjects',
            'priority_todos': ['TODO-005: Automated Cultural Enrichment Engine'],
            'quick_wins': [
                'Add whakataukī to high-quality Math/Science lessons',
                'Connect resources with shared cultural elements',
                'Flag rongoā, waka, whakairo content for cultural context'
            ],
            'strategic_work': [
                'Build cultural concept mapping (science topics → māori concepts)',
                'Create cultural_thread relationships',
                'Target 1,231 Math/Science excellence resources for enrichment'
            ],
            'success_metrics': [
                'Math excellence: 42.6% → 75% cultural',
                'Science excellence: 42.6% → 75% cultural',
                'Platform cultural: 42.7% → 60%+'
            ]
        },
        'graphrag-relationships': {
            'mission': 'Scale underutilized relationship types and build learning pathways',
            'priority_todos': [
                'TODO-003: GraphRAG Relationship Miner',
                'TODO-012: Prerequisite Chain Builder'
            ],
            'quick_wins': [
                'Create prerequisite relationships for isolated lessons',
                'Build cross_curricular_link connections',
                'Scale underutilized types (critical_analysis, bicultural_competence, etc.)'
            ],
            'strategic_work': [
                'Mine patterns from successful one-off relationships',
                'Build prerequisite chains for all 1,000+ lessons',
                'Create career_pathway_sequence relationships'
            ],
            'success_metrics': [
                'Prerequisite relationships: 738 → 5,000+',
                '30 underutilized types scaled from 1 use → 50-100+ uses',
                'Learning pathways visualizable for all major units'
            ]
        },
        'content-creation': {
            'mission': 'Create new lessons, handouts, and units aligned with NZ Curriculum',
            'priority_todos': ['TODO-011: Orphan Rescue Automation'],
            'quick_wins': [
                'Add handouts for lessons that lack them',
                'Create unit overview pages for orphaned lessons',
                'Complete House Leader units (Hērangi, Ngata, etc.)'
            ],
            'strategic_work': [
                'Build Year 11-13 senior content',
                'Create guided inquiry projects',
                'Develop assessment frameworks'
            ],
            'success_metrics': [
                'Zero orphaned lessons (all in units)',
                'All units have 5-8 week sequences',
                'House Leader units 100% complete'
            ]
        },
        'pipeline-automation': {
            'mission': 'Unify and automate deployment and quality pipelines',
            'priority_todos': [
                'TODO-001: Pipeline Unification',
                'TODO-006: Production Feedback Loop'
            ],
            'quick_wins': [
                'Chain existing pipeline scripts',
                'Add GraphRAG update hooks to deployment',
                'Automate cultural safety validation'
            ],
            'strategic_work': [
                'Build unified orchestrator',
                'Create quality gates',
                'Implement self-improving feedback loops'
            ],
            'success_metrics': [
                'Single command runs entire pipeline',
                'Quality failures block deployment',
                'Changed files auto-indexed to GraphRAG'
            ]
        },
        'agent-coordination': {
            'mission': 'Improve multi-agent collaboration and knowledge sharing',
            'priority_todos': [
                'TODO-009: Agent Collaboration Protocol 2.0',
                'TODO-007: Visual Intelligence Dashboard'
            ],
            'quick_wins': [
                'Update agent_status heartbeats',
                'Log session work to agent_knowledge',
                'Send coordination messages via agent_messages'
            ],
            'strategic_work': [
                'Build mandatory coordination protocol',
                'Create visual coordination dashboard',
                'Implement automated knowledge synthesis'
            ],
            'success_metrics': [
                '100% agent sessions use protocol',
                'Zero duplicate work on same files',
                'All discoveries logged within 24 hours'
            ]
        },
        'quality-improvement': {
            'mission': 'Enhance resource quality and create excellence pathways',
            'priority_todos': ['TODO-010: Quality Cascade System'],
            'quick_wins': [
                'Fix broken links in high-quality resources',
                'Add missing metadata',
                'Complete placeholder content'
            ],
            'strategic_work': [
                'Build quality cascade propagation',
                'Improve super-hubs (benefit ripples to 100+ resources)',
                'Create network quality multipliers'
            ],
            'success_metrics': [
                'Super-hub improvements cascade to 50+ connected resources',
                'Quality distribution more even',
                'Fewer low-quality outliers'
            ]
        },
        'ai-semantic': {
            'mission': 'Implement AI-powered semantic discovery using embeddings',
            'priority_todos': ['TODO-008: Semantic Relationship Engine'],
            'quick_wins': [
                'Test OpenAI embeddings API',
                'Generate embeddings for sample resources',
                'Test semantic similarity queries'
            ],
            'strategic_work': [
                'Generate embeddings for all 19,737 resources',
                'Build semantic similarity finder',
                'Create 50,000+ semantic_similarity relationships'
            ],
            'success_metrics': [
                'All resources have embeddings',
                '50,000+ semantic relationships created',
                'Semantic search more accurate than keyword'
            ]
        }
    }
    
    return specialty_map.get(specialty, specialty_map['content-creation'])

def generate_brief(agent_name, specialty):
    """Generate personalized brief for agent"""
    
    print(f"🎓 GENERATING ONBOARDING BRIEF FOR: {agent_name}")
    print(f"   Specialty: {specialty}")
    print()
    
    template = load_template()
    focus = get_specialty_focus(specialty)
    
    # Replace template variables
    brief = template.replace('{{AGENT_NAME}}', agent_name)
    brief = brief.replace('{{TIMESTAMP}}', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    brief = brief.replace('{{AGENT_SPECIALTY}}', specialty)
    brief = brief.replace('{{MISSION_DESCRIPTION}}', focus['mission'])
    
    # Build priority recommendations
    priority_recs = f"**Your Top Priority TODOs:**\n"
    for todo in focus['priority_todos']:
        priority_recs += f"- {todo}\n"
    priority_recs += f"\n**Quick Wins (30-60 min each):**\n"
    for win in focus['quick_wins']:
        priority_recs += f"- {win}\n"
    priority_recs += f"\n**Strategic Work (3-5 hours each):**\n"
    for work in focus['strategic_work']:
        priority_recs += f"- {work}\n"
    
    brief = brief.replace('{{PRIORITY_RECOMMENDATIONS}}', priority_recs)
    
    # Add quick win recommendation
    quick_win = f"**Recommended:** {focus['quick_wins'][0]}\n\n"
    quick_win += f"**Why:** Fast impact, builds momentum, demonstrates value\n"
    quick_win += f"**Time:** 30-60 minutes\n"
    
    brief = brief.replace('{{QUICK_WIN_RECOMMENDATION}}', quick_win)
    
    # Add strategic recommendation
    if focus['priority_todos']:
        strategic = f"**Recommended:** {focus['priority_todos'][0]}\n\n"
        strategic += f"**Why:** High-impact work aligned with your specialty\n"
        strategic += f"**Time:** 3-4 hours\n"
    else:
        strategic = "Query agent_knowledge for strategic_planning TODOs"
    
    brief = brief.replace('{{STRATEGIC_RECOMMENDATION}}', strategic)
    
    # Add cultural recommendation
    cultural = "**Recommended:** Add whakataukī and cultural context to 10 Math/Science excellence resources\n\n"
    cultural += "**Why:** Excellence + Culture = Transcendence\n"
    cultural += "**Time:** 2-3 hours\n"
    
    brief = brief.replace('{{CULTURAL_RECOMMENDATION}}', cultural)
    
    # Add placeholders for dynamic content (would be filled by amplifier script)
    brief = brief.replace('{{TOTAL_RESOURCES}}', '19,737')
    brief = brief.replace('{{TOTAL_RELATIONSHIPS}}', '231,469')
    brief = brief.replace('{{CULTURAL_PERCENTAGE}}', '42.7')
    brief = brief.replace('{{EXCELLENCE_COUNT}}', '5,379')
    brief = brief.replace('{{RECENT_DISCOVERIES}}', '*(Run agent-intelligence-amplifier.py for real-time data)*')
    brief = brief.replace('{{SUCCESSFUL_PATTERNS}}', '*(Run agent-intelligence-amplifier.py for real-time data)*')
    brief = brief.replace('{{FAILED_PATTERNS}}', '*(Query agent_coordination WHERE status = \'failed\')*')
    brief = brief.replace('{{ORPHANED_RESOURCES}}', '*(Run agent-intelligence-amplifier.py for real-time orphan detection)*')
    brief = brief.replace('{{SUPER_HUBS}}', '*(Complete Assessments Library: 4,676 connections | Adaptive Learning Pathways: 1,617 connections)*')
    brief = brief.replace('{{ACTIVE_AGENTS}}', '*(Run agent-intelligence-amplifier.py for real-time agent status)*')
    brief = brief.replace('{{STRATEGIC_TODOS}}', '*(Query agent_knowledge WHERE source_type = \'strategic_planning\')*')
    brief = brief.replace('{{UNDERUTILIZED_RELATIONSHIPS}}', '*(30 types with <10 uses each - see TODO-003)*')
    
    return brief

def main():
    parser = argparse.ArgumentParser(description='Generate personalized agent onboarding brief')
    parser.add_argument('--name', default='New Agent', help='Agent name')
    parser.add_argument('--specialty', required=True, 
                       choices=['cultural-enrichment', 'graphrag-relationships', 'content-creation', 
                               'pipeline-automation', 'agent-coordination', 'quality-improvement', 'ai-semantic'],
                       help='Agent specialty area')
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("🎓 AGENT ONBOARDING GENERATOR")
    print("=" * 80)
    print()
    
    brief = generate_brief(args.name, args.specialty)
    
    # Save to file
    safe_name = args.name.lower().replace(' ', '-').replace('_', '-')
    safe_specialty = args.specialty.lower().replace('_', '-')
    output_file = f"agent-brief-{safe_specialty}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(brief)
    
    print("=" * 80)
    print(f"✅ PERSONALIZED BRIEF GENERATED: {output_file}")
    print("=" * 80)
    print()
    print(f"🎯 {args.name} is now ready to work on {args.specialty}!")
    print("📚 Brief includes:")
    print("   - Platform state snapshot")
    print("   - Specialty-specific mission and priorities")
    print("   - Quick wins and strategic work recommendations")
    print("   - Coordination protocol reminder")
    print()
    print("🧠 50x INTELLIGENCE MULTIPLIER ACTIVATED!")
    print()
    print("🚀 Next Steps:")
    print(f"   1. Read {output_file}")
    print("   2. Query agent_coordination to check for active tasks")
    print("   3. Choose a TODO or quick win from brief")
    print("   4. Claim task in agent_coordination")
    print("   5. START BUILDING!")
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled by user")
        sys.exit(0)

