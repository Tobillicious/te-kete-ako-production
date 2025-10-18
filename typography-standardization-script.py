#!/usr/bin/env python3
"""
Typography Standardization - Phase 1.1
Replace inline font-size styles with CSS variables
Coordinated execution with Overseer edef03f6
"""

from pathlib import Path
import re

PUBLIC = Path("public")

# Standardization mapping (inline style → CSS variable)
FONT_SIZE_MAP = {
    r'font-size:\s*0\.75rem': 'font-size: var(--text-xs)',
    r'font-size:\s*0\.85rem': 'font-size: var(--text-sm)',
    r'font-size:\s*0\.875rem': 'font-size: var(--text-sm)',
    r'font-size:\s*0\.9rem': 'font-size: var(--text-sm)',
    r'font-size:\s*0\.95rem': 'font-size: var(--text-base)',
    r'font-size:\s*1rem': 'font-size: var(--text-base)',
    r'font-size:\s*1\.1rem': 'font-size: var(--text-lg)',
    r'font-size:\s*1\.125rem': 'font-size: var(--text-lg)',
    r'font-size:\s*1\.2rem': 'font-size: var(--text-xl)',
    r'font-size:\s*1\.25rem': 'font-size: var(--text-xl)',
    r'font-size:\s*1\.3rem': 'font-size: var(--text-xl)',
    r'font-size:\s*1\.4rem': 'font-size: var(--text-2xl)',
    r'font-size:\s*1\.5rem': 'font-size: var(--text-2xl)',
    r'font-size:\s*1\.875rem': 'font-size: var(--text-3xl)',
    r'font-size:\s*2rem': 'font-size: var(--text-3xl)',
    r'font-size:\s*2\.25rem': 'font-size: var(--text-4xl)',
    r'font-size:\s*2\.5rem': 'font-size: var(--text-4xl)',
    r'font-size:\s*3rem': 'font-size: var(--text-5xl)',
    r'font-size:\s*3\.5rem': 'font-size: var(--text-5xl)',
    r'font-size:\s*4rem': 'font-size: var(--text-6xl)',
}

def standardize_typography():
    print("🎨 TYPOGRAPHY STANDARDIZATION - Phase 1.1")
    print("=" * 60)
    print("Coordinated with Overseer edef03f6-e82b-46a2-8dd3-f6e0e6a05f6a")
    print()
    
    files_updated = 0
    replacements_made = 0
    
    # Focus on key pages first (high-impact)
    priority_files = [
        PUBLIC / "index.html",
        PUBLIC / "lessons.html",
        PUBLIC / "handouts.html",
        PUBLIC / "curriculum-index.html",
        PUBLIC / "units" / "index.html",
    ]
    
    print("📋 Processing priority pages...")
    for file_path in priority_files:
        if file_path.exists():
            try:
                content = file_path.read_text(encoding='utf-8')
                original_content = content
                
                # Apply all replacements
                for pattern, replacement in FONT_SIZE_MAP.items():
                    content, count = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
                    if count > 0:
                        replacements_made += count
                
                # Save if changed
                if content != original_content:
                    file_path.write_text(content, encoding='utf-8')
                    files_updated += 1
                    print(f"   ✅ {file_path.relative_to(PUBLIC)}")
                    
            except Exception as e:
                print(f"   ⚠️  Error processing {file_path}: {e}")
    
    print()
    print("=" * 60)
    print(f"✅ Phase 1.1 Complete:")
    print(f"   Files updated: {files_updated}")
    print(f"   Replacements: {replacements_made}")
    print("=" * 60)
    
    return files_updated, replacements_made

if __name__ == "__main__":
    updated, replaced = standardize_typography()
    print(f"\n🎯 Typography now standardized using CSS variables!")
    print(f"   Consistent font sizes across {updated} priority pages")

