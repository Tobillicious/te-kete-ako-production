#!/usr/bin/env python3
"""
FAST INDEX ALL HTML - Working with actual schema
Index all HTML files from backups using BATCH inserts for speed
"""

from supabase import create_client
from pathlib import Path
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("🚀 FAST HTML INDEXING - ALL VERSIONS")
print("=" * 70)

# Directories to index
sources = [
    ("dist", Path("dist")),
    ("css_backup", Path("backup_before_css_migration")),
    ("backups", Path("backups")),
]

# Get all existing paths ONCE at the start
print("📥 Loading existing paths...")
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

print(f"   Found {len(existing)} existing resources\n")

total_indexed = 0

for source_name, source_path in sources:
    if not source_path.exists():
        continue
    
    print(f"📂 {source_name}/")
    files = [f for f in source_path.rglob("*.html") if 'node_modules' not in str(f)]
    print(f"   Files: {len(files)}")
    
    # Batch processing
    batch = []
    indexed = 0
    
    for i, fp in enumerate(files, 1):
        try:
            # Create unique path
            rel = str(fp.relative_to(source_path))
            if rel.startswith('public/'):
                rel = rel[7:]
            path = f"/BACKUP_{source_name}/{rel}"
            
            # Skip if already exists
            if path in existing:
                continue
            
            # Extract metadata quickly
            content = fp.read_text(errors='ignore')[:3000]
            
            title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
            title = title_m.group(1).strip()[:200] if title_m else fp.name
            
            desc_m = re.search(r'<meta name="description" content="(.*?)"', content)
            desc = desc_m.group(1)[:500] if desc_m else f"Backup: {title}"
            
            # Type detection
            p = str(fp).lower()
            typ = ('lesson' if '/lessons/' in p or 'lesson' in p else
                   'handout' if '/handouts/' in p or 'handout' in p else
                   'game' if '/games/' in p or 'game' in p else
                   'unit-plan' if '/units/' in p else
                   'assessment' if 'assess' in p else
                   'activity' if 'activity' in p else
                   'interactive' if 'interactive' in p or 'dashboard' in p else
                   'lesson')
            
            # Subject
            subj = ('Mathematics' if 'math' in p else
                    'Science' if 'science' in p else
                    'English' if 'english' in p or 'writing' in p else
                    'Te Reo Māori' if 'te-reo' in p or 'maori' in p else
                    'Social Studies' if 'social' in p else
                    'Cross-curricular')
            
            batch.append({
                'path': path,
                'title': title,
                'description': desc,
                'type': typ,
                'subject': subj,
                'level': 'All Levels',
                'author': f'Backup-{source_name}',
                'is_active': False,  # Backups inactive
                'difficulty_level': 'intermediate',
                'estimated_duration_minutes': 30,
                'featured': False,
                'tags': ['backup-version', source_name, 'teaching-option']
            })
            
            # Upload in batches of 50
            if len(batch) >= 50:
                supabase.table('resources').upsert(batch, on_conflict='path').execute()
                indexed += len(batch)
                existing.update(item['path'] for item in batch)
                batch = []
                print(f"   Progress: {i}/{len(files)} ({indexed} new)")
                
        except Exception as e:
            if 'duplicate' not in str(e).lower():
                print(f"   ⚠️  Skip {fp.name}: {str(e)[:40]}")
    
    # Upload remaining
    if batch:
        supabase.table('resources').upsert(batch, on_conflict='path').execute()
        indexed += len(batch)
    
    print(f"   ✅ Indexed {indexed} new from {source_name}\n")
    total_indexed += indexed

print("=" * 70)
print(f"✅ INDEXING COMPLETE!")
print(f"   New resources: {total_indexed}")

# Final count
total = supabase.table('resources').select('*', count='exact').execute()
print(f"\n📊 GraphRAG total: {total.count} resources")
print(f"🎉 Ready for version comparison and merging!")

