#!/usr/bin/env python3
"""
Batch Apply West Coast NZ Design
Systematically applies West Coast colors and next-level header
Agent-9 - Overnight Sprint - October 15, 2025
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

# Priority pages for overnight work
PRIORITY_PAGES = [
    'curriculum-index.html',
    'lessons.html',
    'handouts.html',
    'games.html',
    'youtube.html',
    'resource-hub.html',
    'teachers/index.html',
    'units/index.html',
]

def add_west_coast_css(filepath):
    """Add West Coast NZ CSS if not present"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'west-coast-nz-colors.css' in content:
            return False
        
        if '</head>' not in content:
            return False
        
        # Add West Coast CSS before other stylesheets
        if 'te-kete-professional.css' in content:
            content = content.replace(
                '<link rel="stylesheet" href="/css/te-kete-professional.css',
                '<link rel="stylesheet" href="/css/west-coast-nz-colors.css">\n    <link rel="stylesheet" href="/css/te-kete-professional.css'
            )
        else:
            # Add before </head>
            content = content.replace(
                '</head>',
                '    <link rel="stylesheet" href="/css/west-coast-nz-colors.css">\n</head>'
            )
        
        # Also add loading states and CTA enhancements
        if 'loading-states.css' not in content and 'te-kete-professional.css' in content:
            content = content.replace(
                'href="/css/te-kete-professional.css">',
                'href="/css/te-kete-professional.css">\n    <link rel="stylesheet" href="/css/loading-states.css">\n    <link rel="stylesheet" href="/css/cta-enhancements.css">'
            )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"   ❌ Error in {filepath}: {str(e)[:50]}")
        return False

def deploy_next_level_header(filepath):
    """Replace header-component with header-next-level"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'header-next-level' in content:
            return False
        
        if 'header-component' not in content:
            return False
        
        # Replace component div
        content = content.replace(
            'id="header-component"',
            'id="header-next-level"'
        )
        
        # Add component loader if not present
        if 'header-next-level.html' not in content:
            loader_script = '''
    <script>
        // Load Next-Level Header
        fetch('/components/header-next-level.html')
            .then(response => response.text())
            .then(html => {
                document.getElementById('header-next-level').innerHTML = html;
                console.log('✅ Next-Level Header loaded');
            })
            .catch(error => console.error('Header load error:', error));
    </script>'''
            
            # Add before </body>
            content = content.replace('</body>', f'{loader_script}\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"   ❌ Error in {filepath}: {str(e)[:50]}")
        return False

def main():
    print("🌙 OVERNIGHT BATCH PROCESSOR - WEST COAST NZ")
    print("=" * 70)
    
    css_count = 0
    header_count = 0
    
    # Process priority pages first
    print("\n📋 Processing priority pages...")
    for page_path in PRIORITY_PAGES:
        filepath = PUBLIC_DIR / page_path
        if filepath.exists():
            print(f"\n🔄 {page_path}:")
            
            if add_west_coast_css(filepath):
                print(f"   ✅ West Coast CSS added")
                css_count += 1
            else:
                print(f"   ⏭️  Already has CSS")
            
            if deploy_next_level_header(filepath):
                print(f"   ✅ Next-level header deployed")
                header_count += 1
            else:
                print(f"   ⏭️  Header already updated")
    
    # Process all unit index pages
    print("\n\n📋 Processing unit pages...")
    unit_pages = list(PUBLIC_DIR.glob('units/*/index.html'))
    for filepath in unit_pages[:10]:  # First 10 units
        if add_west_coast_css(filepath):
            css_count += 1
        if deploy_next_level_header(filepath):
            header_count += 1
    
    print("\n\n" + "=" * 70)
    print(f"✅ BATCH COMPLETE:")
    print(f"   🎨 West Coast CSS added to: {css_count} pages")
    print(f"   🚀 Next-level header deployed to: {header_count} pages")
    print(f"\n📊 GraphRAG will be updated with these changes.")
    print("🌙 Overnight progress continues...\n")

if __name__ == '__main__':
    main()

