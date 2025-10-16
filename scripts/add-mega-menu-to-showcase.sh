#!/bin/bash
# Add mega menu to showcase lessons that are missing it
# Critical for October 22 presentation!

echo "════════════════════════════════════════════════════"
echo "🚨 FIXING MEGA MENU ON SHOWCASE LESSONS"
echo "════════════════════════════════════════════════════"
echo ""

MEGA_MENU_CODE='    <!-- Professional Mega Menu Navigation -->
    <script>
        fetch('\''/components/navigation-mega-menu.html'\'')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('\''div'\'');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>'

# Function to add mega menu after <body> tag
add_mega_menu() {
    local file="$1"
    local filename=$(basename "$file")
    
    if [ ! -f "$file" ]; then
        echo "⚠️  $filename - File not found"
        return
    fi
    
    if grep -q "navigation-mega-menu.html" "$file"; then
        echo "✅ $filename - Already has mega menu"
        return
    fi
    
    # Add mega menu right after <body> tag
    sed -i.backup '/^<body/a\
'"$MEGA_MENU_CODE" "$file"
    
    echo "✅ $filename - Mega menu added!"
}

echo "Adding mega menu to showcase lessons..."
echo ""

# Democracy
add_mega_menu "public/y8-systems/lessons/lesson-2-1.html"

# Treaty
add_mega_menu "public/y8-systems/lessons/lesson-4-1.html"

# Guided Inquiry
add_mega_menu "public/y8-systems/lessons/lesson-5-1.html"

echo ""
echo "════════════════════════════════════════════════════"
echo "✅ MEGA MENU FIX COMPLETE!"
echo "════════════════════════════════════════════════════"

