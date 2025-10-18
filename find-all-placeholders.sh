#!/bin/bash
echo "🔍 COMPREHENSIVE PLACEHOLDER HUNT"
echo "===================================================================="

echo -e "\n📋 1. Searching for placeholder text patterns..."

echo -e "\n❌ TODO markers:"
grep -r "TODO" public/ --include="*.html" -l | head -20

echo -e "\n❌ FIXME markers:"
grep -r "FIXME" public/ --include="*.html" -l | head -10

echo -e "\n❌ [Placeholder] or [INSERT]:"
grep -r "\[.*INSERT.*\]" public/ --include="*.html" -l | head -10
grep -r "\[.*PLACEHOLDER.*\]" public/ --include="*.html" -l | head -10

echo -e "\n❌ Lorem ipsum:"
grep -ri "lorem ipsum" public/ --include="*.html" -l | head -10

echo -e "\n❌ Coming soon text:"
grep -ri "coming soon" public/ --include="*.html" -l | head -10

echo -e "\n❌ Under construction:"
grep -ri "under construction" public/ --include="*.html" -l | head -10

echo -e "\n❌ TBD or To be determined:"
grep -ri "TBD\|to be determined" public/ --include="*.html" -l | head -10

echo -e "\n❌ Example text:"
grep -r "This is an example" public/ --include="*.html" -l | head -10

echo -e "\n❌ Test content:"
grep -ri "test content\|sample content" public/ --include="*.html" -l | head -10

echo -e "\n===================================================================="
echo "💡 Found all placeholder patterns - time to fix them!"
