#!/usr/bin/env python3
"""
Fix ALL script path inconsistencies across the entire site
Ensures 100% sitewide header and script consistency
"""
import os
import re
from pathlib import Path

def fix_script_paths(filepath):
    """Fix script paths based on file depth"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    original = content
    changes = []
    
    # Determine correct path prefix based on depth
    depth = str(filepath).count('/')
    
    if depth == 0:  # Top level (index.html, about.html, etc.)
        js_path = 'js/'
    elif depth == 1:  # One level (games/, handouts/)
        js_path = '../js/'
    elif depth == 2:  # Two levels (units/lessons/, handouts/video-activities/)
        js_path = '../../js/'
    else:
        js_path = '../' * depth + 'js/'
    
    # Fix analytics-dashboard.js path
    wrong_patterns = [
        (r'src="js/analytics-dashboard\.js"', f'src="{js_path}analytics-dashboard.js"'),
        (r'src="../js/analytics-dashboard\.js"', f'src="{js_path}analytics-dashboard.js"'),
        (r'src="../../js/analytics-dashboard\.js"', f'src="{js_path}analytics-dashboard.js"'),
    ]
    
    for pattern, replacement in wrong_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            if pattern != replacement:
                changes.append(f"analytics-dashboard path")
    
    # Fix supabase-client.js path  
    wrong_supabase = [
        (r'src="js/supabase-client\.js"', f'src="{js_path}supabase-client.js"'),
        (r'src="../js/supabase-client\.js"', f'src="{js_path}supabase-client.js"'),
        (r'src="../../js/supabase-client\.js"', f'src="{js_path}supabase-client.js"'),
    ]
    
    for pattern, replacement in wrong_supabase:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            if content != original:
                changes.append(f"supabase-client path")
                break
    
    # Fix auth-ui.js path
    wrong_auth = [
        (r'src="js/auth-ui\.js"', f'src="{js_path}auth-ui.js"'),
        (r'src="../js/auth-ui\.js"', f'src="{js_path}auth-ui.js"'),
        (r'src="../../js/auth-ui\.js"', f'src="{js_path}auth-ui.js"'),
    ]
    
    for pattern, replacement in wrong_auth:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            if content != original:
                changes.append(f"auth-ui path")
                break
    
    # Fix main.js path
    wrong_main = [
        (r'src="js/main\.js"', f'src="{js_path}main.js"'),
        (r'src="../js/main\.js"', f'src="{js_path}main.js"'),
        (r'src="../../js/main\.js"', f'src="{js_path}main.js"'),
    ]
    
    for pattern, replacement in wrong_main:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            if content != original:
                changes.append(f"main.js path")
                break
    
    # Fix daily-whakatauki.js path
    wrong_whakatauki = [
        (r'src="js/daily-whakatauki\.js"', f'src="{js_path}daily-whakatauki.js"'),
        (r'src="../js/daily-whakatauki\.js"', f'src="{js_path}daily-whakatauki.js"'),
        (r'src="../../js/daily-whakatauki\.js"', f'src="{js_path}daily-whakatauki.js"'),
    ]
    
    for pattern, replacement in wrong_whakatauki:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            if content != original:
                changes.append(f"daily-whakatauki path")
                break
    
    if content == original:
        return None  # No changes needed
    
    # Write back
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        if changes:
            print(f"✅ Fixed {len(set(changes))} path(s) in: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Failed: {filepath} - {e}")
        return False

def main():
    fixed = 0
    skipped = 0
    
    # Process all HTML files (excluding dist, archive, backups)
    exclude_dirs = {'dist', 'archive', 'archived-bloat', 'backups', 'node_modules', '.git'}
    
    print("🔧 Fixing script paths across all HTML files...")
    print("=" * 60)
    
    for root, dirs, files in os.walk('.'):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
        
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                result = fix_script_paths(filepath)
                
                if result is True:
                    fixed += 1
                elif result is None:
                    skipped += 1
    
    print("=" * 60)
    print(f"\n📊 Summary:")
    print(f"  ✅ Fixed: {fixed} files")
    print(f"  ⏭️  Skipped: {skipped} files (already correct)")
    print(f"\n🎉 Script path consistency complete!")

if __name__ == '__main__':
    main()

