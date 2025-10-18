#!/bin/bash
echo "🎯 CHECKING ALL FEATURED UNITS - One by One"
echo "===================================================================="

check_unit() {
    local dir=$1
    local name=$2
    
    echo ""
    echo "📦 $name"
    
    if [ -f "$dir/index.html" ]; then
        echo -n "   ✓ Has index page: ✅   "
        
        # Count lessons
        LESSONS=$(find "$dir" -name "*.html" -type f | grep -i lesson | wc -l | tr -d ' ')
        echo "Lessons: $LESSONS"
        
        # Check for placeholders in index
        echo -n "   ✓ No placeholders: "
        grep -qi "coming soon\|TODO\|\[INSERT\]" "$dir/index.html" && echo "❌ FOUND" || echo "✅"
        
        # Check for meta description
        echo -n "   ✓ Has meta: "
        grep -q 'meta name="description"' "$dir/index.html" && echo "✅" || echo "❌ MISSING"
    else
        echo "   ❌ NO INDEX PAGE"
    fi
}

# Check all main units
check_unit "public/units/y7-maths-algebra" "Y7 Maths Algebra"
check_unit "public/units/y7-science-ecosystems" "Y7 Science Ecosystems"
check_unit "public/units/y7-digital-technology" "Y7 Digital Technology"
check_unit "public/units/y7-foundational-reading" "Y7 Foundational Reading"
check_unit "public/units/y8-statistics" "Y8 Statistics"
check_unit "public/units/y8-digital-kaitiakitanga" "Y8 Digital Kaitiakitanga"
check_unit "public/units/y8-critical-thinking" "Y8 Critical Thinking"
check_unit "public/units/y9-science-ecology" "Y9 Science Ecology"
check_unit "public/units/y9-maths-geometry-patterns" "Y9 Geometry Patterns"
check_unit "public/units/y10-physics-forces" "Y10 Physics Forces"
check_unit "public/units/y10-physics-navigation" "Y10 Physics Navigation"
check_unit "public/y8-systems" "Y8 Systems (main)"
check_unit "public/writers-toolkit" "Writers Toolkit"
check_unit "public/guided-inquiry-unit" "Guided Inquiry"

echo ""
echo "===================================================================="
echo "✅ Unit quality check complete!"
echo "===================================================================="
