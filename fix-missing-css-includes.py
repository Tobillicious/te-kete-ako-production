#!/usr/bin/env python3
"""
Fix missing CSS includes in HTML files.

This script finds HTML files missing the main CSS includes and adds them
while preserving existing meta tags and other head content.
"""

import os
import re
from pathlib import Path

# Standard CSS includes that should be in every HTML file
STANDARD_CSS_INCLUDES = '''<!-- CSS - UNIFIED PROFESSIONAL DESIGN SYSTEM (CONSOLIDATED) -->
<!-- ⭐ PROFESSIONAL SYSTEM FIRST - Core design tokens -->
<link rel="stylesheet" href="/css/professionalization-system.css">

<!-- ⭐ THEME SYSTEM (Tailwind + Ultimate Beauty) -->
<link rel="stylesheet" href="/css/te-kete-professional.css"/>
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css"/>

<!-- ⭐ COMPONENT STYLES -->
    <link rel="stylesheet" href="/css/main.css">
    <link rel="stylesheet" href="/css/navigation-standard.css">
    <link rel="stylesheet" href="/css/mobile-revolution.css">
    <link rel="stylesheet" href="/css/mobile-first-classroom-tablets.css"/>

<!-- ⭐ PRINT STYLES (media="print" = only for printing) -->
    <link rel="stylesheet" href="/css/print.css" media="print"/>
<link rel="stylesheet" href="/css/print-professional.css" media="print"/>

<!-- ⭐ TAILWIND (Loads second-to-last - utilities only, NO DUPLICATES) -->
<link rel="stylesheet" href="/css/tailwind.css">

<!-- ⭐ CASCADE FIX (Loads LAST - overrides conflicting variables) -->
<link rel="stylesheet" href="/css/cascade-fix.css">'''

# Standard meta tags that should be in every HTML file
STANDARD_META = '''<!-- UNIFIED DESIGN SYSTEM -->
<!-- PWA Manifest -->
<link href="/manifest.json" rel="manifest"/>
<meta content="#1a4d2e" name="theme-color"/>'''

def find_html_files_missing_css():
    """Find HTML files missing the main CSS include."""
    public_dir = Path('/Users/admin/Documents/te-kete-ako-clean/public')
    missing_files = []

    for html_file in public_dir.rglob('*.html'):
        # Skip component files and certain directories
        if any(part in html_file.parts for part in ['components', 'archive', 'min']):
            continue

        # Check if file contains the main CSS include
        try:
            content = html_file.read_text()
            if 'professionalization-system.css' not in content:
                missing_files.append(html_file)
        except Exception as e:
            print(f"Error reading {html_file}: {e}")
            continue

    return missing_files

def extract_existing_meta(html_content):
    """Extract existing meta tags, title, and other head content."""
    # Find the head section
    head_match = re.search(r'<head>(.*?)</head>', html_content, re.DOTALL | re.IGNORECASE)
    if not head_match:
        return ""

    head_content = head_match.group(1)

    # Extract important elements
    title_match = re.search(r'<title[^>]*>(.*?)</title>', head_content, re.DOTALL | re.IGNORECASE)
    meta_tags = re.findall(r'<meta[^>]*>', head_content, re.IGNORECASE)
    other_links = re.findall(r'<link[^>]*>', head_content, re.IGNORECASE)

    # Filter out CSS links (we'll replace them)
    css_links = [link for link in other_links if 'stylesheet' in link.lower()]

    # Keep non-CSS links and meta tags
    preserved_content = []
    if title_match:
        preserved_content.append(f"    {title_match.group(0)}")
    for meta in meta_tags:
        preserved_content.append(f"    {meta}")
    for link in other_links:
        if 'stylesheet' not in link.lower():
            preserved_content.append(f"    {link}")

    return '\n'.join(preserved_content)

def fix_html_file(file_path):
    """Fix a single HTML file by adding proper CSS includes."""
    try:
        content = file_path.read_text()

        # Extract existing head content
        existing_meta = extract_existing_meta(content)

        # Create new head section
        new_head = f'''<head>
{existing_meta}

{STANDARD_META}

{STANDARD_CSS_INCLUDES}'''

        # Replace the old head with new head
        old_head_pattern = r'<head>.*?</head>'
        new_content = re.sub(old_head_pattern, new_head, content, flags=re.DOTALL | re.IGNORECASE)

        # Write back to file
        file_path.write_text(new_content)
        return True

    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Main function to fix all missing CSS includes."""
    print("🔍 Finding HTML files missing CSS includes...")

    missing_files = find_html_files_missing_css()
    print(f"📄 Found {len(missing_files)} files missing CSS includes")

    if not missing_files:
        print("✅ All HTML files have proper CSS includes!")
        return

    print("🔧 Starting fixes...")
    fixed_count = 0

    for i, file_path in enumerate(missing_files, 1):
        print(f"  [{i}/{len(missing_files)}] Fixing: {file_path.name}")
        if fix_html_file(file_path):
            fixed_count += 1

    print(f"\n✅ Fixed {fixed_count} files successfully!")
    print(f"❌ Failed to fix {len(missing_files) - fixed_count} files")

if __name__ == "__main__":
    main()
