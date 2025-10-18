#!/usr/bin/env python3
"""
CREATE MASTER INDEX PAGES
Make all 11,840 resources discoverable
"""

from supabase_graphrag_connector import SupabaseGraphRAGConnector
from pathlib import Path

print("📚 CREATING MASTER INDEX PAGES")
print("=" * 70)

connector = SupabaseGraphRAGConnector()
supabase = connector.client

# Get all active resources by type
print("Loading resources...")
lessons = supabase.table('resources').select('*').eq('type', 'lesson').eq('is_active', True).execute()
handouts = supabase.table('resources').select('*').eq('type', 'handout').eq('is_active', True).execute()
units = supabase.table('resources').select('*').eq('type', 'unit-plan').eq('is_active', True).execute()
interactive = supabase.table('resources').select('*').eq('type', 'interactive').eq('is_active', True).execute()

print(f"✅ Lessons: {len(lessons.data):,}")
print(f"✅ Handouts: {len(handouts.data):,}")
print(f"✅ Units: {len(units.data):,}")
print(f"✅ Interactive: {len(interactive.data):,}\n")

# Group by subject
from collections import defaultdict

lessons_by_subject = defaultdict(list)
for lesson in lessons.data:
    subject = lesson.get('subject') or 'General'
    lessons_by_subject[subject].append(lesson)

# Create comprehensive lessons index
lessons_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Lessons ({len(lessons.data):,}) | Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-professional.css">
</head>
<body>
    <div id="navigation-placeholder"></div>
    
    <main class="container">
        <h1>📚 All Lessons ({len(lessons.data):,})</h1>
        <p class="lead">Complete collection of culturally-integrated lessons</p>
"""

for subject in sorted(lessons_by_subject.keys()):
    lessons_list = lessons_by_subject[subject]
    lessons_html += f"""
        <section class="subject-section">
            <h2>{subject} ({len(lessons_list)} lessons)</h2>
            <div class="resource-grid">
"""
    for lesson in sorted(lessons_list, key=lambda x: x.get('title', '')):
        title = lesson.get('title', 'Untitled')
        path = lesson.get('path', '')
        level = lesson.get('level', '')
        
        lessons_html += f"""
                <div class="resource-card">
                    <h3><a href="/{path}">{title}</a></h3>
                    {f'<span class="badge">{level}</span>' if level else ''}
                </div>
"""
    lessons_html += """
            </div>
        </section>
"""

lessons_html += """
    </main>
    <script src="/components/navigation-loader.js"></script>
</body>
</html>
"""

# Write file
Path('public/lessons-complete.html').write_text(lessons_html)
print("✅ Created: public/lessons-complete.html")

# Create handouts index similarly
handouts_by_subject = defaultdict(list)
for handout in handouts.data:
    subject = handout.get('subject') or 'General'
    handouts_by_subject[subject].append(handout)

handouts_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Handouts ({len(handouts.data):,}) | Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-professional.css">
</head>
<body>
    <div id="navigation-placeholder"></div>
    
    <main class="container">
        <h1>📄 All Handouts ({len(handouts.data):,})</h1>
        <p class="lead">Printable resources for students</p>
"""

for subject in sorted(handouts_by_subject.keys()):
    handouts_list = handouts_by_subject[subject]
    handouts_html += f"""
        <section class="subject-section">
            <h2>{subject} ({len(handouts_list)} handouts)</h2>
            <div class="resource-grid">
"""
    for handout in sorted(handouts_list, key=lambda x: x.get('title', '')):
        title = handout.get('title', 'Untitled')
        path = handout.get('path', '')
        
        handouts_html += f"""
                <div class="resource-card">
                    <h3><a href="/{path}">{title}</a></h3>
                </div>
"""
    handouts_html += """
            </div>
        </section>
"""

handouts_html += """
    </main>
    <script src="/components/navigation-loader.js"></script>
</body>
</html>
"""

Path('public/handouts-complete.html').write_text(handouts_html)
print("✅ Created: public/handouts-complete.html")

print("\n✅ Master indexes created!")
print(f"   - {len(lessons.data):,} lessons indexed")
print(f"   - {len(handouts.data):,} handouts indexed")
print(f"   - Organized by {len(lessons_by_subject)} subjects")

