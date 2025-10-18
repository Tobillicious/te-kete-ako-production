#!/usr/bin/env python3
"""
SYSTEMATIC DEDUPLICATION - Phase 1
Archive duplicates from integrated-handouts and integrated-lessons
Keep canonical versions in main directories
"""

from pathlib import Path
import shutil

print("🧹 SYSTEMATIC DEDUPLICATION - Phase 1")
print("=" * 70)

# Strategy: integrated-handouts and integrated-lessons appear to be redundant
# Keep: generated-resources-alpha, handouts, lessons, units
# Archive: integrated-handouts, integrated-lessons

redundant_dirs = [
    'public/integrated-handouts',
    'public/integrated-lessons',
]

archived = 0
for dir_path in redundant_dirs:
    dir_obj = Path(dir_path)
    if dir_obj.exists():
        # Count files first
        files = list(dir_obj.rglob('*.html'))
        count = len(files)
        
        # Move entire directory to archive
        archive_dest = Path(f'archive/redundant-duplicates-oct18/{dir_obj.name}')
        archive_dest.parent.mkdir(parents=True, exist_ok=True)
        
        if archive_dest.exists():
            shutil.rmtree(archive_dest)
        
        shutil.move(str(dir_obj), str(archive_dest))
        archived += count
        
        print(f"✅ Archived {count} files from {dir_obj.name}/")

print(f"\n=" * 70)
print(f"✅ Archived {archived} duplicate files")
print(f"   Moved integrated-handouts/ and integrated-lessons/ to archive")
print(f"   Canonical versions remain in main directories")
print("=" * 70)
