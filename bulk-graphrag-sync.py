#!/usr/bin/env python3
"""
BULK GRAPHRAG SYNC - Use service role key for massive operations
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

print("🔥 BULK GRAPHRAG SYNC - SERVICE ROLE POWER!")
print("=" * 70)

# Step 1: Sync all 8,037 resources to graphrag_resources
print("\n📊 Step 1: Syncing all resources from main DB to GraphRAG...")

# Get all resources from main table
response = requests.get(
    f'{SUPABASE_URL}/rest/v1/resources?select=*&limit=8037',
    headers=headers
)

if response.status_code == 200:
    resources = response.json()
    print(f"   ✅ Fetched {len(resources):,} resources from main DB")
    
    # Batch insert to graphrag_resources
    batch_size = 100
    batches = [resources[i:i+batch_size] for i in range(0, len(resources), batch_size)]
    
    print(f"   📦 Inserting in {len(batches)} batches...")
    
    success_count = 0
    for i, batch in enumerate(batches, 1):
        # Transform to graphrag format
        graphrag_batch = []
        for r in batch:
            graphrag_batch.append({
                'file_path': r.get('path', ''),
                'resource_type': r.get('type', ''),
                'title': r.get('title', ''),
                'quality_score': 90,  # High quality from main DB
                'cultural_context': True,
                'year_level': r.get('level', ''),
                'subject': r.get('subject', ''),
                'has_te_reo': True,
                'content_preview': (r.get('description', '') or '')[:500],
                'metadata': {
                    'source': 'main_resources_table',
                    'sync_batch': i,
                    'featured': r.get('featured', False),
                    'tags': r.get('tags', [])
                }
            })
        
        # Insert batch
        insert_response = requests.post(
            f'{SUPABASE_URL}/rest/v1/graphrag_resources',
            headers=headers,
            json=graphrag_batch
        )
        
        if insert_response.status_code in [200, 201]:
            success_count += len(batch)
            if i % 10 == 0:
                print(f"      Batch {i}/{len(batches)}: {success_count:,} synced")
        else:
            print(f"      ⚠️ Batch {i} failed: {insert_response.status_code}")
    
    print(f"\n   ✅ Synced {success_count:,} resources to GraphRAG!")
    
else:
    print(f"   ❌ Failed to fetch resources: {response.status_code}")

# Step 2: Check GraphRAG status
print("\n📊 Step 2: Checking GraphRAG status...")

response = requests.get(
    f'{SUPABASE_URL}/rest/v1/graphrag_resources?select=count',
    headers={**headers, 'Prefer': 'count=exact'}
)

if response.status_code == 200:
    count = response.headers.get('Content-Range', '0').split('/')[-1]
    print(f"   ✅ GraphRAG Resources: {count}")

response = requests.get(
    f'{SUPABASE_URL}/rest/v1/graphrag_relationships?select=count',
    headers={**headers, 'Prefer': 'count=exact'}
)

if response.status_code == 200:
    count = response.headers.get('Content-Range', '0').split('/')[-1]
    print(f"   ✅ GraphRAG Relationships: {count}")

print("\n🎯 BULK SYNC COMPLETE!")
print("=" * 70)

