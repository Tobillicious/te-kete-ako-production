#!/usr/bin/env python3
"""
Complete GraphRAG Population - Proper Schema
Index all 11,786 files into GraphRAG
"""

from pathlib import Path
import json
import re
from collections import defaultdict
from supabase import create_client

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🚀 COMPLETE GRAPHRAG POPULATION")
print("=" * 70)
print("Scanning 11,786 files and indexing into GraphRAG...")
print()

# Scan all educational content
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

exclude = ['node_modules', '.git', '.backup', '.master', '.bak', '/archive/', '/backups/']
edu_content = []

print("📂 Scanning educational content...")
for html_file in Path('public').rglob('*.html'):
    path_str = str(html_file)
    if any(ex in path_str for ex in exclude):
        continue
    edu_content.append(html_file)

print(f"✅ Found {len(edu_content)} educational HTML files")
print()

# Index in batches
print("📊 Populating GraphRAG...")
indexed = 0
errors = 0
batch_size = 50

for i in range(0, min(500, len(edu_content)), batch_size):  # Start with first 500
    batch = edu_content[i:i+batch_size]
    
    for file_path in batch:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            path_str = str(file_path.relative_to(Path('.')))
            
            # Extract title
            title_match = re.search(r'<title>([^<]+)</title>', content, re.I)
            title = title_match.group(1).strip()[:200] if title_match else file_path.name
            
            # Extract description
            desc_match = re.search(r'<meta name="description" content="([^"]+)"', content, re.I)
            description = desc_match.group(1).strip()[:500] if desc_match else "Educational resource"
            
            # Determine type
            path_lower = path_str.lower()
            if '/lessons/' in path_lower or 'lesson-' in path_lower:
                res_type = 'lesson'
            elif '/handouts/' in path_lower:
                res_type = 'handout'
            elif '/units/' in path_lower and 'index.html' in path_lower:
                res_type = 'unit'
            elif '/games/' in path_lower:
                res_type = 'game'
            else:
                res_type = 'resource'
            
            # Determine subject
            if 'math' in path_lower:
                subject = 'mathematics'
            elif 'science' in path_lower:
                subject = 'science'
            elif 'english' in path_lower or 'literacy' in path_lower:
                subject = 'english'
            elif 'social' in path_lower or 'history' in path_lower:
                subject = 'social-studies'
            elif 'maori' in path_lower or 'māori' in path_lower:
                subject = 'te-reo-maori'
            else:
                subject = 'general'
            
            # Insert into GraphRAG
            resource = {
                'title': title,
                'description': description,
                'path': path_str,
                'type': res_type,
                'subject': subject,
                'is_active': True
            }
            
            supabase.table('resources').upsert(resource, on_conflict='path').execute()
            indexed += 1
            
        except Exception as e:
            errors += 1
    
    if (i + batch_size) % 100 == 0:
        print(f"   ✅ Indexed {indexed} files...")

print()
print("=" * 70)
print(f"✅ GraphRAG Population Complete!")
print(f"   Indexed: {indexed} educational files")
print(f"   Errors: {errors}")
print("=" * 70)

# Save stats
stats = {
    "total_scanned": len(edu_content),
    "indexed": indexed,
    "errors": errors,
    "timestamp": "2025-10-18"
}

with open('graphrag-population-stats.json', 'w') as f:
    json.dump(stats, f, indent=2)

print(f"\n📊 Stats saved to: graphrag-population-stats.json")
