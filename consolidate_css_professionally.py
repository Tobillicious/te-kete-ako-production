#!/usr/bin/env python3
"""
CSS Consolidation Batch Fix - Professional Implementation
Replaces 5-6 CSS file loads with single te-kete-professional.css
Target: 99 HTML pages tagged "needs_consolidation" in GraphRAG
"""

import re
from pathlib import Path
from typing import List, Tuple
import json

# Target: Single consolidated CSS
TARGET_CSS = '<link rel="stylesheet" href="/css/te-kete-professional.css">'

# CSS files to remove (in order they typically appear)
REMOVE_CSS_PATTERNS = [
    r'<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system\.css">',
    r'<link rel="stylesheet" href="/css/main\.css">',
    r'<link rel="stylesheet" href="/css/professionalization-system\.css">',
    r'<link rel="stylesheet" href="/css/mobile-revolution\.css">',
    r'<link rel="stylesheet" href="/css/print\.css" media="print">',
    r'<link rel="stylesheet" href="/css/tailwind\.css">',
    r'<link rel="stylesheet" href="/css/cascade-fix\.css">',
    r'<link rel="stylesheet" href="/css/professional\.css">',
]

def consolidate_css_in_file(file_path: Path) -> Tuple[bool, str]:
    """
    Replace multiple CSS <link> tags with single consolidated CSS
    Returns: (success, message)
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # Check if already consolidated
        if TARGET_CSS in content and not any(re.search(pattern, content) for pattern in REMOVE_CSS_PATTERNS):
            return (False, "Already consolidated")
        
        # Count how many CSS files we're removing
        removed_count = 0
        for pattern in REMOVE_CSS_PATTERNS:
            matches = re.findall(pattern, content)
            removed_count += len(matches)
            content = re.sub(pattern, '', content)
        
        # Add single consolidated CSS if not present
        if TARGET_CSS not in content:
            # Find <head> tag and insert after it
            head_pattern = r'(<head[^>]*>)'
            if re.search(head_pattern, content):
                content = re.sub(
                    head_pattern,
                    f'\\1\n    {TARGET_CSS}',
                    content,
                    count=1
                )
            else:
                # Fallback: Add before </head>
                content = content.replace('</head>', f'    {TARGET_CSS}\n</head>')
        
        # Only write if changes were made
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return (True, f"Consolidated {removed_count} CSS files → 1")
        else:
            return (False, "No changes needed")
            
    except Exception as e:
        return (False, f"Error: {str(e)}")

def get_files_needing_consolidation() -> List[Path]:
    """
    Find all HTML files in key directories that likely need CSS consolidation
    Focus on: units/, lessons/, handouts/, generated-resources-alpha/
    """
    base_path = Path('/Users/admin/Documents/te-kete-ako-clean/public')
    target_dirs = [
        'units',
        'lessons',
        'handouts',
        'generated-resources-alpha',
        'dist-handouts',
        'integrated-handouts',
        'integrated-lessons',
    ]
    
    files = []
    for dir_name in target_dirs:
        dir_path = base_path / dir_name
        if dir_path.exists():
            files.extend(dir_path.rglob('*.html'))
    
    return files

def main():
    print("🎨 CSS CONSOLIDATION BATCH FIX - PROFESSIONAL EDITION")
    print("=" * 70)
    print()
    
    # Get files
    files = get_files_needing_consolidation()
    total_files = len(files)
    
    print(f"📁 Found {total_files} HTML files to process")
    print()
    
    # Process files
    success_count = 0
    already_done_count = 0
    error_count = 0
    
    for i, file_path in enumerate(files, 1):
        success, message = consolidate_css_in_file(file_path)
        
        if success:
            success_count += 1
            if (i % 10 == 0) or (i == total_files):  # Progress every 10 files
                print(f"✅ Progress: {i}/{total_files} ({success_count} consolidated)")
        elif "Already" in message:
            already_done_count += 1
        else:
            error_count += 1
            if error_count <= 5:  # Only show first 5 errors
                print(f"⚠️  {file_path.relative_to(Path.cwd())}: {message}")
    
    print()
    print("=" * 70)
    print("📊 FINAL RESULTS")
    print("=" * 70)
    print(f"✅ Consolidated: {success_count} files")
    print(f"✓  Already done: {already_done_count} files")
    print(f"⚠️  Errors: {error_count} files")
    print(f"📁 Total processed: {total_files} files")
    print()
    
    if success_count > 0:
        print("🎉 CSS CONSOLIDATION COMPLETE!")
        print(f"   Performance gain: {success_count * 4} fewer HTTP requests!")
        print(f"   (avg 5 CSS files → 1 per page)")
    
    return success_count

if __name__ == "__main__":
    main()

