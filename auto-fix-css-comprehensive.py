#!/usr/bin/env python3
"""
Comprehensive CSS/JS Fixer for Te Kete Ako
Adds missing CSS to ANY HTML file that needs it
"""

import os
import re
from pathlib import Path

# Standard CSS trio to add
CSS_TRIO = '''    <link rel="stylesheet" href="/css/main.css">
    <link rel="stylesheet" href="/css/mobile-revolution.css">
    <link rel="stylesheet" href="/css/print.css" media="print">'''

def analyze_file(file_path):
    """Analyze what CSS is missing from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check what CSS it has
        has_head = '<head' in content.lower()
        has_main = 'main.css' in content
        has_mobile = 'mobile-revolution.css' in content
        has_print = 'print.css' in content or 'print-professional.css' in content
        has_any_css = 'rel="stylesheet"' in content or 'link rel="stylesheet"' in content
        
        return {
            'has_head': has_head,
            'has_main': has_main,
            'has_mobile': has_mobile,
            'has_print': has_print,
            'has_any_css': has_any_css,
            'needs_fix': has_head and not has_main
        }
    except Exception as e:
        return {'error': str(e), 'needs_fix': False}

def fix_css_comprehensive(file_path):
    """Add missing CSS to a file intelligently"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strategy 1: If file has te-kete-ultimate-beauty-system.css, add after it
        if 'te-kete-ultimate-beauty-system.css' in content:
            pattern = r'(<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system\.css"[^>]*>)'
            if re.search(pattern, content):
                new_content = re.sub(pattern, r'\1\n' + CSS_TRIO, content, count=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return 'beauty_system'
        
        # Strategy 2: If file has design-system-v3.css, add after it
        if 'design-system-v3.css' in content:
            pattern = r'(<link rel="stylesheet" href="/css/design-system-v3\.css"[^>]*/>)'
            if re.search(pattern, content):
                new_content = re.sub(pattern, r'\1\n' + CSS_TRIO, content, count=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return 'design_system'
        
        # Strategy 3: If file has ANY stylesheet, add after the last one
        css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', content)
        if css_links:
            last_css = css_links[-1]
            new_content = content.replace(last_css, last_css + '\n' + CSS_TRIO, 1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'after_last_css'
        
        # Strategy 4: Add just before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', CSS_TRIO + '\n</head>', 1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'before_head_close'
        
        return 'no_strategy'
            
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {str(e)}")
        return f'error: {str(e)}'

def process_batch(files, dry_run=True):
    """Process a batch of files"""
    if dry_run:
        print(f"\n📋 Would fix {len(files)} files")
        for i, file_path in enumerate(files[:5], 1):
            info = analyze_file(file_path)
            print(f"   {i}. {file_path.name}")
            print(f"      Has CSS: {info['has_any_css']}, Needs: main={not info['has_main']}")
        if len(files) > 5:
            print(f"   ... and {len(files) - 5} more")
        return
    
    # Actually fix files
    fixed = {'beauty_system': 0, 'design_system': 0, 'after_last_css': 0, 'before_head_close': 0, 'no_strategy': 0, 'error': 0}
    
    for i, file_path in enumerate(files, 1):
        if i % 50 == 0:
            print(f"Progress: {i}/{len(files)} files...")
        
        result = fix_css_comprehensive(file_path)
        if result.startswith('error'):
            fixed['error'] += 1
        else:
            fixed[result] = fixed.get(result, 0) + 1
    
    print(f"\n✅ Results:")
    for strategy, count in fixed.items():
        if count > 0:
            print(f"   {strategy}: {count} files")
    
    return fixed

def main():
    print("=" * 70)
    print("🔧 COMPREHENSIVE CSS/JS FIXER - Te Kete Ako")
    print("=" * 70)
    print()
    
    base_dir = '/Users/admin/Documents/te-kete-ako-clean/public'
    
    print("🔍 Scanning all HTML files...")
    html_files = list(Path(base_dir).rglob('*.html'))
    print(f"   Found {len(html_files)} HTML files")
    
    print("\n📊 Analyzing files...")
    files_needing_fix = []
    for file_path in html_files:
        info = analyze_file(file_path)
        if info.get('needs_fix'):
            files_needing_fix.append(file_path)
    
    print(f"   {len(files_needing_fix)} files need CSS fixes")
    
    if len(files_needing_fix) == 0:
        print("\n🎉 All files already have CSS!")
        return
    
    # Dry run first
    print("\n" + "=" * 70)
    print("PHASE 1: DRY RUN - Preview")
    process_batch(files_needing_fix, dry_run=True)
    
    print("\n" + "=" * 70)
    response = input(f"\n❓ Fix {len(files_needing_fix)} files? (yes/no): ")
    
    if response.lower() != 'yes':
        print("Cancelled.")
        return
    
    print("\nPHASE 2: FIXING FILES...")
    results = process_batch(files_needing_fix, dry_run=False)
    
    print("\n" + "=" * 70)
    print(f"🎉 COMPLETE! Fixed {sum(results.values())} files")
    print("=" * 70)

if __name__ == '__main__':
    main()

