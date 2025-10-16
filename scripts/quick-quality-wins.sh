#!/bin/bash
# ==========================================
# QUICK QUALITY WINS - Automated Improvements
# Fixes: DOCTYPE, charset, viewport, lang attribute
# ==========================================

echo "🚀 APPLYING QUICK QUALITY IMPROVEMENTS"
echo "======================================"

count_fixed=0

# Function to fix a single HTML file
fix_html_file() {
    local file="$1"
    local tmpfile=$(mktemp)
    local needs_fix=0
    
    # Read file
    cat "$file" > "$tmpfile"
    
    # 1. Add DOCTYPE if missing (check first line)
    if ! head -1 "$tmpfile" | grep -q "DOCTYPE"; then
        echo "<!DOCTYPE html>" > "$file"
        cat "$tmpfile" >> "$file"
        cat "$file" > "$tmpfile"
        needs_fix=1
    fi
    
    # 2. Add charset if missing
    if ! grep -q 'charset="UTF-8"' "$tmpfile" && ! grep -q "charset='UTF-8'" "$tmpfile"; then
        sed -i.bak '/<head>/a\
    <meta charset="UTF-8">
' "$tmpfile"
        needs_fix=1
    fi
    
    # 3. Add viewport if missing
    if ! grep -q 'name="viewport"' "$tmpfile" && ! grep -q "name='viewport'" "$tmpfile"; then
        sed -i.bak '/<head>/a\
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
' "$tmpfile"
        needs_fix=1
    fi
    
    # 4. Add lang attribute if missing
    if grep -q '<html>' "$tmpfile" && ! grep -q 'lang=' "$tmpfile"; then
        sed -i.bak 's/<html>/<html lang="en">/' "$tmpfile"
        needs_fix=1
    fi
    
    # Apply changes if needed
    if [ $needs_fix -eq 1 ]; then
        cat "$tmpfile" > "$file"
        ((count_fixed++))
        echo "  ✅ $(basename $file)"
    fi
    
    # Cleanup
    rm -f "$tmpfile" "$tmpfile.bak"
}

# Process all HTML files
echo ""
echo "📄 Processing HTML files..."
echo ""

find public -name "*.html" -type f | while read file; do
    # Skip backups and certain directories
    if echo "$file" | grep -qE "(backup|node_modules|dist|\.git)"; then
        continue
    fi
    
    fix_html_file "$file"
    
    if [ $((count_fixed % 50)) -eq 0 ] && [ $count_fixed -gt 0 ]; then
        echo "  📊 Progress: $count_fixed files fixed..."
    fi
done

echo ""
echo "======================================"
echo "✅ QUICK QUALITY WINS COMPLETE!"
echo "📊 Files improved: $count_fixed"
echo "✨ Improvements:"
echo "   - DOCTYPE declarations added"
echo "   - UTF-8 charset ensured"
echo "   - Viewport meta tags added"
echo "   - Lang attributes set to English"
echo "======================================"

