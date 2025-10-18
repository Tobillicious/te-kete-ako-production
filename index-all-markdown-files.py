#!/usr/bin/env python3
"""
Markdown File Indexer - Index ALL .md files to GraphRAG
Complete the knowledge graph with documentation and markdown content
"""
from supabase import create_client
from pathlib import Path
import re
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("📝 MARKDOWN FILE INDEXER")
print("=" * 80)
print("Indexing ALL .md files to GraphRAG...")
print("=" * 80)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
BASE_DIR = Path(__file__).parent

# Get indexed MD files
print("\n📊 Checking current MD file coverage...")
indexed_md = supabase.table('graphrag_resources')\
    .select('file_path')\
    .like('file_path', '%.md')\
    .execute()

indexed_paths = set()
for item in indexed_md.data:
    path = item['file_path']
    indexed_paths.add(path)
    indexed_paths.add(path.lstrip('/'))
    indexed_paths.add('/' + path.lstrip('/'))
    indexed_paths.add(str(BASE_DIR / path))

print(f"   Already indexed: {len(indexed_md.data)} MD files")

# Find ALL markdown files
print("\n🔍 Scanning for markdown files...")
all_md_files = list(BASE_DIR.rglob('*.md'))
print(f"   Found {len(all_md_files)} total MD files")

# Filter to unindexed, skip node_modules
skip_patterns = ['node_modules', '.git', '__pycache__', '.netlify']
to_index = []

for file_path in all_md_files:
    rel_path = str(file_path.relative_to(BASE_DIR))
    
    # Skip certain directories
    if any(pattern in rel_path for pattern in skip_patterns):
        continue
    
    # Check if already indexed
    if (rel_path not in indexed_paths and 
        '/' + rel_path not in indexed_paths and
        str(file_path) not in indexed_paths):
        to_index.append(file_path)

print(f"   Unindexed: {len(to_index)} MD files")
print(f"   Coverage: {len(indexed_md.data)}/{len(to_index) + len(indexed_md.data)} ({len(indexed_md.data)/(len(to_index) + len(indexed_md.data))*100:.1f}%)")

# Categorize
categories = {}
for file_path in to_index:
    rel_path = str(file_path.relative_to(BASE_DIR))
    
    if 'README' in file_path.name.upper():
        cat = 'README'
    elif any(x in rel_path.lower() for x in ['doc', 'guide', 'instruction']):
        cat = 'documentation'
    elif any(x in rel_path.lower() for x in ['plan', 'roadmap', 'strategy']):
        cat = 'planning'
    elif any(x in rel_path.lower() for x in ['report', 'audit', 'analysis']):
        cat = 'reports'
    elif 'archive' in rel_path.lower():
        cat = 'archives'
    elif 'backup' in rel_path.lower():
        cat = 'backups'
    elif any(x in rel_path.lower() for x in ['unit', 'lesson', 'handout']):
        cat = 'educational'
    elif 'agent' in rel_path.lower() or 'coordination' in rel_path.lower():
        cat = 'agent-coordination'
    else:
        cat = 'other'
    
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(file_path)

print(f"\n📦 Breakdown:")
for cat, files in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"   {cat}: {len(files)} files")

