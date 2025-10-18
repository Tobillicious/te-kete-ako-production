#!/usr/bin/env python3
"""
🎨 Deploy Ultimate Beauty System to Mega-Hub Pages
These pages have 4,000+ GraphRAG connections - they need to look INCREDIBLE!
"""

import os
import re
from pathlib import Path

# Mega-hub pages to beautify
MEGA_HUBS = [
    '/Users/admin/Documents/te-kete-ako-clean/public/assessments-complete.html',
    '/Users/admin/Documents/te-kete-ako-clean/public/handouts-complete.html',
    '/Users/admin/Documents/te-kete-ako-clean/public/lessons-complete.html',
    '/Users/admin/Documents/te-kete-ako-clean/public/units/year-7-complete-curriculum.html',
    '/Users/admin/Documents/te-kete-ako-clean/public/units/year-8-complete-curriculum.html',
    '/Users/admin/Documents/te-kete-ako-clean/public/units/year-9-complete-curriculum.html',
    '/Users/admin/Documents/te-kete-ako-clean/public/units/complete-units-index.html',
]

def deploy_beauty_to_mega_hub(file_path):
    """Apply Ultimate Beauty System to a mega-hub page"""
    
    if not os.path.exists(file_path):
        print(f"❌ {file_path} not found")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has Ultimate Beauty System
    if 'te-kete-ultimate-beauty-system.css' in content:
        print(f"✅ {os.path.basename(file_path)} already has Ultimate Beauty System")
        return False
    
    # 1. Add Ultimate Beauty System CSS
    if '<link rel="stylesheet"' in content and 'te-kete-ultimate-beauty-system.css' not in content:
        content = content.replace(
            '<link rel="stylesheet"',
            '''<!-- 🎨 ULTIMATE BEAUTY SYSTEM -->
    <link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="/tailwind.config.ultimate.js"></script>
    
    <link rel="stylesheet"''',
            1
        )
    
    # 2. Add whakairo pattern (storytelling/heritage) to body tag
    content = re.sub(
        r'<body([^>]*)>',
        r'<body class="pattern-whakairo"\1>',
        content
    )
    
    # 3. Replace purple gradients with cultural pounamu-moana gradient
    content = re.sub(
        r'linear-gradient\([^)]*#7c3aed[^)]*\)',
        'linear-gradient(135deg, #1B7F5A 0%, #006994 50%, #fbbf24 100%)',
        content
    )
    content = re.sub(
        r'linear-gradient\([^)]*#5b21b6[^)]*\)',
        'linear-gradient(135deg, #1B7F5A 0%, #006994 50%, #fbbf24 100%)',
        content
    )
    
    # 4. Add Framer Motion script
    if 'framer-cultural-gestures-ultimate.js' not in content:
        content = content.replace(
            '</body>',
            '''    <!-- 🎨 Cultural Motion System -->
    <script src="/js/framer-cultural-gestures-ultimate.js"></script>
</body>'''
        )
    
    # 5. Update shadows to cultural pounamu glow
    content = re.sub(
        r'rgba\(124,\s*58,\s*237,\s*[\d.]+\)',
        'rgba(27, 127, 90, 0.15)',
        content
    )
    
    # 6. Make hero sections use Playfair Display
    content = re.sub(
        r'(<h1[^>]*style="[^"]*)(font-family:[^;]+;)',
        r"\1font-family: 'Playfair Display', serif; font-weight: 900;",
        content
    )
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Deploy beauty to all mega-hub pages"""
    
    print("🎨 DEPLOYING ULTIMATE BEAUTY TO MEGA-HUBS...")
    print("=" * 60)
    print("🌟 These pages have 1,000+ GraphRAG connections each!")
    print("=" * 60)
    
    updated_count = 0
    
    for file_path in MEGA_HUBS:
        filename = os.path.basename(file_path)
        if deploy_beauty_to_mega_hub(file_path):
            print(f"  ✨ {filename}: Beauty deployed!")
            updated_count += 1
        else:
            print(f"  ⏭️  {filename}: Already beautiful or not found")
    
    print("\n" + "=" * 60)
    print(f"🎨 MEGA-HUB BEAUTY DEPLOYMENT COMPLETE!")
    print(f"✅ Updated: {updated_count} mega-hub pages")
    print(f"🌿 Pattern: Whakairo (carved patterns - stories, heritage)")
    print(f"🎨 Gradient: Pounamu → Moana → Kōwhai (full cultural spectrum)")
    print(f"✨ Features: Glass morphism, Playfair Display, Hariru animations")
    print("=" * 60)

if __name__ == '__main__':
    main()

