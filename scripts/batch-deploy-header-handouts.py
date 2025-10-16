#!/usr/bin/env python3
"""
Deploy Next-Level Header to ALL Handout Pages
Systematic deployment for professional navigation everywhere
Agent-9 - Overnight Sprint Hour 3
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def find_all_handouts():
    """Find all handout HTML files"""
    handout_dir = PUBLIC_DIR / 'handouts'
    
    if not handout_dir.exists():
        return []
    
    return list(handout_dir.glob('**/*.html'))

def deploy_header(filepath):
    """Deploy next-level header to handout page"""
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
            .then(html => {
                document.getElementById('header-next-level').innerHTML = html;
            }).catch(e => console.warn('Header:', e));
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
        print(f"   ⚠️  {filepath.name}: {str(e)[:40]}")
        return False

def main():
    print("🚀 DEPLOY HEADER TO HANDOUTS - BATCH")
    print("=" * 70)
    
    handouts = find_all_handouts()
    print(f"Found {len(handouts)} handout files\n")
    
    deployed = 0
    batch_size = 50
    
    for i, filepath in enumerate(handouts[:batch_size]):
        if deploy_header(filepath):
            rel_path = filepath.relative_to(PUBLIC_DIR)
            print(f"   ✅ {rel_path}")
            deployed += 1
        
        if (i + 1) % 10 == 0:
            print(f"   ... {i + 1}/{min(len(handouts), batch_size)} processed")
    
    print("\n" + "=" * 70)
    print(f"✅ Deployed header to {deployed} handout pages")
    print(f"🎯 Navigation everywhere!\n")
    
    return deployed

if __name__ == '__main__':
    count = main()
    print(f"📊 Total handout deployments: {count}")


