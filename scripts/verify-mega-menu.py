#!/usr/bin/env python3
"""
Mega Menu Verification Script
Systematically checks if mega menu is present and functional on key pages
"""

import os
from pathlib import Path

# Key pages to verify
KEY_PAGES = [
    "public/index.html",
    "public/units/index.html",
    "public/resource-hub.html",
    # Showcase lessons
    "public/units/unit-7-digital-tech-ai-ethics/lessons/lesson-1.html",  # AI Ethics
    "public/units/y8-systems/lessons/lesson-4-1.html",  # Treaty
    "public/units/unit-1-te-ao-maori/lessons/climate-change-through-te-taiao-māori-lens.html",  # Climate
    "public/units/y8-systems/lessons/lesson-2-1.html",  # Democracy
    "public/units/y8-systems/lessons/lesson-5-1.html",  # Guided Inquiry
]

def check_mega_menu(filepath):
    """Check if file contains mega menu integration"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return 'navigation-mega-menu.html' in content
    except FileNotFoundError:
        return None  # File doesn't exist
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def main():
    print("=" * 60)
    print("🧭 MEGA MENU VERIFICATION SCRIPT")
    print("=" * 60)
    print()
    
    results = {
        'checked': 0,
        'passed': 0,
        'failed': 0,
        'not_found': 0
    }
    
    for page in KEY_PAGES:
        results['checked'] += 1
        page_name = os.path.basename(page)
        
        has_mega_menu = check_mega_menu(page)
        
        if has_mega_menu is None:
            print(f"⚠️  {page_name:50s} - FILE NOT FOUND")
            results['not_found'] += 1
        elif has_mega_menu:
            print(f"✅ {page_name:50s} - Has mega menu")
            results['passed'] += 1
        else:
            print(f"❌ {page_name:50s} - Missing mega menu")
            results['failed'] += 1
    
    print()
    print("=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"Total Checked:     {results['checked']}")
    print(f"✅ Passed:         {results['passed']}")
    print(f"❌ Failed:         {results['failed']}")
    print(f"⚠️  Not Found:     {results['not_found']}")
    print()
    
    if results['failed'] == 0 and results['not_found'] == 0:
        print("🎉 ALL KEY PAGES HAVE MEGA MENU! EXCELLENT!")
    elif results['failed'] > 0:
        print(f"🔧 {results['failed']} page(s) need mega menu added")
    
    print("=" * 60)
    
    return results

if __name__ == '__main__':
    main()

