#!/usr/bin/env python3
"""
Apply BMAD Authentic CSS to All Hub Pages
Restores cultural design authenticity across platform
"""

import os
import glob
from pathlib import Path

# BMAD CSS link to add (loads FIRST so it wins cascade)
BMAD_CSS_LINK = '<!-- 🌿 BMAD AUTHENTIC CULTURAL DESIGN (Primary - loads FIRST!) -->\n<link rel="stylesheet" href="/css/te-kete-bmad-authentic.css"/>\n'

def add_bmad_to_file(file_path):
    """Add BMAD CSS to a single file if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if BMAD CSS already added
        if 'te-kete-bmad-authentic.css' in content:
            print(f"  ✅ Already has BMAD: {os.path.basename(file_path)}")
            return False
        
        # Find <head> tag and add BMAD CSS right after
        if '<head>' in content:
            content = content.replace('<head>', f'<head>\n{BMAD_CSS_LINK}', 1)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✅ Added BMAD: {os.path.basename(file_path)}")
            return True
        else:
            print(f"  ⚠️  No <head> tag: {os.path.basename(file_path)}")
            return False
            
    except Exception as e:
        print(f"  ❌ Error: {os.path.basename(file_path)} - {e}")
        return False

def main():
    print("🌿 APPLYING BMAD AUTHENTIC CSS TO ALL HUB PAGES...")
    print()
    
    # Find all hub HTML files
    hub_patterns = [
        'public/*-hub.html',
        'public/*/resource-hub.html',
        'public/*/resource-discovery-hub.html',
        'public/*/ai-hub.html',
        'public/*/teacher-ai-intelligence-hub.html',
        'public/*/*/resource-hub.html',
        'public/*/*/resource-discovery-hub.html',
        'public/*/*/ai-hub.html'
    ]
    
    all_hubs = []
    for pattern in hub_patterns:
        all_hubs.extend(glob.glob(pattern))
    
    # Remove duplicates and sort
    all_hubs = sorted(set(all_hubs))
    
    print(f"📊 Found {len(all_hubs)} hub pages")
    print()
    
    # Apply BMAD to each
    added_count = 0
    skipped_count = 0
    
    for hub_path in all_hubs:
        if add_bmad_to_file(hub_path):
            added_count += 1
        else:
            skipped_count += 1
    
    print()
    print(f"🎊 COMPLETE!")
    print(f"  ✅ Added BMAD: {added_count} pages")
    print(f"  ⏭️  Skipped (already had): {skipped_count} pages")
    print(f"  📊 Total processed: {len(all_hubs)} pages")
    print()
    print("🌿 BMAD cultural design now applied across platform!")

if __name__ == "__main__":
    main()

