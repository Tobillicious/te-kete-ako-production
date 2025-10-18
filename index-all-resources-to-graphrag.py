#!/usr/bin/env python3
"""
Complete GraphRAG Indexer - Index ALL 23,166 missing resources
Systematic indexing of lessons, handouts, units, games, assessments, and other resources
"""
from supabase import create_client
from pathlib import Path
import re
from datetime import datetime
import json

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🚀 COMPLETE GRAPHRAG INDEXER")
print("=" * 80)
print("📊 Target: Index ~23,166 missing resources")
print("=" * 80)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
BASE_DIR = Path(__file__).parent

# Get all resources from main table that aren't in GraphRAG
print("\n🔍 Querying main resources table...")
# Fetch ALL resources (Supabase default limit is 1000, need to paginate)
all_resources = []
page_size = 1000
offset = 0

while True:
    resources_result = supabase.table('resources').select('*').range(offset, offset + page_size - 1).execute()
    batch = resources_result.data
    if not batch:
        break
    all_resources.extend(batch)
    offset += page_size
    print(f"   Fetched {len(all_resources)} resources so far...")
    if len(batch) < page_size:
        break

print(f"   Found {len(all_resources)} total resources")

# Get already indexed paths from GraphRAG
print("\n📊 Checking GraphRAG coverage...")
# Fetch ALL graphrag paths (also needs pagination)
indexed_paths_list = []
offset = 0
while True:
    graphrag_result = supabase.table('graphrag_resources').select('file_path').range(offset, offset + page_size - 1).execute()
    batch = graphrag_result.data
    if not batch:
        break
    indexed_paths_list.extend(batch)
    offset += page_size
    if len(batch) < page_size:
        break

indexed_paths = {r['file_path'] for r in indexed_paths_list}
# Also check variations
indexed_paths_set = set()
for path in indexed_paths:
    indexed_paths_set.add(path)
    indexed_paths_set.add(path.lstrip('/'))
    indexed_paths_set.add('/' + path.lstrip('/'))
    if path.startswith('public/'):
        indexed_paths_set.add('/' + path)
        indexed_paths_set.add(path.replace('public/', ''))

print(f"   Already indexed: {len(indexed_paths)} paths")

# Find unindexed resources
to_index = []
for resource in all_resources:
    path = resource['path']
    # Check all variations
    if (path not in indexed_paths_set and 
        ('/' + path) not in indexed_paths_set and
        path.lstrip('/') not in indexed_paths_set and
        ('public/' + path.lstrip('/')) not in indexed_paths_set):
        to_index.append(resource)

print(f"   Unindexed: {len(to_index)} resources")
print(f"   Coverage: {len(indexed_paths)}/{len(all_resources)} ({len(indexed_paths)/len(all_resources)*100:.1f}%)")

# Categorize unindexed
categories = {}
for resource in to_index:
    path = resource['path']
    if '/lessons/' in path:
        cat = 'lessons'
    elif '/handouts/' in path:
        cat = 'handouts'
    elif '/units/' in path:
        cat = 'units'
    elif '/games/' in path:
        cat = 'games'
    elif '/assessment' in path:
        cat = 'assessments'
    elif 'generated-resources-alpha' in path:
        cat = 'generated-resources-alpha'
    else:
        cat = 'other'
    
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(resource)

print("\n📦 Breakdown by category:")
for cat, items in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"   {cat}: {len(items)} resources")

