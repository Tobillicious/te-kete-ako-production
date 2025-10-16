#!/usr/bin/env python3
"""
Simple CSS Minification
Remove comments, whitespace, and optimize CSS
"""
import re
from pathlib import Path
import shutil

def minify_css(css_content):
    """Minify CSS by removing comments and excess whitespace"""
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    
    # Remove newlines and extra spaces
    css = re.sub(r'\s+', ' ', css)
    
    # Remove spaces around special characters
    css = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css)
    
    # Remove trailing semicolons before }
    css = re.sub(r';\s*}', '}', css)
    
    # Remove leading/trailing whitespace
    css = css.strip()
    
    return css

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

CANONICAL_CSS = [
    'css/te-kete-unified-design-system.css',
    'css/component-library.css',
    'css/animations-professional.css',
    'css/beautiful-navigation.css',
    'css/lesson-professionalization.css',
    'css/unit-index-professionalization.css',
    'css/mobile-optimization.css',
    'css/print.css'
]

print("⚡ CSS MINIFICATION - SIMPLE APPROACH")
print("=" * 60)

# Create backup
backup_dir = Path('/Users/admin/Documents/te-kete-ako-clean/backup_before_minification')
if not backup_dir.exists():
    print("\n💾 Creating backup...")
    backup_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(PUBLIC_DIR / 'css', backup_dir / 'css', dirs_exist_ok=True)
    print("✅ Backup created")

# Create minified directory
min_dir = PUBLIC_DIR / 'css' / 'min'
min_dir.mkdir(exist_ok=True)
print(f"\n📁 Minified directory: {min_dir}")

print("\n🔧 Minifying CSS files...")
total_original = 0
total_minified = 0

for css_file in CANONICAL_CSS:
    css_path = PUBLIC_DIR / css_file
    
    if not css_path.exists():
        print(f"⚠️  {css_file}: NOT FOUND")
        continue
    
    # Read original
    with open(css_path, 'r', encoding='utf-8') as f:
        original_css = f.read()
    
    original_size = len(original_css.encode('utf-8'))
    total_original += original_size
    
    # Minify
    minified_css = minify_css(original_css)
    minified_size = len(minified_css.encode('utf-8'))
    total_minified += minified_size
    
    reduction = ((original_size - minified_size) / original_size * 100) if original_size > 0 else 0
    
    # Write minified version
    filename = css_path.stem
    minified_path = min_dir / f"{filename}.min.css"
    with open(minified_path, 'w', encoding='utf-8') as f:
        f.write(minified_css)
    
    print(f"✅ {css_file.split('/')[-1]:50} {original_size:>8} → {minified_size:>8} bytes ({reduction:>5.1f}% reduction)")

print(f"\n📊 MINIFICATION RESULTS:")
print(f"  Original total: {total_original:>10} bytes ({total_original/1024:.1f} KB)")
print(f"  Minified total: {total_minified:>10} bytes ({total_minified/1024:.1f} KB)")
total_reduction = ((total_original - total_minified) / total_original * 100) if total_original > 0 else 0
print(f"  Total reduction: {total_reduction:.1f}%")
print(f"  Savings: {(total_original - total_minified):>10} bytes ({(total_original - total_minified)/1024:.1f} KB)")

print("\n✅ MINIFICATION COMPLETE!")

