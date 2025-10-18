#!/usr/bin/env python3
"""
Code Files Indexer - Index ALL JS, PY, CSS, JSON files
Complete the GraphRAG with code, scripts, configs, and data
"""
from supabase import create_client
from pathlib import Path
import re
from datetime import datetime
import json as json_lib

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("💻 CODE FILES INDEXER")
print("=" * 80)
print("Indexing ALL code files: .js, .py, .css, .json")
print("=" * 80)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
BASE_DIR = Path(__file__).parent

# Extensions to index
EXTENSIONS = ['.js', '.py', '.css', '.json']

# Get currently indexed code files
print("\n📊 Checking current coverage...")
indexed_result = supabase.table('graphrag_resources').select('file_path').execute()
indexed_paths = set()
for item in indexed_result.data:
    path = item['file_path']
    indexed_paths.add(path)
    indexed_paths.add(path.lstrip('/'))
    indexed_paths.add('/' + path.lstrip('/'))

print(f"   Total indexed: {len(indexed_result.data)} resources")

# Find ALL code files
print("\n🔍 Scanning for code files...")
all_code_files = []
for ext in EXTENSIONS:
    files = list(BASE_DIR.rglob(f'*{ext}'))
    all_code_files.extend(files)

print(f"   Found {len(all_code_files)} total code files")

# Filter unindexed, skip unwanted
skip_patterns = ['node_modules', '.git', '__pycache__', '.netlify', 'dist/node_modules', '.cursor']
to_index = []

for file_path in all_code_files:
    rel_path = str(file_path.relative_to(BASE_DIR))
    
    # Skip
    if any(pattern in rel_path for pattern in skip_patterns):
        continue
    
    # Check if indexed
    if rel_path not in indexed_paths and ('/' + rel_path) not in indexed_paths:
        to_index.append(file_path)

print(f"   Unindexed: {len(to_index)} files")

# Categorize
by_type = {'.js': [], '.py': [], '.css': [], '.json': []}
for file_path in to_index:
    ext = file_path.suffix
    if ext in by_type:
        by_type[ext].append(file_path)

print(f"\n📦 Breakdown:")
for ext, files in sorted(by_type.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"   {ext}: {len(files)} files")

# Extract metadata
def extract_code_metadata(file_path):
    """Extract metadata from code files"""
    rel_path = str(file_path.relative_to(BASE_DIR))
    ext = file_path.suffix
    
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        content = ""
    
    # Extract title/description
    title = None
    if ext == '.js':
        # Look for JSDoc comment or description
        match = re.search(r'\/\*\*\s*\n\s*\*\s*(.+?)\n', content)
        if match:
            title = match.group(1).strip()
        resource_type = 'JavaScript'
        subject = 'Frontend Code'
    elif ext == '.py':
        # Look for docstring
        match = re.search(r'"""(.+?)"""', content, re.DOTALL)
        if match:
            title = match.group(1).strip().split('\n')[0]
        resource_type = 'Python Script'
        subject = 'Backend Code'
    elif ext == '.css':
        # Look for header comment
        match = re.search(r'/\*\s*(.+?)\s*\*/', content)
        if match:
            title = match.group(1).strip()
        resource_type = 'Stylesheet'
        subject = 'Design System'
    elif ext == '.json':
        # Try to parse and get description
        try:
            data = json_lib.loads(content)
            if isinstance(data, dict):
                title = data.get('name') or data.get('title') or data.get('description')
        except:
            pass
        resource_type = 'JSON Data'
        subject = 'Configuration'
    
    if not title:
        title = file_path.stem.replace('-', ' ').replace('_', ' ').title()
    
    # Quality based on type and location
    if 'public/' in rel_path:
        quality = 85
    elif 'scripts/' in rel_path:
        quality = 80
    elif 'backup' in rel_path.lower():
        quality = 75
    else:
        quality = 78
    
    # Check for cultural content
    content_lower = content.lower()
    has_te_reo = bool(re.search(r'māori|maori|kia ora|whakapapa|kaitiaki', content, re.IGNORECASE))
    has_whakatauaki = 'whakataukī' in content_lower or 'whakatauki' in content_lower
    
    return {
        'file_path': rel_path,
        'resource_type': resource_type,
        'title': title[:200],
        'quality_score': quality,
        'cultural_context': has_te_reo,
        'year_level': 'All Years',
        'subject': subject,
        'has_whakataukī': has_whakatauaki,
        'has_te_reo': has_te_reo,
        'content_preview': content[:500] if content else None,
        'metadata': {
            'source': 'code_files_indexing',
            'indexed_date': str(datetime.now().date()),
            'file_type': ext[1:],  # Remove dot
            'file_size': file_path.stat().st_size
        }
    }

# Process
print(f"\n🚀 Processing {len(to_index)} code files...")
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
            record = extract_code_metadata(file_path)
            batch_records.append(record)
        except Exception as e:
            print(f"   ⚠️ Error: {file_path.name}: {str(e)[:40]}")
            total_errors += 1
    
    if batch_records:
        try:
            supabase.table('graphrag_resources').insert(batch_records).execute()
            total_indexed += len(batch_records)
            if batch_num % 5 == 0:
                print(f"   ✅ Indexed {total_indexed}/{len(to_index)} ({total_indexed/len(to_index)*100:.1f}%)")
        except Exception as e:
            if 'duplicate' not in str(e).lower():
                print(f"   ❌ Error: {str(e)[:80]}")
                total_errors += len(batch_records)

print(f"\n{'='*80}")
print(f"✅ CODE FILES INDEXING COMPLETE!")
print(f"{'='*80}")
print(f"   Processed: {len(to_index)}")
print(f"   Indexed: {total_indexed}")
print(f"   Errors: {total_errors}")
print(f"{'='*80}")

# Final stats
final = supabase.table('graphrag_resources').select('id', count='exact').execute()
print(f"\n🎉 TOTAL GRAPHRAG RESOURCES: {final.count}")

