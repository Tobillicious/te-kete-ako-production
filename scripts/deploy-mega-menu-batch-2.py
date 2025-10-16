#!/usr/bin/env python3
"""
Deploy Mega Menu to Next 100 Pages - Batch 2
Task 4 - Systematic expansion of professional navigation
Agent-9 with Agent-4 verification
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def find_pages_without_mega_menu():
    """Find HTML pages that don't have mega menu yet"""
    all_html = list(PUBLIC_DIR.glob('**/*.html'))
    
    without_mega_menu = []
    
    for html_file in all_html:
        # Skip certain directories
        if any(skip in str(html_file) for skip in ['node_modules', 'dist', 'archive', 'backup']):
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if has mega menu or navigation component
            has_nav = any(nav in content for nav in [
                'navigation-mega-menu',
                'header-next-level',
                'navigation-header',
                'beautiful-nav-container'
            ])
            
            if not has_nav:
                rel_path = html_file.relative_to(PUBLIC_DIR)
                without_mega_menu.append(rel_path)
        except:
            continue
    
    return without_mega_menu

def deploy_mega_menu(filepath):
    """Add mega menu navigation to page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has navigation
        if any(nav in content for nav in ['navigation-mega-menu', 'header-next-level', 'beautiful-nav']):
            return False
        
        # Find <body> tag and add navigation after it
        body_pattern = r'(<body[^>]*>)'
        match = re.search(body_pattern, content)
        
        if match:
            nav_component = '''
    
    <!-- MEGA MENU NAVIGATION -->
    <div id="navigation-container"></div>
    <script>
        fetch('/components/navigation-mega-menu.html')
            .then(r => r.text())
            .then(html => document.getElementById('navigation-container').innerHTML = html)
            .catch(e => console.warn('Nav:', e));
    </script>
'''
            content = content.replace(match.group(0), match.group(0) + nav_component)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        return False
    
    except Exception as e:
        print(f"   ⚠️  {filepath.name}: {str(e)[:40]}")
        return False

def main():
    print("🚀 MEGA MENU DEPLOYMENT - BATCH 2")
    print("=" * 70)
    
    # Find pages without navigation
    pages = find_pages_without_mega_menu()
    print(f"Found {len(pages)} pages without mega menu\n")
    
    # Deploy to first 100
    batch_size = 100
    deployed = 0
    
    for i, page in enumerate(pages[:batch_size]):
        filepath = PUBLIC_DIR / page
        if deploy_mega_menu(filepath):
            print(f"   ✅ {page}")
            deployed += 1
        
        if (i + 1) % 20 == 0:
            print(f"   ... {i + 1}/{min(len(pages), batch_size)} processed")
    
    print("\n" + "=" * 70)
    print(f"✅ Deployed mega menu to {deployed} additional pages")
    print(f"📊 Remaining pages without nav: {len(pages) - deployed}")
    print(f"🎯 Total pages with nav: 607 + {deployed} = {607 + deployed}\n")
    
    return deployed

if __name__ == '__main__':
    count = main()
    print(f"📊 Batch 2 deployments: {count}")

