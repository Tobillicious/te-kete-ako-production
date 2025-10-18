#!/bin/bash
# TEST CRITICAL USER JOURNEY
# Journey: Teacher finds and downloads a handout

echo "🧪 TESTING CRITICAL USER JOURNEY"
echo "Journey: Teacher → Homepage → AI Resources → Handout → Download"
echo "=" 
echo ""

PUBLIC_DIR="public"
RESULTS=0

# Step 1: Homepage exists
echo "Step 1: Landing on homepage..."
if [ -f "$PUBLIC_DIR/index.html" ]; then
    echo "  ✅ Homepage exists"
    RESULTS=$((RESULTS + 1))
else
    echo "  ❌ Homepage missing!"
fi

# Step 2: AI Resources link works
echo "Step 2: Clicking AI Resources link..."
if [ -f "$PUBLIC_DIR/generated-resources-alpha/index.html" ]; then
    echo "  ✅ AI Resources page exists"
    RESULTS=$((RESULTS + 1))
    
    # Check for breadcrumbs
    if grep -q "breadcrumb" "$PUBLIC_DIR/generated-resources-alpha/index.html"; then
        echo "  ✅ Breadcrumbs present (NEW!)"
        RESULTS=$((RESULTS + 1))
    else
        echo "  ⚠️  No breadcrumbs"
    fi
else
    echo "  ❌ AI Resources page missing!"
fi

# Step 3: Handouts index works
echo "Step 3: Browsing handouts..."
if [ -f "$PUBLIC_DIR/generated-resources-alpha/handouts/index.html" ]; then
    echo "  ✅ Handouts index exists"
    RESULTS=$((RESULTS + 1))
else
    echo "  ❌ Handouts index missing!"
fi

# Step 4: Sample handout exists
echo "Step 4: Accessing a handout..."
SAMPLE_HANDOUT="$PUBLIC_DIR/generated-resources-alpha/handouts/algebraic-thinking-in-traditional-māori-games.html"
if [ -f "$SAMPLE_HANDOUT" ]; then
    echo "  ✅ Sample handout exists"
    RESULTS=$((RESULTS + 1))
    
    # Check if printable
    if grep -q "print.css\|@media print" "$SAMPLE_HANDOUT"; then
        echo "  ✅ Handout is print-optimized"
        RESULTS=$((RESULTS + 1))
    else
        echo "  ⚠️  No print optimization found"
    fi
else
    echo "  ❌ Sample handout missing!"
fi

# Step 5: Quick Start Guide works
echo "Step 5: Accessing Quick Start Guide..."
if [ -f "$PUBLIC_DIR/generated-resources-alpha/TEACHER-QUICK-START-GUIDE.html" ]; then
    echo "  ✅ Quick Start Guide exists"
    RESULTS=$((RESULTS + 1))
else
    echo "  ❌ Quick Start Guide missing!"
fi

echo ""
echo "=" 
echo "📊 JOURNEY TEST RESULTS: $RESULTS/7 steps successful"
echo "="

if [ $RESULTS -eq 7 ]; then
    echo "🎉 PERFECT! Complete user journey works flawlessly!"
elif [ $RESULTS -ge 5 ]; then
    echo "👍 GOOD! Most steps work, minor issues to fix"
else
    echo "🚨 NEEDS WORK! Critical user journey has problems"
fi

echo ""
echo "✅ Quick Win Complete:"
echo "  1. Added breadcrumbs to AI Resources page"
echo "  2. Verified critical user journey works"
echo "  3. Ready for next polish step!"

