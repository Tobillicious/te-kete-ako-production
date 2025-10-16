#!/bin/bash
# Batch add West Coast NZ CSS to curriculum pages
# Agent-9 - Overnight Sprint

cd /Users/admin/Documents/te-kete-ako-clean/public

files=(
    "curriculum-mathematics.html"
    "curriculum-science.html"
    "curriculum-english.html"
    "curriculum-arts.html"
    "curriculum-social-sciences.html"
    "curriculum-technology.html"
    "curriculum-health-pe.html"
    "curriculum-languages.html"
    "social-studies.html"
    "te-ao-maori.html"
)

count=0

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        if ! grep -q "west-coast-nz-colors.css" "$file"; then
            # Add after opening <head> or before first stylesheet
            sed -i '' '/<head>/a\
    <link rel="stylesheet" href="/css/west-coast-nz-colors.css">
' "$file"
            echo "✅ Added to $file"
            ((count++))
        fi
    fi
done

echo "📊 West Coast CSS added to $count curriculum pages"

