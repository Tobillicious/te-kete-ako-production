#!/usr/bin/env python3
"""
Query GraphRAG for English Lessons
Find all English/Literacy/Writing content from the indexed resources
"""

import json
from collections import Counter

print("📚 QUERYING GRAPHRAG FOR ENGLISH CONTENT")
print("=" * 70)

# Read indexed resources
with open('indexed_resources.json', 'r') as f:
    resources = json.load(f)

print(f"\n✅ Total resources in GraphRAG: {len(resources)}")

# Find English content
english_lessons = []
english_handouts = []
writing_content = []

for resource in resources:
    subject = resource.get('subject', '').lower()
    title = resource.get('title', '').lower()
    path = resource.get('path', '').lower()
    res_type = resource.get('type', '')
    
    # Check if it's English/Literacy/Writing content
    is_english = any(keyword in subject or keyword in title or keyword in path 
                     for keyword in ['english', 'literacy', 'writing', 'writers', 'toolkit'])
    
    if is_english:
        if res_type == 'lesson':
            english_lessons.append(resource)
        elif res_type == 'handout':
            english_handouts.append(resource)
        else:
            writing_content.append(resource)

print(f"\n📖 ENGLISH CONTENT FOUND:")
print(f"   Lessons: {len(english_lessons)}")
print(f"   Handouts: {len(english_handouts)}")
print(f"   Other: {len(writing_content)}")
print(f"   TOTAL: {len(english_lessons) + len(english_handouts) + len(writing_content)}")

# Show sample lessons
print(f"\n📚 SAMPLE ENGLISH LESSONS (first 20):")
for i, lesson in enumerate(english_lessons[:20], 1):
    print(f"{i:2}. {lesson['title'][:60]:<60} | {lesson['path'][:50]}")

# Check directories
print(f"\n📂 ENGLISH CONTENT BY DIRECTORY:")
directories = Counter(['/'.join(r['path'].split('/')[:3]) for r in english_lessons + english_handouts])
for directory, count in directories.most_common(10):
    print(f"   {directory}: {count} files")

# Find Writers Toolkit specifically
writers_toolkit = [r for r in resources if 'writers' in r.get('path', '').lower() and 'toolkit' in r.get('path', '').lower()]
print(f"\n✍️ WRITERS TOOLKIT RESOURCES: {len(writers_toolkit)}")
for wt in writers_toolkit[:10]:
    print(f"   - {wt['title'][:50]} ({wt['type']})")

print("\n" + "=" * 70)
print("✅ Query complete - use this data to organize systematically!")

