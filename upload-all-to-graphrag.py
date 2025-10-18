#!/usr/bin/env python3
"""
UPLOAD ALL 10,145 FILES TO GRAPHRAG
Batch upload with progress tracking and error handling
"""

import json
from pathlib import Path
from supabase_graphrag_connector import SupabaseGraphRAGConnector
import time

print('\n🚀 UPLOADING 10,145 FILES TO GRAPHRAG')
print('=' * 70 + '\n')

# Load all index parts
all_records = []
for i in range(1, 4):  # We have 3 parts
    file = Path(f'graphrag-full-index-part{i}.json')
    if file.exists():
        with open(file) as f:
            data = json.load(f)
            all_records.extend(data['records'])
        print(f'✅ Loaded part {i}: {len(data["records"]):,} records')

print(f'\n📊 Total records to upload: {len(all_records):,}\n')

# Connect
graphrag = SupabaseGraphRAGConnector()
test = graphrag.test_connection()
if not test['success']:
    print(f'❌ Connection failed: {test["message"]}')
    exit(1)

print(f'✅ Connected! Current resources in GraphRAG: {test.get("count", 0):,}\n')

# Upload in batches
batch_size = 50
uploaded = 0
errors = 0
start_time = time.time()

for i in range(0, len(all_records), batch_size):
    batch = all_records[i:i+batch_size]
    
    try:
        batch_data = []
        for record in batch:
            # Map to valid schema
            resource_type = record.get('resource_type', record.get('file_type', 'page'))
            type_mapping = {
                'html': 'page', 'json': 'page', 'md': 'page',
                'lesson': 'lesson', 'handout': 'handout',
                'unit': 'unit-plan', 'game': 'game',
                'assessment': 'assessment', 'page': 'page'
            }
            
            resource = {
                'title': record.get('title', 'Untitled')[:200],
                'description': record.get('description', '')[:500],
                'type': type_mapping.get(resource_type, 'page'),
                'path': record.get('filepath', '')[:500],
                'subject': ', '.join(record.get('subjects', []))[:100] if record.get('subjects') else 'General',
                'level': f"Year {record.get('year_level')}" if record.get('year_level') else 'All Levels',
                'tags': (record.get('subjects', []) or ['general'])[:10],
                'cultural_elements': {
                    'has_whakatauaki': record.get('has_whakatauaki', False),
                    'has_te_reo': record.get('has_te_reo', False),
                    'has_cultural_context': record.get('has_cultural_context', False),
                    'is_public': record.get('is_public', False),
                    'is_backup': record.get('is_backup', False)
                },
                'is_active': record.get('is_public', True),  # Only public files are active
                'author': 'Te Kete Ako Team'
            }
            batch_data.append(resource)
        
        # Insert batch
        result = graphrag.client.table('resources').insert(batch_data).execute()
        uploaded += len(batch)
        
        # Progress
        if uploaded % 500 == 0 or uploaded == len(all_records):
            elapsed = time.time() - start_time
            rate = uploaded / elapsed if elapsed > 0 else 0
            remaining = (len(all_records) - uploaded) / rate if rate > 0 else 0
            print(f'  ✅ Uploaded {uploaded:,}/{len(all_records):,} ({(uploaded/len(all_records)*100):.1f}%) - {rate:.0f} rec/sec - ETA: {remaining/60:.1f} min')
        
    except Exception as e:
        # Just skip batches with errors, keep going
        errors += 1
        if errors % 10 == 0:
            print(f'  ⚠️  {errors} batches had errors, continuing...')
        continue

# Final summary
elapsed = time.time() - start_time
print('\n' + '=' * 70)
print('📊 UPLOAD COMPLETE\n')
print(f'Time taken: {elapsed/60:.1f} minutes')
print(f'Total records: {len(all_records):,}')
print(f'✅ Successfully uploaded: {uploaded:,}')
print(f'⚠️  Batches with errors: {errors}')
print(f'Upload rate: {uploaded/elapsed:.0f} records/second')

# Get final count
final = graphrag.test_connection()
print(f'\n🎉 GraphRAG now has: {final.get("count", 0):,} total resources!')
print('=' * 70 + '\n')

