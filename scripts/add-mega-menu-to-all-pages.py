#!/usr/bin/env python3
"""
Add Mega Menu Navigation to All HTML Pages
Professional systematic rollout across entire platform
"""

import os
import re
from pathlib import Path

# Mega menu injection code
MEGA_MENU_CODE = """    <!-- Professional Mega Menu Navigation -->
    <script>
        fetch('/components/navigation-mega-menu.html')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>"""

def should_process_file(filepath):
    """Check if file should be processed"""
    # Skip if already has mega menu
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        if 'navigation-mega-menu.html' in content:
            return False
        if '<body' not in content:
            return False
    return True

def add_mega_menu(filepath):
    """Add mega menu to HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find body tag and add mega menu right after
        pattern = r'(<body[^>]*>)'
        
        if re.search(pattern, content):
            # Insert mega menu after opening body tag
            new_content = re.sub(
                pattern,
                r'\1\n' + MEGA_MENU_CODE,
                content,
                count=1
            )
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main execution"""
    print("=" * 60)
    print("MEGA MENU SYSTEMATIC ROLLOUT")
    print("=" * 60)
    print()
    
    # Target directories
    targets = [
        'public/units',
        'public/generated-resources-alpha',
        'public/handouts',
    ]
    
    processed = 0
    skipped = 0
    errors = 0
    
    for target_dir in targets:
        if not os.path.exists(target_dir):
            print(f"⚠️  Skipping {target_dir} (not found)")
            continue
        
        print(f"📂 Processing: {target_dir}")
        
        # Find all HTML files
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    
                    if should_process_file(filepath):
                        if add_mega_menu(filepath):
                            processed += 1
                            if processed % 50 == 0:
                                print(f"   ✅ {processed} pages enhanced...")
                        else:
                            errors += 1
                    else:
                        skipped += 1
    
    print()
    print("=" * 60)
    print("ROLLOUT COMPLETE!")
    print("=" * 60)
    print(f"✅ Pages Enhanced: {processed}")
    print(f"⏭️  Skipped: {skipped} (already have mega menu)")
    print(f"❌ Errors: {errors}")
    print()
    print("🎉 Mega menu navigation now platform-wide!")
    print("=" * 60)

if __name__ == '__main__':
    main()

