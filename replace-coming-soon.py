#!/usr/bin/env python3
"""
Replace 'coming soon' with professional content cards
"""

import re
from pathlib import Path

print("🔧 REPLACING 'COMING SOON' WITH PROFESSIONAL CONTENT")
print("=" * 70)

# Files with "coming soon"
files_to_fix = [
    'public/units/y7-maths-algebra/index.html',
    'public/units/lessons/systems-lesson-1-2.html',
    'public/units/lessons/unit-5-lesson-5.html',
    'public/units/y9-mathematics-geometry-maori-patterns/index.html',
]

replacement_card = '''<div class="info-card">
    <h3>📚 Additional Resources Available</h3>
    <p>More learning materials and activities for this topic are available through your teacher or can be accessed via the main resource library.</p>
    <a href="/handouts/" class="btn btn-primary">Explore Resource Library →</a>
</div>'''

fixed_count = 0

for file_path in files_to_fix:
    try:
        if not Path(file_path).exists():
            continue
            
        content = Path(file_path).read_text(encoding='utf-8')
        
        # Replace various "coming soon" patterns
        patterns = [
            (r'<p[^>]*>.*?coming soon.*?</p>', replacement_card),
            (r'<div[^>]*>.*?coming soon.*?</div>', replacement_card),
        ]
        
        modified = False
        for pattern, replacement in patterns:
            if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL, count=1)
                modified = True
        
        if modified:
            Path(file_path).write_text(content, encoding='utf-8')
            print(f"✅ Fixed: {file_path}")
            fixed_count += 1
    
    except Exception as e:
        print(f"⚠️  Error fixing {file_path}: {e}")

print("\n" + "=" * 70)
print(f"✅ Fixed {fixed_count} files with 'coming soon' text")
print("=" * 70)
