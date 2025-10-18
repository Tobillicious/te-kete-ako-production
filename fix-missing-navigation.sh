#!/bin/bash
echo "🔧 FIXING MISSING NAVIGATION"
echo "============================================================"

# Fix mathematics-maori-games/index.html
FILE="public/units/mathematics-maori-games/index.html"

if [ -f "$FILE" ]; then
    echo "✅ Adding navigation to Mathematics & Māori Games unit..."
    
    # Add navigation script before closing </body>
    sed -i '' 's|</body>|<script>\n    fetch("/components/navigation-standard.html")\n        .then(r => r.text())\n        .then(html => {\n            const div = document.createElement("div");\n            div.innerHTML = html;\n            document.body.insertBefore(div.firstElementChild, document.body.firstChild);\n        });\n</script>\n</body>|' "$FILE"
    
    echo "✅ Navigation added to $FILE"
else
    echo "⚠️  File not found: $FILE"
fi

echo "============================================================"
echo "✅ Navigation fix complete!"
