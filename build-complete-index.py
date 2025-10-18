#!/usr/bin/env python3
"""
BUILD COMPLETE CODEBASE INDEX
Create comprehensive local index of all 11,786 files
Then enable full searchability
"""

from pathlib import Path
import json
import re
from collections import defaultdict

print("🔍 BUILDING COMPLETE CODEBASE INDEX")
print("=" * 70)

exclude = ['node_modules', '.git', '__pycache__']

# Comprehensive file categorization
index = {
    "metadata": {
        "total_files": 0,
        "timestamp": "2025-10-18",
        "version": "complete-index-v1"
    },
    "educational_content": {
        "units": [],
        "lessons": [],
        "handouts": [],
        "games": [],
        "tools": []
    },
    "by_subject": defaultdict(list),
    "by_year_level": defaultdict(list),
    "file_types": defaultdict(int),
    "directory_map": {},
    "relationships": {
        "unit_to_lessons": defaultdict(list),
        "lesson_to_handouts": defaultdict(list)
    }
}

print("\n📂 Scanning all files...")
for file_path in Path('.').rglob('*'):
    if not file_path.is_file():
        continue
    if any(ex in str(file_path) for ex in exclude):
        continue
        
    index["metadata"]["total_files"] += 1
    suffix = file_path.suffix or 'no_ext'
    index["file_types"][suffix] += 1
    
    # Categorize educational HTML
    if file_path.suffix == '.html' and 'public/' in str(file_path):
        path_str = str(file_path)
        rel_path = str(file_path.relative_to(Path('.')))
        
        # Skip backups
        if any(x in path_str for x in ['.backup', '.master', '.bak']):
            continue
        
        # Read and extract metadata
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            
            # Extract title
            title_match = re.search(r'<title>([^<]+)</title>', content, re.I)
            title = title_match.group(1).strip() if title_match else file_path.name
            
            # Categorize
            item = {"path": rel_path, "title": title}
            
            if '/units/' in path_str and 'index.html' in path_str:
                index["educational_content"]["units"].append(item)
            elif '/lessons/' in path_str or 'lesson-' in file_path.name.lower():
                index["educational_content"]["lessons"].append(item)
            elif '/handouts/' in path_str or 'handout' in path_str.lower():
                index["educational_content"]["handouts"].append(item)
            elif '/games/' in path_str:
                index["educational_content"]["games"].append(item)
            elif '/tools/' in path_str:
                index["educational_content"]["tools"].append(item)
            
            # Subject categorization
            if any(x in path_str.lower() for x in ['math', 'algebra', 'geometry']):
                index["by_subject"]["mathematics"].append(item)
            if any(x in path_str.lower() for x in ['science', 'physics', 'chemistry', 'ecology']):
                index["by_subject"]["science"].append(item)
            if any(x in path_str.lower() for x in ['english', 'literacy', 'writing']):
                index["by_subject"]["english"].append(item)
            if any(x in path_str.lower() for x in ['social', 'walker', 'herangi', 'history']):
                index["by_subject"]["social-studies"].append(item)
            if any(x in path_str.lower() for x in ['māori', 'maori', 'te-reo']):
                index["by_subject"]["te-reo-maori"].append(item)
                
        except:
            pass

# Convert defaultdicts to regular dicts for JSON
index["by_subject"] = dict(index["by_subject"])
index["by_year_level"] = dict(index["by_year_level"])
index["file_types"] = dict(index["file_types"])
index["relationships"] = {
    "unit_to_lessons": dict(index["relationships"]["unit_to_lessons"]),
    "lesson_to_handouts": dict(index["relationships"]["lesson_to_handouts"])
}

# Save comprehensive index
with open('COMPLETE-CODEBASE-INDEX.json', 'w') as f:
    json.dump(index, f, indent=2)

# Print summary
print(f"\n✅ Indexed {index['metadata']['total_files']} total files")
print(f"\n📚 Educational Content:")
print(f"   Units: {len(index['educational_content']['units'])}")
print(f"   Lessons: {len(index['educational_content']['lessons'])}")
print(f"   Handouts: {len(index['educational_content']['handouts'])}")
print(f"   Games: {len(index['educational_content']['games'])}")
print(f"   Tools: {len(index['educational_content']['tools'])}")

print(f"\n📊 By Subject:")
for subject, items in sorted(index['by_subject'].items(), key=lambda x: len(x[1]), reverse=True):
    print(f"   {subject}: {len(items)} files")

print(f"\n📁 Top File Types:")
for ext, count in sorted(index['file_types'].items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"   {ext}: {count}")

print("\n" + "=" * 70)
print("✅ COMPLETE INDEX saved to: COMPLETE-CODEBASE-INDEX.json")
print("=" * 70)
print("\n🎯 Now you can search and understand the entire codebase!")
