#!/bin/bash
# CSS Cleanup Script - Remove conflicting design system links
# October 26, 2025 - BMAD System Only

echo "🎨 CSS CLEANUP: Removing conflicting design system links..."
echo ""

# Find all HTML files and remove the conflicting CSS links
find public -name "*.html" -type f | while read file; do
    # Check if file contains any of the conflicting CSS links
    if grep -q "te-kete-ultimate-beauty-system.css\|te-kete-transformative-design-system.css\|design-system-v3.css" "$file"; then
        echo "Cleaning: $file"
        
        # Remove the conflicting CSS links
        sed -i.bak \
            -e '/te-kete-ultimate-beauty-system\.css/d' \
            -e '/te-kete-transformative-design-system\.css/d' \
            -e '/design-system-v3\.css/d' \
            "$file"
        
        # Remove backup file
        rm "${file}.bak"
    fi
done

echo ""
echo "✅ Cleanup complete!"
echo ""
echo "BMAD System files (should still be loaded):"
echo "  - te-kete-bmad-authentic.css"
echo "  - navigation-standard.css"
echo "  - mobile-revolution.css"
echo "  - tailwind.css"

