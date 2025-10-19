#!/usr/bin/env python3
"""
🌿 DEPLOY KORU PATTERNS SITEWIDE
Add beautiful cultural background patterns to all pages
October 19, 2025 - Cultural Visual Enhancement
"""

import re
from pathlib import Path

print("🌿 DEPLOYING KORU PATTERNS SITEWIDE")
print("=" * 70)

# Find all HTML files in public/
public_dir = Path('public')
html_files = list(public_dir.rglob('*.html'))

print(f"\n📊 Found {len(html_files)} HTML files in public/")

# Track progress
files_updated = 0
files_skipped = 0
files_error = 0

def add_koru_pattern(filepath):
    """Add pattern-koru-subtle class to body if not present"""
    global files_updated, files_skipped, files_error
    
    try:
        content = filepath.read_text(encoding='utf-8')
        original_content = content
        
        # Skip if already has pattern-koru
        if 'pattern-koru' in content:
            files_skipped += 1
            return False
        
        # Skip component files
        if '/components/' in str(filepath):
            files_skipped += 1
            return False
        
        # Skip if no <body tag
        if '<body' not in content:
            files_skipped += 1
            return False
        
        # Add pattern-koru-subtle to body class
        if 'class="' in content and '<body' in content:
            # Add to existing class
            if re.search(r'<body[^>]*class="([^"]*)"', content):
                content = re.sub(
                    r'(<body[^>]*class=")([^"]*)"',
                    r'\1\2 pattern-koru-subtle"',
                    content,
                    count=1
                )
            else:
                # Has class attribute elsewhere, add new one
                content = re.sub(
                    r'(<body[^>]*)>',
                    r'\1 class="pattern-koru-subtle">',
                    content,
                    count=1
                )
        else:
            # No class attribute, add new one
            content = re.sub(
                r'(<body[^>]*)>',
                r'\1 class="pattern-koru-subtle">',
                content,
                count=1
            )
        
        # Only write if content changed
        if content != original_content:
            filepath.write_text(content, encoding='utf-8')
            files_updated += 1
            return True
        else:
            files_skipped += 1
            return False
            
    except Exception as e:
        print(f"   ⚠️  Error: {filepath.name} - {e}")
        files_error += 1
        return False

# Process all files
print("\n🚀 ADDING KORU PATTERNS:\n")

for i, filepath in enumerate(html_files, 1):
    if add_koru_pattern(filepath):
        if i % 100 == 0:
            print(f"   ✅ {i}/{len(html_files)}: {filepath.name}")

print("\n" + "=" * 70)
print("✅ KORU PATTERN DEPLOYMENT COMPLETE")
print("=" * 70)
print(f"\n✅ Files updated: {files_updated}")
print(f"⏭️  Files skipped: {files_skipped}")
print(f"⚠️  Errors: {files_error}")
print(f"\n🌿 Total pages with koru patterns: {files_updated + files_skipped}")
print("\n💎 Te Kete Ako pages now display beautiful cultural patterns!")
print("\n🌿 Visual cultural excellence achieved! 🌿")

