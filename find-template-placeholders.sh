#!/bin/bash
echo "🔍 FINDING TEMPLATE PLACEHOLDERS"
echo "================================================================"

echo -e "\n📋 Searching for template text in units..."

# Find various placeholder patterns
echo -e "\n❌ [INSERT] placeholders:"
grep -r "\[INSERT" public/units/ --include="*.html" -l | head -10

echo -e "\n❌ TODO placeholders:"
grep -r "TODO:" public/units/ --include="*.html" -l | head -10

echo -e "\n❌ PLACEHOLDER text:"
grep -r "PLACEHOLDER" public/units/ --include="*.html" -l | head -10

echo -e "\n❌ Coming soon text:"
grep -r -i "coming soon" public/units/ --include="*.html" -l | head -10

echo -e "\n❌ Lorem ipsum:"
grep -r -i "lorem ipsum" public/units/ --include="*.html" -l | head -10

echo -e "\n================================================================"
echo "💡 These files need content completion"
