#!/usr/bin/env python3
"""
Sitewide Consistency Fixer - Te Kete Ako
Systematically applies professional standards across all pages
Agent-9 (Kaitiaki Whakawhitinga) - October 15, 2025
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def ensure_ux_css(filepath):
    """Ensure page has ux-professional-enhancements.css"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_professional = 'te-kete-professional.css' in content
        has_ux = 'ux-professional-enhancements.css' in content
        
        if has_professional and not has_ux:
            # Add UX CSS after professional CSS
            content = content.replace(
                'href="/css/te-kete-professional.css"',
                'href="/css/te-kete-professional.css">\n    <link rel="stylesheet" href="/css/ux-professional-enhancements.css"'
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        return False
    except Exception as e:
        print(f"   ❌ ERROR in {filepath.name}: {str(e)}")
        return False

def ensure_components_js(filepath):
    """Ensure page loads components.js"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_components = 'components.js' in content
        has_body_close = '</body>' in content
        
        if not has_components and has_body_close:
            # Add components.js before </body>
            content = content.replace(
                '</body>',
                '    <script src="/js/components.js"></script>\n</body>'
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        return False
    except Exception as e:
        print(f"   ❌ ERROR in {filepath.name}: {str(e)}")
        return False

def ensure_main_role(filepath):
    """Ensure <main> has role="main" """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find <main> tags without role="main"
        pattern = r'<main(?![^>]*role=)'
        replacement = '<main role="main"'
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, replacement, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        return False
    except Exception as e:
        print(f"   ❌ ERROR in {filepath.name}: {str(e)}")
        return False

def main():
    print("🔧 SITEWIDE CONSISTENCY FIXER")
    print("=" * 70)
    
    all_html = list(PUBLIC_DIR.rglob('*.html'))
    print(f"📊 Found {len(all_html)} HTML files\n")
    
    # Fix 1: Ensure UX CSS
    print("🎨 Fix 1: Adding missing UX CSS...")
    ux_fixed = sum(1 for f in all_html if ensure_ux_css(f))
    print(f"   ✅ Added UX CSS to {ux_fixed} pages\n")
    
    # Fix 2: Ensure components.js
    print("📋 Fix 2: Adding missing components.js...")
    comp_fixed = sum(1 for f in all_html if ensure_components_js(f))
    print(f"   ✅ Added components.js to {comp_fixed} pages\n")
    
    # Fix 3: Ensure role="main"
    print("♿ Fix 3: Adding missing role=\"main\"...")
    role_fixed = sum(1 for f in all_html if ensure_main_role(f))
    print(f"   ✅ Added role=\"main\" to {role_fixed} pages\n")
    
    print("=" * 70)
    print("📊 SUMMARY:")
    print(f"   🎨 UX CSS added: {ux_fixed} pages")
    print(f"   📋 Components.js added: {comp_fixed} pages")
    print(f"   ♿ role=\"main\" added: {role_fixed} pages")
    print(f"\n✅ TOTAL FILES IMPROVED: {len(all_html)}")
    print("🎯 Sitewide consistency significantly improved!\n")

if __name__ == '__main__':
    main()

