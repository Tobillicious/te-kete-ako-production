#!/usr/bin/env python3
"""
UPLOAD ALL REMAINING 4,242 FILES TO GRAPHRAG
Actually complete the indexing - no stopping on errors
"""

import json
from pathlib import Path
from supabase_graphrag_connector import SupabaseGraphRAGConnector
import time

print('\n🚀 UPLOADING REMAINING 4,242 FILES TO GRAPHRAG')
print('=' * 70 + '\n')

# Load all 10,181 indexed records
all_records = []
for i in range(1, 4):
    file = Path(f'graphrag-full-index-part{i}.json')
    if file.exists():
        with open(file) as f:
            data = json.load(f)
            all_records.extend(data.get('records', []))

print(f'✅ Loaded {len(all_records):,} indexed records')

# Connect
graphrag = SupabaseGraphRAGConnector()
test = graphrag.test_connection()
print(f'✅ Connected! Current in GraphRAG: {test.get("count", 0):,}\n')

# Upload ALL records with better error handling
batch_size = 25  # Smaller batches for better error handling
uploaded = 0
skipped = 0
errors_logged = []
start_time = time.time()

for i in range(0, len(all_records), batch_size):
    batch = all_records[i:i+batch_size]
    
    # Prepare each record individually
    for record in batch:
        try:
            # Map to valid schema
            resource_type = record.get('resource_type', record.get('file_type', 'page'))
            type_mapping = {
                'html': 'page', 'json': 'page', 'md': 'page',
                'lesson': 'lesson', 'handout': 'handout',
                'unit': 'unit-plan', 'game': 'game',
                'assessment': 'assessment', 'page': 'page',
                'activity': 'activity', 'interactive': 'interactive'
            }
            
            valid_type = type_mapping.get(resource_type, 'page')
            
            # Prepare single resource
            resource = {
                'title': str(record.get('title', 'Untitled'))[:200],
                'description': str(record.get('description', ''))[:500],
                'type': valid_type,
                'path': str(record.get('filepath', ''))[:500],
                'subject': (', '.join(record.get('subjects', [])) if record.get('subjects') else 'General')[:100],
                'level': f"Year {record.get('year_level')}" if record.get('year_level') else 'All Levels',
                'tags': (record.get('subjects', []) or ['general'])[:10],
                'cultural_elements': {
                    'has_whakatauaki': bool(record.get('has_whakatauaki', False)),
                    'has_te_reo': bool(record.get('has_te_reo', False)),
                    'has_cultural_context': bool(record.get('has_cultural_context', False)),
                    'is_public': bool(record.get('is_public', False)),
                    'is_backup': bool(record.get('is_backup', False))
                },
                'is_active': bool(record.get('is_public', True)),
                'author': 'Te Kete Ako Team'
            }
            
            # Try to insert single record
            result = graphrag.client.table('resources').insert([resource]).execute()
            uploaded += 1
            
        except Exception as e:
            error_msg = str(e)
            skipped += 1
            # Only log unique errors
            if error_msg not in [e['error'] for e in errors_logged]:
                errors_logged.append({
                    'error': error_msg,
                    'record': record.get('filepath', 'unknown'),
                    'count': 1
                })
    
    # Progress update every 100 records
    if (uploaded + skipped) % 100 == 0:
        elapsed = time.time() - start_time
        rate = (uploaded + skipped) / elapsed if elapsed > 0 else 0
        remaining = (len(all_records) - uploaded - skipped) / rate if rate > 0 else 0
        print(f'  📊 Progress: {uploaded:,} uploaded, {skipped:,} skipped | {(uploaded+skipped)/len(all_records)*100:.1f}% | ETA: {remaining/60:.1f}min')

# Final status
elapsed = time.time() - start_time
final = graphrag.test_connection()

print('\n' + '=' * 70)
print('📊 UPLOAD COMPLETE\n')
print(f'Time: {elapsed/60:.1f} minutes')
print(f'Total processed: {len(all_records):,}')
print(f'✅ Uploaded: {uploaded:,}')
print(f'⏭️  Skipped (duplicates/errors): {skipped:,}')
print(f'Rate: {(uploaded+skipped)/elapsed:.0f} records/second')
print(f'\n🎉 GraphRAG now has: {final.get("count", 0):,} total resources!')
print('=' * 70 + '\n')

# Save error log
if errors_logged:
    with open('upload-errors.json', 'w') as f:
        json.dump(errors_logged, f, indent=2)
    print(f'⚠️  {len(errors_logged)} unique error types logged to upload-errors.json\n')

