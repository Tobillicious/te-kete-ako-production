#!/bin/bash
# Rename DEMO files to PRESENTATION files
# Prevents agent confusion about demo vs production

echo "════════════════════════════════════════════════════"
echo "📝 RENAMING DEMO FILES → PRESENTATION FILES"
echo "════════════════════════════════════════════════════"
echo ""

# Function to safely rename
rename_file() {
    old_name="$1"
    new_name="$2"
    
    if [ -f "$old_name" ]; then
        echo "✅ Renaming: $old_name"
        echo "        → $new_name"
        mv "$old_name" "$new_name"
    else
        echo "⏭️  Skipped: $old_name (not found)"
    fi
    echo ""
}

# Rename demo files
rename_file "DEMO_FLOW_SCRIPT.md" "OCTOBER_22_PRESENTATION_SCRIPT.md"
rename_file "DEMO_STATISTICS.md" "PRODUCT_STATISTICS_FOR_PRESENTATION.md"
rename_file "DEMO_CHECKLIST_COMPREHENSIVE.md" "OCTOBER_22_MEETING_PREPARATION.md"
rename_file "DEMO_SHOWCASE_LESSONS.md" "SHOWCASE_LESSONS_TO_HIGHLIGHT.md"
rename_file "BACKUP_DEMO_PLAN.md" "PRESENTATION_BACKUP_PLANS.md"
rename_file "DEMO_FLOW_TESTING.md" "PRESENTATION_REHEARSAL_NOTES.md"
rename_file "DEMO_READY_FINAL.md" "PRODUCTION_READY_OCT_22.md"
rename_file "DEMO_READY_NOW.md" "PRODUCTION_READY_NOW.md"
rename_file "DEMO_READY_UNITS.md" "PRODUCTION_READY_UNITS.md"

echo "════════════════════════════════════════════════════"
echo "✅ RENAMING COMPLETE!"
echo "════════════════════════════════════════════════════"
echo ""
echo "📝 Summary:"
echo "  - 'DEMO' files renamed to 'PRESENTATION' or 'OCTOBER_22'"
echo "  - Prevents agent confusion"
echo "  - ONE production product (not demo vs production)"
echo ""
echo "🎯 Result: Clarity for all future agents! 🧺✨"
echo "════════════════════════════════════════════════════"

