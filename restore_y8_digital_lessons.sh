#!/bin/bash
# RESTORE Y8 DIGITAL KAITIAKITANGA LESSONS FROM .BAK FILES
# Current: 10-line minified versions
# Target: 500+ line properly formatted versions

LESSON_DIR="public/units/y8-digital-kaitiakitanga/lessons"
BACKUP_DIR="backup_before_css_migration/units/y8-digital-kaitiakitanga/lessons"

echo "🔄 RESTORING Y8 DIGITAL KAITIAKITANGA LESSONS"
echo "=============================================="
echo ""

# Counter
restored=0

# Restore all lesson files
for bak_file in "$BACKUP_DIR"/*.bak; do
    if [ -f "$bak_file" ]; then
        filename=$(basename "$bak_file" .bak)
        target="$LESSON_DIR/$filename"
        
        echo "📝 Restoring: $filename"
        echo "   From: $bak_file ($(wc -l < "$bak_file") lines)"
        echo "   To:   $target ($(wc -l < "$target") lines)"
        
        # Copy backup to current location
        cp "$bak_file" "$target"
        
        ((restored++))
        echo "   ✅ Restored!"
        echo ""
    fi
done

echo "=============================================="
echo "✅ RESTORATION COMPLETE"
echo "   Lessons restored: $restored"
echo ""
echo "NEXT STEPS:"
echo "1. Remove inline styles (replace with CSS classes)"
echo "2. Fix duplicate component loading"
echo "3. Add professionalization-system.css"
echo "4. Test all lessons render correctly"
echo ""

