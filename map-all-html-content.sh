#!/bin/bash
echo "🗺️ MAPPING ALL 8,306 HTML FILES - The Real Educational Content"
echo "===================================================================="

echo -e "\n📊 HTML FILES BY DIRECTORY:"
echo ""

for dir in public/ units/ src/ backup_before_css_migration/ backup_before_minification/ archive/ development/ project/ data/; do
    if [ -d "$dir" ]; then
        COUNT=$(find "$dir" -name "*.html" -type f 2>/dev/null | wc -l | tr -d ' ')
        if [ "$COUNT" -gt 0 ]; then
            SIZE=$(du -sh "$dir" 2>/dev/null | cut -f1)
            echo "$dir: $COUNT HTML files ($SIZE)"
        fi
    fi
done

echo -e "\n📚 EDUCATIONAL CONTENT BREAKDOWN:"
echo ""

echo -n "Lessons: "
find . -path "*/lessons/*.html" -type f | wc -l

echo -n "Handouts: "
find . -path "*/handouts/*.html" -type f | wc -l

echo -n "Units: "
find . -path "*/units/*.html" -type f | wc -l

echo -n "Assessments: "
find . -path "*/assessment*.html" -type f | wc -l

echo -n "Games: "
find . -path "*/games/*.html" -type f | wc -l

echo -e "\n===================================================================="
echo "💡 This is ALL the educational content - let's systematically improve it"
