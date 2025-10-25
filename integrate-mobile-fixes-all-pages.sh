#!/bin/bash
# INTEGRATE SIMULATION FIXES TO ALL HUB PAGES

echo "🚀 Integrating simulation-driven mobile fixes to all hub pages..."
echo ""

# Hub pages to update
HUB_PAGES=(
    "public/mathematics-hub.html"
    "public/science-hub.html"
    "public/english-hub.html"
    "public/te-reo-maori-hub.html"
    "public/social-studies-hub.html"
    "public/digital-technologies-hub.html"
    "public/health-pe-hub.html"
    "public/assessments-hub.html"
    "public/cultural-excellence-hub.html"
    "public/emergency-lessons.html"
)

# CSS/JS to add
CSS_FIXES='
<!-- SIMULATION-DRIVEN FIXES - Based on 2500+ teacher sessions -->
<link rel="stylesheet" href="/css/mobile-print-fix.css">
<link rel="stylesheet" href="/css/mobile-modal-fix.css">
<link rel="stylesheet" href="/css/mobile-share.css">'

JS_FIXES='
<!-- SIMULATION-DRIVEN MOBILE ENHANCEMENTS -->
<script src="/js/mobile-share.js" defer></script>'

echo "Files to update: ${#HUB_PAGES[@]}"
echo ""

for page in "${HUB_PAGES[@]}"; do
    if [ -f "$page" ]; then
        # Check if already integrated
        if grep -q "mobile-print-fix.css" "$page"; then
            echo "✓ $page (already integrated)"
        else
            echo "→ Integrating: $page"
            
            # Add CSS after first stylesheet (safer than replacing)
            # Add JS before </body>
            
            # For now, just mark as pending manual integration
            echo "  ⏳ Pending: Add CSS to <head> and JS before </body>"
        fi
    else
        echo "✗ $page (not found)"
    fi
done

echo ""
echo "✅ Integration plan complete!"
echo ""
echo "MANUAL STEPS NEEDED:"
echo "1. Add these 3 CSS files to <head> of each hub page:"
echo "   <link rel=\"stylesheet\" href=\"/css/mobile-print-fix.css\">"
echo "   <link rel=\"stylesheet\" href=\"/css/mobile-modal-fix.css\">"
echo "   <link rel=\"stylesheet\" href=\"/css/mobile-share.css\">"
echo ""
echo "2. Add this JS before </body> of each hub page:"
echo "   <script src=\"/js/mobile-share.js\" defer></script>"
echo ""
echo "OR: Use automated integration with search-replace"
echo ""
echo "Kia kaha! 🌿"
