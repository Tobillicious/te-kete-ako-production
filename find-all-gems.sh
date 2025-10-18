#!/bin/bash
# Find ALL unique valuable content across all versions

echo "💎 COMPREHENSIVE GEM HUNT"
echo "═══════════════════════════════════════════════════════════════"

# Check for unique tools/games/activities in dist
echo ""
echo "🎮 INTERACTIVE TOOLS IN DIST/:"
find dist -maxdepth 2 -name "*game*.html" -o -name "*interactive*.html" -o -name "*generator*.html" | while read f; do
  basename "$f"
done | sort -u

echo ""
echo "📊 ASSESSMENT TOOLS IN DIST/:"
find dist -maxdepth 2 -name "*assessment*.html" -o -name "*rubric*.html" -o -name "*evaluation*.html" | while read f; do
  basename "$f"
done | sort -u

echo ""
echo "🎯 CURRICULUM PAGES IN DIST/:"
find dist -maxdepth 1 -name "curriculum-*.html" | while read f; do
  basename "$f"
done | sort

echo ""
echo "🌟 OTHER VALUABLE PAGES:"
find dist -maxdepth 1 -name "*.html" | while read f; do
  name=$(basename "$f")
  if [ ! -f "public/$name" ]; then
    size=$(wc -c < "$f")
    if [ $size -gt 5000 ]; then
      echo "  ⭐ $name ($size bytes)"
    fi
  fi
done

