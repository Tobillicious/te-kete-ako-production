#!/usr/bin/env python3
"""
UNIFIED AGENT COORDINATION - Single Source of Truth
Coordinates ALL agent findings into one master view
"""

from pathlib import Path
import json

print("🤝 UNIFIED AGENT COORDINATION")
print("=" * 70)
print("Creating single source of truth from all agent analyses...")
print()

# Real file counts (excluding backups)
public = Path("public")

# Count REAL files only (exclude backups)
real_html = list(public.glob("**/*.html"))
real_html = [f for f in real_html if not any(x in str(f) for x in ['.master', '.backup', '.bak', 'node_modules'])]

# Categorize properly
units = [f for f in real_html if '/units/' in str(f) and 'index.html' in f.name]
lessons = [f for f in real_html if '/lessons/' in str(f) or 'lesson-' in f.name.lower()]
handouts = [f for f in real_html if '/handouts/' in str(f) or 'handout' in f.name.lower()]
games = [f for f in real_html if '/games/' in str(f)]
tools = [f for f in real_html if '/tools/' in str(f)]

# Components and navigation
components = [f for f in real_html if '/components/' in str(f)]
nav_pages = [f for f in real_html if 'index.html' in f.name or 'curriculum' in f.name or 'site-map' in f.name]

print("📊 UNIFIED TRUTH - REAL FILES ONLY")
print("=" * 70)
print(f"\n📁 Total HTML Files: {len(real_html)}")
print(f"   (Excluded backup/master files)")
print()
print(f"📚 Educational Content:")
print(f"   Units (index pages): {len(units)}")
print(f"   Lessons: {len(lessons)}")
print(f"   Handouts: {len(handouts)}")
print(f"   Games: {len(games)}")
print(f"   Tools: {len(tools)}")
print()
print(f"🧭 Navigation & Structure:")
print(f"   Components: {len(components)}")
print(f"   Navigation pages: {len(nav_pages)}")
print()

# List all units
print(f"📦 ALL {len(units)} UNIT INDEX FILES:")
for unit in sorted(units):
    rel_path = unit.relative_to(public)
    print(f"   {rel_path}")

# Save unified truth
truth = {
    "timestamp": "2025-10-18-coordinated",
    "methodology": "Real files only - no backups, no duplicates",
    "total_html_files": len(real_html),
    "units": {
        "count": len(units),
        "files": [str(u.relative_to(public)) for u in sorted(units)]
    },
    "lessons": {
        "count": len(lessons),
        "sample": [str(l.relative_to(public)) for l in sorted(lessons)[:20]]
    },
    "handouts": {
        "count": len(handouts),
        "sample": [str(h.relative_to(public)) for h in sorted(handouts)[:20]]
    },
    "games": {
        "count": len(games),
        "files": [str(g.relative_to(public)) for g in sorted(games)]
    },
    "tools": {
        "count": len(tools),
        "files": [str(t.relative_to(public)) for t in sorted(tools)]
    }
}

with open("UNIFIED-AGENT-TRUTH.json", "w") as f:
    json.dump(truth, f, indent=2)

print()
print("=" * 70)
print("✅ UNIFIED TRUTH saved to: UNIFIED-AGENT-TRUTH.json")
print("=" * 70)
print()
print("🎯 This is the coordinated view all agents should use!")
