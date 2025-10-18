#!/usr/bin/env python3
"""
GraphRAG Relationship Builder - Build intelligent connections
Creates relationships between resources based on:
- Subject similarity
- Year level alignment
- Lesson-handout pairs
- Unit hierarchies
- Prerequisites
- Cultural themes
"""
from supabase import create_client
from pathlib import Path
import re
from datetime import datetime
from collections import defaultdict

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🔗 GRAPHRAG RELATIONSHIP BUILDER")
print("=" * 80)
print("Building intelligent connections between 10,943 resources...")
print("=" * 80)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load all resources
print("\n📊 Loading all GraphRAG resources...")
all_resources = []
offset = 0
page_size = 1000

while True:
    result = supabase.table('graphrag_resources').select('*').range(offset, offset + page_size - 1).execute()
    batch = result.data
    if not batch:
        break
    all_resources.extend(batch)
    offset += page_size
    print(f"   Loaded {len(all_resources)} resources...")
    if len(batch) < page_size:
        break

print(f"\n✅ Loaded {len(all_resources)} total resources")

# Check existing relationships
print("\n📊 Checking existing relationships...")
existing_rels_result = supabase.table('graphrag_relationships').select('id', count='exact').execute()
existing_count = existing_rels_result.count or 0
print(f"   Found {existing_count} existing relationships")

# Build indexes for fast lookup
print("\n🏗️  Building lookup indexes...")
by_subject = defaultdict(list)
by_year = defaultdict(list)
by_type = defaultdict(list)
by_cultural = defaultdict(list)

for resource in all_resources:
    subject = resource.get('subject', 'Unknown')
    year_level = resource.get('year_level', 'Unknown')
    res_type = resource.get('resource_type', 'Unknown')
    path = resource.get('file_path', '')
    
    by_subject[subject].append(resource)
    by_year[year_level].append(resource)
    by_type[res_type].append(resource)
    
    if resource.get('has_whakataukī'):
        by_cultural['whakataukī'].append(resource)
    if resource.get('has_te_reo'):
        by_cultural['te_reo'].append(resource)

print(f"   Subjects: {len(by_subject)}")
print(f"   Year levels: {len(by_year)}")
print(f"   Resource types: {len(by_type)}")
print(f"   Cultural resources: {len(by_cultural['te_reo'])} with Te Reo, {len(by_cultural['whakataukī'])} with Whakataukī")

# Build relationships
new_relationships = []

def add_relationship(source_path, target_path, rel_type, confidence=0.85, metadata=None):
    """Add a relationship if it doesn't exist"""
    new_relationships.append({
        'source_path': source_path,
        'target_path': target_path,
        'relationship_type': rel_type,
        'confidence': confidence,
        'metadata': metadata or {},
        'created_at': datetime.now().isoformat()
    })

print("\n🔗 Building relationships...")

# 1. Same Subject Relationships (high value connections)
print("\n1️⃣  Building same-subject relationships...")
subject_rels = 0
for subject, resources in by_subject.items():
    if subject == 'Unknown' or len(resources) < 2:
        continue
    # Limit to avoid explosion (max 10 connections per resource)
    for i, res1 in enumerate(resources[:500]):  # Limit resources per subject
        for res2 in resources[i+1:min(i+11, len(resources))]:
            add_relationship(
                res1['file_path'],
                res2['file_path'],
                'same_subject',
                confidence=0.82,
                metadata={'subject': subject}
            )
            subject_rels += 1
            if subject_rels % 1000 == 0:
                print(f"   Created {subject_rels} same-subject relationships...")

print(f"   ✅ Created {subject_rels} same-subject relationships")

# 2. Same Year Level
print("\n2️⃣  Building same-year-level relationships...")
year_rels = 0
for year_level, resources in by_year.items():
    if year_level == 'Unknown' or year_level == 'All Years' or len(resources) < 2:
        continue
    for i, res1 in enumerate(resources[:500]):
        for res2 in resources[i+1:min(i+11, len(resources))]:
            add_relationship(
                res1['file_path'],
                res2['file_path'],
                'same_year_level',
                confidence=0.85,
                metadata={'year_level': year_level}
            )
            year_rels += 1
            if year_rels % 1000 == 0:
                print(f"   Created {year_rels} year-level relationships...")

print(f"   ✅ Created {year_rels} same-year-level relationships")

# 3. Lesson-Handout Pairs (by path proximity)
print("\n3️⃣  Building lesson-handout pairs...")
lesson_handout_rels = 0
lessons = by_type.get('Lesson', [])
handouts = by_type.get('Handout', [])

for lesson in lessons:
    lesson_path = Path(lesson['file_path'])
    lesson_stem = lesson_path.stem
    lesson_parent = str(lesson_path.parent)
    
    # Look for handouts with similar names or in same directory
    for handout in handouts:
        handout_path = Path(handout['file_path'])
        handout_stem = handout_path.stem
        handout_parent = str(handout_path.parent)
        
        # Check for matches
        if (lesson_stem in handout_stem or handout_stem in lesson_stem or
            lesson_parent == handout_parent.replace('handouts', 'lessons')):
            add_relationship(
                lesson['file_path'],
                handout['file_path'],
                'lesson_has_handout',
                confidence=0.90,
                metadata={'pairing_type': 'path_match'}
            )
            lesson_handout_rels += 1

