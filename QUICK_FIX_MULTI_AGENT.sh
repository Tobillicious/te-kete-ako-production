#!/bin/bash

# ================================================================
# QUICK FIX: Restore Multi-Agent Access
# ================================================================
# This script guides you through fixing multi-agent coordination
# ================================================================

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🚨  MULTI-AGENT ACCESS FIX  🚨                           ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Recent security fix broke multi-agent coordination."
echo "This will restore access for all 12 agents."
echo ""

# Step 1: Diagnose
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 1: DIAGNOSE CURRENT STATUS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if command -v python3 &> /dev/null; then
    python3 execute-agent-access-fix.py
    DIAGNOSIS_EXIT=$?
else
    echo "❌ Python3 not found. Skipping diagnosis."
    DIAGNOSIS_EXIT=1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 2: APPLY FIX"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ $DIAGNOSIS_EXIT -eq 0 ]; then
    echo "🎉 All tables already accessible!"
    echo "   No fix needed."
    echo ""
    exit 0
fi

echo "⚠️  Multi-agent access is broken. Fix required."
echo ""
echo "📋 TO FIX:"
echo ""
echo "   1. Open Supabase Dashboard:"
echo "      https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql"
echo ""
echo "   2. Click 'New Query'"
echo ""
echo "   3. Copy and paste THIS FILE:"
echo "      supabase/migrations/20251020_restore_multi_agent_access.sql"
echo ""
echo "   4. Click 'Run' (or press Cmd+Enter)"
echo ""
echo "   5. Wait for success message (15-30 seconds)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Offer to open files
echo "Would you like to:"
echo "  1) Open migration SQL file (to copy)"
echo "  2) Open Supabase Dashboard (in browser)"
echo "  3) Skip and do it manually"
echo ""
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        if command -v code &> /dev/null; then
            code supabase/migrations/20251020_restore_multi_agent_access.sql
            echo "✅ Opened in VS Code"
        elif command -v open &> /dev/null; then
            open supabase/migrations/20251020_restore_multi_agent_access.sql
            echo "✅ Opened with default editor"
        else
            echo "📋 File location:"
            echo "   $(pwd)/supabase/migrations/20251020_restore_multi_agent_access.sql"
        fi
        ;;
    2)
        if command -v open &> /dev/null; then
            open "https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql"
            echo "✅ Opened Supabase Dashboard in browser"
        else
            echo "📋 Dashboard URL:"
            echo "   https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql"
        fi
        ;;
    3)
        echo "📋 Manual fix instructions in: APPLY_MULTI_AGENT_FIX_NOW.md"
        ;;
    *)
        echo "📋 Manual fix instructions in: APPLY_MULTI_AGENT_FIX_NOW.md"
        ;;
esac

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 3: VERIFY FIX"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "After applying the fix in Supabase Dashboard, run:"
echo ""
echo "   python3 test-multi-agent-access.py"
echo ""
echo "Expected: ✅ MULTI-AGENT ACCESS FULLY OPERATIONAL"
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Need help? See: APPLY_MULTI_AGENT_FIX_NOW.md             ║"
echo "╚════════════════════════════════════════════════════════════╝"

