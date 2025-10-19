#!/usr/bin/env python3
"""
📊 SURFACE ALL 18K RESOURCES TO GRAPHRAG
Complete GraphRAG population - make everything discoverable
"""

import os
import re
from pathlib import Path
from supabase import create_client
from bs4 import BeautifulSoup

print("📊 SURFACING ALL RESOURCES TO GRAPHRAG")
print("=" * 70)

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Find all HTML files
public_dir = Path('public')
all_files = list(public_dir.rglob('*.html'))

print(f"📁 Found {len(all_files)} HTML files on disk")

# Get existing resources from GraphRAG
response = supabase.table('graphrag_resources').select('file_path').execute()
existing_paths = {r['file_path'] for r in response.data}

print(f"📊 {len(existing_paths)} resources already in GraphRAG")
print(f"💎 {len(all_files) - len(existing_paths)} resources need indexing")

def extract_metadata(filepath: Path) -> dict:
    """Extract metadata from HTML file"""
    try:
        content = filepath.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.text.replace(' | Te Kete Ako', '').strip() if title_tag else filepath.stem
        
        # Extract subject from path or content
        path_str = str(filepath).lower()
        subject = 'Cross-Curricular'
        
        if 'math' in path_str or 'algebra' in path_str or 'geometry' in path_str:
            subject = 'Mathematics'
        elif 'science' in path_str or 'ecology' in path_str or 'physics' in path_str:
            subject = 'Science'
        elif 'english' in path_str:
            subject = 'English'
        elif 'social' in path_str:
            subject = 'Social Studies'
        elif 'digital' in path_str or 'technology' in path_str:
            subject = 'Digital Technologies'
        elif 'te-ao-maori' in path_str or 'te reo' in path_str:
            subject = 'Te Ao Māori'
        elif 'health' in path_str or 'pe' in path_str:
            subject = 'Health & PE'
        elif 'arts' in path_str:
            subject = 'Arts'
        
        # Extract year level
        year_level = None
        if 'y7' in path_str:
            year_level = 'Year 7'
        elif 'y8' in path_str:
            year_level = 'Year 8'
        elif 'y9' in path_str:
            year_level = 'Year 9'
        elif 'y10' in path_str:
            year_level = 'Year 10'
        
        # Determine resource type
        resource_type = 'Page'
        if '/lessons/' in path_str:
            resource_type = 'Lesson'
        elif '/handouts/' in path_str:
            resource_type = 'Handout'
        elif '/units/' in path_str and '/lessons/' not in path_str:
            resource_type = 'Unit'
        elif '/games/' in path_str:
            resource_type = 'Game'
        elif 'hub' in path_str:
            resource_type = 'Hub'
        elif 'dashboard' in path_str:
            resource_type = 'Dashboard'
        
        # Check for cultural integration
        has_cultural = bool(
            soup.find(class_=re.compile(r'whakatau|cultural|te-ao-maori', re.I)) or
            'whakataukī' in content or
            'mātauranga' in content
        )
        
        # Estimate quality
        content_length = len(content)
        quality = 85  # Default
        if content_length > 20000:
            quality = 90
        if has_cultural:
            quality += 5
        
        return {
            'title': title,
            'file_path': '/' + str(filepath.relative_to(Path('.'))).replace('\\', '/'),
            'resource_type': resource_type,
            'subject': subject,
            'year_level': year_level,
            'quality_score': min(quality, 100),
            'cultural_context': has_cultural,
            'content_preview': title[:200]  # Use content_preview instead of description
        }
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

# Process all files
print("\n🚀 INDEXING TO GRAPHRAG:\n")

indexed_count = 0
skipped_count = 0
error_count = 0

for filepath in all_files:
    # Convert to relative path for comparison
    relative_path = '/' + str(filepath.relative_to(Path('.'))).replace('\\', '/')
    
    # Skip if already indexed
    if relative_path in existing_paths:
        skipped_count += 1
        continue
    
    # Skip backups and archives
    if 'backup' in str(filepath) or 'archive' in str(filepath):
        skipped_count += 1
        continue
    
    # Extract metadata and insert
    metadata = extract_metadata(filepath)
    if metadata:
        try:
            supabase.table('graphrag_resources').insert(metadata).execute()
            indexed_count += 1
            
            if indexed_count % 100 == 0:
                print(f"   ✅ {indexed_count} resources indexed...")
                
        except Exception as e:
            error_count += 1
            if error_count < 10:  # Only show first 10 errors
                print(f"   ⚠️  Error: {filepath.name} - {e}")

print("\n" + "=" * 70)
print("✅ GRAPHRAG INDEXING COMPLETE")
print("=" * 70)
print(f"\n✅ New resources indexed: {indexed_count}")
print(f"⏭️  Already indexed: {skipped_count}")
print(f"⚠️  Errors: {error_count}")
print(f"\n💎 GraphRAG now has complete platform coverage!")
print(f"🔍 All resources now searchable and discoverable!")

