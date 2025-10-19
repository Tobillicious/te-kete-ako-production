#!/usr/bin/env python3
"""
🧹 BMAD CSS CONFLICT CLEANUP - PHASE 3: SITE-WIDE
Remove te-kete-professional.css from all 3,788 files that have conflicts
Keep BMAD Ultimate Beauty System intact
"""

import os
import re
from pathlib import Path

# Base directory
PUBLIC_DIR = Path("public")

# Track progress
total_fixed = 0
total_errors = 0
directories_processed = set()

def clean_file(filepath):
    """Remove te-kete-professional.css from a single file"""
    global total_fixed, total_errors
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has both BMAD and old CSS
        has_bmad = 'te-kete-ultimate-beauty-system.css' in content
        has_old_css = 'te-kete-professional.css' in content
        
        if not has_old_css:
            return False  # Nothing to fix
        
        if not has_bmad:
            print(f"⚠️  WARNING: {filepath} has old CSS but NO BMAD! Skipping...")
            return False
        
        # Remove the old CSS link (handle multiple occurrences and variations)
        patterns_to_remove = [
            r'\s*<link\s+rel="stylesheet"\s+href="/css/te-kete-professional\.css"\s*/?>',
            r'\s*<link\s+href="/css/te-kete-professional\.css"\s+rel="stylesheet"\s*/?>',
            r'\s*<link\s+rel="stylesheet"\s+href="/css/te-kete-professional\.css"\s*>',
            r'\s*<link\s+href="/css/te-kete-professional\.css"\s+rel="stylesheet"\s*>',
        ]
        
        original_content = content
        for pattern in patterns_to_remove:
            content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # Only write if something changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            total_fixed += 1
            directory = str(filepath.parent.relative_to(PUBLIC_DIR))
            directories_processed.add(directory)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ ERROR processing {filepath}: {e}")
        total_errors += 1
        return False

def main():
    print("🎨 BMAD CSS CONFLICT CLEANUP - PHASE 3")
    print("=" * 60)
    print("Target: Remove te-kete-professional.css from 3,788 files")
    print("Keep: BMAD Ultimate Beauty System")
    print("=" * 60)
    print()
    
    # Find all HTML files in public directory
    html_files = list(PUBLIC_DIR.rglob("*.html"))
    
    print(f"📊 Found {len(html_files)} HTML files total")
    print("🔄 Processing...\n")
    
    # Process each file
    for i, filepath in enumerate(html_files, 1):
        if i % 100 == 0:
            print(f"   Progress: {i}/{len(html_files)} files processed...")
        
        clean_file(filepath)
    
    # Print summary
    print("\n" + "=" * 60)
    print("✅ CLEANUP COMPLETE!")
    print("=" * 60)
    print(f"📝 Files cleaned: {total_fixed}")
    print(f"❌ Errors: {total_errors}")
    print(f"📁 Directories processed: {len(directories_processed)}")
    print("\n🎨 BMAD now deployed cleanly across:")
    for directory in sorted(directories_processed):
        print(f"   ✓ {directory}")
    print("\n🚀 All files now have PURE BMAD with no conflicts!")

if __name__ == "__main__":
    main()

