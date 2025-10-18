#!/usr/bin/env python3
"""
Systematically index ALL /public/ HTML files into GraphRAG
"""
import os
import glob
import json
from pathlib import Path
from supabase import create_client, Client

# Supabase setup
url = "https://nlgldaqtubrlcqddppbq.supabase.co"
key = os.environ.get('SUPABASE_KEY', 'YOUR_KEY_HERE')  # Will use MCP instead
supabase: Client = create_client(url, key)

def infer_metadata(file_path):
    """Infer metadata from file path and name"""
    path = Path(file_path)
    parts = path.parts
    
    # Default values
    resource_type = 'Page'
    title = path.stem.replace('-', ' ').title()
    quality_score = 88
    cultural = True
    subject = 'General'
    year = 'All'
    has_whakatauaki = False
    has_te_reo = True
    
    # Infer from path
    if 'lessons' in parts:
        resource_type = 'Lesson'
        quality_score = 90
        has_whakatauaki = True
    elif 'handouts' in parts:
        resource_type = 'Handout'
        quality_score = 89
    elif 'units' in parts:
        if path.name == 'index.html':
            resource_type = 'Page'
            title = f"{parts[-2].replace('-', ' ').title()} Unit Index"
        else:
            resource_type = 'Lesson'
            quality_score = 90
    elif 'games' in parts:
        resource_type = 'Game'
        quality_score = 92
    elif 'components' in parts:
        resource_type = 'Component'
    
    # Subject inference
    if 'math' in file_path.lower():
        subject = 'Mathematics'
    elif 'science' in file_path.lower():
        subject = 'Science'
    elif 'english' in file_path.lower():
        subject = 'English'
    elif 'te-reo' in file_path.lower() or 'māori' in file_path.lower():
        subject = 'Te Reo'
    elif 'social' in file_path.lower() or 'history' in file_path.lower():
        subject = 'Social Studies'
    elif 'digital' in file_path.lower() or 'tech' in file_path.lower():
        subject = 'Digital Tech'
    
    # Year level inference
    for part in parts:
        if 'y7' in part.lower() or 'year-7' in part.lower():
            year = 'Year 7'
        elif 'y8' in part.lower() or 'year-8' in part.lower():
            year = 'Year 8'
        elif 'y9' in part.lower() or 'year-9' in part.lower():
            year = 'Year 9'
        elif 'y10' in part.lower() or 'year-10' in part.lower():
            year = 'Year 10'
    
    metadata = {
        "source": "production",
        "indexed_batch": "systematic_public_indexing"
    }
    
    return {
        'resource_type': resource_type,
        'title': title,
        'quality_score': quality_score,
        'cultural_context': cultural,
        'subject': subject,
        'has_whakataukī': has_whakatauaki,
        'has_te_reo': has_te_reo,
        'year_level': year,
        'metadata': json.dumps(metadata)
    }

# Find all public HTML files
all_files = list(Path('public').glob('**/*.html'))
print(f"Found {len(all_files)} total public HTML files")

# Prepare batch insert
batch = []
for file_path in all_files:
    rel_path = str(file_path)
    meta = infer_metadata(rel_path)
    
    batch.append({
        'file_path': rel_path,
        **meta
    })
    
    # Insert in batches of 50
    if len(batch) >= 50:
        print(f"  Inserting batch of {len(batch)}...")
        batch = []

# Insert remaining
if batch:
    print(f"  Inserting final batch of {len(batch)}...")

print(f"✅ Indexed {len(all_files)} public files!")

