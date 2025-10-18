#!/usr/bin/env python3
"""
COMPLETE CONTENT MAPPER - Map ALL teaching content to GraphRAG
Scan filesystem systematically and create complete catalog
"""

import os
import json
from pathlib import Path
from collections import defaultdict
import re

print("🗺️  COMPLETE CONTENT MAPPING - SYSTEMATIC SCAN")
print("=" * 80)

BASE_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

# Content categories
content_map = {
    'lessons': [],
    'handouts': [],
    'units': [],
    'assessments': [],
    'games': [],
    'tools': [],
    'other': []
}

# Subject detection patterns
SUBJECTS = {
    'English': ['writing', 'literacy', 'english', 'writers', 'narrative', 'poetry', 'argumentative'],
    'Mathematics': ['math', 'algebra', 'geometry', 'statistics', 'calculus', 'numeracy'],
    'Science': ['science', 'biology', 'chemistry', 'physics', 'ecology', 'climate'],
    'Social Sciences': ['history', 'geography', 'economics', 'social', 'walker', 'decoloniz'],
    'Te Ao Māori': ['māori', 'maori', 'te reo', 'whakapapa', 'tikanga', 'cultural'],
    'Arts': ['art', 'music', 'drama', 'visual'],
    'Technology': ['digital', 'coding', 'technology', 'computer'],
    'Health & PE': ['health', 'wellbeing', 'physical', 'pe']
}

def detect_subject(path, title):
    """Detect subject from path and title"""
    text = f"{path} {title}".lower()
    subjects = []
    for subject, keywords in SUBJECTS.items():
        if any(kw in text for kw in keywords):
            subjects.append(subject)
    return subjects if subjects else ['General']

def detect_type(path):
    """Detect resource type from path"""
    path_lower = path.lower()
    if '/lessons/' in path_lower or 'lesson-plan' in path_lower or 'lesson-' in path_lower:
        return 'lessons'  # Changed to plural to match dict key
    elif '/handouts/' in path_lower or 'handout' in path_lower:
        return 'handouts'  # Changed to plural
    elif '/units/' in path_lower or '/unit-' in path_lower or 'unit-plan' in path_lower:
        return 'units'  # Changed to plural
    elif '/assessments/' in path_lower or 'assessment' in path_lower or 'rubric' in path_lower:
        return 'assessments'  # Changed to plural
    elif '/games/' in path_lower or 'game' in path_lower or 'wordle' in path_lower:
        return 'games'  # Changed to plural
    elif '/tools/' in path_lower or 'generator' in path_lower:
        return 'tools'  # Changed to plural
    else:
        return 'other'

def extract_title(filepath):
    """Extract title from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(1000)  # First 1000 chars
            # Look for <title> tag
            match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
    except:
        pass
    # Fallback to filename
    return filepath.stem.replace('-', ' ').replace('_', ' ').title()

print("\n📁 Scanning directories...")

# Scan key directories
scan_dirs = [
    'lessons',
    'handouts', 
    'units',
    'games',
    'tools',
    'assessments',
    'writers-toolkit',
    'interactive-literacy',
    'critical-thinking',
    'y7-introduction',
    'y8-systems',
    'guided-inquiry-unit',
    'dist-lessons',
    'dist-handouts',
    'dist-units',
    'generated-resources-alpha'
]

total_scanned = 0
for dir_name in scan_dirs:
    dir_path = BASE_DIR / dir_name
    if not dir_path.exists():
        continue
    
    print(f"\n📂 Scanning: {dir_name}/")
    
    for html_file in dir_path.rglob('*.html'):
        # Skip backups and duplicates
        if any(skip in str(html_file) for skip in ['.backup', '.old', 'master-backup', 'node_modules']):
            continue
        
        relative_path = str(html_file.relative_to(BASE_DIR))
        title = extract_title(html_file)
        resource_type = detect_type(relative_path)
        subjects = detect_subject(relative_path, title)
        
        resource = {
            'path': relative_path,
            'title': title,
            'type': resource_type,
            'subjects': subjects,
            'directory': dir_name,
            'size': html_file.stat().st_size
        }
        
        content_map[resource_type].append(resource)
        total_scanned += 1
        
        if total_scanned % 100 == 0:
            print(f"   Scanned {total_scanned} files...")

print("\n" + "=" * 80)
print("📊 SCANNING COMPLETE")
print("=" * 80)

# Summary by type
print("\n📋 CONTENT BY TYPE:")
for res_type, resources in content_map.items():
    print(f"   {res_type.upper()}: {len(resources)}")

# Summary by subject
print("\n📚 CONTENT BY SUBJECT:")
subject_counts = defaultdict(int)
for res_list in content_map.values():
    for res in res_list:
        for subject in res['subjects']:
            subject_counts[subject] += 1

for subject, count in sorted(subject_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"   {subject}: {count}")

# English content specifically
print("\n✍️  ENGLISH/LITERACY CONTENT:")
english_content = []
for res_type, resources in content_map.items():
    for res in resources:
        if 'English' in res['subjects']:
            english_content.append(res)

print(f"   Total English resources: {len(english_content)}")
print(f"\n   By type:")
english_by_type = defaultdict(int)
for res in english_content:
    english_by_type[res['type']] += 1
for res_type, count in sorted(english_by_type.items(), key=lambda x: x[1], reverse=True):
    print(f"      {res_type}: {count}")

# Sample English lessons
print(f"\n   Sample English lessons:")
english_lessons = [r for r in english_content if r['type'] == 'lesson']
for i, lesson in enumerate(english_lessons[:15], 1):
    print(f"      {i:2}. {lesson['title'][:60]}")

# Save complete map
output_file = 'complete-content-map.json'
with open(output_file, 'w') as f:
    json.dump({
        'total_scanned': total_scanned,
        'scan_date': '2025-10-18',
        'content_by_type': {k: len(v) for k, v in content_map.items()},
        'content_by_subject': dict(subject_counts),
        'all_resources': content_map
    }, f, indent=2)

print(f"\n💾 Complete map saved to: {output_file}")
print(f"📊 Total files scanned: {total_scanned}")
print("\n✅ Use this data to organize systematically!")

