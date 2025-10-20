#!/usr/bin/env python3
"""
🧠 GRAPHRAG UPDATER HOOK
Pipeline hook for auto-indexing changed files to GraphRAG

Purpose: Every deployment automatically updates GraphRAG knowledge graph
Usage: Called by unified-pipeline-orchestrator.py
"""

from pathlib import Path
from bs4 import BeautifulSoup
from supabase import create_client
import re

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def extract_metadata(file_path):
    """Extract GraphRAG metadata from file"""
    
    path = Path(file_path)
    if not path.exists():
        return None
    
    try:
        content = path.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.text.replace(' | Te Kete Ako', '').strip() if title_tag else path.stem
        
        # Determine subject
        path_str = str(path).lower()
        subject = 'Cross-Curricular'
        if 'math' in path_str: subject = 'Mathematics'
        elif 'science' in path_str: subject = 'Science'
        elif 'english' in path_str: subject = 'English'
        elif 'social' in path_str: subject = 'Social Studies'
        elif 'digital' in path_str: subject = 'Digital Technologies'
        elif 'te-ao-maori' in path_str: subject = 'Te Ao Māori'
        
        # Check cultural integration
        has_cultural = bool(
            soup.find(class_=re.compile(r'cultural|whakatau', re.I)) or
            'whakataukī' in content or
            'mātauranga' in content
        )
        
        return {
            'file_path': '/' + str(path.relative_to('.')).replace('\\', '/'),
            'title': title,
            'resource_type': detect_resource_type(path_str),
            'subject': subject,
            'year_level': detect_year_level(path_str),
            'quality_score': estimate_quality(content, has_cultural),
            'cultural_context': has_cultural,
            'content_preview': title[:200]
        }
        
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
        return None

def detect_resource_type(path_str):
    """Detect resource type from path"""
    if '/lessons/' in path_str: return 'Lesson'
    if '/handouts/' in path_str: return 'Handout'
    if '/units/' in path_str: return 'Unit'
    if '/games/' in path_str: return 'Game'
    if 'hub' in path_str: return 'Hub'
    return 'Page'

def detect_year_level(path_str):
    """Detect year level from path"""
    if 'y7' in path_str: return 'Year 7'
    if 'y8' in path_str: return 'Year 8'
    if 'y9' in path_str: return 'Year 9'
    if 'y10' in path_str: return 'Year 10'
    return None

def estimate_quality(content, has_cultural):
    """Estimate quality score"""
    base = 85
    if len(content) > 20000: base = 90
    if has_cultural: base += 5
    return min(base, 100)

def index_to_graphrag(files):
    """Index files to GraphRAG"""
    
    print("🧠 GRAPHRAG UPDATER: Indexing files...")
    
    indexed = 0
    updated = 0
    errors = 0
    
    for file_path in files:
        metadata = extract_metadata(file_path)
        
        if not metadata:
            errors += 1
            continue
        
        try:
            # Check if already exists
            existing = supabase.table('graphrag_resources')\
                .select('file_path')\
                .eq('file_path', metadata['file_path'])\
                .execute()
            
            if existing.data:
                # Update existing
                supabase.table('graphrag_resources')\
                    .update(metadata)\
                    .eq('file_path', metadata['file_path'])\
                    .execute()
                updated += 1
                print(f"   🔄 Updated: {metadata['title'][:50]}")
            else:
                # Insert new
                supabase.table('graphrag_resources').insert(metadata).execute()
                indexed += 1
                print(f"   ✨ Indexed: {metadata['title'][:50]}")
            
        except Exception as e:
            errors += 1
            print(f"   ⚠️  Error: {file_path} - {e}")
    
    print()
    return {
        'indexed': indexed,
        'updated': updated,
        'errors': errors,
        'total_processed': len(files)
    }

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        result = index_to_graphrag(sys.argv[1:])
        print(f"\n✅ Indexed: {result['indexed']}, Updated: {result['updated']}, Errors: {result['errors']}")

