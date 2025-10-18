#!/usr/bin/env python3
"""
FIND UNIQUE VALUABLE CONTENT
Identify pages in dist/backups that don't exist in public/ but should
"""

from pathlib import Path

def find_unique_valuable():
    """Find valuable content missing from production"""
    print("💎 FINDING UNIQUE VALUABLE CONTENT")
    print("=" * 70)
    
    public_files = {f.name for f in Path("public").rglob("*.html")}
    dist_path = Path("dist")
    
    valuable_categories = {
        "ai-tools": [],
        "admin-tools": [],
        "interactive": [],
        "assessment": [],
        "other": []
    }
    
    # Check dist/
    if dist_path.exists():
        for html_file in dist_path.rglob("*.html"):
            filename = html_file.name
            
            # Skip if already in public
            if filename in public_files:
                continue
            
            # Categorize
            filename_lower = filename.lower()
            if 'ai-' in filename_lower or 'generator' in filename_lower:
                valuable_categories["ai-tools"].append(str(html_file.relative_to(dist_path)))
            elif 'admin' in filename_lower or 'dashboard' in filename_lower:
                valuable_categories["admin-tools"].append(str(html_file.relative_to(dist_path)))
            elif 'interactive' in filename_lower or 'game' in filename_lower:
                valuable_categories["interactive"].append(str(html_file.relative_to(dist_path)))
            elif 'assessment' in filename_lower or 'rubric' in filename_lower:
                valuable_categories["assessment"].append(str(html_file.relative_to(dist_path)))
            else:
                valuable_categories["other"].append(str(html_file.relative_to(dist_path)))
    
    # Print findings
    print("\n💎 UNIQUE CONTENT IN DIST/:")
    print("-" * 70)
    
    for category, files in valuable_categories.items():
        if files:
            print(f"\n{category.upper()} ({len(files)} files):")
            for f in files[:10]:  # Show first 10
                print(f"  • {f}")
            if len(files) > 10:
                print(f"  ... and {len(files) - 10} more")
    
    # Save report
    import json
    with open('unique-content-report.json', 'w') as f:
        json.dump(valuable_categories, f, indent=2)
    
    total_unique = sum(len(files) for files in valuable_categories.values())
    print(f"\n📊 Total unique files in dist/: {total_unique}")
    print("💾 Saved to: unique-content-report.json")
    
    return valuable_categories

if __name__ == "__main__":
    find_unique_valuable()
    print("\n" + "=" * 70)
    print("🎯 Next: Review unique-content-report.json and decide what to merge")

