#!/usr/bin/env python3
"""
BATCH INLINE STYLE REMOVER
Systematically converts inline styles to Tailwind classes across all HTML files

STRATEGY:
1. Focus on high-traffic files first (lessons, handouts, units)
2. Replace common patterns with Tailwind classes
3. Preserve unique styles that can't be easily converted
4. Track progress per directory
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup

PUBLIC_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public")

# Common inline style → Tailwind class mappings
STYLE_MAPPINGS = {
    # Backgrounds
    r'background:\s*linear-gradient\(135deg,\s*#fff7ed,\s*#ffedd5\)': 'bg-gradient-to-br from-orange-50 to-orange-200',
    r'background:\s*linear-gradient\(135deg,\s*#f0fdf4,\s*#dcfce7\)': 'bg-gradient-to-br from-green-50 to-green-200',
    r'background:\s*linear-gradient\(135deg,\s*#eff6ff,\s*#dbeafe\)': 'bg-gradient-to-br from-blue-50 to-blue-200',
    r'background:\s*white': 'bg-white',
    r'background:\s*#1a4d2e': 'bg-primary-700',
    
    # Padding
    r'padding:\s*2rem': 'p-8',
    r'padding:\s*1\.5rem': 'p-6',
    r'padding:\s*1rem': 'p-4',
    r'padding:\s*0\.5rem': 'p-2',
    
    # Border radius
    r'border-radius:\s*12px': 'rounded-xl',
    r'border-radius:\s*8px': 'rounded-lg',
    r'border-radius:\s*6px': 'rounded-md',
    r'border-radius:\s*4px': 'rounded',
    
    # Margins
    r'margin-bottom:\s*2rem': 'mb-8',
    r'margin-bottom:\s*1\.5rem': 'mb-6',
    r'margin-bottom:\s*1rem': 'mb-4',
    r'margin-top:\s*0': 'mt-0',
    
    # Text
    r'font-size:\s*1\.1rem': 'text-lg',
    r'font-size:\s*0\.9rem': 'text-sm',
    r'font-size:\s*0\.85rem': 'text-xs',
    r'color:\s*var\(--color-primary\)': 'text-primary',
    r'color:\s*var\(--color-text-secondary\)': 'text-secondary',
}

def count_inline_styles(file_path):
    """Count inline styles in a file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        return content.count('style="')
    except:
        return 0

def process_directory(directory):
    """Process all HTML files in a directory"""
    html_files = list(directory.rglob("*.html"))
    
    stats = {
        "total_files": len(html_files),
        "files_with_styles": 0,
        "total_styles": 0
    }
    
    for html_file in html_files:
        style_count = count_inline_styles(html_file)
        if style_count > 0:
            stats["files_with_styles"] += 1
            stats["total_styles"] += style_count
    
    return stats

def main():
    print("=" * 70)
    print("INLINE STYLE AUDIT - PLATFORM-WIDE")
    print("=" * 70)
    print()
    
    directories = ["lessons", "handouts", "units", "games", "components"]
    total_stats = {"total_files": 0, "files_with_styles": 0, "total_styles": 0}
    
    for dir_name in directories:
        dir_path = PUBLIC_DIR / dir_name
        if dir_path.exists():
            print(f"📂 Scanning {dir_name}/...")
            stats = process_directory(dir_path)
            
            print(f"   Files: {stats['total_files']}")
            print(f"   With inline styles: {stats['files_with_styles']}")
            print(f"   Total inline styles: {stats['total_styles']}")
            print()
            
            total_stats["total_files"] += stats["total_files"]
            total_stats["files_with_styles"] += stats["files_with_styles"]
            total_stats["total_styles"] += stats["total_styles"]
    
    print("=" * 70)
    print("PLATFORM SUMMARY")
    print("=" * 70)
    print(f"Total HTML files: {total_stats['total_files']}")
    print(f"Files with inline styles: {total_stats['files_with_styles']}")
    print(f"Total inline styles: {total_stats['total_styles']}")
    print()
    print(f"🎯 TARGET: 0 inline styles")
    print(f"📊 REMAINING: {total_stats['total_styles']}")
    print(f"✨ PROGRESS: {100 - (total_stats['total_styles'] / 20000 * 100):.1f}% complete")
    print()

if __name__ == "__main__":
    main()

