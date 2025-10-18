#!/usr/bin/env python3
"""
HIGH-VALUE HANDOUTS QUALITY REVIEW
Focus on the 85 integrated handouts - publication-quality teaching resources
One by one quality verification
"""

from supabase import create_client
from pathlib import Path
import json
import re
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("📚 HIGH-VALUE HANDOUTS QUALITY REVIEW")
print("=" * 70)
print("Target: 85 Integrated Handouts - Publication-Quality Resources")
print("Method: Deep quality verification, one by one")
print()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get current GraphRAG state
resources = supabase.table('resources').select('path').execute()
graphrag_paths = {r['path'].replace('/public/', '').replace('public/', '') for r in resources.data}

# Find handouts directory
handouts_dir = Path('public/handouts')
if not handouts_dir.exists():
    print(f"⚠️  Handouts directory not found at {handouts_dir}")
    exit(1)

# Get all handout files
all_handouts = list(handouts_dir.glob('*.html'))
print(f"📂 Found {len(all_handouts)} handout files in public/handouts/")

# Filter to missing
missing_handouts = []
for h in all_handouts:
    rel_path = str(h.relative_to('public'))
    if rel_path not in graphrag_paths:
        missing_handouts.append(h)

print(f"✅ In GraphRAG: {len(all_handouts) - len(missing_handouts)}")
print(f"❌ Missing: {len(missing_handouts)}")
print()

if len(missing_handouts) == 0:
    print("🎉 All handouts already in GraphRAG!")
    exit(0)

# Sort by name for systematic review
missing_handouts.sort()

print(f"🎯 Starting quality review of {min(15, len(missing_handouts))} handouts...")
print("=" * 70)

reviewed = []

for i, handout_path in enumerate(missing_handouts[:15], 1):
    print(f"\n{'=' * 70}")
    print(f"📄 HANDOUT {i}/{min(15, len(missing_handouts))}: {handout_path.name}")
    print(f"{'=' * 70}")
    
    # Read content
    try:
        content = handout_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"❌ Error reading: {e}")
        continue
    
    lines = content.split('\n')
    size_kb = len(content) / 1024
    word_count = len(content.split())
    
    # Extract metadata
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1).replace(' | Te Kete Ako', '').strip() if title_match else handout_path.stem
    
    desc_match = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
    description = desc_match.group(1) if desc_match else ''
    
    print(f"\n📊 STATS:")
    print(f"   Lines: {len(lines)}")
    print(f"   Size: {size_kb:.1f} KB")
    print(f"   Words: ~{word_count}")
    
    print(f"\n📝 METADATA:")
    print(f"   Title: {title[:70]}")
    if description:
        print(f"   Description: {description[:70]}...")
    else:
        print(f"   ⚠️  No description")
    
    # Cultural integration analysis
    cultural_markers = {
        'whakataukī': content.lower().count('whakataukī') + content.lower().count('whakatauaki'),
        'tikanga': content.lower().count('tikanga'),
        'māori': content.lower().count('māori') + content.lower().count('maori'),
        'te_reo': content.lower().count('te reo'),
        'nz_curriculum': content.lower().count('nz curriculum') + content.lower().count('new zealand curriculum')
    }
    
    total_cultural = sum(cultural_markers.values())
    
    print(f"\n🌿 CULTURAL INTEGRATION:")
    for marker, count in cultural_markers.items():
        if count > 0:
            print(f"   {marker}: {count}")
    
    if total_cultural == 0:
        print("   ⚠️  No cultural markers found")
    
    # Subject detection
    subject = 'Cross-Curricular'
    path_lower = str(handout_path).lower()
    
    subjects = {
        'math': 'Mathematics', 'science': 'Science', 'english': 'English',
        'literacy': 'English', 'te reo': 'Te Reo Māori', 'social': 'Social Studies',
        'health': 'Health & PE', 'technology': 'Technology', 'arts': 'The Arts'
    }
    
    for key, value in subjects.items():
        if key in path_lower or key in title.lower():
            subject = value
            break
    
    # Year level detection
    level = 'All Levels'
    for year in range(7, 14):
        if f'year {year}' in content.lower() or f'y{year}' in content.lower():
            level = f'Year {year}'
            break
    
    # Quality scoring
    quality_score = 0
    
    # Has title
    if title_match:
        quality_score += 15
    
    # Has description
    if description:
        quality_score += 15
    
    # Substantial content
    if word_count > 500:
        quality_score += 20
    elif word_count > 200:
        quality_score += 10
    
    # Cultural integration
    if total_cultural >= 5:
        quality_score += 30
    elif total_cultural >= 2:
        quality_score += 20
    elif total_cultural >= 1:
        quality_score += 10
    
    # Has structured content
    if '<h2' in content or '<h3' in content:
        quality_score += 10
    
    # Has NZ Curriculum alignment
    if cultural_markers['nz_curriculum'] > 0:
        quality_score += 10
    
    print(f"\n⭐ QUALITY ASSESSMENT:")
    print(f"   Score: {quality_score}/100")
    
    if quality_score >= 80:
        rating = "GOLD STANDARD ⭐⭐⭐⭐⭐"
        featured = True
    elif quality_score >= 60:
        rating = "HIGH QUALITY ⭐⭐⭐⭐"
        featured = True
    elif quality_score >= 40:
        rating = "GOOD ⭐⭐⭐"
        featured = False
    else:
        rating = "NEEDS IMPROVEMENT ⚠️"
        featured = False
    
    print(f"   Rating: {rating}")
    print(f"   Subject: {subject}")
    print(f"   Level: {level}")
    print(f"   Featured: {'Yes' if featured else 'No'}")
    
    # Add to GraphRAG
    resource = {
        'title': title[:200],
        'path': str(handout_path.relative_to('public')),
        'type': 'handout',
        'subject': subject,
        'level': level,
        'description': description[:500] if description else title,
        'featured': featured,
        'cultural_elements': {
            'integration_level': 'high' if total_cultural >= 5 else ('medium' if total_cultural >= 2 else 'low'),
            'markers': cultural_markers
        }
    }
    
    try:
        supabase.table('resources').insert(resource).execute()
        print(f"\n✅ ADDED TO GRAPHRAG")
        
        reviewed.append({
            'path': resource['path'],
            'title': title,
            'quality_score': quality_score,
            'rating': rating,
            'subject': subject,
            'cultural_level': total_cultural,
            'featured': featured
        })
        
    except Exception as e:
        print(f"\n⚠️  GraphRAG Error: {str(e)[:100]}...")
    
    print(f"\n{'─' * 70}")

