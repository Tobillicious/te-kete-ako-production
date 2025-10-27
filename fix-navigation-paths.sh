#!/bin/bash

# Fix navigation paths site-wide
# Converts relative navigation links to absolute paths

# Files to process (exclude dist, backups, archives)
files=$(find . -name "*.html" -type f \
    ! -path "./dist/*" \
    ! -path "./node_modules/*" \
    ! -path "./backups/*" \
    ! -path "./archive/*" \
    ! -path "./archived-bloat/*" \
    ! -path "./old-lessons/*")

echo "🔧 Fixing navigation paths in HTML files..."
echo "Found $(echo "$files" | wc -l) files to process"

# Navigation pages to fix
nav_pages=(
    "index.html"
    "browse.html"
    "unit-plans.html"
    "lessons.html"
    "handouts.html"
    "games.html"
    "activities.html"
    "youtube.html"
    "login.html"
    "register-simple.html"
    "my-kete.html"
    "curriculum-alignment.html"
    "other-resources.html"
)

for file in $files; do
    # Skip if file doesn't exist
    [[ ! -f "$file" ]] && continue
    
    # Fix each navigation page reference
    for page in "${nav_pages[@]}"; do
        # Fix relative links: href="page.html" or href="../page.html"
        sed -i.bak "s|href=\"\.\./\?${page}\"|href=\"/${page}\"|g" "$file"
        sed -i.bak "s|href=\"${page}\"|href=\"/${page}\"|g" "$file"
        
        # Fix with query params: href="page.html?..." or href="../page.html?..."
        sed -i.bak "s|href=\"\.\./\?${page}?|href=\"/${page}?|g" "$file"
    done
    
    # Remove backup files
    rm -f "${file}.bak"
done

echo "✅ Navigation paths fixed!"
echo "All href links now use absolute paths (e.g., href=\"/browse.html\")"

