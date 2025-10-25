#!/usr/bin/env python3
"""
SYSTEMATIC INLINE STYLE CONVERTER
Target: 94,673 inline styles → 0
Approach: Automated pattern matching + batch conversion

PRIORITY ORDER:
1. lessons/ (160 files, 15,263 styles) - HIGH TRAFFIC
2. games/ (11 files, 417 styles) - QUICK WIN  
3. components/ (49 files, 973 styles) - REUSABLE
4. units/ (423 files, 32,191 styles) - LARGE BUT IMPORTANT
5. handouts/ (378 files, 45,829 styles) - LARGEST

STRATEGY: Process files in batches of 10, commit after each batch
"""

import re
from pathlib import Path
import sys

PUBLIC_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public")

# Comprehensive style → Tailwind mappings
STYLE_PATTERNS = {
    # Background gradients
    (r'style="background:\s*linear-gradient\(135deg,\s*#fff7ed,\s*#ffedd5\);?([^"]*)"', 'class="bg-gradient-to-br from-orange-50 to-orange-200$1"'),
    (r'style="background:\s*linear-gradient\(135deg,\s*#f0fdf4,\s*#dcfce7\);?([^"]*)"', 'class="bg-gradient-to-br from-green-50 to-green-200$1"'),
    (r'style="background:\s*linear-gradient\(135deg,\s*#eff6ff,\s*#dbeafe\);?([^"]*)"', 'class="bg-gradient-to-br from-blue-50 to-blue-200$1"'),
    (r'style="background:\s*linear-gradient\(135deg,\s*#fef3c7,\s*#fde68a\);?([^"]*)"', 'class="bg-gradient-to-br from-amber-100 to-amber-300$1"'),
    (r'style="background:\s*white;?([^"]*)"', 'class="bg-white$1"'),
    (r'style="background:\s*rgba\(255,\s*255,\s*255,\s*0\.1\);?([^"]*)"', 'class="bg-white/10$1"'),
    
    # Padding
    (r'padding:\s*3rem;?', 'p-12 '),
    (r'padding:\s*2\.5rem;?', 'p-10 '),
    (r'padding:\s*2rem;?', 'p-8 '),
    (r'padding:\s*1\.5rem;?', 'p-6 '),
    (r'padding:\s*1rem;?', 'p-4 '),
    (r'padding:\s*0\.5rem\s+1rem;?', 'px-4 py-2 '),
    
    # Border radius
    (r'border-radius:\s*20px;?', 'rounded-full '),
    (r'border-radius:\s*16px;?', 'rounded-2xl '),
    (r'border-radius:\s*12px;?', 'rounded-xl '),
    (r'border-radius:\s*8px;?', 'rounded-lg '),
    
    # Margins
    (r'margin-bottom:\s*2rem;?', 'mb-8 '),
    (r'margin-bottom:\s*1\.5rem;?', 'mb-6 '),
    (r'margin-bottom:\s*1rem;?', 'mb-4 '),
    (r'margin-bottom:\s*0\.5rem;?', 'mb-2 '),
    (r'margin:\s*0;?', 'm-0 '),
    
    # Text styling
    (r'font-size:\s*2\.5rem;?', 'text-4xl '),
    (r'font-size:\s*1\.8rem;?', 'text-3xl '),
    (r'font-size:\s*1\.5rem;?', 'text-2xl '),
    (r'font-size:\s*1\.4rem;?', 'text-xl '),
    (r'font-size:\s*1\.2rem;?', 'text-lg '),
    (r'font-size:\s*1rem;?', 'text-base '),
    (r'font-size:\s*0\.9rem;?', 'text-sm '),
    (r'font-weight:\s*700;?', 'font-bold '),
    (r'font-weight:\s*600;?', 'font-semibold '),
    (r'color:\s*white;?', 'text-white '),
    
    # Display
    (r'display:\s*flex;?', 'flex '),
    (r'display:\s*grid;?', 'grid '),
    (r'text-align:\s*center;?', 'text-center '),
}

def convert_file(file_path):
    """Convert inline styles in a single file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_count = content.count('style="')
        
        # Apply all pattern replacements
        for pattern, replacement in STYLE_PATTERNS:
            content = re.sub(pattern, replacement, content)
        
        # Clean up empty style attributes
        content = re.sub(r'style=""', '', content)
        
        final_count = content.count('style="')
        
        if final_count < original_count:
            file_path.write_text(content, encoding='utf-8')
            return original_count - final_count
        
        return 0
    except Exception as e:
        print(f"  ⚠️ Error processing {file_path.name}: {e}")
        return 0

def process_directory(directory, batch_size=10):
    """Process a directory in batches"""
    html_files = sorted(directory.rglob("*.html"))
    
    print(f"\n📂 Processing {directory.name}/ ({len(html_files)} files)")
    print("=" * 70)
    
    total_converted = 0
    files_processed = 0
    
    for i, file_path in enumerate(html_files):
        if i > 0 and i % batch_size == 0:
            print(f"\n  ✅ Batch {i//batch_size} complete ({batch_size} files)")
            print(f"     Styles converted so far: {total_converted}")
        
        converted = convert_file(file_path)
        if converted > 0:
            files_processed += 1
            total_converted += converted
            if i % batch_size == 0:
                print(f"\n  📝 {file_path.relative_to(PUBLIC_DIR)}")
                print(f"     Converted: {converted} styles")
    
    print(f"\n  ✅ {directory.name}/ COMPLETE")
    print(f"     Files processed: {files_processed}/{len(html_files)}")
    print(f"     Total styles converted: {total_converted}")
    
    return total_converted

def main():
    print("=" * 70)
    print("SYSTEMATIC INLINE STYLE CONVERTER")
    print("Target: 94,673 styles → 0")
    print("=" * 70)
    
    grand_total = 0
    
    # Priority order
    directories = [
        ("lessons", PUBLIC_DIR / "lessons"),
        ("games", PUBLIC_DIR / "games"),
        ("components", PUBLIC_DIR / "components"),
    ]
    
    for name, dir_path in directories:
        if dir_path.exists():
            converted = process_directory(dir_path)
            grand_total += converted
    
    print("\n" + "=" * 70)
    print("SESSION SUMMARY")
    print("=" * 70)
    print(f"Total styles converted: {grand_total}")
    print(f"Remaining estimate: {94673 - grand_total}")
    print()
    print("NEXT: Continue with units/ and handouts/ directories")
    print("=" * 70)

if __name__ == "__main__":
    main()

