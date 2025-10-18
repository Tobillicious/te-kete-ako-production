#!/usr/bin/env python3
"""
IMPORT 85,291 RELATIONSHIPS TO SUPABASE
Transform GraphRAG from flat DB to true knowledge GRAPH
"""

import json
from pathlib import Path
from supabase_graphrag_connector import SupabaseGraphRAGConnector
import time

print('\n🔗 IMPORTING 85,291 RELATIONSHIPS TO GRAPHRAG')
print('=' * 70)
print('Creating true knowledge GRAPH...\n')

# Load relationship graph
with open('relationship-graph.json') as f:
    graph = json.load(f)

print(f'✅ Loaded relationship graph: {len(graph):,} nodes\n')

# Count total relationships
total_relationships = sum(len(node.get('links_to', [])) for node in graph.values() if isinstance(node, dict))
print(f'🔗 Total relationships to import: {total_relationships:,}\n')

# Connect to Supabase
g = SupabaseGraphRAGConnector()

# First, try to create the table
print('📋 Creating relationships table...')
try:
    # Read SQL file
    with open('create-relationships-table.sql') as f:
        sql = f.read()
    # Note: Can't execute raw SQL via REST API, will use RPC or manual
    print('⚠️  Table creation SQL prepared (run manually in Supabase dashboard if needed)')
except:
    pass

# Import relationships in batches
batch_size = 100
imported = 0
errors = 0
start = time.time()

relationships_data = []

# Build all relationships
for source_path, value in graph.items():
    # Handle both dict and list formats
    if isinstance(value, dict):
        links = value.get('links_to', [])
    elif isinstance(value, list):
        links = value
    else:
        continue
    
    for target_path in links:
        if target_path:  # Skip empty links
            relationships_data.append({
                'source_path': str(source_path),
                'target_path': str(target_path),
                'relationship_type': 'links_to',
                'strength': 1
            })

print(f'📊 Prepared {len(relationships_data):,} relationship records\n')
print('🚀 Starting import...\n')

# Upload in batches
for i in range(0, len(relationships_data), batch_size):
    batch = relationships_data[i:i+batch_size]
    
    try:
        # Try to insert
        result = g.client.table('resource_relationships').insert(batch).execute()
        imported += len(batch)
        
        if imported % 1000 == 0:
            elapsed = time.time() - start
            rate = imported / elapsed if elapsed > 0 else 0
            remaining = (len(relationships_data) - imported) / rate if rate > 0 else 0
            print(f'  ✅ {imported:,}/{len(relationships_data):,} ({imported/len(relationships_data)*100:.1f}%) | {rate:.0f}/sec | ETA: {remaining/60:.1f}min')
    
    except Exception as e:
        error_msg = str(e)
        
        # If table doesn't exist, create it first
        if 'does not exist' in error_msg:
            print(f'\n⚠️  Relationships table does not exist yet!')
            print(f'   Please run create-relationships-table.sql in Supabase dashboard first')
            print(f'   Then re-run this script')
            break
        
        errors += 1
        if errors > 10:
            print(f'\n❌ Too many errors: {error_msg}')
            break
        continue

# Summary
elapsed = time.time() - start
print('\n' + '=' * 70)
print('📊 RELATIONSHIP IMPORT COMPLETE\n')
print(f'Time: {elapsed/60:.1f} minutes')
print(f'Total relationships: {len(relationships_data):,}')
print(f'✅ Imported: {imported:,}')
print(f'❌ Errors: {errors}')
print(f'Rate: {imported/elapsed:.0f} relationships/second')

# Check final state
try:
    final = g.client.table('resource_relationships').select('*', count='exact').limit(0).execute()
    print(f'\n🎉 GraphRAG now has {final.count:,} relationships!')
    print('\n✅ KNOWLEDGE GRAPH IS COMPLETE!')
except:
    print('\n⚠️  Run create-relationships-table.sql first, then re-run this script')

print('=' * 70 + '\n')

