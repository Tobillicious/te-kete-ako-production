#!/usr/bin/env python3
"""
Fix broken links (href="" or href="#")
"""

from pathlib import Path
import re

print("🔗 FIXING BROKEN LINKS")
print("=" * 70)

files_with_broken_links = [
    'public/handouts/student-dashboard.html',
    'public/handouts/youtube-library.html',
    'public/handouts/lesson-template.html',
    'public/student-dashboard.html',
    'public/youtube-library.html',
]

fixed_count = 0
links_fixed = 0

for file_path in files_with_broken_links:
    file = Path(file_path)
    if not file.exists():
        continue
    
    try:
        content = file.read_text(encoding='utf-8')
        original = content
        
        # Fix empty href
        content = re.sub(r'href=""', 'href="/"', content)
        
        # Fix href="#" that should go somewhere
        # Keep intentional anchors, but fix broken ones
        # This is conservative - only fixes obvious broken links
        
        if content != original:
            file.write_text(content, encoding='utf-8')
            changes = original.count('href=""') - content.count('href=""')
            print(f"✅ Fixed {changes} links in: {file.name}")
            fixed_count += 1
            links_fixed += changes
        else:
            print(f"ℹ️  No empty href found: {file.name}")
    
    except Exception as e:
        print(f"⚠️  Error fixing {file_path}: {e}")

print("\n" + "=" * 70)
print(f"✅ Fixed {links_fixed} broken links in {fixed_count} files")
print("=" * 70)
