#!/usr/bin/env python3
"""
Deploy Next-Level Header to Generated Resources Alpha
22 AI-generated lesson pages
Agent-9 - Overnight Sprint Hour 4
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

GENERATED_LESSONS = [
    'generated-resources-alpha/lessons/physics-of-traditional-māori-instruments.html',
    'generated-resources-alpha/lessons/health-and-wellbeing-te-whare-tapa-whā-model.html',
    'generated-resources-alpha/lessons/game-development-with-cultural-themes.html',
    'generated-resources-alpha/lessons/scientific-method-using-traditional-māori-practices.html',
    'generated-resources-alpha/lessons/argumentative-writing-on-contemporary-māori-issues.html',
    'generated-resources-alpha/lessons/digital-storytelling-with-pūrākau-framework.html',
    'generated-resources-alpha/lessons/climate-change-through-te-taiao-māori-lens.html',
    'generated-resources-alpha/lessons/creative-problem-solving-with-design-thinking.html',
    'generated-resources-alpha/lessons/renewable-energy-and-māori-innovation.html',
    'generated-resources-alpha/lessons/genetics-and-whakapapa-scientific-and-cultural-perspectives.html',
    'generated-resources-alpha/lessons/traditional-navigation-and-modern-gps-integration.html',
    'generated-resources-alpha/lessons/critical-analysis-of-historical-documents.html',
    'generated-resources-alpha/lessons/debate-skills-with-māori-oratory-traditions.html',
    'generated-resources-alpha/lessons/creative-writing-inspired-by-whakataukī.html',
    'generated-resources-alpha/lessons/research-skills-using-traditional-and-digital-sources.html',
    'generated-resources-alpha/lessons/narrative-writing-using-māori-story-structures.html',
    'generated-resources-alpha/lessons/poetry-analysis-through-māori-literary-traditions.html',
    'generated-resources-alpha/lessons/career-pathways-in-stem-for-māori-students.html',
    'generated-resources-alpha/lessons/statistical-analysis-of-sports-performance.html',
    'generated-resources-alpha/lessons/media-literacy-analyzing-māori-representation.html',
    'generated-resources-alpha/lessons/ai-ethics-through-māori-data-sovereignty.html',
]

def deploy_header(filepath):
    """Deploy next-level header to lesson page"""
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
        print(f"   ⚠️  {filepath}: {str(e)[:40]}")
        return False

def main():
    print("🚀 DEPLOY HEADER TO GENERATED-RESOURCES-ALPHA")
    print("=" * 70)
    
    deployed = 0
    
    for lesson_path in GENERATED_LESSONS:
        filepath = PUBLIC_DIR / lesson_path
        if filepath.exists():
            if deploy_header(filepath):
                print(f"   ✅ {lesson_path}")
                deployed += 1
        else:
            print(f"   ⚠️  {lesson_path} (not found)")
    
    print("\n" + "=" * 70)
    print(f"✅ Deployed header to {deployed} AI-generated lesson pages")
    print(f"🎯 Next-level navigation on premium content!\n")
    
    return deployed

if __name__ == '__main__':
    count = main()
    print(f"📊 Total AI lesson deployments: {count}")


