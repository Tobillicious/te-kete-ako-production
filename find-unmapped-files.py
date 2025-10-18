#!/usr/bin/env python3
"""
Find files NOT yet in GraphRAG and prepare for bulk MCP insert
"""

import os
import json
from pathlib import Path

def get_all_files():
    """Get all indexable files from filesystem"""
    files = set()
    extensions = ['.html', '.js', '.css', '.py']
    
    for root, dirs, filenames in os.walk('.'):
        # Skip hidden and unwanted dirs
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
        
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, filename)
                # Make relative
                file_path = file_path.replace('./', '')
                files.add(file_path)
    
    return files

def read_indexed_from_graphrag_export():
    """Read what's already indexed from a GraphRAG export query result"""
    # We'll need to query GraphRAG via MCP first
    # This is a placeholder - we'll use MCP to get the real data
    return set()

def categorize_file(file_path):
    """Quick categorization for bulk insert"""
    path = str(file_path)
    
    if '/units/' in path and '/lessons/' in path:
        return 'Lesson', 'subject_from_unit', 80
    elif '/units/' in path and 'index.html' in path:
        return 'Unit Plan', 'subject_from_unit', 85
    elif '/games/' in path:
        return 'Interactive Game', 'subject_from_filename', 65
    elif '/components/' in path:
        return 'Component', 'General', 75
    elif path.endswith('.js'):
        return 'JavaScript', 'General', 70
    elif path.endswith('.css'):
        return 'Stylesheet', 'General', 70
    elif path.endswith('.py'):
        return 'Python Script', 'Automation', 75
    elif '-hub.html' in path:
        return 'Hub Page', 'Navigation', 90
    elif 'backup_before_css_migration' in path:
        return 'Legacy Resource', 'subject_from_filename', 70
    else:
        return 'Page', 'General', 75

def main():
    all_files = get_all_files()
    
    print(f"📊 Found {len(all_files)} total files in codebase")
    print(f"\nFirst 20 files:")
    for i, f in enumerate(sorted(all_files)[:20]):
        resource_type, subject, quality = categorize_file(f)
        print(f"  {resource_type:20} | {f}")
    
    # Export sample for MCP batch insert
    sample_files = sorted(all_files)[:100]
    
    print(f"\n📝 Sample of 100 files for testing:")
    for f in sample_files[:10]:
        print(f"  {f}")
    
    # Save full list
    with open('/tmp/all-codebase-files.txt', 'w') as out:
        for f in sorted(all_files):
            out.write(f + '\n')
    
    print(f"\n✅ Full list saved to /tmp/all-codebase-files.txt")
    print(f"📊 Total: {len(all_files)} files")

if __name__ == "__main__":
    main()

