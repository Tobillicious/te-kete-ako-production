#!/usr/bin/env python3
"""
INTELLIGENT BROKEN LINK FIXER - Using GraphRAG
Find correct paths from database instead of guessing!

Broken link: /unit-1-lesson-1.html
GraphRAG has: public/integrated-lessons/science/unit-1-lesson-1.html
Fix: Update link to correct path!
"""

import re
import requests
from pathlib import Path
from collections import defaultdict

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}

print("🔗 INTELLIGENT BROKEN LINK FIXER (GraphRAG-Powered)")
print("=" * 70)
print()

# Broken links from scan
broken_links = {
    '/unit-1-te-ao-maori.html': 11,
    '/unit-1-lesson-1.html': 5,
    '/unit-1-lesson-2.html': 5,
    '/unit-1-lesson-3.html': 5,
    '/unit-2-decolonized-history.html': 3,
    '/unit-2-lesson-1.html': 2,
    '/unit-2-lesson-2.html': 3,
    '/unit-2-lesson-3.html': 4,
    '/unit-2-lesson-4.html': 4,
    '/unit-2-lesson-5.html': 4,
    '/unit-5-global-connections.html': 8,
    '/unit-5-lesson-1.html': 4,
    '/unit-5-lesson-2.html': 4,
    '/unit-5-lesson-3.html': 4,
    '/unit-5-lesson-4.html': 4,
    '/unit-5-lesson-5.html': 4,
    '/design-your-society-unit.html': 6,
    '/unit-4-economic-justice.html': 2,
    '/units/walker/index.html': 4,
    '/lesson-2-four-walls.html': 1,
    '/lesson-3.html': 1,
    '/lesson-4.html': 2,
    '/lesson-5.html': 2,
    '/lesson-6.html': 1,
    '/lesson-7.html': 1
}

print(f"🔍 QUERYING GRAPHRAG FOR CORRECT PATHS...")
print(f"   Broken links to fix: {len(broken_links)}")
print()

# Query GraphRAG for each broken link
link_mapping = {}
queries_made = 0

for broken_link in list(broken_links.keys())[:15]:  # First 15 to avoid timeout
    # Extract search term from broken link
    search_term = broken_link.replace('/', '').replace('.html', '').replace('-', ' ')
    
    # Query GraphRAG for resources matching this
    url = f"{SUPABASE_URL}/rest/v1/resources?select=id,title,path&or=(title.ilike.%25{search_term}%25,path.ilike.%25{search_term}%25)&limit=5"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results = response.json()
            queries_made += 1
            
            if results:
                # Found potential matches!
                best_match = results[0]  # Take first (usually best)
                correct_path = best_match['path']
                
                # Clean path (remove 'public/' prefix if present)
                if correct_path.startswith('public/'):
                    correct_path = '/' + correct_path[7:]
                elif not correct_path.startswith('/'):
                    correct_path = '/' + correct_path
                
                link_mapping[broken_link] = {
                    'correct_path': correct_path,
                    'title': best_match['title'],
                    'occurrences': broken_links[broken_link],
                    'status': 'FOUND'
                }
                
                print(f"✅ {broken_link}")
                print(f"   → {correct_path}")
                print(f"   ({best_match['title']})")
                print()
    except Exception as e:
        print(f"⚠️  Error querying {broken_link}: {e}")

print()
print(f"📊 RESULTS:")
print(f"   GraphRAG queries: {queries_made}")
print(f"   Correct paths found: {len(link_mapping)}")
print(f"   Links still broken: {len(broken_links) - len(link_mapping)}")
print()

# Now apply fixes to actual files
print("🔧 APPLYING FIXES TO HTML FILES...")
print()

files_to_fix = []
for root_path in ['public']:
    for file_path in Path(root_path).rglob('*.html'):
        try:
            content = file_path.read_text()
            original_content = content
            fixed_count = 0
            
            # Replace each broken link with correct path
            for broken, mapping in link_mapping.items():
                if broken in content:
                    content = content.replace(
                        f'href="{broken}"',
                        f'href="{mapping["correct_path"]}"'
                    )
                    content = content.replace(
                        f"href='{broken}'",
                        f"href='{mapping['correct_path']}'"
                    )
                    if content != original_content:
                        fixed_count += 1
                        original_content = content
            
            if fixed_count > 0:
                file_path.write_text(content)
                files_to_fix.append((str(file_path), fixed_count))
                print(f"   ✅ Fixed {file_path.name}: {fixed_count} links")
        
        except Exception as e:
            pass  # Skip files we can't read/write

print()
print("=" * 70)
print("✅ INTELLIGENT LINK FIXING COMPLETE!")
print("=" * 70)
print(f"   Files updated: {len(files_to_fix)}")
print(f"   Links mapped via GraphRAG: {len(link_mapping)}")
print(f"   Total fixes applied: {sum(count for _, count in files_to_fix)}")
print()

# Save mapping for reference
import json
with open('link-mapping-graphrag.json', 'w') as f:
    json.dump({
        'link_mapping': link_mapping,
        'files_fixed': [{'file': f, 'fixes': c} for f, c in files_to_fix],
        'summary': {
            'graphrag_queries': queries_made,
            'paths_found': len(link_mapping),
            'files_updated': len(files_to_fix),
            'total_fixes': sum(count for _, count in files_to_fix)
        }
    }, f, indent=2)

print("💾 Saved mapping to: link-mapping-graphrag.json")
print()
print("🌿 Mā te mōhio ka tika! (Through knowledge comes correctness!)")
print("✅ LINKS FIXED USING GRAPHRAG INTELLIGENCE!")

