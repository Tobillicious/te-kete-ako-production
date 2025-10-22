#!/bin/bash

# Batch add Similar Resources component to lessons that exist
# More robust approach with better error handling

COUNT=0
SUCCESS=0
SKIP=0

echo "🚀 Adding Similar Resources component to existing lessons..."
echo ""

# Find all lesson files that don't already have the component
find /Users/admin/Documents/te-kete-ako-clean/public/lessons -name "*.html" -type f ! -path "*/index.html" ! -path "*/herangi/index.html" | while read file; do
  
  COUNT=$((COUNT + 1))
  
  # Check if already has component
  if grep -q "graphrag-similar-resources" "$file" 2>/dev/null; then
    echo "⏭️  [$COUNT] Already has component: $(basename "$file")"
    continue
  fi
  
  # Check if has closing body tag
  if ! grep -q "</body>" "$file" 2>/dev/null; then
    echo "⚠️  [$COUNT] No </body> tag: $(basename "$file")"
    continue
  fi
  
  # Get relative path for data-resource-path
  REL_PATH=$(echo "$file" | sed 's|/Users/admin/Documents/te-kete-ako-clean/||')
  
  # Create component HTML
  COMPONENT="

<!-- 🔗 GraphRAG Similar Resources Component -->
<div id=\"similar-resources\" data-resource-path=\"/$REL_PATH\"></div>
<script src=\"/components/graphrag-similar-resources.html\"></script>

</body>"
  
  # Create backup
  cp "$file" "$file.bak"
  
  # Replace closing body tag with component + body
  sed -i '' "s|</body>|$COMPONENT|g" "$file"
  
  if [ $? -eq 0 ]; then
    echo "✅ [$COUNT] SUCCESS: $(basename "$file")"
    SUCCESS=$((SUCCESS + 1))
    rm "$file.bak"  # Remove backup on success
  else
    echo "❌ [$COUNT] FAILED: $(basename "$file")"
    mv "$file.bak" "$file"  # Restore backup on failure
  fi
  
  # Limit to 30 additions
  if [ $SUCCESS -ge 30 ]; then
    echo ""
    echo "✋ Reached target of 30 successful additions. Stopping."
    break
  fi
  
done

echo ""
echo "=========================================="
echo "📊 SUMMARY"
echo "=========================================="
echo "✅ Success: $SUCCESS lessons"
echo "⚠️  Skipped: $SKIP lessons"
echo "=========================================="

