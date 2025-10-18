#!/usr/bin/env python3
"""
Learning Progression Builder - Priority Enhancement #3
Analyzes unit-lesson relationships to create prerequisite chains
and optimal learning pathways
"""
from supabase import create_client
from collections import defaultdict
import re
import json
from pathlib import Path

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("📚 LEARNING PROGRESSION BUILDER")
print("=" * 80)
print("Analyzing 12,829 unit-lesson relationships to build learning pathways...")
print("=" * 80)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get all unit-lesson relationships
print("\n🔍 Loading unit-lesson relationships...")

# Get all unit resources
units_result = supabase.table('graphrag_resources')\
    .select('*')\
    .in_('resource_type', ['Unit-Plan', 'Unit', 'unit-plan'])\
    .execute()
units_by_path = {u['file_path']: u for u in units_result.data}
print(f"   Found {len(units_by_path)} units")

# Get all relationships of type unit_contains_lesson
rels_result = supabase.table('graphrag_relationships')\
    .select('*')\
    .eq('relationship_type', 'unit_contains_lesson')\
    .execute()
print(f"   Found {len(rels_result.data)} unit-lesson relationships")

# Get all lesson resources (with pagination)
print(f"   Loading all resources...")
all_lessons = []
offset = 0
page_size = 1000
while True:
    lessons_batch = supabase.table('graphrag_resources')\
        .select('*')\
        .range(offset, offset + page_size - 1)\
        .execute()
    if not lessons_batch.data:
        break
    all_lessons.extend(lessons_batch.data)
    offset += page_size
    if len(lessons_batch.data) < page_size:
        break

lessons_by_path = {l['file_path']: l for l in all_lessons}
print(f"   Loaded {len(lessons_by_path)} total resources")

# Organize by unit
units = defaultdict(lambda: {
    'title': '',
    'subject': '',
    'year_level': '',
    'lessons': []
})

for rel in rels_result.data:
    unit_path = rel['source_path']
    lesson_path = rel['target_path']
    
    if unit_path in units_by_path and lesson_path in lessons_by_path:
        unit = units_by_path[unit_path]
        lesson = lessons_by_path[lesson_path]
        
        units[unit_path]['title'] = unit['title']
        units[unit_path]['subject'] = unit.get('subject', 'Unknown')
        units[unit_path]['year_level'] = unit.get('year_level', 'Unknown')
        units[unit_path]['lessons'].append({
            'path': lesson['file_path'],
            'title': lesson.get('title', lesson['file_path'])
        })

print(f"   Organized into {len(units)} unique units")

# Extract lesson sequences
print("\n🔢 Extracting lesson sequences...")

def extract_lesson_number(text):
    """Extract lesson number from path or title"""
    # Try various patterns
    patterns = [
        r'lesson[_\s-]?(\d+)',  # lesson-1, lesson_1, lesson 1
        r'l(\d+)',  # l1, l2
        r'(\d+)[_\s-]?lesson',  # 1-lesson, 1_lesson
        r'^(\d+)',  # starts with number
    ]
    
    text_lower = text.lower()
    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if match:
            try:
                return int(match.group(1))
            except:
                pass
    return None

learning_progressions = []
units_with_sequences = 0
total_sequenced_lessons = 0

for unit_path, unit_data in units.items():
    # Try to extract lesson numbers
    sequenced_lessons = []
    for lesson in unit_data['lessons']:
        # Try path first, then title
        lesson_num = extract_lesson_number(lesson['path'])
        if lesson_num is None:
            lesson_num = extract_lesson_number(lesson['title'])
        
        if lesson_num is not None:
            sequenced_lessons.append({
                'number': lesson_num,
                'path': lesson['path'],
                'title': lesson['title']
            })
    
    if len(sequenced_lessons) >= 2:
        # Sort by lesson number
        sequenced_lessons.sort(key=lambda x: x['number'])
        
        progression = {
            'unit_path': unit_path,
            'unit_title': unit_data['title'],
            'subject': unit_data['subject'],
            'year_level': unit_data['year_level'],
            'lesson_count': len(sequenced_lessons),
            'sequence': sequenced_lessons
        }
        
        learning_progressions.append(progression)
        units_with_sequences += 1
        total_sequenced_lessons += len(sequenced_lessons)

