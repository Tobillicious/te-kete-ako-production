#!/usr/bin/env python3
"""
DEEP SCAN: Understand the FULL 90K scope
Map every directory, count everything, find what we're missing
"""

import os
import json
from collections import defaultdict
from pathlib import Path

print("🔍 DEEP SCAN: FULL REPOSITORY SCOPE")
print("=" * 70)

# Directories to scan
base_dir = Path('.')
skip_dirs = {'.git', 'node_modules', 'dist', '.vite', '__pycache__', '.pytest_cache'}

# Categorize by directory
by_directory = defaultdict(lambda: {'html': 0, 'json': 0, 'md': 0, 'other': 0, 'total': 0})
educational_content = {'lessons': [], 'handouts': [], 'units': [], 'games': [], 'tools': []}
archive_content = []

# Scan everything
for root, dirs, files in os.walk(base_dir):
    # Skip certain directories
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    root_path = Path(root)
    rel_path = str(root_path.relative_to(base_dir))
    
    for file in files:
        full_path = root_path / file
        ext = file.split('.')[-1].lower()
        
        # Count by type
        if ext == 'html':
            by_directory[rel_path]['html'] += 1
        elif ext == 'json':
            by_directory[rel_path]['json'] += 1
        elif ext == 'md':
            by_directory[rel_path]['md'] += 1
        else:
            by_directory[rel_path]['other'] += 1
        
        by_directory[rel_path]['total'] += 1
        
        # Categorize educational content
        if 'lesson' in str(full_path).lower():
            educational_content['lessons'].append(str(full_path))
        if 'handout' in str(full_path).lower():
            educational_content['handouts'].append(str(full_path))
        if 'unit' in str(full_path).lower() and ext == 'html':
            educational_content['units'].append(str(full_path))
        if 'game' in str(full_path).lower() and ext == 'html':
            educational_content['games'].append(str(full_path))
        if 'tool' in str(full_path).lower() and ext == 'html':
            educational_content['tools'].append(str(full_path))
        
        # Track archives
        if any(x in rel_path for x in ['archive', 'backup', 'old', 'redundant']):
            archive_content.append(str(full_path))

# Print summary
print("\n📊 TOP 30 DIRECTORIES BY FILE COUNT:")
print("-" * 70)
sorted_dirs = sorted(by_directory.items(), key=lambda x: x[1]['total'], reverse=True)
for i, (dir_name, counts) in enumerate(sorted_dirs[:30], 1):
    total = counts['total']
    html = counts['html']
    json = counts['json']
    md = counts['md']
    print(f"{i:2}. {dir_name[:50]:50} | Total: {total:4} (HTML:{html:3} JSON:{json:3} MD:{md:3})")

# Educational content summary
print("\n\n📚 EDUCATIONAL CONTENT BREAKDOWN:")
print("-" * 70)
for category, items in educational_content.items():
    print(f"{category.title():15} {len(items):5} files")

# Archive summary
print("\n\n📦 ARCHIVED/BACKUP CONTENT:")
print("-" * 70)
print(f"Total files in archives: {len(archive_content):,}")

# Category breakdown
archive_by_type = defaultdict(int)
for path in archive_content:
    ext = path.split('.')[-1].lower()
    archive_by_type[ext] += 1

print("\nArchive breakdown:")
for ext, count in sorted(archive_by_type.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  .{ext:10} {count:5}")

# Grand total
total_files = sum(counts['total'] for counts in by_directory.values())
total_html = sum(counts['html'] for counts in by_directory.values())
total_json = sum(counts['json'] for counts in by_directory.values())
total_md = sum(counts['md'] for counts in by_directory.values())

print("\n\n" + "=" * 70)
print("📊 GRAND TOTALS:")
print("-" * 70)
print(f"Total Files:     {total_files:,}")
print(f"HTML Files:      {total_html:,}")
print(f"JSON Files:      {total_json:,}")
print(f"Markdown Files:  {total_md:,}")
print(f"In Archives:     {len(archive_content):,} ({len(archive_content)/total_files*100:.1f}%)")
print(f"Active Content:  {total_files - len(archive_content):,}")

print("\n" + "=" * 70)
print("🎯 INDEXING GAP ANALYSIS:")
print("-" * 70)
print(f"Currently in GraphRAG: 7,687")
print(f"Total indexable files: {total_files:,}")
print(f"Still to index:        {total_files - 7687:,}")
print(f"Coverage:              {7687/total_files*100:.1f}%")

# Save detailed report
report = {
    'totals': {
        'all_files': total_files,
        'html': total_html,
        'json': total_json,
        'md': total_md,
        'in_archives': len(archive_content),
        'active': total_files - len(archive_content)
    },
    'by_directory': dict(sorted_dirs[:50]),
    'educational_content': {k: len(v) for k, v in educational_content.items()},
    'archive_breakdown': dict(archive_by_type)
}

import json as json_module
with open('FULL-SCOPE-ANALYSIS.json', 'w') as f:
    json_module.dump(report, f, indent=2)

print("\n✅ Detailed report saved to FULL-SCOPE-ANALYSIS.json")
print("=" * 70)

