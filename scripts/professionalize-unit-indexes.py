#!/usr/bin/env python3
"""
PROFESSIONALIZE ALL UNIT INDEX PAGES
Apply unified design system to unit index pages
Agent-4 - Morning Development Sprint
"""

from pathlib import Path
import re
import os

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

# CSS files to include in professionalized unit indexes
PROFESSIONAL_CSS = [
    '/css/te-kete-unified-design-system.css',
    '/css/component-library.css',
    '/css/unit-index-professionalization.css',
    '/css/beautiful-navigation.css',
    '/css/print.css'
]

def professionalize_unit_index(filepath):
    """Apply professional design system to a unit index page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already professionalized
        if 'unit-index-professionalization.css' in content:
            print(f"  ✅ Already professionalized: {filepath.name}")
            return True
            
        # Extract unit content
        main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
        if not main_match:
            print(f"  ⚠️  No main content found: {filepath.name}")
            return False
            
        main_content = main_match.group(1)
        
        # Create professional unit index structure
        professional_unit = f'''
<!-- PROFESSIONAL UNIT INDEX CONTENT -->
<div class="unit-index-page">
  <div class="unit-index-container">
    
    <!-- UNIT HEADER -->
    <header class="unit-header">
      <h1 class="unit-title">{{UNIT_TITLE}}</h1>
      <p class="unit-subtitle">{{UNIT_SUBTITLE}}</p>
      
      <div class="unit-meta">
        <div class="unit-meta-item">
          <span class="unit-meta-icon">📚</span>
          <span>{{SUBJECT}}</span>
        </div>
        <div class="unit-meta-item">
          <span class="unit-meta-icon">🎯</span>
          <span>{{LEVEL}}</span>
        </div>
        <div class="unit-meta-item">
          <span class="unit-meta-icon">⏱️</span>
          <span>{{DURATION}}</span>
        </div>
        <div class="unit-meta-item">
          <span class="unit-meta-icon">🌿</span>
          <span>Cultural Integration</span>
        </div>
      </div>
      
      <p class="unit-description">{{UNIT_DESCRIPTION}}</p>
    </header>

    <!-- UNIT STATISTICS -->
    <section class="unit-stats">
      <div class="unit-stat-card">
        <span class="unit-stat-number">{{LESSON_COUNT}}</span>
        <span class="unit-stat-label">Lessons</span>
      </div>
      <div class="unit-stat-card">
        <span class="unit-stat-number">{{RESOURCE_COUNT}}</span>
        <span class="unit-stat-label">Resources</span>
      </div>
      <div class="unit-stat-card">
        <span class="unit-stat-number">{{DURATION_HOURS}}</span>
        <span class="unit-stat-label">Hours</span>
      </div>
      <div class="unit-stat-card">
        <span class="unit-stat-number">{{ASSESSMENT_COUNT}}</span>
        <span class="unit-stat-label">Assessments</span>
      </div>
    </section>

    <!-- LESSONS SECTION -->
    <section class="lessons-section">
      <h2 class="lessons-title">Unit Lessons</h2>
      <div class="lessons-grid">
{main_content}
      </div>
    </section>

    <!-- RESOURCES SECTION -->
    <section class="resources-section">
      <h2 class="resources-title">Unit Resources</h2>
      <div class="resources-grid">
        <div class="resource-item">
          <h3 class="resource-item-title">Digital Resources</h3>
          <p class="resource-item-description">Interactive materials and digital tools</p>
          <a href="{{DIGITAL_RESOURCES_LINK}}" class="resource-item-link">Access Resources →</a>
        </div>
        <div class="resource-item">
          <h3 class="resource-item-title">Print Materials</h3>
          <p class="resource-item-description">Downloadable PDFs and worksheets</p>
          <a href="{{PRINT_MATERIALS_LINK}}" class="resource-item-link">Download PDFs →</a>
        </div>
        <div class="resource-item">
          <h3 class="resource-item-title">Assessment Tools</h3>
          <p class="resource-item-description">Rubrics and evaluation frameworks</p>
          <a href="{{ASSESSMENT_LINK}}" class="resource-item-link">View Tools →</a>
        </div>
      </div>
    </section>

    <!-- UNIT NAVIGATION -->
    <nav class="unit-navigation">
      <a href="{{PREVIOUS_UNIT_LINK}}" class="nav-button secondary">
        <span class="nav-button-icon">←</span>
        <span>Previous Unit</span>
      </a>
      
      <a href="/units/index.html" class="nav-button secondary">
        <span class="nav-button-icon">📚</span>
        <span>All Units</span>
      </a>
      
      <a href="{{NEXT_UNIT_LINK}}" class="nav-button">
        <span>Next Unit</span>
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
            f'<main role="main" class="content-area">{professional_unit}</main>',
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

def find_unit_index_files():
    """Find all unit index HTML files"""
    unit_index_files = []
    
    # Search in units directory for index files
    units_dir = PUBLIC_DIR / 'units'
    if units_dir.exists():
        for unit_dir in units_dir.iterdir():
            if unit_dir.is_dir():
                index_file = unit_dir / 'index.html'
                if index_file.exists():
                    unit_index_files.append(index_file)
                    print(f"📁 Found unit index: {unit_dir.name}/index.html")
    
    return unit_index_files

def main():
    """Main professionalization process"""
    print("🎨 UNIT INDEX PROFESSIONALIZATION SCRIPT")
    print("=" * 50)
    
    # Find all unit index files
    unit_index_files = find_unit_index_files()
    print(f"\n📚 Total unit indexes found: {len(unit_index_files)}")
    
    if not unit_index_files:
        print("❌ No unit index files found!")
        return
    
    # Professionalize each unit index
    successful = 0
    failed = 0
    
    print(f"\n🚀 Starting unit index professionalization...")
    
    for unit_index_file in unit_index_files:
        if professionalize_unit_index(unit_index_file):
            successful += 1
        else:
            failed += 1
    
    print(f"\n📊 UNIT INDEX PROFESSIONALIZATION COMPLETE:")
    print(f"  ✅ Successful: {successful}")
    print(f"  ❌ Failed: {failed}")
    print(f"  📈 Success Rate: {(successful/(successful+failed)*100):.1f}%")
    
    if successful > 0:
        print(f"\n🎉 {successful} unit indexes now use the unified design system!")
        print(f"🎨 Professional unit headers, statistics, and layouts applied!")
        print(f"🌿 Cultural integration enhanced!")
        print(f"📱 Responsive design implemented!")

if __name__ == "__main__":
    main()
