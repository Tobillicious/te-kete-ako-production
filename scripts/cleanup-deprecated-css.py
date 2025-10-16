#!/usr/bin/env python3
"""
CLEANUP DEPRECATED CSS REFERENCES
Remove ALL deprecated CSS references including preload, prefetch, etc.
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

DEPRECATED_CSS = [
    'main.css',
    'te-kete-professional.css',
    'ux-professional-enhancements.css',
    'ux-enhancements.css',
    'west-coast-nz-colors.css',
    'professional-enhancements.css',
    'cta-enhancements.css',
    'loading-states.css',
    'design-system-v3.css',
    'award-winning-polish.css'
]

def cleanup_html_file(filepath):
    """Remove all deprecated CSS references from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes = 0
        
        # Remove all link tags that reference deprecated CSS
        for dep_css in DEPRECATED_CSS:
            # Pattern for any link tag (stylesheet, preload, prefetch, etc.)
            pattern = r'<link[^>]*' + re.escape(dep_css) + r'[^>]*>\s*'
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                changes += len(matches)
                content = re.sub(pattern, '', content, flags=re.IGNORECASE)
        
        # Write back if changes made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        
        return 0
        
    except Exception as e:
        print(f"  ❌ Error: {filepath.name}: {e}")
        return -1

def main():
    print("🧹 CLEANING UP DEPRECATED CSS REFERENCES")
    print("=" * 60)
    
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    print(f"📊 Total HTML files: {len(html_files)}")
    
    total_changes = 0
    files_cleaned = 0
    errors = 0
    
    for i, html_file in enumerate(html_files, 1):
        changes = cleanup_html_file(html_file)
        
        if changes > 0:
            files_cleaned += 1
            total_changes += changes
        elif changes < 0:
            errors += 1
        
        if i % 200 == 0:
            print(f"  Progress: {i}/{len(html_files)} files processed...")
    
    print(f"\n📊 CLEANUP COMPLETE:")
    print(f"  ✅ Files cleaned: {files_cleaned}")
    print(f"  🗑️  References removed: {total_changes}")
    print(f"  ❌ Errors: {errors}")
    
    # Validate
    print(f"\n🧪 VALIDATING CLEANUP...")
    still_has_deprecated = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if any(dep in content for dep in DEPRECATED_CSS):
                still_has_deprecated += 1
        except:
            pass
    
    print(f"  Pages still with deprecated CSS: {still_has_deprecated}")
    
    if still_has_deprecated == 0:
        print(f"\n🎉 SUCCESS! All deprecated CSS removed!")
    else:
        print(f"\n⚠️  {still_has_deprecated} pages still need attention")

if __name__ == "__main__":
    main()

