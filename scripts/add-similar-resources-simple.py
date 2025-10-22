#!/usr/bin/env python3
"""
Simple Python script to add Similar Resources component to lessons
"""

import os
import glob

base_path = "/Users/admin/Documents/te-kete-ako-clean"
lessons_pattern = os.path.join(base_path, "public/lessons/**/*.html")

# Component template
component_template = '''
<!-- 🔗 GraphRAG Similar Resources Component -->
<div id="similar-resources" data-resource-path="{}"></div>
<script src="/components/graphrag-similar-resources.html"></script>
'''

success_count = 0
skip_count = 0
target = 30

print("🚀 Adding Similar Resources component to lessons...\n")

for file_path in glob.glob(lessons_pattern, recursive=True):
    if success_count >= target:
        print(f"\n✋ Reached target of {target} additions. Stopping.")
        break
    
    # Skip index files
    if file_path.endswith("/index.html"):
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has component
        if 'graphrag-similar-resources' in content or 'id="similar-resources"' in content:
            print(f"⏭️  Already has component: {os.path.basename(file_path)}")
            skip_count += 1
            continue
        
        # Skip if no closing body tag
        if '</body>' not in content:
            print(f"⚠️  No </body> tag: {os.path.basename(file_path)}")
            skip_count += 1
            continue
        
        # Get relative path for data-resource-path
        rel_path = file_path.replace(base_path + "/", "")
        
        # Insert component before </body>
        component = component_template.format("/" + rel_path)
        new_content = content.replace('</body>', component + '\n</body>')
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ [{success_count + 1}/{target}] SUCCESS: {os.path.basename(file_path)}")
        success_count += 1
        
    except Exception as e:
        print(f"❌ ERROR: {os.path.basename(file_path)} - {str(e)}")

print("\n" + "=" * 60)
print("📊 SUMMARY")
print("=" * 60)
print(f"✅ Success: {success_count} lessons")
print(f"⚠️  Skipped: {skip_count} lessons")
print("=" * 60)

