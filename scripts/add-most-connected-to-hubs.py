#!/usr/bin/env python3
"""
Add Most Connected widget to remaining subject hubs
"""

import os

base_path = "/Users/admin/Documents/te-kete-ako-clean/public"

# Hubs to enhance
hubs = [
    {
        "file": "digital-technologies-hub.html",
        "subject": "Digital Technologies",
        "display_name": "Digital Technologies"
    },
    {
        "file": "social-studies-hub.html",
        "subject": "Social Studies",
        "display_name": "Social Studies"
    },
    {
        "file": "te-reo-maori-hub.html",
        "subject": "Te Reo Māori",
        "display_name": "Te Reo Māori"
    }
]

# Most Connected widget template
widget_template = '''
        <!-- 🔗 Most Connected Resources (GraphRAG) -->
        <section style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); padding: 3rem 2rem; border-radius: 16px; margin: 3rem 0; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
            <div style="text-align: center; margin-bottom: 2rem;">
                <div style="display: inline-block; background: linear-gradient(135deg, #3b82f6, #2563eb); padding: 0.5rem 1.5rem; border-radius: 24px; margin-bottom: 1rem; color: white; font-weight: 700; font-size: 0.9rem;">🔗 Most Connected</div>
                <h2 style="font-size: 2.25rem; color: #1a4d2e; margin-bottom: 0.5rem;">Hub Champions</h2>
                <p style="color: #666; font-size: 1rem;">Resources with the strongest GraphRAG connections</p>
            </div>
            <div id="most-connected" data-subject="{subject}" data-limit="8" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;"></div>
        </section>
        <script src="/components/graphrag-most-connected.html"></script>
'''

success_count = 0

print("🚀 Adding Most Connected widget to subject hubs...\n")

for hub in hubs:
    file_path = os.path.join(base_path, hub["file"])
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has widget
        if 'most-connected' in content or 'graphrag-most-connected' in content:
            print(f"⏭️  Already has widget: {hub['display_name']}")
            continue
        
        # Find insertion point (before "Browse All Resources" or "Fresh Orphans")
        insert_markers = [
            '🗂️ Browse All Resources',
            'Browse All Resources',
            '🔗 Fresh Orphans',
            'Fresh Orphans'
        ]
        
        insert_pos = -1
        for marker in insert_markers:
            pos = content.find(marker)
            if pos > 0:
                # Find the start of the section (look backwards for <section)
                section_start = content.rfind('<section', 0, pos)
                if section_start > 0:
                    insert_pos = section_start
                    break
        
        if insert_pos == -1:
            print(f"⚠️  Could not find insertion point: {hub['display_name']}")
            continue
        
        # Insert widget
        widget = widget_template.format(subject=hub['subject'])
        new_content = content[:insert_pos] + widget + "\n\n" + content[insert_pos:]
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ SUCCESS: {hub['display_name']}")
        success_count += 1
        
    except Exception as e:
        print(f"❌ ERROR: {hub['display_name']} - {str(e)}")

print("\n" + "=" * 60)
print("📊 SUMMARY")
print("=" * 60)
print(f"✅ Success: {success_count} hubs")
print(f"📝 Total: {len(hubs)} hubs processed")
print("=" * 60)

