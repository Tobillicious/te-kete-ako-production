#!/usr/bin/env python3
"""
🧭 BUILD NAVIGATION FROM GRAPHRAG
Create comprehensive navigation hubs that link to ALL resources in GraphRAG
"""

import json
from pathlib import Path

# We'll use MCP Supabase via SQL files instead of direct queries

print("🧭 BUILDING NAVIGATION FROM GRAPHRAG")
print("=" * 70)

# Create navigation structure based on GraphRAG data
NAVIGATION_STRUCTURE = {
    'subjects': {
        'Mathematics': {
            'hub_file': 'public/mathematics-hub.html',
            'description': 'Mathematics resources with cultural integration',
            'icon': '🔢'
        },
        'Science': {
            'hub_file': 'public/science-hub.html',
            'description': 'Science lessons integrated with mātauranga Māori',
            'icon': '🔬'
        },
        'English': {
            'hub_file': 'public/english-hub.html',
            'description': 'English lessons with pūrākau and cultural narratives',
            'icon': '📚'
        },
        'Social Studies': {
            'hub_file': 'public/social-studies-hub.html',
            'description': 'Social studies with Treaty and cultural history',
            'icon': '🏛️'
        },
        'Digital Technologies': {
            'hub_file': 'public/digital-technologies-hub.html',
            'description': 'Digital tech with data sovereignty and ethics',
            'icon': '💻'
        },
        'Te Ao Māori': {
            'hub_file': 'public/te-ao-maori-hub.html',
            'description': 'Mātauranga Māori across all subjects',
            'icon': '🌿'
        },
        'Health & PE': {
            'hub_file': 'public/health-pe-hub.html',
            'description': 'Health and PE with Te Whare Tapa Whā',
            'icon': '🏃'
        },
        'Arts': {
            'hub_file': 'public/arts-hub.html',
            'description': 'Arts with cultural expression and whakairo',
            'icon': '🎨'
        }
    }
}

# Generate SQL to get resources by subject
sql_query = """
-- Get all high-quality resources by subject
SELECT 
    subject,
    resource_type,
    title,
    file_path,
    quality_score,
    year_level,
    cultural_context,
    COUNT(*) OVER (PARTITION BY subject) as subject_count
FROM graphrag_resources
WHERE quality_score >= 85
  AND resource_type IN ('Lesson', 'Handout', 'Unit')
  AND file_path LIKE '%public/%'
ORDER BY subject, quality_score DESC, title;
"""

# Save query for manual execution
Path('graphrag_queries').mkdir(exist_ok=True)
with open('graphrag_queries/get_nav_resources.sql', 'w') as f:
    f.write(sql_query)

print("✅ Navigation query saved to: graphrag_queries/get_nav_resources.sql")
print("\n📝 Next steps:")
print("1. Run query via MCP Supabase")
print("2. Generate hub pages from results")
print("3. Link all resources in navigation")
print("\n🎯 This will make ALL 17K+ resources discoverable!")

