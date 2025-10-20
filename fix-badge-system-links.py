#!/usr/bin/env python3
"""
Fix Badge System Incorrect Stylesheet Links
Removes the incorrect: <link rel="stylesheet" href="/components/badge-system.html">
from all HTML files in the public directory.

The badge-system.html is a component with CSS/JS that should not be loaded as a stylesheet.
The badge system auto-initializes on page load via its own script.
"""

from pathlib import Path
import re

def fix_badge_system_link(file_path):
    """Remove incorrect badge-system stylesheet link from a file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # Pattern to match the incorrect badge system link
        # Handles variations with/without closing >
        patterns = [
            r'<link\s+rel="stylesheet"\s+href="/components/badge-system\.html"\s*/?>',
            r'<link\s+href="/components/badge-system\.html"\s+rel="stylesheet"\s*/?>',
        ]
        
        for pattern in patterns:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # Only write if content changed
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    public_dir = Path('public')
    
    if not public_dir.exists():
        print("Error: public/ directory not found")
        return
    
    print("🔧 Fixing incorrect badge-system.html stylesheet links...")
    print()
    
    # Find all HTML files
    html_files = list(public_dir.rglob('*.html'))
    print(f"Found {len(html_files)} HTML files")
    
    fixed_count = 0
    for html_file in html_files:
        # Skip backup files
        if '.bak' in str(html_file) or '.backup' in str(html_file):
            continue
            
        if fix_badge_system_link(html_file):
            fixed_count += 1
            if fixed_count % 100 == 0:
                print(f"Fixed {fixed_count} files...")
    
    print()
    print(f"✅ Complete! Fixed {fixed_count} files")
    print()
    print("The badge system will still work - it auto-initializes via its own script")
    print("when included properly as a component, not as a stylesheet.")

if __name__ == '__main__':
    main()

