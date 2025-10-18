#!/usr/bin/env python3
"""
INDEX EVERYTHING TO GRAPHRAG
Complete, comprehensive indexing of all 90K files
"""

import os
import json
import hashlib
import mimetypes
from pathlib import Path
from datetime import datetime
from supabase_graphrag_connector import SupabaseGraphRAGConnector
import time
from bs4 import BeautifulSoup
import re

print("🚀 INDEXING EVERYTHING TO GRAPHRAG")
print("=" * 70)

# Initialize
connector = SupabaseGraphRAGConnector()
supabase = connector.client

# Directories to skip
SKIP_DIRS = {'.git', 'node_modules', 'dist', '.vite', '__pycache__', '.pytest_cache', 
             '.next', 'venv', 'env', '.env'}

# Type mapping for Supabase
TYPE_MAPPING = {
    'html': 'page',
    'json': 'resource',
    'md': 'resource',
    'markdown': 'resource',
    'lesson': 'lesson',
    'handout': 'handout',
    'unit': 'unit-plan',
    'unit-plan': 'unit-plan',
    'game': 'game',
    'tool': 'tool',
    'assessment': 'assessment',
    'activity': 'activity',
    'interactive': 'interactive',
    'css': 'resource',
    'js': 'resource',
    'py': 'resource',
    'image': 'resource',
    'doc': 'resource'
}

def get_file_hash(filepath):
    """Get MD5 hash of file content"""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return None

def extract_html_metadata(filepath):
    """Extract metadata from HTML files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract title
            title_tag = soup.find('title')
            title = title_tag.text.strip() if title_tag else Path(filepath).stem
            
            # Extract description
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            description = desc_tag.get('content', '') if desc_tag else ''
            
            # Extract keywords
            keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
            keywords = keywords_tag.get('content', '').split(',') if keywords_tag else []
            
            # Look for cultural elements
            cultural_elements = []
            if 'māori' in content.lower() or 'maori' in content.lower():
                cultural_elements.append('māori_content')
            if 'te reo' in content.lower():
                cultural_elements.append('te_reo')
            if 'whakataukī' in content.lower() or 'whakatauki' in content.lower():
                cultural_elements.append('whakataukī')
            
            # Extract subject from path or content
            subject = None
            path_lower = str(filepath).lower()
            if 'math' in path_lower:
                subject = 'Mathematics'
            elif 'science' in path_lower:
                subject = 'Science'
            elif 'social' in path_lower:
                subject = 'Social Studies'
            elif 'english' in path_lower:
                subject = 'English'
            elif 'te reo' in path_lower or 'te-reo' in path_lower:
                subject = 'Te Reo Māori'
            
            return {
                'title': title[:500],
                'description': description[:1000] if description else content[:200],
                'tags': keywords[:10],
                'cultural_elements': cultural_elements,
                'subject': subject
            }
    except Exception as e:
        return None

def extract_json_metadata(filepath):
    """Extract metadata from JSON files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Try to find title/description in common fields
            title = data.get('title') or data.get('name') or Path(filepath).stem
            description = data.get('description') or str(data)[:200]
            
            return {
                'title': str(title)[:500],
                'description': str(description)[:1000],
                'tags': [],
                'cultural_elements': [],
                'subject': None
            }
    except:
        return None

