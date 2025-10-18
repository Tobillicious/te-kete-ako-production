#!/bin/bash
echo "🔍 CHECKING PRODUCTION BUILD READINESS"
echo "================================================================"

echo -e "\n📋 1. Checking for HTML parsing issues..."
# Check for malformed HTML
echo "Checking for unclosed tags..."
grep -r "<script" public/ --include="*.html" | grep -v "</script>" | grep -v "src=" | wc -l

echo -e "\n📋 2. Checking script tags for type=module..."
echo "Scripts without type attribute:"
grep -r "<script" public/*.html | grep -v "type=" | grep -v "</script>" | wc -l

echo -e "\n📋 3. Checking for inline scripts that need modules..."
echo "Inline scripts found:"
grep -r "<script>" public/*.html | wc -l

echo -e "\n📋 4. Checking package.json build config..."
if [ -f "package.json" ]; then
    echo "✅ package.json exists"
    grep -A 5 "\"build\"" package.json
else
    echo "⚠️  No package.json found"
fi

echo -e "\n📋 5. Checking vite.config.js..."
if [ -f "vite.config.js" ]; then
    echo "✅ vite.config.js exists"
    head -20 vite.config.js
else
    echo "⚠️  No vite.config.js found"
fi

echo -e "\n================================================================"
echo "💡 Production build status check complete"
