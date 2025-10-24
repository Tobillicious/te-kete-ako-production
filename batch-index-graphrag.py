#!/usr/bin/env python3
"""
🧠 GraphRAG Batch Indexing Script
Indexes missing HTML files from /public/ into graphrag_resources table

CRITICAL: Solves the "1,294 missing files" deployment blocker
Currently only 39% of files indexed - this fixes the gap!
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
from supabase import create_client, Client

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Base directory
PUBLIC_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public")

# Subject detection patterns
SUBJECT_PATTERNS = {
    'Mathematics': ['math', 'algebra', 'geometry', 'calculus', 'statistics', 'numeracy'],
    'Science': ['science', 'biology', 'chemistry', 'physics', 'ecology', 'ecosystems'],
    'English': ['english', 'writing', 'literacy', 'poetry', 'narrative', 'essay'],
    'Social Studies': ['social-studies', 'history', 'geography', 'civics'],
    'Digital Technologies': ['digital', 'technology', 'coding', 'programming', 'ai', 'cyber'],
    'Te Ao Māori': ['te-ao', 'maori', 'māori', 'tikanga', 'whakapapa'],
    'Arts': ['arts', 'drama', 'music', 'visual-arts', 'dance'],
    'Health & PE': ['health', 'pe', 'physical', 'wellbeing', 'hauora'],
    'Te Reo Māori': ['te-reo', 'reo-maori', 'language'],
}

# Year level detection
YEAR_PATTERNS = {
    'Year 7': ['y7', 'year-7', 'year7'],
    'Year 8': ['y8', 'year-8', 'year8'],
    'Year 9': ['y9', 'year-9', 'year9'],
    'Year 10': ['y10', 'year-10', 'year10'],
    'Year 11': ['y11', 'year-11', 'year11'],
    'Year 12': ['y12', 'year-12', 'year12'],
    'Year 13': ['y13', 'year-13', 'year13'],
}

# Resource type detection
RESOURCE_TYPE_PATTERNS = {
    'Lesson': ['/lessons/', '/lesson-', '-lesson-'],
    'Handout': ['/handouts/', '/handout-', '-handout-'],
    'Unit': ['/units/', '/unit-'],
    'Assessment': ['/assessments/', '/assessment-', '/quiz-', '/test-'],
    'Game': ['/games/', '/game-', '-game'],
    'Hub': ['-hub.html', '/hubs/'],
    'Index': ['index.html'],
    'Component': ['/components/'],
}


def get_existing_file_paths():
    """Get all file paths already indexed in GraphRAG"""
    print("📊 Fetching existing indexed files from GraphRAG...")
    
    # Fetch ALL records (paginate if needed)
    all_paths = set()
    page_size = 1000
    offset = 0
    
    while True:
        response = supabase.table('graphrag_resources')\
            .select('file_path')\
            .range(offset, offset + page_size - 1)\
            .execute()
        
        if not response.data:
            break
        
        for row in response.data:
            all_paths.add(row['file_path'])
        
        if len(response.data) < page_size:
            break
        
        offset += page_size
        print(f"  Fetched {offset} paths...")
    
    print(f"✅ Found {len(all_paths)} files already indexed")
    return all_paths


def detect_subject(file_path, content):
    """Detect subject from path and content"""
    path_lower = file_path.lower()
    content_lower = content.lower() if content else ""
    
    for subject, patterns in SUBJECT_PATTERNS.items():
        for pattern in patterns:
            if pattern in path_lower or pattern in content_lower:
                return subject
    
    return "Cross-Curricular"


def detect_year_level(file_path, content):
    """Detect year level from path and content"""
    path_lower = file_path.lower()
    
    for year, patterns in YEAR_PATTERNS.items():
        for pattern in patterns:
            if pattern in path_lower:
                return year
    
    # Check content for year mentions
    if content:
        for year, patterns in YEAR_PATTERNS.items():
            if any(pattern in content.lower() for pattern in patterns):
                return year
    
    return "All Years"


def detect_resource_type(file_path):
    """Detect resource type from path"""
    path_lower = file_path.lower()
    
    for rtype, patterns in RESOURCE_TYPE_PATTERNS.items():
        for pattern in patterns:
            if pattern in path_lower:
                return rtype
    
    return "Page"


def parse_html_file(file_path):
    """Parse HTML file and extract metadata"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else file_path.name
        
        # Extract h1 if title is generic
        if not title or title == "Te Kete Ako":
            h1 = soup.find('h1')
            if h1:
                title = h1.text.strip()
        
        # Get full text content for analysis
        text_content = soup.get_text(separator=' ', strip=True)[:500]  # First 500 chars
        
        # Cultural markers
        has_whakataukī = bool(re.search(r'whakataukī|whakatauk', content, re.IGNORECASE))
        has_te_reo = bool(re.search(r'kia ora|tēnā koe|whānau|kaitiaki|mātauranga', content, re.IGNORECASE))
        cultural_context = has_whakataukī or has_te_reo or 'māori' in content.lower() or 'maori' in content.lower()
        
        # Quality estimation (heuristic based on content length and markers)
        quality_score = 70  # Base score
        
        if len(content) > 5000:
            quality_score += 10  # Substantial content
        if has_whakataukī:
            quality_score += 5
        if has_te_reo:
            quality_score += 5
        if cultural_context:
            quality_score += 5
        if soup.find_all(['section', 'article']):
            quality_score += 5  # Structured content
        
        quality_score = min(quality_score, 95)  # Cap at 95 (reserve 96+ for verified excellence)
        
        return {
            'title': title,
            'content_preview': text_content[:200],  # First 200 chars
            'has_whakataukī': has_whakataukī,
            'has_te_reo': has_te_reo,
            'cultural_context': cultural_context,
            'quality_score': quality_score,
            'full_content': text_content,
        }
    
    except Exception as e:
        print(f"  ⚠️  Error parsing {file_path.name}: {e}")
        return None


