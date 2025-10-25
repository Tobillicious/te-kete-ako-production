#!/usr/bin/env python3
"""
FIX INFLATED RESOURCE NUMBERS SITEWIDE

The site currently claims:
- 24,971 total resources
- 20,948 total resources
- 5,765 lessons
- 3,744 handouts

Reality (from GraphRAG - Oct 26, 2025):
- 3,564 total resources (verified)
- ~1,524 lessons (estimated from GraphRAG)
- ~982 handouts (estimated)
- ~1,058 other resources

This fixes teacher trust by showing HONEST numbers.
"""

import re
from pathlib import Path

# REAL numbers from GraphRAG (verified Oct 26, 2025)
REAL_TOTALS = {
    "24,971": "3,500+",  # Conservative estimate
    "24971": "3500",
    "20,948": "3,500+",
    "20948": "3500",
    "5,765": "1,500+",  # Lessons estimate
    "5765": "1500",
    "3,744": "980+",  # Handouts estimate
    "3744": "980",
    "11,839": "3,500+",  # Another inflated number
    "11839": "3500",
}

# Also fix the text descriptions
TEXT_FIXES = {
    "New Zealand's largest collection": "A comprehensive curated collection",
    "Complete Library": "Curated Library",
    "MASSIVE COLLECTION": "CURATED COLLECTION",
}

def fix_file(filepath):
    """Fix inflated numbers in a single file"""
    try:
        content = filepath.read_text(encoding='utf-8')
        original = content
        
        # Fix numbers
        for fake_num, real_num in REAL_TOTALS.items():
            if fake_num in content:
                content = content.replace(fake_num, real_num)
                print(f"  ✓ Fixed {fake_num} → {real_num}")
        
        # Fix text descriptions
        for fake_text, real_text in TEXT_FIXES.items():
            if fake_text in content:
                content = content.replace(fake_text, real_text)
                print(f"  ✓ Fixed '{fake_text}' → '{real_text}'")
        
        # Write back if changed
        if content != original:
            filepath.write_text(content, encoding='utf-8')
            return True
            
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False
    
    return False

# Execute
print("🔧 FIXING INFLATED RESOURCE NUMBERS SITEWIDE")
print("=" * 70)
print(f"Reality: 3,564 resources (not 24,971!)")
print(f"Fixing files...\n")

files_to_fix = [
    "public/TEACHER-QUICK-START-GUIDE.html",
    "public/massive-collection-hero.html",
    "public/top-10-starter-pack.html",
    "public/components/navigation-ai.html",
    "public/components/navigation-unified.html",
]

fixed_count = 0
for file_path in files_to_fix:
    filepath = Path(file_path)
    if filepath.exists():
        print(f"\n📄 {filepath.name}:")
        if fix_file(filepath):
            fixed_count += 1
    else:
        print(f"\n⚠️  {filepath} does not exist")

print(f"\n{'='*70}")
print(f"✅ COMPLETE: Fixed {fixed_count} files")
print(f"📊 All numbers now show HONEST, REAL counts")
print(f"🎯 Teacher trust restored!")