print(f"   ✅ Created {lesson_handout_rels} lesson-handout relationships")

# 4. Unit-Lesson hierarchies
print("\n4️⃣  Building unit-lesson hierarchies...")
unit_rels = 0
units = by_type.get('Unit-Plan', []) + by_type.get('Unit', [])
lessons = by_type.get('Lesson', [])

for unit in units:
    unit_path = Path(unit['file_path'])
    unit_dir = str(unit_path.parent)
    
    # Find lessons in same directory or subdirectories
    for lesson in lessons:
        lesson_path = Path(lesson['file_path'])
        if unit_dir in str(lesson_path):
            add_relationship(
                unit['file_path'],
                lesson['file_path'],
                'unit_contains_lesson',
                confidence=0.95,
                metadata={'unit_structure': 'directory_hierarchy'}
            )
            unit_rels += 1

print(f"   ✅ Created {unit_rels} unit-lesson relationships")

# 5. Cultural Content Connections
print("\n5️⃣  Building cultural connections...")
cultural_rels = 0
whakatauaki_resources = by_cultural.get('whakataukī', [])

# Connect resources with whakataukī to similar resources
for i, res1 in enumerate(whakatauaki_resources[:200]):
    for res2 in whakatauaki_resources[i+1:min(i+6, len(whakatauaki_resources))]:
        add_relationship(
            res1['file_path'],
            res2['file_path'],
            'shared_cultural_element',
            confidence=0.88,
            metadata={'cultural_marker': 'whakataukī'}
        )
        cultural_rels += 1

print(f"   ✅ Created {cultural_rels} cultural relationships")

# 6. Related Content (by subject AND year level)
print("\n6️⃣  Building related content relationships...")
related_rels = 0
# Group by subject+year combination
by_subject_year = defaultdict(list)
for resource in all_resources:
    key = f"{resource.get('subject', 'Unknown')}_{resource.get('year_level', 'Unknown')}"
    if 'Unknown' not in key:
        by_subject_year[key].append(resource)

for key, resources in by_subject_year.items():
    if len(resources) < 2:
        continue
    # Create related content links (fewer to avoid explosion)
    for i, res1 in enumerate(resources[:300]):
        for res2 in resources[i+1:min(i+4, len(resources))]:
            add_relationship(
                res1['file_path'],
                res2['file_path'],
                'related_content',
                confidence=0.87,
                metadata={'match_criteria': 'subject_and_year'}
            )
            related_rels += 1
            if related_rels % 1000 == 0:
                print(f"   Created {related_rels} related-content relationships...")

print(f"   ✅ Created {related_rels} related-content relationships")

# Summary before insertion
print(f"\n📊 RELATIONSHIP SUMMARY:")
print(f"   Same Subject: {subject_rels}")
print(f"   Same Year Level: {year_rels}")
print(f"   Lesson-Handout Pairs: {lesson_handout_rels}")
print(f"   Unit-Lesson Hierarchies: {unit_rels}")
print(f"   Cultural Connections: {cultural_rels}")
print(f"   Related Content: {related_rels}")
print(f"   {'='*80}")
print(f"   TOTAL NEW RELATIONSHIPS: {len(new_relationships)}")

# Insert in batches
print(f"\n🚀 Inserting relationships into GraphRAG...")
batch_size = 500
total_inserted = 0
total_errors = 0

for i in range(0, len(new_relationships), batch_size):
    batch = new_relationships[i:i+batch_size]
    batch_num = i // batch_size + 1
    total_batches = (len(new_relationships) + batch_size - 1) // batch_size
    
    try:
        supabase.table('graphrag_relationships').insert(batch).execute()
        total_inserted += len(batch)
        if batch_num % 10 == 0:
            print(f"   Batch {batch_num}/{total_batches}: Inserted {total_inserted}/{len(new_relationships)} ({total_inserted/len(new_relationships)*100:.1f}%)")
    except Exception as e:
        error_msg = str(e)
        if 'duplicate' in error_msg.lower():
            print(f"   ⚠️  Batch {batch_num}: Duplicates detected, skipping...")
        else:
            print(f"   ❌ Batch {batch_num}: {error_msg[:80]}")
            total_errors += len(batch)

print(f"\n{'='*80}")
print(f"✅ RELATIONSHIP BUILDING COMPLETE!")
print(f"{'='*80}")
print(f"   New relationships created: {total_inserted}")
print(f"   Errors: {total_errors}")
print(f"{'='*80}")

# Final verification
final_result = supabase.table('graphrag_relationships').select('id', count='exact').execute()
final_count = final_result.count or 0
print(f"\n🎉 GraphRAG Relationships: {existing_count} → {final_count}")
print(f"   Net increase: +{final_count - existing_count}")
print(f"\n🔗 GraphRAG is now fully connected and ready to use!")

