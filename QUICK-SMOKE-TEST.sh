#!/bin/bash

# 🔥 QUICK SMOKE TEST - Verify critical files exist before deploy
# Run this before git push to catch missing files

echo "🔥 QUICK SMOKE TEST - Te Kete Ako"
echo "=================================="
echo ""

FAIL_COUNT=0

# Test 1: Core Pages
echo "✅ Test 1: Core Pages Exist"
FILES=(
    "public/index.html"
    "public/browse-lessons.html"
    "public/browse-handouts.html"
    "public/browse-units.html"
    "public/year-7-hub.html"
    "public/year-8-hub.html"
    "public/cultural-hub.html"
    "public/integration-tools-showcase.html"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ MISSING: $file"
        ((FAIL_COUNT++))
    fi
done
echo ""

# Test 2: CSS Files
echo "✅ Test 2: CSS Files Exist"
CSS_FILES=(
    "public/css/te-kete-professional.css"
    "public/css/te-kete-ultimate-beauty-system.css"
    "public/css/main.css"
)

for file in "${CSS_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ MISSING: $file"
        ((FAIL_COUNT++))
    fi
done
echo ""

# Test 3: JavaScript Files
echo "✅ Test 3: JavaScript Files Exist"
JS_FILES=(
    "public/js/global-search.js"
    "public/components/navigation-standard.html"
    "public/components/footer.html"
)

for file in "${JS_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ MISSING: $file"
        ((FAIL_COUNT++))
    fi
done
echo ""

# Test 4: Netlify Config
echo "✅ Test 4: Deployment Config"
if [ -f "netlify.toml" ]; then
    echo "  ✅ netlify.toml"
else
    echo "  ❌ MISSING: netlify.toml"
    ((FAIL_COUNT++))
fi
echo ""

# Test 5: Check for common issues
echo "✅ Test 5: Common Issues Check"

# Check for placeholder text
PLACEHOLDER_COUNT=$(grep -r "TODO" public/*.html 2>/dev/null | wc -l | tr -d ' ')
echo "  ℹ️  Found $PLACEHOLDER_COUNT TODO markers (acceptable if low)"

# Check for broken Supabase references
BAD_SUPABASE=$(grep -r "YOUR_SUPABASE_URL" public/*.html 2>/dev/null | wc -l | tr -d ' ')
if [ "$BAD_SUPABASE" -eq "0" ]; then
    echo "  ✅ No placeholder Supabase URLs"
else
    echo "  ⚠️  Found $BAD_SUPABASE placeholder Supabase URLs"
    ((FAIL_COUNT++))
fi
echo ""

# Final Result
echo "=================================="
echo ""
if [ $FAIL_COUNT -eq 0 ]; then
    echo "🎉 ALL TESTS PASSED! READY TO DEPLOY!"
    echo ""
    echo "Next steps:"
    echo "  git add ."
    echo "  git commit -m '🚀 Production ready'"
    echo "  git push origin main"
    echo ""
    exit 0
else
    echo "❌ $FAIL_COUNT TESTS FAILED!"
    echo ""
    echo "Fix the issues above before deploying."
    echo ""
    exit 1
fi

