#!/usr/bin/env python3
"""
Fix Content Duplication in Integrated Lessons
October 20, 2025 - Responsive Build Agent

Issue: Some pages in /public/integrated-lessons/ have complete HTML documents
       nested inside content divs, causing duplication.

Solution: Parse HTML, extract inner lesson content, remove duplicate structure
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

print("🔧 CONTENT DUPLICATION FIX SCRIPT")
print("=" * 70)

# Find all HTML files in integrated-lessons
integrated_dir = Path('public/integrated-lessons')
if not integrated_dir.exists():
    print("❌ Directory not found: public/integrated-lessons/")
    print("   Run this script from the project root directory")
    exit(1)

html_files = list(integrated_dir.rglob('*.html'))
print(f"📊 Found {len(html_files)} HTML files in integrated-lessons/")

# Track results
files_fixed = 0
files_skipped = 0
files_error = 0
duplication_found = []

def has_nested_html(content):
    """Check if HTML has nested <!DOCTYPE or <html> tags"""
    # Count occurrences
    doctype_count = content.count('<!DOCTYPE')
    html_tag_count = content.count('<html')
    
    # If more than one, it's nested
    return doctype_count > 1 or html_tag_count > 1

def extract_inner_content(content):
    """Extract the lesson content from nested HTML structure"""
    try:
        # Use BeautifulSoup to parse
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find the main content div (usually has class "content" or similar)
        content_div = soup.find('div', class_='content')
        
        if content_div:
            # Check if there's a nested HTML document inside
            inner_html = content_div.find('html')
            
            if inner_html:
                # Extract just the body content from the nested HTML
                inner_body = inner_html.find('body')
                if inner_body:
                    return str(inner_body.decode_contents())
                return str(inner_html.decode_contents())
            
        return None
    except Exception as e:
        print(f"   ⚠️ Parse error: {e}")
        return None

def fix_page(filepath):
    """Fix a single page with content duplication"""
    global files_fixed, files_skipped, files_error
    
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Check if it has duplication
        if not has_nested_html(content):
            files_skipped += 1
            return False
        
        print(f"📄 Found duplication: {filepath.relative_to('public')}")
        duplication_found.append(str(filepath.relative_to('public')))
        
        # Try to extract inner content
        inner_content = extract_inner_content(content)
        
        if inner_content:
            # Replace the content div with extracted content
            soup = BeautifulSoup(content, 'html.parser')
            content_div = soup.find('div', class_='content')
            
            if content_div:
                content_div.clear()
                content_div.append(BeautifulSoup(inner_content, 'html.parser'))
                
                # Save fixed version
                fixed_content = str(soup.prettify())
                filepath.write_text(fixed_content, encoding='utf-8')
                
                print(f"   ✅ Fixed and saved")
                files_fixed += 1
                return True
        
        # If we couldn't extract, log for manual review
        print(f"   ⚠️ Needs manual review - structure unclear")
        files_error += 1
        return False
        
    except Exception as e:
        print(f"❌ Error processing {filepath.name}: {e}")
        files_error += 1
        return False

# Process all files
print(f"\n🔍 Scanning for content duplication...")
print("-" * 70)

for html_file in sorted(html_files):
    # Skip backup files
    if '.bak' in html_file.name or '.backup' in html_file.name:
        files_skipped += 1
        continue
    
    fix_page(html_file)

# Results
print("\n" + "=" * 70)
print("📊 RESULTS:")
print(f"   ✅ Fixed: {files_fixed} files")
print(f"   ⏭️  Skipped (no duplication): {files_skipped} files")
print(f"   ⚠️  Errors/Manual review needed: {files_error} files")
print(f"   📁 Total processed: {len(html_files)} files")

# Save report
if duplication_found:
    print(f"\n📝 Files with duplication found:")
    for file in duplication_found[:10]:  # Show first 10
        print(f"   - {file}")
    if len(duplication_found) > 10:
        print(f"   ... and {len(duplication_found) - 10} more")
    
    # Save full list
    report = {
        "date": "2025-10-20",
        "files_fixed": files_fixed,
        "files_with_duplication": duplication_found,
        "files_needing_review": files_error,
        "agent": "responsive-build-agent"
    }
    
    report_file = Path('content-duplication-fix-report.json')
    report_file.write_text(json.dumps(report, indent=2))
    print(f"\n✅ Full report saved to: {report_file}")

print("\n🎯 DONE!")
if files_fixed > 0:
    print(f"✨ Successfully fixed {files_fixed} pages with content duplication!")
elif files_skipped == len(html_files):
    print(f"✅ No duplication found - all {files_skipped} pages are clean!")
else:
    print(f"⚠️ {files_error} files need manual review")

print("\n" + "=" * 70)

