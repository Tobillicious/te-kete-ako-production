#!/usr/bin/env python3
"""
Fix nested HTML structure issues in flagged files
"""

from pathlib import Path
import re

def fix_nested_html(file_path):
    """Remove nested HTML/head/body tags, keep only outermost structure"""
    content = file_path.read_text(encoding='utf-8')
    
    # Find first occurrence of key tags
    first_doctype = content.find('<!DOCTYPE html>')
    first_html = content.find('<html')
    first_head = content.find('<head>')
    first_body = content.find('<body>')
    
    # Find last closing tags
    last_body_close = content.rfind('</body>')
    last_html_close = content.rfind('</html>')
    
    if first_doctype == -1 or first_html == -1:
        return content, False
    
    # Extract everything between first opening and last closing
    # Remove any duplicate structures in between
    lines = content.split('\n')
    cleaned_lines = []
    in_nested = False
    doctype_count = 0
    html_count = 0
    head_count = 0
    body_count = 0
    
    for line in lines:
        # Count occurrences
        if '<!DOCTYPE html>' in line:
            doctype_count += 1
            if doctype_count > 1:
                continue  # Skip duplicate DOCTYPE
        
        if '<html' in line and not '</html>' in line:
            html_count += 1
            if html_count > 1:
                continue  # Skip nested html opening
        
        if '<head>' in line:
            head_count += 1
            if head_count > 1:
                in_nested = True
                continue
        
        if '</head>' in line and in_nested:
            in_nested = False
            continue
        
        if '<body>' in line:
            body_count += 1
            if body_count > 1:
                continue
        
        if not in_nested:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines), True

# Files flagged for manual review
flagged_files = [
    'public/generated-resources-alpha/handouts/cultural-safety-checklists-for-classroom-discussions.html',
    'public/generated-resources-alpha/handouts/financial-literacy-with-māori-economic-principles.html',
    'public/generated-resources-alpha/handouts/ncea-level-1-literacy-and-numeracy-must-knows.html',
    'public/generated-resources-alpha/handouts/te-reo-maths-glossary-key-terms-in-māori-and-english.html',
    'public/generated-resources-alpha/handouts/year-9-starter-pack-essential-skills-for-high-school-success.html',
    'public/generated-resources-alpha/lessons/climate-change-through-te-taiao-māori-lens.html',
    'public/generated-resources-alpha/lessons/traditional-navigation-and-modern-gps-integration.html',
]

print("🔧 FIXING NESTED HTML STRUCTURES\n")

for file_path_str in flagged_files:
    file_path = Path(file_path_str)
    if not file_path.exists():
        print(f"   ⚠️  Not found: {file_path.name}")
        continue
    
    fixed_content, was_fixed = fix_nested_html(file_path)
    
    if was_fixed:
        file_path.write_text(fixed_content, encoding='utf-8')
        print(f"   ✅ Fixed: {file_path.name}")
    else:
        print(f"   ⚠️  Could not auto-fix: {file_path.name}")

print("\n✅ Manual review fixes complete!")
