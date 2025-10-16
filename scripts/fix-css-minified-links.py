#!/usr/bin/env python3
"""
Fix Minified CSS Links - Quick Production Fix
Changes /css/min/*.min.css to /css/*.css
Agent-9 - Broken Links Repair
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

# Map minified paths to real CSS files
CSS_FIXES = {
    '/css/min/te-kete-unified-design-system.min.css': '/css/te-kete-unified-design-system.css',
    '/css/min/component-library.min.css': '/css/component-library.css',
    '/css/min/animations-professional.min.css': '/css/animations-professional.css',
    '/css/min/beautiful-navigation.min.css': '/css/beautiful-navigation.css',
    '/css/min/lesson-professionalization.min.css': '/css/lesson-professionalization.css',
    '/css/min/unit-index-professionalization.min.css': '/css/unit-index-professionalization.css',
    '/css/min/mobile-optimization.min.css': '/css/mobile-optimization.css',
    '/css/min/print.min.css': '/css/print.css',
}

def fix_css_links(filepath):
    """Fix CSS links in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # Fix each CSS reference
        for minified_path, real_path in CSS_FIXES.items():
            # Remove version hash if present
            pattern = re.escape(minified_path) + r'(\?v=[a-z0-9]+)?'
            if re.search(pattern, content):
                content = re.sub(pattern, real_path, content)
                changes_made += 1
        
        # Save if changes made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes_made
        
        return 0
    
    except Exception as e:
        print(f"   ⚠️  {filepath.name}: {str(e)[:40]}")
        return 0

def main():
    print("🔧 FIXING MINIFIED CSS LINKS - SYSTEMATIC REPAIR")
    print("=" * 70)
    print("Replacing /css/min/*.min.css with /css/*.css\n")
    
    # Get all HTML files
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    
    # Filter out archives
    html_files = [f for f in html_files if not any(skip in str(f) for skip in ['node_modules', 'archive', 'backup', 'dist'])]
    
    print(f"Processing {len(html_files)} HTML files...\n")
    
    total_changes = 0
    files_fixed = 0
    
    for i, html_file in enumerate(html_files):
        changes = fix_css_links(html_file)
        if changes > 0:
            files_fixed += 1
            total_changes += changes
            rel_path = html_file.relative_to(PUBLIC_DIR)
            if files_fixed <= 20:  # Show first 20
                print(f"   ✅ {rel_path} ({changes} links fixed)")
        
        if (i + 1) % 200 == 0:
            print(f"   ... {i + 1}/{len(html_files)} processed")
    
    print("\n" + "=" * 70)
    print(f"✅ Fixed {total_changes} CSS links across {files_fixed} files")
    print(f"📊 Success rate: {round(files_fixed/len(html_files)*100, 1)}%")
    print(f"🎯 Pages should now load styles correctly!\n")
    
    return files_fixed

if __name__ == '__main__':
    count = main()
    print(f"📊 Total files repaired: {count}")

