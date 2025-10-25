#!/usr/bin/env python3
"""
Fix Missing CSS/JS Includes - Comprehensive Scan & Repair
Finds all HTML files missing standard CSS/JS imports and fixes them systematically.

Usage: python3 fix-missing-css-js-complete.py
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Standard CSS stack that should be in every page
STANDARD_CSS = [
    'te-kete-ultimate-beauty-system.css',
    'te-kete-professional.css',
    'main.css',
    'professionalization-system.css',
    'navigation-standard.css',
]

# Standard JS that should be in every page
STANDARD_JS = [
    'supabase-singleton.js',
    'te-kete-professional.js',
    'posthog-analytics.js',
]

def find_missing_css_js():
    """Scan all HTML files and find which ones are missing standard includes."""
    public_dir = '/Users/admin/Documents/te-kete-ako-clean/public'
    missing_files = []
    
    print("🔍 Scanning for missing CSS/JS includes...")
    print(f"   Checking: {public_dir}\n")
    
    # Find all HTML files
    for root, dirs, files in os.walk(public_dir):
        # Skip certain directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if not file.endswith('.html'):
                continue
            
            filepath = os.path.join(root, file)
            rel_path = filepath.replace(public_dir, '')
            
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                missing_items = []
                
                # Check for each standard CSS
                for css in STANDARD_CSS:
                    if css not in content and f'/css/{css}' not in content:
                        missing_items.append(f"CSS:{css}")
                
                # Check for each standard JS
                for js in STANDARD_JS:
                    if js not in content and f'/js/{js}' not in content:
                        missing_items.append(f"JS:{js}")
                
                if missing_items:
                    missing_files.append({
                        'path': filepath,
                        'rel_path': rel_path,
                        'missing': missing_items,
                        'count': len(missing_items)
                    })
            
            except Exception as e:
                print(f"   ⚠️  Error reading {rel_path}: {e}")
    
    return missing_files

def fix_file(filepath, missing_items):
    """Add missing CSS/JS to a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Extract what's missing
        missing_css = [item.split(':')[1] for item in missing_items if item.startswith('CSS:')]
        missing_js = [item.split(':')[1] for item in missing_items if item.startswith('JS:')]
        
        # Add missing CSS before </head>
        if missing_css:
            css_lines = '\n'.join([
                f'<link rel="stylesheet" href="/css/{css}">'
                for css in missing_css
            ])
            content = content.replace('</head>', f'{css_lines}\n</head>')
        
        # Add missing JS before </body>
        if missing_js:
            js_lines = '\n'.join([
                f'<script src="/js/{js}" defer></script>'
                for js in missing_js
            ])
            if '</body>' in content:
                content = content.replace('</body>', f'{js_lines}\n</body>')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    
    except Exception as e:
        print(f"   Error fixing {filepath}: {e}")
        return False
    
    return False

def main():
    """Main execution."""
    missing_files = find_missing_css_js()
    
    print(f"📊 SCAN RESULTS\n")
    print(f"Total files missing CSS/JS: {len(missing_files)}")
    
    if not missing_files:
        print("✅ All files have complete CSS/JS includes!")
        return
    
    # Group by directory
    by_dir = defaultdict(list)
    for file_info in missing_files:
        dir_path = os.path.dirname(file_info['rel_path'])
        by_dir[dir_path].append(file_info)
    
    print(f"\n📁 BY DIRECTORY:\n")
    for dir_path in sorted(by_dir.keys()):
        files = by_dir[dir_path]
        print(f"   {dir_path or '/'}  ({len(files)} files)")
        for file_info in files[:3]:  # Show first 3
            print(f"      • {os.path.basename(file_info['path'])} - missing: {', '.join([x.split(':')[1] for x in file_info['missing'][:2]])}")
        if len(files) > 3:
            print(f"      + {len(files) - 3} more...")
    
    # Ask to fix
    print(f"\n🔧 FIX THESE FILES?\n")
    response = input(f"Fix all {len(missing_files)} files? (y/n): ").strip().lower()
    
    if response != 'y':
        print("Cancelled.")
        return
    
    # Fix all files
    fixed_count = 0
    for file_info in missing_files:
        if fix_file(file_info['path'], file_info['missing']):
            fixed_count += 1
            print(f"✅ Fixed: {file_info['rel_path']}")
        else:
            print(f"❌ Failed: {file_info['rel_path']}")
    
    print(f"\n🎉 COMPLETE: Fixed {fixed_count}/{len(missing_files)} files")

if __name__ == '__main__':
    main()
