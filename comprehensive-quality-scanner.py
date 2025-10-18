#!/usr/bin/env python3
"""
Comprehensive Quality Scanner - ALL Educational Content
Scan all 6,192+ HTML files systematically
"""

from pathlib import Path
import re
from collections import defaultdict

print("🔍 COMPREHENSIVE QUALITY SCANNER - All Educational Content")
print("=" * 70)

# Track everything
stats = {
    'total_scanned': 0,
    'has_meta_description': 0,
    'missing_meta': 0,
    'has_placeholders': 0,
    'has_todo': 0,
    'has_whakatauaki': 0,
    'has_navigation': 0,
    'empty_files': 0,
    'broken_structure': 0
}

issues_by_type = defaultdict(list)
quality_scores = []

# Scan all educational HTML files
print("\n📊 Scanning lessons, handouts, units, games, assessments...")
print("(This will take a few minutes for 6,000+ files)\n")

scan_patterns = [
    '**/lessons/**/*.html',
    '**/handouts/**/*.html',
    '**/units/**/*.html',
    '**/games/**/*.html',
    '**/assessment*/**/*.html'
]

all_files = []
for pattern in scan_patterns:
    all_files.extend(Path('.').glob(pattern))

# Remove duplicates
all_files = list(set(all_files))

print(f"Found {len(all_files)} educational HTML files to scan\n")

# Scan each file
for i, html_file in enumerate(all_files, 1):
    try:
        stats['total_scanned'] += 1
        content = html_file.read_text(encoding='utf-8')
        
        # Check meta description
        if 'meta name="description"' in content:
            stats['has_meta_description'] += 1
        else:
            stats['missing_meta'] += 1
            if stats['missing_meta'] <= 20:  # Track first 20
                issues_by_type['missing_meta'].append(str(html_file))
        
        # Check for placeholders
        if re.search(r'coming soon|\[INSERT\]|placeholder|TODO|FIXME', content, re.IGNORECASE):
            stats['has_placeholders'] += 1
            if stats['has_placeholders'] <= 20:
                issues_by_type['has_placeholders'].append(str(html_file))
        
        # Check for cultural integration
        if re.search(r'whakataukī|whakatauki', content, re.IGNORECASE):
            stats['has_whakatauaki'] += 1
        
        # Check for navigation
        if 'navigation' in content.lower():
            stats['has_navigation'] += 1
        
        # Check if empty
        if len(content.strip()) < 100:
            stats['empty_files'] += 1
        
        # Progress indicator
        if i % 500 == 0:
            print(f"   Scanned {i}/{len(all_files)} files...")
    
    except Exception as e:
        stats['broken_structure'] += 1

# Results
print("\n" + "=" * 70)
print("📊 COMPREHENSIVE QUALITY SCAN RESULTS")
print("=" * 70)

print(f"\n✅ Total files scanned: {stats['total_scanned']}")

print(f"\n📝 Meta Descriptions:")
print(f"   ✅ Has meta: {stats['has_meta_description']} ({stats['has_meta_description']/stats['total_scanned']*100:.1f}%)")
print(f"   ❌ Missing meta: {stats['missing_meta']} ({stats['missing_meta']/stats['total_scanned']*100:.1f}%)")

print(f"\n🔧 Content Issues:")
print(f"   ⚠️  Has placeholders/TODO: {stats['has_placeholders']} ({stats['has_placeholders']/stats['total_scanned']*100:.1f}%)")
print(f"   ⚠️  Empty/broken files: {stats['empty_files']}")

print(f"\n🌿 Cultural Integration:")
print(f"   ✅ Has Whakataukī: {stats['has_whakatauaki']} ({stats['has_whakatauaki']/stats['total_scanned']*100:.1f}%)")

print(f"\n🧭 Navigation:")
print(f"   ✅ Has navigation: {stats['has_navigation']} ({stats['has_navigation']/stats['total_scanned']*100:.1f}%)")

# Priority fixes
print(f"\n" + "=" * 70)
print("🎯 PRIORITY WORK NEEDED")
print("=" * 70)

print(f"\n1. Add meta descriptions: {stats['missing_meta']} files")
print(f"2. Fix placeholders: {stats['has_placeholders']} files")
print(f"3. Enhance cultural integration: {stats['total_scanned'] - stats['has_whakatauaki']} files")
print(f"4. Add navigation: {stats['total_scanned'] - stats['has_navigation']} files")

# Sample issues
if issues_by_type['missing_meta']:
    print(f"\n📋 Sample files missing meta (first 5):")
    for file in issues_by_type['missing_meta'][:5]:
        print(f"   - {file}")

if issues_by_type['has_placeholders']:
    print(f"\n📋 Sample files with placeholders (first 5):")
    for file in issues_by_type['has_placeholders'][:5]:
        print(f"   - {file}")

print(f"\n" + "=" * 70)
print("✨ Scan complete! Ready for systematic improvement.")
print("=" * 70)
