#!/bin/bash
echo "📱 MOBILE EXPERIENCE VERIFICATION"
echo "=================================="
echo ""

# Check critical pages for mobile optimization
PAGES=(
    "public/index.html"
    "public/generated-resources-alpha/index.html"
    "public/games/te-reo-wordle.html"
    "public/tools/crossword-generator.html"
)

MOBILE_COUNT=0
TOTAL=0

for page in "${PAGES[@]}"; do
    TOTAL=$((TOTAL + 1))
    PAGE_NAME=$(basename "$page")
    
    if [ -f "$page" ]; then
        HAS_VIEWPORT=$(grep -c 'name="viewport"' "$page" || echo 0)
        HAS_MOBILE_CSS=$(grep -c 'mobile-optimization.css\|@media.*max-width' "$page" || echo 0)
        
        if [ "$HAS_VIEWPORT" -gt 0 ] && [ "$HAS_MOBILE_CSS" -gt 0 ]; then
            echo "✅ $PAGE_NAME - Mobile optimized"
            MOBILE_COUNT=$((MOBILE_COUNT + 1))
        else
            echo "⚠️  $PAGE_NAME - Missing mobile optimization"
        fi
    else
        echo "❌ $PAGE_NAME - File not found"
    fi
done

echo ""
echo "📊 RESULTS: $MOBILE_COUNT/$TOTAL pages are mobile-optimized"

if [ $MOBILE_COUNT -eq $TOTAL ]; then
    echo "🎉 PERFECT! All critical pages work on mobile!"
else
    echo "⚠️  Some pages need mobile optimization"
fi
