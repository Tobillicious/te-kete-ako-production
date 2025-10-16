#!/usr/bin/env python3
"""
Apply Unified Design System to Y8 Systems Unit Lessons
Systematically updates all 10 Y8 lessons with the phenomenal design system
"""

import os
import re
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
LESSONS_DIR = BASE_DIR / "public" / "y8-systems" / "lessons"

# Old CSS pattern to replace
OLD_CSS_PATTERN = r'<link rel="stylesheet" href="/css/te-kete-professional\.css">.*?<link rel="stylesheet" href="/css/.*?\.css">'

# New unified design system
NEW_CSS = '''<!-- UNIFIED DESIGN SYSTEM V2.0 -->
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">
    <link rel="stylesheet" href="/css/component-library.css">
    <link rel="stylesheet" href="/css/beautiful-navigation.css">
    <link rel="stylesheet" href="/css/print.css" media="print"/>'''

def update_lesson_file(file_path):
    """Update a single lesson file with unified design system"""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already updated
    if 'te-kete-unified-design-system.css' in content:
        print(f"  ✅ Already has unified design system")
        return False
    
    # Pattern 1: Replace old CSS imports in <head>
    pattern1 = r'<link rel="stylesheet" href="/css/te-kete-professional\.css">[\s\S]*?(?=</head>|<script)'
    if re.search(pattern1, content):
        content = re.sub(
            pattern1,
            NEW_CSS + '\n    ',
            content,
            count=1,
            flags=re.MULTILINE
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Updated with unified design system")
        return True
    
    # Pattern 2: If no old CSS, add before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'    {NEW_CSS}\n</head>', 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Added unified design system")
        return True
    
    print(f"  ⚠️  Could not update")
    return False

def main():
    """Main execution"""
    print("🎨 APPLYING UNIFIED DESIGN SYSTEM TO Y8 SYSTEMS UNIT")
    print("=" * 60)
    
    # Get all lesson files
    lesson_files = sorted(LESSONS_DIR.glob("lesson-*.html"))
    
    if not lesson_files:
        print("❌ No lesson files found!")
        return
    
    print(f"\nFound {len(lesson_files)} lesson files\n")
    
    updated_count = 0
    for lesson_file in lesson_files:
        if update_lesson_file(lesson_file):
            updated_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ COMPLETE: Updated {updated_count}/{len(lesson_files)} lessons")
    print("🎨 Y8 Systems unit now uses phenomenal unified design system!")

if __name__ == "__main__":
    main()

