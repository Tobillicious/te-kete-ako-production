#!/bin/bash
echo "🎯 METHODICAL QUALITY CHECK - Top 10 Critical Pages"
echo "===================================================================="

check_page() {
    local file=$1
    local name=$2
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📄 $name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if [ ! -f "$file" ]; then
        echo "   ❌ FILE NOT FOUND: $file"
        return
    fi
    
    echo -n "   ✓ Exists: ✅   "
    
    # Title
    if grep -q "<title>" "$file"; then
        TITLE=$(grep -o "<title>[^<]*</title>" "$file" | sed 's/<[^>]*>//g')
        echo "Title: '$TITLE'"
    else
        echo "   ❌ NO TITLE TAG"
    fi
    
    # Meta description
    echo -n "   ✓ Meta description: "
    grep -q 'meta name="description"' "$file" && echo "✅" || echo "❌ MISSING"
    
    # Quality checks
    echo -n "   ✓ No TODO markers: "
    grep -q "TODO" "$file" && echo "❌ FOUND" || echo "✅"
    
    echo -n "   ✓ No placeholders: "
    grep -qi "coming soon\|\[INSERT\]\|placeholder" "$file" && echo "❌ FOUND" || echo "✅"
    
    echo -n "   ✓ Has navigation: "
    grep -q "navigation-standard.html\|<nav" "$file" && echo "✅" || echo "⚠️  MISSING"
    
    echo -n "   ✓ Proper CSS links: "
    grep -q "te-kete.*\.css" "$file" && echo "✅" || echo "⚠️  CHECK NEEDED"
    
    # File size check
    SIZE=$(wc -c < "$file" | tr -d ' ')
    echo "   ✓ File size: $SIZE bytes"
}

# Check top 10 critical pages
check_page "public/index.html" "1. HOMEPAGE"
check_page "public/generated-resources-alpha/index.html" "2. AI Resources Index"
check_page "public/games/te-reo-wordle.html" "3. Te Reo Wordle Game"
check_page "public/y8-systems/index.html" "4. Y8 Systems Unit"
check_page "public/writers-toolkit/index.html" "5. Writers Toolkit"
check_page "public/tools/crossword-generator.html" "6. Crossword Generator"
check_page "public/critical-thinking/critical-thinking-toolkit.html" "7. Critical Thinking"
check_page "public/units/y7-maths-algebra/index.html" "8. Y7 Maths Algebra"
check_page "public/guided-inquiry-unit/index.html" "9. Guided Inquiry Unit"
check_page "public/handouts/index.html" "10. Handouts Library"

echo ""
echo "===================================================================="
echo "✅ Quality check of top 10 pages complete!"
echo "===================================================================="
