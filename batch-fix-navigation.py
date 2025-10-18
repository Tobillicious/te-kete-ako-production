#!/usr/bin/env python3
"""
BATCH FIX - Add Navigation to 599 Files
Automatically inject navigation component where missing
"""

import json
import os
from pathlib import Path

# Load files that need navigation
with open('processing-progress.json', 'r') as f:
    data = json.load(f)

needs_nav = [f for f in data['needs_work'] if not f['checks'].get('nav', False)]

print("🔧 BATCH FIX: Adding Navigation")
print("=" * 70)
print(f"\nFiles needing navigation: {len(needs_nav)}\n")

NAVIGATION_SNIPPET = '''<!-- Professional Navigation -->
<script>
fetch('/components/navigation-standard.html')
    .then(r => r.text())
    .then(html => {
        const div = document.createElement('div');
        div.innerHTML = html;
        document.body.insertBefore(div.firstElementChild, document.body.firstChild);
    });
</script>

'''

files_fixed = 0
files_skipped = 0

for i, file_info in enumerate(needs_nav[:100], 1):  # Fix first 100
    filepath = file_info['path']
    
    try:
        # Skip if not in public/ (don't modify archives)
        if not filepath.startswith('./public/'):
            files_skipped += 1
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has navigation
        if 'navigation-standard.html' in content:
            files_skipped += 1
            continue
        
        # Add navigation after <body> tag
        if '<body' in content:
            content = content.replace('<body>', f'<body>\n{NAVIGATION_SNIPPET}', 1)
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            files_fixed += 1
            if i % 10 == 0:
                print(f"   ✅ Fixed {i}/100: {file_info['title'][:50]}")
        else:
            files_skipped += 1
            
    except Exception as e:
        print(f"   ⚠️  Error: {filepath} - {e}")
        files_skipped += 1

print("\n" + "=" * 70)
print("✅ BATCH FIX COMPLETE")
print("=" * 70)
print(f"\n✅ Files fixed: {files_fixed}")
print(f"⏭️  Files skipped: {files_skipped}")
print(f"\n🎯 Next: Run continuous-processor.py again to verify improvements")

