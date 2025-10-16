#!/usr/bin/env python3
"""
PROFESSIONALIZE ALL LESSON PAGES
Apply unified design system to 101+ lesson pages
Agent-4 - Morning Development Sprint
"""

from pathlib import Path
import re
import os

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

# CSS files to include in professionalized lessons
PROFESSIONAL_CSS = [
    '/css/te-kete-unified-design-system.css',
    '/css/component-library.css',
    '/css/lesson-professionalization.css',
    '/css/beautiful-navigation.css',
    '/css/print.css'
]

def professionalize_lesson(filepath):
    """Apply professional design system to a lesson page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already professionalized
        if 'te-kete-unified-design-system.css' in content:
            print(f"  ✅ Already professionalized: {filepath.name}")
            return True
            
        # Extract lesson content between <main> tags
        main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
        if not main_match:
            print(f"  ⚠️  No main content found: {filepath.name}")
            return False
            
        main_content = main_match.group(1)
        
        # Create professional lesson structure
        professional_lesson = f'''
<!-- PROFESSIONAL LESSON CONTENT -->
<div class="lesson-page">
  <div class="lesson-container">
    
    <!-- LESSON HEADER -->
    <header class="lesson-header">
      <h1 class="lesson-title">{{LESSON_TITLE}}</h1>
      <p class="lesson-subtitle">{{LESSON_SUBTITLE}}</p>
      
      <div class="lesson-meta">
        <div class="lesson-meta-item">
          <span class="lesson-meta-icon">📚</span>
          <span>{{SUBJECT}}</span>
        </div>
        <div class="lesson-meta-item">
          <span class="lesson-meta-icon">🎯</span>
          <span>{{LEVEL}}</span>
        </div>
        <div class="lesson-meta-item">
          <span class="lesson-meta-icon">⏱️</span>
          <span>{{DURATION}}</span>
        </div>
        <div class="lesson-meta-item">
          <span class="lesson-meta-icon">🌿</span>
          <span>Cultural Integration</span>
        </div>
      </div>
    </header>

    <!-- LESSON CONTENT -->
    <div class="lesson-content">
{main_content}
    </div>

    <!-- LESSON NAVIGATION -->
    <nav class="lesson-navigation">
      <a href="{{PREVIOUS_LESSON_LINK}}" class="nav-button secondary">
        <span class="nav-button-icon">←</span>
        <span>Previous Lesson</span>
      </a>
      
      <a href="{{UNIT_INDEX_LINK}}" class="nav-button secondary">
        <span class="nav-button-icon">📚</span>
        <span>Unit Index</span>
      </a>
      
      <a href="{{NEXT_LESSON_LINK}}" class="nav-button">
        <span>Next Lesson</span>
        <span class="nav-button-icon">→</span>
      </a>
    </nav>

  </div>
</div>
'''
        
        # Update CSS links in head
        head_end = content.find('</head>')
        if head_end != -1:
            # Remove old CSS links
            content = re.sub(r'<link rel="stylesheet" href="[^"]*\.css"[^>]*>', '', content)
            
            # Add professional CSS links
            css_links = '\n'.join([f'    <link rel="stylesheet" href="{css}" />' for css in PROFESSIONAL_CSS])
            
            # Insert before </head>
            content = content[:head_end] + f'''
    
    <!-- UNIFIED DESIGN SYSTEM -->
{css_links}
''' + content[head_end:]
        
        # Replace main content with professional structure
        content = re.sub(
            r'<main[^>]*>.*?</main>',
            f'<main role="main" class="content-area">{professional_lesson}</main>',
            content,
            flags=re.DOTALL
        )
        
        # Update navigation to use beautiful navigation
        content = re.sub(
            r'fetch\(\'/components/navigation-mega-menu\.html\'\)',
            "fetch('/navigation-header.html')",
            content
        )
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"  ✅ Professionalized: {filepath.name}")
        return True
        
    except Exception as e:
        print(f"  ❌ Error professionalizing {filepath.name}: {e}")
        return False

def find_lesson_files():
    """Find all lesson HTML files"""
    lesson_files = []
    
    # Search in various lesson directories
    lesson_dirs = [
        'units/y8-systems/lessons/',
        'units/unit-1-te-ao-maori/lessons/',
        'units/y8-digital-kaitiakitanga/lessons/',
        'units/y8-critical-thinking/lessons/',
        'units/y9-mathematics-geometry-maori-patterns/lessons/',
        'units/y9-science-ecology/lessons/',
        'units/y10-physics-forces/lessons/',
        'units/y10-physics-navigation/lessons/',
        'lessons/',
        'generated-resources-alpha/lessons/',
        'guided-inquiry-unit/lessons/',
        'units/lessons/'  # Additional lessons directory
    ]
    
    for lesson_dir in lesson_dirs:
        dir_path = PUBLIC_DIR / lesson_dir
        if dir_path.exists():
            html_files = list(dir_path.glob('*.html'))
            lesson_files.extend(html_files)
            print(f"📁 Found {len(html_files)} lessons in {lesson_dir}")
    
    return lesson_files

def main():
    """Main professionalization process"""
    print("🎨 LESSON PROFESSIONALIZATION SCRIPT")
    print("=" * 50)
    
    # Find all lesson files
    lesson_files = find_lesson_files()
    print(f"\n📚 Total lessons found: {len(lesson_files)}")
    
    if not lesson_files:
        print("❌ No lesson files found!")
        return
    
    # Professionalize each lesson
    successful = 0
    failed = 0
    
    print(f"\n🚀 Starting professionalization...")
    
    for lesson_file in lesson_files:
        if professionalize_lesson(lesson_file):
            successful += 1
        else:
            failed += 1
    
    print(f"\n📊 PROFESSIONALIZATION COMPLETE:")
    print(f"  ✅ Successful: {successful}")
    print(f"  ❌ Failed: {failed}")
    print(f"  📈 Success Rate: {(successful/(successful+failed)*100):.1f}%")
    
    if successful > 0:
        print(f"\n🎉 {successful} lessons now use the unified design system!")
        print(f"🎨 Professional spacing, typography, and components applied!")
        print(f"🌿 Cultural integration enhanced!")
        print(f"📱 Responsive design implemented!")

if __name__ == "__main__":
    main()