def index_file(file_path, existing_paths):
    """Index a single HTML file to GraphRAG"""
    # Convert to database path format
    db_path = str(file_path).replace(str(PUBLIC_DIR.parent), "")
    
    # Skip if already indexed
    if db_path in existing_paths:
        return None
    
    # Skip backup files
    if '.bak' in str(file_path) or '/archive/' in str(file_path):
        return None
    
    # Skip component files (they're included dynamically)
    if '/components/' in str(file_path) and file_path.name != 'index.html':
        return None
    
    # Parse the file
    parsed = parse_html_file(file_path)
    if not parsed:
        return None
    
    # Detect attributes
    subject = detect_subject(db_path, parsed['full_content'])
    year_level = detect_year_level(db_path, parsed['full_content'])
    resource_type = detect_resource_type(db_path)
    
    # Build record
    record = {
        'file_path': db_path,
        'resource_type': resource_type,
        'title': parsed['title'],
        'quality_score': parsed['quality_score'],
        'cultural_context': parsed['cultural_context'],
        'year_level': year_level,
        'subject': subject,
        'has_whakataukī': parsed['has_whakataukī'],
        'has_te_reo': parsed['has_te_reo'],
        'content_preview': parsed['content_preview'],
        'is_backup': False,
        'archive_status': 'active',
    }
    
    return record


def batch_index_files():
    """Main indexing function"""
    print("🚀 Starting GraphRAG Batch Indexing Script")
    print("=" * 70)
    
    # Get existing files
    existing_paths = get_existing_file_paths()
    
    # Find all HTML files
    print(f"\n📂 Scanning {PUBLIC_DIR} for HTML files...")
    html_files = list(PUBLIC_DIR.rglob('*.html'))
    print(f"✅ Found {len(html_files)} HTML files total")
    
    # Filter to new files
    new_files = []
    for file_path in html_files:
        db_path = str(file_path).replace(str(PUBLIC_DIR.parent), "")
        if db_path not in existing_paths:
            if '.bak' not in str(file_path) and '/archive/' not in str(file_path):
                new_files.append(file_path)
    
    print(f"🆕 Found {len(new_files)} new files to index")
    
    if len(new_files) == 0:
        print("✅ All files already indexed! Nothing to do.")
        return
    
    # Process files
    records = []
    errors = 0
    
    print(f"\n⚙️  Processing {len(new_files)} files...")
    for i, file_path in enumerate(new_files, 1):
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(new_files)} ({i*100//len(new_files)}%)")
        
        record = index_file(file_path, existing_paths)
        if record:
            records.append(record)
        else:
            errors += 1
    
    print(f"✅ Successfully parsed {len(records)} files")
    print(f"⚠️  {errors} files skipped or had errors")
    
    # Batch insert to Supabase
    if records:
        print(f"\n💾 Inserting {len(records)} records to GraphRAG...")
        
        # Insert in batches of 100
        batch_size = 100
        for i in range(0, len(records), batch_size):
            batch = records[i:i + batch_size]
            try:
                supabase.table('graphrag_resources').insert(batch).execute()
                print(f"  ✅ Batch {i//batch_size + 1}: Inserted {len(batch)} records")
            except Exception as e:
                print(f"  ❌ Batch {i//batch_size + 1} failed: {e}")
    
    print("\n" + "=" * 70)
    print("🎉 BATCH INDEXING COMPLETE!")
    print(f"📊 Total New Files Indexed: {len(records)}")
    print(f"📈 GraphRAG Coverage: {len(existing_paths)} → {len(existing_paths) + len(records)}")
    print(f"🎯 New Coverage: {100 * (len(existing_paths) + len(records)) / len(html_files):.1f}%")


if __name__ == "__main__":
    try:
        batch_index_files()
    except KeyboardInterrupt:
        print("\n⚠️  Indexing interrupted by user")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        raise

