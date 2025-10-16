#!/usr/bin/env python3
"""
Index Generated-Resources-Alpha to GraphRAG
Systematically extract metadata and add to Supabase resources table
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).parent.parent
ALPHA_DIR = BASE_DIR / "public" / "generated-resources-alpha"

def extract_metadata(file_path):
    """Extract title, description, subject, level from HTML file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extract title
    title = soup.find('title')
    title = title.text.strip() if title else file_path.stem.replace('-', ' ').title()
    
    # Extract description from meta tag or first p
    desc_meta = soup.find('meta', attrs={'name': 'description'})
    description = desc_meta['content'] if desc_meta else ''
    
    if not description:
        first_p = soup.find('p')
        description = first_p.text.strip()[:200] if first_p else 'Educational resource'
    
    # Extract subject from meta or infer from title/content
    subject_meta = soup.find('meta', attrs={'name': 'subject'})
    subject = subject_meta['content'] if subject_meta else 'Cross-curricular'
    
    # Extract level from meta or infer
    level_meta = soup.find('meta', attrs={'name': 'year-level'})
    level = level_meta['content'] if level_meta else 'Y9-13'
    
    # Determine type from path
    if 'handouts' in str(file_path):
        resource_type = 'handout'
    elif 'lessons' in str(file_path):
        resource_type = 'lesson'
    else:
        resource_type = 'interactive'
    
    # Extract tags from content
    tags = []
    if 'māori' in title.lower() or 'maori' in title.lower():
        tags.append('cultural-integration')
    if 'traditional' in title.lower():
        tags.append('traditional-knowledge')
    if 'stem' in title.lower():
        tags.append('stem')
    if 'ncea' in title.lower():
        tags.append('ncea')
    
    # Get relative path
    rel_path = file_path.relative_to(BASE_DIR / "public")
    path = f"/public/{rel_path}"
    
    return {
        'title': title,
        'description': description[:500],  # Limit length
        'path': path,
        'type': resource_type,
        'subject': subject,
        'level': level,
        'tags': tags
    }

def generate_sql_insert(resources):
    """Generate SQL INSERT statements for Supabase"""
    
    sql = """
-- Generated Resources Alpha - Bulk Insert to GraphRAG
-- Date: October 16, 2025
-- Count: {} resources

INSERT INTO resources (title, description, path, type, subject, level, tags, author, featured) VALUES
""".format(len(resources))
    
    values = []
    for res in resources:
        tags_sql = "{" + ",".join(f'"{t}"' for t in res['tags']) + "}" if res['tags'] else '{}'
        
        value = f"""(
    '{res['title'].replace("'", "''")}',
    '{res['description'].replace("'", "''")}',
    '{res['path']}',
    '{res['type']}',
    '{res['subject']}',
    '{res['level']}',
    ARRAY{tags_sql},
    'Generated Resources Alpha Oct 2025',
    true
)"""
        values.append(value)
    
    sql += ",\n".join(values)
    sql += "\nON CONFLICT (path) DO UPDATE SET\n    title = EXCLUDED.title,\n    description = EXCLUDED.description,\n    updated_at = now();\n"
    
    return sql

def main():
    """Main execution"""
    print("📊 INDEXING GENERATED-RESOURCES-ALPHA TO GRAPHRAG")
    print("=" * 60)
    
    if not ALPHA_DIR.exists():
        print("❌ Generated-resources-alpha directory not found!")
        return
    
    # Find all HTML files
    html_files = []
    for subdir in ['handouts', 'lessons', '.']:
        search_dir = ALPHA_DIR if subdir == '.' else ALPHA_DIR / subdir
        if search_dir.exists():
            html_files.extend(search_dir.glob("*.html"))
    
    print(f"\nFound {len(html_files)} HTML files")
    print("\nExtracting metadata...")
    
    resources = []
    for html_file in html_files:
        if 'index.html' in html_file.name:
            continue  # Skip index files for now
        
        try:
            metadata = extract_metadata(html_file)
            resources.append(metadata)
            print(f"  ✅ {html_file.name}")
        except Exception as e:
            print(f"  ❌ {html_file.name}: {str(e)}")
    
    print(f"\n\n📝 Extracted metadata from {len(resources)} resources")
    
    # Generate SQL
    sql_output = generate_sql_insert(resources)
    
    # Save to file
    sql_file = BASE_DIR / "supabase" / "migrations" / "20251016_index_generated_resources.sql"
    sql_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(sql_file, 'w', encoding='utf-8') as f:
        f.write(sql_output)
    
    print(f"✅ SQL migration saved: {sql_file.name}")
    print(f"📊 Ready to insert {len(resources)} resources to GraphRAG")
    
    print("\n" + "=" * 60)
    print("NEXT STEP: Apply migration via MCP Supabase")
    print("=" * 60)

if __name__ == "__main__":
    main()

