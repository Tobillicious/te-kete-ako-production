#!/bin/bash
# Add External Resources to Handouts
# Kaiārahi Hoahoa - Supporting Teaching Excellence

echo "📄 Enriching Handouts with Resource Structure"
echo "============================================="

count=0
for file in public/units/y8-digital-kaitiakitanga/handouts/*.html public/units/y7-maths-algebra/resources/handout-*.html; do
    [ -f "$file" ] || continue
    
    if ! grep -q "external-resources\|External Resources" "$file"; then
        cp "$file" "$file.enrich-backup"
        
        # Add before closing tags
        if grep -q "</body>" "$file"; then
            sed -i.enrich '/<\/body>/i\
\
<section class="external-resources no-print">\
    <h2 class="section-title">\
        <span>🔗</span>\
        <span>Related Resources | Ngā Rauemi</span>\
    </h2>\
    <div class="resource-links">\
        <div class="resource-card">\
            <h3>🎓 Teaching Notes</h3>\
            <ul>\
                <li><button onclick="window.print()" class="btn-print">Print Handout</button></li>\
                <li><em>Ready for: Teacher implementation guides</em></li>\
            </ul>\
        </div>\
    </div>\
</section>\
' "$file"
            count=$((count + 1))
            echo "  ✅ $(basename $file)"
        fi
    fi
done

echo "============================================="
echo "✅ $count handouts enriched with resource structure!"
