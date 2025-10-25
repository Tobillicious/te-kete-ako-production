#!/usr/bin/env python3
"""
FIX Y8 DIGITAL KAITIAKITANGA LESSONS PROFESSIONALLY
- Add professionalization-system.css
- Remove duplicate component loading
- Fix CSS includes order
"""

from pathlib import Path
import re

LESSON_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public/units/y8-digital-kaitiakitanga/lessons")

def fix_lesson_file(file_path):
    """Fix a single lesson file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = []
    
    # 1. Add professionalization-system.css if not present
    if '/css/professionalization-system.css' not in content:
        # Find where te-kete-professional.css is loaded and add after it
        if '/css/te-kete-professional.css' in content:
            content = content.replace(
                '<link rel="stylesheet" href="/css/te-kete-professional.css"/>',
                '<link rel="stylesheet" href="/css/te-kete-professional.css"/>\n    <link rel="stylesheet" href="/css/professionalization-system.css"/>'
            )
            changes_made.append("Added professionalization-system.css")
    
    # 2. Remove duplicate footer loading (appears 2x in many files)
    footer_pattern = r'<div id="footer-container"></div>\s*<script>\s*fetch\(\'/components/footer\.html\'\).*?</script>'
    footer_matches = list(re.finditer(footer_pattern, content, re.DOTALL))
    if len(footer_matches) > 1:
        # Keep first occurrence, remove others
        for match in footer_matches[1:]:
            content = content.replace(match.group(0), '<!-- Footer already loaded above, duplicate removed -->')
        changes_made.append(f"Removed {len(footer_matches)-1} duplicate footer loading(s)")
    
    # 3. Remove duplicate mobile nav loading
    mobile_nav_pattern = r'<div id="mobile-nav-bottom"></div>\s*<script>\s*fetch\(\'/components/mobile-bottom-nav\.html\'\).*?</script>'
    mobile_matches = list(re.finditer(mobile_nav_pattern, content, re.DOTALL))
    if len(mobile_matches) > 1:
        for match in mobile_matches[1:]:
            content = content.replace(match.group(0), '<!-- Mobile nav already loaded above, duplicate removed -->')
        changes_made.append(f"Removed {len(mobile_matches)-1} duplicate mobile nav loading(s)")
    
    # 4. Remove duplicate FAB loading
    fab_pattern = r'<div id="fab-quick-actions"></div>\s*<script>\s*fetch\(\'/components/quick-actions-fab\.html\'\).*?</script>'
    fab_matches = list(re.finditer(fab_pattern, content, re.DOTALL))
    if len(fab_matches) > 1:
        for match in fab_matches[1:]:
            content = content.replace(match.group(0), '<!-- FAB already loaded above, duplicate removed -->')
        changes_made.append(f"Removed {len(fab_matches)-1} duplicate FAB loading(s)")
    
    # 5. Remove duplicate framer-cultural-gestures loading
    framer_pattern = r'<script src="/js/framer-cultural-gestures-ultimate\.js" defer></script>'
    framer_count = content.count(framer_pattern)
    if framer_count > 1:
        # Keep first, remove rest
        parts = content.split(framer_pattern)
        content = framer_pattern.join([parts[0], '<!-- Framer gestures already loaded above, duplicate removed -->'] + parts[2:])
        changes_made.append(f"Removed {framer_count-1} duplicate framer script loading(s)")
    
    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes_made
    return False, []

def main():
    print("🔧 FIXING Y8 DIGITAL KAITIAKITANGA LESSONS")
    print("=" * 60)
    print("")
    
    lesson_files = sorted(LESSON_DIR.glob("lesson-*.html"))
    storytelling = LESSON_DIR / "digital-storytelling-with-pūrākau-framework.html"
    if storytelling.exists():
        lesson_files = [storytelling] + lesson_files
    
    total_fixed = 0
    total_changes = 0
    
    for lesson_file in lesson_files:
        print(f"📝 Processing: {lesson_file.name}")
        changed, changes = fix_lesson_file(lesson_file)
        
        if changed:
            total_fixed += 1
            total_changes += len(changes)
            for change in changes:
                print(f"   ✅ {change}")
        else:
            print(f"   ℹ️  No changes needed")
        print("")
    
    print("=" * 60)
    print("✅ PROCESSING COMPLETE")
    print(f"   Files processed: {len(lesson_files)}")
    print(f"   Files modified: {total_fixed}")
    print(f"   Total changes: {total_changes}")
    print("")
    print("NEXT: Remove inline styles and replace with CSS classes")
    print("=" * 60)

if __name__ == "__main__":
    main()

