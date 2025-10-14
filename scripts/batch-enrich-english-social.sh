#!/bin/bash
# Batch Enrichment - English & Social Studies Handouts
# agent-12 - Continuing systematic enrichment

HANDOUTS_DIR="public/handouts"

# Function to add English/Literacy resources
add_english_resources() {
    local file=$1
    if ! grep -q "External Resources" "$file"; then
        sed -i.enrichbak2 '/<\/body>/i\
    <section class="external-resources no-print" style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); padding: 2rem; border-radius: 12px; margin: 3rem 0; border-left: 4px solid var(--color-info); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\
        <h2 style="color: var(--color-primary); margin-top: 0;"><span>🔗</span> <span>External Resources</span></h2>\
        <div style="display: grid; gap: 1rem;"><div style="background: white; padding: 1rem; border-radius: 8px;">\
            <h4 style="margin: 0 0 0.5rem; color: var(--color-primary);">📚 English & Literacy</h4>\
            <ul style="margin: 0; font-size: 0.95rem;">\
                <li><a href="https://literacyonline.tki.org.nz/" target="_blank">Literacy Online</a> - NZ reading resources</li>\
                <li><a href="https://www.tki.org.nz/r/english/" target="_blank">TKI: English</a> - Curriculum support</li>\
                <li><a href="https://www.readingeggs.co.nz/" target="_blank">Reading Eggs NZ</a> - Learning platform</li>\
            </ul></div></div></section>\
' "$file"
        echo "✅ English: $(basename $file)"
    fi
}

# Function to add Social Studies resources
add_social_resources() {
    local file=$1
    if ! grep -q "External Resources" "$file"; then
        sed -i.enrichbak2 '/<\/body>/i\
    <section class="external-resources no-print" style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); padding: 2rem; border-radius: 12px; margin: 3rem 0; border-left: 4px solid var(--color-info); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\
        <h2 style="color: var(--color-primary); margin-top: 0;"><span>🔗</span> <span>External Resources</span></h2>\
        <div style="display: grid; gap: 1rem;"><div style="background: white; padding: 1rem; border-radius: 8px;">\
            <h4 style="margin: 0 0 0.5rem; color: var(--color-primary);">🌏 Social Studies</h4>\
            <ul style="margin: 0; font-size: 0.95rem;">\
                <li><a href="https://nzhistory.govt.nz/" target="_blank">NZ History</a> - Official history resources</li>\
                <li><a href="https://www.tki.org.nz/r/social_sciences/" target="_blank">TKI: Social Sciences</a> - Teaching resources</li>\
                <li><a href="https://teara.govt.nz/" target="_blank">Te Ara</a> - NZ Encyclopedia</li>\
            </ul></div></div></section>\
' "$file"
        echo "✅ Social: $(basename $file)"
    fi
}

# Enrich English/Writing handouts
for file in $HANDOUTS_DIR/*{writing,reading,comprehension,english,literacy,authors,vocabulary}*.html; do
    [ -f "$file" ] && add_english_resources "$file"
done

# Enrich Social Studies handouts
for file in $HANDOUTS_DIR/*{history,government,civic,democracy,politics,society}*.html; do
    [ -f "$file" ] && add_social_resources "$file"
done

echo "Second batch enrichment complete!"

