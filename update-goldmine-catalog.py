#!/usr/bin/env python3
"""
UPDATE GOLDMINE CATALOG
Add specific treasure details after manual review
"""

from supabase import create_client
import json
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

# MANUALLY REVIEWED TREASURES
treasures = [
    {
        'name': 'Virtual Marae Training Protocol',
        'file': 'public/experiences/virtual-marae.html',
        'type': 'revolutionary_cultural_tool',
        'value': 'EXTREMELY HIGH - Unique in NZ education',
        'features': [
            'VR/AR marae protocol training',
            'MCP multi-agent development framework',
            'Complete cultural protocols (Pōwhiri, Whakatau, Tikanga, Karakia, Hongi)',
            'Community liaison protocols',
            'Assessment rubrics',
            'Audio/language learning',
            'Mobile and cross-platform'
        ],
        'unique_aspects': [
            'Only virtual marae training system in NZ',
            'Respectfully handles sacred cultural elements',
            'Connects digital learning to real marae visits',
            'Built-in kaumātua validation process'
        ],
        'status': 'complete_but_hidden',
        'potential_impact': 'Could serve 100+ NZ schools without marae access',
        'line_count': 661,
        'quality': 'world_class'
    },
    {
        'name': 'Living Whakapapa Interactive Tool',
        'file': 'public/experiences/living-whakapapa.html',
        'type': 'interactive_cultural_experience',
        'value': 'HIGH - Connects students to cultural identity',
        'status': 'placeholder_only',
        'note': 'Title and structure exist, content says "Coming Soon"',
        'potential': 'Interactive genealogy tool - very valuable if completed',
        'quality': 'incomplete'
    },
    {
        'name': 'Adaptive Learning Pathways System',
        'file': 'public/experiences/adaptive-pathways.html',
        'type': 'ai_personalization_engine',
        'value': 'VERY HIGH - Modern EdTech feature',
        'features': [
            'AI-powered personalization',
            'Initial assessment system',
            'Dynamic content delivery',
            'Continuous adaptation based on progress',
            'Cultural context awareness',
            'Optimal difficulty adjustment'
        ],
        'flow': 'Assessment → Personalization → Content → Adaptation',
        'status': 'framework_complete',
        'quality': 'professional',
        'potential_impact': 'Differentiated learning for all students'
    },
    {
        'name': 'Dropdown Mega Menu Code',
        'file': 'archived-bloat/master-files-oct14-pre-enhancement/*.master',
        'type': 'ui_component',
        'value': 'MEDIUM - Good UX but replaced with better system',
        'features': [
            'Grid-based dropdown',
            'Card UI with icons',
            'Visual unit showcase',
            'Hover animations'
        ],
        'status': 'archived_extractable',
        'note': 'Lost in CSS migration but code preserved',
        'potential_use': 'Could merge with current navigation for visual enhancement'
    }
]

print("\n💎 UPDATING GOLDMINE CATALOG")
print("=" * 70)
print(f"Adding {len(treasures)} manually reviewed treasures\n")

# Save detailed catalog
catalog = {
    'catalog_date': datetime.now().isoformat(),
    'review_method': 'manual_file_by_file',
    'reviewer': 'collaborative_agent',
    'total_treasures': len(treasures),
    'treasures': treasures,
    'summary': {
        'world_class': len([t for t in treasures if t.get('quality') == 'world_class']),
        'professional': len([t for t in treasures if t.get('quality') == 'professional']),
        'incomplete': len([t for t in treasures if t.get('quality') == 'incomplete']),
        'extremely_high_value': len([t for t in treasures if 'EXTREMELY HIGH' in t.get('value', '')]),
        'very_high_value': len([t for t in treasures if 'VERY HIGH' in t.get('value', '')])
    }
}

# Save locally
with open('DETAILED-TREASURE-CATALOG.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✅ Detailed catalog saved: DETAILED-TREASURE-CATALOG.json")

# Try GraphRAG
try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    for treasure in treasures:
        entry = {
            'agent_name': f"treasure-cataloger-{treasure['type']}",
            'task_claimed': f"Cataloged: {treasure['name']}",
            'status': 'documented',
            'key_decisions': treasure
        }
        supabase.table('agent_coordination').insert(entry).execute()
    
    print(f"✅ Saved {len(treasures)} treasures to GraphRAG")
    
except Exception as e:
    print(f"⚠️  GraphRAG error: {e}")

print("\n📊 TREASURE SUMMARY:")
for name, treasure in enumerate(treasures, 1):
    print(f"  {name}. {treasure['name']}")
    print(f"     Value: {treasure['value']}")
    print(f"     Status: {treasure['status']}")
    print()

print("\n🎯 READY FOR:")
print("  1. Feature Virtual Marae (world-class, unique)")
print("  2. Complete Living Whakapapa (placeholder only)")
print("  3. Highlight Adaptive Pathways (professional)")
print("  4. Consider restoring dropdown menu code")

