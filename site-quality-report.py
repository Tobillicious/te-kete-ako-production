#!/usr/bin/env python3
"""
Site Quality Assessment - Header, Navigation, CSS Consistency
"""

import os
import re
from pathlib import Path

print("🔍 TE KETE AKO - SITE QUALITY ASSESSMENT")
print("=" * 80)

public_dir = Path("public")
html_files = list(public_dir.glob("*.html"))

# Track issues
issues = {
    "missing_navigation": [],
    "missing_professional_css": [],
    "missing_doctype": [],
    "inconsistent_title": [],
    "large_files": []
}

stats = {
    "total_pages": 0,
    "with_navigation": 0,
    "with_professional_css": 0,
    "with_doctype": 0,
    "proper_structure": 0
}

print(f"\n📊 Scanning {len(html_files)} top-level HTML pages...\n")

for html_file in html_files:
    stats["total_pages"] += 1
    
    try:
        content = html_file.read_text(encoding='utf-8')
        file_size = len(content)
        
        # Check for navigation
        has_nav = 'navigation-standard.html' in content
        if has_nav:
            stats["with_navigation"] += 1
        else:
            issues["missing_navigation"].append(html_file.name)
        
        # Check for professional CSS
        has_pro_css = 'te-kete-professional.css' in content
        if has_pro_css:
            stats["with_professional_css"] += 1
        else:
            issues["missing_professional_css"].append(html_file.name)
        
        # Check for DOCTYPE
        has_doctype = content.strip().upper().startswith('<!DOCTYPE')
        if has_doctype:
            stats["with_doctype"] += 1
        else:
            issues["missing_doctype"].append(html_file.name)
        
        # Check for proper title
        title_match = re.search(r'<title>(.+?)</title>', content, re.IGNORECASE)
        if not title_match or 'Te Kete Ako' not in title_match.group(1):
            issues["inconsistent_title"].append(html_file.name)
        
        # Check file size (>2000 lines is concerning)
        if file_size > 150000:  # ~2000 lines
            issues["large_files"].append((html_file.name, len(content.split('\n'))))
        
        # Overall structure check
        if has_nav and has_pro_css and has_doctype:
            stats["proper_structure"] += 1
            
    except Exception as e:
        print(f"⚠️  Error reading {html_file.name}: {e}")

# REPORT
print("\n" + "=" * 80)
print("📊 QUALITY STATISTICS")
print("=" * 80)
print(f"Total Pages Scanned:        {stats['total_pages']}")
print(f"With Navigation Header:     {stats['with_navigation']} ({stats['with_navigation']/stats['total_pages']*100:.1f}%)")
print(f"With Professional CSS:      {stats['with_professional_css']} ({stats['with_professional_css']/stats['total_pages']*100:.1f}%)")
print(f"With Proper DOCTYPE:        {stats['with_doctype']} ({stats['with_doctype']/stats['total_pages']*100:.1f}%)")
print(f"Fully Professional:         {stats['proper_structure']} ({stats['proper_structure']/stats['total_pages']*100:.1f}%)")

print("\n" + "=" * 80)
print("🚨 ISSUES FOUND")
print("=" * 80)

if issues["missing_navigation"]:
    print(f"\n❌ Missing Navigation Header ({len(issues['missing_navigation'])} pages):")
    for page in issues["missing_navigation"][:10]:
        print(f"   - {page}")
    if len(issues["missing_navigation"]) > 10:
        print(f"   ... and {len(issues['missing_navigation']) - 10} more")

if issues["missing_professional_css"]:
    print(f"\n❌ Missing Professional CSS ({len(issues['missing_professional_css'])} pages):")
    for page in issues["missing_professional_css"][:10]:
        print(f"   - {page}")
    if len(issues["missing_professional_css"]) > 10:
        print(f"   ... and {len(issues['missing_professional_css']) - 10} more")

if issues["missing_doctype"]:
    print(f"\n❌ Missing DOCTYPE ({len(issues['missing_doctype'])} pages):")
    for page in issues["missing_doctype"][:5]:
        print(f"   - {page}")

if issues["large_files"]:
    print(f"\n⚠️  Large Files (>2000 lines, may need optimization):")
    for page, lines in sorted(issues["large_files"], key=lambda x: x[1], reverse=True)[:5]:
        print(f"   - {page}: {lines} lines")

if issues["inconsistent_title"]:
    print(f"\n⚠️  Inconsistent Titles ({len(issues['inconsistent_title'])} pages):")
    for page in issues["inconsistent_title"][:5]:
        print(f"   - {page}")

print("\n" + "=" * 80)
print("✅ RECOMMENDATIONS")
print("=" * 80)

if stats["proper_structure"] < stats["total_pages"]:
    print(f"\n1. Standardize {stats['total_pages'] - stats['proper_structure']} pages to use:")
    print("   - navigation-standard.html (consistent header)")
    print("   - te-kete-professional.css (unified styling)")
    print("   - Proper DOCTYPE and structure")

if issues["large_files"]:
    print(f"\n2. Optimize {len(issues['large_files'])} large files:")
    print("   - Extract repeated content to components")
    print("   - Minimize inline styles/scripts")
    print("   - Consider code splitting")

print("\n" + "=" * 80)
overall_health = (stats["proper_structure"] / stats["total_pages"]) * 100
print(f"🎯 OVERALL SITE HEALTH: {overall_health:.1f}%")
if overall_health >= 90:
    print("   Status: ✅ EXCELLENT - Professional quality!")
elif overall_health >= 75:
    print("   Status: 🟡 GOOD - Minor improvements needed")
else:
    print("   Status: 🔴 NEEDS WORK - Standardization required")
print("=" * 80)

