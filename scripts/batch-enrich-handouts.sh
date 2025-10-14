#!/bin/bash
# Batch Handout Enrichment Script
# agent-12 - Systematic external resources addition

HANDOUTS_DIR="public/handouts"

# Function to add external resources before </body>
add_resources() {
    local file=$1
    local category=$2
    
    if ! grep -q "External Resources" "$file"; then
        sed -i.enrichbak '/<\/body>/i\
    <section class="external-resources no-print" style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); padding: 2rem; border-radius: 12px; margin: 3rem 0; border-left: 4px solid var(--color-info); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\
        <h2 style="color: var(--color-primary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">\
            <span>🔗</span> <span>External Resources</span>\
        </h2>\
        <div style="display: grid; gap: 1rem;">\
            <div style="background: white; padding: 1rem; border-radius: 8px;">\
                <h4 style="margin: 0 0 0.5rem; color: var(--color-primary);">'"$category"'</h4>\
                <ul style="margin: 0; font-size: 0.95rem;">\
                    <li><a href="https://www.tki.org.nz/" target="_blank">TKI Resources</a></li>\
                    <li><a href="https://teara.govt.nz/" target="_blank">Te Ara Encyclopedia</a></li>\
                </ul>\
            </div>\
        </div>\
    </section>\
' "$file"
        echo "✅ Enriched: $(basename $file)"
    fi
}

# Enrich mathematics handouts
for file in $HANDOUTS_DIR/*algebra*.html $HANDOUTS_DIR/*probability*.html $HANDOUTS_DIR/*statistics*.html; do
    [ -f "$file" ] && add_resources "$file" "📐 Mathematics Resources"
done

# Enrich science handouts  
for file in $HANDOUTS_DIR/*ecosystem*.html $HANDOUTS_DIR/*biology*.html $HANDOUTS_DIR/*chemistry*.html; do
    [ -f "$file" ] && add_resources "$file" "🔬 Science Resources"
done

# Enrich cultural handouts
for file in $HANDOUTS_DIR/*māori*.html $HANDOUTS_DIR/*maori*.html $HANDOUTS_DIR/*cultural*.html; do
    [ -f "$file" ] && add_resources "$file" "🌿 Cultural Resources"
done

echo "Batch enrichment complete!"

