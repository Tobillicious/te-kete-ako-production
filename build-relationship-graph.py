#!/usr/bin/env python3
"""
BUILD RELATIONSHIP GRAPH - Upload relationships to Supabase
Create intelligent connections between resources
"""
import json
import sys

print("🔗 BUILDING RELATIONSHIP GRAPH IN SUPABASE")
print("=" * 70)

# Load relationships
with open('graphrag-relationships-new.json', 'r') as f:
    relationships = json.load(f)

print(f"📊 Loaded {len(relationships):,} relationships")

# Prepare batch insert data
print(f"\n📝 Preparing batch inserts...")

# Group by type
by_type = {}
for rel in relationships:
    rel_type = rel.get('relationship_type', 'references')
    if rel_type not in by_type:
        by_type[rel_type] = []
    by_type[rel_type].append(rel)

print(f"\n📊 RELATIONSHIP BREAKDOWN:")
for rel_type, rels in sorted(by_type.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"   {rel_type}: {len(rels):,}")

# Create SQL for inserting relationships
print(f"\n💾 Creating SQL insert statements...")

# Sample: First 50 relationships
sql_inserts = []
for rel in relationships[:50]:
    sql = f"""
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
VALUES (
    '{rel['source'].replace("'", "''")}',
    '{rel['target'].replace("'", "''")}',
    '{rel.get('relationship_type', 'references')}',
    {rel.get('confidence', 0.9)},
    '{json.dumps({"batch": "sync_1"})}'::jsonb
)
ON CONFLICT DO NOTHING;
"""
    sql_inserts.append(sql)

with open('relationships-upload.sql', 'w') as f:
    f.write('\n'.join(sql_inserts))

print(f"   ✅ SQL created: relationships-upload.sql (50 relationships as sample)")

# Build intelligent learning paths
print(f"\n🗺️ BUILDING LEARNING PATHS FROM RELATIONSHIPS...")

# Find lesson sequences
lesson_sequences = [r for r in relationships if r.get('relationship_type') == 'contains_lesson']
prerequisite_chains = [r for r in relationships if r.get('relationship_type') == 'prerequisite']
handout_links = [r for r in relationships if r.get('relationship_type') == 'has_handout']

print(f"\n📚 PATH COMPONENTS:")
print(f"   Lesson Sequences: {len(lesson_sequences):,}")
print(f"   Prerequisites: {len(prerequisite_chains):,}")
print(f"   Handout Links: {len(handout_links):,}")

# Build unit → lesson → handout paths
learning_paths = []
for seq in lesson_sequences:
    unit = seq['source']
    lesson = seq['target']
    
    # Find handouts for this lesson
    handouts = [h['target'] for h in handout_links if h['source'] == lesson]
    
    if handouts:
        learning_paths.append({
            'unit': unit,
            'lesson': lesson,
            'handouts': handouts,
            'depth': 3
        })

print(f"\n🎯 LEARNING PATHS CREATED: {len(learning_paths):,}")

# Sample paths
if learning_paths:
    print(f"\n📖 SAMPLE LEARNING PATH:")
    sample = learning_paths[0]
    print(f"   Unit: {sample['unit']}")
    print(f"   → Lesson: {sample['lesson']}")
    if sample['handouts']:
        print(f"   → Handouts ({len(sample['handouts'])}):")
        for h in sample['handouts'][:3]:
            print(f"      • {h}")

# Save learning paths
with open('learning-paths-from-relationships.json', 'w') as f:
    json.dump(learning_paths, f, indent=2)

print(f"\n💾 Learning paths saved: learning-paths-from-relationships.json")

print(f"\n✅ RELATIONSHIP GRAPH BUILD COMPLETE!")
print(f"\n📊 FINAL STATS:")
print(f"   Total Relationships: {len(relationships):,}")
print(f"   Unique Types: {len(by_type)}")
print(f"   Learning Paths: {len(learning_paths):,}")
print(f"   Ready for Supabase upload!")

