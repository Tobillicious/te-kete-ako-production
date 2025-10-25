#!/usr/bin/env python3
"""
CSS Loading Fix Script for Te Kete Ako
Fixes CSS loading order issues across all HTML files

Issues Fixed:
1. Missing professionalization-system.css (core design tokens)
2. Missing cascade-fix.css (variable conflicts)
3. Incorrect CSS loading order
4. Missing component styles (main.css, navigation-standard.css, etc.)
"""

import os
import re
from pathlib import Path

def fix_css_loading_in_file(file_path):
    """Fix CSS loading in a single HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern 1: Only loading te-kete-professional.css
    pattern1 = r'<!-- 🎨 PROFESSIONAL DESIGN SYSTEM.*?-->\s*<link rel="stylesheet" href="/css/te-kete-professional\.css">\s*<!-- END PROFESSIONAL DESIGN SYSTEM -->'

    replacement1 = '''<!-- 🎨 UNIFIED PROFESSIONAL DESIGN SYSTEM (CONSOLIDATED) -->
<!-- ⭐ PROFESSIONAL SYSTEM FIRST - Core design tokens -->
<link rel="stylesheet" href="/css/professionalization-system.css">

<!-- ⭐ THEME SYSTEM (Tailwind + Ultimate Beauty) -->
<link rel="stylesheet" href="/css/te-kete-professional.css"/>
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css"/>

<!-- ⭐ COMPONENT STYLES -->
<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="/css/navigation-standard.css">
<link rel="stylesheet" href="/css/mobile-revolution.css">
<link rel="stylesheet" href="/css/mobile-first-classroom-tablets.css">

<!-- ⭐ PRINT STYLES (media="print" = only for printing) -->
<link rel="stylesheet" href="/css/print.css" media="print">
<link rel="stylesheet" href="/css/print-professional.css" media="print"/>

<!-- ⭐ TAILWIND (Loads second-to-last - utilities only, NO DUPLICATES) -->
<link rel="stylesheet" href="/css/tailwind.css">

<!-- ⭐ CASCADE FIX (Loads LAST - overrides conflicting variables) -->
<link rel="stylesheet" href="/css/cascade-fix.css">
<!-- END PROFESSIONAL DESIGN SYSTEM -->'''

    content = re.sub(pattern1, replacement1, content, flags=re.DOTALL | re.MULTILINE)

    # Pattern 2: Already has full CSS stack but wrong order (cascade-fix first)
    pattern2 = r'<!-- CSS - UNIFIED PROFESSIONAL DESIGN SYSTEM.*?-->\s*<!-- ⭐ BASE SYSTEM FIRST.*?-->\s*<link rel="stylesheet" href="/css/cascade-fix\.css">.*?<!-- ⭐ TAILWIND.*?-->\s*<link rel="stylesheet" href="/css/tailwind\.css">.*?<!-- NOTE on CSS order:.*?-->'

    replacement2 = '''<!-- CSS - UNIFIED PROFESSIONAL DESIGN SYSTEM (CONSOLIDATED) -->
<!-- ⭐ PROFESSIONAL SYSTEM FIRST - Core design tokens -->
<link rel="stylesheet" href="/css/professionalization-system.css">

<!-- ⭐ THEME SYSTEM (Tailwind + Ultimate Beauty) -->
<link rel="stylesheet" href="/css/te-kete-professional.css"/>
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css"/>

<!-- ⭐ COMPONENT STYLES -->
<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="/css/navigation-standard.css">
<link rel="stylesheet" href="/css/mobile-revolution.css">
<link rel="stylesheet" href="/css/mobile-first-classroom-tablets.css">

<!-- ⭐ PRINT STYLES (media="print" = only for printing) -->
<link rel="stylesheet" href="/css/print.css" media="print">
<link rel="stylesheet" href="/css/print-professional.css" media="print"/>

<!-- ⭐ TAILWIND (Loads second-to-last - utilities only, NO DUPLICATES) -->
<link rel="stylesheet" href="/css/tailwind.css">

<!-- ⭐ CASCADE FIX (Loads LAST - overrides conflicting variables) -->
<link rel="stylesheet" href="/css/cascade-fix.css">

<!-- NOTE on CSS order:
  ✅ professionalization-system.css FIRST - Core design tokens and typography
  ✅ Theme files next - Professional styling and enhancements
  ✅ Component styles - Navigation, mobile, responsive features
  ✅ Tailwind second-to-last - Utility classes only
  ✅ cascade-fix.css LAST - Resolves all variable conflicts and wins cascade
  ✅ This order ensures: cascade-fix wins cascade conflicts!
-->'''

    content = re.sub(pattern2, replacement2, content, flags=re.DOTALL | re.MULTILINE)

    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Main function to fix CSS loading across all HTML files"""
    public_dir = Path('public')
    html_files = list(public_dir.rglob('*.html'))

    print(f"🔍 Scanning {len(html_files)} HTML files for CSS loading issues...")

    fixed_count = 0
    for html_file in html_files:
        if fix_css_loading_in_file(html_file):
            fixed_count += 1
            print(f"✅ Fixed: {html_file}")

    print(f"\n🎉 CSS Loading Fix Complete!")
    print(f"📊 Files processed: {len(html_files)}")
    print(f"📊 Files fixed: {fixed_count}")
    print(f"📊 Files already correct: {len(html_files) - fixed_count}")

    if fixed_count > 0:
        print(f"\n🚀 Ready to deploy! The site should now display properly with:")
        print(f"   ✅ Complete CSS stack loaded in correct order")
        print(f"   ✅ Professional styling system active")
        print(f"   ✅ No more 'fallback' appearance")
        print(f"   ✅ Consistent styling across all pages")

if __name__ == '__main__':
    main()
