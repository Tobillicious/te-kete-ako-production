#!/usr/bin/env python3
"""
Link Validator - Check all HTML files for broken links
Based on clean version patterns, not AI-generated complexity
"""
import os
import re
from pathlib import Path

def find_html_files(root_dir='.'):
    """Find all HTML files, excluding backups and node_modules"""
    html_files = []
    exclude_dirs = {'node_modules', 'backup', '.git', 'te-kete-TEACHING-CONTENT-BACKUP'}
    
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    return html_files

def extract_links(html_file):
    """Extract all href links from HTML file"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all href attributes
        links = re.findall(r'href=["\']([^"\']+)["\']', content)
        
        # Filter to local HTML links only (no http://, no #anchors, no mailto:)
        local_links = [
            link for link in links 
            if link.endswith('.html') and not link.startswith(('http:', 'https:', '#', 'mailto:'))
        ]
        
        return local_links
    except Exception as e:
        print(f"⚠️  Error reading {html_file}: {e}")
        return []

def check_link_exists(source_file, link):
    """Check if a link resolves to an existing file"""
    # Get directory of source file
    source_dir = os.path.dirname(source_file)
    
    # Resolve relative path
    if link.startswith('/'):
        # Absolute path from root
        target_path = link[1:]  # Remove leading /
    else:
        # Relative path
        target_path = os.path.join(source_dir, link)
    
    # Normalize path
    target_path = os.path.normpath(target_path)
    
    return os.path.exists(target_path), target_path

def main():
    print("🔍 Te Kete Ako Link Validator")
    print("=" * 70)
    print()
    
    # Find all HTML files
    html_files = find_html_files()
    print(f"📄 Found {len(html_files)} HTML files")
    print()
    
    # Track stats
    total_links = 0
    broken_links = []
    files_with_broken_links = set()
    
    # Check each file
    for html_file in sorted(html_files):
        links = extract_links(html_file)
        total_links += len(links)
        
        file_broken_links = []
        for link in links:
            exists, resolved_path = check_link_exists(html_file, link)
            if not exists:
                file_broken_links.append((link, resolved_path))
                broken_links.append((html_file, link, resolved_path))
        
        if file_broken_links:
            files_with_broken_links.add(html_file)
    
    # Report results
    print(f"📊 RESULTS:")
    print(f"   Total links checked: {total_links}")
    print(f"   Broken links: {len(broken_links)}")
    print(f"   Files with broken links: {len(files_with_broken_links)}")
    print()
    
    if broken_links:
        print("❌ BROKEN LINKS:")
        print()
        
        # Group by source file
        current_file = None
        for source_file, link, resolved_path in sorted(broken_links):
            if source_file != current_file:
                print(f"\n📄 {source_file}")
                current_file = source_file
            print(f"   ❌ {link}")
            print(f"      → Resolved to: {resolved_path}")
        
        print()
        print(f"💡 TIP: Fix these links or remove them to improve site quality")
    else:
        print("✅ NO BROKEN LINKS FOUND!")
        print("   All internal HTML links are valid.")
    
    print()
    print("=" * 70)
    
    # Exit code: 0 if no broken links, 1 if broken links found
    return 1 if broken_links else 0

if __name__ == "__main__":
    exit(main())

