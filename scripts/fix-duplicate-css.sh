#!/bin/bash
# Fix duplicate CSS links in generated-resources-alpha files
# Agent 2 - coordinating with team via MCP

echo "🔧 Fixing duplicate CSS links in 47 files..."

count=0
for file in public/generated-resources-alpha/**/*.html; do
  if [ -f "$file" ]; then
    # Create backup
    cp "$file" "$file.bak"
    
    # Remove duplicate CSS link lines (pattern matching)
    # Keep first CSS links, remove duplicates after </style>
    sed -i.tmp '/^[[:space:]]*<link rel="stylesheet" href="\/css\/print.css"/,/^[[:space:]]*<script src="\/js\/breadcrumbs.js"/{ 
      /<\/style>/,/<script/ {
        /<link rel="stylesheet"/d
        /<script src="\/js\/breadcrumbs/d
      }
    }' "$file" 2>/dev/null
    
    rm "$file.tmp" 2>/dev/null
    count=$((count+1))
    echo "Fixed: $file"
  fi
done

echo "✅ Fixed $count files"
echo "Team: Check git diff to verify improvements"

