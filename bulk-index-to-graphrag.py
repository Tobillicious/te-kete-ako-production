#!/usr/bin/env python3
"""
Bulk Index Remaining Files to GraphRAG
High-value enhancement: Improve discoverability
"""

from supabase import create_client
from pathlib import Path
import re
import json
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("📊 BULK INDEXING TO GRAPHRAG")
print("=" * 70)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get currently indexed files
print("\n🔍 Checking currently indexed files...")
try:
    result = supabase.table('resources').select('path').execute()
    indexed_paths = {r['path'] for r in result.data if r.get('path')}
    print(f"   Currently indexed: {len(indexed_paths)} files")
except Exception as e:
    print(f"   ⚠️  Error checking indexed files: {e}")
    indexed_paths = set()

# Find all HTML files
print("\n📁 Scanning for HTML files...")
all_html_files = list(Path('public').rglob('*.html'))
print(f"   Found: {len(all_html_files)} HTML files")

# Identify unindexed files
unindexed = []
for html_file in all_html_files:
    rel_path = '/' + str(html_file.relative_to('public'))
    if rel_path not in indexed_paths:
        unindexed.append(html_file)

print(f"\n📊 Unindexed files: {len(unindexed)}")

if len(unindexed) == 0:
    print("\n✅ All files already indexed in GraphRAG!")
    exit(0)

# Index first 100 files (batch limit)
batch_size = 100
to_index = unindexed[:batch_size]

print(f"\n📤 Indexing first {len(to_index)} files to GraphRAG...")

stats = {'success': 0, 'failed': 0, 'errors': []}

for html_file in to_index:
    try:
        content = html_file.read_text(encoding='utf-8')
        
        # Extract metadata
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else html_file.stem
        
        # Determine type
        path_str = str(html_file)
        if '/lessons/' in path_str:
            resource_type = 'lesson'
        elif '/handouts/' in path_str:
            resource_type = 'handout'
        elif '/units/' in path_str:
            resource_type = 'unit-plan'
        elif '/games/' in path_str:
            resource_type = 'game'
        elif '/assessment' in path_str:
            resource_type = 'assessment'
        else:
            resource_type = 'interactive'
        
        # Extract description
        desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
        description = desc_match.group(1) if desc_match else f"{title} - Educational resource"
        
        # Check for cultural elements
        has_whakatauaki = 'whakataukī' in content.lower() or 'whakatauki' in content.lower()
        has_cultural_context = 'cultural context' in content.lower() or 'te ao māori' in content.lower()
        
        cultural_level = 'high' if (has_whakatauaki and has_cultural_context) else \
                        'medium' if has_cultural_context else 'low'
        
        # Create resource entry
        resource = {
            'title': title[:200],  # Limit length
            'description': description[:500],
            'path': '/' + str(html_file.relative_to('public')),
            'type': resource_type,
            'subject': 'general',
            'level': 'all-levels',
            'tags': ['indexed', 'bulk-import'],
            'cultural_elements': json.dumps({
                'cultural_integration': cultural_level,
                'whakatauaki_present': has_whakatauaki
            }),
            'author': 'Bulk Indexer',
            'is_active': True
        }
        
        # Insert to GraphRAG
        supabase.table('resources').insert(resource).execute()
        stats['success'] += 1
        
        if stats['success'] % 10 == 0:
            print(f"   ✅ Indexed {stats['success']} files...")
    
    except Exception as e:
        stats['failed'] += 1
        stats['errors'].append(f"{html_file.name}: {str(e)[:50]}")

# Summary
print("\n" + "=" * 70)
print("📊 BULK INDEX SUMMARY")
print("=" * 70)
print(f"\n✅ Successfully indexed: {stats['success']} files")
print(f"⚠️  Failed: {stats['failed']} files")
print(f"📈 Total in GraphRAG: {len(indexed_paths) + stats['success']}")
print(f"📊 Coverage improvement: {len(unindexed) - stats['success']} files remaining")

if stats['success'] > 0:
    coverage_pct = ((len(indexed_paths) + stats['success']) / len(all_html_files)) * 100
    print(f"\n🎯 GraphRAG Coverage: {coverage_pct:.1f}%")

if stats['errors']:
    print(f"\n⚠️  Sample errors:")
    for error in stats['errors'][:3]:
        print(f"   - {error}")

print("\n" + "=" * 70)
print("✨ Enhancement complete! Run again to index more files.")
