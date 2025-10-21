#!/usr/bin/env python3
"""
Strategic CSS/JS Batch Fixer - Alpha Readiness Priority
Targets the critical 1,921 files missing CSS/JS for Mangakōtukutuku College deployment
"""

import os
import re
import glob
from pathlib import Path

# Standard CSS includes for professional styling
CSS_INCLUDES = '''    <link rel="stylesheet" href="/css/main.css">
    <link rel="stylesheet" href="/css/mobile-optimization.css">
    <link rel="stylesheet" href="/css/print.css" media="print">'''

def needs_css_fix(file_path):
    """Check if HTML file needs CSS includes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Must have <head> and be missing main.css
        has_head = '<head' in content.lower()
        missing_main_css = 'main.css' not in content
        
        return has_head and missing_main_css
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def apply_css_fix(file_path):
    """Apply CSS fix to a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strategy 1: Add after te-kete-ultimate-beauty-system.css
        if 'te-kete-ultimate-beauty-system.css' in content:
            pattern = r'(<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system\.css"[^>]*>)'
            if re.search(pattern, content):
                new_content = re.sub(pattern, r'\1\n' + CSS_INCLUDES, content, count=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return 'after_beauty_system'
        
        # Strategy 2: Add after te-kete-professional.css
        if 'te-kete-professional.css' in content:
            pattern = r'(<link rel="stylesheet" href="/css/te-kete-professional\.css"[^>]*>)'
            if re.search(pattern, content):
                new_content = re.sub(pattern, r'\1\n' + CSS_INCLUDES, content, count=1)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return 'after_professional'
        
        # Strategy 3: Add before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', CSS_INCLUDES + '\n</head>', 1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'before_head_close'
        
        return 'no_suitable_location'
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return 'error'

def process_priority_batch(directory, batch_name, limit=None):
    """Process a specific directory batch"""
    print(f"\n🎯 Processing {batch_name}...")
    
    pattern = os.path.join(directory, "**/*.html")
    html_files = glob.glob(pattern, recursive=True)
    
    if limit:
        html_files = html_files[:limit]
    
    files_needing_fix = [f for f in html_files if needs_css_fix(f)]
    
    print(f"Found {len(files_needing_fix)} files needing CSS fix in {batch_name}")
    
    fixed_count = 0
    strategies = {}
    
    for file_path in files_needing_fix:
        rel_path = os.path.relpath(file_path, '/Users/admin/Documents/te-kete-ako-clean/public')
        strategy = apply_css_fix(file_path)
        
        if strategy not in ['error', 'no_suitable_location']:
            fixed_count += 1
            strategies[strategy] = strategies.get(strategy, 0) + 1
            if fixed_count <= 5:  # Show first 5 fixes
                print(f"  ✅ Fixed: {rel_path} ({strategy})")
        else:
            print(f"  ❌ Failed: {rel_path} ({strategy})")
    
    print(f"✅ {batch_name} Complete: {fixed_count}/{len(files_needing_fix)} files fixed")
    if strategies:
        print(f"   Strategies used: {strategies}")
    
    return fixed_count, len(files_needing_fix)

def main():
    """Strategic batch processing for alpha readiness"""
    print("🚀 STRATEGIC CSS/JS FIXER - ALPHA READINESS")
    print("=" * 60)
    
    base_dir = "/Users/admin/Documents/te-kete-ako-clean/public"
    
    # Priority order based on strategic roadmap
    priority_batches = [
        # Phase 1: Generated Resources Alpha (high quality, orphaned)
        (f"{base_dir}/generated-resources-alpha", "Generated Resources Alpha", 50),
        
        # Phase 2: Core Hub Pages (high visibility)
        (f"{base_dir}/curriculum-*.html", "Curriculum Hub Pages", None),
        
        # Phase 3: Core lesson/handout directories
        (f"{base_dir}/lessons", "Lessons Directory", 100),
        (f"{base_dir}/handouts", "Handouts Directory", 100),
        
        # Phase 4: Unit Plans
        (f"{base_dir}/units", "Units Directory", 100),
        
        # Phase 5: Integrated Resources
        (f"{base_dir}/integrated-lessons", "Integrated Lessons", 200),
        (f"{base_dir}/integrated-handouts", "Integrated Handouts", 200),
    ]
    
    total_fixed = 0
    total_needed = 0
    
    for directory, batch_name, limit in priority_batches:
        if os.path.exists(directory) or '*' in directory:
            fixed, needed = process_priority_batch(directory, batch_name, limit)
            total_fixed += fixed
            total_needed += needed
    
    print("\n" + "=" * 60)
    print(f"🎉 STRATEGIC BATCH COMPLETE")
    print(f"📊 Total Files Fixed: {total_fixed}/{total_needed}")
    print(f"🎯 Alpha Readiness: {((total_fixed/total_needed)*100):.1f}% CSS coverage")
    print("\n🔗 Next: Link orphaned pages to navigation")

if __name__ == "__main__":
    main()