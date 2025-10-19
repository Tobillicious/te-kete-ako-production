#!/usr/bin/env python3
"""
📝 DEPLOY WAGOLL CONSISTENCY SITEWIDE
Replace WILF with WAGOLL across all lesson pages
October 19, 2025 - Professional Standards Update
"""

import re
from pathlib import Path

print("📝 DEPLOYING WAGOLL CONSISTENCY SITEWIDE")
print("=" * 70)

# Find all HTML files in public/
public_dir = Path('public')
html_files = list(public_dir.rglob('*.html'))

print(f"\n📊 Found {len(html_files)} HTML files in public/")

# Track progress
files_transformed = 0
files_skipped = 0
files_error = 0

# REPLACEMENT PATTERNS
REPLACEMENTS = [
    # Primary pattern with bilingual label
    (
        r'Success Criteria \(WILF - What I\'m Looking For\) \| Ngā Paearu:',
        'Success Criteria (WAGOLL - What a Good One Looks Like) | Ngā Paearu:'
    ),
    # English-only pattern
    (
        r'Success Criteria \(WILF - What I\'m Looking For\):',
        'Success Criteria (WAGOLL - What a Good One Looks Like):'
    ),
    # Just WILF in parentheses
    (
        r'\(WILF - What I\'m Looking For\)',
        '(WAGOLL - What a Good One Looks Like)'
    ),
    # Standalone WILF heading
    (
        r'WILF - What I\'m Looking For',
        'WAGOLL - What a Good One Looks Like'
    ),
]

def transform_file(filepath):
    """Transform a single file to use WAGOLL"""
    global files_transformed, files_skipped, files_error
    
    try:
        content = filepath.read_text(encoding='utf-8')
        original_content = content
        
        # Skip if no WILF found
        if 'WILF' not in content:
            files_skipped += 1
            return False
        
        # Skip component files, templates, and backup files
        skip_patterns = ['/components/', '.bak', '.master-backup', 'template']
        if any(pattern in str(filepath) for pattern in skip_patterns):
            files_skipped += 1
            return False
        
        # Apply all replacements
        replacements_made = 0
        for old_pattern, new_text in REPLACEMENTS:
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_text, content)
                replacements_made += 1
        
        # Only write if content changed
        if content != original_content:
            filepath.write_text(content, encoding='utf-8')
            files_transformed += 1
            return True
        else:
            files_skipped += 1
            return False
            
    except Exception as e:
        print(f"   ⚠️  Error: {filepath.name} - {e}")
        files_error += 1
        return False

# PRIORITY ORDER - Focus on lesson pages first
PRIORITY_PATHS = [
    # Perfect Learning Chains first
    'units/y8-digital-kaitiakitanga/lessons/',
    'units/y7-maths-algebra/lessons/',
    'units/y9-science-ecology/',
    # Other unit lessons
    'units/lessons/',
    'guided-inquiry-unit/lessons/',
    # Standalone lessons
    'lessons/',
    # Handouts and resources
    'handouts/',
    'units/y8-digital-kaitiakitanga/handouts/',
    'units/y9-science-ecology/resources/',
    'units/y7-maths-algebra/resources/',
]

# Process files in priority order
print("\n🚀 TRANSFORMING FILES IN PRIORITY ORDER:\n")

for priority_path in PRIORITY_PATHS:
    matching_files = [f for f in html_files if priority_path in str(f)]
    
    if not matching_files:
        continue
    
    print(f"\n📁 Processing: {priority_path} ({len(matching_files)} files)")
    
    transformed_in_group = 0
    for filepath in matching_files:
        if transform_file(filepath):
            transformed_in_group += 1
    
    if transformed_in_group > 0:
        print(f"   ✅ Transformed {transformed_in_group} files in {priority_path}")
    else:
        print(f"   ⏭️  No WILF found in {priority_path}")

# Process remaining files
print("\n📁 Processing remaining files...")
remaining_transformed = 0
for filepath in html_files:
    # Skip if already processed in priority paths
    if any(p in str(filepath) for p in PRIORITY_PATHS):
        continue
    if transform_file(filepath):
        remaining_transformed += 1

if remaining_transformed > 0:
    print(f"   ✅ Transformed {remaining_transformed} additional files")

print("\n" + "=" * 70)
print("✅ WAGOLL CONSISTENCY DEPLOYMENT COMPLETE")
print("=" * 70)
print(f"\n✅ Files transformed: {files_transformed}")
print(f"⏭️  Files skipped: {files_skipped}")
print(f"⚠️  Errors: {files_error}")
print(f"\n📝 Total pages with WAGOLL standard: {files_transformed}")
print(f"\n💎 Professional teaching standards consistent sitewide!")
print("\n🌿 Whaowhia te kete mātauranga! 🌿")