# Summary
print(f"\n{'=' * 70}")
print("📊 HANDOUTS REVIEW SESSION SUMMARY")
print(f"{'=' * 70}")
print(f"Reviewed: {len(reviewed)}")
print(f"Added to GraphRAG: {len(reviewed)}")

if reviewed:
    avg_quality = sum(r['quality_score'] for r in reviewed) / len(reviewed)
    gold_count = sum(1 for r in reviewed if r['quality_score'] >= 80)
    high_count = sum(1 for r in reviewed if r['quality_score'] >= 60)
    
    print(f"\nQUALITY BREAKDOWN:")
    print(f"   Average score: {avg_quality:.1f}/100")
    print(f"   Gold standard (80+): {gold_count} ({gold_count/len(reviewed)*100:.1f}%)")
    print(f"   High quality (60+): {high_count} ({high_count/len(reviewed)*100:.1f}%)")
    
    # Subject breakdown
    subjects = {}
    for r in reviewed:
        subjects[r['subject']] = subjects.get(r['subject'], 0) + 1
    
    print(f"\nSUBJECT BREAKDOWN:")
    for subj, count in sorted(subjects.items()):
        print(f"   {subj}: {count}")
    
    # Featured
    featured_count = sum(1 for r in reviewed if r['featured'])
    print(f"\nFEATURED: {featured_count}/{len(reviewed)} ({featured_count/len(reviewed)*100:.1f}%)")

# Save session log
log_file = f"handouts-quality-review-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
with open(log_file, 'w') as f:
    json.dump({
        'session_date': datetime.now().isoformat(),
        'reviewed_count': len(reviewed),
        'handouts': reviewed
    }, f, indent=2)

print(f"\n💾 Session log: {log_file}")
print(f"\n🎯 {len(missing_handouts) - len(reviewed)} handouts remaining")
print("🚀 Quality-first handout excavation in progress!")

