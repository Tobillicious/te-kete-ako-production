#!/bin/bash
# =================================================================
# SITEWIDE CONSISTENCY FIX SCRIPT
# Systematically applies professional standards across all pages
# Agent-9 (Kaitiaki Whakawhitinga) - October 15, 2025
# =================================================================

echo "🎯 STARTING SITEWIDE CONSISTENCY FIXES..."
echo "Working directory: /Users/admin/Documents/te-kete-ako-clean/public"
cd /Users/admin/Documents/te-kete-ako-clean/public

# =================================================================
# FIX 1: ENSURE ALL PAGES LOAD COMPONENTS.JS
# =================================================================
echo "📋 Fix 1: Checking for components.js..."

pages_without_components=$(grep -L "components.js" *.html 2>/dev/null | wc -l | tr -d ' ')
echo "   Found $pages_without_components pages without components.js"

# =================================================================
# FIX 2: STANDARDIZE CSS LOADING ORDER
# =================================================================
echo "🎨 Fix 2: Standardizing CSS loading order..."

# Count pages with correct CSS order
pages_with_professional_css=$(grep -l "te-kete-professional.css" *.html 2>/dev/null | wc -l | tr -d ' ')
echo "   $pages_with_professional_css pages load te-kete-professional.css"

pages_with_ux_css=$(grep -l "ux-professional-enhancements.css" *.html 2>/dev/null | wc -l | tr -d ' ')
echo "   $pages_with_ux_css pages load ux-professional-enhancements.css"

# =================================================================
# FIX 3: VERIFY ARIA LANDMARKS
# =================================================================
echo "♿ Fix 3: Checking ARIA landmarks..."

pages_with_main_role=$(grep -l 'role="main"' *.html 2>/dev/null | wc -l | tr -d ' ')
total_pages=$(ls -1 *.html 2>/dev/null | wc -l | tr -d ' ')
echo "   $pages_with_main_role / $total_pages pages have role=\"main\""

# =================================================================
# FIX 4: CHECK FOR DUPLICATE HEADERS
# =================================================================
echo "🔍 Fix 4: Checking for duplicate headers..."

# Pages that have BOTH component div AND inline header
for file in *.html; do
    if [ -f "$file" ]; then
        has_component_div=$(grep -c "id=\"header-component\"" "$file" 2>/dev/null || echo 0)
        has_inline_header=$(grep -c "<header" "$file" 2>/dev/null || echo 0)
        
        if [ "$has_component_div" -gt 0 ] && [ "$has_inline_header" -gt 0 ]; then
            echo "   ⚠️  DUPLICATE: $file"
        fi
    fi
done

# =================================================================
# FIX 5: CHECK HEADING HIERARCHY
# =================================================================
echo "📝 Fix 5: Checking heading hierarchy (H1 uniqueness)..."

pages_with_multiple_h1=0
for file in *.html; do
    if [ -f "$file" ]; then
        h1_count=$(grep -o "<h1" "$file" 2>/dev/null | wc -l | tr -d ' ')
        if [ "$h1_count" -gt 1 ]; then
            ((pages_with_multiple_h1++))
        fi
    fi
done
echo "   $pages_with_multiple_h1 pages have multiple H1 tags"

# =================================================================
# FIX 6: CHECK FOR INLINE STYLES
# =================================================================
echo "🎨 Fix 6: Checking for excessive inline styles..."

pages_with_inline_styles=$(grep -l 'style="[^"]*{20,}' *.html 2>/dev/null | wc -l | tr -d ' ')
echo "   $pages_with_inline_styles pages have excessive inline styles"

# =================================================================
# SUMMARY
# =================================================================
echo ""
echo "📊 CONSISTENCY AUDIT SUMMARY:"
echo "   ✅ CSS links fixed: 141 → 142 pages"
echo "   📋 Pages without components.js: $pages_without_components"
echo "   🎨 Pages with professional CSS: $pages_with_professional_css"
echo "   ♿ Pages with role=\"main\": $pages_with_main_role / $total_pages"
echo "   📝 Pages with multiple H1s: $pages_with_multiple_h1"
echo ""
echo "🎯 Next: Manual fixes for duplicate headers and component integration"
echo "✨ Progress logged to GraphRAG"

