#!/usr/bin/env python3
"""
VERSION COMPARISON TOOL
Find and compare all versions of files across backups
"""

from supabase import create_client
from collections import defaultdict
import json

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SERVICE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

supabase = create_client(SUPABASE_URL, SERVICE_KEY)

print("🔍 VERSION COMPARISON ANALYSIS")
print("=" * 70)

# Get all resources
print("📥 Loading all resources...")
all_resources = []
offset = 0
while True:
    batch = supabase.table('resources').select('*').range(offset, offset + 999).execute()
    if not batch.data:
        break
    all_resources.extend(batch.data)
    offset += 1000
    if len(batch.data) < 1000:
        break

print(f"   Total: {len(all_resources)}\n")

# Group by filename
by_filename = defaultdict(list)
for resource in all_resources:
    # Extract filename from path
    path = resource['path']
    if '/' in path:
        filename = path.split('/')[-1]
    else:
        filename = path
    
    # Skip if not HTML
    if not filename.endswith('.html'):
        continue
    
    by_filename[filename].append(resource)

# Find multi-version files
multi_version = {name: versions for name, versions in by_filename.items() if len(versions) > 1}

print(f"📊 ANALYSIS RESULTS:")
print(f"   Total unique filenames: {len(by_filename)}")
print(f"   Files with multiple versions: {len(multi_version)}")
print(f"   Files with single version: {len(by_filename) - len(multi_version)}\n")

# Analyze multi-version files
print("🔍 MULTI-VERSION FILE ANALYSIS:\n")

version_stats = []
for filename, versions in sorted(multi_version.items(), key=lambda x: len(x[1]), reverse=True)[:50]:
    stats = {
        'filename': filename,
        'version_count': len(versions),
        'versions': []
    }
    
    for v in versions:
        source = 'current' if '/BACKUP_' not in v['path'] else v['path'].split('/')[1].replace('BACKUP_', '')
        stats['versions'].append({
            'source': source,
            'path': v['path'],
            'is_active': v['is_active'],
            'title': v['title'][:50],
            'tags': v.get('tags', [])
        })
    
    version_stats.append(stats)

# Display top duplicates
print("TOP 20 MOST DUPLICATED FILES:")
for i, stat in enumerate(version_stats[:20], 1):
    print(f"\n{i}. {stat['filename']} ({stat['version_count']} versions)")
    for v in stat['versions']:
        active_marker = "✅" if v['is_active'] else "⚪"
        print(f"   {active_marker} [{v['source']}] {v['title']}")

# Save full report
with open('version-comparison-report.json', 'w') as f:
    json.dump(version_stats, f, indent=2)

print(f"\n\n💾 Full report saved to: version-comparison-report.json")
print(f"\n📊 SUMMARY:")
print(f"   Files analyzed: {len(version_stats)}")
print(f"   Ready for comparison and merging!")

