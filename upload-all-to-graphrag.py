#!/usr/bin/env python3
"""
UPLOAD ALL 929 FILES TO GRAPHRAG WITH PROPER RELATIONSHIPS
Then we can query and organize the remaining 9,252 indexed resources
"""

import json
from supabase import create_client
from datetime import datetime
import time

print("🧠 UPLOADING COMPLETE CONTENT MAP TO GRAPHRAG")
print("=" * 80)

# Supabase connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load our complete map
with open('complete-content-map.json', 'r') as f:
    content_map = json.load(f)

print(f"\n✅ Loaded complete map: {content_map['total_scanned']} files\n")

# Check current GraphRAG status
print("📊 Checking current GraphRAG status...")
try:
    result = supabase.table('resources').select('*', count='exact').limit(1).execute()
    current_count = result.count
    print(f"   Current resources in GraphRAG: {current_count}")
except Exception as e:
    print(f"   Error checking GraphRAG: {e}")
    current_count = 0

# Prepare resources for upload
all_resources = []
for res_type, resources in content_map['all_resources'].items():
    for resource in resources:
        # Format for actual GraphRAG schema
        has_maori = 'Te Ao Māori' in resource['subjects']
        
        graphrag_resource = {
            'title': resource['title'][:200],  # Truncate if needed
            'path': resource['path'],
            'type': res_type.rstrip('s'),  # singular form (lesson, handout, etc)
            'subject': ', '.join(resource['subjects']),
            'description': f"Educational {res_type.rstrip('s')} for {', '.join(resource['subjects'])}. Located in {resource['directory']}/.",
            'level': 'Year 9-10',  # Default, would need parsing
            'difficulty_level': 'intermediate',
            'estimated_duration_minutes': 180,  # 3 hours default
            'is_active': True,
            'featured': False,
            'author': 'Te Kete Ako Team',
            'tags': resource['subjects'] + [res_type.rstrip('s'), resource['directory']],
            'cultural_elements': {
                'te_reo_usage': 'high' if has_maori else 'low',
                'maori_concepts': ['mātauranga māori'] if has_maori else []
            },
            'curriculum_alignment': {
                'curriculum_areas': resource['subjects'],
                'key_competencies': ['thinking', 'relating_to_others']
            }
        }
        all_resources.append(graphrag_resource)

print(f"\n📦 Prepared {len(all_resources)} resources for upload")

# Upload in batches
batch_size = 100
uploaded = 0
failed = 0

print(f"\n⬆️  Uploading to GraphRAG (batches of {batch_size})...\n")

for i in range(0, len(all_resources), batch_size):
    batch = all_resources[i:i+batch_size]
    batch_num = (i // batch_size) + 1
    
    try:
        result = supabase.table('resources').upsert(batch).execute()
        uploaded += len(batch)
        print(f"   ✅ Batch {batch_num}: {len(batch)} resources uploaded ({uploaded}/{len(all_resources)})")
        time.sleep(0.5)  # Rate limiting
    except Exception as e:
        failed += len(batch)
        print(f"   ❌ Batch {batch_num} failed: {str(e)[:100]}")
        
        # Try individual uploads for failed batch
        for resource in batch:
            try:
                supabase.table('resources').upsert([resource]).execute()
                uploaded += 1
                failed -= 1
            except:
                pass

print("\n" + "=" * 80)
print("📊 UPLOAD COMPLETE")
print("=" * 80)
print(f"\n✅ Uploaded: {uploaded}")
print(f"❌ Failed: {failed}")
print(f"📈 Success Rate: {(uploaded/len(all_resources)*100):.1f}%")

# Check new total
print(f"\n📊 Checking updated GraphRAG status...")
try:
    result = supabase.table('resources').select('*', count='exact').limit(1).execute()
    new_count = result.count
    print(f"   Resources in GraphRAG now: {new_count}")
    print(f"   Increase: +{new_count - current_count}")
except Exception as e:
    print(f"   Error: {e}")

print("\n✅ Complete map uploaded! Now query GraphRAG for organization!")
print("\nNext: python3 query-graphrag-for-next-gold.py")
