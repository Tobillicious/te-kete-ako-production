#!/usr/bin/env python3
"""
Filesystem GraphRAG Indexer - Index ALL HTML files from disk
Covers files not in resources table (archives, backups, etc.)
"""
from supabase import create_client
from pathlib import Path
import re
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🗂️  FILESYSTEM GRAPHRAG INDEXER")
print("=" * 80)
print("📂 Scanning entire project for HTML files...")
print("=" * 80)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
BASE_DIR = Path(__file__).parent

# Get all indexed paths from GraphRAG
print("\n📊 Loading GraphRAG index...")
indexed_paths_list = []
offset = 0
page_size = 1000
while True:
    result = supabase.table('graphrag_resources').select('file_path').range(offset, offset + page_size - 1).execute()
    batch = result.data
    if not batch:
        break
    indexed_paths_list.extend([r['file_path'] for r in batch])
    offset += page_size
    if len(batch) < page_size:
        break

print(f"   Already indexed: {len(indexed_paths_list)} paths")

# Create normalized path set for comparison
indexed_paths_set = set()
for path in indexed_paths_list:
    # Add all variations
    indexed_paths_set.add(path)
    indexed_paths_set.add(path.lstrip('/'))
    indexed_paths_set.add('/' + path.lstrip('/'))
    if not path.startswith('public/'):
        indexed_paths_set.add('public/' + path.lstrip('/'))
    indexed_paths_set.add(str(BASE_DIR / path))
    indexed_paths_set.add(str(BASE_DIR / path.lstrip('/')))

print(f"   Created {len(indexed_paths_set)} path variations for matching")

# Find ALL HTML files
print("\n🔍 Scanning filesystem...")
all_html_files = list(BASE_DIR.rglob('*.html'))
print(f"   Found {len(all_html_files)} HTML files total")

# Filter to unindexed files
to_index = []
for file_path in all_html_files:
    rel_path = str(file_path.relative_to(BASE_DIR))
    
    # Check if already indexed (any variation)
    if (rel_path in indexed_paths_set or
        ('/' + rel_path) in indexed_paths_set or
        rel_path.lstrip('/') in indexed_paths_set or
        ('public/' + rel_path.lstrip('/')) in indexed_paths_set or
        str(file_path) in indexed_paths_set):
        continue
    
    to_index.append(file_path)

print(f"   Unindexed: {len(to_index)} files")
print(f"   Coverage: {len(indexed_paths_list)}/{len(all_html_files)} ({len(indexed_paths_list)/len(all_html_files)*100:.1f}%)")

# Categorize
categories = {}
skip_patterns = ['node_modules', '.git', 'dist', '__pycache__', 'lighthouse']
filtered_to_index = []

for file_path in to_index:
    rel_path = str(file_path.relative_to(BASE_DIR))
    
    # Skip certain directories
    if any(pattern in rel_path for pattern in skip_patterns):
        continue
    
    filtered_to_index.append(file_path)
    
    # Categorize
    if '/lessons/' in rel_path:
        cat = 'lessons'
    elif '/handouts/' in rel_path:
        cat = 'handouts'
    elif '/units/' in rel_path:
        cat = 'units'
    elif '/games/' in rel_path:
        cat = 'games'
    elif '/assessment' in rel_path:
        cat = 'assessments'
    elif 'archive' in rel_path:
        cat = 'archive'
    elif 'backup' in rel_path.lower():
        cat = 'backup'
    else:
        cat = 'other'
    
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(file_path)

print(f"\n📦 After filtering: {len(filtered_to_index)} files to index")
print("\nBreakdown:")
for cat, items in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"   {cat}: {len(items)}")

