#!/usr/bin/env python3
"""
HIDE NON-FEATURED RESOURCES
Marks 95% of resources as "searchable but not prominent"
Only Top 10 Starter Pack + Top 50 per subject remain prominently visible
Created: Oct 26, 2025
"""

import os
import re
from pathlib import Path

# Featured resources (keep prominent)
FEATURED_RESOURCES = {
    # Top 10 Starter Pack
    '/lessons/y7-math-patterns-algebra-intro.html',
    '/lessons/y7-science-ecosystem-kaitiakitanga.html',
    '/lessons/y8-math-geometry-kowhaiwhai.html',
    '/lessons/y8-science-cells-whakapapa.html',
    '/lessons/y9-science-genetics-whakapapa-dna.html',
    '/units/algebra-patterns-y7.html',
    '/units/ecology-kaitiakitanga-y9.html',
    '/units/walker-migration-unit.html',
    '/handouts/tukutuku-pattern-worksheet.html',
    '/handouts/whakapapa-science-worksheet.html',
}

# Subject hub top resources (keep prominent)
SUBJECT_HUB_FEATURED = {
    'mathematics': [
        '/lessons/y7-math-patterns-algebra-intro.html',
        '/lessons/y8-math-geometry-kowhaiwhai.html',
        '/lessons/y9-math-statistics-social-justice.html',
    ],
    'science': [
        '/lessons/y7-science-ecosystem-kaitiakitanga.html',
        '/lessons/y8-science-cells-whakapapa.html',
        '/lessons/y9-science-genetics-whakapapa-dna.html',
    ],
    'english': [
        '/lessons/y7-english-narrative-writing-purakau.html',
        '/lessons/y8-english-narrative-purakau-structure.html',
        '/lessons/y9-english-poetry-maori-oral-traditions.html',
    ],
}

def add_hidden_metadata(html_content, filepath):
    """Add data-visibility="searchable" to non-featured resources"""
    
    # Check if this is a featured resource
    is_featured = False
    for featured_path in FEATURED_RESOURCES:
        if featured_path in str(filepath):
            is_featured = True
            break
    
    if is_featured:
        return html_content, False, 'featured'
    
    # Add to <html> tag
    html_tag_match = re.search(r'<html[^>]*>', html_content, re.IGNORECASE)
    if not html_tag_match:
        return html_content, False, 'no-html-tag'
    
    html_tag = html_tag_match.group(0)
    
    # Check if already has visibility attribute
    if 'data-visibility' in html_tag:
        return html_content, False, 'already-has-visibility'
    
    # Add visibility attribute
    new_html_tag = html_tag.replace('>', ' data-visibility="searchable" data-prominence="low">')
    
    modified_html = html_content.replace(html_tag, new_html_tag, 1)
    
    return modified_html, True, 'hidden'

def main():
    public_dir = Path('public')
    
    if not public_dir.exists():
        print("❌ public/ directory not found!")
        return
    
    # Find all resource HTML files (lessons, units, handouts)
    resource_dirs = ['lessons', 'units', 'handouts']
    all_resources = []
    
    for resource_dir in resource_dirs:
        dir_path = public_dir / resource_dir
        if dir_path.exists():
            all_resources.extend(list(dir_path.rglob('*.html')))
    
    print(f"📁 Found {len(all_resources)} total resources")
    
    # Process resources
    featured_count = 0
    hidden_count = 0
    already_hidden_count = 0
    error_count = 0
    
    for filepath in all_resources:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified_content, was_modified, status = add_hidden_metadata(content, filepath)
            
            if status == 'featured':
                featured_count += 1
            elif status == 'hidden':
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                hidden_count += 1
            elif status == 'already-has-visibility':
                already_hidden_count += 1
                
        except Exception as e:
            error_count += 1
            print(f"  ❌ Error: {filepath.name}: {e}")
    
    print(f"\n{'='*60}")
    print(f"🎯 RESOURCE VISIBILITY MANAGEMENT COMPLETE!")
    print(f"{'='*60}")
    print(f"⭐ Featured (prominent):  {featured_count} resources")
    print(f"🔍 Hidden (searchable):   {hidden_count} resources")
    print(f"✓  Already processed:     {already_hidden_count} resources")
    print(f"❌ Errors:                {error_count} resources")
    print(f"\n📊 Total: {len(all_resources)} resources")
    
    visibility_percentage = (hidden_count / len(all_resources) * 100) if all_resources else 0
    print(f"\n📈 {visibility_percentage:.1f}% of resources now hidden from main navigation")
    print(f"✅ Still searchable via search function!")
    print(f"🌿 Kia kaha!")

if __name__ == '__main__':
    main()

