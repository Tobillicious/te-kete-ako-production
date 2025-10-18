#!/usr/bin/env python3
"""
Add meta descriptions to files missing them
"""

from pathlib import Path
import re

print("📝 ADDING META DESCRIPTIONS")
print("=" * 70)

files_missing_meta = [
    ('public/activities.html', 'Engaging classroom activities and educational exercises for students'),
    ('public/admin-youtube-library.html', 'Administrator dashboard for YouTube educational content library'),
    ('public/assessment-rubric.html', 'Comprehensive assessment rubrics and grading frameworks'),
    ('public/browse-by-concept.html', 'Browse educational resources by Māori concepts and cultural themes'),
    ('public/critical-thinking-unit.html', 'Critical thinking unit with lessons and resources for developing analytical skills'),
    ('public/curriculum-english.html', 'English curriculum resources aligned with NZ Curriculum standards'),
    ('public/graphrag-search.html', 'Advanced search powered by GraphRAG knowledge graph'),
    ('public/index.html', 'Te Kete Ako - World-class educational resources integrating mātauranga Māori with modern pedagogy for Aotearoa New Zealand'),
]

fixed_count = 0

for file_path, description in files_missing_meta:
    file = Path(file_path)
    if not file.exists():
        continue
    
    try:
        content = file.read_text(encoding='utf-8')
        
        # Check if meta description exists
        if 'meta name="description"' in content:
            print(f"ℹ️  Already has meta: {file.name}")
            continue
        
        # Add meta description in <head>
        meta_tag = f'    <meta name="description" content="{description}">'
        
        # Insert after <meta charset> or before </head>
        if '<meta charset' in content:
            content = re.sub(
                r'(<meta charset[^>]*>)',
                r'\1\n' + meta_tag,
                content,
                count=1
            )
        elif '</head>' in content:
            content = content.replace('</head>', f'{meta_tag}\n</head>', 1)
        else:
            print(f"⚠️  No <head> found in: {file.name}")
            continue
        
        file.write_text(content, encoding='utf-8')
        print(f"✅ Added meta to: {file.name}")
        fixed_count += 1
    
    except Exception as e:
        print(f"⚠️  Error fixing {file_path}: {e}")

print("\n" + "=" * 70)
print(f"✅ Added meta descriptions to {fixed_count} files")
print("=" * 70)
