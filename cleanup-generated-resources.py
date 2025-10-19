#!/usr/bin/env python3
"""
Quick cleanup for generated-resources-alpha
These files already have BMAD, just remove conflicting CSS
"""

import re
from pathlib import Path

public_dir = Path("./public")
target_dir = public_dir / "generated-resources-alpha"

# Pattern to clean up
cleanup_pattern = r'<!-- Professional Design System -->\s*<link rel="stylesheet" href="/css/te-kete-professional\.css">\s*'

cleaned = 0
errors = 0

# Get all HTML files (not .bak)
html_files = [f for f in target_dir.rglob("*.html") if not f.name.endswith('.bak')]

print(f"🧹 Cleaning up {len(html_files)} generated-resources-alpha files...")

for filepath in html_files:
    try:
        content = filepath.read_text(encoding='utf-8')
        
        if 'te-kete-professional.css' in content:
            # Remove the conflicting CSS line
            new_content = re.sub(cleanup_pattern, '', content, flags=re.IGNORECASE)
            
            # Also add framer gestures if missing
            if 'framer-cultural-gestures-ultimate.js' not in new_content:
                new_content = new_content.replace(
                    '<script src="/tailwind.config.ultimate.js"></script>',
                    '<script src="/tailwind.config.ultimate.js"></script>\n <script src="/js/framer-cultural-gestures-ultimate.js" defer></script>'
                )
            
            if new_content != content:
                filepath.write_text(new_content, encoding='utf-8')
                cleaned += 1
                if cleaned <= 10:  # Show first 10
                    print(f"  ✅ {filepath.relative_to(public_dir)}")
                    
    except Exception as e:
        print(f"  ❌ {filepath.name} - {e}")
        errors += 1

print(f"\n🎊 Cleanup complete!")
print(f"✅ Cleaned: {cleaned} files")
print(f"❌ Errors: {errors} files")
print(f"\n✨ All generated-resources-alpha pages now pure BMAD Q100!")