# Extract metadata from MD files
def extract_md_metadata(file_path):
    """Extract metadata from Markdown file"""
    rel_path = str(file_path.relative_to(BASE_DIR))
    
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        content = ""
    
    # Extract title (first # heading or filename)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        # Remove emojis and clean
        title = re.sub(r'[🎉🔥💡📊🌟✅❌⚠️🚀📝🎯💪🏆]', '', title)
        title = title.strip()
    else:
        title = file_path.stem.replace('-', ' ').replace('_', ' ').title()
    
    # Determine type
    filename_upper = file_path.name.upper()
    rel_lower = rel_path.lower()
    
    if 'README' in filename_upper:
        resource_type = 'Documentation'
    elif any(x in rel_lower for x in ['guide', 'instruction', 'tutorial']):
        resource_type = 'Guide'
    elif any(x in rel_lower for x in ['plan', 'roadmap', 'strategy']):
        resource_type = 'Planning Document'
    elif any(x in rel_lower for x in ['report', 'audit', 'analysis']):
        resource_type = 'Report'
    elif any(x in rel_lower for x in ['unit', 'lesson']):
        resource_type = 'Educational Documentation'
    elif 'agent' in rel_lower or 'coordination' in rel_lower:
        resource_type = 'Agent Coordination'
    else:
        resource_type = 'Documentation'
    
    # Subject
    subject = 'Documentation'
    if any(x in content.lower() for x in ['mathematics', 'maths', 'algebra']):
        subject = 'Mathematics Documentation'
    elif 'science' in content.lower():
        subject = 'Science Documentation'
    elif 'english' in content.lower() or 'literacy' in content.lower():
        subject = 'English Documentation'
    elif 'social studies' in content.lower() or 'history' in content.lower():
        subject = 'Social Studies Documentation'
    elif 'technical' in content.lower() or 'development' in content.lower():
        subject = 'Technical Documentation'
    elif 'cultural' in content.lower() or 'māori' in content.lower():
        subject = 'Cultural Documentation'
    
    # Quality based on type
    if 'README' in filename_upper:
        quality = 90
    elif 'guide' in rel_lower or 'instruction' in rel_lower:
        quality = 88
    elif 'report' in rel_lower or 'analysis' in rel_lower:
        quality = 85
    else:
        quality = 83
    
    # Cultural elements
    content_lower = content.lower()
    has_whakatauaki = bool(re.search(r'whakataukī|whakatauki', content, re.IGNORECASE))
    has_te_reo = bool(re.search(r'te reo|māori|maori|kia ora|whakapapa|kaitiaki|mātauranga|iwi|ngā|tino rangatiratanga', content, re.IGNORECASE))
    cultural_context = has_te_reo or 'cultural' in content_lower
    
    # Year level (if mentioned)
    year_match = re.search(r'[Yy]ear\s*(\d+)|Y(\d+)', content)
    year_level = f"Year {year_match.group(1) or year_match.group(2)}" if year_match else "All Years"
    
    return {
        'file_path': rel_path,
        'resource_type': resource_type,
        'title': title[:200],
        'quality_score': quality,
        'cultural_context': cultural_context,
        'year_level': year_level,
        'subject': subject,
        'has_whakataukī': has_whakatauaki,
        'has_te_reo': has_te_reo,
        'content_preview': content[:500] if content else None,
        'metadata': {
            'source': 'markdown_indexing',
            'indexed_date': str(datetime.now().date()),
            'file_type': 'markdown',
            'file_size': file_path.stat().st_size,
            'directory': str(file_path.parent.relative_to(BASE_DIR))
        }
    }

# Process in batches
print(f"\n🚀 Processing {len(to_index)} markdown files...")
batch_size = 100
total_indexed = 0
total_errors = 0

for i in range(0, len(to_index), batch_size):
    batch_files = to_index[i:i+batch_size]
    batch_num = i // batch_size + 1
    total_batches = (len(to_index) + batch_size - 1) // batch_size
    
    print(f"\n📦 Batch {batch_num}/{total_batches}: Processing {len(batch_files)} files")
    
    batch_records = []
    for file_path in batch_files:
        try:
            record = extract_md_metadata(file_path)
            batch_records.append(record)
        except Exception as e:
            print(f"   ⚠️ Error: {file_path.name}: {str(e)[:50]}")
            total_errors += 1
    
    # Insert
    if batch_records:
        try:
            supabase.table('graphrag_resources').insert(batch_records).execute()
            total_indexed += len(batch_records)
            print(f"   ✅ Indexed {len(batch_records)} files")
            print(f"   📊 Progress: {total_indexed}/{len(to_index)} ({total_indexed/len(to_index)*100:.1f}%)")
        except Exception as e:
            error_msg = str(e)
            if 'duplicate' in error_msg.lower():
                print(f"   ℹ️  Some duplicates skipped")
            else:
                print(f"   ❌ Error: {error_msg[:100]}")
                total_errors += len(batch_records)
    
    if batch_num % 10 == 0:
        print(f"\n{'='*80}")
        print(f"   CHECKPOINT: {total_indexed} indexed | {total_errors} errors")
        print(f"{'='*80}")

# Final summary
print(f"\n{'='*80}")
print(f"✅ MARKDOWN INDEXING COMPLETE!")
print(f"{'='*80}")
print(f"   Files processed: {len(to_index)}")
print(f"   Successfully indexed: {total_indexed}")
print(f"   Errors: {total_errors}")
print(f"   Success rate: {total_indexed/(len(to_index) or 1)*100:.1f}%")
print(f"{'='*80}")

# Final count
final_md = supabase.table('graphrag_resources')\
    .select('id', count='exact')\
    .like('file_path', '%.md')\
    .execute()
    
final_all = supabase.table('graphrag_resources')\
    .select('id', count='exact')\
    .execute()

print(f"\n📊 FINAL GRAPHRAG STATUS:")
print(f"   Total MD files indexed: {final_md.count}")
print(f"   Total resources (HTML + MD): {final_all.count}")
print(f"\n🎉 ALL MARKDOWN FILES NOW IN GRAPHRAG!")

