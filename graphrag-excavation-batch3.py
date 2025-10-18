#!/usr/bin/env python3
"""
GRAPHRAG EXCAVATION - BATCH 3
Continue systematic excavation - focus on handouts, lessons, components
Goal: Get from 46.7% to 70%+ completion
"""

from supabase import create_client
from pathlib import Path
import json
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🚀 GRAPHRAG EXCAVATION - BATCH 3")
print("=" * 70)
print("Target: Add 100+ files, get to 70% completion")
print()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def normalize_path(path):
    return path.replace('/public/', '').replace('public/', '')

def get_graphrag_paths():
    resources = supabase.table('resources').select('path').execute()
    return {normalize_path(r['path']) for r in resources.data}

def extract_metadata(file_path):
    full_path = Path('public') / file_path
    if not full_path.exists():
        return None
    
    try:
        content = full_path.read_text(encoding='utf-8', errors='ignore')
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1).replace(' | Te Kete Ako', '').strip() if title_match else full_path.stem
        desc_match = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
        description = desc_match.group(1) if desc_match else ''
        
        return {
            'title': title[:200],
            'description': description[:500] if description else title,
            'content': content
        }
    except Exception as e:
        return None

def determine_safe_type(path, content):
    if 'lesson' in path.lower():
        return 'lesson'
    elif 'handout' in path.lower():
        return 'handout'
    elif 'game' in path.lower():
        return 'game'
    elif 'assessment' in path.lower() or 'rubric' in path.lower():
        return 'assessment'
    elif 'unit' in path.lower():
        return 'unit-plan'
    elif 'activity' in path.lower():
        return 'activity'
    else:
        return 'interactive'

def check_cultural_level(content):
    content_lower = content.lower()
    count = 0
    if 'whakataukī' in content_lower or 'whakatauaki' in content_lower:
        count += 3
    if 'tikanga' in content_lower:
        count += 2
    if 'māori' in content_lower or 'maori' in content_lower:
        count += 1
    if 'cultural context' in content_lower:
        count += 1
    
    if count >= 5:
        return 'essential'
    elif count >= 3:
        return 'high'
    elif count >= 1:
        return 'medium'
    else:
        return 'low'

def determine_subject(path, content):
    path_lower = path.lower()
    subjects = {
        'math': 'Mathematics', 'science': 'Science', 'english': 'English',
        'te reo': 'Te Reo Māori', 'maori': 'Te Reo Māori', 'social': 'Social Studies',
        'health': 'Health & PE', 'technology': 'Technology', 'arts': 'The Arts',
        'curriculum': 'Cross-Curricular'
    }
    for key, value in subjects.items():
        if key in path_lower:
            return value
    return 'Cross-Curricular'

def add_resource(file_path, metadata, priority='normal'):
    resource = {
        'title': metadata['title'],
        'path': file_path,
        'type': determine_safe_type(file_path, metadata['content']),
        'subject': determine_subject(file_path, metadata['content']),
        'level': 'All Levels',
        'description': metadata['description'],
        'featured': priority == 'high',
        'cultural_elements': {
            'integration_level': check_cultural_level(metadata['content'])
        }
    }
    
    try:
        supabase.table('resources').insert(resource).execute()
        return True
    except Exception as e:
        return False

def excavate_directory(directory, pattern='*.html', priority='normal', max_files=None):
    print(f"\n💎 EXCAVATING: {directory}")
    print("-" * 70)
    
    graphrag_paths = get_graphrag_paths()
    
    # Find all files
    search_path = Path('public') / directory
    if not search_path.exists():
        print(f"⚠️  Directory not found: {directory}")
        return 0
    
    files = list(search_path.glob(pattern))
    
    # Filter to missing
    missing = []
    for f in files:
        rel_path = str(f.relative_to('public'))
        if normalize_path(rel_path) not in graphrag_paths:
            missing.append(rel_path)
    
    print(f"📂 Total: {len(files)} | In GraphRAG: {len(files) - len(missing)} | Missing: {len(missing)}")
    
    if not missing:
        return 0
    
    # Limit if specified
    to_add = missing if max_files is None else missing[:max_files]
    
    print(f"📝 Adding {len(to_add)} files...")
    
    added = 0
    for file_path in to_add:
        metadata = extract_metadata(file_path)
        if metadata and add_resource(file_path, metadata, priority):
            added += 1
            if added % 10 == 0:
                print(f"  ... {added} added so far")
    
    print(f"✨ Added {added}/{len(to_add)} from {directory}")
    return added

# BATCH 3: Major content directories
print("\n🎯 BATCH 3 TARGET DIRECTORIES:")
print("-" * 70)

total_added = 0

# Handouts - major category
print("\n📚 HANDOUTS DIRECTORIES:")
total_added += excavate_directory('handouts', priority='high')
total_added += excavate_directory('handouts/video-activities', priority='medium')
total_added += excavate_directory('handouts/do-now-activities', priority='medium')
total_added += excavate_directory('handouts/printable-worksheets', priority='medium')
total_added += excavate_directory('handouts/enhanced', priority='medium')

# Lessons directories
print("\n📖 LESSONS DIRECTORIES:")
total_added += excavate_directory('lessons', priority='high')
total_added += excavate_directory('lessons/writers-toolkit', priority='high')
total_added += excavate_directory('lessons/writers-toolkit/resources', priority='medium')

# More units
print("\n🎓 MORE UNIT DIRECTORIES:")
total_added += excavate_directory('units/unit-1-te-ao-maori/lessons', priority='high')
total_added += excavate_directory('units/unit-1-te-ao-maori/handouts', priority='high')
total_added += excavate_directory('y8-systems/lessons', priority='medium')
total_added += excavate_directory('y8-systems/resources', priority='medium')
total_added += excavate_directory('guided-inquiry-unit/lessons', priority='high')

# Components - rest of them
print("\n🧩 REMAINING COMPONENTS:")
total_added += excavate_directory('components', priority='medium')

# Professional development
print("\n👩‍🏫 PROFESSIONAL DEVELOPMENT:")
total_added += excavate_directory('professional-development', priority='high')

# Assessment frameworks
print("\n📊 ASSESSMENT FRAMEWORKS:")
total_added += excavate_directory('assessment-frameworks', priority='high')

print("\n" + "=" * 70)
print("🎉 BATCH 3 COMPLETE!")
print("=" * 70)
print(f"📊 Total files added this batch: {total_added}")

# Calculate progress
graphrag_paths = get_graphrag_paths()
public_files = list(Path('public').rglob('*.html'))
# Filter out backups, node_modules, etc
public_files = [f for f in public_files if not any(x in str(f) for x in ['backup', 'node_modules', '.git'])]
total_files = len(public_files)
coverage = len(graphrag_paths) / total_files * 100

print(f"📈 GraphRAG Coverage: {len(graphrag_paths)}/{total_files} files ({coverage:.1f}%)")
print()
print(f"🎯 Target: 100% | Current: {coverage:.1f}% | Gap: {100 - coverage:.1f}%")

# Save detailed report
report = {
    'batch': 3,
    'files_added': total_added,
    'total_in_graphrag': len(graphrag_paths),
    'total_public_files': total_files,
    'coverage_percent': coverage,
    'remaining': total_files - len(graphrag_paths)
}

with open('graphrag-batch3-report.json', 'w') as f:
    json.dump(report, f, indent=2)

print(f"💾 Report saved: graphrag-batch3-report.json")
print()
print("🚀 Continuing toward 100% completion!")

