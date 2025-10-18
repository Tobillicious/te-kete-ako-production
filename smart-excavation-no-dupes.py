#!/usr/bin/env python3
"""
SMART EXCAVATION - NO DUPLICATES
Check before adding to prevent duplicate entries
"""

from supabase import create_client
from pathlib import Path
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🎯 SMART EXCAVATION - DUPLICATE-AWARE")
print("=" * 70)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load ALL existing paths to check against
print("📥 Loading existing GraphRAG paths...")
resources = supabase.table('resources').select('path').execute()
existing_paths = set()

for r in resources.data:
    # Normalize path
    path = r['path'].replace('/public/', '').replace('public/', '')
    existing_paths.add(path)

print(f"✅ Loaded {len(existing_paths)} unique paths")
print()

# Get all public files
all_files = [f for f in Path('public').rglob('*.html') 
             if not any(x in str(f) for x in ['backup', 'node_modules', '.git'])]

# Find truly missing
missing = []
for f in all_files:
    rel_path = str(f.relative_to('public'))
    if rel_path not in existing_paths:
        missing.append(f)

print(f"📊 Status:")
print(f"   Total files: {len(all_files)}")
print(f"   Already in GraphRAG: {len(existing_paths)}")
print(f"   Missing: {len(missing)}")
print()

if len(missing) == 0:
    print("🎉 100% COVERAGE ACHIEVED!")
    exit(0)

print(f"🎯 Adding {min(100, len(missing))} files (no duplicates)...")
print()

added = 0
skipped = 0

for file_path in missing[:100]:
    rel_path = str(file_path.relative_to('public'))
    
    # Double-check not in existing
    if rel_path in existing_paths:
        skipped += 1
        continue
    
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
            'path': rel_path,
            'type': rtype,
            'subject': 'Cross-Curricular',
            'level': 'All Levels',
            'description': description,
            'featured': cultural >= 5,
            'cultural_elements': {'integration_level': 'high' if cultural >= 5 else 'medium'}
        }
        
        supabase.table('resources').insert(resource).execute()
        existing_paths.add(rel_path)  # Add to cache
        added += 1
        
        if added % 10 == 0:
            print(f"  ✅ {added} added...")
            
    except Exception as e:
        print(f"  ⚠️  {rel_path}: {str(e)[:60]}")

print(f"\n✅ Added: {added}")
print(f"⏭️  Skipped (duplicates): {skipped}")

# Final coverage
coverage = len(existing_paths) / len(all_files) * 100
print(f"\n📈 Coverage: {len(existing_paths)}/{len(all_files)} ({coverage:.1f}%)")
print(f"🎯 Remaining: {len(all_files) - len(existing_paths)}")

