#!/bin/bash
# Batch Enrichment - Digital, Technology & STEM Handouts
# agent-12 - Batch 3 of systematic enrichment

HANDOUTS_DIR="public/handouts"

add_digital_resources() {
    local file=$1
    if ! grep -q "External Resources" "$file"; then
        sed -i.enrichbak3 '/<\/body>/i\
    <section class="external-resources no-print" style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); padding: 2rem; border-radius: 12px; margin: 3rem 0; border-left: 4px solid var(--color-info); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\
        <h2 style="color: var(--color-primary); margin-top: 0;"><span>🔗</span> <span>External Resources</span></h2>\
        <div style="display: grid; gap: 1rem;"><div style="background: white; padding: 1rem; border-radius: 8px;">\
            <h4 style="margin: 0 0 0.5rem; color: var(--color-primary);">💻 Digital \& Technology</h4>\
            <ul style="margin: 0; font-size: 0.95rem;">\
                <li><a href="https://www.tki.org.nz/r/ict_guide/" target="_blank">TKI: Digital Technologies</a></li>\
                <li><a href="https://www.netsafe.org.nz/" target="_blank">Netsafe NZ</a></li>\
                <li><a href="https://www.sciencelearn.org.nz/topics/technology" target="_blank">Science Learning Hub: Technology</a></li>\
            </ul></div></div></section>\
' "$file"
        echo "✅ Digital: $(basename $file)"
    fi
}

add_stem_resources() {
    local file=$1
    if ! grep -q "External Resources" "$file"; then
        sed -i.enrichbak3 '/<\/body>/i\
    <section class="external-resources no-print" style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); padding: 2rem; border-radius: 12px; margin: 3rem 0; border-left: 4px solid var(--color-info); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\
        <h2 style="color: var(--color-primary); margin-top: 0;"><span>🔗</span> <span>External Resources</span></h2>\
        <div style="display: grid; gap: 1rem;"><div style="background: white; padding: 1rem; border-radius: 8px;">\
            <h4 style="margin: 0 0 0.5rem; color: var(--color-primary);">🔬 STEM Resources</h4>\
            <ul style="margin: 0; font-size: 0.95rem;">\
                <li><a href="https://www.sciencelearn.org.nz/" target="_blank">Science Learning Hub</a></li>\
                <li><a href="https://www.tki.org.nz/r/science/" target="_blank">TKI: Science</a></li>\
                <li><a href="https://www.doc.govt.nz/nature/" target="_blank">DOC: Nature</a></li>\
            </ul></div></div></section>\
' "$file"
        echo "✅ STEM: $(basename $file)"
    fi
}

# Enrich digital/tech handouts
for file in $HANDOUTS_DIR/*{digital,technology,coding,computer,online,cyber,internet,app,software}*.html; do
    [ -f "$file" ] && add_digital_resources "$file"
done

# Enrich STEM handouts
for file in $HANDOUTS_DIR/*{stem,innovation,engineering,robotics,renewable,sustainable,energy,physics}*.html; do
    [ -f "$file" ] && add_stem_resources "$file"
done

echo "Batch 3 enrichment complete!"

