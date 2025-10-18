#!/usr/bin/env python3
"""
Mass CSS Migration: Deprecated → te-kete-professional.css
Fixes the 580-page CSS fragmentation issue
"""

import os
import re
from pathlib import Path

# Deprecated CSS systems to replace
DEPRECATED_CSS = [
    'te-kete-unified-design-system.css',
    'main.css'
]

CANONICAL_CSS = 'te-kete-professional.css'

def migrate_file(file_path):
    """Migrate a single file from deprecated CSS to canonical CSS"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Replace each deprecated CSS reference
        for deprecated in DEPRECATED_CSS:
            if deprecated in content:
                # Replace the link tag
                pattern = f'<link rel="stylesheet" href="[./]*css/{re.escape(deprecated)}"[^>]*>'
                replacement = f'<link rel="stylesheet" href="/css/{CANONICAL_CSS}">'
                
                new_content = re.sub(pattern, replacement, content)
                
                if new_content != content:
                    changes_made.append(f"{deprecated} → {CANONICAL_CSS}")
                    content = new_content
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        
        return False, []
    
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False, []

def main():
    print("🔧 CSS MIGRATION: Deprecated → te-kete-professional.css\n")
    
    public_dir = Path('/Users/admin/Documents/te-kete-ako-clean/public')
    
    # Find all HTML files
    html_files = list(public_dir.rglob('*.html'))
    
    print(f"📂 Found {len(html_files)} HTML files in public/\n")
    
    migrated = 0
    skipped = 0
    
    for file_path in html_files:
        success, changes = migrate_file(file_path)
        
        if success:
            migrated += 1
            relative_path = file_path.relative_to(public_dir.parent)
            print(f"✅ {relative_path}")
            for change in changes:
                print(f"   → {change}")
        else:
            skipped += 1
    
    print(f"\n📊 MIGRATION COMPLETE!")
    print(f"   ✅ Migrated: {migrated} files")
    print(f"   ⏭️  Skipped: {skipped} files (already using canonical CSS)")
    print(f"   📦 Total: {len(html_files)} files processed")

if __name__ == "__main__":
    main()

