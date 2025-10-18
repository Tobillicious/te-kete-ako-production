#!/usr/bin/env python3
"""
GRAPHRAG EXCAVATION - BATCH 2
Fix schema issues + add more categories
Goal: Get from 2% to 20%+ completion
"""

from supabase import create_client
from pathlib import Path
import json
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🚀 GRAPHRAG EXCAVATION - BATCH 2")
print("=" * 70)
print("Target: Add 50+ files, get to 20% completion")
print()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def normalize_path(path):
    """Normalize path for comparison"""
    return path.replace('/public/', '').replace('public/', '')

def get_graphrag_paths():
    """Get all paths currently in GraphRAG"""
    resources = supabase.table('resources').select('path').execute()
    return {normalize_path(r['path']) for r in resources.data}

def extract_metadata(file_path):
    """Extract metadata from HTML file"""
    full_path = Path('public') / file_path
    
    if not full_path.exists():
        return None
    
    try:
        content = full_path.read_text(encoding='utf-8', errors='ignore')
        
        # Title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1).replace(' | Te Kete Ako', '').strip() if title_match else full_path.stem
        
        # Description
        desc_match = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
        description = desc_match.group(1) if desc_match else ''
        
        return {
            'title': title[:200],
            'description': description[:500] if description else title,
            'content': content
        }
    except Exception as e:
        print(f"    Error reading {file_path}: {str(e)[:60]}")
        return None

def determine_safe_type(path, content):
    """Determine type using only allowed schema values"""
    # Allowed types based on schema: lesson, handout, interactive, game, activity, assessment, unit-plan
    
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
        # Default to interactive for experiences, tools, etc.
        return 'interactive'

def check_cultural_level(content):
    """Determine cultural integration level"""
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
    """Smart subject determination"""
    path_lower = path.lower()
    
    subjects = {
        'math': 'Mathematics',
        'science': 'Science',
        'english': 'English',
        'te reo': 'Te Reo Māori',
        'maori': 'Te Reo Māori',
        'social': 'Social Studies',
        'health': 'Health & PE',
        'technology': 'Technology',
        'tech': 'Technology',
        'arts': 'The Arts',
        'curriculum': 'Cross-Curricular'
    }
    
    for key, value in subjects.items():
        if key in path_lower:
            return value
    
    return 'Cross-Curricular'

def add_resource(file_path, metadata, priority='normal'):
    """Add a single resource to GraphRAG"""
    
    resource = {
        'title': metadata['title'],
        'path': file_path,
        'type': determine_safe_type(file_path, metadata['content']),
        'subject': determine_subject(file_path, metadata['content']),
        'level': 'All Levels',  # Can be refined later
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
        print(f"    ⚠️  {str(e)[:80]}")
        return False

def excavate_directory(directory, pattern='*.html', priority='normal'):
    """Excavate entire directory"""
    print(f"\n💎 EXCAVATING: {directory}")
    print("-" * 70)
    
    graphrag_paths = get_graphrag_paths()
    
    # Find all files
    files = list(Path('public').glob(f"{directory}/{pattern}"))
    
    # Filter to missing
    missing = []
    for f in files:
        rel_path = str(f.relative_to('public'))
        if normalize_path(rel_path) not in graphrag_paths:
            missing.append(rel_path)
    
    print(f"📂 Total files: {len(files)}")
    print(f"✅ In GraphRAG: {len(files) - len(missing)}")
    print(f"❌ Missing: {len(missing)}")
    
    if not missing:
        return 0
    
    print(f"\n📝 Adding {len(missing)} files...")
    
    added = 0
    for file_path in missing:
        metadata = extract_metadata(file_path)
        if metadata:
            if add_resource(file_path, metadata, priority):
                added += 1
                print(f"  ✅ {file_path}")
            else:
                print(f"  ⚠️  {file_path}")
    
    print(f"\n✨ Added {added}/{len(missing)} from {directory}")
    return added

# BATCH 2: Multiple directories
print("\n🎯 BATCH 2 TARGET DIRECTORIES:")
print("-" * 70)

total_added = 0

# High priority
total_added += excavate_directory('curriculum-documents', priority='high')
total_added += excavate_directory('tools', priority='medium')
total_added += excavate_directory('templates', priority='medium')

# Games directory
total_added += excavate_directory('games', priority='medium')

# Activities
total_added += excavate_directory('activities', priority='medium')

# Units (multiple subdirectories)
for unit_dir in ['y7-maths-algebra', 'y7-science-ecosystems', 'y8-critical-thinking', 
                  'y8-digital-kaitiakitanga', 'y9-science-ecology', 'walker-unit']:
    total_added += excavate_directory(f'units/{unit_dir}/lessons', priority='medium')
    total_added += excavate_directory(f'units/{unit_dir}/handouts', priority='medium')
    total_added += excavate_directory(f'units/{unit_dir}/resources', priority='low')

print("\n" + "=" * 70)
print("🎉 BATCH 2 COMPLETE!")
print("=" * 70)
print(f"📊 Total files added: {total_added}")

# Update progress
graphrag_paths = get_graphrag_paths()
total_files = len(list(Path('public').rglob('*.html')))
coverage = len(graphrag_paths) / total_files * 100

print(f"📈 GraphRAG Coverage: {len(graphrag_paths)}/{total_files} files ({coverage:.1f}%)")
print()
print("🚀 Progress toward 100% completion!")

# Save report
with open('graphrag-batch2-report.json', 'w') as f:
    json.dump({
        'batch': 2,
        'files_added': total_added,
        'total_in_graphrag': len(graphrag_paths),
        'coverage_percent': coverage
    }, f, indent=2)

