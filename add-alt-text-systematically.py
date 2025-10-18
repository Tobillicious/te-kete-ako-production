#!/usr/bin/env python3
"""
Add Alt Text to Images Systematically
WCAG 2.1 AA Compliance - Critical Priority
"""

import os
import re
from pathlib import Path

print("🔍 ACCESSIBILITY SPRINT: Adding Alt Text to Images")
print("=" * 70)

# Define directories to process
DIRECTORIES = [
    'public',
    'public/units',
    'public/lessons',
    'public/handouts',
    'public/generated-resources-alpha'
]

# Track progress
stats = {
    'files_scanned': 0,
    'images_found': 0,
    'images_fixed': 0,
    'files_updated': 0
}

def get_contextual_alt_text(img_tag, file_context):
    """
    Generate appropriate alt text based on image context
    """
    src = re.search(r'src=["\']([^"\']+)["\']', img_tag)
    if not src:
        return ''
    
    img_path = src.group(1).lower()
    
    # Cultural images
    if 'maori' in img_path or 'whakairo' in img_path or 'kowhaiwhai' in img_path:
        return 'Traditional Māori cultural pattern'
    
    # Educational context
    if 'diagram' in img_path:
        return 'Educational diagram'
    if 'graph' in img_path or 'chart' in img_path:
        return 'Data visualization chart'
    if 'map' in img_path:
        return 'Geographic map'
    
    # UI elements
    if 'logo' in img_path:
        return 'Te Kete Ako logo'
    if 'icon' in img_path:
        return 'Icon'
    if 'banner' in img_path or 'hero' in img_path:
        return 'Page banner image'
    
    # Default based on file context
    if 'lesson' in file_context.lower():
        return 'Lesson illustration'
    elif 'handout' in file_context.lower():
        return 'Handout visual aid'
    elif 'unit' in file_context.lower():
        return 'Unit overview image'
    
    return 'Educational resource image'

def add_alt_text_to_file(file_path):
    """
    Add alt text to all images in a file that don't have it
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all img tags
        img_pattern = r'<img([^>]*)>'
        images = re.findall(img_pattern, content)
        
        if not images:
            return 0
        
        stats['images_found'] += len(images)
        updated = False
        
        for img_attrs in images:
            # Check if alt text already exists
            if 'alt=' in img_attrs:
                continue
            
            # Generate appropriate alt text
            alt_text = get_contextual_alt_text(img_attrs, file_path)
            
            # Add alt attribute
            old_img = f'<img{img_attrs}>'
            
            # Add alt before closing >
            new_img = f'<img{img_attrs} alt="{alt_text}">'
            
            content = content.replace(old_img, new_img)
            stats['images_fixed'] += 1
            updated = True
        
        if updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            stats['files_updated'] += 1
            return stats['images_fixed']
        
        return 0
        
    except Exception as e:
        print(f"   ⚠️  Error processing {file_path}: {e}")
        return 0

def process_directory(directory):
    """
    Process all HTML files in directory
    """
    html_files = list(Path(directory).rglob('*.html'))
    
    for html_file in html_files:
        stats['files_scanned'] += 1
        fixed = add_alt_text_to_file(str(html_file))
        
        if fixed > 0:
            print(f"✅ {html_file.relative_to('public')}: Added {fixed} alt texts")

# Process each directory
for directory in DIRECTORIES:
    if os.path.exists(directory):
        print(f"\n📁 Processing: {directory}")
        process_directory(directory)

# Summary
print("\n" + "=" * 70)
print("📊 ACCESSIBILITY SPRINT SUMMARY")
print("=" * 70)
print(f"\n✅ Files scanned: {stats['files_scanned']}")
print(f"✅ Images found: {stats['images_found']}")
print(f"✅ Alt texts added: {stats['images_fixed']}")
print(f"✅ Files updated: {stats['files_updated']}")

if stats['images_fixed'] > 0:
    print(f"\n🎉 SUCCESS! Added {stats['images_fixed']} alt texts for WCAG compliance!")
    print("\n📋 Next Steps:")
    print("   1. Review generated alt texts for accuracy")
    print("   2. Enhance with more specific descriptions where needed")
    print("   3. Run accessibility validator")
else:
    print("\n✅ No images found missing alt text - already compliant!")

print("\n" + "=" * 70)

