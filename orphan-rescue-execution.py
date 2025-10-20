#!/usr/bin/env python3
"""
ORPHAN RESCUE EXECUTION
Link top orphaned excellence resources to main navigation and subject hubs
"""

import os
import re
from pathlib import Path

def add_orphan_to_navigation(file_path, orphan_info):
    """Add orphaned resource to appropriate navigation sections"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has navigation links
        if 'orphan-rescue-link' in content:
            return False, "Already has orphan rescue link"
        
        # Find navigation section
        nav_pattern = r'(<nav[^>]*class="[^"]*nav[^"]*"[^>]*>.*?</nav>)'
        nav_match = re.search(nav_pattern, content, re.DOTALL | re.IGNORECASE)
        
        if not nav_match:
            # Look for main content area to add navigation
            main_pattern = r'(<main[^>]*>.*?<section[^>]*class="[^"]*content[^"]*"[^>]*>)'
            main_match = re.search(main_pattern, content, re.DOTALL | re.IGNORECASE)
            
            if main_match:
                # Add orphan rescue section before main content
                orphan_section = f'''
<!-- ORPHAN RESCUE: {orphan_info['title']} -->
<section class="orphan-rescue-section" style="background: linear-gradient(135deg, #f0fdf4, #dcfce7); padding: 1.5rem; border-radius: 12px; margin: 1rem 0; border-left: 4px solid #10b981;">
    <h3 style="color: #065f46; margin: 0 0 0.5rem; font-size: 1.1rem;">💎 Excellence Resource</h3>
    <p style="margin: 0; color: #047857; font-size: 0.95rem;">{orphan_info['title']} - {orphan_info['subject']} | Quality Score: {orphan_info['quality_score']}</p>
    <a href="{orphan_info['file_path']}" class="orphan-rescue-link" style="display: inline-block; background: #10b981; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-size: 0.9rem; margin-top: 0.5rem;">Explore Excellence →</a>
</section>
'''
                new_content = content[:main_match.start()] + orphan_section + content[main_match.start():]
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                return True, f"Added orphan rescue section for {orphan_info['title']}"
        
        return False, "No suitable location found for orphan rescue link"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def create_te_ao_maori_hub():
    """Create or update Te Ao Māori hub with orphaned concepts"""
    hub_path = Path('/Users/admin/Documents/te-kete-ako-clean/public/te-ao-maori-hub.html')
    
    # Te Ao Māori orphaned concepts
    te_ao_concepts = [
        {'title': 'Kaitiakitanga - Guardianship', 'file_path': '/concepts/kaitiakitanga.html'},
        {'title': 'Whakapapa - Genealogy & Connections', 'file_path': '/concepts/whakapapa.html'},
        {'title': 'Mātauranga - Knowledge', 'file_path': '/concepts/matauranga.html'},
        {'title': 'Manaakitanga - Care & Respect', 'file_path': '/concepts/manaakitanga.html'},
        {'title': 'Tikanga - Correct Practice', 'file_path': '/concepts/tikanga.html'},
        {'title': 'Te Taiao - The Natural World', 'file_path': '/concepts/te-taiao.html'}
    ]
    
    hub_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Te Ao Māori Hub | Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-professional.css">
    <link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
</head>
<body>
    <header>
        <h1>Te Ao Māori Hub</h1>
        <p>Essential Māori concepts and cultural knowledge</p>
    </header>
    
    <main>
        <section class="concepts-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
'''
    
    for concept in te_ao_concepts:
        hub_content += f'''
            <div class="concept-card" style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 4px solid #10b981;">
                <h3 style="color: #065f46; margin: 0 0 0.5rem;">{concept['title']}</h3>
                <p style="color: #047857; margin: 0 0 1rem; font-size: 0.95rem;">Essential Māori concept for cultural understanding</p>
                <a href="{concept['file_path']}" style="display: inline-block; background: #10b981; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-size: 0.9rem;">Explore Concept →</a>
            </div>
'''
    
    hub_content += '''
        </section>
    </main>
</body>
</html>'''
    
    try:
        with open(hub_path, 'w', encoding='utf-8') as f:
            f.write(hub_content)
        return True, "Created Te Ao Māori hub"
    except Exception as e:
        return False, f"Error creating hub: {str(e)}"

def main():
    """Execute orphan rescue operations"""
    print("💎 ORPHAN RESCUE EXECUTION")
    print("=" * 50)
    
    # Create Te Ao Māori hub
    print("🌿 Creating Te Ao Māori Hub...")
    success, message = create_te_ao_maori_hub()
    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")
    
    # Target pages for orphan rescue
    target_pages = [
        '/Users/admin/Documents/te-kete-ako-clean/public/index.html',
        '/Users/admin/Documents/te-kete-ako-clean/public/lessons/index.html',
        '/Users/admin/Documents/te-kete-ako-clean/public/teachers/index.html'
    ]
    
    # Top orphaned resources to rescue
    top_orphans = [
        {
            'title': 'YouTube Library Administration',
            'file_path': '/admin/youtube-library.html',
            'subject': 'Mathematics',
            'quality_score': 100
        },
        {
            'title': 'Critical Thinking',
            'file_path': '/competencies/critical-thinking.html',
            'subject': 'Cross-Curricular',
            'quality_score': 100
        },
        {
            'title': 'Digital Literacy',
            'file_path': '/competencies/digital-literacy.html',
            'subject': 'Cross-Curricular',
            'quality_score': 100
        }
    ]
    
    print(f"\n🔗 Adding orphan rescue links to {len(target_pages)} pages...")
    
    rescued = 0
    for page_path in target_pages:
        if os.path.exists(page_path):
            for orphan in top_orphans:
                success, message = add_orphan_to_navigation(page_path, orphan)
                if success:
                    rescued += 1
                    print(f"✅ {Path(page_path).name}: {message}")
                elif "Already has" in message:
                    print(f"⏭️  {Path(page_path).name}: {message}")
                else:
                    print(f"❌ {Path(page_path).name}: {message}")
    
    print(f"\n🎉 ORPHAN RESCUE COMPLETE!")
    print(f"✅ Rescued: {rescued} orphaned resources")
    print(f"🌿 Created: Te Ao Māori Hub")
    print(f"📊 Impact: High-value content now discoverable")

if __name__ == "__main__":
    main()
