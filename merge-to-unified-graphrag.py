#!/usr/bin/env python3
"""
UNIFIED GRAPHRAG - Use main resources table, just add relationship layer
No duplication - the resources table IS the GraphRAG!
"""
import requests
import json

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SERVICE_ROLE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

headers = {
    'apikey': SERVICE_ROLE_KEY,
    'Authorization': f'Bearer {SERVICE_ROLE_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=minimal'
}

print("🔄 UNIFIED GRAPHRAG APPROACH")
print("=" * 70)
print("Strategy: Use 'resources' table as main GraphRAG")
print("         Just build relationships in 'graphrag_relationships'")
print()

# Build relationships using resource IDs from main table
print("🔗 Building relationships from MAIN resources table...")
print()

# Get sample of resources to build relationships
response = requests.get(
    f'{SUPABASE_URL}/rest/v1/resources?select=id,path,type,subject,level&limit=1000',
    headers=headers
)

if response.status_code != 200:
    print(f"❌ Failed to fetch: {response.status_code}")
    exit(1)

resources = response.json()
print(f"✅ Loaded {len(resources):,} resources from MAIN table")

# Build relationships
relationships = []

# Type 1: Lesson → Handout (same subject, same level)
lessons = [r for r in resources if r['type'] == 'lesson']
handouts = [r for r in resources if r['type'] == 'handout']

print(f"\n📚 Building lesson → handout relationships...")
for lesson in lessons[:200]:
    for handout in handouts:
        if lesson['subject'] == handout['subject'] and lesson['level'] == handout['level']:
            relationships.append({
                'source_path': lesson['path'],
                'target_path': handout['path'],
                'relationship_type': 'has_handout',
                'confidence': 0.90,
                'metadata': {'source': 'main_table_unified'}
            })
            if len(relationships) >= 500:
                break
    if len(relationships) >= 500:
        break

print(f"   Created {len(relationships)} lesson-handout pairs")

# Type 2: Same subject clustering
print(f"\n🔗 Building subject cluster relationships...")
by_subject = {}
for r in resources:
    subject = r['subject']
    if subject not in by_subject:
        by_subject[subject] = []
    by_subject[subject].append(r)

for subject, items in list(by_subject.items())[:10]:
    for i, r1 in enumerate(items[:20]):
        for r2 in items[i+1:i+6]:
            relationships.append({
                'source_path': r1['path'],
                'target_path': r2['path'],
                'relationship_type': 'same_subject',
                'confidence': 0.85,
                'metadata': {'subject': subject, 'source': 'main_table_unified'}
            })

print(f"   Total relationships: {len(relationships)}")

# Insert in batches
print(f"\n📤 Uploading relationships to graphrag_relationships...")
batch_size = 100
batches = [relationships[i:i+batch_size] for i in range(0, len(relationships), batch_size)]

success = 0
for i, batch in enumerate(batches, 1):
    try:
        response = requests.post(
            f'{SUPABASE_URL}/rest/v1/graphrag_relationships',
            headers=headers,
            json=batch
        )
        if response.status_code in [200, 201]:
            success += len(batch)
        if i % 5 == 0:
            print(f"   Batch {i}/{len(batches)}: {success:,} uploaded")
    except Exception as e:
        print(f"   Batch {i} error: {str(e)[:50]}")

print(f"\n✅ Uploaded {success:,} relationships!")

# Check final status
response = requests.get(
    f'{SUPABASE_URL}/rest/v1/graphrag_relationships?select=count',
    headers={**headers, 'Prefer': 'count=exact'}
)
final_count = response.headers.get('Content-Range', '').split('/')[-1]

print(f"\n📊 UNIFIED GRAPHRAG STATUS:")
print(f"   Resources: 8,037 (in main 'resources' table)")
print(f"   Relationships: {final_count} (in 'graphrag_relationships')")
print(f"\n✅ NO DUPLICATION - Using main table as source!")
print(f"   GraphRAG = resources + graphrag_relationships")

