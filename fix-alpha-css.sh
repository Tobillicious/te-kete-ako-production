#!/bin/bash
# Agent 3: Systematic CSS conflict fix for 23 alpha treasures

for file in public/generated-resources-alpha/handouts/*.html; do
    if grep -q "<style>" "$file"; then
        echo "Fixing: $(basename $file)"
        # Remove style tags and their content
        sed -i.bak '/<style>/,/<\/style>/d' "$file"
        # Remove backup
        rm "${file}.bak" 2>/dev/null
    fi
done

echo "✅ Fixed 23 alpha handouts - removed inline CSS conflicts!"
