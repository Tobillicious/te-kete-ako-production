#!/usr/bin/env python3
"""
Restore High-Quality Archive Content to Production
"""
import os
import json
import shutil
from pathlib import Path

print("🔄 RESTORING ARCHIVE GEMS TO PRODUCTION")
print("=" * 70)

# Load mining results
with open('archive-mining-results.json', 'r') as f:
    findings = json.load(f)

# Priority categories (biggest gaps)
priorities = {
    'Arts': 10,  # Need 10 Arts resources (current 6 → 16)
    'Y10-13': 20,  # Need 20 senior secondary (current ~0 → 20)
}

restored = {
    'Arts': [],
    'Y10-13': [],
    'total': 0
}

def restore_file(source_path, category, index):
    """Restore a file to production"""
    try:
        # Parse subject and year from path
        path_parts = source_path.split('/')
        
        # Determine target directory
        if category == 'Arts':
            target_dir = 'public/units/arts'
        elif category == 'Y10-13':
            # Extract year level from findings
            target_dir = 'public/units/senior-secondary'
        else:
            target_dir = f'public/units/{category.lower()}'
        
        # Create directory if needed
        os.makedirs(target_dir, exist_ok=True)
        
        # Generate target filename
        filename = Path(source_path).name
        # Avoid collisions
        target_path = os.path.join(target_dir, f"{index:02d}-{filename}")
        
        # Copy file
        shutil.copy2(source_path, target_path)
        
        return target_path
    except Exception as e:
        print(f"   ⚠️  Failed: {source_path} - {str(e)}")
        return None

# Restore priority categories
for category, count in priorities.items():
    print(f"\n📁 {category}: Restoring top {count} resources...")
    
    items = findings.get(category, [])
    # Sort by quality
    items = sorted(items, key=lambda x: x['quality_score'], reverse=True)
    
    for i, item in enumerate(items[:count], 1):
        target = restore_file(item['path'], category, i)
        if target:
            restored[category].append({
                'title': item['title'],
                'source': item['path'],
                'target': target,
                'quality': item['quality_score']
            })
            restored['total'] += 1
            print(f"   ✅ {i}/{count}: {item['title'][:50]}")

print(f"\n✅ RESTORATION COMPLETE!")
print(f"   Total files restored: {restored['total']}")
print(f"   Arts: {len(restored['Arts'])} files")
print(f"   Senior Secondary (Y10-13): {len(restored['Y10-13'])} files")

# Save restoration log
with open('restoration-log.json', 'w') as f:
    json.dump(restored, f, indent=2)

print(f"\n💾 Log saved to: restoration-log.json")

# Generate navigation updates
print(f"\n📝 Generating navigation updates...")

# Arts hub
arts_html = """
<section class="unit-grid">
    <h2>🎨 Arts Resources</h2>
    <div class="resource-cards">
"""
for item in restored['Arts']:
    relative_path = item['target'].replace('public/', '/')
    arts_html += f"""
        <a href="{relative_path}" class="resource-card">
            <h3>{item['title']}</h3>
            <span class="quality-badge">Quality: {item['quality']}</span>
        </a>
"""
arts_html += """
    </div>
</section>
"""

# Save for integration
with open('navigation-updates-arts.html', 'w') as f:
    f.write(arts_html)

# Senior secondary hub
senior_html = """
<section class="unit-grid">
    <h2>🎓 Senior Secondary (Years 10-13)</h2>
    <div class="resource-cards">
"""
for item in restored['Y10-13']:
    relative_path = item['target'].replace('public/', '/')
    senior_html += f"""
        <a href="{relative_path}" class="resource-card">
            <h3>{item['title']}</h3>
            <span class="quality-badge">Quality: {item['quality']}</span>
        </a>
"""
senior_html += """
    </div>
</section>
"""

with open('navigation-updates-senior.html', 'w') as f:
    f.write(senior_html)

print(f"   ✅ navigation-updates-arts.html")
print(f"   ✅ navigation-updates-senior.html")

print(f"\n🎯 NEXT: Add these sections to public/index.html")

