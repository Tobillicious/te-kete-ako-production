#!/bin/bash

# Fix missing te-kete-professional.css in 68 files
# cursor-node-1 - CSS/JS Final 10% Verification

echo "🎯 FIXING MISSING CSS INCLUDES - 68 FILES"
echo "=========================================="

# Get list of files missing te-kete-professional.css
MISSING_FILES=$(find /Users/admin/Documents/te-kete-ako-clean/public -name "*.html" -exec grep -L "te-kete-professional\.css" {} \;)

echo "📊 Files to fix: $(echo "$MISSING_FILES" | wc -l)"

# Counter for progress
count=0
total=$(echo "$MISSING_FILES" | wc -l)

echo "$MISSING_FILES" | while read -r file; do
    if [ -f "$file" ]; then
        count=$((count + 1))
        echo "[$count/$total] Processing: $(basename "$file")"
        
        # Check if file has a <head> section
        if grep -q "<head>" "$file"; then
            # Add te-kete-professional.css after <head> or after first <link> if exists
            if grep -q '<link.*rel="stylesheet"' "$file"; then
                # Add after first stylesheet link
                sed -i '' '/<link.*rel="stylesheet"/a\
    <link rel="stylesheet" href="/css/te-kete-professional.css">' "$file"
            else
                # Add after <head>
                sed -i '' '/<head>/a\
    <link rel="stylesheet" href="/css/te-kete-professional.css">' "$file"
            fi
        else
            echo "  ⚠️  No <head> section found, skipping"
        fi
    fi
done

echo ""
echo "✅ CSS FIX COMPLETE!"
echo "📊 Verifying results..."

# Verify the fix
NEW_MISSING=$(find /Users/admin/Documents/te-kete-ako-clean/public -name "*.html" -exec grep -L "te-kete-professional\.css" {} \; | wc -l)
echo "📈 Files still missing: $NEW_MISSING"

if [ "$NEW_MISSING" -eq 0 ]; then
    echo "🎉 SUCCESS: 100% CSS coverage achieved!"
else
    echo "⚠️  $NEW_MISSING files still need manual review"
fi
