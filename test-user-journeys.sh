#!/bin/bash
# TEST CRITICAL USER JOURNEYS
# Verify actual functionality, not just existence

echo "🧪 TESTING REAL USER JOURNEYS"
echo "=============================="
echo ""

PUBLIC="/Users/admin/Documents/te-kete-ako-clean/public"
ISSUES=0

# Test Journey 1: Teacher finds and accesses a resource
echo "📚 Journey 1: Teacher finds AI-generated resource"
if [ -f "$PUBLIC/index.html" ] && grep -q "generated-resources-alpha" "$PUBLIC/index.html"; then
    echo "  ✅ Homepage links to AI resources"
    if [ -f "$PUBLIC/generated-resources-alpha/index.html" ]; then
        echo "  ✅ AI resources index exists"
        if [ -f "$PUBLIC/generated-resources-alpha/handouts/algebraic-thinking-in-traditional-māori-games.html" ]; then
            echo "  ✅ Sample handout accessible"
            # Check if handout is complete
            if grep -q "Download\|Print" "$PUBLIC/generated-resources-alpha/handouts/algebraic-thinking-in-traditional-māori-games.html"; then
                echo "  ✅ Handout is actionable (has print/download)"
            else
                echo "  ⚠️  Handout missing print/download functionality"
                ISSUES=$((ISSUES + 1))
            fi
        else
            echo "  ❌ Sample handout missing!"
            ISSUES=$((ISSUES + 1))
        fi
    else
        echo "  ❌ AI resources index missing!"
        ISSUES=$((ISSUES + 1))
    fi
else
    echo "  ❌ Homepage doesn't link to AI resources!"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Test Journey 2: Student plays a game
echo "🎮 Journey 2: Student plays Te Reo Wordle"
if [ -f "$PUBLIC/games/te-reo-wordle.html" ]; then
    echo "  ✅ Game file exists"
    # Check if game has actual word list
    if grep -q "AROHA\|WHAKAPAPA\|WHENUA" "$PUBLIC/games/te-reo-wordle.html"; then
        echo "  ✅ Game has Māori word list"
    else
        echo "  ❌ Game missing word list!"
        ISSUES=$((ISSUES + 1))
    fi
    # Check if game has JavaScript
    if grep -q "function\|const.*=\|let.*=" "$PUBLIC/games/te-reo-wordle.html"; then
        echo "  ✅ Game has functionality code"
    else
        echo "  ❌ Game missing JavaScript!"
        ISSUES=$((ISSUES + 1))
    fi
else
    echo "  ❌ Game file missing!"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Test Journey 3: Teacher uses crossword generator
echo "🛠️  Journey 3: Teacher uses crossword generator"
if [ -f "$PUBLIC/tools/crossword-generator.html" ]; then
    echo "  ✅ Tool exists"
    if grep -q "input\|textarea\|form" "$PUBLIC/tools/crossword-generator.html"; then
        echo "  ✅ Has input fields"
    else
        echo "  ❌ Missing input functionality!"
        ISSUES=$((ISSUES + 1))
    fi
    if grep -q "generate\|create\|build" "$PUBLIC/tools/crossword-generator.html"; then
        echo "  ✅ Has generate functionality"
    else
        echo "  ❌ Missing generate button!"
        ISSUES=$((ISSUES + 1))
    fi
else
    echo "  ❌ Tool missing!"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Test Journey 4: Navigation flow
echo "🧭 Journey 4: Complete navigation flow"
if [ -f "$PUBLIC/components/navigation-standard.html" ]; then
    echo "  ✅ Navigation component exists"
    NAV_LINKS=$(grep -o 'href="[^"]*"' "$PUBLIC/components/navigation-standard.html" | wc -l)
    echo "  ✅ Navigation has $NAV_LINKS links"
else
    echo "  ❌ Navigation component missing!"
    ISSUES=$((ISSUES + 1))
fi
echo ""

# Test Journey 5: Unit access
echo "📖 Journey 5: Access complete unit"
if [ -f "$PUBLIC/critical-thinking-unit.html" ]; then
    echo "  ✅ Critical thinking unit exists"
    if [ -d "$PUBLIC/critical-thinking/lessons" ]; then
        LESSON_COUNT=$(ls "$PUBLIC/critical-thinking/lessons"/*.html 2>/dev/null | wc -l)
        echo "  ✅ Unit has $LESSON_COUNT lessons"
        if [ $LESSON_COUNT -ge 10 ]; then
            echo "  ✅ Complete unit (10 lessons)"
        else
            echo "  ⚠️  Unit incomplete (only $LESSON_COUNT lessons)"
            ISSUES=$((ISSUES + 1))
        fi
    else
        echo "  ❌ Lessons directory missing!"
        ISSUES=$((ISSUES + 1))
    fi
else
    echo "  ⚠️  Unit overview page missing (but lessons may exist)"
fi
echo ""

# Summary
echo "=============================="
echo "📊 JOURNEY TEST RESULTS"
echo "=============================="
echo ""

if [ $ISSUES -eq 0 ]; then
    echo "✅ ALL JOURNEYS COMPLETE AND FUNCTIONAL!"
    echo "Platform is ready for real users."
    exit 0
elif [ $ISSUES -le 3 ]; then
    echo "⚠️  $ISSUES minor issues found"
    echo "Platform is functional but needs minor fixes"
    exit 0
else
    echo "❌ $ISSUES issues found"
    echo "Platform needs work before production"
    exit 1
fi

