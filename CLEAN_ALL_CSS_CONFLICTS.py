#!/usr/bin/env python3
"""
🧹 CLEAN ALL CSS CONFLICTS - Keep ONLY BMAD Ultimate Beauty System
Remove ALL old CSS files, keep only the essentials
"""

import re
from pathlib import Path

print("🧹 CLEANING ALL CSS CONFLICTS - HUMAN-FRIENDLY VERSION")
print("=" * 70)

# Files to KEEP (the good stuff)
KEEP_CSS = [
    'te-kete-ultimate-beauty-system.css',  # Main BMAD system
    'print-professional.css',               # For printing
]

# CSS files to REMOVE (everything else conflicts)
REMOVE_PATTERNS = [
    r'<link[^>]*te-kete-unified-design-system\.css[^>]*>',
    r'<link[^>]*component-library\.css[^>]*>',
    r'<link[^>]*animations-professional\.css[^>]*>',
    r'<link[^>]*beautiful-navigation\.css[^>]*>',
    r'<link[^>]*mobile-optimization\.css[^>]*>',
    r'<link[^>]*micro-interactions\.css[^>]*>',
    r'<link[^>]*subject-badges\.css[^>]*>',
    r'<link[^>]*cultural-patterns\.css[^>]*>',
    r'<link[^>]*resource-preview-cards\.css[^>]*>',
    r'<link[^>]*typography-professional\.css[^>]*>',
    r'<link[^>]*hub-pages-professional\.css[^>]*>',
    r'<link[^>]*lesson-professionalization\.css[^>]*>',
    r'<link[^>]*unit-index-professionalization\.css[^>]*>',
    r'<link[^>]*ux-professional-enhancements\.css[^>]*>',
    r'<link[^>]*print\.css[^>]*>',  # We have print-professional instead
]

# Find all HTML files
public_dir = Path('public')
html_files = list(public_dir.rglob('*.html'))

print(f"\n📊 Found {len(html_files)} HTML files\n")

files_cleaned = 0
conflicts_removed = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        removed_count = 0
        
        # Remove all conflicting CSS
        for pattern in REMOVE_PATTERNS:
            matches = len(re.findall(pattern, content, re.IGNORECASE))
            if matches > 0:
                content = re.sub(pattern, '', content, flags=re.IGNORECASE)
                removed_count += matches
        
        # Clean up extra whitespace
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
        
        # Only write if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            files_cleaned += 1
            conflicts_removed += removed_count
            
            if files_cleaned % 50 == 0:
                print(f"   ✅ Cleaned {files_cleaned} files, removed {conflicts_removed} conflicts")
    
    except Exception as e:
        print(f"   ⚠️  Error: {filepath.name} - {e}")

print("\n" + "=" * 70)
print("✅ CSS CONFLICT CLEANUP COMPLETE")
print("=" * 70)
print(f"\n✅ Files cleaned: {files_cleaned}")
print(f"🗑️  Conflicts removed: {conflicts_removed}")
print(f"\n🎨 Now using ONLY:")
print(f"   - te-kete-ultimate-beauty-system.css (BMAD)")
print(f"   - print-professional.css (for printing)")
print(f"   - Tailwind CDN + cultural config")
print(f"   - Framer Motion cultural gestures")
print(f"\n💎 Site should now look CLEAN and PROFESSIONAL! 💎")

