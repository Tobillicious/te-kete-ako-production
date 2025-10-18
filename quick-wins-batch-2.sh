#!/bin/bash
# QUICK WINS BATCH 2 - Find pages needing breadcrumbs

echo "🔍 FINDING PAGES WITHOUT BREADCRUMBS"
echo "===================================="
echo ""

# Key pages that should have breadcrumbs
PAGES_TO_CHECK=(
    "public/critical-thinking/critical-thinking-toolkit.html"
    "public/y8-systems/index.html"
    "public/writers-toolkit/index.html"
    "public/guided-inquiry-unit/index.html"
    "public/tools/index.html"
    "public/games/index.html"
)

MISSING=()

for page in "${PAGES_TO_CHECK[@]}"; do
    if [ -f "$page" ]; then
        if grep -q "breadcrumb\|🏠 Home" "$page"; then
            echo "✅ $(basename $page) - Has breadcrumbs"
        else
            echo "❌ $(basename $page) - MISSING breadcrumbs"
            MISSING+=("$page")
        fi
    else
        echo "⚠️  $(basename $page) - File not found"
    fi
done

echo ""
echo "📊 SUMMARY:"
echo "  Pages checked: ${#PAGES_TO_CHECK[@]}"
echo "  Missing breadcrumbs: ${#MISSING[@]}"

if [ ${#MISSING[@]} -gt 0 ]; then
    echo ""
    echo "📝 PAGES TO FIX:"
    for page in "${MISSING[@]}"; do
        echo "  - $page"
    done
fi