# Helper function to extract metadata
def extract_metadata(resource, html_content=None):
    """Extract metadata from resource record and optionally HTML content"""
    path = resource['path']
    
    # Base metadata from resource table
    title = resource.get('title', Path(path).stem.replace('-', ' ').title())
    resource_type = resource.get('type', 'lesson')
    subject = resource.get('subject', 'Multi-subject')
    year_level = resource.get('level', 'All Years')
    
    # Quality score based on source
    if 'generated-resources-alpha' in path:
        quality_score = 90  # High quality for alpha
    elif 'backup' in path.lower():
        quality_score = 88  # Good quality for backups
    elif any(x in path for x in ['/units/', '/lessons/', '/handouts/']):
        quality_score = 87  # Standard quality
    else:
        quality_score = 85  # Default
    
    # Check cultural elements from HTML if available
    cultural_context = False
    has_whakatauaki = False
    has_te_reo = False
    content_preview = None
    
    if html_content:
        content_lower = html_content.lower()
        has_whakatauaki = bool(re.search(r'whakataukī|whakatauki', html_content, re.IGNORECASE))
        has_te_reo = bool(re.search(r'te reo|māori|maori|kia ora|whakapapa', html_content, re.IGNORECASE))
        cultural_context = has_te_reo or 'cultural' in content_lower or 'māori' in content_lower
        content_preview = html_content[:500]
        
        # Extract better title from HTML if available
        title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)
        if title_match:
            extracted_title = title_match.group(1).strip()
            extracted_title = re.sub(r'\s+', ' ', extracted_title)
            if len(extracted_title) > 5 and len(extracted_title) < 200:
                title = extracted_title
    
    return {
        'file_path': path,
        'resource_type': resource_type.title(),
        'title': title[:200],  # Limit length
        'quality_score': quality_score,
        'cultural_context': cultural_context,
        'year_level': year_level,
        'subject': subject,
        'has_whakataukī': has_whakatauaki,
        'has_te_reo': has_te_reo,
        'content_preview': content_preview,
        'metadata': {
            'source': 'comprehensive_indexing',
            'indexed_date': str(datetime.now().date()),
            'original_resource_id': str(resource.get('id', '')),
            'tags': resource.get('tags', [])
        }
    }

# Process in batches
batch_size = 100
total_indexed = 0
total_errors = 0
total_skipped = 0

print(f"\n🚀 Starting batch processing...")
print(f"   Batch size: {batch_size}")
print(f"   Total to process: {len(to_index)}")

for i in range(0, len(to_index), batch_size):
    batch = to_index[i:i+batch_size]
    batch_num = i // batch_size + 1
    total_batches = (len(to_index) + batch_size - 1) // batch_size
    
    print(f"\n📦 Batch {batch_num}/{total_batches}: Processing {len(batch)} resources")
    
    batch_records = []
    for resource in batch:
        try:
            path = resource['path']
            
            # Try to read HTML content if it's a file
            html_content = None
            file_path = BASE_DIR / 'public' / path.lstrip('/')
            if not file_path.exists():
                file_path = BASE_DIR / path.lstrip('/')
            
            if file_path.exists() and file_path.suffix in ['.html', '.htm']:
                try:
                    html_content = file_path.read_text(encoding='utf-8', errors='ignore')
                except:
                    pass
            
            # Extract metadata
            record = extract_metadata(resource, html_content)
            batch_records.append(record)
            
        except Exception as e:
            print(f"   ⚠️  Error processing {resource.get('path', 'unknown')}: {str(e)[:60]}")
            total_errors += 1
    
    # Insert batch into GraphRAG
    if batch_records:
        try:
            supabase.table('graphrag_resources').insert(batch_records).execute()
            total_indexed += len(batch_records)
            print(f"   ✅ Indexed {len(batch_records)} resources")
            print(f"   📊 Progress: {total_indexed}/{len(to_index)} ({total_indexed/len(to_index)*100:.1f}%)")
        except Exception as e:
            error_msg = str(e)
            if 'duplicate' in error_msg.lower():
                print(f"   ⚠️  Some duplicates detected, continuing...")
                total_skipped += len(batch_records)
            else:
                print(f"   ❌ Batch error: {error_msg[:100]}")
                total_errors += len(batch_records)
    
    # Progress indicator
    if batch_num % 10 == 0:
        print(f"\n{'='*80}")
        print(f"   CHECKPOINT: {total_indexed} indexed | {total_errors} errors | {total_skipped} skipped")
        print(f"{'='*80}")

# Final summary
print(f"\n{'='*80}")
print(f"✅ INDEXING COMPLETE!")
print(f"{'='*80}")
print(f"   Total processed: {len(to_index)}")
print(f"   Successfully indexed: {total_indexed}")
print(f"   Errors: {total_errors}")
print(f"   Skipped (duplicates): {total_skipped}")
print(f"   Success rate: {total_indexed/(len(to_index) or 1)*100:.1f}%")
print(f"{'='*80}")

# Final verification
print("\n🔍 Final GraphRAG coverage check...")
final_result = supabase.table('graphrag_resources').select('file_path', count='exact').execute()
print(f"   GraphRAG now contains: {final_result.count} resources")
print(f"   Original total in resources table: {len(all_resources)}")
print(f"   Coverage: {final_result.count}/{len(all_resources)} ({final_result.count/len(all_resources)*100:.1f}%)")
print(f"\n🎉 GraphRAG indexing complete!")

