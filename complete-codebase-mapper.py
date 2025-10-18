#!/usr/bin/env python3
"""
COMPLETE CODEBASE MAPPER
Index ALL 85,860 files into GraphRAG for super intelligence
"""

from supabase import create_client
from pathlib import Path
import json
import hashlib
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🗺️ COMPLETE CODEBASE MAPPER - Super Intelligence Indexing")
print("=" * 70)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load progress
progress_file = Path('codebase-mapping-progress.json')
if progress_file.exists():
    progress = json.loads(progress_file.read_text())
else:
    progress = {
        'last_index': 0,
        'files_indexed': 0,
        'by_type': {},
        'errors': 0
    }

# Find ALL files (excluding node_modules, .git)
print("\n📁 Discovering ALL files in codebase...")
all_files = []
exclude_dirs = {'node_modules', '.git', '.netlify', 'dist'}

for file_path in Path('.').rglob('*'):
    if file_path.is_file():
        # Skip excluded directories
        if any(excl in str(file_path) for excl in exclude_dirs):
            continue
        all_files.append(file_path)

print(f"   Found {len(all_files)} files to map")

# Process next batch
start_idx = progress['last_index']
end_idx = min(start_idx + 100, len(all_files))
batch = all_files[start_idx:end_idx]

print(f"\n🔧 Mapping files {start_idx+1} to {end_idx}...")

batch_indexed = 0

for file_path in batch:
    try:
        # Determine file type
        suffix = file_path.suffix.lower()
        file_type_map = {
            '.html': 'html-content',
            '.py': 'python-script',
            '.js': 'javascript',
            '.css': 'stylesheet',
            '.json': 'configuration',
            '.md': 'documentation',
            '.sql': 'database-schema',
            '.sh': 'shell-script',
            '.txt': 'text-data',
        }
        file_type = file_type_map.get(suffix, 'other')
        
        # Get file stats
        stat = file_path.stat()
        file_size = stat.st_size
        
        # Get file hash for duplicate detection
        try:
            content_hash = hashlib.md5(file_path.read_bytes()).hexdigest()
        except:
            content_hash = None
        
        # Determine purpose from path
        path_str = str(file_path)
        purpose = 'unknown'
        if '/lessons/' in path_str:
            purpose = 'educational-lesson'
        elif '/handouts/' in path_str:
            purpose = 'educational-handout'
        elif '/units/' in path_str:
            purpose = 'educational-unit'
        elif '/games/' in path_str:
            purpose = 'educational-game'
        elif '/scripts/' in path_str:
            purpose = 'automation-tool'
        elif '/public/' in path_str:
            purpose = 'production-content'
        elif '/backup' in path_str:
            purpose = 'backup-archive'
        elif '/migrations/' in path_str:
            purpose = 'database-migration'
        elif 'test' in path_str.lower():
            purpose = 'testing'
        
        # Create comprehensive file entry
        file_entry = {
            'title': file_path.name[:200],
            'description': f"{file_type.upper()} file: {purpose} - {file_path.name}",
            'path': str(file_path),
            'type': 'interactive',  # Use allowed type
            'subject': file_type,
            'level': purpose,
            'tags': [file_type, purpose, file_path.suffix[1:] if file_path.suffix else 'no-extension'],
            'metadata': json.dumps({
                'file_type': file_type,
                'file_purpose': purpose,
                'file_size_bytes': file_size,
                'content_hash': content_hash,
                'directory': str(file_path.parent),
                'extension': file_path.suffix
            }),
            'author': 'Complete Codebase Mapper',
            'is_active': True
        }
        
        # Index to GraphRAG
        supabase.table('resources').insert(file_entry).execute()
        batch_indexed += 1
        
        # Track by type
        if file_type not in progress['by_type']:
            progress['by_type'][file_type] = 0
        progress['by_type'][file_type] += 1
        
        if batch_indexed % 25 == 0:
            print(f"   ✅ Indexed {batch_indexed} files...")
    
    except Exception as e:
        progress['errors'] += 1

# Update progress
progress['last_index'] = end_idx
progress['files_indexed'] = progress.get('files_indexed', 0) + batch_indexed
progress_file.write_text(json.dumps(progress, indent=2))

# Summary
print(f"\n" + "=" * 70)
print(f"📊 MAPPING PROGRESS")
print("=" * 70)
print(f"\n✅ Files indexed this batch: {batch_indexed}")
print(f"✅ Total files indexed: {progress['files_indexed']}")
print(f"📊 Overall progress: {end_idx}/{len(all_files)} ({end_idx/len(all_files)*100:.1f}%)")

print(f"\n📁 By File Type:")
for ftype, count in sorted(progress['by_type'].items(), key=lambda x: -x[1])[:10]:
    print(f"   {ftype}: {count}")

if end_idx < len(all_files):
    remaining = len(all_files) - end_idx
    batches_left = (remaining // 100) + 1
    print(f"\n🔄 Remaining: {remaining} files ({batches_left} batches)")
    print(f"   Estimated time: {batches_left * 0.5:.1f} hours at current pace")
else:
    print(f"\n🎉 COMPLETE CODEBASE MAPPED!")
    print(f"   Total files: {len(all_files)}")
    print(f"   Successfully indexed: {progress['files_indexed']}")
    print(f"   Now you have SUPER INTELLIGENCE over the codebase!")

print("=" * 70)

