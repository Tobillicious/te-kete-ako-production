#!/usr/bin/env python3
"""
ANALYZE ALL 90K FILES - Full Iceberg Analysis
Understand what content exists across ALL versions
"""

from pathlib import Path
from collections import defaultdict
import hashlib

print("🔍 ANALYZING THE FULL ICEBERG - ALL 90K FILES")
print("=" * 70)

# All directories to analyze
directories = {
    "CURRENT (public/)": Path("public"),
    "DIST (dist/)": Path("dist"),
    "CSS_BACKUP (backup_before_css_migration/)": Path("backup_before_css_migration"),
    "MINIFY_BACKUP (backup_before_minification/)": Path("backup_before_minification"),
    "BACKUPS (backups/)": Path("backups"),
}

all_unique_files = {}  # filename -> list of (path, size, version)
file_versions = defaultdict(list)

print("\n📁 Scanning all directories...")

for version_name, dir_path in directories.items():
    if not dir_path.exists():
        continue
    
    html_files = list(dir_path.rglob("*.html"))
    # Filter out node_modules
    html_files = [f for f in html_files if 'node_modules' not in str(f)]
    
    print(f"\n{version_name}:")
    print(f"  HTML files: {len(html_files)}")
    
    for file_path in html_files:
        filename = file_path.name
        size = file_path.stat().st_size
        
        # Track all versions of this file
        file_versions[filename].append({
            "version": version_name,
            "path": str(file_path),
            "size": size
        })

print(f"\n" + "=" * 70)
print(f"📊 AGGREGATED ANALYSIS")
print("=" * 70)

# Find files that exist in multiple versions
multi_version = {name: versions for name, versions in file_versions.items() if len(versions) > 1}

print(f"\nTotal unique filenames: {len(file_versions)}")
print(f"Files with multiple versions: {len(multi_version)}")
print(f"Files with only one version: {len(file_versions) - len(multi_version)}")

# Find unique content (only in backups, not in current)
current_files = set()
if Path("public").exists():
    current_files = {f.name for f in Path("public").rglob("*.html") if 'node_modules' not in str(f)}

backup_only = {}
for filename, versions in file_versions.items():
    if filename not in current_files:
        # This file exists in backups but NOT in current public/
        backup_only[filename] = versions

print(f"\n💎 FILES ONLY IN BACKUPS (not in current public/):")
print(f"   Count: {len(backup_only)}")
print(f"   These might be lost treasures!\n")

# Sample some
print("  Sample backup-only files:")
for filename in list(backup_only.keys())[:20]:
    versions = backup_only[filename]
    print(f"    • {filename} (in {len(versions)} backup versions)")

# Find files with significantly different sizes (potential improvements)
print(f"\n📊 FILES WITH MULTIPLE VERSIONS (potential improvements):")
size_differences = []

for filename, versions in list(multi_version.items())[:20]:
    sizes = [v['size'] for v in versions]
    if max(sizes) > min(sizes) * 1.2:  # 20% size difference
        size_differences.append({
            "file": filename,
            "min_size": min(sizes),
            "max_size": max(sizes),
            "versions": len(versions)
        })

size_differences.sort(key=lambda x: x['max_size'] - x['min_size'], reverse=True)

print(f"   Files with significant size differences: {len(size_differences)}")
for item in size_differences[:10]:
    diff = item['max_size'] - item['min_size']
    print(f"    • {item['file']}: {item['min_size']:,} → {item['max_size']:,} (+{diff:,} bytes)")

# Export for further analysis
import json
with open('full-iceberg-analysis.json', 'w') as f:
    json.dump({
        "total_unique_files": len(file_versions),
        "multi_version_files": len(multi_version),
        "backup_only_files": len(backup_only),
        "backup_only_list": list(backup_only.keys())[:100],
        "size_differences": size_differences[:50]
    }, f, indent=2)

print(f"\n💾 Saved to: full-iceberg-analysis.json")

print("\n" + "=" * 70)
print("🎯 KEY FINDINGS:")
print(f"  • {len(backup_only)} files exist ONLY in backups")
print(f"  • {len(size_differences)} files have better versions in backups")
print(f"  • Need to review and merge valuable backup content")
print("=" * 70)

