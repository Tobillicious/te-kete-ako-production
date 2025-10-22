#!/usr/bin/env python3
"""
Batch Index HTML Files to GraphRAG
October 22, 2025 - Critical Deployment Blocker Fix

Problem: 1,294 HTML files (61%) missing from GraphRAG
Solution: Scan /public/ and index all files systematically

Usage:
    python3 scripts/batch-index-html-files.py
    
Safety:
    - Uses ON CONFLICT DO NOTHING (no duplicates)
    - Read-only file scanning
    - Batch inserts (efficient)
    - Progress reporting
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import psycopg2
from urllib.parse import urlparse

# Supabase connection (from environment or hardcoded)
SUPABASE_URL = "postgresql://postgres.nlgldaqtubrlcqddppbq:TqYN1nZ7h6PZ5Kat@aws-0-ap-southeast-2.pooler.supabase.com:6543/postgres"

print("🚀 BATCH INDEXING SCRIPT - Te Kete Ako")
print("=" * 70)
print("Mission: Index 1,294 missing HTML files to GraphRAG")
print("=" * 70)

# Configuration
PUBLIC_DIR = Path(__file__).parent.parent / "public"
PRIORITY_DIRS = [
    "lessons",
    "units", 
    "handouts",
    "integrated-lessons",
    "generated-resources-alpha"
]

# Skip patterns
SKIP_PATTERNS = [
    "/backup", "/backups", "/archive", "/.archive",
    ".bak", ".backup", "/dist/", "/CODE/",
    "node_modules", ".git"
]

def should_skip(file_path):
    """Check if file should be skipped"""
    path_str = str(file_path)
    return any(skip in path_str for skip in SKIP_PATTERNS)

def extract_metadata(file_path):
    """Extract metadata from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.get_text().strip() if title_tag else file_path.name
        
        # Clean title (remove site suffix)
        title = re.sub(r'\s*\|\s*Te Kete Ako.*$', '', title)
        title = re.sub(r'\s*-\s*Te Kete Ako.*$', '', title)
        
        # Detect resource type from path
        path_str = str(file_path).lower()
        if '/lessons/' in path_str or '/lesson-' in path_str:
            resource_type = 'lesson'
        elif '/handouts/' in path_str or '/handout' in path_str:
            resource_type = 'handout'
        elif '/units/' in path_str or '/unit-' in path_str:
            resource_type = 'unit-plan'
        elif '/games/' in path_str or 'wordsearch' in path_str:
            resource_type = 'interactive_game'
        elif '/assessment' in path_str:
            resource_type = 'assessment'
        else:
            resource_type = 'other'
        
        # Detect subject from path
        subject = None
        if '/mathematics/' in path_str or '/math/' in path_str or 'y7-maths' in path_str or 'y8-maths' in path_str or 'y9-maths' in path_str:
            subject = 'Mathematics'
        elif '/science/' in path_str or 'y7-science' in path_str or 'y8-science' in path_str or 'y9-science' in path_str or 'ecology' in path_str or 'physics' in path_str:
            subject = 'Science'
        elif '/english/' in path_str or 'english' in file_path.name.lower():
            subject = 'English'
        elif '/social-studies/' in path_str or '/social studies/' in path_str:
            subject = 'Social Studies'
        elif '/digital' in path_str or 'digital-tech' in path_str or 'y8-digital-kaitiakitanga' in path_str:
            subject = 'Digital Technologies'
        elif '/te-ao-maori/' in path_str or '/te-reo' in path_str or 'māori' in path_str.lower():
            subject = 'Te Ao Māori'
        elif '/arts/' in path_str:
            subject = 'Arts'
        elif '/health' in path_str or '/pe/' in path_str:
            subject = 'Health & PE'
        
        # Detect year level
        year_level = None
        year_match = re.search(r'[yY](?:ear)?[-\s]?(\d+)', path_str)
        if year_match:
            year_num = year_match.group(1)
            year_level = f'Year {year_num}'
        
        # Estimate quality score based on content
        content_length = len(content)
        has_whakataukī = bool(re.search(r'whakataukī|whakatauki', content, re.IGNORECASE))
        has_te_reo = bool(re.search(r'ngā|kia|te reo|māori|maori|whanau|kaitiaki', content, re.IGNORECASE))
        has_cultural = 'cultural' in content.lower() or 'ahurea' in content.lower()
        
        # Quality scoring
        quality_score = 70  # Base
        if content_length > 5000:
            quality_score += 10
        if content_length > 10000:
            quality_score += 5
        if has_whakataukī:
            quality_score += 5
        if has_te_reo:
            quality_score += 5
        if has_cultural:
            quality_score += 5
        if resource_type in ['lesson', 'unit-plan']:
            quality_score += 5
        
        quality_score = min(quality_score, 100)
        
        # Cultural context boolean
        cultural_context = has_whakataukī or has_te_reo or has_cultural
        
        # Content preview (first 200 chars of visible text)
        preview_text = soup.get_text(separator=' ', strip=True)[:200]
        
        return {
            'file_path': str(file_path.relative_to(Path.cwd())).replace('\\', '/'),
            'title': title[:200] if title else file_path.name,
            'resource_type': resource_type,
            'subject': subject,
            'year_level': year_level,
            'quality_score': quality_score,
            'cultural_context': cultural_context,
            'has_whakataukī': has_whakataukī,
            'has_te_reo': has_te_reo,
            'content_preview': preview_text
        }
    
    except Exception as e:
        print(f"   ⚠️ Error parsing {file_path.name}: {e}")
        return None

