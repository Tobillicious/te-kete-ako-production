#!/usr/bin/env python3
"""
Fix malformed HTML in orphaned generated-resources-alpha pages
and integrate them into the main site.
"""

import os
import re
from pathlib import Path

# Paths
LESSONS_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public/generated-resources-alpha/lessons")
HANDOUTS_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public/generated-resources-alpha/handouts")

def fix_html_line1(file_path):
    """Fix line 1 if it has markdown mixed with HTML"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern: <!DOCTYPE html>### **Year Level:** X-Y | **Subject:** Zzz<html lang="en"><head>
    # Should be: <!DOCTYPE html>\n<html lang="en">\n<head>
    # And add metadata comment with year/subject info
    
    pattern = r'<!DOCTYPE html>### \*\*Year Level:\*\* ([\d-]+) \| \*\*Subject:\*\* ([^<]+)<html lang="en"><head>'
    
    match = re.search(pattern, content)
    if match:
        year_level = match.group(1)
        subject = match.group(2)
        
        # Replace with proper HTML
        fixed_content = re.sub(
            pattern,
            f'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <!-- Year Level: {year_level} | Subject: {subject} -->',
            content
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"✅ Fixed: {file_path.name} (Year {year_level}, {subject})")
        return True
    
    return False

def main():
    """Fix all orphaned pages"""
    fixed_count = 0
    
    # Fix lessons
    print("\n🔧 Fixing lessons...")
    for html_file in LESSONS_DIR.glob("*.html"):
        if html_file.name != "index.html":
            if fix_html_line1(html_file):
                fixed_count += 1
    
    # Fix handouts
    print("\n🔧 Fixing handouts...")
    for html_file in HANDOUTS_DIR.glob("*.html"):
        if html_file.name != "index.html":
            if fix_html_line1(html_file):
                fixed_count += 1
    
    print(f"\n✅ Total files fixed: {fixed_count}")

if __name__ == "__main__":
    main()

