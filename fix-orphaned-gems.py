#!/usr/bin/env python3
"""
FIX ORPHANED GEMS - Add 995 excellent but hidden pages to navigation
Create subject hubs, year level hubs, feature pages
"""

import json

with open('strategic-analysis-results.json', 'r') as f:
    analysis = json.load(f)

print("🔗 FIXING ORPHANED GEMS - Adding to Navigation")
print("=" * 70)

orphaned = analysis.get('orphaned_gems', [])
print(f"\nFound {len(orphaned)} orphaned gems to surface\n")

# Top 20 to add to homepage/navigation immediately
top_orphans = orphaned[:20]

print("🎯 TOP 20 TO FEATURE IMMEDIATELY:\n")

homepage_sections = {
    'Interactive Tools': [],
    'Teacher Resources': [],
    'Cultural Experiences': [],
    'Assessment & Planning': []
}

for path, inbound_count in top_orphans:
    if 'numeracy' in path or 'literacy' in path or 'purakau' in path:
        homepage_sections['Interactive Tools'].append(path)
    elif 'teacher' in path or 'admin' in path or 'dashboard' in path:
        homepage_sections['Teacher Resources'].append(path)
    elif 'whakapapa' in path or 'marae' in path or 'cultural' in path:
        homepage_sections['Cultural Experiences'].append(path)
    elif 'curriculum' in path or 'assessment' in path:
        homepage_sections['Assessment & Planning'].append(path)

for section, paths in homepage_sections.items():
    if paths:
        print(f"\n📌 {section}:")
        for path in paths:
            filename = path.split('/')[-1]
            print(f"   • {filename}")

# Generate HTML snippets to add to homepage
print("\n" + "=" * 70)
print("📝 HOMEPAGE ADDITIONS NEEDED")
print("=" * 70)

html_additions = []

if homepage_sections['Teacher Resources']:
    html_additions.append("""
<!-- TEACHER RESOURCES HUB -->
<div style="background: linear-gradient(135deg, #fef3c7, #fde68a); padding: 2.5rem; border-radius: 12px; margin-bottom: 2rem;">
    <h3 style="font-size: 1.8rem; color: #92400e; margin-bottom: 1.5rem;">
        👩‍🏫 Teacher Resource Hub
    </h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <a href="/teacher-dashboard-ai.html" style="background: white; padding: 1rem; border-radius: 8px; text-decoration: none; color: #92400e; font-weight: 600;">
            🤖 AI Teacher Dashboard →
        </a>
        <a href="/admin-youtube-library.html" style="background: white; padding: 1rem; border-radius: 8px; text-decoration: none; color: #92400e; font-weight: 600;">
            📺 YouTube Library →
        </a>
    </div>
</div>
""")

if homepage_sections['Interactive Tools']:
    html_additions.append("""
<!-- Already added by user! Māori Numeracy Adventures -->
""")

if homepage_sections['Assessment & Planning']:
    html_additions.append("""
<!-- CURRICULUM & ASSESSMENT -->
<div style="background: linear-gradient(135deg, #e0e7ff, #c7d2fe); padding: 2.5rem; border-radius: 12px; margin-bottom: 2rem;">
    <h3 style="font-size: 1.8rem; color: #3730a3; margin-bottom: 1.5rem;">
        📋 Curriculum & Assessment Tools
    </h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        <a href="/curriculum-science.html" style="background: white; padding: 1rem; border-radius: 8px; text-decoration: none; color: #3730a3; font-weight: 600;">
            🔬 Science Curriculum →
        </a>
        <a href="/curriculum-alignment.html" style="background: white; padding: 1rem; border-radius: 8px; text-decoration: none; color: #3730a3; font-weight: 600;">
            📊 Full Alignment →
        </a>
    </div>
</div>
""")

with open('homepage-additions.html', 'w') as f:
    f.write('\n'.join(html_additions))

print("\n✅ Generated homepage-additions.html")
print("\n📋 Add these sections to public/index.html to surface orphaned gems!")
print("\n" + "=" * 70)

