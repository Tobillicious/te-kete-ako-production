#!/usr/bin/env python3
"""
METADATA EXTRACTION SCRIPT - Unlock 9,461 Resources
Extract subject, level, type from file paths and HTML content
Time: 30 min to write ✅, 10 min to execute

IMPACT: Makes 90% of resources discoverable to users!
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict

# Pattern definitions
YEAR_PATTERNS = [
    r'y(\d+)',  # y7, y8, y9
    r'year[-_\s]*(\d+)',  # year-7, year_8, year 9
    r'level[-_\s]*(\d+)',  # level-4
]

SUBJECT_KEYWORDS = {
    'mathematics': ['math', 'algebra', 'geometry', 'statistics', 'calculus', 'trigonometry', 'measurement'],
    'science': ['science', 'physics', 'chemistry', 'biology', 'ecology', 'cells', 'climate', 'plants'],
    'english': ['english', 'writing', 'reading', 'literacy', 'literature', 'poetry', 'narrative'],
    'social studies': ['social', 'history', 'geography', 'civics', 'society', 'treaty', 'waitangi', 'government'],
    'digital technologies': ['digital', 'coding', 'tech', 'computing', 'programming', 'ai', 'ethics'],
    'te reo māori': ['te-reo', 'māori', 'maori', 'reo', 'whakataukī'],
    'health & pe': ['health', 'pe', 'physical', 'wellbeing', 'fitness'],
    'arts': ['art', 'music', 'drama', 'dance', 'visual', 'creative'],
}

TYPE_KEYWORDS = {
    'lesson': ['lesson', 'akoranga'],
    'handout': ['handout', 'worksheet', 'activity', 'template'],
    'unit-plan': ['unit', 'waehere'],
    'game': ['game', 'wordle', 'quiz', 'interactive'],
    'assessment': ['assessment', 'rubric', 'test', 'evaluation'],
}

def extract_year_level(path, content=None):
    """Extract year level from path or content"""
    path_lower = path.lower()
    
    # Try path patterns
    for pattern in YEAR_PATTERNS:
        match = re.search(pattern, path_lower)
        if match:
            year = int(match.group(1))
            if 1 <= year <= 13:
                return f'Year {year}'
    
    # Try content if available
    if content:
        # Look for "Year X" in title or headers
        year_match = re.search(r'year\s+(\d+)', content.lower())
        if year_match:
            year = int(year_match.group(1))
            if 1 <= year <= 13:
                return f'Year {year}'
    
    return 'All Levels'

def extract_subject(path, content=None):
    """Extract subject from path or content"""
    path_lower = path.lower()
    
    # Score each subject based on keyword matches
    scores = defaultdict(int)
    
    for subject, keywords in SUBJECT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in path_lower:
                scores[subject] += 2  # Path matches weighted higher
            if content and keyword in content.lower():
                scores[subject] += 1
    
    # Return highest scoring subject
    if scores:
        return max(scores.items(), key=lambda x: x[1])[0].title()
    
    # Check if in cross-curricular directories
    if any(x in path_lower for x in ['cross-curricular', 'integrated', 'inquiry']):
        return 'Cross-Curricular'
    
    return 'Cross-Curricular'  # Default

def extract_type(path, content=None):
    """Extract resource type from path"""
    path_lower = path.lower()
    
    # Check directory structure first
    if '/lessons/' in path_lower:
        return 'lesson'
    if '/handouts/' in path_lower or '/worksheets/' in path_lower:
        return 'handout'
    if '/unit-plans/' in path_lower or '/units/' in path_lower:
        return 'unit-plan'
    if '/games/' in path_lower:
        return 'game'
    if '/assessments/' in path_lower:
        return 'assessment'
    
    # Check filename
    for type_name, keywords in TYPE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in path_lower:
                return type_name
    
    return 'lesson'  # Default assumption

def extract_title_from_html(filepath):
    """Extract title from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Try <title> tag
            if soup.title and soup.title.string:
                return soup.title.string.strip()
            
            # Try <h1>
            h1 = soup.find('h1')
            if h1:
                return h1.get_text().strip()
            
            # Fallback to filename
            return Path(filepath).stem.replace('-', ' ').replace('_', ' ').title()
    except:
        return Path(filepath).stem.replace('-', ' ').replace('_', ' ').title()

