#!/usr/bin/env python3
"""
INJECT PROFESSIONAL SIDEBAR AUTO-LOADER
Adds sidebar-auto-loader.js to all authenticated pages (lessons, units, handouts, dashboards)
Created: Oct 26, 2025
"""

import os
import re
from pathlib import Path

def should_inject_sidebar(filepath):
    """Determine if this page should have the sidebar"""
    
    # Skip these pages (public/unauthenticated)
    skip_patterns = [
        '/login', '/register', '/signup', '/auth',
        '/index.html', '/pricing', '/about', '/contact',
        '/404', '/500', '/error'
    ]
    
    for pattern in skip_patterns:
        if pattern in str(filepath):
            return False
    
    # Include these authenticated pages
    include_patterns = [
        '/lessons/', '/units/', '/handouts/',
        '/teacher-dashboard', '/student-dashboard',
        '/my-', '/ai-', '/subscription-',
        '/-hub.html', '/admin/'
    ]
    
    for pattern in include_patterns:
        if pattern in str(filepath):
            return True
    
    return False

def inject_sidebar_loader(html_content, filepath):
    """Add sidebar auto-loader script if not already present"""
    
    # Skip if already has sidebar loader
    if 'sidebar-auto-loader.js' in html_content:
        return html_content, False
    
    # Find </head> tag
    head_close_match = re.search(r'</head>', html_content, re.IGNORECASE)
    if not head_close_match:
        print(f"  ⚠️  No </head> found: {filepath.name}")
        return html_content, False
    
    # Prepare injection
    injection = '''    <!-- Professional Sidebar Auto-Loader -->
    <script src="/js/sidebar-auto-loader.js" defer></script>
'''
    
    # Inject before </head>
    position = head_close_match.start()
    modified_html = (
        html_content[:position] +
        injection +
        html_content[position:]
    )
    
    return modified_html, True

def main():
    public_dir = Path('public')
    
    if not public_dir.exists():
        print("❌ public/ directory not found!")
        return
    
    # Find all HTML files
    all_html_files = list(public_dir.rglob('*.html'))
    print(f"📁 Found {len(all_html_files)} HTML files")
    
    # Filter to authenticated pages
    authenticated_pages = [f for f in all_html_files if should_inject_sidebar(f)]
    print(f"🔐 {len(authenticated_pages)} authenticated pages")
    
    # Inject sidebar loader
    injected_count = 0
    skipped_count = 0
    
    for filepath in authenticated_pages:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified_content, was_injected = inject_sidebar_loader(content, filepath)
            
            if was_injected:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                injected_count += 1
                print(f"  ✅ Injected: {filepath.relative_to(public_dir)}")
            else:
                skipped_count += 1
                
        except Exception as e:
            print(f"  ❌ Error processing {filepath}: {e}")
    
    print(f"\n{'='*60}")
    print(f"🎯 SIDEBAR INJECTION COMPLETE!")
    print(f"{'='*60}")
    print(f"✅ Injected into:  {injected_count} pages")
    print(f"⏭️  Already had it:  {skipped_count} pages")
    print(f"📊 Total processed: {len(authenticated_pages)} pages")
    print(f"\n🚀 Professional sidebar now loads on all authenticated pages!")
    print(f"🌿 Kia kaha!")

if __name__ == '__main__':
    main()

