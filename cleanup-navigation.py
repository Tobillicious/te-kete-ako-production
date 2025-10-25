#!/bin/bash
# Navigation Cleanup Script
# Remove redundant navigation files after consolidation

echo "🧹 Cleaning up redundant navigation files..."

# Files to remove (backups first)
declare -a files_to_remove=(
    "public/components/navigation-standard.html.bak"
    "public/components/navigation-mega-menu.html.bak"
    "public/components/navigation-ai.html.bak"
    "public/components/navigation-hegelian-synthesis.html.bak"
    "public/components/navigation-year-dropdown.html.bak"
    "public/components/navigation-standard.html.graphrag-backup"
)

# Remove backup files
for file in "${files_to_remove[@]}"; do
    if [ -f "$file" ]; then
        rm "$file"
        echo "✅ Removed: $file"
    fi
done

echo ""
echo "📋 RECOMMENDED: Manual review of these files before deletion:"
echo "   - navigation-standard.html (keep as backup)"
echo "   - navigation-mega-menu.html (keep as backup)"
echo "   - navigation-ai.html (keep as backup)"
echo "   - navigation-hegelian-synthesis.html (keep as backup)"
echo "   - navigation-year-dropdown.html (integrated into unified)"
echo ""
echo "🔄 Next steps:"
echo "   1. Test navigation-unified.html thoroughly"
echo "   2. Update all remaining HTML files to use unified navigation"
echo "   3. Remove old navigation files only after full testing"
echo "   4. Update documentation to reflect new navigation system"
echo ""
echo "🌿 Navigation consolidation complete!"
