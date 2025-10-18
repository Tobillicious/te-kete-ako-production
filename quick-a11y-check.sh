#!/bin/bash
# QUICK ACCESSIBILITY CHECK
# Check for basic accessibility issues

echo "♿ QUICK ACCESSIBILITY CHECK"
echo "============================"
echo ""

PAGES=(
    "public/index.html"
    "public/games/index.html"
    "public/tools/index.html"
    "public/generated-resources-alpha/index.html"
)

GOOD=0
WARNINGS=0

for page in "${PAGES[@]}"; do
    PAGE_NAME=$(basename $(dirname $page))/$(basename $page)
    echo "📄 Checking: $PAGE_NAME"
    
    if [ -f "$page" ]; then
        # Check for lang attribute
        if grep -q '<html lang="en"' "$page"; then
            echo "  ✅ Language declared"
            GOOD=$((GOOD + 1))
        else
            echo "  ⚠️  No language attribute"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        # Check for viewport meta
        if grep -q 'name="viewport"' "$page"; then
            echo "  ✅ Viewport meta present"
            GOOD=$((GOOD + 1))
        else
            echo "  ⚠️  Missing viewport meta"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        # Check for role="main"
        if grep -q 'role="main"\|<main' "$page"; then
            echo "  ✅ Main landmark present"
            GOOD=$((GOOD + 1))
        else
            echo "  ⚠️  No main landmark"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        # Check for nav elements
        if grep -q '<nav\|role="navigation"' "$page"; then
            echo "  ✅ Navigation landmark"
            GOOD=$((GOOD + 1))
        else
            echo "  ⚠️  No navigation landmark"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        echo ""
    fi
done

echo "=="
echo "📊 ACCESSIBILITY RESULTS:"
echo "  ✅ Good practices: $GOOD"
echo "  ⚠️  Warnings: $WARNINGS"
echo "=="

if [ $WARNINGS -eq 0 ]; then
    echo "🎉 EXCELLENT! All basic accessibility checks pass!"
elif [ $WARNINGS -le 5 ]; then
    echo "👍 GOOD! Minor accessibility improvements possible"
else
    echo "⚠️  Several accessibility improvements needed"
fi
