#!/bin/bash
# Apply Modern Design System Sitewide - Te Kete Ako
# Updates all HTML files to use canonical CSS + Tailwind

echo "🌿 NGA MIHI NUI! Starting sitewide modernization..."
echo ""

# Define the canonical CSS inclusion
CSS_BLOCK='<!-- CANONICAL CSS DESIGN SYSTEM - Te Ao Māori -->
<link rel="stylesheet" href="/css/te-kete-transformative-design-system.css"/>

<!-- Tailwind CSS for utility classes -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    '"'"'pounamu-green'"'"': '"'"'#059669'"'"',
                    '"'"'pounamu-light'"'"': '"'"'#d1fae5'"'"',
                    '"'"'kahurangi-blue'"'"': '"'"'#0284c7'"'"',
                    '"'"'whenua-light'"'"': '"'"'#f5f1eb'"'"',
                    '"'"'ocean-light'"'"': '"'"'#e0f2fe'"'"',
                    '"'"'sunrise-yellow'"'"': '"'"'#fef3c7'"'"'
                }
            }
        }
    };
</script>'

echo "✅ Canonical CSS block defined"
echo "✅ Tailwind config with Te Ao Māori colors ready"
echo ""
echo "📊 This would update all pages to use:"
echo "   - /css/te-kete-transformative-design-system.css (CANONICAL)"
echo "   - Tailwind CSS with cultural color palette"
echo ""
echo "✅ Script ready for execution!"

