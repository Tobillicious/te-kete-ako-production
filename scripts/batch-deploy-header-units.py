#!/usr/bin/env python3
"""
Deploy Next-Level Header to ALL Unit Index Pages
14 unit index pages for comprehensive navigation
Agent-9 - Overnight Sprint Hour 5-6
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

UNIT_INDEX_PAGES = [
    'units/y9-science-ecology/index.html',
    'units/y10-physics-navigation/index.html',
    'units/y9-mathematics-geometry-maori-patterns/index.html',
    'units/y8-statistics/index.html',
    'units/y9-maths-geometry-patterns/index.html',
    'units/y8-digital-kaitiakitanga/index.html',
    'units/y7-digital-technology/index.html',
    'units/y7-science-ecosystems/index.html',
    'units/y10-physics-forces/index.html',
    'units/walker-unit/index.html',
    'units/y7-maths-algebra/index.html',
    'units/unit-1-te-ao-maori/index.html',
    'units/y7-foundational-reading/index.html',
    'units/y8-critical-thinking/index.html',
]

def deploy_header(filepath):
    """Deploy next-level header to unit index page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has next-level
        if 'header-next-level' in content:
            return False
        
        # Replace header-component with next-level
        if 'header-component' in content:
            content = content.replace(
                'id="header-component"',
                'id="header-next-level" style="min-height: 72px;"'
            )
            
            # Add loader if not present
            if 'header-next-level.html' not in content:
                loader = '''    <script>
        fetch('/components/header-next-level.html')
            .then(r => r.text())
            .then(html => document.getElementById('header-next-level').innerHTML = html)
            .catch(e => console.warn('Header:', e));
    </script>'''
                content = content.replace('</body>', f'{loader}\n</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        # Also try replacing old site-header
        elif 'site-header' in content:
            pattern = r'<header class="site-header[^"]*".*?</header>'
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(
                    pattern,
                    '<div id="header-next-level" style="min-height: 72px;"></div>',
                    content,
                    count=1,
                    flags=re.DOTALL
                )
                
                # Add loader
                if 'header-next-level.html' not in content:
                    loader = '''    <script>
        fetch('/components/header-next-level.html')
            .then(r => r.text())
            .then(html => document.getElementById('header-next-level').innerHTML = html)
            .catch(e => console.warn('Header:', e));
    </script>'''
                    content = content.replace('</body>', f'{loader}\n</body>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                return True
        
        return False
    
    except Exception as e:
        print(f"   ⚠️  {filepath.name}: {str(e)[:50]}")
        return False

def main():
    print("🚀 DEPLOY HEADER TO ALL UNIT INDEX PAGES")
    print("=" * 70)
    
    deployed = 0
    
    for unit_path in UNIT_INDEX_PAGES:
        filepath = PUBLIC_DIR / unit_path
        if filepath.exists():
            if deploy_header(filepath):
                print(f"   ✅ {unit_path}")
                deployed += 1
            else:
                print(f"   ⏭️  {unit_path} (already done)")
        else:
            print(f"   ⚠️  {unit_path} (not found)")
    
    print("\n" + "=" * 70)
    print(f"✅ Deployed header to {deployed} unit index pages")
    print(f"🎯 Complete navigation across all units!\n")
    
    return deployed

if __name__ == '__main__':
    count = main()
    print(f"📊 Total unit deployments: {count}")

