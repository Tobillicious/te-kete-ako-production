#!/usr/bin/env python3
"""
SYSTEMATIC DEDUPLICATION
Find duplicate resources, keep the best version
Quality is EVERYTHING
"""

from pathlib import Path
import hashlib
from collections import defaultdict

print("🔍 FINDING DUPLICATE RESOURCES")
print("=" * 70)

# Find all HTML files (excluding archives/backups)
exclude = ['/archive/', '/backup', '.master', '.bak', 'node_modules', 'temp-restore']
html_files = []

for f in Path('public').rglob('*.html'):
    if not any(ex in str(f) for ex in exclude):
        html_files.append(f)

# Group by filename
by_name = defaultdict(list)
for f in html_files:
    by_name[f.name].append(f)

# Find duplicates
duplicates = {name: paths for name, paths in by_name.items() if len(paths) > 1}

print(f"✅ Scanned {len(html_files)} files")
print(f"🔍 Found {len(duplicates)} filenames with duplicates\n")

# Analyze top duplicates
print("📊 TOP 20 DUPLICATED FILES:")
sorted_dups = sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True)

for i, (filename, paths) in enumerate(sorted_dups[:20], 1):
    print(f"\n{i}. {filename} ({len(paths)} copies)")
    for path in paths[:4]:  # Show first 4 locations
        print(f"   - {path.relative_to(Path('public'))}")

# Deduplication strategy
print("\n" + "=" * 70)
print("🎯 DEDUPLICATION STRATEGY")
print("=" * 70)
print("\nKeep BEST version in canonical location:")
print("  1. generated-resources-alpha/ (newest, professionally styled)")
print("  2. handouts/ (main handout directory)")
print("  3. lessons/ (main lesson directory)")
print("\nArchive duplicates from:")
print("  - integrated-handouts/ (redundant)")
print("  - integrated-lessons/ (redundant)")
print("  - dist-handouts/ (if duplicate)")

# Save deduplication report
import json
dedup_report = {}
for name, paths in sorted_dups[:50]:  # Top 50
    dedup_report[name] = [str(p.relative_to(Path('public'))) for p in paths]

with open('deduplication-report.json', 'w') as f:
    json.dump(dedup_report, f, indent=2)

print("\n✅ Deduplication analysis saved to: deduplication-report.json")
