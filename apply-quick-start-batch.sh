#!/bin/bash
# Apply Quick Start to remaining lessons

TEMPLATE=$(cat quick-start-template.html)
COUNT=0

find public/lessons public/units -name "*.html" -type f ! -path "*/index.html" | while read file; do
  # Skip if already has it or file too small
  if ! grep -q "quick-start-guide" "$file" 2>/dev/null && [ $(wc -c < "$file" 2>/dev/null || echo 0) -gt 5000 ]; then
    # Find first <h1> and insert after
    if grep -q "<h1" "$file"; then
      # Use sed to insert after first h1 close tag
      sed -i.bak '0,/<\/h1>/{s|</h1>|</h1>\n\n'"$(echo "$TEMPLATE" | sed 's/|/\\|/g')"'\n\n|}' "$file" 2>/dev/null && {
        echo "✅ $(basename $file)"
        COUNT=$((COUNT + 1))
      }
    fi
    
    # Stop at 50
    [ $COUNT -ge 50 ] && break
  fi
done

echo ""
echo "✅ Added Quick Start to $COUNT more lessons"
