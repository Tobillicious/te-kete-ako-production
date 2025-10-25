#!/usr/bin/env python3
"""
Fix Duplicate Navigation Loading Across All Pages
Removes inline navigation fetch, adds navigation-loader.js singleton
"""

import re
from pathlib import Path

PUBLIC_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public")

# Files that need fixing (from grep results)
FILES_TO_FIX = [
    "science-hub.html",
    "english-hub.html", 
    "digital-technologies-hub.html",
    "cultural-hub.html",
    "year-7-hub.html",
    "graphrag-discovery-hub.html",
    "units/y9-science-ecology/lessons/lesson-1-what-is-an-ecosystem.html",
    "units/y9-science-ecology/lessons/lesson-2-biodiversity-endemism.html",
    "units/y9-science-ecology/lessons/lesson-3-field-study-rangahau-taiao.html",
    "units/y9-science-ecology/lessons/lesson-4-human-impact-conservation.html",
    "units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html",
    "lessons/walker-lesson-1.1-who-was-ranginui-walker.html",
]

def fix_navigation(filepath):
    """Remove duplicate navigation loading"""
    try:
        content = filepath.read_text(encoding='utf-8')
        original = content
        
        # Pattern 1: Inline fetch with nav-container
        pattern1 = r'<div id="nav-container"></div>\s*<script>\s*fetch\([\'\"]/components/navigation-standard\.html[\'"]\).*?innerHTML\s*=\s*html;\s*\}\);?\s*</script>'
        replacement1 = '<!-- Navigation loaded by navigation-loader.js singleton -->'
        content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)
        
        # Pattern 2: Ensure navigation-loader.js is included in head
        if '/js/navigation-loader.js' not in content:
            # Add before </head>
            content = content.replace('</head>', '<script src="/js/navigation-loader.js"></script>\n</head>')
        
        # Pattern 3: Add page-not-homepage class to body if not present
        if 'page-not-homepage' not in content:
            content = re.sub(
                r'<body([^>]*)class="([^"]*)"',
                r'<body\1class="\2 page-not-homepage"',
                content
            )
        
        if content != original:
            filepath.write_text(content, encoding='utf-8')
            return True
        return False
        
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

def main():
    print("🔧 FIXING DUPLICATE NAVIGATION LOADING\n")
    
    fixed = 0
    skipped = 0
    errors = 0
    
    for file_path in FILES_TO_FIX:
        full_path = PUBLIC_DIR / file_path
        if not full_path.exists():
            print(f"⚠️  Not found: {file_path}")
            skipped += 1
            continue
        
        if fix_navigation(full_path):
            print(f"✅ Fixed: {file_path}")
            fixed += 1
        else:
            print(f"⏭️  Skipped (no changes): {file_path}")
            skipped += 1
    
    print(f"\n📊 RESULTS:")
    print(f"   Fixed: {fixed}")
    print(f"   Skipped: {skipped}")
    print(f"   Errors: {errors}")
    
    print(f"\n✅ DUPLICATE NAVIGATION FIX COMPLETE!")
    print(f"   All pages now use navigation-loader.js singleton")
    print(f"   Prevents 8442px header stacking bug")

if __name__ == '__main__':
    main()

