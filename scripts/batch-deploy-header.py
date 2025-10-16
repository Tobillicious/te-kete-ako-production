#!/usr/bin/env python3
"""
Batch Deploy Next-Level Header
Deploys beautiful navigation to all key pages
Agent-9 - Overnight Sprint Hour 2
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

# Next batch of pages for header deployment
BATCH_2_PAGES = [
    'curriculum-mathematics.html',
    'curriculum-science.html',
    'curriculum-english.html',
    'curriculum-social-sciences.html',
    'curriculum-arts.html',
    'curriculum-technology.html',
    'about.html',
    'contact.html',
    'teacher-dashboard.html',
    'student-dashboard.html',
    'my-kete.html',
    'units/y8-statistics/index.html',
    'units/y7-algebra/index.html',
    'units/y9-ecology/index.html',
    'units/walker-unit/index.html',
    'lessons/herangi/index.html',
    'lessons/writers-toolkit/index.html',
    'guided-inquiry-unit/index.html',
    'generated-resources-alpha/index.html',
    'critical-thinking/index.html',
]

def deploy_header(filepath):
    """Deploy next-level header to page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has next-level
        if 'header-next-level' in content:
            return False
        
        # Replace header-component with header-next-level
        if 'header-component' in content:
            content = content.replace('id="header-component"', 'id="header-next-level" style="min-height: 72px;"')
            
            # Add loader script if not present
            if 'header-next-level.html' not in content:
                loader = '''
    <script>
        fetch('/components/header-next-level.html')
            .then(r => r.text())
            .then(html => {
                document.getElementById('header-next-level').innerHTML = html;
                console.log('✅ Next-Level Header loaded');
            });
    </script>'''
                
                content = content.replace('</body>', f'{loader}\n</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        return False
    
    except Exception as e:
        print(f"   ❌ {filepath}: {str(e)[:40]}")
        return False

def main():
    print("🚀 BATCH HEADER DEPLOYMENT - HOUR 2")
    print("=" * 70)
    
    deployed = 0
    
    for page_path in BATCH_2_PAGES:
        filepath = PUBLIC_DIR / page_path
        if filepath.exists():
            if deploy_header(filepath):
                print(f"   ✅ {page_path}")
                deployed += 1
            else:
                print(f"   ⏭️  {page_path} (already done)")
        else:
            print(f"   ⚠️  {page_path} (not found)")
    
    print("\n" + "=" * 70)
    print(f"✅ Deployed header to {deployed} pages")
    print(f"🎯 Next-level navigation spreading across site!\n")
    
    return deployed

if __name__ == '__main__':
    count = main()
    print(f"📊 Total new deployments: {count}")


