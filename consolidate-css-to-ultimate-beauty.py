#!/usr/bin/env python3
"""
CONSOLIDATE CSS TO ULTIMATE BEAUTY SYSTEM

Removes cascade conflicts by consolidating 40 CSS files → 6 core files:
1. te-kete-ultimate-beauty-system.css (PRIMARY - Kehinde Wiley design!)
2. cultural-patterns.css (Koru, kowhaiwhai patterns)
3. navigation-standard.css (Navigation components)
4. mobile-revolution.css (Mobile responsive)
5. print.css (Print styles)
6. tailwind.css (Utilities only - loads last!)

REMOVES:
- professionalization-system.css (generic corporate!)
- cascade-fix.css (band-aid, not solution!)
- All duplicate mobile-* files
- Conflicting "professional" CSS

ULTIMATE BEAUTY SYSTEM (Oct 18):
- Kehinde Wiley aesthetic (bold, regal, cultural!)
- Earth-tone palette (pounamu, moana, kowhai, whenua)
- Playfair Display typography (elegant!)
- Cultural patterns (koru, kowhaiwhai)
- User validated: "Older better" = THIS system!
"""

import re
from pathlib import Path

# The 6 core CSS files (in load order)
CORE_CSS_STACK = [
    '/css/te-kete-ultimate-beauty-system.css',  # PRIMARY!
    '/css/cultural-patterns.css',
    '/css/navigation-standard.css',
    '/css/mobile-revolution.css',
    '/css/print.css',
    '/css/tailwind.css'
]

# CSS files to REMOVE (causing conflicts)
REMOVE_CSS = [
    'professionalization-system.css',
    'te-kete-professional.css',
    'cascade-fix.css',
    'mobile-print-fix.css',
    'mobile-modal-fix.css',
    'mobile-share.css',
    'mobile-first-classroom-tablets.css',
    'enhanced-beauty-system.css',
    'main.css',  # Redundant
]

def consolidate_html_css(filepath):
    """Replace CSS includes with Ultimate Beauty stack"""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        original = content
        
        # Find all CSS link tags
        css_links = re.findall(r'<link[^>]*href=["\'][^"\']*\.css["\'][^>]*>', content)
        
        if not css_links:
            return False
        
        # Remove all existing CSS links
        for link in css_links:
            # Keep only if it's a component-specific CSS
            if 'components/' in link:
                continue  # Keep component styles
            content = content.replace(link, '')
        
        # Find </head> and inject Ultimate Beauty stack before it
        ultimate_beauty_stack = '\n'.join([
            '    <!-- ULTIMATE BEAUTY SYSTEM (Kehinde Wiley Cultural Design!) -->',
            f'    <link rel="stylesheet" href="{CORE_CSS_STACK[0]}">',
            f'    <link rel="stylesheet" href="{CORE_CSS_STACK[1]}">',
            f'    <link rel="stylesheet" href="{CORE_CSS_STACK[2]}">',
            f'    <link rel="stylesheet" href="{CORE_CSS_STACK[3]}">',
            f'    <link rel="stylesheet" href="{CORE_CSS_STACK[4]}" media="print">',
            f'    <link rel="stylesheet" href="{CORE_CSS_STACK[5]}">',
            ''
        ])
        
        if '</head>' in content:
            content = content.replace('</head>', f'{ultimate_beauty_stack}</head>')
        
        # Write if changed
        if content != original:
            filepath.write_text(content, encoding='utf-8')
            return True
            
    except Exception as e:
        print(f"  ✗ Error in {filepath.name}: {e}")
        return False
    
    return False

# Execute
print("🎨 CONSOLIDATING TO ULTIMATE BEAUTY SYSTEM")
print("=" * 70)
print("Kehinde Wiley Aesthetic | Cultural Boldness | Premium Design")
print("")

public_dir = Path('public')
html_files = list(public_dir.rglob('*.html'))

consolidated = 0
total = len(html_files)

print(f"Processing {total} HTML files...")
print("")

for i, html_file in enumerate(html_files, 1):
    if i % 100 == 0:
        print(f"  Progress: {i}/{total} files...")
    
    if consolidate_html_css(html_file):
        consolidated += 1

print(f"\n{'='*70}")
print(f"✅ COMPLETE: Consolidated {consolidated}/{total} files")
print(f"🎨 Ultimate Beauty System now standard across site!")
print(f"🌿 Cultural boldness restored!")
print(f"💎 Premium design consistency achieved!")
print("")
print("Next: Test on 50 random pages to verify consistency!")

