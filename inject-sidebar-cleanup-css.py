#!/usr/bin/env python3
"""
INJECT SIDEBAR CLEANUP CSS
Adds sidebar-navigation-cleanup.css to all pages that have sidebar-auto-loader.js
Created: Oct 26, 2025
"""

import os
import re
from pathlib import Path

def has_sidebar_loader(html_content):
    """Check if page has sidebar-auto-loader.js"""
    return 'sidebar-auto-loader.js' in html_content

def has_cleanup_css(html_content):
    """Check if page already has sidebar-navigation-cleanup.css"""
    return 'sidebar-navigation-cleanup.css' in html_content

def inject_cleanup_css(html_content, filepath):
    """Add sidebar-navigation-cleanup.css link"""
    
    # Find </head> tag
    head_close_match = re.search(r'</head>', html_content, re.IGNORECASE)
    if not head_close_match:
        return html_content, False
    
    # Prepare injection
    injection = '''    <!-- Sidebar Navigation Cleanup -->
    <link rel="stylesheet" href="/css/sidebar-navigation-cleanup.css">
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
    
    # Filter to pages with sidebar loader
    pages_with_sidebar = []
    for filepath in all_html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if has_sidebar_loader(content) and not has_cleanup_css(content):
                pages_with_sidebar.append(filepath)
        except Exception as e:
            pass
    
    print(f"📁 Found {len(pages_with_sidebar)} pages with sidebar (missing cleanup CSS)")
    
    # Inject cleanup CSS
    injected_count = 0
    
    for filepath in pages_with_sidebar:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified_content, was_injected = inject_cleanup_css(content, filepath)
            
            if was_injected:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                injected_count += 1
                
        except Exception as e:
            print(f"  ❌ Error processing {filepath}: {e}")
    
    print(f"\n{'='*60}")
    print(f"🎯 SIDEBAR CLEANUP CSS INJECTION COMPLETE!")
    print(f"{'='*60}")
    print(f"✅ Injected cleanup CSS: {injected_count} pages")
    print(f"\n🚀 Old navigation will now hide when sidebar is active!")
    print(f"🌿 Kia kaha!")

if __name__ == '__main__':
    main()

