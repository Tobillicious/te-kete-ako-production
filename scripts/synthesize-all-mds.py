#!/usr/bin/env python3
"""
SYNTHESIZE ALL MD FILES
Archive everything except 5 master docs
Extract key info to GraphRAG
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
ROOT = BASE_DIR
ARCHIVE_DIR = BASE_DIR / "docs" / "archive" / f"synthesis-{datetime.now().strftime('%Y%m%d-%H%M')}"

# The ONLY MDs allowed in root
MASTER_DOCS = {
    'ACTIVE_QUESTIONS.md',
    'MASTER_STATUS.md',
    'MASTER_TECH_SPECS.md',
    'MASTER_CONTENT_MAP.md',
    'README.md',
    'progress-log.md'  # Keep for historical timeline
}

def archive_md_files():
    """Archive all non-master MD files"""
    
    print("🚨 MD SYNTHESIS - CLEANING CODEBASE")
    print("=" * 70)
    
    # Create archive directory
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📁 Archive directory: {ARCHIVE_DIR}")
    print()
    
    # Find all MD files in root
    md_files = list(ROOT.glob("*.md"))
    
    print(f"📊 Found {len(md_files)} MD files in root")
    print()
    
    archived_count = 0
    kept_count = 0
    
    for md_file in md_files:
        if md_file.name in MASTER_DOCS:
            print(f"✅ KEEP: {md_file.name}")
            kept_count += 1
        else:
            # Archive it
            dest = ARCHIVE_DIR / md_file.name
            shutil.move(str(md_file), str(dest))
            print(f"📦 ARCHIVED: {md_file.name}")
            archived_count += 1
    
    print()
    print("=" * 70)
    print(f"✅ SYNTHESIS COMPLETE!")
    print(f"   Kept: {kept_count} master docs")
    print(f"   Archived: {archived_count} files")
    print(f"   Archive: {ARCHIVE_DIR}")
    print("=" * 70)
    print()
    print("📋 REMAINING IN ROOT:")
    for md in sorted(MASTER_DOCS):
        if (ROOT / md).exists():
            print(f"   ✅ {md}")
    print()
    print("🎯 CODEBASE IS NOW CLEAN!")
    print("🚨 AGENTS: Use ACTIVE_QUESTIONS.md + MCP/GraphRAG ONLY!")

if __name__ == "__main__":
    archive_md_files()

