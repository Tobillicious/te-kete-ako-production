#!/bin/bash
# Script to add professional CSS import to HTML files that don't have it

files=$(find /Users/admin/Documents/te-kete-ako-clean/public -name "*.html" -exec grep -L "te-kete-professional.css" {} \;)

for file in $files; do
    echo "Processing: $file"
    
    # Check if file has meta author tag
    if grep -q '<meta name="author" content="Te Kete Ako">' "$file"; then
        # Add after meta author tag
        sed -i.bak '/<meta name="author" content="Te Kete Ako">/a\
<!-- Professional Design System -->\
<link rel="stylesheet" href="/css/te-kete-professional.css">' "$file"
    elif grep -q '<meta name="description" content=' "$file"; then
        # Add after meta description tag
        sed -i.bak '/<meta name="description" content=/a\
<!-- Professional Design System -->\
<link rel="stylesheet" href="/css/te-kete-professional.css">' "$file"
    else
        # Add before closing head tag
        sed -i.bak '/<\/head>/i\
<!-- Professional Design System -->\
<link rel="stylesheet" href="/css/te-kete-professional.css">' "$file"
    fi
    
    echo "✓ Added professional CSS to $file"
done

echo "Professional CSS import process complete!"
