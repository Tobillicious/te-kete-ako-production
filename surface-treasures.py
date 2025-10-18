#!/usr/bin/env python3
"""
SURFACE TREASURES
Add high-quality hidden resources to navigation
"""

import json

print("⭐ SURFACING QUALITY TREASURES")
print("=" * 70)

with open('treasure-hunt-results.json') as f:
    treasures = json.load(f)

# Filter high-quality only (score >= 8)
high_quality = [t for t in treasures if t['score'] >= 8 and not t['issues']]

print(f"\n🏆 HIGH-QUALITY TREASURES TO SURFACE:")
print(f"   Found {len(high_quality)} resources (score >= 8, no issues)\n")

for i, treasure in enumerate(high_quality[:15], 1):
    print(f"{i}. {treasure['name']} (score: {treasure['score']})")
    print(f"   Path: {treasure['path']}")
    print()

# Categorize by type
experiences = [t for t in high_quality if 'experiences/' in t['path']]
curriculum = [t for t in high_quality if 'curriculum-documents/' in t['path']]
prof_dev = [t for t in high_quality if 'professional-development/' in t['path']]

print("=" * 70)
print("📊 TREASURE CATEGORIES:")
print(f"   Experiences: {len(experiences)} quality resources")
print(f"   Curriculum Docs: {len(curriculum)} quality resources")
print(f"   Prof Development: {len(prof_dev)} quality resources")
print("=" * 70)

print("\n🎯 RECOMMENDATION:")
print("   Add these to homepage or special 'Advanced Features' section")
print("   Each is complete and professionally developed")
