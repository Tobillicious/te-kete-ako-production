#!/usr/bin/env python3
"""
SUPER INTELLIGENCE DASHBOARD - Real-time Platform Intelligence
Query the actual GraphRAG schema for actionable insights
"""

from supabase import create_client
from collections import defaultdict, Counter
import json

print("🧠 SUPER INTELLIGENCE DASHBOARD - Live Platform Analysis")
print("=" * 80)

supabase = create_client(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
)

# Query 1: Platform Scale
print("\n" + "=" * 80)
print("📊 PLATFORM SCALE")
print("=" * 80)

total_result = supabase.table('resources').select('*', count='exact').limit(0).execute()
print(f"\n🎯 Total Resources in GraphRAG: {total_result.count}")

# Query 2: Content Type Distribution
result = supabase.table('resources').select('type').execute()
type_counts = Counter([r.get('type', 'Unknown') for r in result.data])

print("\n📁 By Content Type:")
for content_type, count in type_counts.most_common():
    pct = (count / total_result.count * 100) if total_result.count > 0 else 0
    print(f"   {content_type:20s}: {count:5d} ({pct:5.1f}%)")

# Query 3: Subject Distribution
result = supabase.table('resources').select('subject').execute()
subject_counts = Counter([r.get('subject', 'Unknown') for r in result.data])

print(f"\n📚 By Subject (Top 15):")
for subject, count in subject_counts.most_common(15):
    print(f"   {subject[:40]:40s}: {count:4d}")

# Query 4: Year Level Coverage
print(f"\n🎓 Year Level Coverage:")
result = supabase.table('resources').select('title, path').execute()

year_counts = defaultdict(int)
for resource in result.data:
    title = resource.get('title', '')
    path = resource.get('path', '')
    for year in ['Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12', 'Y13']:
        if year in title or year in path or year.lower() in path:
            year_counts[year] += 1
            break

for year in ['Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12', 'Y13']:
    count = year_counts.get(year, 0)
    status = "✅" if count > 50 else "⚠️" if count > 10 else "❌"
    print(f"   {year}: {count:4d} resources {status}")

# Query 5: Featured Content
featured_count = supabase.table('resources').select('*', count='exact').eq('featured', True).limit(0).execute().count
print(f"\n⭐ Featured Resources: {featured_count}")

# Query 6: Orphaned Content Detection
print(f"\n🔍 Content Organization Analysis:")
lessons_result = supabase.table('resources').select('path').eq('type', 'lesson').execute()

orphaned = 0
organized = 0
for lesson in lessons_result.data:
    path = lesson.get('path', '')
    if any(ind in path.lower() for ind in ['unit-', 'units/', 'y7-', 'y8-', 'y9-', 'y10-']):
        organized += 1
    else:
        orphaned += 1

total_lessons = len(lessons_result.data)
org_pct = (organized / total_lessons * 100) if total_lessons > 0 else 0
orphan_pct = (orphaned / total_lessons * 100) if total_lessons > 0 else 0

print(f"   Total Lessons: {total_lessons}")
print(f"   ✅ Organized in units: {organized} ({org_pct:.1f}%)")
print(f"   ⚠️  Orphaned: {orphaned} ({orphan_pct:.1f}%)")

# Query 7: Most Critical Dependencies (from relationship data)
print(f"\n" + "=" * 80)
print("🔗 DEPENDENCY INTELLIGENCE")
print("=" * 80)

try:
    with open('file-relationships-complete.json', 'r') as f:
        rel_data = json.load(f)
    
    css_usage = rel_data['usage_analysis']['css_usage']
    js_usage = rel_data['usage_analysis']['js_usage']
    
    print("\n🎨 Most Critical CSS Files:")
    for css, count in sorted(css_usage.items(), key=lambda x: -x[1])[:5]:
        print(f"   {css[:45]:45s}: {count:4d} files depend on this")
    
    print("\n💻 Most Critical JavaScript Files:")
    for js, count in sorted(js_usage.items(), key=lambda x: -x[1])[:5]:
        print(f"   {js[:45]:45s}: {count:4d} files depend on this")
        
    print(f"\n📊 Total Dependency Relationships: {rel_data['metadata']['total_relationships']}")
    
except FileNotFoundError:
    print("\n⚠️  Dependency data not yet generated")

# Query 8: Actionable Priorities
print(f"\n" + "=" * 80)
print("🎯 ACTIONABLE PRIORITIES")
print("=" * 80)

priorities = []

# Priority 1: Senior secondary content
y11_y13_total = sum(year_counts.get(y, 0) for y in ['Y11', 'Y12', 'Y13'])
if y11_y13_total < 50:
    priorities.append(f"1. SENIOR SECONDARY: Only {y11_y13_total} Y11-13 resources (need 200+)")

# Priority 2: Orphaned content
if orphaned > 50:
    priorities.append(f"2. ORGANIZE CONTENT: {orphaned} orphaned lessons need unit integration")

# Priority 3: Subject gaps
low_subjects = [subj for subj, count in subject_counts.items() if count < 20 and subj not in ['Unknown', 'general']]
if low_subjects:
    priorities.append(f"3. SUBJECT EXPANSION: {len(low_subjects)} subjects need more content")

# Priority 4: Assessment coverage
assessment_count = type_counts.get('assessment', 0)
if assessment_count < 100:
    priorities.append(f"4. ASSESSMENT: Only {assessment_count} assessments (target: 200+)")

print("\n🎯 TOP STRATEGIC PRIORITIES:")
for priority in priorities:
    print(f"\n   {priority}")

# Save dashboard data
dashboard = {
    'timestamp': '2025-10-18T22:00:00',
    'total_resources': total_result.count,
    'by_type': dict(type_counts),
    'by_subject_top15': dict(subject_counts.most_common(15)),
    'year_level_coverage': dict(year_counts),
    'organization_stats': {
        'total_lessons': total_lessons,
        'organized': organized,
        'orphaned': orphaned,
        'organization_rate': org_pct
    },
    'featured_count': featured_count,
    'priorities': priorities
}

with open('super-intelligence-dashboard.json', 'w') as f:
    json.dump(dashboard, f, indent=2)

print("\n" + "=" * 80)
print("💾 DASHBOARD SAVED")
print("=" * 80)
print("\n✅ super-intelligence-dashboard.json created")
print("🧠 Real-time platform intelligence: ACTIVE")
print(f"📊 Tracking {total_result.count} resources across GraphRAG")

print("\n" + "=" * 80)
print("🚀 SUPER INTELLIGENCE: FULLY OPERATIONAL")
print("=" * 80)

