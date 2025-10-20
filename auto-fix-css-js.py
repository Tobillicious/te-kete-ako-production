#!/usr/bin/env python3
"""
Automated CSS/JS Fixer for Te Kete Ako
Systematically adds missing CSS/JS includes to HTML files
"""

import os
import re
from pathlib import Path

# Standard CSS trio to add
CSS_TRIO = '''<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="/css/mobile-revolution.css">
<link rel="stylesheet" href="/css/print.css" media="print">'''

def needs_css_fix(file_path):
    """Check if file needs CSS fixes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Check if it has te-kete-ultimate-beauty-system but NOT main.css
            has_beauty = 'te-kete-ultimate-beauty-system.css' in content
            has_main = 'main.css' in content
            return has_beauty and not has_main
    except Exception as e:
        print(f"⚠️  Error reading {file_path}: {str(e)}")
        return False

def fix_css(file_path):
    """Add missing CSS to a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the te-kete-ultimate-beauty-system.css line
        pattern = r'(<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system\.css"[^>]*>)'
        
        if re.search(pattern, content):
            # Add CSS trio after it
            new_content = re.sub(
                pattern,
                r'\1\n' + CSS_TRIO,
                content,
                count=1
            )
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        else:
            print(f"⚠️  Pattern not found in {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {str(e)}")
        return False

def process_directory(directory, dry_run=True, limit=None):
    """Process all HTML files in a directory"""
    html_files = list(Path(directory).rglob('*.html'))
    
    print(f"\n🔍 Found {len(html_files)} HTML files in {directory}")
    
    # Filter to files that need fixing
    files_to_fix = []
    for file_path in html_files:
        if needs_css_fix(file_path):
            files_to_fix.append(file_path)
            if limit and len(files_to_fix) >= limit:
                break
    
    print(f"🎯 {len(files_to_fix)} files need CSS fixes")
    
    if dry_run:
        print("\n📋 DRY RUN - Would fix:")
        for i, file_path in enumerate(files_to_fix[:10], 1):
            print(f"   {i}. {file_path}")
        if len(files_to_fix) > 10:
            print(f"   ... and {len(files_to_fix) - 10} more")
        return files_to_fix
    
    # Actually fix files
    fixed_count = 0
    failed_count = 0
    
    for i, file_path in enumerate(files_to_fix, 1):
        print(f"[{i}/{len(files_to_fix)}] Fixing {file_path.name}...", end=' ')
        
        if fix_css(file_path):
            print("✅")
            fixed_count += 1
        else:
            print("❌")
            failed_count += 1
    
    print(f"\n✅ Fixed: {fixed_count}")
    print(f"❌ Failed: {failed_count}")
    
    return files_to_fix

def main():
    print("=" * 70)
    print("🔧 AUTOMATED CSS/JS FIXER - Te Kete Ako")
    print("=" * 70)
    print()
    
    # Test on a few files first
    print("PHASE 1: DRY RUN on /public root files")
    public_files = process_directory('/Users/admin/Documents/te-kete-ako-clean/public', dry_run=True, limit=10)
    
    print("\n" + "=" * 70)
    response = input("\n❓ Proceed with actual fixes? (yes/no): ")
    
    if response.lower() != 'yes':
        print("Cancelled.")
        return
    
    print("\nPHASE 2: FIXING FILES...")
    
    # Fix in batches
    directories = [
        '/Users/admin/Documents/te-kete-ako-clean/public',
    ]
    
    total_fixed = 0
    for directory in directories:
        print(f"\n📂 Processing {directory}...")
        files = process_directory(directory, dry_run=False)
        total_fixed += len(files)
    
    print("\n" + "=" * 70)
    print(f"🎉 COMPLETE! Fixed {total_fixed} files total")
    print("=" * 70)

if __name__ == '__main__':
    main()

