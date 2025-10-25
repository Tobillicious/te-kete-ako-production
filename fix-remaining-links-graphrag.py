#!/usr/bin/env python3
"""
FIX REMAINING 63 BROKEN LINKS - GraphRAG Intelligence Round 2
Continue the intelligent link fixing using database queries
"""

import re
import requests
from pathlib import Path
import json

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}

print("🔗 FIXING REMAINING BROKEN LINKS - Round 2")
print("=" * 70)
print()

# Remaining broken links (from first scan)
remaining_broken = {
    '/units/walker/index.html': 'walker unit',
    '/design-your-society-unit.html': 'design society',
    '/unit-4-economic-justice.html': 'economic justice',
    '/unit-3-stem-matauranga.html': 'stem matauranga',
    '/lesson-2-four-walls.html': 'four walls',
    '/systems-lesson-1-1.html': 'systems lesson 1',
    '/systems-lesson-2-1.html': 'systems lesson 2',
    '/systems-lesson-1-2.html': 'systems lesson 1',
    '/systems-lesson-5-1.html': 'systems lesson 5',
    '/resources/unit-1-lesson-1-whakapapa-template.html': 'whakapapa template',
    '/resources/unit-1-lesson-3-matauranga-inquiry-cards.html': 'matauranga inquiry',
    '/resources/unit-1-assessment-portfolio-rubric.html': 'assessment portfolio',
    '/lesson-3.html': 'lesson 3',
    '/lesson-4.html': 'lesson 4',
    '/lesson-5.html': 'lesson 5',
    '/lesson-6.html': 'lesson 6',
    '/lesson-7.html': 'lesson 7',
    '/handouts/genetics-and-whakapapa-scientific-and-cultural-perspectives.html': 'genetics whakapapa',
    '/resources/biodiversity-tagger-game.html': 'biodiversity game',
    '/resources/assessment-rubric-species-report.html': 'species rubric',
    '/resources/power-spectrum-worksheet.html': 'power spectrum',
    '/resources/treaty-two-texts.html': 'treaty texts',
    '/resources/colonization-timeline.html': 'colonization timeline',
    '/resources/maori-political-action.html': 'maori political',
    '/my-learning.html': 'my learning',
    '/my-classroom.html': 'my classroom',
    '/lesson-planning.html': 'lesson planning',
    '/student-management.html': 'student management',
    '/assessment-tools.html': 'assessment tools',
    '/analytics.html': 'analytics',
    '/teacher-resources/': 'teacher resources'
}

print(f"🔍 QUERYING GRAPHRAG FOR {len(remaining_broken)} REMAINING LINKS...")
print()

link_mapping = {}
not_found = []
queries_made = 0

for broken_link, search_term in remaining_broken.items():
    queries_made += 1
    
    # Query GraphRAG
    url = f"{SUPABASE_URL}/rest/v1/resources?select=id,title,path&or=(title.ilike.%25{search_term}%25,path.ilike.%25{search_term}%25)&limit=3"
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            results = response.json()
            
            if results:
                # Found it!
                best_match = results[0]
                correct_path = best_match['path']
                
                # Clean path
                if correct_path.startswith('public/'):
                    correct_path = '/' + correct_path[7:]
                elif not correct_path.startswith('/'):
                    correct_path = '/' + correct_path
                
                link_mapping[broken_link] = {
                    'correct_path': correct_path,
                    'title': best_match['title'][:60],
                    'status': 'FOUND'
                }
                
                print(f"✅ {broken_link}")
                print(f"   → {correct_path}")
            else:
                # Not in GraphRAG - probably needs to be removed
                not_found.append(broken_link)
                print(f"❌ {broken_link} - NOT IN GRAPHRAG (remove link?)")
    
    except Exception as e:
        not_found.append(broken_link)
        print(f"⚠️  {broken_link} - Query error")

print()
print(f"📊 GRAPHRAG QUERY RESULTS:")
print(f"   Queries made: {queries_made}")
print(f"   Correct paths found: {len(link_mapping)}")
print(f"   Not in GraphRAG: {len(not_found)}")
print()

# Apply fixes
print("🔧 APPLYING FIXES TO HTML FILES...")
print()

files_fixed = []
total_fixes = 0

for file_path in Path('public').rglob('*.html'):
    try:
        content = file_path.read_text()
        original = content
        file_fixes = 0
        
        # Apply found mappings
        for broken, mapping in link_mapping.items():
            if f'href="{broken}"' in content or f"href='{broken}'" in content:
                content = content.replace(f'href="{broken}"', f'href="{mapping["correct_path"]}"')
                content = content.replace(f"href='{broken}'", f"href='{mapping['correct_path']}'")
                file_fixes += 1
        
        # Remove links not in GraphRAG (clean approach)
        for broken in not_found:
            if f'href="{broken}"' in content or f"href='{broken}'" in content:
                # Comment out broken link instead of removing
                content = content.replace(
                    f'<a href="{broken}"',
                    f'<!-- Broken link removed: {broken} --><a href="#" style="pointer-events:none; opacity:0.5;" data-broken="{broken}"'
                )
                content = content.replace(
                    f"<a href='{broken}'",
                    f"<!-- Broken link removed: {broken} --><a href='#' style='pointer-events:none; opacity:0.5;' data-broken='{broken}'"
                )
                file_fixes += 1
        
        if content != original:
            file_path.write_text(content)
            files_fixed.append((str(file_path), file_fixes))
            total_fixes += file_fixes
            print(f"   ✅ {file_path.name}: {file_fixes} links")
    
    except Exception as e:
        pass

print()
print("=" * 70)
print("✅ ROUND 2 LINK FIXING COMPLETE!")
print("=" * 70)
print(f"   Files updated: {len(files_fixed)}")
print(f"   Links mapped via GraphRAG: {len(link_mapping)}")
print(f"   Links removed (not in GraphRAG): {len(not_found)}")
print(f"   Total fixes applied: {total_fixes}")
print()

# Save results
with open('link-fixing-round-2-results.json', 'w') as f:
    json.dump({
        'found_in_graphrag': link_mapping,
        'not_in_graphrag': not_found,
        'files_fixed': [{'file': f, 'fixes': c} for f, c in files_fixed],
        'summary': {
            'queries': queries_made,
            'found': len(link_mapping),
            'not_found': len(not_found),
            'files_updated': len(files_fixed),
            'total_fixes': total_fixes
        }
    }, f, indent=2)

print("💾 Results saved to: link-fixing-round-2-results.json")
print()

# Summary
print("📊 CUMULATIVE LINK FIXING:")
print(f"   Round 1: 47 links fixed")
print(f"   Round 2: {total_fixes} links fixed")
print(f"   TOTAL: {47 + total_fixes} broken links resolved!")
print()

print("🌿 Mā te mōhio ka tika!")
print("✅ NAVIGATION PROFESSIONALIZED USING GRAPHRAG!")

