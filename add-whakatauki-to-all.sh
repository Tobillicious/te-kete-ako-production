#!/bin/bash

# Add whakataukī sidebar to ALL content pages
# Works by:
# 1. Adding empty <aside class="left-sidebar"> structure after header
# 2. Adding daily-whakatauki.js script before </body>
# 3. Script dynamically injects whakataukī into sidebar!

echo "🌟 Adding whakataukī to all content pages..."

# Process video activities (depth 2: handouts/video-activities/)
for file in handouts/video-activities/*.html; do
    [ ! -f "$file" ] && continue
    
    # Skip if already has sidebar
    grep -q "left-sidebar" "$file" && continue
    
    # Add sidebar structure after header (before first <main or first <div after header)
    sed -i '' '/<\/header>/a\
\
    <div class="main-container">\
        <aside class="left-sidebar no-print"></aside>\
        <main class="content-area">
' "$file"
    
    # Close the wrapping divs before footer
    sed -i '' 's|<footer|    </main>\
    </div>\
\
<footer|' "$file"
    
    # Add script before </body> if missing
    if ! grep -q "daily-whakatauki.js" "$file"; then
        sed -i '' 's|</body>|    <script src="../../js/daily-whakatauki.js"></script>\
</body>|' "$file"
    fi
    
    echo "✓ $file"
done

echo "✅ Video activities complete! Script will auto-inject whakataukī."
echo "Run this for other directories (units/, handouts/, games/, lessons/) with appropriate paths"

