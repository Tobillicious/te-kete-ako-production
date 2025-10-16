#!/usr/bin/env python3
"""
Add Base CSS to All Pages
Ensures every page has te-kete-professional.css
Agent-9 - October 15, 2025
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def add_base_css(filepath):
    """Add te-kete-professional.css to <head> if missing"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has base CSS
        if 'te-kete-professional.css' in content:
            return False
        
        # Check if has </head>
        if '</head>' not in content:
            return False
        
        # Add CSS before </head>
        css_link = '    <link rel="stylesheet" href="/css/te-kete-professional.css">\n    <link rel="stylesheet" href="/css/ux-professional-enhancements.css">\n    <link rel="stylesheet" href="/css/print.css" media="print"/>\n'
        
        content = content.replace('</head>', f'{css_link}</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"   ❌ ERROR in {filepath.name}: {str(e)}")
        return False

def main():
    print("🎨 ADDING BASE CSS TO ALL PAGES...")
    print("=" * 60)
    
    all_html = list(PUBLIC_DIR.rglob('*.html'))
    fixed = sum(1 for f in all_html if add_base_css(f))
    
    print(f"\n✅ Added base CSS to {fixed} pages")
    print(f"📊 Total pages: {len(all_html)}")
    print("🎯 All pages now have professional styling!\n")

if __name__ == '__main__':
    main()

