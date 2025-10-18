#!/usr/bin/env python3
"""
AGGRESSIVE GRAPHRAG EXCAVATION
Target the biggest gaps - add 200+ files per run
"""

from supabase import create_client
from pathlib import Path
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🔥 AGGRESSIVE GRAPHRAG EXCAVATION")
print("=" * 70)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_graphrag_paths():
    resources = supabase.table('resources').select('path').execute()
    return {r['path'].replace('/public/', '').replace('public/', '') for r in resources.data}

def add_file(file_path):
    """Quick add with minimal processing"""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1).replace(' | Te Kete Ako', '').strip()[:200] if title_match else file_path.stem[:200]
        
        desc_match = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
        description = (desc_match.group(1)[:500] if desc_match else title)
        
        path_str = str(file_path).lower()
        if 'lesson' in path_str:
            rtype = 'lesson'
        elif 'handout' in path_str:
            rtype = 'handout'
        elif 'game' in path_str:
            rtype = 'game'
        elif 'assessment' in path_str:
            rtype = 'assessment'
        elif 'unit' in path_str:
            rtype = 'unit-plan'
        elif 'activity' in path_str:
            rtype = 'activity'
        else:
            rtype = 'interactive'
        
        cultural = content.lower().count('māori') + content.lower().count('tikanga')
        
        resource = {
            'title': title,
            'path': str(file_path.relative_to('public')),
            'type': rtype,
            'subject': 'Cross-Curricular',
            'level': 'All Levels',
            'description': description,
            'featured': cultural >= 5,
            'cultural_elements': {'integration_level': 'high' if cultural >= 5 else 'medium'}
        }
        
        supabase.table('resources').insert(resource).execute()
        return True
    except:
        return False

# Get current state
graphrag_paths = get_graphrag_paths()
all_files = [f for f in Path('public').rglob('*.html') 
             if not any(x in str(f) for x in ['backup', 'node_modules', '.git'])]

missing = [f for f in all_files if str(f.relative_to('public')) not in graphrag_paths]

print(f"📊 Starting: {len(graphrag_paths)} in GraphRAG")
print(f"🎯 Target: Add {min(200, len(missing))} files")
print()

# Add aggressively
added = 0
for i, file_path in enumerate(missing[:200], 1):
    if add_file(file_path):
        added += 1
        if added % 25 == 0:
            print(f"  Progress: {added}/200 added...")

print(f"\n✅ Added {added} files")

# Final stats
graphrag_paths = get_graphrag_paths()
coverage = len(graphrag_paths) / len(all_files) * 100

print(f"\n📈 Coverage: {len(graphrag_paths)}/{len(all_files)} ({coverage:.1f}%)")
print(f"🎯 Remaining: {len(all_files) - len(graphrag_paths)}")

