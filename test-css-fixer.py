#!/usr/bin/env python3
"""
Test CSS Fixer on 10 files only
"""

import os
import re
import shutil
from pathlib import Path

# Standard CSS trio to add
CSS_TRIO = '''    <link rel="stylesheet" href="/css/main.css">
    <link rel="stylesheet" href="/css/mobile-revolution.css">
    <link rel="stylesheet" href="/css/print.css" media="print">'''

def needs_fix(file_path):
    """Check if file needs CSS"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return '<head' in content.lower() and 'main.css' not in content
    except:
        return False

def fix_css(file_path):
    """Fix CSS in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strategy: Add after te-kete-ultimate-beauty-system.css if exists
        if 'te-kete-ultimate-beauty-system.css' in content:
            pattern = r'(<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system\.css"[^>]*>)'
            if re.search(pattern, content):
                new_content = re.sub(pattern, r'\1\n' + CSS_TRIO, content, count=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return 'beauty_system'
        
        # Strategy: Add after design-system-v3.css if exists
        if 'design-system-v3.css' in content:
            pattern = r'(<link rel="stylesheet" href="/css/design-system-v3\.css"[^>]*/>)'
            if re.search(pattern, content):
                new_content = re.sub(pattern, r'\1\n' + CSS_TRIO, content, count=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return 'design_system'
        
        # Strategy: Add after last CSS link
        css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', content)
        if css_links:
            last_css = css_links[-1]
            new_content = content.replace(last_css, last_css + '\n' + CSS_TRIO, 1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'after_last'
        
        # Strategy: Add before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', CSS_TRIO + '\n</head>', 1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'before_head'
        
        return 'no_strategy'
    except Exception as e:
        return f'error: {str(e)}'

def main():
    print("🧪 TEST CSS FIXER - 10 Files Only")
    print("=" * 70)
    
    base_dir = '/Users/admin/Documents/te-kete-ako-clean/public'
    html_files = [f for f in Path(base_dir).rglob('*.html') if needs_fix(f)]
    
    test_files = html_files[:10]
    print(f"\n✅ Found {len(test_files)} test files:")
    for i, f in enumerate(test_files, 1):
        print(f"   {i}. {f.name}")
    
    input("\nPress ENTER to fix these 10 files...")
    
    print("\n🔧 Fixing files...")
    results = {}
    for i, file_path in enumerate(test_files, 1):
        result = fix_css(file_path)
        results[result] = results.get(result, 0) + 1
        print(f"   [{i}/10] {file_path.name} → {result}")
    
    print("\n📊 Results:")
    for strategy, count in results.items():
        print(f"   {strategy}: {count} files")
    
    print("\n✅ Test complete! Check files to verify.")
    print("\nTo fix ALL files, run: python3 auto-fix-css-comprehensive.py")

if __name__ == '__main__':
    main()

