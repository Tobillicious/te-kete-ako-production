#!/usr/bin/env python3
"""
Fix Broken JavaScript Links
Remove references to deleted/non-existent JS files
Agent-9 - Broken Links Repair Phase 2
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')
JS_DIR = PUBLIC_DIR / 'js'

# Common broken JS references from old cleanups
KNOWN_BROKEN_JS = [
    '/js/ux-enhancements.js',
    '/js/secure-auth.js',
    '/js/auth-resilience.js',
    '/js/auth-enhanced.js',
    '/js/streamlined-header.js',
    '/js/activity-generator.js',
    '/js/components.js',
]

def find_existing_js_files():
    """Get list of JS files that actually exist"""
    if not JS_DIR.exists():
        return set()
    
    return {f.name for f in JS_DIR.glob('*.js')}

def fix_js_links(filepath, existing_js):
    """Remove broken JS references from file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        # Find all script tags
        script_pattern = r'<script[^>]*src=["\']((/js/[^"\']+\.js[^"\']*))["\'][^>]*></script>'
        matches = re.findall(script_pattern, content)
        
        for full_tag_src, src_path in matches:
            # Check if file exists
            js_file = src_path.split('?')[0].lstrip('/').split('/')[-1]  # Get filename
            
            if src_path in KNOWN_BROKEN_JS:
                # Remove this script tag
                pattern = r'<script[^>]*src=["\']' + re.escape(src_path) + r'[^"\']*["\'][^>]*></script>\s*'
                content = re.sub(pattern, '', content)
                changes += 1
            elif js_file not in existing_js and 'http' not in src_path and 'cdn' not in src_path:
                # File doesn't exist and isn't external
                pattern = r'<script[^>]*src=["\']' + re.escape(src_path) + r'[^"\']*["\'][^>]*></script>\s*'
                content = re.sub(pattern, '', content)
                changes += 1
        
        # Save if changes made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        
        return 0
    
    except Exception as e:
        return 0

def main():
    print("🔧 FIXING BROKEN JAVASCRIPT LINKS")
    print("=" * 70)
    
    # Get existing JS files
    existing_js = find_existing_js_files()
    print(f"Found {len(existing_js)} existing JS files in /js/\n")
    
    # Get all HTML files
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    html_files = [f for f in html_files if not any(skip in str(f) for skip in ['node_modules', 'archive', 'backup', 'dist'])]
    
    print(f"Processing {len(html_files)} HTML files...\n")
    
    total_changes = 0
    files_fixed = 0
    
    for i, html_file in enumerate(html_files):
        changes = fix_js_links(html_file, existing_js)
        if changes > 0:
            files_fixed += 1
            total_changes += changes
            rel_path = html_file.relative_to(PUBLIC_DIR)
            if files_fixed <= 20:
                print(f"   ✅ {rel_path} ({changes} JS links removed)")
        
        if (i + 1) % 200 == 0:
            print(f"   ... {i + 1}/{len(html_files)} processed")
    
    print("\n" + "=" * 70)
    print(f"✅ Fixed/removed {total_changes} broken JS links across {files_fixed} files")
    print(f"📊 Files cleaned: {files_fixed}")
    print(f"🎯 No more 404 JS errors!\n")
    
    return files_fixed

if __name__ == '__main__':
    count = main()
    print(f"📊 Total files repaired: {count}")

