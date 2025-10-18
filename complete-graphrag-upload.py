#!/usr/bin/env python3
"""Upload ALL 10,181 records - one by one, error-tolerant"""
import json, time
from pathlib import Path
from supabase_graphrag_connector import SupabaseGraphRAGConnector

all_records = []
for i in range(1,4):
    with open(f'graphrag-full-index-part{i}.json') as f:
        all_records.extend(json.load(f)['records'])

print(f'Uploading {len(all_records):,} records...\n')

g = SupabaseGraphRAGConnector()
uploaded, skipped, errors = 0, 0, 0
start = time.time()

types_map = {'html':'page','lesson':'lesson','handout':'handout','unit':'unit-plan','game':'game','page':'page'}

for i, rec in enumerate(all_records):
    try:
        res = {
            'title': str(rec.get('title','Untitled'))[:200],
            'description': str(rec.get('description',''))[:500],
            'type': types_map.get(rec.get('resource_type','page'), 'page'),
            'path': str(rec.get('filepath',''))[:500],
            'subject': 'General', 'level': 'All Levels', 'tags': ['general'],
            'is_active': True, 'author': 'Te Kete Ako'
        }
        g.client.table('resources').insert([res]).execute()
        uploaded += 1
    except Exception as e:
        if 'duplicate' in str(e).lower(): skipped += 1
        else: errors += 1
    
    if (i+1) % 200 == 0:
        elapsed = time.time() - start
        print(f'[{i+1:,}/{len(all_records):,}] Up:{uploaded:,} Skip:{skipped:,} Err:{errors} | {(i+1)/elapsed:.0f}/sec')

print(f'\n✅ Done: {uploaded:,} uploaded, {skipped:,} skipped, {errors} errors in {(time.time()-start)/60:.1f}min')
final = g.client.table('resources').select('*', count='exact').limit(0).execute()
print(f'🎉 GraphRAG total: {final.count:,}')

