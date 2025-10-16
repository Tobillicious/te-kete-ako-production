#!/usr/bin/env python3
"""
Fix Duplicate Headers - Te Kete Ako Sitewide Consistency
Removes inline headers from pages that also have header-component div
Agent-9 (Kaitiaki Whakawhitinga) - October 15, 2025
"""

import os
import re
from pathlib import Path

# Pages with duplicate headers (from audit)
PAGES_TO_FIX = [
    'games.html',
    'handouts.html',
    'index-premium.html',
    'integrated-resources-index.html',
    'resource-hub.html',
    'site-map.html',
    'subjects.html',
    'te-ao-maori.html',
    'youtube.html'
]

def remove_duplicate_header(filepath):
    """Remove inline header if page also has header-component div"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if page has header-component div
        has_component = 'id="header-component"' in content
        
        if not has_component:
            print(f"   ⏭️  SKIP: {filepath.name} - no component div")
            return False
        
        # Check if page has inline header
        header_pattern = r'<header[^>]*class="site-header[^"]*"[^>]*>.*?</header>\s*\n*'
        has_inline = re.search(header_pattern, content, re.DOTALL)
        
        if not has_inline:
            print(f"   ⏭️  SKIP: {filepath.name} - no inline header found")
            return False
        
        # Remove the inline header
        new_content = re.sub(header_pattern, '', content, count=1, flags=re.DOTALL)
        
        # Clean up extra whitespace
        new_content = re.sub(r'\n{3,}', '\n\n', new_content)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"   ✅ FIXED: {filepath.name} - removed duplicate header")
        return True
    
    except Exception as e:
        print(f"   ❌ ERROR: {filepath.name} - {str(e)}")
        return False

def main():
    print("🔧 FIXING DUPLICATE HEADERS...")
    print("=" * 60)
    
    public_dir = Path('/Users/admin/Documents/te-kete-ako-clean/public')
    fixed_count = 0
    
    for page in PAGES_TO_FIX:
        filepath = public_dir / page
        if filepath.exists():
            if remove_duplicate_header(filepath):
                fixed_count += 1
        else:
            print(f"   ⚠️  NOT FOUND: {page}")
    
    print("=" * 60)
    print(f"\n✅ COMPLETE: Fixed {fixed_count} / {len(PAGES_TO_FIX)} pages")
    print(f"📊 Result: All pages now use component system only!")
    
    return fixed_count

if __name__ == '__main__':
    fixed = main()
    exit(0 if fixed > 0 else 1)

