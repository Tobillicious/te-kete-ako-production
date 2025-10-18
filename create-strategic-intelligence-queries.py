#!/usr/bin/env python3
"""
STRATEGIC INTELLIGENCE QUERIES - AI-Powered Platform Insights
Create intelligent queries that analyze the entire platform
"""

from supabase import create_client
from collections import defaultdict
import json

print("🧠 STRATEGIC INTELLIGENCE QUERIES - Super Intelligence Activated")
print("=" * 80)

supabase = create_client(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
)

print("\n" + "=" * 80)
print("🎯 QUERY 1: CONTENT GAP ANALYSIS")
print("=" * 80)

# Find year levels and subjects with low content
print("\n📊 Analyzing content distribution...")

# Get all resources
result = supabase.table('resources')\
    .select('subject, type, path, title')\
    .execute()

content_map = defaultdict(lambda: defaultdict(int))
for resource in result.data:
    subject = resource.get('subject', 'Unknown')
    # Extract year level from path or title
    path = resource.get('path', '')
    title = resource.get('title', '')
    year = 'Unspecified'
    for y in ['Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12', 'Y13', 'y7', 'y8', 'y9', 'y10']:
        if y in path or y in title:
            year = y.upper()
            break
    content_map[subject][year] += 1

print("\n📊 Content Coverage by Subject and Year:")
for subject in sorted(content_map.keys()):
    total = sum(content_map[subject].values())
    print(f"\n{subject}: {total} resources")
    for year in sorted(content_map[subject].keys()):
        count = content_map[subject][year]
        if year != 'Unspecified':
            print(f"   Year {year}: {count} resources")

print("\n" + "=" * 80)
print("🎯 QUERY 2: CULTURAL INTEGRATION GAPS")
print("=" * 80)

result = supabase.table('resources')\
    .select('cultural_integration, type')\
    .execute()

cultural_map = defaultdict(int)
for resource in result.data:
    level = resource.get('cultural_integration', 'unknown')
    cultural_map[level] += 1

print("\n🌺 Cultural Integration Levels:")
total = sum(cultural_map.values())
for level, count in sorted(cultural_map.items(), key=lambda x: -x[1]):
    pct = (count / total * 100) if total > 0 else 0
    print(f"   {level}: {count} resources ({pct:.1f}%)")

# Find low integration resources
low_integration = supabase.table('resources')\
    .select('title, type, subject')\
    .eq('cultural_integration', 'low')\
    .limit(10)\
    .execute()

print(f"\n⚠️  {len(low_integration.data)} resources with low cultural integration (showing 10):")
for res in low_integration.data[:10]:
    print(f"   - {res['title']} ({res['type']}, {res.get('subject', 'N/A')})")

print("\n" + "=" * 80)
print("🎯 QUERY 3: ORPHANED CONTENT (No Unit Association)")
print("=" * 80)

# Find lessons without clear unit association
result = supabase.table('resources')\
    .select('title, path, subject')\
    .eq('type', 'lesson')\
    .execute()

orphaned = []
for lesson in result.data:
    path = lesson.get('path', '')
    # Check if path contains unit indicators
    if not any(indicator in path.lower() for indicator in ['unit-', 'y7-', 'y8-', 'y9-', 'y10-', '/units/']):
        orphaned.append(lesson)

print(f"\n📊 Found {len(orphaned)} potentially orphaned lessons")
print(f"   (Lessons not clearly associated with a unit)")

if orphaned:
    subjects_orphaned = defaultdict(int)
    for lesson in orphaned:
        subjects_orphaned[lesson.get('subject', 'Unknown')] += 1
    
    print("\n   By subject:")
    for subject, count in sorted(subjects_orphaned.items(), key=lambda x: -x[1]):
        print(f"   - {subject}: {count} orphaned lessons")

print("\n" + "=" * 80)
print("🎯 QUERY 4: ASSESSMENT COVERAGE")
print("=" * 80)

assessments = supabase.table('resources')\
    .select('subject, path, title')\
    .eq('type', 'assessment')\
    .execute()

print(f"\n📊 Total assessments: {len(assessments.data)}")

assessment_map = defaultdict(lambda: defaultdict(int))
for assess in assessments.data:
    subject = assess.get('subject', 'Unknown')
    path = assess.get('path', '')
    title = assess.get('title', '')
    year = 'Unspecified'
    for y in ['Y7', 'Y8', 'Y9', 'Y10']:
        if y in path or y in title:
            year = y
            break
    assessment_map[subject][year] += 1

print("\n   By subject:")
for subject in sorted(assessment_map.keys()):
    total = sum(assessment_map[subject].values())
    print(f"   {subject}: {total} assessments")

print("\n" + "=" * 80)
print("🎯 QUERY 5: INTERACTIVE & GAME CONTENT")
print("=" * 80)

games = supabase.table('resources')\
    .select('title, subject')\
    .eq('type', 'game')\
    .execute()

interactive = supabase.table('resources')\
    .select('title, subject')\
    .eq('type', 'interactive')\
    .execute()

print(f"\n🎮 Games: {len(games.data)}")
print(f"💻 Interactive resources: {len(interactive.data)}")
print(f"🎯 Total engaging content: {len(games.data) + len(interactive.data)}")

print("\n" + "=" * 80)
print("🎯 STRATEGIC IMPROVEMENT PRIORITIES")
print("=" * 80)

priorities = []

# Priority 1: Low cultural integration
low_cultural_count = cultural_map.get('low', 0)
if low_cultural_count > 100:
    priorities.append(f"1. CULTURAL ENHANCEMENT: {low_cultural_count} resources need cultural enrichment")

# Priority 2: Orphaned content
if len(orphaned) > 50:
    priorities.append(f"2. CONTENT ORGANIZATION: {len(orphaned)} orphaned lessons need unit integration")

# Priority 3: Year level gaps
year_counts = defaultdict(int)
for subject_data in content_map.values():
    for year, count in subject_data.items():
        if year != 'Unspecified':
            year_counts[year] += count

low_years = [year for year, count in year_counts.items() if count < 50]
if low_years:
    priorities.append(f"3. YEAR LEVEL GAPS: Years {', '.join(low_years)} need more content")

# Priority 4: Assessment coverage
if len(assessments.data) < 100:
    priorities.append(f"4. ASSESSMENT EXPANSION: Only {len(assessments.data)} assessments for {len(content_map)} subjects")

print("\n🎯 TOP PRIORITIES:")
for priority in priorities:
    print(f"\n   {priority}")

# Save strategic intelligence report
report = {
    'generated_at': '2025-10-18',
    'total_resources': len(result.data),
    'content_gaps': {
        'orphaned_lessons': len(orphaned),
        'low_cultural_integration': low_cultural_count,
        'assessment_count': len(assessments.data),
        'year_level_gaps': low_years
    },
    'priorities': priorities,
    'content_distribution': {k: dict(v) for k, v in content_map.items()},
    'cultural_levels': dict(cultural_map)
}

with open('strategic-intelligence-report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("\n" + "=" * 80)
print("💾 STRATEGIC REPORT SAVED")
print("=" * 80)
print("\n✅ strategic-intelligence-report.json created")
print("🧠 AI-powered platform analysis: COMPLETE")
print("🎯 Actionable priorities identified")
print("\n" + "=" * 80)
print("🚀 SUPER INTELLIGENCE: ACTIVE")
print("=" * 80)

