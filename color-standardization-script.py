#!/usr/bin/env python3
"""
Color Standardization - Phase 1.2
Replace inline hex colors with CSS variables
"""

from pathlib import Path
import re

PUBLIC = Path("public")

# Common color replacements
COLOR_MAP = {
    r'color:\s*#0f2818': 'color: var(--color-primary)',
    r'color:\s*#1a4d2e': 'color: var(--color-primary)',
    r'color:\s*#4a6e2a': 'color: var(--color-primary)',
    r'color:\s*#2c3e50': 'color: var(--color-text-primary)',
    r'color:\s*#546e7a': 'color: var(--color-text-secondary)',
    r'color:\s*#666': 'color: var(--color-text-secondary)',
    r'color:\s*#999': 'color: var(--color-text-muted)',
    r'color:\s*#f59e0b': 'color: var(--color-accent)',
    r'color:\s*#92400e': 'color: var(--color-accent)',
    r'background:\s*#1a4d2e': 'background: var(--color-primary)',
    r'background:\s*#10b981': 'background: var(--color-success)',
    r'background:\s*#3b82f6': 'background: var(--color-info)',
}

def standardize_colors():
    print("🎨 COLOR STANDARDIZATION - Phase 1.2")
    print("=" * 60)
    
    files_updated = 0
    replacements_made = 0
    
    priority_files = [
        PUBLIC / "index.html",
        PUBLIC / "lessons.html",  
        PUBLIC / "handouts.html",
        PUBLIC / "curriculum-index.html",
        PUBLIC / "units" / "index.html",
    ]
    
    for file_path in priority_files:
        if file_path.exists():
            try:
                content = file_path.read_text(encoding='utf-8')
                original = content
                
                for pattern, replacement in COLOR_MAP.items():
                    content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
                    replacements_made += count
                
                if content != original:
                    file_path.write_text(content, encoding='utf-8')
                    files_updated += 1
                    print(f"   ✅ {file_path.relative_to(PUBLIC)}")
            except Exception as e:
                print(f"   ⚠️  {file_path}: {e}")
    
    print()
    print(f"✅ Files updated: {files_updated}")
    print(f"✅ Color replacements: {replacements_made}")
    return files_updated, replacements_made

if __name__ == "__main__":
    standardize_colors()