def extract_content_preview(filepath, max_length=500):
    """Extract content preview from HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Remove script and style tags
            for tag in soup(['script', 'style', 'nav', 'footer']):
                tag.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text[:max_length]
    except:
        return ""

def scan_public_directory():
    """Scan public directory for all HTML files"""
    print("🔍 Scanning public directory for HTML files...")
    
    html_files = []
    for root, dirs, files in os.walk('public'):
        # Skip certain directories
        if any(skip in root for skip in ['node_modules', '.git', 'dist']):
            continue
            
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                filepath = os.path.join(root, file)
                html_files.append(filepath)
    
    print(f"✅ Found {len(html_files)} HTML files")
    return html_files

def extract_metadata_from_file(filepath):
    """Extract all metadata from a single file"""
    try:
        # Get content for analysis
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        metadata = {
            'file_path': filepath,
            'title': extract_title_from_html(filepath),
            'subject': extract_subject(filepath, content),
            'level': extract_year_level(filepath, content),
            'type': extract_type(filepath, content),
            'content_preview': extract_content_preview(filepath),
        }
        
        return metadata
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return None

def generate_sql_updates(metadata_list):
    """Generate SQL UPDATE statements for batch execution"""
    sql_statements = []
    
    for metadata in metadata_list:
        if not metadata:
            continue
        
        # Escape single quotes for SQL
        file_path = metadata['file_path'].replace("'", "''")
        title = metadata['title'].replace("'", "''")
        subject = metadata['subject'].replace("'", "''")
        level = metadata['level'].replace("'", "''")
        type_val = metadata['type'].replace("'", "''")
        
        sql = f"""
-- Update metadata for: {metadata['title'][:50]}
UPDATE resources 
SET 
    subject = '{subject}',
    level = '{level}',
    type = '{type_val}',
    title = COALESCE(NULLIF(title, ''), '{title}')
WHERE path = '{file_path}' OR path LIKE '%{os.path.basename(file_path)}';
"""
        sql_statements.append(sql)
    
    return sql_statements

def main():
    print("=" * 80)
    print("🚀 METADATA EXTRACTION - Unlock 9,461 Resources")
    print("=" * 80)
    print()
    
    # Scan for files
    html_files = scan_public_directory()
    
    # Extract metadata
    print(f"\n📊 Extracting metadata from {len(html_files)} files...")
    metadata_list = []
    
    for i, filepath in enumerate(html_files, 1):
        if i % 100 == 0:
            print(f"   Processed {i}/{len(html_files)}...")
        
        metadata = extract_metadata_from_file(filepath)
        if metadata:
            metadata_list.append(metadata)
    
    print(f"✅ Extracted metadata from {len(metadata_list)} files")
    
    # Generate statistics
    print("\n📈 METADATA STATISTICS:")
    
    subjects = defaultdict(int)
    levels = defaultdict(int)
    types = defaultdict(int)
    
    for m in metadata_list:
        subjects[m['subject']] += 1
        levels[m['level']] += 1
        types[m['type']] += 1
    
    print("\nSubjects:")
    for subject, count in sorted(subjects.items(), key=lambda x: x[1], reverse=True):
        print(f"  {subject:30} {count:5}")
    
    print("\nLevels:")
    for level, count in sorted(levels.items()):
        print(f"  {level:30} {count:5}")
    
    print("\nTypes:")
    for type_name, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
        print(f"  {type_name:30} {count:5}")
    
    # Save results
    print("\n💾 Saving results...")
    
    # Save as JSON
    with open('metadata-extraction-results.json', 'w', encoding='utf-8') as f:
        json.dump(metadata_list, f, indent=2, ensure_ascii=False)
    print("✅ Saved: metadata-extraction-results.json")
    
    # Generate SQL
    sql_statements = generate_sql_updates(metadata_list)
    with open('metadata-extraction-updates.sql', 'w', encoding='utf-8') as f:
        f.write("-- METADATA EXTRACTION BATCH UPDATE\n")
        f.write(f"-- Generated: {len(sql_statements)} UPDATE statements\n")
        f.write("-- Impact: Makes resources discoverable via search/filter\n\n")
        f.write("BEGIN;\n\n")
        f.write('\n'.join(sql_statements))
        f.write("\n\nCOMMIT;\n")
    print("✅ Saved: metadata-extraction-updates.sql")
    
    # Save CSV for manual review
    import csv
    with open('metadata-extraction-results.csv', 'w', newline='', encoding='utf-8') as f:
        if metadata_list:
            writer = csv.DictWriter(f, fieldnames=metadata_list[0].keys())
            writer.writeheader()
            writer.writerows(metadata_list)
    print("✅ Saved: metadata-extraction-results.csv")
    
    print("\n" + "=" * 80)
    print("✅ METADATA EXTRACTION COMPLETE!")
    print("=" * 80)
    print(f"\n📊 RESULTS:")
    print(f"  Files processed: {len(html_files)}")
    print(f"  Metadata extracted: {len(metadata_list)}")
    print(f"  SQL statements generated: {len(sql_statements)}")
    print(f"\n📁 OUTPUT FILES:")
    print(f"  1. metadata-extraction-results.json (full data)")
    print(f"  2. metadata-extraction-updates.sql (for Supabase)")
    print(f"  3. metadata-extraction-results.csv (for review)")
    print(f"\n🚀 NEXT STEPS:")
    print(f"  1. Review CSV file for accuracy")
    print(f"  2. Execute SQL file in Supabase")
    print(f"  3. Verify resources now discoverable")
    print()
    
if __name__ == '__main__':
    main()

