#!/usr/bin/env python3
"""
Content Integration Starter
Simple script to move high-quality teaching content from /dist to /public
"""

import os
import shutil
from pathlib import Path

def integrate_content():
    """Move high-quality content from dist to public directory"""
    
    # Source and destination directories
    base_dir = Path("/Users/admin/Documents/te-kete-ako-clean")
    dist_dir = base_dir / "dist"
    public_dir = base_dir / "public"
    
    # Create directories in public if they don't exist
    (public_dir / "dist-handouts").mkdir(exist_ok=True)
    (public_dir / "dist-lessons").mkdir(exist_ok=True)
    
    print("🎯 Starting content integration...")
    
    # 1. Move top 20 handouts
    print("\n📄 Moving top 20 handouts...")
    handouts_dir = dist_dir / "handouts"
    if handouts_dir.exists():
        handout_files = list(handouts_dir.glob("*.html"))[:20]
        for handout in handout_files:
            dest = public_dir / "dist-handouts" / handout.name
            shutil.copy2(handout, dest)
            print(f"  ✅ Copied: {handout.name}")
    
    # 2. Move guided inquiry lessons
    print("\n🎓 Moving guided inquiry lessons...")
    lessons_dir = dist_dir / "guided-inquiry-unit" / "lessons"
    if lessons_dir.exists():
        lesson_files = list(lessons_dir.glob("*.html"))
        for lesson in lesson_files:
            dest = public_dir / "dist-lessons" / lesson.name
            shutil.copy2(lesson, dest)
            print(f"  ✅ Copied: {lesson.name}")
    
    # 3. Create index pages for the new content
    create_index_pages(public_dir)
    
    print("\n🎉 Content integration complete!")
    print("📊 Next steps:")
    print("  1. Fix CSS/styling issues in moved content")
    print("  2. Update navigation to include new content")
    print("  3. Test all moved pages")

def create_index_pages(public_dir):
    """Create index pages for the new content"""
    
    # Create index for handouts
    handout_index = public_dir / "dist-handouts" / "index.html"
    with open(handout_index, 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Integrated Handouts | Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-professional.css">
</head>
<body>
    <div id="header-component"></div>
    
    <div class="container">
        <h1>📄 Integrated Handouts</h1>
        <p>High-quality teaching handouts moved from the dist directory</p>
        
        <div class="resource-grid">
""")
        
        # List all handouts
        for handout in sorted((public_dir / "dist-handouts").glob("*.html")):
            if handout.name != "index.html":
                title = handout.stem.replace("-", " ").title()
                f.write(f'            <a href="{handout.name}" class="resource-item">\n')
                f.write(f'                <h3>{title}</h3>\n')
                f.write(f'                <p>Teaching handout</p>\n')
                f.write(f'            </a>\n')
        
        f.write("""        </div>
    </div>
    
    <script src="/js/components/header.js"></script>
</body>
</html>""")
    
    # Create index for lessons
    lesson_index = public_dir / "dist-lessons" / "index.html"
    with open(lesson_index, 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Integrated Lessons | Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-professional.css">
</head>
<body>
    <div id="header-component"></div>
    
    <div class="container">
        <h1>🎓 Integrated Lessons</h1>
        <p>High-quality teaching lessons moved from the dist directory</p>
        
        <div class="resource-grid">
""")
        
        # List all lessons
        for lesson in sorted((public_dir / "dist-lessons").glob("*.html")):
            if lesson.name != "index.html":
                title = lesson.stem.replace("-", " ").title()
                f.write(f'            <a href="{lesson.name}" class="resource-item">\n')
                f.write(f'                <h3>{title}</h3>\n')
                f.write(f'                <p>Teaching lesson</p>\n')
                f.write(f'            </a>\n')
        
        f.write("""        </div>
    </div>
    
    <script src="/js/components/header.js"></script>
</body>
</html>""")

if __name__ == "__main__":
    integrate_content()
