#!/usr/bin/env python3
"""
Fix CSS paths in integrated content
Update the integrated handouts and lessons to use te-kete-professional.css
"""

import os
import re
from pathlib import Path

def fix_css_paths():
    """Fix CSS paths in integrated content"""
    
    # Directories with integrated content
    base_dir = Path("/Users/admin/Documents/te-kete-ako-clean/public")
    handouts_dir = base_dir / "dist-handouts"
    lessons_dir = base_dir / "dist-lessons"
    
    print("🔧 Fixing CSS paths in integrated content...")
    
    # Fix handouts
    if handouts_dir.exists():
        for handout in handouts_dir.glob("*.html"):
            if handout.name != "index.html":
                fix_file_css(handout)
    
    # Fix lessons
    if lessons_dir.exists():
        for lesson in lessons_dir.glob("*.html"):
            if lesson.name != "index.html":
                fix_file_css(lesson)
    
    print("\n✅ CSS paths fixed in all integrated content!")

def fix_file_css(file_path):
    """Fix CSS paths in a single file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace old CSS references with te-kete-professional.css
    old_patterns = [
        r'<link rel="stylesheet" href="\.\.\/css\/main\.css">',
        r'<link rel="stylesheet" href="\.\.\/css\/handout-style\.css">',
        r'<link rel="stylesheet" href="\.\.\/css\/[^"]*">',
    ]
    
    new_css = '<link rel="stylesheet" href="/css/te-kete-professional.css"/>'
    
    for pattern in old_patterns:
        content = re.sub(pattern, new_css, content)
    
    # Fix navigation paths
    content = content.replace('../../index.html', '/index.html')
    content = content.replace('../../unit-plans.html', '/unit-plans.html')
    content = content.replace('../../teachers/index.html', '/teachers/index.html')
    content = content.replace('../../lessons.html', '/lessons.html')
    content = content.replace('../../handouts.html', '/handouts.html')
    content = content.replace('../../games.html', '/games.html')
    
    # Add header component script if not present
    if '<div id="header-component"></div>' not in content:
        # Replace the old header with the component
        old_header = r'<header class="site-header no-print">.*?</header>'
        new_header = '<div id="header-component"></div>'
        content = re.sub(old_header, new_header, content, flags=re.DOTALL)
        
        # Add script at the end of body if not present
        if '<script src="/js/components/header.js"></script>' not in content:
            content = content.replace('</body>', '<script src="/js/components/header.js"></script>\n</body>')
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"  ✅ Fixed: {file_path.name}")

if __name__ == "__main__":
    fix_css_paths()
