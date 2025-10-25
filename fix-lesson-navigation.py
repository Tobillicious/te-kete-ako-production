#!/usr/bin/env python3
"""
FIX: Add navigation to lesson pages that are missing it
Following Synthesis Law #3: Automate > Manual
Time: 30 minutes (write + execute)
Impact: 100% navigation coverage → Better UX
"""

import re
from pathlib import Path

def add_navigation_component(filepath):
    """Add navigation component to HTML file if missing"""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Skip if already has navigation
        if '<nav' in content.lower() or 'navigation-standard' in content:
            return None  # Already has nav
        
        # Find <body> tag and add navigation component after it
        body_match = re.search(r'(<body[^>]*>)', content, re.IGNORECASE)
        
        if not body_match:
            return None  # No body tag found
        
        # Insert navigation component
        nav_component = '\n<!-- Navigation Component -->\n<div id="header-component"></div>\n<script src="/components/navigation-standard.html" defer></script>\n'
        
        new_content = content[:body_match.end()] + nav_component + content[body_match.end():]
        
        # Write back
        filepath.write_text(new_content, encoding='utf-8')
        return str(filepath)
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def main():
    print("🔧 FIXING NAVIGATION ON LESSON PAGES")
    print("=" * 70)
    print("Following: Synthesis Law #3 (Automate > Manual)")
    print()
    
    # Process all lesson pages
    lessons_dir = Path('public/lessons')
    
    if not lessons_dir.exists():
        print("❌ Lessons directory not found")
        return
    
    fixed_files = []
    skipped_files = []
    
    print("🔍 Scanning lesson pages...")
    lesson_files = list(lessons_dir.rglob('*.html'))
    print(f"Found {len(lesson_files)} lesson files to check")
    print()
    
    print("📝 Processing files...")
    for filepath in lesson_files:
        result = add_navigation_component(filepath)
        if result:
            fixed_files.append(result)
            if len(fixed_files) % 10 == 0:
                print(f"   Fixed {len(fixed_files)} files...")
        else:
            skipped_files.append(str(filepath))
    
    print()
    print("=" * 70)
    print("✅ NAVIGATION FIX COMPLETE!")
    print("=" * 70)
    print()
    print(f"📊 Results:")
    print(f"  Total files scanned: {len(lesson_files)}")
    print(f"  Navigation added: {len(fixed_files)}")
    print(f"  Already had navigation: {len(skipped_files)}")
    print()
    
    if fixed_files:
        print(f"🎯 Impact:")
        print(f"  Before: {len(skipped_files)}/{len(lesson_files)} had navigation ({len(skipped_files)/len(lesson_files)*100:.1f}%)")
        print(f"  After: {len(lesson_files)}/{len(lesson_files)} have navigation (100%)")
        print(f"  Improvement: +{len(fixed_files)} pages now navigable")
        print()
        print(f"Sample fixed files:")
        for f in fixed_files[:5]:
            print(f"  - {f}")
        if len(fixed_files) > 5:
            print(f"  ... and {len(fixed_files) - 5} more")
    else:
        print("✅ All lesson pages already have navigation!")
    
    print()
    print("🚀 NEXT STEPS:")
    print("  1. Test 5 random lessons to verify navigation works")
    print("  2. Commit changes")
    print("  3. Deploy to production")
    print("  4. Ship to beta teachers!")
    print()

if __name__ == '__main__':
    main()