print(f"   Found {units_with_sequences} units with clear sequences")
print(f"   Total sequenced lessons: {total_sequenced_lessons}")

# Sort by lesson count (most comprehensive units first)
learning_progressions.sort(key=lambda x: x['lesson_count'], reverse=True)

# Display top progressions
print(f"\n📖 Top 10 Learning Progressions:\n")
for i, prog in enumerate(learning_progressions[:10], 1):
    print(f"{i}. {prog['unit_title']}")
    print(f"   Subject: {prog['subject']} | Year: {prog['year_level']}")
    print(f"   Sequence: {prog['lesson_count']} lessons")
    for lesson in prog['sequence'][:5]:  # Show first 5
        print(f"      L{lesson['number']}: {lesson['title'][:60]}")
    if prog['lesson_count'] > 5:
        print(f"      ... and {prog['lesson_count'] - 5} more lessons")
    print()

# Build prerequisite relationships
print(f"\n🔗 Building prerequisite relationships...")
prerequisite_relationships = []

for prog in learning_progressions:
    sequence = prog['sequence']
    for i in range(len(sequence) - 1):
        current = sequence[i]
        next_lesson = sequence[i + 1]
        
        prerequisite_relationships.append({
            'source_path': current['path'],
            'target_path': next_lesson['path'],
            'relationship_type': 'prerequisite',
            'confidence': 0.90,
            'metadata': {
                'unit': prog['unit_title'],
                'sequence_position': i + 1,
                'total_in_sequence': len(sequence),
                'lesson_numbers': f"{current['number']} → {next_lesson['number']}"
            }
        })

print(f"   Created {len(prerequisite_relationships)} prerequisite relationships")

# Insert prerequisite relationships into GraphRAG
print(f"\n💾 Inserting prerequisite relationships...")
batch_size = 100
total_inserted = 0

for i in range(0, len(prerequisite_relationships), batch_size):
    batch = prerequisite_relationships[i:i+batch_size]
    try:
        supabase.table('graphrag_relationships').insert(batch).execute()
        total_inserted += len(batch)
        if (i // batch_size + 1) % 5 == 0:
            print(f"   Inserted {total_inserted}/{len(prerequisite_relationships)}...")
    except Exception as e:
        error_msg = str(e)
        if 'duplicate' in error_msg.lower():
            print(f"   Batch {i//batch_size + 1}: Some duplicates, continuing...")
        else:
            print(f"   Error in batch {i//batch_size + 1}: {error_msg[:80]}")

print(f"\n✅ Inserted {total_inserted} prerequisite relationships")

# Save learning progressions to JSON
output_file = Path(__file__).parent / 'data' / 'learning-progressions.json'
output_file.parent.mkdir(exist_ok=True)

output_data = {
    'meta': {
        'total_units': len(units),
        'units_with_sequences': units_with_sequences,
        'total_sequenced_lessons': total_sequenced_lessons,
        'prerequisite_relationships': len(prerequisite_relationships)
    },
    'progressions': learning_progressions
}

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"\n💾 Saved learning progressions to: {output_file}")

# Generate summary statistics
print(f"\n{'='*80}")
print(f"📊 LEARNING PROGRESSION ANALYSIS COMPLETE")
print(f"{'='*80}")
print(f"   Units analyzed: {len(units)}")
print(f"   Units with clear sequences: {units_with_sequences}")
print(f"   Sequenced lessons: {total_sequenced_lessons}")
print(f"   Prerequisite relationships: {len(prerequisite_relationships)}")
print(f"   Average lessons per unit: {total_sequenced_lessons / units_with_sequences if units_with_sequences > 0 else 0:.1f}")
print(f"{'='*80}")

# Subject breakdown
print(f"\n📚 By Subject:")
subject_counts = defaultdict(int)
for prog in learning_progressions:
    subject_counts[prog['subject']] += 1

for subject, count in sorted(subject_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"   {subject}: {count} units")

print(f"\n🎯 Learning progression analysis complete!")
print(f"   Use these pathways to guide students through optimal learning sequences")

