#!/usr/bin/env python3
"""
MANUAL BATCH-BY-BATCH UPLOAD
Upload in very small batches, show progress, handle errors
"""

import json
from pathlib import Path
from supabase_graphrag_connector import SupabaseGraphRAGConnector
import time

# Load records
all_records = []
for i in range(1, 4):
    file = Path(f'graphrag-full-index-part{i}.json')
    with open(file) as f:
        all_records.extend(json.load(f)['records'])

print(f'\n📊 Total records: {len(all_records):,}')

# Connect
g = SupabaseGraphRAGConnector()
current = g.client.table('resources').select('*', count='exact').limit(0).execute()
print(f'✅ Current in GraphRAG: {current.count:,}')
print(f'🎯 Need to add: ~{len(all_records) - current.count:,}\n')

# Upload in tiny batches
batch_size = 10
uploaded_this_session = 0
skipped_duplicates = 0

start = time.time()

for i in range(0, len(all_records), batch_size):
    batch = all_records[i:i+batch_size]
    
    for record in batch:
        try:
            # Prepare single record
            rt = record.get('resource_type', 'page')
            types = {'html':'page','json':'page','md':'page','lesson':'lesson','handout':'handout','unit':'unit-plan','game':'game','assessment':'assessment','page':'page','activity':'activity','interactive':'interactive'}
            
            res = {
                'title': str(record.get('title',''))[:200],
                'description': str(record.get('description',''))[:500],
                'type': types.get(rt, 'page'),
                'path': str(record.get('filepath',''))[:500],
                'subject': (', '.join(record.get('subjects',[])) or 'General')[:100],
                'level': f"Year {record.get('year_level')}" if record.get('year_level') else 'All Levels',
                'tags': (record.get('subjects',[]) or ['general'])[:10],
                'cultural_elements': {
                    'has_whakatauaki': bool(record.get('has_whakatauaki')),
                    'has_te_reo': bool(record.get('has_te_reo')),
                    'has_cultural_context': bool(record.get('has_cultural_context'))
                },
                'is_active': True,
                'author': 'Te Kete Ako Team'
            }
            
            g.client.table('resources').insert([res]).execute()
            uploaded_this_session += 1
            
        except Exception as e:
            if 'duplicate' in str(e).lower() or 'unique' in str(e).lower():
                skipped_duplicates += 1
            # Continue silently
            pass
    
    # Progress every 100
    if (uploaded_this_session + skipped_duplicates) % 100 == 0:
        elapsed = time.time() - start
        total_processed = uploaded_this_session + skipped_duplicates
        rate = total_processed / elapsed if elapsed > 0 else 0
        print(f'  [{total_processed:,}/{len(all_records):,}] Uploaded: {uploaded_this_session:,} | Skipped: {skipped_duplicates:,} | Rate: {rate:.0f}/sec')

# Final
elapsed = time.time() - start
final_count = g.client.table('resources').select('*', count='exact').limit(0).execute()

print(f'\n✅ DONE in {elapsed/60:.1f} minutes')
print(f'Uploaded this session: {uploaded_this_session:,}')
print(f'Skipped (duplicates): {skipped_duplicates:,}')
print(f'🎉 GraphRAG now has: {final_count.count:,} resources')
