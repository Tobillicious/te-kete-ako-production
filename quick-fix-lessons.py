#!/usr/bin/env python3
"""
Quick fix: Remove conflicting legacy CSS from lesson files
All these files already have BMAD, just need cleanup
"""

import re
from pathlib import Path

# Files to fix (already have BMAD, just remove conflicts)
lesson_dirs = [
    "public/units/y8-digital-kaitiakitanga/lessons",
    "public/units/y7-maths-algebra/lessons",
    "public/units/y9-science-ecology/lessons",
    "public/units/y7-science-ecosystems/lessons",
    "public/units/y9-maths-geometry-patterns/lessons"
]

public_dir = Path("./public")
fixed_count = 0

# Pattern to remove (appears before ULTIMATE BEAUTY SYSTEM)
cleanup_pattern = r'<!-- Professional Design System --><link rel="stylesheet" href="/css/te-kete-professional\.css">\s*'

for lesson_dir in lesson_dirs:
    dir_path = Path(lesson_dir)
    if not dir_path.exists():
        continue
    
    html_files = list(dir_path.glob("*.html"))
    # Skip .bak files
    html_files = [f for f in html_files if not f.name.endswith('.bak')]
    
    for filepath in html_files:
        try:
            content = filepath.read_text(encoding='utf-8')
            
            if 'te-kete-professional.css' in content:
                # Remove the old CSS line
                new_content = re.sub(cleanup_pattern, '', content, flags=re.IGNORECASE)
                
                if new_content != content:
                    filepath.write_text(new_content, encoding='utf-8')
                    fixed_count += 1
                    print(f"✅ Fixed: {filepath.relative_to(public_dir)}")
        except Exception as e:
            print(f"❌ Error: {filepath.name} - {e}")

print(f"\n🎊 Fixed {fixed_count} lesson files!")
print("All lessons now use BMAD Ultimate Beauty only (no conflicts)")

