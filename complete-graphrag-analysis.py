#!/usr/bin/env python3
"""
COMPLETE GRAPHRAG ANALYSIS
Fully understand what's in the knowledge graph before proceeding
"""

from supabase import create_client
import json
from collections import defaultdict

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🔍 COMPLETE GRAPHRAG ANALYSIS")
print("=" * 70)
print()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get ALL resources
print("📥 Loading ALL resources from GraphRAG...")
resources = supabase.table('resources').select('*').execute()

print(f"✅ Loaded {len(resources.data)} resources")
print()

# Detailed analysis
analysis = {
    'by_type': defaultdict(list),
    'by_directory': defaultdict(list),
    'by_cultural_value': defaultdict(list),
    'featured': [],
    'paths': [],
    'unique_directories': set()
}

for resource in resources.data:
    rtype = resource.get('type', 'unknown')
    path = resource.get('path', '')
    cultural = resource.get('cultural_integration_level', 'unknown')
    featured = resource.get('featured', False)
    
    analysis['by_type'][rtype].append(path)
    analysis['by_cultural_value'][cultural].append(path)
    analysis['paths'].append(path)
    
    if featured:
        analysis['featured'].append(resource)
    
    # Extract directory
    if '/' in path:
        directory = '/'.join(path.split('/')[:-1])
        analysis['by_directory'][directory].append(path)
        analysis['unique_directories'].add(directory)

print("📊 GRAPHRAG CONTENT ANALYSIS")
print("=" * 70)
print()

print("🗂️  TOP DIRECTORIES IN GRAPHRAG:")
top_dirs = sorted(analysis['by_directory'].items(), key=lambda x: len(x[1]), reverse=True)[:15]
for directory, items in top_dirs:
    print(f"  {len(items):3d} files in {directory}/")

print()
print("📋 RESOURCE TYPES:")
for rtype, items in sorted(analysis['by_type'].items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {rtype}: {len(items)}")

print()
print(f"⭐ FEATURED RESOURCES: {len(analysis['featured'])}")

print()
print("🌿 CULTURAL INTEGRATION:")
for level, items in sorted(analysis['by_cultural_value'].items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {level}: {len(items)}")

print()
print("📂 UNIQUE DIRECTORIES: {}")
for directory in sorted(analysis['unique_directories'])[:20]:
    print(f"  - {directory}")

# Find what's NOT in GraphRAG
print()
print("=" * 70)
print("🔍 FINDING GAPS")
print("=" * 70)
print()

from pathlib import Path

# Get all actual HTML files in public
actual_files = []
for html_file in Path('public').rglob('*.html'):
    rel_path = str(html_file.relative_to('public'))
    if not any(x in rel_path for x in ['backup', '.master', 'node_modules']):
        actual_files.append(rel_path)

print(f"📁 Actual HTML files in public/: {len(actual_files)}")
print(f"📊 Files in GraphRAG: {len(analysis['paths'])}")
print(f"❓ Potential gap: {len(actual_files) - len(analysis['paths'])} files")

# Find specific gaps
graphrag_paths_set = set(analysis['paths'])
missing = [f for f in actual_files if f not in graphrag_paths_set]

if missing:
    print()
    print(f"⚠️  EXAMPLE FILES NOT IN GRAPHRAG (showing first 20):")
    for path in sorted(missing)[:20]:
        print(f"  - {path}")

# Save complete map
map_data = {
    'total_in_graphrag': len(resources.data),
    'total_actual_files': len(actual_files),
    'gap': len(actual_files) - len(analysis['paths']),
    'by_type': {k: len(v) for k, v in analysis['by_type'].items()},
    'by_directory': {k: len(v) for k, v in analysis['by_directory'].items()},
    'top_20_directories': [{'dir': k, 'count': len(v)} for k, v in top_dirs[:20]],
    'missing_from_graphrag': missing[:100]
}

with open('COMPLETE-GRAPHRAG-MAP.json', 'w') as f:
    json.dump(map_data, f, indent=2)

print()
print("✅ Complete map saved: COMPLETE-GRAPHRAG-MAP.json")
print()
print("🎯 NOW I understand the landscape!")

