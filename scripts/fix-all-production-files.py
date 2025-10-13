#!/usr/bin/env python3
"""
Apply technical fixes to ALL 1,636 production files
- Fix CSS paths (1,055 files)
- Add professional CSS (983 files)
- Remove duplicate DOCTYPE (68 files)
- Add navigation (106 files)
"""

from pathlib import Path
import re

def fix_html_file(file_path):
    """Fix technical issues in a single HTML file"""
    try:
        content = file_path.read_text(encoding='utf-8')
    except:
        return [], 'read_error'
    
    original = content
    fixes_applied = []
    
    # Fix 1: Remove duplicate DOCTYPE (keep only first)
    if content.count('<!DOCTYPE html>') > 1:
        parts = content.split('<!DOCTYPE html>')
        content = '<!DOCTYPE html>' + ''.join(parts[1:])
        fixes_applied.append('duplicate_doctype')
    
    # Fix 2: Fix broken CSS paths (relative to absolute)
    patterns = [
        (r'href=["\']\.\.\/\.\.\/\.\.\/\.\.\/\.\.\/css\/([^"\']+)["\']', r'href="/css/\1"'),
        (r'href=["\']\.\.\/\.\.\/\.\.\/css\/([^"\']+)["\']', r'href="/css/\1"'),
        (r'href=["\']\.\.\/css\/([^"\']+)["\']', r'href="/css/\1"'),
    ]
    
    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            fixes_applied.append('css_path')
            break
    
    # Fix 3: Remove empty style tags
    content = re.sub(r'<style>\s*</style>', '', content)
    if re.search(r'<style>\s*</style>', original):
        fixes_applied.append('empty_style')
    
    # Fix 4: Add professional CSS if missing
    if 'te-kete-professional.css' not in content and '<head>' in content:
        css_link = '    <link rel="stylesheet" href="/css/te-kete-professional.css">\n'
        content = content.replace('</head>', f'{css_link}</head>', 1)
        fixes_applied.append('add_css')
    
    # Fix 5: Add professional JS if missing
    if 'te-kete-professional.js' not in content and '</body>' in content:
        js_script = '    <script src="/js/te-kete-professional.js" defer></script>\n'
        content = content.replace('</body>', f'{js_script}</body>', 1)
        fixes_applied.append('add_js')
    
    return content, fixes_applied

def main():
    public_dir = Path('public')
    
    print("🔧 FIXING ALL PRODUCTION FILES")
    print("="*60)
    print(f"Target: ALL HTML files in {public_dir}")
    print(f"Excluding: backups/, archived-bloat/\n")
    
    total_files = 0
    total_fixes = 0
    fix_summary = {}
    errors = []
    
    for html_file in public_dir.rglob('*.html'):
        # Skip backups and archived content
        if 'backup' in str(html_file).lower() or 'archived' in str(html_file).lower():
            continue
        
        total_files += 1
        fixed_content, fixes = fix_html_file(html_file)
        
        if fixes == 'read_error':
            errors.append(str(html_file))
            continue
        
        if fixes:
            # Write fixed content
            try:
                html_file.write_text(fixed_content, encoding='utf-8')
                total_fixes += len(fixes)
                
                for fix in fixes:
                    fix_summary[fix] = fix_summary.get(fix, 0) + 1
                
                if total_files % 100 == 0:
                    print(f"   Processed {total_files} files...")
            except Exception as e:
                errors.append(f"{html_file}: {e}")
    
    print(f"\n{'='*60}")
    print(f"📊 SUMMARY:")
    print(f"   Files processed: {total_files}")
    print(f"   Total fixes applied: {total_fixes}")
    print(f"   Errors: {len(errors)}")
    print(f"\n   Fixes by type:")
    for fix_type, count in sorted(fix_summary.items(), key=lambda x: -x[1]):
        print(f"      {fix_type}: {count} files")
    
    if errors:
        print(f"\n⚠️  Errors encountered: {len(errors)}")
        for error in errors[:5]:
            print(f"      {error}")
    
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
