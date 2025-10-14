#!/bin/bash
# =================================================================
# MASTER CSS SYSTEMIZATION SCRIPT
# Kaiārahi Hoahoa - Guide of Design
# =================================================================
# Purpose: Systematically convert inline styles to CSS classes
# Scope: All lesson files across Te Kete Ako platform
# Impact: 136 lessons, ~17,659 inline styles to professional system
# =================================================================

echo "🎨 KAIĀRAHI HOAHOA - MASTER CSS SYSTEMIZATION"
echo "=============================================="
echo "Scope: Site-wide inline style conversion"
echo "Target: All lesson files using te-kete-professional.css"
echo ""

# Counter variables
total_files=0
total_before=0
total_after=0

# Process all lesson directories
lesson_dirs=(
    "public/units/walker-unit"
    "public/units/y8-critical-thinking"
    "public/units/unit-1-te-ao-maori/lessons"
    "public/units/y7-maths-algebra/lessons"
    "public/units/y7-science-ecosystems/lessons"
    "public/units/y8-digital-kaitiakitanga/lessons"
    "public/units/y9-maths-geometry-patterns/lessons"
    "public/units/y9-science-ecology/lessons"
    "public/y8-systems/lessons"
    "public/guided-inquiry-unit/lessons"
    "public/lessons"
)

# Standard CSS class conversion patterns
convert_file() {
    local file="$1"
    
    # Backup
    cp "$file" "$file.master-backup"
    
    # Apply all conversions
    sed -i.master \
        -e 's/<section class="cultural-integration" style="[^"]*">/<section class="cultural-integration te-kete-section cultural-section">/g' \
        -e 's/<div class="whakatauaki-section" style="[^"]*">/<div class="whakatauki-container">/g' \
        -e 's/<div class="whakataukī-section" style="[^"]*">/<div class="whakatauki-container">/g' \
        -e 's/<div style="background: rgba(241, 143, 1, 0\.1);[^"]*">/<div class="value-highlight">/g' \
        -e 's/<section class="external-resources[^"]*" style="[^"]*">/<section class="external-resources no-print">/g' \
        -e 's/<div class="resource-card" style="[^"]*">/<div class="resource-card">/g' \
        -e 's/style="padding: 0\.75rem 1\.5rem; background: var(--color-pounamu);[^"]*"/class="nav-btn"/g' \
        -e 's/style="padding: 0\.75rem 1\.5rem; background: var(--color-secondary);[^"]*"/class="nav-btn secondary"/g' \
        -e 's/<footer class="site-footer no-print" style="[^"]*">/<footer class="site-footer no-print">/g' \
        -e 's/<p style="font-style: italic; color:[^"]*;">/<p class="footer-quote">/g' \
        -e 's/<h2 style="color: var(--color-primary);[^"]*">/<h2 class="section-title">/g' \
        -e 's/<div class="ai-resources-highlight" style="[^"]*">/<div class="ai-resources-highlight">/g' \
        -e 's/<div class="stat-box" style="[^"]*">/<div class="stat-box">/g' \
        -e 's/<h3 class="assessment-tools" style="[^"]*">/<h3 class="assessment-tools">/g' \
        -e 's/<div class="assessment-card" style="[^"]*">/<div class="assessment-card">/g' \
        "$file"
}

# Process each directory
for dir in "${lesson_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "📁 Processing: $dir"
        file_count=0
        
        for file in "$dir"/*.html "$dir"/lesson-*.html; do
            [ -f "$file" ] || continue
            
            before=$(grep -c "style=" "$file" 2>/dev/null)
            if [ "$before" -gt 0 ]; then
                convert_file "$file"
                after=$(grep -c "style=" "$file" 2>/dev/null)
                
                total_files=$((total_files + 1))
                total_before=$((total_before + before))
                total_after=$((total_after + after))
                file_count=$((file_count + 1))
                
                printf "  %-50s %4d → %4d (-%d)\n" "$(basename $file)" "$before" "$after" "$((before - after))"
            fi
        done
        
        [ "$file_count" -gt 0 ] && echo "  Subtotal: $file_count files processed"
        echo ""
    fi
done

echo "=============================================="
echo "✅ MASTER CSS SYSTEMIZATION COMPLETE!"
echo ""
echo "Files Processed: $total_files"
echo "Before: $total_before inline styles"
echo "After: $total_after inline styles"
echo "Converted: $((total_before - total_after)) inline styles"
echo "Improvement: $((100 * (total_before - total_after) / total_before))%"
echo ""
echo "All backups saved with .master-backup extension"
echo "=============================================="
echo ""
echo "🎨 Kaiārahi Hoahoa - Guide of Design"
echo "Systematic Excellence Achieved! 🧺✨"


