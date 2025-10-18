#!/bin/bash
echo "🎯 METHODICAL QUALITY CHECK - One File at a Time"
echo "===================================================================="
echo ""
echo "Starting with most critical user-facing pages..."
echo ""

# Check homepage quality
echo "1️⃣ HOMEPAGE (index.html):"
echo "   📄 Checking /public/index.html..."

if [ -f "public/index.html" ]; then
    # Check for issues
    echo -n "   - Has title tag: "
    grep -q "<title>" public/index.html && echo "✅" || echo "❌"
    
    echo -n "   - Has meta description: "
    grep -q 'meta name="description"' public/index.html && echo "✅" || echo "❌"
    
    echo -n "   - No TODO markers: "
    grep -q "TODO" public/index.html && echo "❌ FOUND" || echo "✅"
    
    echo -n "   - No coming soon: "
    grep -qi "coming soon" public/index.html && echo "❌ FOUND" || echo "✅"
    
    echo -n "   - No placeholders: "
    grep -q "\[INSERT\]" public/index.html && echo "❌ FOUND" || echo "✅"
    
    echo -n "   - File size reasonable: "
    SIZE=$(wc -c < public/index.html)
    echo "$SIZE bytes"
else
    echo "   ❌ FILE NOT FOUND"
fi

echo ""
echo "===================================================================="
