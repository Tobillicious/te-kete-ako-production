#!/usr/bin/env python3
"""
Complete Sidebar Deployment - Add to ALL remaining HTML pages
Ensures 100% coverage across platform
"""

import os
import glob

# Sidebar script tag to add
SIDEBAR_SCRIPT = '<script src="/js/sidebar-auto-loader.js" defer></script>\n'

def has_sidebar(content):
    """Check if page already has sidebar"""
    return 'sidebar-auto-loader.js' in content

def add_sidebar(file_path):
    """Add sidebar to a single file if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has sidebar
        if has_sidebar(content):
            return False, "has_sidebar"
        
        # Skip if no </head> tag
        if '</head>' not in content:
            return False, "no_head"
        
        # Add sidebar script before </head>
        updated = content.replace('</head>', f'{SIDEBAR_SCRIPT}</head>', 1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        
        return True, "added"
        
    except Exception as e:
        return False, f"error: {e}"

def main():
    print("🚀 COMPLETING SIDEBAR DEPLOYMENT TO ALL PAGES...")
    print()
    
    # Find ALL HTML files in public/
    all_html = glob.glob('public/**/*.html', recursive=True)
    
    print(f"📊 Found {len(all_html)} total HTML pages")
    print()
    
    stats = {
        'added': 0,
        'has_sidebar': 0,
        'no_head': 0,
        'error': 0
    }
    
    for html_path in all_html:
        success, status = add_sidebar(html_path)
        
        if success:
            stats['added'] += 1
            print(f"  ✅ Added: {os.path.basename(html_path)}")
        elif 'has_sidebar' in status:
            stats['has_sidebar'] += 1
        elif 'no_head' in status:
            stats['no_head'] += 1
        else:
            stats['error'] += 1
            print(f"  ❌ Error: {os.path.basename(html_path)}")
    
    print()
    print(f"🎊 DEPLOYMENT COMPLETE!")
    print(f"  ✅ Added sidebar: {stats['added']} pages")
    print(f"  ⏭️  Already had: {stats['has_sidebar']} pages")
    print(f"  ⚠️  No <head> tag: {stats['no_head']} pages")
    print(f"  ❌ Errors: {stats['error']} pages")
    print(f"  📊 Total: {len(all_html)} pages")
    print()
    
    coverage = ((stats['has_sidebar'] + stats['added']) / len(all_html)) * 100
    print(f"🎯 SIDEBAR COVERAGE: {coverage:.1f}%")
    print()
    print("🌿 Professional sidebar now on (almost) every page!")

if __name__ == "__main__":
    main()

