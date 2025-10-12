#!/bin/bash
# Fix malformed HTML in generated-resources-alpha handouts
# Add missing <style> tags

cd "$(dirname "$0")"

FILES=(
"public/generated-resources-alpha/handouts/algebraic-thinking-in-traditional-māori-games.html"
"public/generated-resources-alpha/handouts/biotechnology-ethics-through-māori-worldview.html"
"public/generated-resources-alpha/handouts/calculus-applications-in-environmental-modeling.html"
"public/generated-resources-alpha/handouts/chromebook-optimized-mobile-learning-guide.html"
"public/generated-resources-alpha/handouts/coding-projects-inspired-by-māori-patterns.html"
"public/generated-resources-alpha/handouts/cultural-safety-checklists-for-classroom-discussions.html"
"public/generated-resources-alpha/handouts/data-visualization-of-cultural-demographics.html"
"public/generated-resources-alpha/handouts/financial-literacy-with-māori-economic-principles.html"
"public/generated-resources-alpha/handouts/food-security-through-traditional-knowledge-systems.html"
"public/generated-resources-alpha/handouts/geometric-patterns-in-māori-art-and-architecture.html"
"public/generated-resources-alpha/handouts/global-citizenship-with-tangata-whenua-perspective.html"
"public/generated-resources-alpha/handouts/information-literacy-in-the-digital-age.html"
"public/generated-resources-alpha/handouts/leadership-development-through-cultural-values.html"
"public/generated-resources-alpha/handouts/mathematical-modeling-of-ecological-systems.html"
"public/generated-resources-alpha/handouts/ncea-level-1-literacy-and-numeracy-must-knows.html"
"public/generated-resources-alpha/handouts/probability-and-chance-in-māori-games.html"
"public/generated-resources-alpha/handouts/public-speaking-with-cultural-confidence.html"
"public/generated-resources-alpha/handouts/social-media-and-cultural-identity.html"
"public/generated-resources-alpha/handouts/statistical-analysis-of-treaty-settlement-data.html"
"public/generated-resources-alpha/handouts/sustainable-energy-solutions-from-traditional-knowledge.html"
"public/generated-resources-alpha/handouts/te-reo-maths-glossary-key-terms-in-māori-and-english.html"
"public/generated-resources-alpha/handouts/visual-arts-analysis-with-cultural-context.html"
"public/generated-resources-alpha/handouts/workplace-readiness-with-cultural-competency.html"
"public/generated-resources-alpha/handouts/year-9-starter-pack-essential-skills-for-high-school-success.html"
)

echo "🔧 Fixing malformed HTML in generated-resources-alpha handouts..."
echo "Adding missing <style> tags to 24 files..."
echo ""

FIXED=0
FAILED=0

for file in "${FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ File not found: $file"
        ((FAILED++))
        continue
    fi
    
    # Check if file already has <style> tag
    if grep -q "<style>" "$file"; then
        echo "✅ Already fixed: $(basename "$file")"
        continue
    fi
    
    # Create temp file
    TEMP_FILE="${file}.tmp"
    
    # Process the file
    # Find the line with print.css and add <style> after it
    # Find the last } before </head> and add </style> after it
    
    awk '
    /<link rel="stylesheet" href="\/css\/print.css"/ {
        print
        print "    <style>"
        next
    }
    /<\/head>/ {
        print "    </style>"
        print
        next
    }
    { print }
    ' "$file" > "$TEMP_FILE"
    
    # Replace original file
    mv "$TEMP_FILE" "$file"
    
    echo "✅ Fixed: $(basename "$file")"
    ((FIXED++))
done

echo ""
echo "📊 Summary:"
echo "   Fixed: $FIXED files"
echo "   Failed: $FAILED files"
echo ""
echo "🎉 All handouts should now display correctly!"

