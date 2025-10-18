#!/usr/bin/env python3
"""
CSS Consolidation Audit
Identify which CSS files are actually used and can be merged
"""

import os
import re
from pathlib import Path
from collections import defaultdict

print("🎨 CSS CONSOLIDATION AUDIT")
print("=" * 70)

# Find all CSS files
css_dir = Path('public/css')
css_files = list(css_dir.glob('**/*.css'))

print(f"\n📊 Found {len(css_files)} CSS files\n")

# Track usage
css_usage = defaultdict(list)

# Scan HTML files for CSS references
html_files = list(Path('public').rglob('*.html'))

print(f"🔍 Scanning {len(html_files)} HTML files for CSS references...\n")

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find CSS link tags
        css_links = re.findall(r'<link[^>]*href=["\']([^"\']*\.css)["\']', content)
        
        for css_link in css_links:
            # Extract filename
            css_filename = css_link.split('/')[-1]
            css_usage[css_filename].append(str(html_file.relative_to('public')))
    
    except Exception as e:
        pass

# Categorize CSS files
categories = {
    'Core Design': [],
    'Components': [],
    'Specialized': [],
    'Mobile/Print': [],
    'Archived': [],
    'Unused': []
}

for css_file in css_files:
    filename = css_file.name
    used_count = len(css_usage.get(filename, []))
    
    # Categorize
    if 'archive' in str(css_file):
        categories['Archived'].append((filename, used_count, css_file))
    elif used_count == 0:
        categories['Unused'].append((filename, used_count, css_file))
    elif 'mobile' in filename or 'print' in filename:
        categories['Mobile/Print'].append((filename, used_count, css_file))
    elif any(x in filename for x in ['component', 'navigation', 'footer', 'header']):
        categories['Components'].append((filename, used_count, css_file))
    elif 'professional' in filename or 'main' in filename or 'unified' in filename:
        categories['Core Design'].append((filename, used_count, css_file))
    else:
        categories['Specialized'].append((filename, used_count, css_file))

# Display results
print("=" * 70)
print("📋 CSS FILE CATEGORIZATION")
print("=" * 70)

for category, files in categories.items():
    if files:
        print(f"\n🎨 {category} ({len(files)} files):")
        for filename, count, path in sorted(files, key=lambda x: -x[1]):
            if count > 0:
                print(f"   ✅ {filename} - Used in {count} files")
            else:
                print(f"   ⚠️  {filename} - UNUSED")

# Consolidation recommendations
print("\n" + "=" * 70)
print("💡 CONSOLIDATION RECOMMENDATIONS")
print("=" * 70)

print("\n📦 Keep These Core Files (10 max):")
core_keep = [
    'te-kete-professional.css',
    'navigation-enhanced.css',
    'lesson-plan.css',
    'handout.css',
    'mobile-optimization.css',
    'print.css',
    'animations-professional.css',
    'critical.css',
    'component-library.css',
    'west-coast-nz-colors.css'
]

for css_name in core_keep:
    used_count = len(css_usage.get(css_name, []))
    status = "✅" if used_count > 0 else "⚠️ "
    print(f"   {status} {css_name} ({used_count} files)")

print("\n🗄️ Archive These (in /css/archive/):")
archive_count = len([f for f in categories['Archived']])
unused_count = len([f for f in categories['Unused']])
print(f"   Already archived: {archive_count} files")
print(f"   Can be archived: {unused_count} unused files")

print("\n🔄 Merge These Into Core:")
merge_candidates = [f for f in categories['Specialized'] if f[1] < 5]
for filename, count, path in merge_candidates[:10]:
    print(f"   → {filename} (used {count}x) → Merge into te-kete-professional.css")

# Action plan
print("\n" + "=" * 70)
print("🎯 ACTION PLAN")
print("=" * 70)

print("""
1. Keep 10 core CSS files (listed above)
2. Archive unused files to /css/archive/
3. Merge low-usage specialized files into core
4. Update HTML references to consolidated files
5. Test thoroughly after consolidation

Target: 45 files → 10 core files (78% reduction)
""")

print("=" * 70)

