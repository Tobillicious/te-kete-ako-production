#!/usr/bin/env python3
"""
CONVERT QUALITY NUMBERS TO STAR BADGES
Replace technical numbers (96/100, Q94, etc) with human-friendly star ratings
"""

from pathlib import Path
import re

def quality_to_stars(quality_num):
    """Convert quality number (0-100) to star rating"""
    if quality_num >= 95:
        return "🌟🌟🌟🌟🌟 Excellence"
    elif quality_num >= 90:
        return "🌟🌟🌟🌟 High Quality"
    elif quality_num >= 80:
        return "🌟🌟🌟 Good"
    elif quality_num >= 70:
        return "🌟🌟 Fair"
    else:
        return "🌟 Developing"

def convert_quality_badges(content):
    """Convert quality number patterns to star badges"""
    # Pattern 1: "Quality: 96/100" or "Q96" or "96/100"
    def replace_quality(match):
        num_str = match.group(1)
        num = int(num_str)
        stars = quality_to_stars(num)
        return stars
    
    # Replace various quality patterns
    content = re.sub(r'Quality:\s*(\d{2,3})/100', replace_quality, content, flags=re.IGNORECASE)
    content = re.sub(r'Q(\d{2,3})\b', replace_quality, content)
    content = re.sub(r'(\d{2,3})/100(?:\s*quality)?', replace_quality, content, flags=re.IGNORECASE)
    
    # Replace quality badge divs
    content = re.sub(
        r'<div class="quality-badge[^"]*">.*?(\d{2,3})/100.*?</div>',
        lambda m: f'<div class="quality-badge">{quality_to_stars(int(m.group(1)))}</div>',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Replace quality spans
    content = re.sub(
        r'<span class="quality[^"]*">.*?(\d{2,3})/100.*?</span>',
        lambda m: f'<span class="quality-badge">{quality_to_stars(int(m.group(1)))}</span>',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    return content

# Convert across all HTML files
html_files = list(Path('public').rglob('*.html'))
converted = 0

print("🌟 CONVERTING QUALITY NUMBERS TO STAR BADGES")
print("=" * 60)

for html_path in html_files:
    try:
        content = html_path.read_text(encoding='utf-8', errors='ignore')
        original = content
        
        new_content = convert_quality_badges(content)
        
        if new_content != original:
            html_path.write_text(new_content, encoding='utf-8')
            converted += 1
            
            if converted <= 10:  # Show first 10
                print(f"  ✓ {html_path.relative_to('public')}")
                
    except Exception as e:
        pass  # Skip files with issues

print(f"\n✅ Converted {converted} HTML files")
print("🎊 Quality badges now human-friendly!")
print("")
print("Examples:")
print("  96/100 → 🌟🌟🌟🌟🌟 Excellence")
print("  92/100 → 🌟🌟🌟🌟 High Quality")
print("  85/100 → 🌟🌟🌟 Good")

