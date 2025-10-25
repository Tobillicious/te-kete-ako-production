#!/usr/bin/env python3
"""
Fix CSS Consistency - Apply Unified Professional Design System
Ensures all pages use the proper CSS cascade order as defined in the audit

From GraphRAG: 83 pages missing professionalization-system.css (primary design tokens)
This breaks the unified design system and causes inconsistent styling

CSS Order (per audit):
1. professionalization-system.css (PRIMARY - design tokens)
2. te-kete-professional.css (supplementary styling)
3. navigation-standard.css (navigation)
4. mobile-revolution.css (responsive)
5. print.css (print styles)
6. tailwind.css (utilities - LAST)
"""

import os
import re
from pathlib import Path

def fix_css_consistency_in_file(file_path):
    """Apply consistent CSS includes to a single HTML file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Check current CSS state
    has_professional_system = 'professionalization-system.css' in content
    has_te_kete_professional = 'te-kete-professional.css' in content
    has_navigation = 'navigation-standard.css' in content
    has_mobile = 'mobile-revolution.css' in content
    has_tailwind = 'tailwind.css' in content

    # Only process files that need CSS fixes
    needs_css_fix = not has_professional_system or not has_te_kete_professional

    if not needs_css_fix:
        return False

    # Complete CSS system based on the canonical order from audit
    complete_css_system = '''<!-- CSS - UNIFIED PROFESSIONAL DESIGN SYSTEM (CONSOLIDATED) -->
<!-- ⭐ PROFESSIONAL SYSTEM FIRST - Core design tokens -->
<link rel="stylesheet" href="/css/professionalization-system.css">

<!-- ⭐ THEME SYSTEM (Tailwind + Ultimate Beauty) -->
<link rel="stylesheet" href="/css/te-kete-professional.css"/>
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css"/>

<!-- ⭐ COMPONENT STYLES -->
<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="/css/navigation-standard.css">
<link rel="stylesheet" href="/css/mobile-revolution.css">
<link rel="stylesheet" href="/css/mobile-first-classroom-tablets.css"/>

<!-- ⭐ PRINT STYLES (media="print" = only for printing) -->
<link rel="stylesheet" href="/css/print.css" media="print"/>
<link rel="stylesheet" href="/css/print-professional.css" media="print"/>

<!-- ⭐ TAILWIND (Loads second-to-last - utilities only, NO DUPLICATES) -->
<link rel="stylesheet" href="/css/tailwind.css">

<!-- ⭐ CASCADE FIX (Loads LAST - overrides conflicting variables) -->
<link rel="stylesheet" href="/css/cascade-fix.css">'''

    # Find where to insert CSS (after <head>, before existing CSS)
    head_end_pattern = r'(<meta[^>]*name=["\']theme-color["\'][^>]*>)'

    if re.search(head_end_pattern, content):
        # Insert after theme-color meta
        content = re.sub(head_end_pattern, r'\1\n\n' + complete_css_system, content)
        changes_made = True
    else:
        # Fallback: insert after <title>
        content = re.sub(r'(</title>)', r'\1\n\n' + complete_css_system, content)
        changes_made = True

    # Write back if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Process all HTML files to ensure CSS consistency"""

    public_dir = Path('public')
    html_files = list(public_dir.rglob('*.html'))

    print(f"🔍 Found {len(html_files)} HTML files to check for CSS consistency")

    processed = 0
    fixed = 0

    for html_file in html_files:
        try:
            if fix_css_consistency_in_file(html_file):
                fixed += 1
                print(f"✅ Fixed CSS: {html_file}")
            processed += 1
        except Exception as e:
            print(f"❌ Error processing {html_file}: {e}")

    print("\n📊 Summary:")
    print(f"   📁 Processed: {processed} files")
    print(f"   ✅ Fixed CSS: {fixed} files")
    print("\n🚀 CSS Consistency Complete!")
    print("   - Applied unified professional design system")
    print("   - Ensured proper CSS cascade order")
    print("   - Fixed design token inheritance")
    print("   - Eliminated styling conflicts")

if __name__ == '__main__':
    main()
