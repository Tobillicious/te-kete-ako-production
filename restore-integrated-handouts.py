#!/usr/bin/env python3
"""
RESTORE 85 INTEGRATED HANDOUTS
Based on Goldmine Cataloger's discovery!
"""
import os
import shutil
from pathlib import Path

print("📄 RESTORING 85 INTEGRATED HANDOUTS")
print("=" * 70)

source_dir = 'backup_before_css_migration/integrated-handouts'
target_dir = 'public/integrated-handouts'

if not os.path.exists(source_dir):
    source_dir = 'archive/redundant-duplicates-oct18/integrated-handouts'

if os.path.exists(source_dir):
    print(f"✓ Found source: {source_dir}")
    
    os.makedirs(target_dir, exist_ok=True)
    
    copied_count = 0
    for root, dirs, files in os.walk(source_dir):
        rel_dir = os.path.relpath(root, source_dir)
        target_subdir = os.path.join(target_dir, rel_dir) if rel_dir != '.' else target_dir
        
        os.makedirs(target_subdir, exist_ok=True)
        
        for file in files:
            if file.endswith('.html'):
                shutil.copy2(os.path.join(root, file), os.path.join(target_subdir, file))
                copied_count += 1
                if copied_count % 20 == 0:
                    print(f"   Progress: {copied_count} handouts...")
    
    print(f"\n✅ {copied_count} handouts restored!")
    
else:
    print(f"❌ Source not found")