def extract_md_metadata(filepath):
    """Extract metadata from Markdown files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract title from first # heading or filename
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else Path(filepath).stem
            
            return {
                'title': title[:500],
                'description': content[:1000],
                'tags': [],
                'cultural_elements': [],
                'subject': None
            }
    except:
        return None

def determine_resource_type(filepath, metadata):
    """Determine resource type from path and content"""
    path_lower = str(filepath).lower()
    
    # Check path for type indicators
    if 'lesson' in path_lower:
        return 'lesson'
    elif 'handout' in path_lower:
        return 'handout'
    elif 'unit' in path_lower:
        return 'unit-plan'
    elif 'game' in path_lower:
        return 'game'
    elif 'assessment' in path_lower or 'rubric' in path_lower:
        return 'assessment'
    elif 'activity' in path_lower:
        return 'activity'
    elif 'interactive' in path_lower or 'tool' in path_lower:
        return 'interactive'
    
    # Default by file extension
    ext = Path(filepath).suffix.lower().lstrip('.')
    return TYPE_MAPPING.get(ext, 'resource')

def index_file(filepath, base_dir):
    """Index a single file"""
    try:
        rel_path = str(Path(filepath).relative_to(base_dir))
        
        # Get file info
        file_stat = os.stat(filepath)
        ext = Path(filepath).suffix.lower().lstrip('.')
        
        # Extract metadata based on file type
        metadata = None
        if ext == 'html':
            metadata = extract_html_metadata(filepath)
        elif ext == 'json':
            metadata = extract_json_metadata(filepath)
        elif ext in ['md', 'markdown']:
            metadata = extract_md_metadata(filepath)
        
        # Fallback metadata
        if not metadata:
            metadata = {
                'title': Path(filepath).stem[:500],
                'description': f'{ext.upper()} file',
                'tags': [],
                'cultural_elements': [],
                'subject': None
            }
        
        # Determine type
        resource_type = determine_resource_type(filepath, metadata)
        
        # Create record
        record = {
            'title': metadata['title'],
            'description': metadata['description'],
            'path': rel_path,
            'type': resource_type,
            'subject': metadata.get('subject'),
            'tags': metadata.get('tags', []),
            'cultural_elements': metadata.get('cultural_elements'),
            'is_active': 'archive' not in rel_path.lower() and 'backup' not in rel_path.lower()
        }
        
        return record
        
    except Exception as e:
        print(f"  ⚠️  Error indexing {filepath}: {e}")
        return None

# Main indexing loop
print("\n📂 Scanning all files...")
base_dir = Path('.')
all_files = []

for root, dirs, files in os.walk(base_dir):
    # Skip certain directories
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    
    for file in files:
        filepath = Path(root) / file
        all_files.append(filepath)

total_files = len(all_files)
print(f"✅ Found {total_files:,} files to index\n")

# Get current GraphRAG count
current = supabase.table('resources').select('*', count='exact').limit(0).execute()
print(f"📊 Current GraphRAG: {current.count:,} resources")
print(f"🎯 Target: Index all {total_files:,} files\n")

# Index in batches
BATCH_SIZE = 50
indexed = 0
skipped = 0
errors = 0
batch = []

start_time = time.time()

for i, filepath in enumerate(all_files):
    try:
        # Index file
        record = index_file(filepath, base_dir)
        
        if record:
            batch.append(record)
        
        # Upload batch
        if len(batch) >= BATCH_SIZE:
            try:
                # Check for existing
                for rec in batch:
                    existing = supabase.table('resources')\
                        .select('id')\
                        .eq('path', rec['path'])\
                        .limit(1)\
                        .execute()
                    
                    if not existing.data:
                        supabase.table('resources').insert(rec).execute()
                        indexed += 1
                    else:
                        skipped += 1
                
                batch = []
                
            except Exception as e:
                errors += len(batch)
                batch = []
        
        # Progress update
        if (i + 1) % 100 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed
            remaining = (total_files - i - 1) / rate if rate > 0 else 0
            print(f"  📊 Progress: {i+1:,}/{total_files:,} | ✅ {indexed:,} | ⏭️  {skipped:,} | ❌ {errors} | ETA: {remaining/60:.1f}min")
    
    except Exception as e:
        errors += 1

# Upload remaining batch
if batch:
    try:
        for rec in batch:
            existing = supabase.table('resources').select('id').eq('path', rec['path']).limit(1).execute()
            if not existing.data:
                supabase.table('resources').insert(rec).execute()
                indexed += 1
            else:
                skipped += 1
    except:
        errors += len(batch)

# Final stats
elapsed = time.time() - start_time
final_count = supabase.table('resources').select('*', count='exact').limit(0).execute()

print("\n" + "=" * 70)
print("🎉 INDEXING COMPLETE!")
print("=" * 70)
print(f"Time: {elapsed/60:.1f} minutes")
print(f"Files processed: {total_files:,}")
print(f"✅ Indexed: {indexed:,}")
print(f"⏭️  Skipped: {skipped:,}")
print(f"❌ Errors: {errors}")
print(f"\n📊 GraphRAG now has: {final_count.count:,} total resources!")
print(f"📈 Growth: +{final_count.count - current.count:,}")
print("=" * 70)

