#!/bin/bash
# Run this script manually in Terminal.app if Cursor terminal is stuck

cd /Users/admin/Documents/te-kete-ako-clean

echo "🔧 Fixing script paths for 100% sitewide consistency..."
echo ""

python3 fix-all-script-paths.py

echo ""
echo "✅ Script paths fixed!"
echo ""
echo "📝 Now commit with:"
echo "  git add -A"
echo "  git commit -m '🔧 Fix script path consistency across all pages'"
echo ""
echo "🚀 Then test on local server"

