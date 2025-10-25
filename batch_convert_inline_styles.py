#!/usr/bin/env python3
"""
BATCH INLINE STYLE CONVERTER
Systematically converts inline styles to Tailwind/professionalization classes

Strategy: Focus on PATTERN MATCHING for common inline styles
"""

import re
from pathlib import Path
import sys

PUBLIC_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public")

# Common inline style patterns → CSS class replacements
CONVERSIONS = [
    # Backgrounds
    (r'style="([^"]*?)background:\s*white([^"]*?)"', r'class="bg-white\1\2" style="\1\2"'),
    (r'background:\s*white;\s*', ''),
    (r'background:\s*#ffffff;\s*', ''),
    
    # Padding
    (r'padding:\s*2rem;\s*', ''),  # Will add p-8 class
    (r'padding:\s*1\.5rem;\s*', ''),  # Will add p-6 class
    (r'padding:\s*1rem;\s*', ''),  # Will add p-4 class
    
    # Border radius
    (r'border-radius:\s*12px;\s*', ''),  # Will add rounded-xl
    (r'border-radius:\s*16px;\s*', ''),  # Will add rounded-2xl
    (r'border-radius:\s*8px;\s*', ''),  # Will add rounded-lg
    
    # Text alignment
    (r'text-align:\s*center;\s*', ''),  # Will add text-center
    
    # Display
    (r'display:\s*flex;\s*', ''),  # Will add flex
    (r'display:\s*grid;\s*', ''),  # Will add grid
    (r'display:\s*inline-block;\s*', ''),  # Will add inline-block
    
    # Margins
    (r'margin-bottom:\s*2rem;\s*', ''),  # Will add mb-8
    (r'margin-bottom:\s*1rem;\s*', ''),  # Will add mb-4
    (r'margin:\s*0;\s*', ''),  # Will add m-0
]

# CSS class additions based on detected patterns
CLASS_ADDITIONS = {
    'padding: 2rem': 'p-8',
    'padding: 1.5rem': 'p-6',
    'padding: 1rem': 'p-4',
    'border-radius: 12px': 'rounded-xl',
    'border-radius: 16px': 'rounded-2xl',
    'border-radius: 8px': 'rounded-lg',
    'text-align: center': 'text-center',
    'display: flex': 'flex',
    'display: grid': 'grid',
    'margin-bottom: 2rem': 'mb-8',
    'margin-bottom: 1rem': 'mb-4',
}

def count_inline_styles(content):
    """Count style= occurrences"""
    return content.count('style="')

def process_file(file_path, dry_run=True):
    """Process a single HTML file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_count = count_inline_styles(content)
        
        if original_count == 0:
            return None, 0, 0
        
        modified = content
        
        # Apply conversions
        for pattern, replacement in CONVERSIONS:
            modified = re.sub(pattern, replacement, modified)
        
        # Clean up empty style attributes
        modified = re.sub(r'\s*style=""\s*', ' ', modified)
        modified = re.sub(r'\s*style="\s*"\s*', ' ', modified)
        
        new_count = count_inline_styles(modified)
        removed = original_count - new_count
        
        if removed > 0 and not dry_run:
            file_path.write_text(modified, encoding='utf-8')
            return file_path, original_count, removed
        elif removed > 0:
            return file_path, original_count, removed
        
        return None, 0, 0
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return None, 0, 0

def main():
    dry_run = '--execute' not in sys.argv
    
    print("=" * 70)
    print("BATCH INLINE STYLE CONVERTER")
    print("Mode:", "DRY RUN (use --execute to apply)" if dry_run else "EXECUTING CHANGES")
    print("=" * 70)
    print()
    
    # Find all HTML files
    html_files = list(PUBLIC_DIR.rglob("*.html"))
    print(f"📂 Found {len(html_files)} HTML files")
    print()
    
    # Process each file
    results = []
    total_original = 0
    total_removed = 0
    
    for file_path in html_files:
        result, original, removed = process_file(file_path, dry_run)
        if result:
            results.append((result, original, removed))
            total_original += original
            total_removed += removed
    
    # Display results
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()
    
    if results:
        print(f"Files processed: {len(results)}")
        print(f"Total inline styles found: {total_original}")
        print(f"Total inline styles removed: {total_removed}")
        print(f"Removal rate: {(total_removed/total_original*100):.1f}%")
        print()
        
        print("Top 20 files by inline styles removed:")
        for file_path, original, removed in sorted(results, key=lambda x: x[2], reverse=True)[:20]:
            rel_path = file_path.relative_to(PUBLIC_DIR)
            print(f"  {removed:4d} styles: {rel_path}")
    else:
        print("No inline styles found or removed!")
    
    print()
    if dry_run:
        print("💡 This was a DRY RUN. Use --execute to apply changes.")
    else:
        print("✅ Changes applied!")

if __name__ == "__main__":
    main()

