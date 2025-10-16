#!/bin/bash
# Deploy Enhanced Navigation Site-Wide
# Kaiārahi Hoahoa - Oct 15-16 Night Shift

echo "🎨 DEPLOYING STUNNING NAVIGATION SITE-WIDE"
echo "==========================================="

count=0

# Find all HTML files that load components
for file in $(find public -name "*.html" -exec grep -l 'components.js\|header-component' {} \; | grep -v backup | head -100); do
    
    # Add navigation CSS if not present
    if ! grep -q "navigation-enhanced.css" "$file"; then
        # Add after te-kete-professional.css
        sed -i.nav-deploy '/te-kete-professional\.css/a\
    <link rel="stylesheet" href="/css/navigation-enhanced.css">
' "$file"
    fi
    
    # Add navigation JS if not present
    if ! grep -q "navigation-enhanced.js" "$file"; then
        # Add before components.js or at end of scripts
        if grep -q "components.js" "$file"; then
            sed -i.nav-deploy '/components\.js/i\
    <script src="/js/navigation-enhanced.js" defer></script>
' "$file"
        fi
    fi
    
    count=$((count + 1))
    echo "  ✅ $(basename $file)"
    
    if [ $((count % 20)) -eq 0 ]; then
        echo "  📊 $count files processed..."
    fi
done

echo "==========================================="
echo "✅ Enhanced navigation deployed to $count files!"
echo "🎨 Site-wide stunning navigation COMPLETE!"
