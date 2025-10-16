#!/bin/bash

echo "🎯 STANDARDIZING NAVIGATION ACROSS ALL PAGES"
echo "============================================="

# Define the standard navigation component
STANDARD_NAV="
    <!-- Professional Mega Menu Navigation -->
    <div id=\"beautiful-nav-container\"></div>
    <script>
        fetch('/components/navigation-mega-menu.html')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>
"

# Function to standardize a file
standardize_navigation() {
    FILE_PATH=$1
    echo "  🔧 Standardizing: $FILE_PATH"
    
    # Remove old navigation containers and scripts
    sed -i '' '/<div id="professional-nav-container"><\/div>/d' "$FILE_PATH"
    sed -i '' '/<div id="beautiful-nav-container"><\/div>/d' "$FILE_PATH"
    sed -i '' '/fetch.*professional-navigation\.html/,/<\/script>/d' "$FILE_PATH"
    sed -i '' '/fetch.*navigation-mega-menu\.html/,/<\/script>/d' "$FILE_PATH"
    sed -i '' '/fetch.*navigation-header\.html/,/<\/script>/d' "$FILE_PATH"
    
    # Remove old header divs
    sed -i '' '/<div id="header-next-level"/d' "$FILE_PATH"
    
    # Add standard navigation after <body> tag
    sed -i '' "/<body[^>]*>/a\\
$STANDARD_NAV" "$FILE_PATH"
}

echo "📄 Processing main pages..."
standardize_navigation "public/index.html"
standardize_navigation "public/teacher-dashboard.html"
standardize_navigation "public/about.html"
standardize_navigation "public/lessons.html"
standardize_navigation "public/handouts.html"
standardize_navigation "public/units.html"
standardize_navigation "public/students.html"
standardize_navigation "public/teachers.html"

echo "📄 Processing generated resources..."
standardize_navigation "public/generated-resources-alpha/index.html"
standardize_navigation "public/generated-resources-alpha/handouts/index.html"
standardize_navigation "public/generated-resources-alpha/lessons/index.html"

echo "📄 Processing unit pages..."
for file in public/units/*/index.html; do
    if [ -f "$file" ]; then
        standardize_navigation "$file"
    fi
done

echo "📄 Processing lesson pages..."
for file in public/units/*/lessons/*.html; do
    if [ -f "$file" ]; then
        standardize_navigation "$file"
    fi
done

echo "📄 Processing handout pages..."
for file in public/generated-resources-alpha/handouts/*.html; do
    if [ -f "$file" ]; then
        standardize_navigation "$file"
    fi
done

for file in public/generated-resources-alpha/lessons/*.html; do
    if [ -f "$file" ]; then
        standardize_navigation "$file"
    fi
done

echo ""
echo "============================================="
echo "✅ NAVIGATION STANDARDIZATION COMPLETE!"
echo "🎯 All pages now use: navigation-mega-menu.html"
echo "🔧 Standardized navigation across all pages"
echo "============================================="
