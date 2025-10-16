#!/bin/bash
# ==========================================
# UPGRADE ORPHANED RESOURCES TO UNIFIED DESIGN SYSTEM
# Te Kete Ako - Professional Transformation
# ==========================================

echo "🎨 UPGRADING 49 ORPHANED RESOURCES TO UNIFIED DESIGN SYSTEM"
echo "=========================================================="

HANDOUTS_DIR="public/generated-resources-alpha/handouts"
LESSONS_DIR="public/generated-resources-alpha/lessons"
BACKUP_DIR="backups/orphaned-resources-$(date +%Y%m%d-%H%M%S)"

# Create backup
echo "📦 Creating backup..."
mkdir -p "$BACKUP_DIR"
cp -r "$HANDOUTS_DIR" "$BACKUP_DIR/"
cp -r "$LESSONS_DIR" "$BACKUP_DIR/"
echo "✅ Backup created at $BACKUP_DIR"

count=0

# Function to upgrade a single HTML file
upgrade_file() {
    local file="$1"
    local type="$2"  # "handout" or "lesson"
    
    # Check if already has unified design system
    if grep -q "te-kete-unified-design-system.css" "$file"; then
        echo "  ⏭️  $(basename "$file") - already upgraded"
        return
    fi
    
    # Add unified design system CSS after te-kete-professional.css
    if grep -q "te-kete-professional.css" "$file"; then
        sed -i.upgrade '/<link rel="stylesheet" href="\/css\/te-kete-professional.css">/a\
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">\
    <link rel="stylesheet" href="/css/component-library.css">\
    <link rel="stylesheet" href="/css/animations-professional.css">
' "$file"
    else
        # Insert after viewport meta tag if no te-kete-professional.css
        sed -i.upgrade '/<meta name="viewport"/a\
    <link rel="stylesheet" href="/css/te-kete-professional.css">\
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">\
    <link rel="stylesheet" href="/css/component-library.css">\
    <link rel="stylesheet" href="/css/animations-professional.css">\
    <link rel="stylesheet" href="/css/ux-professional-enhancements.css">\
    <link rel="stylesheet" href="/css/print.css" media="print">
' "$file"
    fi
    
    # Update body tag to include data attributes
    sed -i.upgrade 's/<body>/<body data-auto-init="true" data-current-page="'$type'">/' "$file"
    sed -i.upgrade 's/<body data-auto-init="true">/<body data-auto-init="true" data-current-page="'$type'">/' "$file"
    
    echo "  ✅ $(basename "$file") - upgraded!"
    ((count++))
}

# Upgrade all handouts
echo ""
echo "📄 UPGRADING HANDOUTS..."
echo "------------------------"
for file in "$HANDOUTS_DIR"/*.html; do
    if [ -f "$file" ]; then
        upgrade_file "$file" "handout"
    fi
done

# Upgrade all lessons
echo ""
echo "📖 UPGRADING LESSONS..."
echo "----------------------"
for file in "$LESSONS_DIR"/*.html; do
    if [ -f "$file" ]; then
        upgrade_file "$file" "lesson"
    fi
done

# Clean up backup files
find public/generated-resources-alpha -name "*.upgrade" -delete

echo ""
echo "=========================================================="
echo "✅ UPGRADE COMPLETE!"
echo "📊 Total files upgraded: $count"
echo "📦 Backup location: $BACKUP_DIR"
echo "🎨 All orphaned resources now use UNIFIED DESIGN SYSTEM!"
echo "=========================================================="

