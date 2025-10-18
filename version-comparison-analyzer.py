#!/usr/bin/env python3
"""
VERSION COMPARISON ANALYZER
Compare current public/ with backups/dist to find best features to merge
"""

from pathlib import Path
import os

def analyze_directories():
    """Compare different versions"""
    print("🔍 VERSION COMPARISON ANALYSIS")
    print("=" * 70)
    
    versions = {
        "CURRENT (public/)": Path("public"),
        "DIST (dist/)": Path("dist"),
        "CSS_BACKUP (backup_before_css_migration/public/)": Path("backup_before_css_migration/public"),
        "BACKUPS (backups/)": Path("backups")
    }
    
    results = {}
    
    for name, path in versions.items():
        if path.exists():
            # Count files
            html_count = len(list(path.rglob("*.html")))
            css_count = len(list(path.rglob("*.css")))
            js_count = len(list(path.rglob("*.js")))
            
            # Find unique features
            subdirs = [d.name for d in path.iterdir() if d.is_dir() and not d.name.startswith('.')]
            
            results[name] = {
                "html": html_count,
                "css": css_count,
                "js": js_count,
                "dirs": subdirs[:20]  # First 20 dirs
            }
    
    # Print comparison
    print("\n📊 FILE COUNTS BY VERSION:")
    print("-" * 70)
    for version, data in results.items():
        print(f"\n{version}:")
        print(f"  HTML: {data['html']:,}")
        print(f"  CSS:  {data['css']:,}")
        print(f"  JS:   {data['js']:,}")
    
    # Find unique features in each version
    print("\n\n🎯 UNIQUE FEATURES ANALYSIS:")
    print("-" * 70)
    
    current_dirs = set(results["CURRENT (public/)"]["dirs"])
    
    for version, data in results.items():
        if version == "CURRENT (public/)":
            continue
        
        version_dirs = set(data["dirs"])
        unique = version_dirs - current_dirs
        
        if unique:
            print(f"\n{version} has UNIQUE directories:")
            for dir in sorted(unique):
                print(f"  • {dir}")
    
    # Check dist/ for features
    dist_path = Path("dist")
    if dist_path.exists():
        print("\n\n💎 FEATURES IN DIST/ (Might Be Better!):")
        print("-" * 70)
        
        interesting_files = [
            "ai-purakau-story-generator.html",
            "admin-youtube-library.html",
            "ai-hub.html",
            "ai-coordination-dashboard.html",
        ]
        
        for filename in interesting_files:
            if (dist_path / filename).exists():
                size = (dist_path / filename).stat().st_size
                print(f"  ✨ {filename} ({size:,} bytes)")
        
        # Check for unique directories
        dist_dirs = [d.name for d in dist_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
        current_dirs_list = [d.name for d in Path("public").iterdir() if d.is_dir() and not d.name.startswith('.')]
        
        unique_dist_dirs = set(dist_dirs) - set(current_dirs_list)
        if unique_dist_dirs:
            print("\n  📁 UNIQUE directories in dist/:")
            for dir in sorted(unique_dist_dirs):
                file_count = len(list((dist_path / dir).rglob("*.*")))
                print(f"     • {dir}/ ({file_count} files)")

if __name__ == "__main__":
    analyze_directories()
    
    print("\n" + "=" * 70)
    print("✨ ANALYSIS COMPLETE!")
    print("=" * 70)
    print("\n🎯 Next: Review unique features and merge best content into public/")

