#!/bin/bash
echo "📊 COMPLETE CODEBASE AUDIT"
echo "=========================="
echo ""

echo "🗂️ Directory Structure:"
find . -maxdepth 1 -type d ! -name "." ! -name ".git" ! -name "node_modules" | sort | while read dir; do
    count=$(find "$dir" -type f 2>/dev/null | wc -l)
    size=$(du -sh "$dir" 2>/dev/null | cut -f1)
    echo "  $dir: $count files ($size)"
done

echo ""
echo "📝 Documentation Files by Type:"
echo "  Root MD files: $(find . -maxdepth 1 -name "*.md" | wc -l)"
echo "  Archive MDs: $(find ./archive -name "*.md" 2>/dev/null | wc -l)"
echo "  Archived-bloat MDs: $(find ./archived-bloat -name "*.md" 2>/dev/null | wc -l)"
echo "  Docs folder MDs: $(find ./docs -name "*.md" 2>/dev/null | wc -l)"

echo ""
echo "🐍 Python Scripts by Location:"
find . -name "*.py" ! -path "./node_modules/*" ! -path "./.git/*" -exec dirname {} \; | sort | uniq -c | sort -rn | head -10

echo ""
echo "📊 JSON Files (Top Categories):"
find . -name "*.json" ! -path "./node_modules/*" ! -path "./.git/*" -exec dirname {} \; | sort | uniq -c | sort -rn | head -10

echo ""
echo "⚠️ Potential Cleanup Candidates:"
echo "  Backup directories: $(find . -maxdepth 1 -type d -name "*backup*" | wc -l)"
echo "  Archive directories: $(find . -maxdepth 1 -type d -name "*archive*" | wc -l)"
echo "  .old/.bak files: $(find . -name "*.old" -o -name "*.bak" -o -name "*-backup.*" | wc -l)"

