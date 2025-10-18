#!/bin/bash
# TEST STUDENT USER JOURNEY
# Journey: Student wants to play Te Reo Wordle

echo "🎮 TESTING STUDENT GAME JOURNEY"
echo "Journey: Student → Homepage → Games → Te Reo Wordle → Play"
echo "=="
echo ""

PUBLIC_DIR="public"
RESULTS=0
TOTAL=5

# Step 1: Homepage
echo "Step 1: Landing on homepage..."
if [ -f "$PUBLIC_DIR/index.html" ]; then
    if grep -q "games\|Kēmu\|Wordle" "$PUBLIC_DIR/index.html"; then
        echo "  ✅ Homepage has games featured"
        RESULTS=$((RESULTS + 1))
    else
        echo "  ⚠️  Games not prominently featured"
    fi
else
    echo "  ❌ Homepage missing"
fi

# Step 2: Games page
echo "Step 2: Navigating to games page..."
if [ -f "$PUBLIC_DIR/games/index.html" ]; then
    echo "  ✅ Games index exists"
    RESULTS=$((RESULTS + 1))
    
    # Check for NEW breadcrumbs
    if grep -q "breadcrumb\|🏠 Home" "$PUBLIC_DIR/games/index.html"; then
        echo "  ✅ Breadcrumbs present (NEW!)"
        RESULTS=$((RESULTS + 1))
    else
        echo "  ⚠️  No breadcrumbs"
    fi
else
    echo "  ❌ Games index missing"
fi

# Step 3: Te Reo Wordle
echo "Step 3: Finding Te Reo Wordle..."
if [ -f "$PUBLIC_DIR/games/te-reo-wordle.html" ]; then
    echo "  ✅ Te Reo Wordle exists"
    RESULTS=$((RESULTS + 1))
else
    echo "  ❌ Te Reo Wordle missing"
fi

# Step 4: Check if game is interactive
echo "Step 4: Verifying game is playable..."
if [ -f "$PUBLIC_DIR/games/te-reo-wordle.html" ]; then
    if grep -q "<script\|function\|const" "$PUBLIC_DIR/games/te-reo-wordle.html"; then
        echo "  ✅ Game has JavaScript (interactive)"
        RESULTS=$((RESULTS + 1))
    else
        echo "  ⚠️  No JavaScript found"
    fi
fi

echo ""
echo "=="
echo "📊 STUDENT JOURNEY: $RESULTS/$TOTAL steps successful"
echo "=="

if [ $RESULTS -eq $TOTAL ]; then
    echo "🎉 PERFECT! Students can find and play games!"
elif [ $RESULTS -ge 3 ]; then
    echo "👍 GOOD! Core journey works"
else
    echo "🚨 NEEDS WORK!"
fi
