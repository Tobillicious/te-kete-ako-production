#!/usr/bin/env python3
"""
INDEX ALL VERSIONS TO GRAPHRAG
Upload every HTML file from all backups/versions
Tag with version info for comparison
"""

from supabase import create_client
from pathlib import Path
import re
import time

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("📤 INDEXING ALL VERSIONS TO GRAPHRAG")
print("=" * 70)

# Directories to index
sources = [
    ("dist", Path("dist")),
    ("css_backup", Path("backup_before_css_migration")),
    ("backups", Path("backups")),
]

total_uploaded = 0
total_skipped = 0

for source_name, source_path in sources:
    if not source_path.exists():
        continue
    
    print(f"\n📁 Processing {source_name}...")
    
    html_files = [f for f in source_path.rglob("*.html") if 'node_modules' not in str(f)]
    print(f"   Found: {len(html_files)} HTML files")
    
    uploaded_this_source = 0
    
    for i, file_path in enumerate(html_files, 1):
        try:
            # Create unique path with version prefix
            rel_path = str(file_path.relative_to(source_path))
            if rel_path.startswith('public/'):
                rel_path = rel_path[7:]  # Remove 'public/' prefix
            
            unique_path = f"/BACKUP_{source_name}/{rel_path}"
            
            # Extract metadata
            content = file_path.read_text(errors='ignore')[:5000]
            
            title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
            title = title_match.group(1).strip().replace('\n', ' ')[:200] if title_match else file_path.name
            
            desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
            desc = (desc_match.group(1)[:500] if desc_match else f"Backup version: {title}")
            
            # Type detection
            p = str(file_path).lower()
            if '/lessons/' in p: typ = 'lesson'
            elif '/handouts/' in p: typ = 'handout'
            elif '/games/' in p: typ = 'game'
            elif '/units/' in p: typ = 'unit-plan'
            elif 'assess' in p: typ = 'assessment'
            elif 'activity' in p: typ = 'activity'
            elif 'interactive' in p or 'dashboard' in p: typ = 'interactive'
            else: typ = 'lesson'
            
            data = {
                'path': unique_path,
                'title': f"[{source_name}] {title}",
                'description': desc,
                'type': typ,
                'subject': 'Cross-curricular',
                'level': 'All Levels',
                'author': f'Backup-{source_name}',
                'is_active': False,  # Mark backups as inactive
                'difficulty_level': 'intermediate',
                'estimated_duration_minutes': 30,
                'featured': False,
                'tags': ['backup-version', source_name, 'needs-comparison']
            }
            
            supabase.table('resources').upsert(data, on_conflict='path').execute()
            uploaded_this_source += 1
            
            if i % 100 == 0:
                print(f"     {i}/{len(html_files)}: {uploaded_this_source} indexed")
                time.sleep(0.5)
                
        except Exception as e:
            if 'duplicate' not in str(e).lower():
                total_skipped += 1
    
    total_uploaded += uploaded_this_source
    print(f"   ✅ Indexed {uploaded_this_source} files from {source_name}")

print(f"\n{'='*70}")
print(f"📊 INDEXING COMPLETE:")
print(f"   Uploaded: {total_uploaded}")
print(f"   Skipped: {total_skipped}")

# Final count
total = supabase.table('resources').select('*', count='exact').execute()
print(f"\n✅ GRAPHRAG NOW HAS: {total.count} total resources")
print(f"   (includes all current + all backup versions)")

print(f"\n🎯 Next: Query GraphRAG to compare versions and find best content!")

