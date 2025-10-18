#!/bin/bash
echo "🔍 THE REAL CODEBASE - All 90k+ Files"
echo "===================================================================="

echo -e "\n📊 TOTAL FILE COUNT:"
find . -type f | wc -l
echo "files in entire codebase"

echo -e "\n📁 BREAKDOWN BY TYPE:"

echo -e "\nHTML files (all directories):"
find . -name "*.html" -type f | wc -l

echo -e "\nPython files:"
find . -name "*.py" -type f | wc -l

echo -e "\nJavaScript files:"
find . -name "*.js" -type f | wc -l

echo -e "\nCSS files:"
find . -name "*.css" -type f | wc -l

echo -e "\nJSON files:"
find . -name "*.json" -type f | wc -l

echo -e "\nMarkdown files:"
find . -name "*.md" -type f | wc -l

echo -e "\n📂 MAJOR DIRECTORIES:"
echo ""
du -sh public/ 2>/dev/null | head -1
du -sh scripts/ 2>/dev/null | head -1
du -sh netlify/ 2>/dev/null | head -1
du -sh units/ 2>/dev/null | head -1
du -sh src/ 2>/dev/null | head -1
du -sh node_modules/ 2>/dev/null | head -1

echo -e "\n===================================================================="
echo "💡 This is the REAL scope - let's build the real deal"
