#!/usr/bin/env python3
"""
Merge knowledge from local SQLite databases into Supabase GraphRAG
This completes the Hegelian synthesis - best of all systems
"""

import sqlite3
from supabase_graphrag_connector import SupabaseGraphRAGConnector
import time
import json

print("🔄 MERGING LOCAL DB KNOWLEDGE → SUPABASE GRAPHRAG")
print("=" * 70)

connector = SupabaseGraphRAGConnector()
supabase = connector.client

# Check current Supabase state
current = supabase.table('resources').select('*', count='exact').limit(0).execute()
print(f"📊 Current Supabase: {current.count:,} resources")

# Database files to merge
db_files = [
    'te-kete-complete-knowledge.db',
    'te-kete-local-index.db'
]

total_imported = 0
total_skipped = 0
total_errors = 0

for db_file in db_files:
    try:
        print(f"\n📂 Processing: {db_file}")
        print("-" * 70)
        
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Get all records
        cursor.execute("SELECT * FROM resources LIMIT 100")
        records = cursor.fetchall()
        
        print(f"Found {len(records)} records to process (showing first 100)")
        
        for i, row in enumerate(records):
            try:
                # Convert to dict
                record = dict(row)
                
                # Type mapping for Supabase constraints
                type_mapping = {
                    'html': 'page',
                    'json': 'resource',
                    'md': 'resource',
                    'lesson': 'lesson',
                    'handout': 'handout',
                    'unit': 'unit-plan',
                    'unit-plan': 'unit-plan',
                    'game': 'game',
                    'tool': 'tool',
                    'resource': 'resource',
                    'page': 'page',
                    'interactive': 'interactive',
                    'assessment': 'assessment',
                    'activity': 'activity'
                }
                
                raw_type = record.get('type') or record.get('content_type', 'resource')
                mapped_type = type_mapping.get(raw_type, 'resource')
                
                # Map to Supabase schema
                supabase_record = {
                    'title': record.get('title', 'Untitled'),
                    'description': record.get('description', ''),
                    'path': record.get('path') or record.get('file_path', ''),
                    'type': mapped_type,
                    'subject': record.get('subject', ''),
                    'level': record.get('level') or record.get('year_level', ''),
                    'tags': record.get('tags', []),
                    'cultural_elements': record.get('cultural_elements'),
                    'curriculum_alignment': record.get('curriculum_alignment'),
                    'is_active': True
                }
                
                # Check if already exists
                existing = supabase.table('resources')\
                    .select('id')\
                    .eq('path', supabase_record['path'])\
                    .limit(1)\
                    .execute()
                
                if existing.data:
                    total_skipped += 1
                else:
                    # Insert new record
                    supabase.table('resources').insert(supabase_record).execute()
                    total_imported += 1
                
                if (i + 1) % 10 == 0:
                    print(f"  Progress: {i+1}/{len(records)} | Imported: {total_imported} | Skipped: {total_skipped}")
                    
            except Exception as e:
                total_errors += 1
                if total_errors <= 3:
                    print(f"  ⚠️  Error on record {i}: {e}")
        
        conn.close()
        print(f"✅ Completed {db_file}")
        
    except Exception as e:
        print(f"❌ Could not process {db_file}: {e}")

print("\n" + "=" * 70)
print("📊 MERGE COMPLETE")
print(f"✅ Imported: {total_imported}")
print(f"⏭️  Skipped (duplicates): {total_skipped}")
print(f"❌ Errors: {total_errors}")

# Final count
final = supabase.table('resources').select('*', count='exact').limit(0).execute()
print(f"\n🎉 Final Supabase GraphRAG: {final.count:,} resources")
print(f"📈 Growth: +{final.count - current.count:,}")
print("=" * 70)

