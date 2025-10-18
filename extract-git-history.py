#!/usr/bin/env python3
"""
EXTRACT GIT HISTORY GOLD
Find all deleted files in git history and index them to GraphRAG
"""

from supabase import create_client
import subprocess
import time

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SERVICE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

supabase = create_client(SUPABASE_URL, SERVICE_KEY)

print("💎 EXTRACTING GOLD FROM GIT HISTORY")
print("=" * 70)

# Get existing
print("📥 Loading existing...")
existing = set()
offset = 0
while True:
    batch = supabase.table('resources').select('path').range(offset, offset + 999).execute()
    if not batch.data:
        break
    existing.update(r['path'] for r in batch.data)
    offset += 1000
    if len(batch.data) < 1000:
        break
print(f"   Existing: {len(existing)}\n")

# Get all deleted files
print("🔍 Finding deleted files in git history...")
result = subprocess.run(
    ['git', 'log', '--all', '--pretty=format:', '--name-only', '--diff-filter=D'],
    capture_output=True,
    text=True
)

deleted_files = []
for line in result.stdout.split('\n'):
    line = line.strip()
    if line and (line.endswith('.html') or line.endswith('.js') or 
                 line.endswith('.css') or line.endswith('.py') or 
                 line.endswith('.json') or line.endswith('.md')):
        deleted_files.append(line)

# Remove duplicates
deleted_files = list(set(deleted_files))
print(f"   Found {len(deleted_files)} deleted files\n")

# Get the content of each deleted file from git
print("📜 Extracting content from git history...")
batch = []
indexed = 0
errors = 0

for i, filepath in enumerate(deleted_files, 1):
    try:
        path = f"/GIT_HISTORY/{filepath}"
        
        if path in existing:
            continue
        
        # Get the last commit where this file existed
        commit_result = subprocess.run(
            ['git', 'rev-list', '-n', '1', 'HEAD', '--', filepath],
            capture_output=True,
            text=True
        )
        
        if not commit_result.stdout.strip():
            # Try all branches
            commit_result = subprocess.run(
                ['git', 'rev-list', '-n', '1', '--all', '--', filepath],
                capture_output=True,
                text=True
            )
        
        commit = commit_result.stdout.strip()
        if not commit:
            continue
        
        # Get file content from that commit
        content_result = subprocess.run(
            ['git', 'show', f'{commit}:{filepath}'],
            capture_output=True,
            text=True,
            errors='ignore'
        )
        
        if content_result.returncode != 0:
            continue
        
        content = content_result.stdout[:500]  # Preview
        
        # Determine type
        ext = filepath.split('.')[-1]
        if ext == 'html':
            resource_type = 'lesson'
        elif ext in ['js', 'css', 'py']:
            resource_type = 'interactive'
        else:
            resource_type = 'interactive'
        
        # Extract title from filename
        filename = filepath.split('/')[-1]
        title = filename.replace('-', ' ').replace('_', ' ').replace('.html', '').title()
        
        data = {
            'path': path,
            'title': f"[DELETED] {title}",
            'description': f"Deleted file from git history: {filepath} (commit {commit[:8]})",
            'type': resource_type,
            'subject': 'Historical',
            'level': 'Archive',
            'author': 'Git-History',
            'is_active': False,
            'difficulty_level': 'intermediate',
            'estimated_duration_minutes': 0,
            'featured': False,
            'tags': ['git-history', 'deleted', f'deleted-{ext}'],
            'cultural_elements': {}
        }
        
        batch.append(data)
        existing.add(path)
        
        # Upload in batches
        if len(batch) >= 50:
            supabase.table('resources').upsert(batch, on_conflict='path').execute()
            indexed += len(batch)
            batch = []
            print(f"   Progress: {i}/{len(deleted_files)} ({indexed} indexed)")
            time.sleep(0.3)
    
    except Exception as e:
        errors += 1
        if errors < 10:
            print(f"   ⚠️  {filepath}: {str(e)[:50]}")

# Upload remaining
if batch:
    supabase.table('resources').upsert(batch, on_conflict='path').execute()
    indexed += len(batch)

print(f"\n{'='*70}")
print(f"✅ GIT HISTORY EXTRACTION COMPLETE!")
print(f"   Indexed: {indexed}")
print(f"   Errors: {errors}")

# Final count
total = supabase.table('resources').select('*', count='exact').execute()
print(f"\n📊 GRAPHRAG ULTIMATE TOTAL: {total.count} resources")
print(f"💎 Including deleted git history gold!")

