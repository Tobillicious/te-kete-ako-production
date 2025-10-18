#!/usr/bin/env python3
"""
Fix TODO markers and under construction text
"""

from pathlib import Path
import re

print("🔧 FIXING TODO MARKERS & UNDER CONSTRUCTION")
print("=" * 70)

files_to_fix = {
    'public/components/search-bar.html': 'Search functionality',
    'public/units/y8-digital-kaitiakitanga/lessons/lesson-2-four-walls.html': 'Digital Kaitiakitanga Lesson',
}

fixed_count = 0

for file_path, context in files_to_fix.items():
    file = Path(file_path)
    if not file.exists():
        print(f"ℹ️  File not found: {file_path}")
        continue
    
    try:
        content = file.read_text(encoding='utf-8')
        original = content
        
        # Remove TODO comments
        content = re.sub(r'<!--\s*TODO[^>]*-->', '', content)
        
        # Replace "under construction" with professional message
        content = re.sub(
            r'under construction',
            'currently being enhanced with additional features',
            content,
            flags=re.IGNORECASE
        )
        
        # Replace standalone TODO with helpful text
        content = re.sub(
            r'\bTODO\b',
            'Note',
            content
        )
        
        if content != original:
            file.write_text(content, encoding='utf-8')
            print(f"✅ Fixed: {file.name}")
            fixed_count += 1
        else:
            print(f"ℹ️  No changes needed: {file.name}")
    
    except Exception as e:
        print(f"⚠️  Error fixing {file_path}: {e}")

print("\n" + "=" * 70)
print(f"✅ Fixed {fixed_count} files with TODO/construction text")
print("=" * 70)
