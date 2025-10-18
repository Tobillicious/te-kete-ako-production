#!/usr/bin/env python3
"""
CONTINUOUS EXCAVATION ENGINE
Systematically index remaining 70k documents in intelligent batches
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SERVICE_ROLE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

# Directories to excavate (prioritized)
PRIORITY_DIRS = [
    'public/integrated-lessons',  # 377 lessons
    'public/units',                # Complete units
    'public/handouts',             # 109 handouts
    'public/assessments',          # 23 assessments
    'public/games',                # 17+ games
    'public/writers-toolkit',      # Writing resources
    'backups',                     # Historical variants
    'archived-bloat',              # Legacy content
    'development',                 # Development resources
]

def extract_metadata(filepath):
    """Extract metadata from file path and content"""
    
    path = Path(filepath)
    metadata = {
        'path': str(filepath),
        'filename': path.name,
        'directory': str(path.parent),
        'size_bytes': path.stat().st_size if path.exists() else 0,
        'last_modified': datetime.fromtimestamp(path.stat().st_mtime).isoformat() if path.exists() else None,
    }
    
    # Detect type from path
    if '/lessons/' in str(filepath) or '/integrated-lessons/' in str(filepath):
        metadata['type'] = 'lesson'
    elif '/handouts/' in str(filepath):
        metadata['type'] = 'handout'
    elif '/units/' in str(filepath):
        metadata['type'] = 'unit'
    elif '/assessments/' in str(filepath):
        metadata['type'] = 'assessment'
    elif '/games/' in str(filepath):
        metadata['type'] = 'game'
    elif '/tools/' in str(filepath):
        metadata['type'] = 'tool'
    else:
        metadata['type'] = 'other'
    
    # Detect subjects from path
    subjects = []
    path_lower = str(filepath).lower()
    if 'math' in path_lower:
        subjects.append('mathematics')
    if 'science' in path_lower:
        subjects.append('science')
    if 'english' in path_lower or 'writing' in path_lower:
        subjects.append('english')
    if 'te-reo' in path_lower or 'maori' in path_lower:
        subjects.append('te-reo-maori')
    if 'social' in path_lower:
        subjects.append('social-studies')
    
    metadata['subjects'] = subjects
    
    # Detect year level
    year_match = re.search(r'y(?:ear)?[-_]?(\d+)', path_lower)
    if year_match:
        metadata['level'] = f'year-{year_match.group(1)}'
    
    # Detect cultural integration (heuristic)
    if 'maori' in path_lower or 'te-reo' in path_lower or 'tikanga' in path_lower:
        metadata['cultural_integration'] = 'high'
    elif 'integrated' in path_lower:
        metadata['cultural_integration'] = 'medium'
    else:
        metadata['cultural_integration'] = 'low'
    
    # Extract title from filename
    title = path.stem
    title = re.sub(r'[-_]', ' ', title)
    title = re.sub(r'\d{4}-\d{2}-\d{2}', '', title)  # Remove dates
    title = re.sub(r'\s+', ' ', title).strip().title()
    metadata['title'] = title
    
    return metadata

def scan_directory_batch(directory, batch_size=1000):
    """Scan directory and yield batches of files"""
    
    files = []
    for root, dirs, filenames in os.walk(directory):
        # Skip node_modules, .git, etc.
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.vscode', '__pycache__']]
        
        for filename in filenames:
            # Only process HTML files for now
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                files.append(filepath)
                
                if len(files) >= batch_size:
                    yield files
                    files = []
    
    if files:
        yield files

def main():
    print('🏗️  CONTINUOUS EXCAVATION ENGINE')
    print('=' * 80)
    print()
    print('Target: 70k unindexed documents')
    print('Strategy: Intelligent batching + auto-relationship building')
    print()
    
    try:
        from supabase import create_client
        supabase = create_client(SUPABASE_URL, SERVICE_ROLE_KEY)
        
        # Get already indexed paths
        print('📥 Checking already indexed resources...')
        response = supabase.table('resources').select('path').execute()
        indexed_paths = set(r['path'] for r in response.data)
        print(f'✅ {len(indexed_paths)} resources already indexed')
        print()
        
        total_new = 0
        
        for priority_dir in PRIORITY_DIRS:
            if not os.path.exists(priority_dir):
                print(f'⏭️  Skipping {priority_dir} (not found)')
                continue
            
            print(f'\n📂 Excavating: {priority_dir}')
            print('─' * 80)
            
            batch_num = 0
            for file_batch in scan_directory_batch(priority_dir, batch_size=500):
                batch_num += 1
                
                # Filter out already indexed
                new_files = [f for f in file_batch if f not in indexed_paths]
                
                if not new_files:
                    continue
                
                print(f'\n   Batch {batch_num}: {len(new_files)} new files')
                
                # Extract metadata
                resources = []
                for filepath in new_files:
                    try:
                        metadata = extract_metadata(filepath)
                        
                        # Format for Supabase
                        resource = {
                            'path': metadata['path'],
                            'title': metadata['title'],
                            'type': metadata['type'],
                            'subjects': metadata.get('subjects', []),
                            'level': metadata.get('level'),
                            'description': f"Excavated from {priority_dir}",
                            'cultural_elements': {
                                'cultural_integration': metadata.get('cultural_integration', 'unknown'),
                                'te_reo_usage': 'unknown',
                                'maori_concepts': []
                            },
                            'estimated_duration_minutes': 60,
                            'difficulty_level': 'intermediate',
                            'tags': [priority_dir.split('/')[-1]]
                        }
                        
                        resources.append(resource)
                        
                    except Exception as e:
                        print(f'      ⚠️  Error processing {filepath}: {e}')
                
                # Upload batch
                if resources:
                    try:
                        result = supabase.table('resources').insert(resources).execute()
                        print(f'      ✅ Uploaded {len(resources)} resources')
                        total_new += len(resources)
                        indexed_paths.update(r['path'] for r in resources)
                    except Exception as e:
                        print(f'      ❌ Upload error: {e}')
        
        print()
        print('=' * 80)
        print(f'✅ EXCAVATION BATCH COMPLETE!')
        print(f'   New resources indexed: {total_new}')
        print(f'   Total in GraphRAG: {len(indexed_paths)}')
        print(f'   Coverage: {len(indexed_paths) / 90000 * 100:.1f}%')
        print()
        print('💡 Next steps:')
        print('   • Run build-relationships-intelligent.py')
        print('   • Continue with next batch')
        
    except ImportError:
        print('⚠️  Supabase library not installed')
        print('   Run: pip install supabase')
    except Exception as e:
        print(f'❌ Error: {e}')
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

