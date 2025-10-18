#!/usr/bin/env python3
"""
Update GraphRAG with Comprehensive Audit Findings
Adds all discovery data to the knowledge graph
"""

from supabase import create_client
from datetime import datetime
import json

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🧠 Updating GraphRAG with Comprehensive Audit Findings")
print("=" * 60)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Audit findings to add to GraphRAG
audit_entries = [
    {
        'title': 'Comprehensive Creative Audit October 2025',
        'description': 'Complete codebase investigation revealing: 526 duplicate titles (67% duplication), 13.2% cross-linking rate, 1,219 files NOT in GraphRAG (84.9%), 172 orphaned lessons, 5 hidden gem directories with 20 resources. Platform quality: 87% Gold/Professional tier across 23 units.',
        'path': '/COMPREHENSIVE-CREATIVE-AUDIT-OCT18.md',
        'type': 'assessment',
        'subject': 'platform-audit',
        'level': 'comprehensive',
        'tags': ['audit', 'platform-quality', 'graphrag-coverage', 'duplication-analysis', 'accessibility'],
        'curriculum_alignment': 'platform_health',
        'cultural_elements': json.dumps({
            'cultural_integration': 'high',
            'maori_concepts': ['kaitiakitanga', 'whakapapa', 'tino rangatiratanga'],
            'cultural_depth_score': 2.0
        }),
        'estimated_duration_minutes': 120,
        'author': 'Multi-Agent Creative Investigation Team',
        'is_active': True
    },
    {
        'title': 'Hidden Gems: Experiences Directory',
        'description': '13 valuable interactive experiences discovered: adaptive pathways, cultural assessment, curriculum alignment tools. Currently orphaned, needs integration into main navigation.',
        'path': '/public/experiences/',
        'type': 'interactive',
        'subject': 'professional-development',
        'level': 'all-levels',
        'tags': ['hidden-gems', 'experiences', 'adaptive-learning', 'cultural-assessment'],
        'curriculum_alignment': 'cross_curricular',
        'cultural_elements': json.dumps({
            'cultural_integration': 'high',
            'maori_concepts': ['kaitiakitanga']
        }),
        'estimated_duration_minutes': 60,
        'author': 'Deep Site Investigation',
        'is_active': True
    },
    {
        'title': 'Interactive Tools: Generators Hub',
        'description': 'Crossword and wordsearch generators for creating custom educational games. Hidden in /tools/ directory, needs featuring.',
        'path': '/public/tools/',
        'type': 'interactive',
        'subject': 'educational-tools',
        'level': 'all-levels',
        'tags': ['hidden-gems', 'tools', 'game-generators', 'interactive'],
        'curriculum_alignment': 'cross_curricular',
        'cultural_elements': json.dumps({
            'cultural_integration': 'low'
        }),
        'estimated_duration_minutes': 30,
        'author': 'Deep Site Investigation',
        'is_active': True
    },
    {
        'title': 'Duplication Report: 526 Duplicate Titles',
        'description': 'Critical finding: 526 duplicate titles across 780 unique titles (67% duplication rate). Examples: 404.html in 3 locations, about.html duplicated 3x. Requires systematic deduplication.',
        'path': '/deep-investigation-report.json',
        'type': 'assessment',
        'subject': 'technical-health',
        'level': 'platform',
        'tags': ['duplication', 'cleanup-required', 'technical-debt'],
        'curriculum_alignment': 'platform_health',
        'cultural_elements': json.dumps({
            'cultural_integration': 'low'
        }),
        'estimated_duration_minutes': 240,
        'author': 'Deep Site Investigation',
        'is_active': True
    },
    {
        'title': 'GraphRAG Coverage Gap Analysis',
        'description': 'Only 15.1% of codebase (217 files) indexed in GraphRAG. 1,219 files NOT indexed (84.9%). Urgent action required to index remaining content for discoverability.',
        'path': '/graphrag-content-analysis.json',
        'type': 'assessment',
        'subject': 'graphrag',
        'level': 'platform',
        'tags': ['graphrag', 'coverage-gap', 'indexing-required'],
        'curriculum_alignment': 'platform_health',
        'cultural_elements': json.dumps({
            'cultural_integration': 'low'
        }),
        'estimated_duration_minutes': 180,
        'author': 'GraphRAG Content Analyzer',
        'is_active': True
    },
    {
        'title': 'Relationship Mapping: 383 Lesson-Handout Connections',
        'description': '383 lessons successfully mapped to handouts, 189 prerequisite chains discovered, 24 Māori cultural concepts connecting resources (whakapapa: 13, tino rangatiratanga: 8, kaitiakitanga: 8). Strong foundation for learning pathways.',
        'path': '/graphrag-relationships.json',
        'type': 'assessment',
        'subject': 'relationships',
        'level': 'platform',
        'tags': ['relationships', 'prerequisites', 'cultural-connections', 'learning-pathways'],
        'curriculum_alignment': 'cross_curricular',
        'cultural_elements': json.dumps({
            'cultural_integration': 'high',
            'maori_concepts': ['whakapapa', 'tino rangatiratanga', 'kaitiakitanga', 'mana', 'te tiriti']
        }),
        'estimated_duration_minutes': 90,
        'author': 'GraphRAG Relationship Mapper',
        'is_active': True
    },
    {
        'title': 'Year Level Coverage Gap: Y11-13',
        'description': 'Zero content for senior secondary (Y11, Y12, Y13). Current coverage: Y7 (4 units), Y8 (3), Y9 (3), Y10 (2). Senior market opportunity untapped.',
        'path': '/deep-investigation-report.json',
        'type': 'assessment',
        'subject': 'coverage-analysis',
        'level': 'strategic',
        'tags': ['year-levels', 'coverage-gaps', 'senior-secondary', 'expansion-opportunity'],
        'curriculum_alignment': 'nzc_levels_5_6_7',
        'cultural_elements': json.dumps({
            'cultural_integration': 'medium'
        }),
        'estimated_duration_minutes': 60,
        'author': 'Deep Site Investigation',
        'is_active': True
    },
    {
        'title': 'Orphaned Lessons: 172 Require Unit Integration',
        'description': '172 lessons not integrated into any unit structure. Primarily Y8 Systems lessons, digital kaitiakitanga, and science ecology content. High-quality content needing organization.',
        'path': '/graphrag-content-analysis.json',
        'type': 'assessment',
        'subject': 'content-organization',
        'level': 'platform',
        'tags': ['orphaned-content', 'unit-integration', 'organization-required'],
        'curriculum_alignment': 'cross_curricular',
        'cultural_elements': json.dumps({
            'cultural_integration': 'variable'
        }),
        'estimated_duration_minutes': 300,
        'author': 'GraphRAG Content Analyzer',
        'is_active': True
    },
    {
        'title': 'Accessibility Audit: Critical Issues Found',
        'description': 'Zero alt text found (critical accessibility failure), only 1 ARIA label, minimal heading structure validation. Requires immediate remediation for WCAG compliance.',
        'path': '/deep-investigation-report.json',
        'type': 'assessment',
        'subject': 'accessibility',
        'level': 'platform',
        'tags': ['accessibility', 'wcag', 'alt-text-missing', 'aria-labels', 'critical'],
        'curriculum_alignment': 'platform_health',
        'cultural_elements': json.dumps({
            'cultural_integration': 'low'
        }),
        'estimated_duration_minutes': 360,
        'author': 'Deep Site Investigation',
        'is_active': True
    },
    {
        'title': 'Unit Clusters Discovered: 6 Natural Groupings',
        'description': 'Y8-unknown (148 resources), Y8-technology (68), Y7-mathematics (32), Y9-science (32), Y7-science (7), Y9-unknown (6). Ready for structured unit creation.',
        'path': '/graphrag-content-analysis.json',
        'type': 'assessment',
        'subject': 'content-clusters',
        'level': 'strategic',
        'tags': ['clusters', 'unit-creation', 'content-organization', 'natural-groupings'],
        'curriculum_alignment': 'cross_curricular',
        'cultural_elements': json.dumps({
            'cultural_integration': 'variable'
        }),
        'estimated_duration_minutes': 180,
        'author': 'GraphRAG Content Analyzer',
        'is_active': True
    }
]

# Insert each audit entry into GraphRAG
added_count = 0
failed_count = 0

for entry in audit_entries:
    try:
        result = supabase.table('resources').insert(entry).execute()
        print(f"✅ Added: {entry['title'][:50]}...")
        added_count += 1
    except Exception as e:
        print(f"⚠️  Failed: {entry['title'][:50]}... ({str(e)[:50]})")
        failed_count += 1

print("\n" + "=" * 60)
print(f"📊 GraphRAG Update Summary:")
print(f"   ✅ Successfully added: {added_count} entries")
print(f"   ⚠️  Failed: {failed_count} entries")
print(f"   📈 Total new knowledge: {added_count} audit findings")

print("\n✨ GraphRAG now contains comprehensive audit knowledge!")
print("   - Platform quality metrics")
print("   - Hidden gems locations")
print("   - Coverage gaps identified")
print("   - Relationship mappings")
print("   - Accessibility issues")
print("   - Strategic opportunities")
