#!/usr/bin/env python3
"""
REMOVE CASCADE CONFLICTS - Clean CSS System
Remove professionalization CSS files that conflict with Ultimate Beauty System
"""

from pathlib import Path
import re

# Files to remove (cause cascade conflicts)
CONFLICT_FILES = [
    'public/css/professionalization-system.css',
    'public/css/lesson-professionalization.css',
    'public/css/unit-index-professionalization.css',
    'public/css/cascade-fix.css',
    'public/css/min/unit-index-professionalization.min.css',
    'public/css/min/lesson-professionalization.min.css',
]

# Remove references from HTML files
def remove_css_references(html_path):
    """Remove professionalization CSS references from HTML"""
    content = html_path.read_text(encoding='utf-8', errors='ignore')
    original = content
    
    # Remove link tags for these CSS files
    patterns = [
        r'<link[^>]*professionalization[^>]*>\s*',
        r'<link[^>]*cascade-fix[^>]*>\s*',
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
    
    if content != original:
        html_path.write_text(content, encoding='utf-8')
        return True
    return False

# Execute
removed_files = 0
removed_refs = 0

print("🧹 REMOVING CASCADE CONFLICTS")
print("=" * 60)

# Remove conflict CSS files
for file_path in CONFLICT_FILES:
    path = Path(file_path)
    if path.exists():
        path.unlink()
        removed_files += 1
        print(f"  ✓ Removed: {file_path}")

print(f"\n✅ Removed {removed_files} conflict CSS files")
print("")

# Remove references from HTML
print("🔧 REMOVING CSS REFERENCES FROM HTML")
html_files = list(Path('public').rglob('*.html'))

for html in html_files:
    if remove_css_references(html):
        removed_refs += 1

print(f"✅ Removed references from {removed_refs} HTML files")
print("")
print("🎊 CASCADE CONFLICTS RESOLVED!")
print("   Ultimate Beauty System is now PRIMARY!")

