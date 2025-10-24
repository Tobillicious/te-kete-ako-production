#!/usr/bin/env python3
"""
Batch Index Markdown Files to GraphRAG
Index all the missing planning and documentation markdown files
"""

import os
import sys
import hashlib
from pathlib import Path
from supabase import create_client

def get_file_hash(content):
    """Generate consistent hash for content"""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def extract_title_from_md(content, filename):
    """Extract title from markdown content"""
    lines = content.split('\n')
    
    # Look for # Title
    for line in lines[:10]:
        if line.strip().startswith('# '):
            return line.strip()[2:].strip()
    
    # Fallback to filename
    return filename.replace('.md', '').replace('-', ' ').title()

def categorize_md_file(content, path):
    """Categorize markdown file type"""
    content_lower = content.lower()
    
    if any(x in content_lower for x in ['roadmap', 'plan', 'strategy']):
        return 'planning'
    elif any(x in content_lower for x in ['session', 'summary', 'complete']):
        return 'session_knowledge' 
    elif any(x in content_lower for x in ['status', 'report', 'audit']):
        return 'status_report'
    elif any(x in content_lower for x in ['deploy', 'instructions', 'guide']):
        return 'deployment_guide'
    else:
        return 'documentation'

def assess_cultural_level(content):
    """Assess cultural integration level"""
    content_lower = content.lower()
    maori_terms = ['māori', 'maori', 'whakataukī', 'kaitiaki', 'wānanga', 'mana', 'tikanga', 'whenua']
    
    maori_count = sum(1 for term in maori_terms if term in content_lower)
    
    if maori_count >= 5:
        return 'high'
    elif maori_count >= 2:
        return 'medium'
    else:
        return 'low'

def main():
    print("🚀 BATCH MARKDOWN INDEXING - GraphRAG Recovery")
    print("=" * 70)
    
    # Initialize Supabase
    supabase_url = os.environ.get('SUPABASE_URL')
    supabase_key = os.environ.get('SUPABASE_ANON_KEY')
    
    if not supabase_url or not supabase_key:
        print("❌ Error: SUPABASE_URL and SUPABASE_ANON_KEY must be set")
        sys.exit(1)
    
    supabase = create_client(supabase_url, supabase_key)
    
    # Find all markdown files
    root_path = Path('.')
    md_files = list(root_path.glob('*.md'))
    
    print(f"📂 Found {len(md_files)} markdown files in root directory")
    print("-" * 70)
    
    inserted_count = 0
    skipped_count = 0
    error_count = 0
    
    for md_file in md_files:
        try:
            # Read file content
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if len(content.strip()) < 50:  # Skip very short files
                continue
                
            # Extract metadata
            title = extract_title_from_md(content, md_file.name)
            file_type = categorize_md_file(content, str(md_file))
            cultural_level = assess_cultural_level(content)
            content_hash = get_file_hash(content)
            
            # Check if already exists
            existing = supabase.table('resources').select('id').eq('path', str(md_file)).execute()
            
            if existing.data:
                print(f"⏭️  Skipping {md_file.name} (already indexed)")
                skipped_count += 1
                continue
            
            # Prepare resource data
            resource_data = {
                'id': content_hash,
                'title': title,
                'type': file_type,
                'path': str(md_file),
                'content': content,
                'cultural_level': cultural_level,
                'subject_areas': [],  # Planning docs don't have specific subjects
                'metadata': {
                    'file_type': 'markdown',
                    'source': 'planning_docs',
                    'indexed_date': '2025-10-24'
                }
            }
            
            # Insert to GraphRAG
            result = supabase.table('resources').insert(resource_data).execute()
            
            if result.data:
                print(f"✅ Indexed: {title}")
                inserted_count += 1
            else:
                print(f"❌ Failed to index: {md_file.name}")
                error_count += 1
                
        except Exception as e:
            print(f"❌ Error processing {md_file.name}: {str(e)}")
            error_count += 1
    
    print("\n" + "=" * 70)
    print("📊 MARKDOWN INDEXING RESULTS:")
    print("=" * 70)
    print(f"✅ Files inserted:      {inserted_count}")
    print(f"⏭️  Files skipped:       {skipped_count}")
    print(f"⚠️  Errors:              {error_count}")
    print(f"📁 Total processed:     {len(md_files)}")
    print("=" * 70)
    
    if inserted_count > 0:
        print(f"🚀 Successfully indexed {inserted_count} planning documents to GraphRAG!")
    else:
        print("⚠️ No new files were indexed. Check existing content or errors.")
    
    print("=" * 70)

if __name__ == "__main__":
    main()