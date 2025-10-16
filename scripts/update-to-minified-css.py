#!/usr/bin/env python3
"""
Update all HTML files to use minified CSS with cache hashing
"""
import re
import hashlib
from pathlib import Path

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')
MIN_DIR = PUBLIC_DIR / 'css' / 'min'

# Generate hashes for cache busting
def generate_hash(filepath):
    """Generate short hash for cache busting"""
    with open(filepath, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()[:8]
    return file_hash

# Generate hash manifest
print("⚡ GENERATING CSS HASH MANIFEST")
print("=" * 60)

css_hashes = {}
for css_file in MIN_DIR.glob('*.min.css'):
    filename = css_file.name
    file_hash = generate_hash(css_file)
    css_hashes[filename] = file_hash
    print(f"  {filename:55} hash: {file_hash}")

print(f"\n✅ Generated hashes for {len(css_hashes)} CSS files")

# Update HTML files
print(f"\n🔧 UPDATING HTML FILES...")

html_files = list(PUBLIC_DIR.glob('**/*.html'))
print(f"  Found {len(html_files)} HTML files")

updated_count = 0
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace canonical CSS links with minified versions + hash
        replacements = {
            'te-kete-unified-design-system.css': 'te-kete-unified-design-system.min.css',
            'component-library.css': 'component-library.min.css',
            'animations-professional.css': 'animations-professional.min.css',
            'beautiful-navigation.css': 'beautiful-navigation.min.css',
            'lesson-professionalization.css': 'lesson-professionalization.min.css',
            'unit-index-professionalization.css': 'unit-index-professionalization.min.css',
            'mobile-optimization.css': 'mobile-optimization.min.css',
            'print.css': 'print.min.css'
        }
        
        for original, minified in replacements.items():
            if minified in css_hashes:
                file_hash = css_hashes[minified]
                # Update href="/css/original.css" to href="/css/min/minified.css?v=hash"
                pattern = rf'href="(/css/){re.escape(original)}"'
                replacement = rf'href="\1min/{minified}?v={file_hash}"'
                content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            
            if updated_count % 100 == 0:
                print(f"  Progress: {updated_count} files updated...")
    
    except Exception as e:
        print(f"  ⚠️  Error updating {html_file.name}: {e}")

print(f"\n📊 UPDATE COMPLETE:")
print(f"  Files updated: {updated_count}")
print(f"  Total files processed: {len(html_files)}")

# Save hash manifest
manifest_path = PUBLIC_DIR / 'CSS_VERSION_MANIFEST.json'
import json
with open(manifest_path, 'w') as f:
    json.dump(css_hashes, f, indent=2)

print(f"\n✅ Hash manifest saved: {manifest_path}")
print("\n✅ ALL HTML FILES UPDATED TO MINIFIED CSS WITH CACHE HASHING!")

