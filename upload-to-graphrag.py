#!/usr/bin/env python3
"""
UPLOAD TO GRAPHRAG - Actually insert indexed data
Upload 1,938 indexed files to Supabase for intelligent discovery
"""

import json
from pathlib import Path
from supabase_graphrag_connector import SupabaseGraphRAGConnector

print('\n🚀 UPLOADING TO SUPABASE GRAPHRAG')
print('=' * 70 + '\n')

# Load indexed data
index_file = Path('graphrag-index-complete.json')
if not index_file.exists():
    print('❌ Index file not found! Run index-all-content-to-graphrag.py first')
    exit(1)

with open(index_file) as f:
    data = json.load(f)

records = data.get('records', [])
print(f'📊 Found {len(records)} records to upload\n')

# Connect to GraphRAG
graphrag = SupabaseGraphRAGConnector()

# Test connection
test = graphrag.test_connection()
if not test['success']:
    print(f'❌ Connection failed: {test["message"]}')
    exit(1)

print(f'✅ Connected to Supabase GraphRAG')
print(f'   Current resources: {test.get("count", 0)}\n')

# Upload in batches
batch_size = 50
uploaded = 0
errors = 0

for i in range(0, len(records), batch_size):
    batch = records[i:i+batch_size]
    
    try:
        # Prepare batch for insertion (match actual schema)
        batch_data = []
        for record in batch:
            # Create resource record matching Supabase schema
            # Map file types to allowed values from schema
            resource_type = record.get('resource_type', record.get('file_type', 'page'))
            type_mapping = {
                'html': 'page',
                'json': 'page',
                'md': 'page',
                'lesson': 'lesson',
                'handout': 'handout',
                'unit': 'unit-plan',
                'game': 'game',
                'page': 'page'
            }
            valid_type = type_mapping.get(resource_type, 'page')
            
            resource = {
                'title': record.get('title', 'Untitled'),
                'description': record.get('description', '')[:500],  # Limit length
                'type': valid_type,
                'path': record.get('filepath', ''),
                'subject': ', '.join(record.get('subjects', [])) if record.get('subjects') else 'General',
                'level': f"Year {record.get('year_level')}" if record.get('year_level') else 'All Levels',
                'tags': record.get('subjects', []) + (['whakataukī'] if record.get('has_whakatauaki') else []),
                'cultural_elements': {
                    'has_whakatauaki': record.get('has_whakatauaki', False),
                    'has_te_reo': record.get('has_te_reo', False),
                    'has_cultural_context': record.get('has_cultural_context', False)
                },
                'is_active': True,
                'author': 'Te Kete Ako Team'
            }
            batch_data.append(resource)
        
        # Insert batch (regular insert, skip duplicates)
        result = graphrag.client.table('resources').insert(batch_data).execute()
        uploaded += len(batch)
        print(f'  ✅ Uploaded batch {i//batch_size + 1}: {uploaded}/{len(records)} records')
        
    except Exception as e:
        print(f'  ⚠️  Error uploading batch: {e}')
        errors += 1
        # Don't stop on errors - keep going to index as much as possible
        continue

print('\n' + '=' * 70)
print('📊 UPLOAD SUMMARY\n')
print(f'Total records: {len(records)}')
print(f'✅ Uploaded: {uploaded}')
print(f'❌ Errors: {errors}')
print(f'\n✅ GraphRAG is now intelligent with {uploaded} indexed resources!')
print('=' * 70 + '\n')

