#!/usr/bin/env python3
"""
🎨 Deploy Ultimate Beauty System to All Unit Pages
Systematically update 21 unit pages (Math/Science/English Units 1-7)
"""

import os
import re
from pathlib import Path

# Cultural patterns for each subject
SUBJECT_PATTERNS = {
    'mathematics': 'pattern-tukutuku',  # Geometric weaving for systematic math
    'science': 'pattern-koru',          # Unfurling fern for discovery
    'english': 'pattern-kowhaiwhai'     # Rafter patterns for narrative
}

SUBJECT_GRADIENTS = {
    'mathematics': 'linear-gradient(135deg, #1B7F5A 0%, #0284c7 100%)',  # Pounamu → Moana
    'science': 'linear-gradient(135deg, #006994 0%, #1B7F5A 100%)',      # Moana → Pounamu
    'english': 'linear-gradient(135deg, #fbbf24 0%, #1B7F5A 100%)'       # Kōwhai → Pounamu
}

def deploy_beauty_to_unit(file_path):
    """Apply Ultimate Beauty System to a single unit page"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine subject from path
    subject = None
    for subj in ['mathematics', 'science', 'english']:
        if subj in file_path:
            subject = subj
            break
    
    if not subject:
        print(f"⚠️ Could not determine subject for {file_path}")
        return False
    
    pattern = SUBJECT_PATTERNS[subject]
    gradient = SUBJECT_GRADIENTS[subject]
    
    # Check if already has Ultimate Beauty System
    if 'te-kete-ultimate-beauty-system.css' in content:
        print(f"✅ {file_path} already has Ultimate Beauty System")
        return False
    
    # 1. Add Ultimate Beauty System CSS (after <head> or before first </head>)
    if '<link rel="stylesheet"' in content and 'te-kete-ultimate-beauty-system.css' not in content:
        # Find first stylesheet link and insert before it
        content = content.replace(
            '<link rel="stylesheet"',
            '''<!-- 🎨 ULTIMATE BEAUTY SYSTEM -->
    <link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="/tailwind.config.ultimate.js"></script>
    
    <link rel="stylesheet"''',
            1  # Only replace first occurrence
        )
    
    # 2. Add cultural pattern to body tag
    if f'class="{pattern}"' not in content:
        # Find body tag and add pattern class
        content = re.sub(
            r'<body([^>]*)>',
            f'<body class="{pattern}"\\1>',
            content
        )
    
    # 3. Replace any purple gradients with cultural gradients
    content = re.sub(
        r'linear-gradient\([^)]*#7c3aed[^)]*\)',
        gradient,
        content
    )
    content = re.sub(
        r'linear-gradient\([^)]*#5b21b6[^)]*\)',
        gradient,
        content
    )
    
    # 4. Add Framer Motion script before </body>
    if 'framer-cultural-gestures-ultimate.js' not in content:
        content = content.replace(
            '</body>',
            '''    <!-- 🎨 Cultural Motion System -->
    <script src="/js/framer-cultural-gestures-ultimate.js"></script>
</body>'''
        )
    
    # 5. Update any purple box-shadows to cultural pounamu glow
    content = re.sub(
        r'rgba\(124,\s*58,\s*237,\s*[\d.]+\)',
        'rgba(27, 127, 90, 0.15)',
        content
    )
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Deploy beauty to all 21 unit pages"""
    
    base_dir = Path('/Users/admin/Documents/te-kete-ako-clean/public/units')
    
    subjects = ['mathematics', 'science', 'english']
    updated_count = 0
    
    print("🎨 DEPLOYING ULTIMATE BEAUTY SYSTEM TO ALL UNITS...")
    print("=" * 60)
    
    for subject in subjects:
        print(f"\n📚 {subject.upper()} UNITS:")
        for i in range(1, 8):  # Units 1-7
            unit_dir = base_dir / f'unit-{i}-{subject}'
            index_file = unit_dir / 'index.html'
            
            if index_file.exists():
                if deploy_beauty_to_unit(str(index_file)):
                    print(f"  ✨ Unit {i}: Beauty deployed!")
                    updated_count += 1
                else:
                    print(f"  ⏭️  Unit {i}: Already beautiful")
            else:
                print(f"  ❌ Unit {i}: File not found")
    
    print("\n" + "=" * 60)
    print(f"🎨 BEAUTY DEPLOYMENT COMPLETE!")
    print(f"✅ Updated: {updated_count} unit pages")
    print(f"🌿 Patterns: Tukutuku (Math), Koru (Science), Kōwhaiwhai (English)")
    print(f"✨ Features: Glass morphism, cultural gradients, Hariru animations")
    print("=" * 60)

if __name__ == '__main__':
    main()

