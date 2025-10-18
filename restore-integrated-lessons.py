#!/usr/bin/env python3
"""
RESTORE 377 INTEGRATED LESSONS TO PRODUCTION
Based on Goldmine Cataloger's discovery!
"""
import os
import shutil
from pathlib import Path

print("🔄 RESTORING 377 INTEGRATED LESSONS TO PRODUCTION")
print("=" * 70)

source_dir = 'backup_before_css_migration/integrated-lessons'
target_dir = 'public/integrated-lessons'

if not os.path.exists(source_dir):
    print(f"⚠️  Source not found: {source_dir}")
    print("Checking archive...")
    source_dir = 'archive/redundant-duplicates-oct18/integrated-lessons'

if os.path.exists(source_dir):
    print(f"✓ Found source: {source_dir}")
    
    # Copy entire directory structure
    print(f"\n📦 Copying to {target_dir}...")
    
    if os.path.exists(target_dir):
        print(f"   Target already exists, merging...")
    else:
        print(f"   Creating target directory...")
        os.makedirs(target_dir, exist_ok=True)
    
    # Copy all subdirectories and files
    copied_count = 0
    for root, dirs, files in os.walk(source_dir):
        # Calculate relative path
        rel_dir = os.path.relpath(root, source_dir)
        target_subdir = os.path.join(target_dir, rel_dir) if rel_dir != '.' else target_dir
        
        # Create subdirectory if needed
        os.makedirs(target_subdir, exist_ok=True)
        
        # Copy HTML files
        for file in files:
            if file.endswith('.html'):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_subdir, file)
                shutil.copy2(source_file, target_file)
                copied_count += 1
                
                if copied_count % 50 == 0:
                    print(f"   Progress: {copied_count} files copied...")
    
    print(f"\n✅ RESTORATION COMPLETE!")
    print(f"   Files copied: {copied_count}")
    print(f"   Target: {target_dir}")
    
    # Count by subject
    subjects = {}
    for root, dirs, files in os.walk(target_dir):
        subject = Path(root).name
        html_count = sum(1 for f in files if f.endswith('.html'))
        if html_count > 0:
            subjects[subject] = html_count
    
    print(f"\n📊 BY SUBJECT:")
    total_lessons = 0
    for subject, count in sorted(subjects.items(), key=lambda x: x[1], reverse=True):
        print(f"   {subject}: {count}")
        total_lessons += count
    
    print(f"\n   TOTAL: {total_lessons} lessons")
    
else:
    print(f"❌ Could not find integrated-lessons directory")
    print(f"   Checked: backup_before_css_migration/")
    print(f"   Checked: archive/redundant-duplicates-oct18/")

print(f"\n🎯 Next: Create index page with subject navigation!")

