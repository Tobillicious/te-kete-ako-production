#!/usr/bin/env python3
"""
BUILD ALL RELATIONSHIPS - FAST
Map every connection in the knowledge graph
"""

from supabase_graphrag_connector import SupabaseGraphRAGConnector
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
import time

print("🔗 BUILDING ALL RELATIONSHIPS")
print("=" * 70)

connector = SupabaseGraphRAGConnector()
supabase = connector.client

# Get all resources
print("📊 Loading all resources...")
all_resources = supabase.table('resources').select('id,path,type,title').execute()
resources_by_path = {r['path']: r for r in all_resources.data}
print(f"✅ Loaded {len(resources_by_path):,} resources\n")

# Current relationships
current_rels = supabase.table('graphrag_relationships').select('*', count='exact').limit(0).execute()
print(f"📊 Current relationships: {current_rels.count:,}\n")

relationships = []
processed = 0

print("🔍 Scanning for relationships...\n")

for path, resource in resources_by_path.items():
    try:
        # Read file to find links
        file_path = Path(path)
        if not file_path.exists():
            continue
        
        if path.endswith('.html'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                
                # Find all links
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    
                    # Clean up href
                    if href.startswith('#') or href.startswith('http'):
                        continue
                    
                    # Normalize path
                    if href.startswith('/'):
                        target_path = href[1:]
                    else:
                        target_path = str((file_path.parent / href).resolve().relative_to(Path.cwd()))
                    
                    # Check if target exists
                    if target_path in resources_by_path:
                        relationships.append({
                            'source_path': path,
                            'target_path': target_path,
                            'relationship_type': 'links_to',
                            'confidence': 1.0
                        })
        
        processed += 1
        if processed % 100 == 0:
            print(f"  Processed: {processed:,}/{len(resources_by_path):,} | Found: {len(relationships):,} relationships")
    
    except Exception as e:
        continue

print(f"\n✅ Scan complete!")
print(f"📊 Found {len(relationships):,} relationships\n")

# Upload in batches
print("🚀 Uploading relationships...\n")
BATCH_SIZE = 100
uploaded = 0
errors = 0

for i in range(0, len(relationships), BATCH_SIZE):
    batch = relationships[i:i+BATCH_SIZE]
    try:
        supabase.table('graphrag_relationships').insert(batch).execute()
        uploaded += len(batch)
        if (i + BATCH_SIZE) % 1000 == 0:
            print(f"  Uploaded: {uploaded:,}/{len(relationships):,}")
    except Exception as e:
        errors += 1

print(f"\n{'=' * 70}")
print("🎉 RELATIONSHIP BUILD COMPLETE!")
print(f"{'=' * 70}")
print(f"Total found: {len(relationships):,}")
print(f"✅ Uploaded: {uploaded:,}")
print(f"❌ Errors: {errors}")

# Final count
final = supabase.table('graphrag_relationships').select('*', count='exact').limit(0).execute()
print(f"\n📊 Total relationships: {final.count:,}")
print(f"📈 Growth: +{final.count - current_rels.count:,}")
print("=" * 70)

