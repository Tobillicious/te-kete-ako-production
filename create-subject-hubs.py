#!/usr/bin/env python3
"""
Create Subject-Based Navigation Hubs
"""
import json
import os
import shutil
from pathlib import Path

print("🎯 CREATING SUBJECT-BASED NAVIGATION HUBS")
print("=" * 70)

# Load archive mining results
with open('archive-mining-results.json', 'r') as f:
    findings = json.load(f)

# Subject configuration
subjects = {
    'Math': {
        'count': 15,
        'icon': '📐',
        'color': '#7c3aed',
        'bg': '#f3e8ff',
        'description': 'Mathematics resources integrating cultural patterns, traditional knowledge, and contemporary curriculum'
    },
    'Science': {
        'count': 15,
        'icon': '🔬',
        'color': '#059669',
        'bg': '#d1fae5',
        'description': 'Science resources connecting mātauranga Māori with modern scientific inquiry'
    },
    'English': {
        'count': 12,
        'icon': '📖',
        'color': '#dc2626',
        'bg': '#fee2e2',
        'description': 'Literacy and English resources including critical literacy, digital storytelling, and cultural texts'
    },
    'Social Studies': {
        'count': 12,
        'icon': '🌏',
        'color': '#ea580c',
        'bg': '#ffedd5',
        'description': 'Social studies resources exploring decolonized history, governance, and contemporary issues'
    }
}

restored = {}

# Restore files for each subject
for subject, config in subjects.items():
    print(f"\n📁 {subject}: Processing...")
    
    items = findings.get(subject, [])
    # Sort by quality and remove duplicates by title
    seen_titles = set()
    unique_items = []
    for item in sorted(items, key=lambda x: x['quality_score'], reverse=True):
        if item['title'] not in seen_titles:
            seen_titles.add(item['title'])
            unique_items.append(item)
    
    # Take top N
    top_items = unique_items[:config['count']]
    
    # Create directory
    subject_dir = f"public/units/{subject.lower().replace(' ', '-')}"
    os.makedirs(subject_dir, exist_ok=True)
    
    # Restore files
    restored[subject] = []
    for i, item in enumerate(top_items, 1):
        try:
            filename = Path(item['path']).name
            target = os.path.join(subject_dir, f"{i:02d}-{filename}")
            shutil.copy2(item['path'], target)
            
            restored[subject].append({
                'title': item['title'],
                'path': target.replace('public/', '/'),
                'quality': item['quality_score'],
                'cultural': item['cultural']
            })
            print(f"   ✅ {i}/{config['count']}: {item['title'][:50]}")
        except Exception as e:
            print(f"   ⚠️  Failed: {item['title'][:50]} - {str(e)}")

print(f"\n✅ SUBJECT HUB FILES RESTORED")
for subject, items in restored.items():
    print(f"   {subjects[subject]['icon']} {subject}: {len(items)} files")

# Save restoration record
with open('subject-hubs-restoration.json', 'w') as f:
    json.dump(restored, f, indent=2)

print(f"\n💾 Restoration record: subject-hubs-restoration.json")
print(f"\n🎯 Next: Creating index pages for each subject hub...")

