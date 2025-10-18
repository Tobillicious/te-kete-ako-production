#!/usr/bin/env python3
"""
Find units missing navigation components
"""

from pathlib import Path

print("🔍 FINDING UNITS MISSING NAVIGATION")
print("=" * 70)

units_dir = Path('public/units')
missing_nav = []

for index_file in units_dir.rglob('index.html'):
    try:
        content = index_file.read_text(encoding='utf-8')
        
        # Check for navigation component
        has_nav = (
            'navigation-standard.html' in content or
            '<nav' in content or
            'navigation-enhanced' in content
        )
        
        if not has_nav:
            missing_nav.append(str(index_file.relative_to('public')))
    
    except Exception as e:
        pass

print(f"\n📊 Found {len(missing_nav)} units missing navigation:\n")

for unit_path in sorted(missing_nav):
    print(f"   ❌ {unit_path}")

print(f"\n💡 Total units to fix: {len(missing_nav)}")
print("=" * 70)
