#!/usr/bin/env python3
"""
BATCH APPLY PROFESSIONALIZATION FEATURES
Add Quick Start guides, Answer Key notices, and Curated lists to appropriate pages
"""

from pathlib import Path
import re

print("🚀 BATCH PROFESSIONALIZATION APPLICATION")
print("=" * 70)
print()

# Load templates
quick_start = Path('quick-start-template.html').read_text()
answer_key = Path('answer-key-notice-template.html').read_text()

# =============================================================================
# STEP 1: Add Quick Start to Top Lessons
# =============================================================================
print("📚 STEP 1: Adding Quick Start Guides to Lessons")
print("-" * 70)

lesson_files = list(Path('public/lessons').rglob('*.html'))
lessons_enhanced = 0

for lesson_file in lesson_files[:30]:  # Top 30 lessons
    try:
        content = lesson_file.read_text()
        
        # Skip if already has quick-start
        if 'quick-start-guide' in content:
            continue
        
        # Find first <h1> or <h2> and insert after
        if '<h1' in content:
            # Insert after first heading
            pattern = r'(<h1[^>]*>.*?</h1>)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                insert_pos = match.end()
                new_content = content[:insert_pos] + '\n\n' + quick_start + '\n\n' + content[insert_pos:]
                lesson_file.write_text(new_content)
                lessons_enhanced += 1
                print(f"   ✅ {lesson_file.name}")
    except Exception as e:
        pass

print(f"\n✅ Enhanced {lessons_enhanced} lessons with Quick Start guides")
print()

# =============================================================================
# STEP 2: Add Answer Key Notices
# =============================================================================
print("📝 STEP 2: Adding Answer Key Notices")
print("-" * 70)

answer_key_added = 0

for lesson_file in lesson_files[:30]:
    try:
        content = lesson_file.read_text()
        
        # Skip if already has answer-key-notice
        if 'answer-key-notice' in content:
            continue
        
        # Find assessment section or end of main content
        if 'assessment' in content.lower() or 'activity' in content.lower():
            # Insert before closing main or article tag
            if '</main>' in content:
                content = content.replace('</main>', answer_key + '\n</main>')
                lesson_file.write_text(content)
                answer_key_added += 1
                print(f"   ✅ {lesson_file.name}")
    except:
        pass

print(f"\n✅ Added answer key notices to {answer_key_added} lessons")
print()

# =============================================================================
# STEP 3: Integrate Curated Lists into Hubs
# =============================================================================
print("⭐ STEP 3: Adding Curated Lists to Subject Hubs")
print("-" * 70)

import json

# Load curated lists
with open('curated-top-10-lists.json') as f:
    curated = json.load(f)

hub_pages = [
    'public/mathematics-hub.html',
    'public/science-hub.html',
    'public/english-hub.html',
    'public/social-studies-hub.html',
    'public/digital-technologies-hub.html'
]

hubs_enhanced = 0

