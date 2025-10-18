#!/usr/bin/env python3
"""
Complete Code Files Indexer - ALL JS, PY, CSS, JSON
Direct Supabase API - no terminal dependencies
"""
from supabase import create_client
from pathlib import Path
import re
from datetime import datetime
import json as json_lib

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

BASE_DIR = Path(__file__).parent
EXTENSIONS = {'.js': 'JavaScript', '.py': 'Python Script', '.css': 'Stylesheet', '.json': 'JSON Data'}

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get indexed paths
print("Loading indexed paths...")
indexed = set()
try:
    result = supabase.table('graphrag_resources').select('file_path').execute()
    for r in result.data:
        indexed.add(r['file_path'])
        indexed.add(r['file_path'].lstrip('/'))
except Exception as e:
    print(f"Error loading indexed: {e}")

print(f"Currently indexed: {len(indexed)} files")

# Find all code files
skip = ['node_modules', '.git', '__pycache__', '.netlify/plugins', 'dist/node_modules']
to_index = []

for ext, type_name in EXTENSIONS.items():
    files = BASE_DIR.rglob(f'*{ext}')
    for f in files:
        rel = str(f.relative_to(BASE_DIR))
        if any(s in rel for s in skip):
            continue
        if rel not in indexed and ('/' + rel) not in indexed:
            to_index.append((f, ext, type_name))

print(f"\nFound {len(to_index)} unindexed code files")
by_ext = {}
for f, ext, _ in to_index:
    by_ext[ext] = by_ext.get(ext, 0) + 1
for ext, count in sorted(by_ext.items(), key=lambda x: x[1], reverse=True):
    print(f"  {ext}: {count}")

# Process in batches
def make_record(file_path, ext, type_name):
    rel = str(file_path.relative_to(BASE_DIR))
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        content = ""
    
    # Extract title
    title = None
    if ext == '.json':
        try:
            data = json_lib.loads(content[:5000])
            if isinstance(data, dict):
                title = data.get('name') or data.get('title') or data.get('description')
        except:
            pass
    elif ext in ['.js', '.py']:
        m = re.search(r'(?:"""|/\*\*)\s*\n\s*(?:\*\s*)?(.+?)(?:"""|$)', content)
        if m:
            title = m.group(1).strip()
    
    if not title:
        title = file_path.stem.replace('-', ' ').replace('_', ' ').title()
    
    # Subject mapping
    subj = {'.js': 'Frontend', '.py': 'Backend', '.css': 'Design', '.json': 'Data'}
    
    return {
        'file_path': rel,
        'resource_type': type_name,
        'title': title[:200],
        'quality_score': 80 if 'public/' in rel else 75,
        'cultural_context': bool(re.search(r'māori|maori|cultural|whakataukī', content, re.I)),
        'year_level': 'All Years',
        'subject': subj.get(ext, 'General'),
        'has_whakataukī': bool(re.search(r'whakataukī|whakatauki', content, re.I)),
        'has_te_reo': bool(re.search(r'māori|maori|te reo', content, re.I)),
        'content_preview': content[:500],
        'metadata': {
            'file_type': ext[1:],
            'indexed_date': str(datetime.now().date())
        }
    }

# Index in batches
total = 0
errors = 0
batch_size = 50

print(f"\nIndexing {len(to_index)} files...")
for i in range(0, len(to_index), batch_size):
    batch = to_index[i:i+batch_size]
    records = []
    
    for f, ext, type_name in batch:
        try:
            records.append(make_record(f, ext, type_name))
        except Exception as e:
            errors += 1
    
    if records:
        try:
            supabase.table('graphrag_resources').insert(records).execute()
            total += len(records)
            if (i // batch_size + 1) % 5 == 0:
                print(f"  Progress: {total}/{len(to_index)} ({total/len(to_index)*100:.0f}%)")
        except Exception as e:
            if 'duplicate' not in str(e).lower():
                errors += len(records)

print(f"\n✅ Complete!")
print(f"Indexed: {total} | Errors: {errors}")

# Final check
final = supabase.table('graphrag_resources').select('id', count='exact').execute()
print(f"Total GraphRAG resources: {final.count}")

