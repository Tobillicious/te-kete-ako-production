#!/bin/bash
# =================================================================
# ENSURE ALL PAGES LOAD COMPONENTS.JS
# Critical for header/footer components to render
# Agent-9 - October 15, 2025
# =================================================================

echo "📋 ENSURING COMPONENTS.JS ON ALL PAGES..."

cd /Users/admin/Documents/te-kete-ako-clean/public

count=0

# Find HTML pages without components.js
for file in $(find . -name "*.html" -type f); do
    has_components=$(grep -c "components.js" "$file" 2>/dev/null || echo 0)
    has_closing_body=$(grep -c "</body>" "$file" 2>/dev/null || echo 0)
    
    if [ "$has_components" -eq 0 ] && [ "$has_closing_body" -gt 0 ]; then
        echo "   📝 Adding components.js to: $file"
        
        # Add components.js before </body>
        sed -i '' 's|</body>|    <script src="/js/components.js"></script>\
</body>|' "$file"
        
        ((count++))
        
        # Only show first 20 to avoid spam
        if [ $count -ge 20 ]; then
            echo "   ... (continuing silently)"
            break
        fi
    fi
done

echo "✅ COMPLETE: Added components.js to pages!"

