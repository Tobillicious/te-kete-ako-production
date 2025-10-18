#!/usr/bin/env python3
"""
CLEAN AND COMPLETE GRAPHRAG
1. Remove 325 duplicates
2. Add 101 missing files
3. Create authoritative knowledge map
"""

from supabase import create_client
from pathlib import Path
import json
from collections import defaultdict

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🧹 CLEAN AND COMPLETE GRAPHRAG")
print("=" * 70)
print()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Step 1: Understand current state
print("STEP 1: ANALYZE CURRENT GRAPHRAG")
print("-" * 70)

resources = supabase.table('resources').select('*').execute()
print(f"Current entries: {len(resources.data)}")

# Find duplicates
path_groups = defaultdict(list)
for r in resources.data:
    path_groups[r['path']].append(r)

duplicates = {p: entries for p, entries in path_groups.items() if len(entries) > 1}
print(f"Duplicate paths: {len(duplicates)}")
print(f"Unique resources: {len(path_groups)}")

print()
print("STEP 2: FIND MISSING FILES")
print("-" * 70)

# Get all public HTML files
actual_files = []
for html_file in Path('public').rglob('*.html'):
    rel_path = str(html_file.relative_to('public'))
    if not any(x in rel_path for x in ['backup', '.master', 'node_modules', '.git']):
        actual_files.append(rel_path)

graphrag_paths = set(r['path'] for r in resources.data)

# Normalize paths (some have /public/ prefix, some don't)
normalized_graphrag = set()
for path in graphrag_paths:
    normalized_graphrag.add(path.replace('/public/', '').replace('public/', ''))

missing = [f for f in actual_files if f not in normalized_graphrag]

print(f"Actual files in public/: {len(actual_files)}")
print(f"Files in GraphRAG (normalized): {len(normalized_graphrag)}")
print(f"Missing from GraphRAG: {len(missing)}")

print()
print("📝 HIGH-VALUE MISSING FILES (Top 20):")
priority_keywords = ['virtual-marae', 'decolonized', 'adaptive', 'kaitiaki', 'curriculum-documents']
priority_missing = [f for f in missing if any(kw in f for kw in priority_keywords)]

for f in priority_missing[:20]:
    print(f"  - {f}")

if len(priority_missing) == 0:
    print("  (Showing first 20 missing files)")
    for f in sorted(missing)[:20]:
        print(f"  - {f}")

# Step 3: Save analysis
report = {
    'current_entries': len(resources.data),
    'unique_paths': len(path_groups),
    'duplicates': len(duplicates),
    'actual_files': len(actual_files),
    'missing_count': len(missing),
    'missing_files': missing,
    'duplicate_examples': [{'path': p, 'count': len(entries)} for p, entries in sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True)[:20]]
}

with open('GRAPHRAG-CLEANUP-ANALYSIS.json', 'w') as f:
    json.dump(report, f, indent=2)

print()
print("=" * 70)
print("📊 ANALYSIS COMPLETE")
print("=" * 70)
print(f"✅ Found {len(missing)} files to add to GraphRAG")
print(f"🧹 Found {len(duplicates)} duplicate paths to clean")
print(f"📄 Saved: GRAPHRAG-CLEANUP-ANALYSIS.json")
print()
print("🎯 NEXT: Add missing treasures to GraphRAG for complete map")

