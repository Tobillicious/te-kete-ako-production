#!/usr/bin/env python3
"""
Thoroughly verify alt text status
Check for empty alt="" vs missing alt attribute
"""

import re
from pathlib import Path

print("🔍 THOROUGH ALT TEXT VERIFICATION")
print("=" * 70)

stats = {
    'total_images': 0,
    'has_alt_attribute': 0,
    'empty_alt': 0,
    'descriptive_alt': 0,
    'no_alt': 0
}

examples = {
    'empty_alt': [],
    'descriptive_alt': [],
    'no_alt': []
}

# Scan public directory
for html_file in Path('public').rglob('*.html'):
    try:
        content = html_file.read_text(encoding='utf-8')
        
        # Find all img tags (more comprehensive regex)
        img_tags = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
        
        for img in img_tags:
            stats['total_images'] += 1
            
            # Check for alt attribute
            alt_match = re.search(r'alt\s*=\s*["\']([^"\']*)["\']', img, re.IGNORECASE)
            
            if alt_match:
                stats['has_alt_attribute'] += 1
                alt_text = alt_match.group(1)
                
                if not alt_text or alt_text.strip() == '':
                    stats['empty_alt'] += 1
                    if len(examples['empty_alt']) < 3:
                        examples['empty_alt'].append(f"{html_file.name}: {img[:80]}")
                else:
                    stats['descriptive_alt'] += 1
                    if len(examples['descriptive_alt']) < 3:
                        examples['descriptive_alt'].append(f"{html_file.name}: alt=\"{alt_text}\"")
            else:
                stats['no_alt'] += 1
                if len(examples['no_alt']) < 3:
                    examples['no_alt'].append(f"{html_file.name}: {img[:80]}")
    
    except Exception as e:
        pass

# Results
print(f"\n📊 IMAGE ALT TEXT STATUS")
print("=" * 70)
print(f"\n✅ Total images found: {stats['total_images']}")
print(f"\n📋 Alt Text Breakdown:")
print(f"   ✅ Descriptive alt text: {stats['descriptive_alt']} ({stats['descriptive_alt']/stats['total_images']*100:.1f}%)")
print(f"   ⚠️  Empty alt text (alt=\"\"): {stats['empty_alt']} ({stats['empty_alt']/stats['total_images']*100:.1f}%)")
print(f"   ❌ No alt attribute: {stats['no_alt']} ({stats['no_alt']/stats['total_images']*100:.1f}%)")

# Examples
if examples['descriptive_alt']:
    print(f"\n✅ Good Examples (Descriptive Alt Text):")
    for ex in examples['descriptive_alt']:
        print(f"   {ex}")

if examples['empty_alt']:
    print(f"\n⚠️  Empty Alt Text Examples:")
    for ex in examples['empty_alt']:
        print(f"   {ex}")

if examples['no_alt']:
    print(f"\n❌ Missing Alt Attribute Examples:")
    for ex in examples['no_alt']:
        print(f"   {ex}")

# WCAG Assessment
print("\n" + "=" * 70)
print("🎯 WCAG 2.1 AA COMPLIANCE ASSESSMENT")
print("=" * 70)

compliant = stats['has_alt_attribute']
total = stats['total_images']

if total == 0:
    print("\n✅ No images found - N/A")
elif compliant == total and stats['empty_alt'] == 0:
    print("\n🎉 FULLY COMPLIANT - All images have descriptive alt text!")
elif compliant == total:
    print(f"\n⚠️  PARTIAL COMPLIANCE - All have alt attributes, but {stats['empty_alt']} are empty")
    print("   → Empty alt=\"\" is acceptable for decorative images only")
else:
    print(f"\n❌ NON-COMPLIANT - {stats['no_alt']} images missing alt attribute")
    print("   → Must add alt text to all images")

print("\n" + "=" * 70)
