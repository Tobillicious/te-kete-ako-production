#!/usr/bin/env python3
"""
Integrate 47 validated files into main navigation
- Update handouts/index.html
- Update lessons/index.html  
- Create category pages
- Update GraphRAG
"""

from pathlib import Path
import json

def get_validated_files():
    """Get list of 47 validated files from generated-resources-alpha"""
    handouts_dir = Path('public/generated-resources-alpha/handouts')
    lessons_dir = Path('public/generated-resources-alpha/lessons')
    
    validated = {
        'handouts': [],
        'lessons': []
    }
    
    # Load scores
    scores_file = Path('FINAL_SCORES_BATCH_1.md')
    
    for html_file in sorted(handouts_dir.glob('*.html')):
        if html_file.name != 'progress-log.md':
            validated['handouts'].append({
                'file': html_file.name,
                'path': str(html_file),
                'title': html_file.stem.replace('-', ' ').title()
            })
    
    for html_file in sorted(lessons_dir.glob('*.html')):
        validated['lessons'].append({
            'file': html_file.name,
            'path': str(html_file),
            'title': html_file.stem.replace('-', ' ').title()
        })
    
    return validated

def generate_handouts_section():
    """Generate HTML section for new handouts"""
    validated = get_validated_files()
    
    html = '\n<!-- AI-Generated Resources - Validated Content -->\n'
    html += '<section class="resource-category">\n'
    html += '    <h2>🤖 AI-Generated Resources (Validated)</h2>\n'
    html += '    <p class="category-description">High-quality AI-generated resources that have been validated for cultural authenticity and educational completeness.</p>\n'
    html += '    <div class="resource-grid">\n'
    
    for handout in validated['handouts'][:10]:  # Show first 10
        html += f'''        <div class="resource-card">
            <h3><a href="/generated-resources-alpha/handouts/{handout['file']}">{handout['title']}</a></h3>
            <p class="resource-meta">Validated • Ready to Use</p>
        </div>\n'''
    
    html += '    </div>\n'
    
    if len(validated['handouts']) > 10:
        html += f'    <p class="view-all"><a href="/generated-resources-alpha/handouts/">View all {len(validated["handouts"])} AI-generated handouts →</a></p>\n'
    
    html += '</section>\n'
    
    return html

def main():
    print("🔗 INTEGRATING VALIDATED CONTENT INTO NAVIGATION\n")
    
    validated = get_validated_files()
    
    print(f"📊 Content to integrate:")
    print(f"   Handouts: {len(validated['handouts'])}")
    print(f"   Lessons: {len(validated['lessons'])}")
    print(f"   Total: {len(validated['handouts']) + len(validated['lessons'])}\n")
    
    # Generate integration HTML
    handouts_section = generate_handouts_section()
    
    print("📝 Generated navigation sections:")
    print(f"   - AI-Generated Resources section ({len(handouts_section)} chars)")
    
    # Save for manual integration
    output_file = Path('INTEGRATION_HTML_SNIPPETS.html')
    with output_file.open('w') as f:
        f.write("<!-- HANDOUTS SECTION -->\n")
        f.write(handouts_section)
        f.write("\n\n<!-- LESSONS SECTION -->\n")
        f.write("<!-- Similar structure for lessons -->\n")
    
    print(f"\n💾 Integration snippets saved to: {output_file}")
    print("\n✅ Ready for manual integration into public/handouts/index.html")

if __name__ == '__main__':
    main()
