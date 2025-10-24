#!/bin/bash
# Disable GraphRAG Connection Counter Sitewide
# This script comments out the connection counter on all hub pages

echo "🔧 Disabling GraphRAG Connection Counter sitewide..."

# List of all hub files
HUB_FILES=(
    "public/social-studies-hub.html"
    "public/te-ao-maori-hub.html"
    "public/te-reo-maori-hub.html"
    "public/reading-hub.html"
    "public/writing-hub.html"
    "public/year-7-hub.html"
    "public/resource-hub.html"
    "public/student-success-hub.html"
    "public/teacher-feedback-hub.html"
    "public/writers-toolkit-hub.html"
    "public/graphrag-hub.html"
)

for file in "${HUB_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  Processing: $file"
        sed -i.bak 's|<script src="/js/graphrag-connection-counter.js"></script>|<!-- GraphRAG Connection Counter - DISABLED FOR END USERS -->\n<!-- <script src="/js/graphrag-connection-counter.js"></script> -->|g' "$file"
        rm -f "$file.bak"
    else
        echo "  ⚠️  Not found: $file"
    fi
done

echo "✅ GraphRAG Counter disabled on all hub pages!"
echo ""
echo "Remaining GraphRAG features:"
echo "- Still accessible in /admin/ dashboards"
echo "- Still accessible in /discovery-tools.html"
echo "- Hidden from end users on main site"

