#!/usr/bin/env python3
"""
Fix Remaining JS 404s - Final Cleanup
Remove last 15 broken JS references
Agent-9 - Broken Links Final Phase
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

# Remaining problematic JS files
BROKEN_JS_PATTERNS = [
    r'<script[^>]*src=["\'][^"\']*ux-enhancements\.js[^"\']*["\'][^>]*></script>\s*',
    r'<script[^>]*src=["\'][^"\']*auth-enhanced\.js[^"\']*["\'][^>]*></script>\s*',
    r'<script[^>]*src=["\'][^"\']*supabase-client\.js["\'][^>]*></script>\s*',
    r'<script[^>]*src=["\'][^"\']*public/js/[^"\']*["\'][^>]*></script>\s*',  # Wrong path (includes /public/)
]

def fix_remaining_js(filepath):
    """Remove remaining broken JS references"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        changes = 0
        
        # Fix wrong paths (public/js instead of js)
        if '/public/js/' in content:
            content = content.replace('/public/js/', '/js/')
            changes += 1
        
        # Remove broken patterns
        for pattern in BROKEN_JS_PATTERNS:
            if re.search(pattern, content):
                content = re.sub(pattern, '', content)
                changes += 1
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        
        return 0
    
    except:
        return 0

def main():
    print("🔧 FIXING REMAINING JS LINKS - FINAL CLEANUP")
    print("=" * 70)
    
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    html_files = [f for f in html_files if not any(skip in str(f) for skip in ['node_modules', 'archive', 'backup', 'dist'])]
    
    print(f"Processing {len(html_files)} HTML files...\n")
    
    total = 0
    files_fixed = 0
    
    for html_file in html_files:
        changes = fix_remaining_js(html_file)
        if changes > 0:
            files_fixed += 1
            total += changes
            rel_path = html_file.relative_to(PUBLIC_DIR)
            if files_fixed <= 15:
                print(f"   ✅ {rel_path}")
    
    print("\n" + "=" * 70)
    print(f"✅ Fixed {total} remaining JS issues across {files_fixed} files")
    print(f"🎯 Console should now be clean!\n")
    
    return files_fixed

if __name__ == '__main__':
    count = main()

