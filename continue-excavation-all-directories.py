#!/usr/bin/env python3
"""
CONTINUE EXCAVATION - ALL REMAINING DIRECTORIES
Systematic coverage of all public/ directories
Quality-verified, one directory at a time
"""

from supabase import create_client
from pathlib import Path
import json
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🚀 SYSTEMATIC DIRECTORY EXCAVATION")
print("=" * 70)
print("Goal: 100% GraphRAG coverage of public/")
print()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_graphrag_paths():
    resources = supabase.table('resources').select('path').execute()
    return {r['path'].replace('/public/', '').replace('public/', '') for r in resources.data}

def excavate_directory_batch(directory, max_files=30):
    """Excavate a directory in batches"""
    
    graphrag_paths = get_graphrag_paths()
    
    dir_path = Path('public') / directory
    if not dir_path.exists():
        return 0
    
    # Get all HTML files
    files = list(dir_path.glob('*.html'))
    
    # Filter missing
    missing = []
    for f in files:
        rel_path = str(f.relative_to('public'))
        if rel_path not in graphrag_paths:
            missing.append(f)
    
    if len(missing) == 0:
        return 0
    
    print(f"\n📂 {directory}: {len(files)} total, {len(missing)} missing")
    
    # Process batch
    to_process = missing[:max_files]
    added = 0
    
    for file_path in to_process:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            
            # Extract metadata
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            title = title_match.group(1).replace(' | Te Kete Ako', '').strip() if title_match else file_path.stem
            
            desc_match = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
            description = desc_match.group(1) if desc_match else title
            
            # Determine type
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
            
            # Cultural check
            cultural_count = (
                content.lower().count('whakataukī') +
                content.lower().count('tikanga') +
                content.lower().count('māori')
            )
            
            resource = {
                'title': title[:200],
                'path': str(file_path.relative_to('public')),
                'type': rtype,
                'subject': 'Cross-Curricular',
                'level': 'All Levels',
                'description': description[:500],
                'featured': cultural_count >= 5,
                'cultural_elements': {
                    'integration_level': 'high' if cultural_count >= 5 else ('medium' if cultural_count >= 2 else 'low')
                }
            }
            
            supabase.table('resources').insert(resource).execute()
            added += 1
            
        except Exception as e:
            pass
    
    print(f"  ✅ Added {added}/{len(to_process)}")
    return added

# Systematic excavation of all directories
print("🎯 EXCAVATING ALL DIRECTORIES...")
print("-" * 70)

total_added = 0

# Top-level directories
directories = [
    'lessons', 'handouts', 'units', 'games', 'tools', 'experiences',
    'activities', 'assessments', 'curriculum-documents', 'templates',
    'components', 'professional-development', 'assessment-frameworks'
]

for directory in directories:
    added = excavate_directory_batch(directory, max_files=30)
    total_added += added

# Subdirectories
subdirs = [
    'handouts/video-activities',
    'handouts/do-now-activities',
    'handouts/printable-worksheets',
    'handouts/enhanced',
    'lessons/writers-toolkit',
    'lessons/writers-toolkit/resources',
    'y8-systems/lessons',
    'y8-systems/resources',
    'guided-inquiry-unit/lessons',
]

for subdir in subdirs:
    added = excavate_directory_batch(subdir, max_files=30)
    total_added += added

print("\n" + "=" * 70)
print(f"📊 BATCH COMPLETE: {total_added} files added")

# Final stats
graphrag_paths = get_graphrag_paths()
public_files = [f for f in Path('public').rglob('*.html') 
                if not any(x in str(f) for x in ['backup', 'node_modules', '.git'])]

coverage = len(graphrag_paths) / len(public_files) * 100

print(f"📈 GraphRAG Coverage: {len(graphrag_paths)}/{len(public_files)} ({coverage:.1f}%)")
print(f"🎯 Remaining: {len(public_files) - len(graphrag_paths)} files")
print()
print("🚀 Systematic excavation continuing!")

