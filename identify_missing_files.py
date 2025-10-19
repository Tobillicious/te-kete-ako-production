#!/usr/bin/env python3
import os
import requests
import json

# Get list of HTML files on disk
html_files_on_disk = []
for root, dirs, files in os.walk('/Users/admin/Documents/te-kete-ako-clean/public'):
    for file in files:
        if file.endswith('.html'):
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, '/Users/admin/Documents/te-kete-ako-clean/public')
            html_files_on_disk.append(relative_path)

print(f"Total HTML files on disk: {len(html_files_on_disk)}")

# Get list of HTML files in GraphRAG
# Note: We'll need to use MCP to query this properly
# For now, let's create a list of files that should be indexed

missing_files = []
for file_path in html_files_on_disk:
    # Skip certain file types that shouldn't be in GraphRAG
    if any(skip in file_path for skip in ['/components/', '/templates/', '/js/', '/css/', '/games/', '/node_modules/']):
        continue
    
    # Skip backup and temporary files
    if file_path.endswith('.bak') or '.backup' in file_path or 'backup' in file_path:
        continue
    
    missing_files.append(file_path)

print(f"Files that should be indexed: {len(missing_files)}")

# Write the list to a file for processing
with open('files_to_index.json', 'w') as f:
    json.dump(missing_files, f, indent=2)

print(f"Written {len(missing_files)} files to files_to_index.json")
