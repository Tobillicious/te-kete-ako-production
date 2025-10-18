#!/usr/bin/env python3
"""
DEEP ICEBERG SCAN - Analyze ALL 90,000 Resources
Comprehensive scan of entire codebase to understand the full scope
"""
import os
import json
from pathlib import Path
from collections import defaultdict
import re

print("🏔️ DEEP ICEBERG SCAN - ANALYZING ALL 90K RESOURCES")
print("=" * 70)

# Comprehensive directory scan
all_directories = [
    'public',
    'archive',
    'archived-bloat',
    'backup_before_css_migration',
    'backup_before_minification',
    'backups',
    'dist'
]

file_inventory = {
    'total_files': 0,
    'html_files': 0,
    'js_files': 0,
    'css_files': 0,
    'json_files': 0,
    'image_files': 0,
    'other_files': 0,
    'by_directory': {},
    'by_type': defaultdict(int),
    'large_directories': []
}

resource_categories = {
    'lessons': [],
    'handouts': [],
    'games': [],
    'units': [],
    'assessments': [],
    'tools': [],
    'media': [],
    'data': [],
    'other': []
}

def categorize_file(file_path):
    """Categorize file by path and content"""
    path_lower = file_path.lower()
    
    if 'lesson' in path_lower:
        return 'lessons'
    elif 'handout' in path_lower or 'worksheet' in path_lower:
        return 'handouts'
    elif 'game' in path_lower or 'interactive' in path_lower:
        return 'games'
    elif 'unit' in path_lower:
        return 'units'
    elif 'assessment' in path_lower or 'rubric' in path_lower or 'test' in path_lower:
        return 'assessments'
    elif 'tool' in path_lower or 'calculator' in path_lower or 'generator' in path_lower:
        return 'tools'
    elif any(ext in path_lower for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.mp4', '.mp3']):
        return 'media'
    elif '.json' in path_lower or '.csv' in path_lower:
        return 'data'
    
    return 'other'

print("\n📂 Scanning directories...")

for directory in all_directories:
    if not os.path.exists(directory):
        print(f"   ⚠️  {directory} not found, skipping")
        continue
    
    print(f"\n📁 Scanning {directory}/...")
    dir_stats = {
        'total': 0,
        'html': 0,
        'js': 0,
        'css': 0,
        'json': 0,
        'other': 0
    }
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_inventory['total_files'] += 1
            dir_stats['total'] += 1
            
            # Categorize by extension
            ext = Path(file).suffix.lower()
            file_inventory['by_type'][ext] += 1
            
            if ext == '.html':
                file_inventory['html_files'] += 1
                dir_stats['html'] += 1
                
                # Categorize HTML resources
                category = categorize_file(file_path)
                resource_categories[category].append({
                    'path': file_path,
                    'name': file,
                    'directory': directory,
                    'size': os.path.getsize(file_path) if os.path.exists(file_path) else 0
                })
                
            elif ext == '.js':
                file_inventory['js_files'] += 1
                dir_stats['js'] += 1
            elif ext == '.css':
                file_inventory['css_files'] += 1
                dir_stats['css'] += 1
            elif ext == '.json':
                file_inventory['json_files'] += 1
                dir_stats['json'] += 1
            elif ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
                file_inventory['image_files'] += 1
            else:
                file_inventory['other_files'] += 1
                dir_stats['other'] += 1
    
    file_inventory['by_directory'][directory] = dir_stats
    print(f"   📊 {dir_stats['total']:,} files ({dir_stats['html']:,} HTML)")

print(f"\n{'=' * 70}")
print(f"📊 COMPREHENSIVE FILE INVENTORY")
print(f"{'=' * 70}")
print(f"Total Files: {file_inventory['total_files']:,}")
print(f"  HTML: {file_inventory['html_files']:,}")
print(f"  JavaScript: {file_inventory['js_files']:,}")
print(f"  CSS: {file_inventory['css_files']:,}")
print(f"  JSON: {file_inventory['json_files']:,}")
print(f"  Images: {file_inventory['image_files']:,}")
print(f"  Other: {file_inventory['other_files']:,}")

print(f"\n{'=' * 70}")
print(f"📚 RESOURCE CATEGORIES (HTML only)")
print(f"{'=' * 70}")
total_html = 0
for category, items in resource_categories.items():
    count = len(items)
    total_html += count
    if count > 0:
        print(f"  {category.title()}: {count:,} files")

print(f"\n  TOTAL HTML RESOURCES: {total_html:,}")

# Top file types
print(f"\n{'=' * 70}")
print(f"📋 TOP FILE TYPES")
print(f"{'=' * 70}")
top_types = sorted(file_inventory['by_type'].items(), key=lambda x: x[1], reverse=True)[:15]
for ext, count in top_types:
    ext_display = ext if ext else '(no extension)'
    print(f"  {ext_display}: {count:,}")

# Save detailed inventory
with open('deep-iceberg-inventory.json', 'w') as f:
    json.dump({
        'summary': file_inventory,
        'categories': {k: len(v) for k, v in resource_categories.items()},
        'total_html': total_html
    }, f, indent=2)

print(f"\n💾 Detailed inventory saved: deep-iceberg-inventory.json")

print(f"\n🏔️ ICEBERG ANALYSIS:")
print(f"   Total Files in Codebase: {file_inventory['total_files']:,}")
print(f"   Total HTML Resources: {total_html:,}")
print(f"   Currently Live: 231")
print(f"   Percentage Live: {(231/total_html*100):.2f}%")
print(f"   HIDDEN ICEBERG: {total_html - 231:,} resources ({((total_html-231)/total_html*100):.1f}%)")

print(f"\n✅ Deep scan complete! Now we see the FULL iceberg! 🏔️")

