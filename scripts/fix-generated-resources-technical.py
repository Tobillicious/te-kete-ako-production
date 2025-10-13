#!/usr/bin/env python3
"""
Fix technical issues in generated-resources-alpha files
- Remove duplicate DOCTYPE
- Fix CSS paths
- Remove empty style tags
- Fix broken HTML structure
- Add missing JavaScript
"""

from pathlib import Path
import re

def fix_html_file(file_path):
    """Fix technical issues in a single HTML file"""
    content = file_path.read_text(encoding='utf-8')
    original = content
    fixes_applied = []
    
    # Fix 1: Remove duplicate DOCTYPE (keep only first)
    if content.count('<!DOCTYPE html>') > 1:
        parts = content.split('<!DOCTYPE html>')
        content = '<!DOCTYPE html>' + ''.join(parts[1:])
        fixes_applied.append('duplicate_doctype')
    
    # Fix 2: Fix broken CSS paths
    content = re.sub(
        r'href=["\']\.\.\/\.\.\/\.\.\/\.\.\/\.\.\/css\/([^"\']+)["\']',
        r'href="/css/\1"',
        content
    )
    if '../../../../../css/' in original:
        fixes_applied.append('css_path')
    
    # Fix 3: Remove empty style tags
    content = re.sub(r'<style>\s*</style>', '', content)
    if re.search(r'<style>\s*</style>', original):
        fixes_applied.append('empty_style')
    
    # Fix 4: Add te-kete-professional.css if missing
    if 'te-kete-professional.css' not in content and '<head>' in content:
        css_link = '    <link rel="stylesheet" href="/css/te-kete-professional.css">\n'
        content = content.replace('</head>', f'{css_link}</head>')
        fixes_applied.append('add_css')
    
    # Fix 5: Add te-kete-professional.js if missing
    if 'te-kete-professional.js' not in content and '</body>' in content:
        js_script = '    <script src="/js/te-kete-professional.js" defer></script>\n'
        content = content.replace('</body>', f'{js_script}</body>')
        fixes_applied.append('add_js')
    
    # Fix 6: Remove nested HTML tags (keep only outermost)
    # This is complex - flag for manual review
    if content.count('<html') > 1:
        fixes_applied.append('MANUAL_REVIEW_nested_html')
    
    return content, fixes_applied

def main():
    handouts_dir = Path('public/generated-resources-alpha/handouts')
    lessons_dir = Path('public/generated-resources-alpha/lessons')
    
    print("🔧 FIXING TECHNICAL ISSUES IN GENERATED RESOURCES\n")
    
    total_files = 0
    total_fixes = 0
    fix_summary = {}
    
    for directory in [handouts_dir, lessons_dir]:
        if not directory.exists():
            print(f"⚠️  Directory not found: {directory}")
            continue
        
        print(f"\n📁 Processing: {directory}")
        
        for html_file in sorted(directory.glob('*.html')):
            total_files += 1
            fixed_content, fixes = fix_html_file(html_file)
            
            if fixes:
                # Write fixed content
                html_file.write_text(fixed_content, encoding='utf-8')
                total_fixes += len(fixes)
                
                print(f"   ✅ {html_file.name}: {', '.join(fixes)}")
                
                for fix in fixes:
                    fix_summary[fix] = fix_summary.get(fix, 0) + 1
            else:
                print(f"   ✓  {html_file.name}: No fixes needed")
    
    print(f"\n{'='*60}")
    print(f"📊 SUMMARY:")
    print(f"   Files processed: {total_files}")
    print(f"   Total fixes applied: {total_fixes}")
    print(f"\n   Fixes by type:")
    for fix_type, count in sorted(fix_summary.items()):
        print(f"      {fix_type}: {count} files")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
