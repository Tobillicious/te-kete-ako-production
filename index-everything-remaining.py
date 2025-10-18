#!/usr/bin/env python3
"""
INDEX EVERYTHING REMAINING
Archive, docs, reports, scripts, supabase, units - ALL FILES!
"""

from supabase import create_client
from pathlib import Path
import time

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SERVICE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

supabase = create_client(SUPABASE_URL, SERVICE_KEY)

print("🔍 INDEXING ALL REMAINING DIRECTORIES")
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

# Directories to index
directories = [
    ('archive', Path('archive')),
    ('docs', Path('docs')),
    ('reports', Path('reports')),
    ('scripts', Path('scripts')),
    ('supabase', Path('supabase')),
    ('units', Path('units')),
    ('archived-bloat', Path('archived-bloat')),
    ('backup_before_minification', Path('backup_before_minification')),
]

# File extensions to index
extensions = ['.html', '.js', '.css', '.py', '.json', '.md', '.sql', '.txt', '.yml', '.yaml', '.sh']

grand_total = 0

for dir_name, dir_path in directories:
    if not dir_path.exists():
        continue
    
    print(f"📂 {dir_name.upper()}/")
    
    # Find all files with interesting extensions
    files = []
    for ext in extensions:
        found = list(dir_path.rglob(f'*{ext}'))
        files.extend([f for f in found if 'node_modules' not in str(f) and '.git' not in str(f)])
    
    # Remove duplicates
    files = list(set(files))
    print(f"   Found: {len(files)} files")
    
    batch = []
    indexed = 0
    skipped = 0
    
    for i, fp in enumerate(files, 1):
        try:
            path = f"/ARCHIVE_{dir_name}/{str(fp.relative_to(dir_path))}"
            
            if path in existing:
                skipped += 1
                continue
            
            # Read preview
            try:
                preview = fp.read_text(errors='ignore')[:500]
            except:
                preview = ""
            
            # Determine type
            ext = fp.suffix.lower()
            if ext == '.html':
                resource_type = 'lesson'
            elif ext in ['.js', '.css', '.py', '.sh']:
                resource_type = 'interactive'
            elif ext in ['.json', '.yml', '.yaml']:
                resource_type = 'interactive'
            elif ext == '.md':
                resource_type = 'interactive'
            elif ext == '.sql':
                resource_type = 'interactive'
            else:
                resource_type = 'interactive'
            
            # Title
            title = fp.name.replace('-', ' ').replace('_', ' ').title()
            
            data = {
                'path': path,
                'title': f"[{dir_name}] {title}",
                'description': f"Archive file from {dir_name}: {fp.name}",
                'type': resource_type,
                'subject': 'Technical',
                'level': 'Developer',
                'author': f'Archive-{dir_name}',
                'is_active': False,  # Archive files inactive
                'difficulty_level': 'advanced',
                'estimated_duration_minutes': 0,
                'featured': False,
                'tags': [f'archive-{dir_name}', 'system-file', ext[1:] if ext else 'other'],
                'cultural_elements': {}
            }
            
            batch.append(data)
            existing.add(path)
            
            # Upload in batches
            if len(batch) >= 100:
                supabase.table('resources').upsert(batch, on_conflict='path').execute()
                indexed += len(batch)
                batch = []
                if i % 200 == 0:
                    print(f"   Progress: {i}/{len(files)} ({indexed} new, {skipped} skipped)")
                time.sleep(0.3)
        
        except Exception as e:
            if 'duplicate' not in str(e).lower() and indexed < 5:
                print(f"   ⚠️  {fp.name}: {str(e)[:50]}")
    
    # Upload remaining
    if batch:
        supabase.table('resources').upsert(batch, on_conflict='path').execute()
        indexed += len(batch)
    
    print(f"   ✅ {indexed} new, {skipped} skipped\n")
    grand_total += indexed

print("=" * 70)
print(f"✅ ALL REMAINING DIRECTORIES INDEXED!")
print(f"   Total new: {grand_total}")

# Final count
total = supabase.table('resources').select('*', count='exact').execute()
print(f"\n📊 GRAPHRAG MEGA TOTAL: {total.count} resources")
print(f"🎉 COMPLETE CODEBASE INDEXED!")

