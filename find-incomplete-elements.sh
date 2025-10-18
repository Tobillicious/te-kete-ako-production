#!/bin/bash
echo "🔍 FINDING INCOMPLETE ELEMENTS"
echo "===================================================================="

echo -e "\n📋 1. Empty or missing titles:"
grep -r "<title></title>\|<title>.*Untitled.*</title>" public/ --include="*.html" -l | head -10

echo -e "\n📋 2. Missing meta descriptions:"
grep -L 'meta name="description"' public/*.html | head -10

echo -e "\n📋 3. Broken image references:"
grep -r 'src=""\|src="#"' public/ --include="*.html" -l | head -10

echo -e "\n📋 4. Broken links:"
grep -r 'href="#"\|href=""' public/ --include="*.html" -l | head -10

echo -e "\n�� 5. Empty headings:"
grep -r "<h[1-6]></h[1-6]>\|<h[1-6]>\s*</h[1-6]>" public/ --include="*.html" -l | head -10

echo -e "\n📋 6. Commented out sections (may need completion):"
grep -r "<!-- TODO\|<!-- FIX" public/ --include="*.html" -l | head -10

echo -e "\n===================================================================="
echo "💡 Found incomplete elements - ready to complete them!"
