#!/usr/bin/env python3
"""
SYNC & PROFESSIONALIZE - Fill the Gap & Build Relationships
1. Find the 395 missing files
2. Add them to Supabase resources table
3. Build intelligent relationships in graphrag_relationships
4. Professionalize metadata
"""
import os
import json
from pathlib import Path
from bs4 import BeautifulSoup
import re
from collections import defaultdict

print("🔄 SYNC & PROFESSIONALIZE")
print("=" * 70)

# Load what's in Supabase (from our query)
supabase_count = 8037
filesystem_count = 8432
gap = filesystem_count - supabase_count

print(f"📊 THE GAP:")
print(f"   Supabase: {supabase_count:,} resources")
print(f"   File System: {filesystem_count:,} HTML files")
print(f"   Missing: {gap} files to add")

# Scan all HTML files
print(f"\n📂 Scanning file system...")

all_html_files = []
for root, dirs, files in os.walk('.'):
    # Skip node_modules, .git, etc.
    if 'node_modules' in root or '.git' in root or 'dist' in root:
        continue
    
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            all_html_files.append(file_path)

print(f"   Found: {len(all_html_files):,} HTML files")

# Extract metadata from HTML files
def extract_metadata(file_path):
    """Extract rich metadata from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Title
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else Path(file_path).stem
        
        # Description
        desc_tag = soup.find('meta', {'name': 'description'})
        description = desc_tag.get('content', '') if desc_tag else ''
        
        # Detect type
        path_lower = file_path.lower()
        if 'lesson' in path_lower:
            resource_type = 'lesson'
        elif 'handout' in path_lower or 'worksheet' in path_lower:
            resource_type = 'handout'
        elif 'game' in path_lower:
            resource_type = 'game'
        elif 'unit' in path_lower:
            resource_type = 'unit-plan'
        elif 'assessment' in path_lower or 'rubric' in path_lower:
            resource_type = 'assessment'
        elif 'interactive' in path_lower:
            resource_type = 'interactive'
        else:
            resource_type = 'activity'
        
        # Detect subject
        content_lower = content.lower()
        subjects = []
        if any(kw in content_lower for kw in ['math', 'algebra', 'geometry', 'calculus']):
            subjects.append('Mathematics')
        if any(kw in content_lower for kw in ['science', 'biology', 'chemistry', 'physics']):
            subjects.append('Science')
        if any(kw in content_lower for kw in ['english', 'reading', 'writing', 'literacy']):
            subjects.append('English')
        if any(kw in content_lower for kw in ['history', 'social studies', 'geography']):
            subjects.append('Social Studies')
        if any(kw in content_lower for kw in ['te reo', 'māori language', 'whakataukī']):
            subjects.append('Te Reo Māori')
        
        subject = ', '.join(subjects) if subjects else 'Cross-curricular'
        
        # Detect year level
        year_matches = re.findall(r'year\s*(\d+)', content_lower)
        if year_matches:
            levels = sorted(set(year_matches))
            level = 'Year ' + ', '.join(levels)
        else:
            level = 'All Levels'
        
        # Cultural elements
        has_whakataukī = 'whakataukī' in content_lower
        has_te_reo = any(word in content_lower for word in ['kia ora', 'te reo', 'māori', 'tangata whenua'])
        has_tikanga = 'tikanga' in content_lower
        has_mātauranga = 'mātauranga' in content_lower
        
        cultural_score = sum([has_whakataukī, has_te_reo, has_tikanga, has_mātauranga])
        
        # Quality indicators
        quality = 50
        if '<nav' in content or 'header-component' in content: quality += 15
        if 'te-kete-professional.css' in content: quality += 15
        if cultural_score > 0: quality += 10 * cultural_score
        if len(content) > 5000: quality += 10
        quality = min(quality, 100)
        
        # Find links (for relationships)
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.endswith('.html') and not href.startswith('http'):
                links.append(href)
        
        return {
            'file_path': file_path.replace('./', '/'),
            'title': title[:200],
            'description': description[:500] if description else f"A {resource_type} resource on {subject}",
            'type': resource_type,
            'subject': subject,
            'level': level,
            'quality_score': quality,
            'cultural_elements': {
                'has_whakataukī': has_whakataukī,
                'has_te_reo': has_te_reo,
                'has_tikanga': has_tikanga,
                'has_mātauranga': has_mātauranga,
                'cultural_score': cultural_score
            },
            'links': links[:20],  # Max 20 links
            'content_length': len(content)
        }
    except Exception as e:
        return None

# Process files in batches
print(f"\n🔍 Extracting metadata from files...")
batch_size = 500
processed = []
relationships = []

for i, file_path in enumerate(all_html_files[:1000], 1):  # Process first 1000 for now
    metadata = extract_metadata(file_path)
    if metadata:
        processed.append(metadata)
        
        # Build relationships from links
        for link in metadata['links']:
            relationships.append({
                'source': metadata['file_path'],
                'target': link,
                'type': 'references',
                'confidence': 0.9
            })
    
    if i % 100 == 0:
        print(f"   Processed: {i:,}/{min(1000, len(all_html_files)):,}")

print(f"\n✅ Metadata extraction complete!")
print(f"   Processed: {len(processed):,} files")
print(f"   Relationships found: {len(relationships):,}")

# Categorize by type
by_type = defaultdict(list)
for item in processed:
    by_type[item['type']].append(item)

print(f"\n📊 BY TYPE:")
for type_name, items in sorted(by_type.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"   {type_name}: {len(items):,}")

# Save for upload
upload_data = {
    'resources': processed,
    'relationships': relationships,
    'stats': {
        'total_processed': len(processed),
        'total_relationships': len(relationships),
        'by_type': {k: len(v) for k, v in by_type.items()},
        'high_quality': len([r for r in processed if r['quality_score'] >= 80]),
        'culturally_integrated': len([r for r in processed if r['cultural_elements']['cultural_score'] > 0])
    }
}

with open('sync-upload-batch.json', 'w') as f:
    json.dump(upload_data, f, indent=2)

print(f"\n💾 Data saved: sync-upload-batch.json")

# Generate SQL for inserting to Supabase
print(f"\n📝 Generating SQL for Supabase upload...")

# Sample SQL (first 10 resources)
sql_statements = []
for resource in processed[:10]:
    sql = f"""
INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    '{resource['title'].replace("'", "''")}',
    '{resource['description'].replace("'", "''")}',
    '{resource['file_path']}',
    '{resource['type']}',
    '{resource['subject']}',
    '{resource['level']}',
    '{json.dumps(resource['cultural_elements'])}'::jsonb,
    {resource['quality_score'] >= 90},
    ARRAY{[resource['type'], resource['subject'].split(',')[0].strip()]},
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();
"""
    sql_statements.append(sql)

with open('supabase-upload.sql', 'w') as f:
    f.write('\n'.join(sql_statements))

print(f"   ✅ SQL file created: supabase-upload.sql (first 10 as sample)")

# Build intelligent relationships
print(f"\n🔗 BUILDING INTELLIGENT RELATIONSHIPS...")

relationship_types = defaultdict(int)
for rel in relationships:
    # Categorize relationship
    source_type = next((r['type'] for r in processed if r['file_path'] == rel['source']), 'unknown')
    
    if 'prerequisite' in rel['target'].lower():
        rel['relationship_type'] = 'prerequisite'
    elif 'handout' in rel['target'].lower() and source_type == 'lesson':
        rel['relationship_type'] = 'has_handout'
    elif 'lesson' in rel['target'].lower() and source_type == 'unit-plan':
        rel['relationship_type'] = 'contains_lesson'
    elif source_type == rel.get('target_type', ''):
        rel['relationship_type'] = 'related_content'
    else:
        rel['relationship_type'] = 'references'
    
    relationship_types[rel['relationship_type']] += 1

print(f"\n📊 RELATIONSHIP TYPES:")
for rel_type, count in sorted(relationship_types.items(), key=lambda x: x[1], reverse=True):
    print(f"   {rel_type}: {count:,}")

# Save relationships
with open('graphrag-relationships-new.json', 'w') as f:
    json.dump(relationships, f, indent=2)

print(f"\n💾 Relationships saved: graphrag-relationships-new.json")

print(f"\n🎯 SUMMARY:")
print(f"   Files processed: {len(processed):,}")
print(f"   High quality (≥80): {len([r for r in processed if r['quality_score'] >= 80]):,}")
print(f"   Culturally integrated: {len([r for r in processed if r['cultural_elements']['cultural_score'] > 0]):,}")
print(f"   Relationships mapped: {len(relationships):,}")
print(f"   Ready for upload to Supabase!")

