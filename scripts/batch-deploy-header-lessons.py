#!/usr/bin/env python3
"""
Deploy Next-Level Header to ALL Lesson Pages
Systematic deployment to 136 lessons
Agent-9 - Overnight Sprint Hour 2-3
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def find_all_lessons():
    """Find all lesson HTML files"""
    lesson_dirs = [
        'units/y8-statistics/lessons',
        'units/y7-maths-algebra/lessons',
        'units/y9-science-ecology/lessons',
        'y8-systems/lessons',
    ]
    
    all_lessons = []
    
    for lesson_dir in lesson_dirs:
        dir_path = PUBLIC_DIR / lesson_dir
        if dir_path.exists():
            html_files = list(dir_path.glob('*.html'))
            for f in html_files:
                if f.name != 'index.html':
                    all_lessons.append(f)
    
    return all_lessons

def deploy_header(filepath):
    """Deploy next-level header to lesson page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has next-level
        if 'header-next-level' in content:
            return False
        
        # Find old header and replace
        if 'site-header' in content and 'header-next-level' not in content:
            # Replace entire old header section with new component div
            # Find from <header to </header>
            header_pattern = r'<header class="site-header[^"]*".*?</header>'
            if re.search(header_pattern, content, re.DOTALL):
                content = re.sub(
                    header_pattern,
                    '<div id="header-next-level" style="min-height: 72px;"></div>',
                    content,
                    count=1,
                    flags=re.DOTALL
                )
                
                # Add loader script if not present
                if 'header-next-level.html' not in content:
                    loader = '''    <script>
        fetch('/components/header-next-level.html')
            .then(r => r.text())
            .then(html => {
                document.getElementById('header-next-level').innerHTML = html;
            }).catch(e => console.warn('Header load:', e));
    </script>'''
                    
                    content = content.replace('</body>', f'{loader}\n</body>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                return True
        
        return False
    
    except Exception as e:
        print(f"   ❌ {filepath.name}: {str(e)[:40]}")
        return False

def main():
    print("🚀 DEPLOY HEADER TO ALL LESSONS - BATCH")
    print("=" * 70)
    
    lessons = find_all_lessons()
    print(f"Found {len(lessons)} lesson files\n")
    
    deployed = 0
    
    for filepath in lessons:
        if deploy_header(filepath):
            rel_path = filepath.relative_to(PUBLIC_DIR)
            print(f"   ✅ {rel_path}")
            deployed += 1
    
    print("\n" + "=" * 70)
    print(f"✅ Deployed header to {deployed} lesson pages")
    print(f"🎯 Next-level navigation across all units!\n")
    
    return deployed

if __name__ == '__main__':
    count = main()
    print(f"📊 Total lesson deployments: {count}")


