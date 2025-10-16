#!/usr/bin/env python3
"""
Find all lesson HTML files for header deployment
Agent-9 - Overnight Sprint
"""

from pathlib import Path

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def find_lesson_files():
    """Find all lesson HTML files"""
    lesson_dirs = [
        'units/y8-statistics/lessons',
        'units/y7-maths-algebra/lessons', 
        'units/y9-science-ecology/lessons',
        'y8-systems/lessons',
        'lessons',
    ]
    
    all_lessons = []
    
    for lesson_dir in lesson_dirs:
        dir_path = PUBLIC_DIR / lesson_dir
        if dir_path.exists():
            html_files = list(dir_path.glob('**/*.html'))
            for f in html_files:
                if f.name != 'index.html':
                    rel_path = f.relative_to(PUBLIC_DIR)
                    all_lessons.append(str(rel_path))
    
    return all_lessons

if __name__ == '__main__':
    lessons = find_lesson_files()
    print(f"Found {len(lessons)} lesson pages")
    for lesson in lessons[:50]:  # First 50
        print(f"  {lesson}")