# Process in batches
def extract_metadata_from_file(file_path):
    """Extract metadata from HTML file"""
    rel_path = str(file_path.relative_to(BASE_DIR))
    
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        content = ""
    
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        title = re.sub(r'\s+', ' ', title)
    else:
        title = file_path.stem.replace('-', ' ').title()
    
    # Determine type
    if '/lessons/' in rel_path:
        resource_type = 'lesson'
    elif '/handouts/' in rel_path:
        resource_type = 'handout'
    elif '/units/' in rel_path:
        resource_type = 'unit-plan'
    elif '/games/' in rel_path:
        resource_type = 'game'
    elif '/assessment' in rel_path:
        resource_type = 'assessment'
    else:
        resource_type = 'page'
    
    # Subject
    subject = 'Multi-subject'
    rel_lower = rel_path.lower()
    if 'math' in rel_lower:
        subject = 'Mathematics'
    elif 'science' in rel_lower:
        subject = 'Science'
    elif 'english' in rel_lower or 'literacy' in rel_lower:
        subject = 'English'
    elif 'social' in rel_lower or 'history' in rel_lower:
        subject = 'Social Studies'
    elif 'digital' in rel_lower or 'tech' in rel_lower:
        subject = 'Digital Technologies'
    
    # Quality score
    if 'archive' in rel_lower or 'backup' in rel_lower:
        quality_score = 85  # Lower for archived
    elif 'generated' in rel_lower:
        quality_score = 90  # Higher for generated
    else:
        quality_score = 87  # Standard
    
    # Cultural elements
    content_lower = content.lower()
    has_whakatauaki = bool(re.search(r'whakataukī|whakatauki', content, re.IGNORECASE))
    has_te_reo = bool(re.search(r'te reo|māori|maori|kia ora|whakapapa|kaitiaki', content, re.IGNORECASE))
    cultural_context = has_te_reo or 'cultural' in content_lower
    
    # Year level
    year_match = re.search(r'[Yy]ear?\s*(\d+)|Y(\d+)', content + rel_path)
    year_level = f"Year {year_match.group(1) or year_match.group(2)}" if year_match else "All Years"
    
    return {
        'file_path': rel_path,
        'resource_type': resource_type.title(),
        'title': title[:200],
        'quality_score': quality_score,
        'cultural_context': cultural_context,
        'year_level': year_level,
        'subject': subject,
        'has_whakataukī': has_whakatauaki,
        'has_te_reo': has_te_reo,
        'content_preview': content[:500] if content else None,
        'metadata': {
            'source': 'filesystem_scan',
            'indexed_date': str(datetime.now().date()),
            'file_size': file_path.stat().st_size,
            'last_modified': str(datetime.fromtimestamp(file_path.stat().st_mtime).date())
        }
    }

# Batch processing
batch_size = 100
total_indexed = 0
total_errors = 0
total_skipped = 0

print(f"\n🚀 Processing {len(filtered_to_index)} files...")

for i in range(0, len(filtered_to_index), batch_size):
    batch_files = filtered_to_index[i:i+batch_size]
    batch_num = i // batch_size + 1
    total_batches = (len(filtered_to_index) + batch_size - 1) // batch_size
    
    print(f"\n📦 Batch {batch_num}/{total_batches}: Processing {len(batch_files)} files")
    
    batch_records = []
    for file_path in batch_files:
        try:
            record = extract_metadata_from_file(file_path)
            batch_records.append(record)
        except Exception as e:
            print(f"   ⚠️  Error: {file_path.name}: {str(e)[:50]}")
            total_errors += 1
    
    # Insert
    if batch_records:
        try:
            supabase.table('graphrag_resources').insert(batch_records).execute()
            total_indexed += len(batch_records)
            print(f"   ✅ Indexed {len(batch_records)} files")
            print(f"   📊 Progress: {total_indexed}/{len(filtered_to_index)} ({total_indexed/len(filtered_to_index)*100:.1f}%)")
        except Exception as e:
            error_msg = str(e)
            if 'duplicate' in error_msg.lower():
                print(f"   ⚠️  Duplicates detected, skipping...")
                total_skipped += len(batch_records)
            else:
                print(f"   ❌ Error: {error_msg[:80]}")
                total_errors += len(batch_records)
    
    if batch_num % 10 == 0:
        print(f"\n{'='*80}")
        print(f"   CHECKPOINT: {total_indexed} indexed | {total_errors} errors | {total_skipped} skipped")
        print(f"{'='*80}")

# Final summary
print(f"\n{'='*80}")
print(f"✅ FILESYSTEM INDEXING COMPLETE!")
print(f"{'='*80}")
print(f"   Total processed: {len(filtered_to_index)}")
print(f"   Successfully indexed: {total_indexed}")
print(f"   Errors: {total_errors}")
print(f"   Skipped (duplicates): {total_skipped}")
print(f"{'='*80}")

# Final count
final_result = supabase.table('graphrag_resources').select('file_path', count='exact').execute()
print(f"\n🎉 GraphRAG now contains: {final_result.count} resources")
print(f"   Coverage of filesystem: {final_result.count}/{len(all_html_files)} ({final_result.count/len(all_html_files)*100:.1f}%)")