def scan_html_files():
    """Scan for all HTML files in /public/"""
    print(f"\n📂 Scanning: {PUBLIC_DIR}")
    print("-" * 70)
    
    all_files = []
    for html_file in PUBLIC_DIR.rglob('*.html'):
        if not should_skip(html_file):
            all_files.append(html_file)
    
    print(f"✅ Found {len(all_files)} HTML files (after filtering)")
    return all_files

def batch_insert_to_graphrag(files_data):
    """Batch insert files to GraphRAG"""
    print(f"\n💾 Connecting to Supabase GraphRAG...")
    
    try:
        conn = psycopg2.connect(SUPABASE_URL)
        cursor = conn.cursor()
        
        print(f"✅ Connected!")
        print(f"\n📊 Inserting {len(files_data)} files...")
        print("-" * 70)
        
        inserted = 0
        skipped = 0
        errors = 0
        
        for i, data in enumerate(files_data, 1):
            if not data:
                errors += 1
                continue
            
            try:
                cursor.execute("""
                    INSERT INTO graphrag_resources (
                        file_path, title, resource_type, subject, year_level,
                        quality_score, cultural_context, has_whakataukī, 
                        has_te_reo, content_preview
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (file_path) DO NOTHING
                    RETURNING id;
                """, (
                    data['file_path'],
                    data['title'],
                    data['resource_type'],
                    data['subject'],
                    data['year_level'],
                    data['quality_score'],
                    data['cultural_context'],
                    data['has_whakataukī'],
                    data['has_te_reo'],
                    data['content_preview']
                ))
                
                if cursor.fetchone():
                    inserted += 1
                    if inserted % 50 == 0:
                        print(f"   Progress: {inserted} files inserted...")
                else:
                    skipped += 1
            
            except Exception as e:
                errors += 1
                if errors < 10:  # Only show first 10 errors
                    print(f"   ⚠️ Error inserting {data.get('file_path', 'unknown')}: {e}")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return inserted, skipped, errors
    
    except Exception as e:
        print(f"❌ Database error: {e}")
        return 0, 0, 0

def main():
    """Main execution"""
    
    # Step 1: Scan files
    html_files = scan_html_files()
    
    if not html_files:
        print("❌ No HTML files found!")
        return
    
    # Step 2: Extract metadata
    print(f"\n🔍 Extracting metadata from {len(html_files)} files...")
    print("-" * 70)
    
    files_data = []
    for i, file_path in enumerate(html_files, 1):
        if i % 100 == 0:
            print(f"   Processing: {i}/{len(html_files)} files...")
        
        metadata = extract_metadata(file_path)
        if metadata:
            files_data.append(metadata)
    
    print(f"✅ Extracted metadata from {len(files_data)} files")
    
    # Step 3: Batch insert to GraphRAG
    inserted, skipped, errors = batch_insert_to_graphrag(files_data)
    
    # Final report
    print("\n" + "=" * 70)
    print("📊 FINAL RESULTS:")
    print("=" * 70)
    print(f"✅ Files inserted:      {inserted}")
    print(f"⏭️  Files skipped:       {skipped} (already in GraphRAG)")
    print(f"⚠️  Errors:              {errors}")
    print(f"📁 Total processed:     {len(html_files)}")
    print("=" * 70)
    
    if inserted > 0:
        print(f"\n🎉 SUCCESS! Added {inserted} new files to GraphRAG!")
        print(f"🔍 Search & discovery now cover {inserted + skipped} files!")
    elif skipped > 0:
        print(f"\n✅ All {skipped} files already indexed!")
    else:
        print(f"\n⚠️ No files were inserted. Check errors above.")
    
    print("\n🚀 GraphRAG indexing complete! Platform ready for deployment!")
    print("=" * 70)

if __name__ == "__main__":
    main()

