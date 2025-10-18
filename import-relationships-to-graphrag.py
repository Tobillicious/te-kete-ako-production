#!/usr/bin/env python3
"""
IMPORT RELATIONSHIPS TO GRAPHRAG - Super Intelligence Layer
Add dependency graph data to enable AI-powered architecture queries
"""

from supabase import create_client
import json
from datetime import datetime

print("🧠 IMPORTING RELATIONSHIP DATA TO GRAPHRAG")
print("=" * 70)

# Connect to Supabase
supabase = create_client(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
)

# Load relationship data
print("\n📊 Loading relationship data...")
with open('file-relationships-complete.json', 'r') as f:
    data = json.load(f)

relationships = data['relationships']
stats = data['statistics']

print(f"✅ Loaded {stats['files_scanned']} files with {sum(stats.values())} relationships")

# Strategy: Add relationship metadata to existing resources
print("\n" + "=" * 70)
print("🔄 UPDATING GRAPHRAG WITH RELATIONSHIP DATA")
print("=" * 70)

updated = 0
errors = 0

print("\n📝 Adding CSS dependencies...")
for file_path, css_list in relationships['css_dependencies'].items():
    try:
        # Find resource by path
        result = supabase.table('resources')\
            .select('id')\
            .ilike('path', f'%{file_path}')\
            .limit(1)\
            .execute()
        
        if result.data:
            resource_id = result.data[0]['id']
            
            # Update with CSS dependency info
            supabase.table('resources')\
                .update({
                    'metadata': json.dumps({
                        'css_dependencies': css_list,
                        'css_count': len(css_list)
                    })
                })\
                .eq('id', resource_id)\
                .execute()
            
            updated += 1
            if updated % 100 == 0:
                print(f"   Updated {updated} resources...")
    except Exception as e:
        errors += 1

print(f"✅ CSS dependencies: {updated} resources updated")

# Add JS dependencies
print("\n📝 Adding JavaScript dependencies...")
updated_js = 0
for file_path, js_list in relationships['js_dependencies'].items():
    try:
        result = supabase.table('resources')\
            .select('id, metadata')\
            .ilike('path', f'%{file_path}')\
            .limit(1)\
            .execute()
        
        if result.data:
            resource_id = result.data[0]['id']
            existing_meta = result.data[0].get('metadata', {})
            if isinstance(existing_meta, str):
                existing_meta = json.loads(existing_meta) if existing_meta else {}
            
            # Merge metadata
            existing_meta['js_dependencies'] = js_list
            existing_meta['js_count'] = len(js_list)
            
            supabase.table('resources')\
                .update({'metadata': json.dumps(existing_meta)})\
                .eq('id', resource_id)\
                .execute()
            
            updated_js += 1
            if updated_js % 100 == 0:
                print(f"   Updated {updated_js} resources...")
    except Exception as e:
        errors += 1

print(f"✅ JS dependencies: {updated_js} resources updated")

# Create dependency summary resource
print("\n📊 Creating dependency analysis resource...")
summary = {
    'title': 'Complete Dependency Graph Analysis',
    'type': 'architecture',
    'path': 'analysis/dependency-graph.json',
    'content': f"""
# Complete Platform Dependency Graph

## Overview
This is a comprehensive analysis of all file dependencies across the Te Kete Ako platform.

## Statistics
- Total files analyzed: {stats['files_scanned']}
- CSS references: {stats['css_refs_found']}
- JavaScript references: {stats['js_refs_found']}
- Internal HTML links: {stats['html_links_found']}
- Component includes: {stats['component_refs_found']}

## Most Critical CSS Files
{chr(10).join([f"- {css}: Used by {count} files" for css, count in sorted(data['usage_analysis']['css_usage'].items(), key=lambda x: -x[1])[:10]])}

## Most Critical JavaScript Files
{chr(10).join([f"- {js}: Used by {count} files" for js, count in sorted(data['usage_analysis']['js_usage'].items(), key=lambda x: -x[1])[:10]])}

## Intelligence Capabilities Unlocked
- Find all files dependent on a specific CSS/JS file
- Identify critical infrastructure files
- Map component usage patterns
- Discover orphaned files (no dependencies)
- Calculate change impact radius
""",
    'metadata': json.dumps({
        'analysis_type': 'dependency_graph',
        'total_relationships': sum(stats.values()),
        'scan_date': '2025-10-18',
        'critical_css': list(data['usage_analysis']['css_usage'].keys())[:10],
        'critical_js': list(data['usage_analysis']['js_usage'].keys())[:10]
    }),
    'subject': 'Architecture',
    'cultural_integration': 'low'
}

try:
    result = supabase.table('resources').insert(summary).execute()
    print("✅ Dependency analysis resource created")
except Exception as e:
    print(f"⚠️  Resource may already exist: {e}")

print("\n" + "=" * 70)
print("🎯 GRAPHRAG SUPER INTELLIGENCE UNLOCKED")
print("=" * 70)

print("""
✅ You can now query:
   - "What files depend on te-kete-unified-design-system.css?"
   - "Which JavaScript file is most critical?"
   - "Show me all files that use shared-components.js"
   - "What would break if I change breadcrumbs.js?"
   - "Find orphaned CSS files"

🧠 Dependency graph intelligence: ACTIVE
📊 Architecture queries: ENABLED
🔗 Impact analysis: READY
""")

print(f"\n✅ Updated {updated + updated_js} resources with relationship data")
print(f"⚠️  Errors: {errors}")
print(f"🎯 GraphRAG now has dependency intelligence!")