for hub_path in hub_pages:
    try:
        if not Path(hub_path).exists():
            continue
        
        content = Path(hub_path).read_text()
        
        # Skip if already has top-10
        if 'top-10-curated' in content.lower():
            continue
        
        # Extract subject from filename
        subject = hub_path.split('/')[-1].replace('-hub.html', '').replace('-', ' ').title()
        
        # Create curated section HTML
        curated_html = f'''
<!-- TOP 10 CURATED LISTS -->
<section class="top-10-curated" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd); padding: 2rem; border-radius: 12px; margin: 2rem 0;">
    <h2 style="color: #0c4a6e; margin-top: 0;">⭐ Top 10 {subject} Resources</h2>
    <p style="color: #075985; margin-bottom: 1.5rem;">Handpicked high-quality resources to start with</p>
    
    <div class="year-level-tabs" style="display: flex; gap: 1rem; margin-bottom: 1rem;">
        <button class="year-tab active" data-year="7" style="padding: 0.75rem 1.5rem; background: white; border: 2px solid #0284c7; border-radius: 8px; cursor: pointer; font-weight: 600; color: #0284c7;">Year 7</button>
        <button class="year-tab" data-year="8" style="padding: 0.75rem 1.5rem; background: white; border: 2px solid #cbd5e1; border-radius: 8px; cursor: pointer; font-weight: 600; color: #64748b;">Year 8</button>
        <button class="year-tab" data-year="9" style="padding: 0.75rem 1.5rem; background: white; border: 2px solid #cbd5e1; border-radius: 8px; cursor: pointer; font-weight: 600; color: #64748b;">Year 9</button>
        <button class="year-tab" data-year="10" style="padding: 0.75rem 1.5rem; background: white; border: 2px solid #cbd5e1; border-radius: 8px; cursor: pointer; font-weight: 600; color: #64748b;">Year 10</button>
    </div>
    
    <div id="curated-list-container">
        <p style="color: #475569;">Select a year level above to see top resources...</p>
    </div>
</section>

<script>
// Load curated lists from data
const curatedLists = {json.dumps(curated, indent=2)};

// Tab switching
document.querySelectorAll('.year-tab').forEach(tab => {{
    tab.addEventListener('click', () => {{
        // Update active state
        document.querySelectorAll('.year-tab').forEach(t => {{
            t.style.border = '2px solid #cbd5e1';
            t.style.color = '#64748b';
            t.classList.remove('active');
        }});
        tab.style.border = '2px solid #0284c7';
        tab.style.color = '#0284c7';
        tab.classList.add('active');
        
        // Load list for selected year
        const year = tab.dataset.year;
        loadCuratedList('{subject}', `Year ${{year}}`);
    }});
}});

function loadCuratedList(subject, year) {{
    const key = `${{subject}}_${{year.replace(' ', '_')}}`;
    const resources = curatedLists[key] || [];
    
    const container = document.getElementById('curated-list-container');
    if (resources.length === 0) {{
        container.innerHTML = '<p style="color: #64748b;">No curated list available for this combination yet.</p>';
        return;
    }}
    
    let html = '<div class="curated-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">';
    
    resources.forEach((resource, index) => {{
        html += `
            <div class="resource-card" style="background: white; padding: 1.5rem; border-radius: 8px; border: 2px solid #e0f2fe; transition: all 0.2s;">
                <div style="display: flex; align-items: start; gap: 0.75rem;">
                    <span style="font-size: 1.5rem; font-weight: 700; color: #0284c7;">${{index + 1}}</span>
                    <div style="flex: 1;">
                        <h3 style="margin: 0 0 0.5rem 0; font-size: 1.1rem; color: #1e40af;">
                            <a href="${{resource.path}}" style="color: #1e40af; text-decoration: none;">${{resource.title}}</a>
                        </h3>
                    </div>
                </div>
            </div>
        `;
    }});
    
    html += '</div>';
    container.innerHTML = html;
}}

// Load Year 7 by default
loadCuratedList('{subject}', 'Year 7');
</script>
'''
        
        # Insert before </body> or after hero section
        if '<main' in content:
            # Insert after opening <main> tag
            main_match = re.search(r'<main[^>]*>', content)
            if main_match:
                insert_pos = main_match.end()
                content = content[:insert_pos] + curated_html + content[insert_pos:]
                Path(hub_path).write_text(content)
                hubs_enhanced += 1
                print(f"   ✅ {hub_path.split('/')[-1]}")
    except Exception as e:
        print(f"   ⚠️  {hub_path}: {e}")

print(f"\n✅ Enhanced {hubs_enhanced} hub pages with curated lists")
print()

# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 70)
print("🎊 BATCH PROFESSIONALIZATION COMPLETE!")
print("=" * 70)
print(f"   Lessons with Quick Start: {lessons_enhanced}")
print(f"   Lessons with Answer Key notice: {answer_key_added}")
print(f"   Hubs with Top 10 lists: {hubs_enhanced}")
print()

total_enhancements = lessons_enhanced + answer_key_added + hubs_enhanced
print(f"📊 TOTAL FILES ENHANCED: {total_enhancements}")
print()

print("✅ PROFESSIONALIZATION FEATURES DEPLOYED!")
print("🌿 Haere tonu! (Keep going!)")

