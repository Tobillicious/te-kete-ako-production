#!/usr/bin/env python3
"""
Fix the most common broken links
"""

from pathlib import Path
import re

def fix_broken_links_in_file(file_path):
    """Fix common broken link patterns"""
    try:
        content = file_path.read_text(encoding='utf-8')
    except:
        return 0
    
    original = content
    fixes = 0
    
    # Fix 1: Remove non-existent CSS files
    if 'design-system-v3.css' in content:
        content = re.sub(r'<link[^>]*design-system-v3\.css[^>]*>\n?', '', content)
        fixes += 1
    
    if 'award-winning-polish.css' in content:
        content = re.sub(r'<link[^>]*award-winning-polish\.css[^>]*>\n?', '', content)
        fixes += 1
    
    # Fix 2: Fix wrong CSS paths
    content = re.sub(r'href=["\']/../../../css/([^"\']+)["\']', r'href="/css/\1"', content)
    content = re.sub(r'href=["\']/../../css/([^"\']+)["\']', r'href="/css/\1"', content)
    if '/../../../css/' in original or '/../../css/' in original:
        fixes += 1
    
    # Fix 3: Fix /public/generated-resources-alpha/ links
    content = re.sub(r'href=["\']\/public\/generated-resources-alpha\/', r'href="/generated-resources-alpha/', content)
    if '/public/generated-resources-alpha/' in original:
        fixes += 1
    
    if fixes > 0:
        file_path.write_text(content, encoding='utf-8')
    
    return fixes

# Process all files
public_dir = Path('public')
print("🔧 FIXING BROKEN LINKS")
print("="*60)

total_files = 0
total_fixes = 0

for html_file in public_dir.rglob('*.html'):
    if 'backup' in str(html_file).lower():
        continue
    
    total_files += 1
    fixes = fix_broken_links_in_file(html_file)
    total_fixes += fixes
    
    if total_files % 200 == 0:
        print(f"   Processed {total_files} files, {total_fixes} fixes...")

print(f"\n{'='*60}")
print(f"✅ COMPLETE")
print(f"   Files processed: {total_files}")
print(f"   Total fixes: {total_fixes}")
print(f"{'='*60}\n")
