#!/usr/bin/env python3
"""
STRATEGIC AUDIT - Data-Driven Analysis
Use the complete mapped codebase to reveal best paths forward
"""

import json
from collections import defaultdict, Counter
from pathlib import Path

print("🎯 STRATEGIC AUDIT - Finding the Gold")
print("=" * 70)

# Load all data
with open('processing-progress.json', 'r') as f:
    data = json.load(f)

approved = data['approved']
needs_work = data['needs_work']
relationships = data['relationships']

print(f"\n📊 Data loaded:")
print(f"   • {len(approved):,} approved resources")
print(f"   • {len(relationships):,} relationships")
print("\n🔍 Running strategic analysis...\n")

# === ANALYSIS 1: Hidden Gems (High Quality, Not in Production) ===
print("💎 ANALYSIS 1: HIDDEN GEMS")
print("-" * 70)

hidden_gems = [f for f in approved 
               if not f['in_production'] 
               and f['score'] >= 95 
               and f['size_kb'] > 5]

hidden_gems.sort(key=lambda x: x['score'], reverse=True)

print(f"Found {len(hidden_gems)} high-quality files NOT in production!\n")
for i, gem in enumerate(hidden_gems[:10], 1):
    print(f"{i}. {gem['title'][:60]}")
    print(f"   Score: {gem['score']}% | Size: {gem['size_kb']:.1f}KB | Links: {gem['links']}")
    print(f"   Path: {gem['path']}")
    print()

# === ANALYSIS 2: Most Connected Resources (Hub Pages) ===
print("\n🔗 ANALYSIS 2: HUB PAGES (Most Connected)")
print("-" * 70)

# Count outbound links
outbound_counts = Counter()
for rel in relationships:
    outbound_counts[rel['from']] += 1

top_hubs = []
for resource in approved:
    if resource['in_production']:
        count = outbound_counts.get(resource['path'], 0)
        if count > 10:
            top_hubs.append((resource, count))

top_hubs.sort(key=lambda x: x[1], reverse=True)

print(f"Top 10 most connected pages (navigation hubs):\n")
for i, (hub, count) in enumerate(top_hubs[:10], 1):
    print(f"{i}. {hub['title'][:50]} - {count} outbound links")
    print(f"   {hub['path']}")
    print()

# === ANALYSIS 3: Orphaned Gems (Good Content, Few Inbound Links) ===
print("\n🏝️  ANALYSIS 3: ORPHANED GEMS")
print("-" * 70)

# Count inbound links
inbound_counts = Counter()
for rel in relationships:
    inbound_counts[rel['to']] += 1

orphaned = []
for resource in approved:
    if resource['in_production'] and resource['score'] >= 90:
        inbound = inbound_counts.get(resource['path'], 0)
        if inbound < 3:  # Very few inbound links
            orphaned.append((resource, inbound))

orphaned.sort(key=lambda x: x[0]['score'], reverse=True)

print(f"High-quality pages with <3 inbound links (hard to discover):\n")
for i, (resource, inbound) in enumerate(orphaned[:10], 1):
    print(f"{i}. {resource['title'][:50]} ({resource['score']}%)")
    print(f"   Inbound links: {inbound} | Should be featured more!")
    print(f"   {resource['path']}")
    print()

# === ANALYSIS 4: Subject Coverage Analysis ===
print("\n📚 ANALYSIS 4: SUBJECT COVERAGE")
print("-" * 70)

subjects = {
    'mathematics': [],
    'science': [],
    'english': [],
    'social': [],
    'te reo': [],
    'arts': [],
    'technology': []
}

for resource in approved:
    if resource['in_production']:
        path_lower = resource['path'].lower()
        title_lower = resource['title'].lower()
        combined = f"{path_lower} {title_lower}"
        
        for subject in subjects.keys():
            if subject in combined or subject.replace(' ', '-') in combined:
                subjects[subject].append(resource)

