#!/usr/bin/env python3
"""
SYSTEMATIC GRAPHRAG MINING - Find ALL Complete Units
Query GraphRAG for complete units and create organization roadmap
"""

from supabase import create_client
from collections import defaultdict
import json

print("⛏️ SYSTEMATIC GRAPHRAG MINING - COMPLETE UNITS")
print("=" * 80)

supabase = create_client(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
)

# Get ALL lessons (not just 1000)
print("\n📊 Getting comprehensive lesson list...")
all_lessons = []
offset = 0
batch_size = 1000

while True:
    result = supabase.table('resources')\
        .select('title, path, subject')\
        .eq('type', 'lesson')\
        .range(offset, offset + batch_size - 1)\
        .execute()
    
    if not result.data:
        break
    
    all_lessons.extend(result.data)
    offset += batch_size
    print(f"   Retrieved {len(all_lessons)} lessons...")
    
    if len(result.data) < batch_size:
        break

print(f"\n✅ Total lessons retrieved: {len(all_lessons)}")

# Deduplicate by path (remove backup versions)
unique_lessons = {}
for lesson in all_lessons:
    path = lesson.get('path', '')
    # Skip backups, dist copies
    if 'backup' in path.lower() or path.startswith('dist/') or path.startswith('backups/'):
        continue
    
    # Use path as key to deduplicate
    if path not in unique_lessons:
        unique_lessons[path] = lesson

print(f"✅ Unique lessons (excluding backups): {len(unique_lessons)}")

# Categorize by unit patterns
units_catalog = defaultdict(lambda: defaultdict(list))

for path, lesson in unique_lessons.items():
    title = lesson.get('title', '')
    subject = lesson.get('subject', 'General')
    
    # Detect unit type
    if 'Y7' in title or '/y7-' in path.lower():
        units_catalog['Year 7'][subject].append(lesson)
    elif 'Y8' in title or '/y8-' in path.lower():
        units_catalog['Year 8'][subject].append(lesson)
    elif 'Y9' in title or '/y9-' in path.lower():
        units_catalog['Year 9'][subject].append(lesson)
    elif 'Y10' in title or '/y10-' in path.lower():
        units_catalog['Year 10'][subject].append(lesson)
    elif 'Unit 1' in title or '/unit-1-' in path or 'unit 1' in path.lower():
        units_catalog['Unit 1'][subject].append(lesson)
    elif 'Unit 2' in title or '/unit-2-' in path:
        units_catalog['Unit 2'][subject].append(lesson)
    elif 'Unit 3' in title or '/unit-3-' in path:
        units_catalog['Unit 3'][subject].append(lesson)
    elif 'Unit 4' in title or '/unit-4-' in path:
        units_catalog['Unit 4'][subject].append(lesson)
    elif 'Unit 5' in title or '/unit-5-' in path:
        units_catalog['Unit 5'][subject].append(lesson)
    elif 'Unit 6' in title or '/unit-6-' in path:
        units_catalog['Unit 6'][subject].append(lesson)
    elif 'Unit 7' in title or '/unit-7-' in path:
        units_catalog['Unit 7'][subject].append(lesson)
    elif 'statistic' in title.lower() or 'statistic' in path.lower():
        units_catalog['Statistics'][subject].append(lesson)
    elif 'algebra' in title.lower() or 'algebra' in path.lower():
        units_catalog['Algebra'][subject].append(lesson)
    elif 'ecosystem' in title.lower() or 'ecology' in title.lower():
        units_catalog['Ecosystems'][subject].append(lesson)
    elif 'literacy' in title.lower() and 'writer' not in title.lower():
        units_catalog['Literacy'][subject].append(lesson)
    elif 'walker' in title.lower() or 'walker' in path.lower():
        units_catalog['Walker Unit'][subject].append(lesson)

# Display results
print("\n" + "=" * 80)
print("📚 COMPLETE UNITS CATALOG")
print("=" * 80)

for unit_name in sorted(units_catalog.keys()):
    total_lessons = sum(len(lessons) for lessons in units_catalog[unit_name].values())
    if total_lessons >= 5:
        print(f"\n{unit_name}: {total_lessons} lessons")
        for subject in sorted(units_catalog[unit_name].keys()):
            lessons = units_catalog[unit_name][subject]
            print(f"   {subject}: {len(lessons)} lessons")

# Save catalog
output = {
    'total_unique_lessons': len(unique_lessons),
    'units_found': {unit: {subj: len(lessons) for subj, lessons in subjects.items()} 
                    for unit, subjects in units_catalog.items()},
    'full_catalog': {unit: {subj: [{'title': l['title'], 'path': l['path']} for l in lessons]
                           for subj, lessons in subjects.items()}
                    for unit, subjects in units_catalog.items()}
}

with open('graphrag-units-catalog.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\n💾 Complete catalog saved to: graphrag-units-catalog.json")
print(f"📊 Total unique lessons cataloged: {len(unique_lessons)}")
print(f"📚 Total units found: {len(units_catalog)}")
print("\n✅ Ready to organize systematically!")

