#!/bin/bash
# Kaitiaki Whakawhitinga - Systematic ARIA role="main" Addition
# Fixes WCAG 4.1.2 violation across Te Kete Ako platform
# Agent-9 - October 14, 2025

echo "🌉 Kaitiaki Whakawhitinga - Adding role='main' to <main> elements"
echo "=================================================================="

BASE_DIR="/Users/admin/Documents/te-kete-ako-clean/public"
COUNT=0
FIXED=0

# Find all HTML files with <main> but missing role="main"
find "$BASE_DIR" -name "*.html" -type f | while read file; do
    COUNT=$((COUNT + 1))
    
    # Check if file has <main> without role="main"
    if grep -q '<main' "$file" && ! grep -q 'role="main"' "$file" && ! grep -q "role='main'" "$file"; then
        echo "  Fixing: $(basename "$file")"
        
        # Add role="main" to <main> tags
        # Handle various formats: <main>, <main class="...">, <main id="...">
        sed -i '' 's/<main\([^>]*\)>/<main role="main"\1>/g' "$file"
        
        FIXED=$((FIXED + 1))
    fi
done

echo "=================================================================="
echo "✅ Complete! Fixed $FIXED files"
echo "🌉 Kaitiaki Whakawhitinga - ARIA landmarks improved!"

