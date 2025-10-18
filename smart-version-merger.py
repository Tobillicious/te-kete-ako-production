#!/usr/bin/env python3
"""
SMART VERSION MERGER
Compares versions and identifies best features to merge into production
"""

from pathlib import Path
import os
import shutil

def find_better_content():
    """Find content in backups that's better than current"""
    print("🔍 SMART VERSION ANALYSIS")
    print("=" * 70)
    
    recommendations = []
    
    # Check for missing AI tools
    ai_tools = [
        "ai-purakau-story-generator.html",
        "admin-youtube-library.html", 
        "ai-hub.html",
        "ai-coordination-dashboard.html"
    ]
    
    print("\n📱 AI TOOLS CHECK:")
    print("-" * 70)
    for tool in ai_tools:
        current = Path(f"public/{tool}")
        dist = Path(f"dist/{tool}")
        
        if dist.exists():
            dist_size = dist.stat().st_size
            
            if current.exists():
                current_size = current.stat().st_size
                if dist_size > current_size:
                    print(f"  ⬆️  {tool}: dist/ version is LARGER ({dist_size:,} vs {current_size:,})")
                    recommendations.append({
                        "action": "UPDATE",
                        "file": tool,
                        "reason": f"dist/ version more complete ({dist_size:,} bytes vs {current_size:,})"
                    })
                else:
                    print(f"  ✅ {tool}: current is good ({current_size:,} bytes)")
            else:
                print(f"  ⭐ {tool}: EXISTS in dist/ but MISSING in public! ({dist_size:,} bytes)")
                recommendations.append({
                    "action": "COPY",
                    "file": tool,
                    "reason": f"Missing valuable tool ({dist_size:,} bytes)"
                })
        else:
            print(f"  ❌ {tool}: not in dist/")
    
    # Check for unique directories in dist/
    print("\n\n📁 UNIQUE FEATURES IN DIST/:")
    print("-" * 70)
    
    dist_path = Path("dist")
    public_path = Path("public")
    
    if dist_path.exists():
        dist_dirs = {d.name for d in dist_path.iterdir() if d.is_dir()}
        public_dirs = {d.name for d in public_path.iterdir() if d.is_dir()}
        
        unique_in_dist = dist_dirs - public_dirs
        
        for dir_name in sorted(unique_in_dist):
            dir_path = dist_path / dir_name
            file_count = len(list(dir_path.rglob("*.*")))
            dir_size = sum(f.stat().st_size for f in dir_path.rglob("*.*") if f.is_file())
            
            print(f"  💎 {dir_name}/ - {file_count} files, {dir_size/1024:.1f}KB")
            
            if file_count > 0:
                recommendations.append({
                    "action": "EVALUATE",
                    "dir": dir_name,
                    "reason": f"Unique directory with {file_count} files"
                })
    
    # Compare specific files that exist in both
    print("\n\n🔄 FILE VERSION COMPARISON:")
    print("-" * 70)
    
    test_files = [
        "index.html",
        "critical-thinking/critical-thinking-toolkit.html",
        "handouts.html",
        "lessons.html"
    ]
    
    for file_rel in test_files:
        current = Path(f"public/{file_rel}")
        dist = Path(f"dist/{file_rel}")
        
        if current.exists() and dist.exists():
            c_size = current.stat().st_size
            d_size = dist.stat().st_size
            diff = d_size - c_size
            
            if abs(diff) > 5000:  # Significant difference
                if diff > 0:
                    print(f"  ⬆️  {file_rel}: dist/ is LARGER (+{diff:,} bytes)")
                    recommendations.append({
                        "action": "COMPARE",
                        "file": file_rel,
                        "reason": f"dist/ version significantly larger (+{diff:,} bytes)"
                    })
                else:
                    print(f"  ⬇️  {file_rel}: current is LARGER (+{abs(diff):,} bytes)")
            else:
                print(f"  ≈  {file_rel}: similar size (diff: {diff:,} bytes)")
    
    # Print recommendations
    print("\n\n✨ MERGE RECOMMENDATIONS:")
    print("=" * 70)
    
    by_action = {}
    for rec in recommendations:
        action = rec['action']
        if action not in by_action:
            by_action[action] = []
        by_action[action].append(rec)
    
    for action, recs in by_action.items():
        print(f"\n{action} ({len(recs)} items):")
        for rec in recs:
            if 'file' in rec:
                print(f"  • {rec['file']}: {rec['reason']}")
            elif 'dir' in rec:
                print(f"  • {rec['dir']}/: {rec['reason']}")
    
    # Save recommendations
    import json
    with open('merge-recommendations.json', 'w') as f:
        json.dump(recommendations, f, indent=2)
    
    print(f"\n💾 Saved {len(recommendations)} recommendations to merge-recommendations.json")
    
    return recommendations

if __name__ == "__main__":
    recommendations = find_better_content()
    
    print("\n" + "=" * 70)
    print("🎯 NEXT STEPS:")
    print("=" * 70)
    print("1. Review merge-recommendations.json")
    print("2. Manually inspect recommended files") 
    print("3. Merge best features into public/")
    print("4. Test merged site")
    print("\n✨ Goal: World-class platform with BEST of all versions!")

