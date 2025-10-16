#!/usr/bin/env python3
"""
Add mega menu to showcase lessons that are missing it
Critical for October 22 presentation!
"""

import re

MEGA_MENU_CODE = '''    <!-- Professional Mega Menu Navigation -->
    <script>
        fetch('/components/navigation-mega-menu.html')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>
'''

SHOWCASE_LESSONS = [
    "public/y8-systems/lessons/lesson-2-1.html",  # Democracy
    "public/y8-systems/lessons/lesson-4-1.html",  # Treaty
    "public/y8-systems/lessons/lesson-5-1.html",  # Guided Inquiry
]

def add_mega_menu(filepath):
    """Add mega menu to file if missing"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has mega menu
        if 'navigation-mega-menu.html' in content:
            return 'already'
        
        # Find <body> tag and add mega menu right after
        pattern = r'(<body[^>]*>)'
        replacement = r'\1\n' + MEGA_MENU_CODE
        
        new_content = re.sub(pattern, replacement, content, count=1)
        
        if new_content == content:
            return 'no_body_tag'
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return 'added'
        
    except FileNotFoundError:
        return 'not_found'
    except Exception as e:
        return f'error: {e}'

def main():
    print("=" * 60)
    print("🚨 FIXING MEGA MENU ON SHOWCASE LESSONS")
    print("=" * 60)
    print()
    
    results = {'added': 0, 'already': 0, 'errors': 0}
    
    for filepath in SHOWCASE_LESSONS:
        filename = filepath.split('/')[-1]
        print(f"Processing: {filename:40s}", end=" ")
        
        result = add_mega_menu(filepath)
        
        if result == 'added':
            print("✅ Mega menu added!")
            results['added'] += 1
        elif result == 'already':
            print("✅ Already has mega menu")
            results['already'] += 1
        elif result == 'not_found':
            print("⚠️  File not found")
            results['errors'] += 1
        else:
            print(f"❌ {result}")
            results['errors'] += 1
    
    print()
    print("=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"✅ Added mega menu: {results['added']}")
    print(f"✅ Already had it: {results['already']}")
    print(f"❌ Errors: {results['errors']}")
    print()
    
    if results['added'] > 0:
        print(f"🎉 Success! {results['added']} showcase lesson(s) now have mega menu!")
    
    print("=" * 60)

if __name__ == '__main__':
    main()

