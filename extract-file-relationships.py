#!/usr/bin/env python3
"""
EXTRACT FILE RELATIONSHIPS - Build Dependency Graph
Map which files import/link to which other files
"""

from pathlib import Path
import re
import json
from collections import defaultdict

print("🔗 EXTRACTING FILE RELATIONSHIPS - Dependency Intelligence")
print("=" * 70)

# Track all relationships
relationships = {
    'css_dependencies': defaultdict(list),
    'js_dependencies': defaultdict(list),
    'html_links': defaultdict(list),
    'component_includes': defaultdict(list),
    'imports': defaultdict(list)
}

stats = {
    'files_scanned': 0,
    'css_refs_found': 0,
    'js_refs_found': 0,
    'html_links_found': 0,
    'component_refs_found': 0
}

print("\n📊 Scanning HTML files for relationships...")

# Scan all HTML files in public/ (production content)
html_files = list(Path('public').rglob('*.html'))
total = len(html_files)

for i, html_file in enumerate(html_files, 1):
    try:
        stats['files_scanned'] += 1
        content = html_file.read_text(encoding='utf-8')
        rel_path = str(html_file.relative_to('public'))
        
        # Extract CSS dependencies
        css_links = re.findall(r'<link[^>]*href=["\']([^"\']*\.css)["\']', content)
        for css in css_links:
            relationships['css_dependencies'][rel_path].append(css)
            stats['css_refs_found'] += 1
        
        # Extract JS dependencies
        js_refs = re.findall(r'<script[^>]*src=["\']([^"\']*\.js)["\']', content)
        for js in js_refs:
            relationships['js_dependencies'][rel_path].append(js)
            stats['js_refs_found'] += 1
        
        # Extract internal HTML links
        html_links = re.findall(r'href=["\']([^"\']*\.html)["\']', content)
        for link in html_links:
            if not link.startswith('http'):
                relationships['html_links'][rel_path].append(link)
                stats['html_links_found'] += 1
        
        # Extract component includes (fetch calls)
        components = re.findall(r'fetch\(["\']([^"\']*\.html)["\']', content)
        for comp in components:
            relationships['component_includes'][rel_path].append(comp)
            stats['component_refs_found'] += 1
        
        if i % 200 == 0:
            print(f"   Scanned {i}/{total} files...")
    
    except Exception as e:
        pass

print(f"\n✅ Scanned {stats['files_scanned']} HTML files")

# Analyze patterns
print(f"\n" + "=" * 70)
print("📊 RELATIONSHIP ANALYSIS")
print("=" * 70)

print(f"\n🎨 CSS Dependencies:")
print(f"   Files using CSS: {len(relationships['css_dependencies'])}")
print(f"   Total CSS references: {stats['css_refs_found']}")

# Find most used CSS files
css_usage = defaultdict(int)
for file_css_list in relationships['css_dependencies'].values():
    for css in file_css_list:
        css_name = css.split('/')[-1]
        css_usage[css_name] += 1

print(f"\n   Most used CSS files:")
for css, count in sorted(css_usage.items(), key=lambda x: -x[1])[:5]:
    print(f"   - {css}: {count} files")

print(f"\n💻 JavaScript Dependencies:")
print(f"   Files using JS: {len(relationships['js_dependencies'])}")
print(f"   Total JS references: {stats['js_refs_found']}")

# Find most used JS files
js_usage = defaultdict(int)
for file_js_list in relationships['js_dependencies'].values():
    for js in file_js_list:
        js_name = js.split('/')[-1]
        js_usage[js_name] += 1

print(f"\n   Most used JS files:")
for js, count in sorted(js_usage.items(), key=lambda x: -x[1])[:5]:
    print(f"   - {js}: {count} files")

print(f"\n🔗 Internal Links:")
print(f"   Files with links: {len(relationships['html_links'])}")
print(f"   Total links: {stats['html_links_found']}")

print(f"\n🧩 Component Includes:")
print(f"   Files using components: {len(relationships['component_includes'])}")
print(f"   Total component refs: {stats['component_refs_found']}")

# Save complete relationship data
output = {
    'metadata': {
        'scan_date': '2025-10-18',
        'files_scanned': stats['files_scanned'],
        'total_relationships': sum(stats.values())
    },
    'statistics': stats,
    'relationships': {
        'css_dependencies': dict(relationships['css_dependencies']),
        'js_dependencies': dict(relationships['js_dependencies']),
        'html_links': dict(relationships['html_links']),
        'component_includes': dict(relationships['component_includes'])
    },
    'usage_analysis': {
        'css_usage': dict(css_usage),
        'js_usage': dict(js_usage)
    }
}

with open('file-relationships-complete.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\n" + "=" * 70)
print("💾 RELATIONSHIP DATA SAVED")
print("=" * 70)
print(f"\n✅ file-relationships-complete.json created")
print(f"📊 Total relationships mapped: {sum(stats.values())}")
print(f"🎯 Dependency graph data ready for GraphRAG import")

print(f"\n" + "=" * 70)
print("🚀 NEXT: Import this to GraphRAG for super intelligence!")
print("=" * 70)