print("Production resources by subject:\n")
for subject, resources in sorted(subjects.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{subject.title():20} {len(resources):4} resources")

# Find gaps
print("\n⚠️  Gaps to fill:")
min_count = min(len(r) for r in subjects.values())
max_count = max(len(r) for r in subjects.values())
for subject, resources in subjects.items():
    if len(resources) < min_count * 2:
        print(f"   📉 {subject.title()}: Only {len(resources)} resources (could add more)")

# === ANALYSIS 5: Year Level Coverage ===
print("\n\n📊 ANALYSIS 5: YEAR LEVEL COVERAGE")
print("-" * 70)

year_levels = defaultdict(list)
for resource in approved:
    if resource['in_production']:
        path = resource['path'].lower()
        title = resource['title'].lower()
        
        for year in range(7, 14):  # Y7-Y13
            if f'y{year}' in path or f'year {year}' in title or f'year-{year}' in path:
                year_levels[f'Year {year}'].append(resource)
                break

print("Resources by year level:\n")
for year in [f'Year {i}' for i in range(7, 14)]:
    count = len(year_levels.get(year, []))
    bar = '█' * (count // 10)
    print(f"{year:10} {count:4} {bar}")

# === ANALYSIS 6: Cultural Integration Opportunities ===
print("\n\n🌿 ANALYSIS 6: CULTURAL INTEGRATION")
print("-" * 70)

cultural_stats = {
    'has_cultural': 0,
    'missing_cultural': 0,
    'high_priority_missing': []
}

for resource in approved:
    if resource['in_production']:
        if resource['checks'].get('cultural', False):
            cultural_stats['has_cultural'] += 1
        else:
            cultural_stats['missing_cultural'] += 1
            if resource['score'] >= 85 and resource['links'] > 5:
                cultural_stats['high_priority_missing'].append(resource)

print(f"Production files WITH cultural context: {cultural_stats['has_cultural']}")
print(f"Production files WITHOUT: {cultural_stats['missing_cultural']}")
print(f"\nHigh-priority files to add cultural context ({len(cultural_stats['high_priority_missing'])}):\n")

for i, resource in enumerate(cultural_stats['high_priority_missing'][:5], 1):
    print(f"{i}. {resource['title'][:50]}")
    print(f"   Score: {resource['score']}% | Very connected ({resource['links']} links)")
    print()

# === STRATEGIC RECOMMENDATIONS ===
print("\n" + "=" * 70)
print("🎯 STRATEGIC RECOMMENDATIONS")
print("=" * 70)

print("\n📌 PRIORITY 1: Restore Hidden Gems (Immediate Impact)")
print(f"   • {len(hidden_gems)} high-quality archived files")
print(f"   • Action: Restore top 20 to production")
print(f"   • Time: 2 hours")
print(f"   • Impact: Add excellent content immediately")

print("\n📌 PRIORITY 2: Surface Orphaned Gems (Discoverability)")
print(f"   • {len(orphaned)} excellent pages hard to find")
print(f"   • Action: Add to homepage/navigation")
print(f"   • Time: 1 hour")
print(f"   • Impact: Make great content discoverable")

print("\n📌 PRIORITY 3: Fill Subject Gaps")
gaps = [s for s, r in subjects.items() if len(r) < 50]
print(f"   • Subjects needing more: {', '.join(gaps)}")
print(f"   • Action: Mine archives for these subjects")
print(f"   • Time: 3 hours")
print(f"   • Impact: Balanced curriculum")

print("\n📌 PRIORITY 4: Add Cultural Context")
print(f"   • {len(cultural_stats['high_priority_missing'])} high-priority files")
print(f"   • Action: Add whakataukī & cultural notes")
print(f"   • Time: 2 hours")
print(f"   • Impact: Consistent cultural integration")

print("\n📌 PRIORITY 5: Build Learning Paths")
print(f"   • {len([r for r in relationships if 'lesson' in r['from']])} lesson sequences")
print(f"   • Action: Use prerequisites to create paths")
print(f"   • Time: 4 hours")
print(f"   • Impact: Guided student journeys")

# Save detailed analysis
with open('strategic-analysis-results.json', 'w') as f:
    json.dump({
        'hidden_gems': hidden_gems[:50],
        'hub_pages': [(hub[0]['path'], hub[1]) for hub in top_hubs[:20]],
        'orphaned_gems': [(r[0]['path'], r[1]) for r in orphaned[:20]],
        'subject_coverage': {k: len(v) for k, v in subjects.items()},
        'year_coverage': {k: len(v) for k, v in year_levels.items()},
        'cultural_opportunities': [r['path'] for r in cultural_stats['high_priority_missing'][:20]]
    }, f, indent=2)

print("\n💾 Detailed analysis saved to: strategic-analysis-results.json")
print("\n" + "=" * 70)
print("✅ STRATEGIC AUDIT COMPLETE!")
print("=" * 70)
print("\n🎯 Use these insights to prioritize next improvements!\n")

