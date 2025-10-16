#!/bin/bash
# =================================================================
# ADD MISSING UX CSS TO ALL PAGES
# Ensures all pages have ux-professional-enhancements.css
# Agent-9 - October 15, 2025
# =================================================================

echo "🎨 ADDING MISSING UX CSS..."

cd /Users/admin/Documents/te-kete-ako-clean/public

# Find pages that have te-kete-professional.css but NOT ux-professional-enhancements.css
for file in $(find . -name "*.html" -type f); do
    has_professional=$(grep -c "te-kete-professional.css" "$file" 2>/dev/null || echo 0)
    has_ux=$(grep -c "ux-professional-enhancements.css" "$file" 2>/dev/null || echo 0)
    
    if [ "$has_professional" -gt 0 ] && [ "$has_ux" -eq 0 ]; then
        echo "   📝 Adding UX CSS to: $file"
        
        # Add ux-professional-enhancements.css right after te-kete-professional.css
        sed -i '' '/te-kete-professional\.css/a\
    <link rel="stylesheet" href="/css/ux-professional-enhancements.css"/>
' "$file"
    fi
done

echo "✅ COMPLETE: UX CSS added to all pages!"

