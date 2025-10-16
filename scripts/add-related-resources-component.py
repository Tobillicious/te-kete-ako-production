#!/usr/bin/env python3
"""
Add Related Resources Component to All Lesson Pages
GraphRAG-powered navigation for hierarchical content discovery
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PUBLIC_DIR = BASE_DIR / "public"

# Component to inject
RELATED_RESOURCES_COMPONENT = '''
    <!-- Related Resources (GraphRAG-Powered) -->
    <div id="related-resources-container"></div>
    <script>
        // Set current lesson metadata for related resources
        setCurrentResource({
            title: document.title,
            subject: document.querySelector('meta[name="subject"]')?.content || 'General',
            level: document.querySelector('meta[name="year-level"]')?.content || 'All Levels',
            tags: [],
            type: 'lesson'
        });
        
        // Load related resources component
        fetch('/components/related-resources.html')
            .then(r => r.text())
            .then(html => {
                document.getElementById('related-resources-container').innerHTML = html;
            })
            .catch(err => console.error('Related resources loading error:', err));
    </script>
'''

def add_related_resources_to_lesson(file_path):
    """Add related resources component to a lesson file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has related resources
    if 'related-resources-container' in content:
        return False, "Already has component"
    
    # Find where to inject (before closing </main> or </body>)
    if '</main>' in content:
        # Inject before </main>
        content = content.replace('</main>', f'{RELATED_RESOURCES_COMPONENT}\n</main>', 1)
    elif '</body>' in content:
        # Inject before </body> as fallback
        content = content.replace('</body>', f'{RELATED_RESOURCES_COMPONENT}\n</body>', 1)
    else:
        return False, "No injection point found"
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, "Component added"

def main():
    """Main execution"""
    print("🔗 ADDING RELATED RESOURCES COMPONENT TO LESSONS")
    print("=" * 60)
    
    # Directories to process
    lesson_dirs = [
        PUBLIC_DIR / "y8-systems" / "lessons",
        PUBLIC_DIR / "units" / "y7-maths-algebra" / "lessons",
        PUBLIC_DIR / "units" / "y7-science-ecosystems" / "lessons",
        PUBLIC_DIR / "units" / "y8-digital-kaitiakitanga" / "lessons",
        PUBLIC_DIR / "units" / "y9-science-ecology" / "lessons",
        PUBLIC_DIR / "units" / "unit-1-te-ao-maori" / "lessons",
        PUBLIC_DIR / "units" / "walker-unit",
        PUBLIC_DIR / "units" / "y8-critical-thinking",
    ]
    
    total_updated = 0
    total_skipped = 0
    
    for lesson_dir in lesson_dirs:
        if not lesson_dir.exists():
            print(f"\n⚠️  {lesson_dir.name}: Directory not found")
            continue
        
        print(f"\n📁 Processing: {lesson_dir.name}")
        
        lesson_files = sorted(lesson_dir.glob("*.html"))
        if lesson_dir.name == "walker-unit":  # Walker has lessons in lessons/ subdir
            lesson_files = sorted(lesson_dir.glob("lessons/*.html")) if (lesson_dir / "lessons").exists() else lesson_files
        
        for lesson_file in lesson_files:
            if 'index.html' in lesson_file.name:
                continue  # Skip index files
            
            success, message = add_related_resources_to_lesson(lesson_file)
            if success:
                print(f"  ✅ {lesson_file.name}: {message}")
                total_updated += 1
            else:
                print(f"  ⏭️  {lesson_file.name}: {message}")
                total_skipped += 1
    
    print("\n" + "=" * 60)
    print(f"✅ COMPLETE!")
    print(f"   Updated: {total_updated} lessons")
    print(f"   Skipped: {total_skipped} lessons (already had component)")
    print("🔗 Related resources navigation now live!")

if __name__ == "__main__":
    main()

