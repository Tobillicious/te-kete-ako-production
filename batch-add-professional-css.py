#!/usr/bin/env python3
"""
Batch Add Professional CSS
Apply te-kete-professional.css consistently across all pages
"""

import os
import re
from pathlib import Path

# Professional CSS to add
PROFESSIONAL_CSS = """
    <link rel="stylesheet" href="/css/te-kete-professional.css">
    <link rel="stylesheet" href="/css/te-kete-responsive.css">
    <link rel="stylesheet" href="/css/te-kete-accessibility.css">
"""

# JavaScript enhancements
PROFESSIONAL_JS = """
    <script src="/js/te-kete-intelligence.js"></script>
    <script src="/js/te-kete-navigation.js"></script>
    <script src="/js/te-kete-accessibility.js"></script>
"""

def add_professional_css(file_path):
    """Add professional CSS to a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has professional CSS
        if 'te-kete-professional.css' in content:
            print(f"  ✅ {file_path} - Already has professional CSS")
            return True
        
        # Find head tag
        head_match = re.search(r'<head[^>]*>', content, re.IGNORECASE)
        if not head_match:
            print(f"  ⚠️  {file_path} - No head tag found")
            return False
        
        # Insert professional CSS after head tag
        head_end = head_match.end()
        new_content = content[:head_end] + PROFESSIONAL_CSS + content[head_end:]
        
        # Find body tag for JavaScript
        body_match = re.search(r'</body>', new_content, re.IGNORECASE)
        if body_match:
            body_start = body_match.start()
            new_content = new_content[:body_start] + PROFESSIONAL_JS + new_content[body_start:]
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ {file_path} - Professional CSS added")
        return True
        
    except Exception as e:
        print(f"  ❌ {file_path} - Error: {e}")
        return False

def process_directory(directory):
    """Process all HTML files in directory"""
    html_files = list(Path(directory).rglob("*.html"))
    
    print(f"📁 Processing {len(html_files)} HTML files in {directory}")
    
    success_count = 0
    for file_path in html_files:
        if add_professional_css(file_path):
            success_count += 1
    
    print(f"✅ Successfully processed {success_count}/{len(html_files)} files")
    return success_count

def main():
    print("🎨 PROFESSIONAL CSS BATCH APPLICATION")
    print("=" * 50)
    
    # Process public directory
    public_dir = "/Users/admin/Documents/te-kete-ako-clean/public"
    if os.path.exists(public_dir):
        process_directory(public_dir)
    
    # Process other HTML files
    root_dir = "/Users/admin/Documents/te-kete-ako-clean"
    if os.path.exists(root_dir):
        process_directory(root_dir)
    
    print("\n🎉 Professional CSS application complete!")
    print("📋 Next steps:")
    print("  1. Test pages in browser")
    print("  2. Verify CSS is loading correctly")
    print("  3. Check responsive design")
    print("  4. Validate accessibility")

if __name__ == "__main__":
    main()