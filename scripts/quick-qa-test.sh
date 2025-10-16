#!/bin/bash
# QUICK QA TEST SUITE - Oct 22 Demo Critical Checks
# Agent-9 | Created: Oct 16, 2025

echo "🧪 TE KETE AKO - QUICK QA TEST SUITE"
echo "===================================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASS=0
FAIL=0
WARN=0

# Test 1: Check critical pages exist
echo "📄 Test 1: Critical Pages Exist"
echo "--------------------------------"

CRITICAL_PAGES=(
    "public/index.html"
    "public/login.html"
    "public/signup-student.html"
    "public/signup-teacher.html"
    "public/students/dashboard.html"
    "public/teachers/dashboard.html"
    "public/curriculum-documents/mathematics.html"
    "public/curriculum-documents/science.html"
    "public/curriculum-documents/english.html"
)

for page in "${CRITICAL_PAGES[@]}"; do
    if [ -f "$page" ]; then
        echo -e "   ${GREEN}✓${NC} $page"
        ((PASS++))
    else
        echo -e "   ${RED}✗${NC} $page - MISSING!"
        ((FAIL++))
    fi
done

echo ""

# Test 2: Check games exist
echo "🎮 Test 2: Games Files Exist"
echo "----------------------------"

GAMES=(
    "public/games/te-reo-wordle.html"
    "public/games/english-wordle.html"
    "public/games/categories.html"
    "public/games/countdown-letters.html"
    "public/games/spelling-bee.html"
)

for game in "${GAMES[@]}"; do
    if [ -f "$game" ]; then
        echo -e "   ${GREEN}✓${NC} $game"
        ((PASS++))
    else
        echo -e "   ${RED}✗${NC} $game - MISSING!"
        ((FAIL++))
    fi
done

echo ""

# Test 3: Check critical CSS files
echo "🎨 Test 3: Critical CSS Files"
echo "-----------------------------"

CSS_FILES=(
    "public/css/critical.css"
    "public/css/min/te-kete-unified-design-system.min.css"
    "public/css/min/component-library.min.css"
)

for css in "${CSS_FILES[@]}"; do
    if [ -f "$css" ]; then
        size=$(wc -c < "$css" | xargs)
        if [ "$size" -gt 100 ]; then
            echo -e "   ${GREEN}✓${NC} $css (${size} bytes)"
            ((PASS++))
        else
            echo -e "   ${YELLOW}⚠${NC} $css (${size} bytes - too small?)"
            ((WARN++))
        fi
    else
        echo -e "   ${RED}✗${NC} $css - MISSING!"
        ((FAIL++))
    fi
done

echo ""

# Test 4: Check JavaScript files
echo "⚡ Test 4: Critical JavaScript"
echo "-----------------------------"

JS_FILES=(
    "public/js/supabase-client.js"
    "public/service-worker.js"
)

for js in "${JS_FILES[@]}"; do
    if [ -f "$js" ]; then
        echo -e "   ${GREEN}✓${NC} $js"
        ((PASS++))
    else
        echo -e "   ${RED}✗${NC} $js - MISSING!"
        ((FAIL++))
    fi
done

echo ""

# Test 5: Check for broken internal links (sample)
echo "🔗 Test 5: Check Sample Links"
echo "-----------------------------"

# Check homepage for critical links
if [ -f "public/index.html" ]; then
    if grep -q 'href="/login.html"' public/index.html; then
        echo -e "   ${GREEN}✓${NC} Homepage → Login link exists"
        ((PASS++))
    else
        echo -e "   ${YELLOW}⚠${NC} Homepage → Login link not found"
        ((WARN++))
    fi
    
    if grep -q 'href="/signup-student.html"' public/index.html || grep -q 'href="/signup-teacher.html"' public/index.html; then
        echo -e "   ${GREEN}✓${NC} Homepage → Signup links exist"
        ((PASS++))
    else
        echo -e "   ${YELLOW}⚠${NC} Homepage → Signup links not found"
        ((WARN++))
    fi
fi

echo ""

# Test 6: Check navigation components
echo "🧭 Test 6: Navigation Components"
echo "--------------------------------"

NAV_COMPONENTS=(
    "public/components/navigation-header.html"
    "public/components/footer.html"
)

for component in "${NAV_COMPONENTS[@]}"; do
    if [ -f "$component" ]; then
        echo -e "   ${GREEN}✓${NC} $component"
        ((PASS++))
    else
        echo -e "   ${YELLOW}⚠${NC} $component - not found (may use inline nav)"
        ((WARN++))
    fi
done

echo ""

# Test 7: Check PWA files
echo "📱 Test 7: PWA Components"
echo "-------------------------"

if [ -f "public/manifest.json" ]; then
    echo -e "   ${GREEN}✓${NC} PWA manifest exists"
    ((PASS++))
else
    echo -e "   ${YELLOW}⚠${NC} PWA manifest not found"
    ((WARN++))
fi

if [ -f "public/service-worker.js" ]; then
    echo -e "   ${GREEN}✓${NC} Service worker exists"
    ((PASS++))
else
    echo -e "   ${YELLOW}⚠${NC} Service worker not found"
    ((WARN++))
fi

echo ""

# Summary
echo "===================================="
echo "📊 TEST SUMMARY"
echo "===================================="
echo -e "${GREEN}✓ Passed:${NC} $PASS"
echo -e "${RED}✗ Failed:${NC} $FAIL"
echo -e "${YELLOW}⚠ Warnings:${NC} $WARN"
echo ""

TOTAL=$((PASS + FAIL + WARN))
if [ $TOTAL -gt 0 ]; then
    PASS_RATE=$((PASS * 100 / TOTAL))
    echo "Pass Rate: ${PASS_RATE}%"
fi

echo ""

if [ $FAIL -eq 0 ]; then
    echo -e "${GREEN}🎉 ALL CRITICAL TESTS PASSED!${NC}"
    echo "Site is ready for Oct 22 demo!"
    exit 0
else
    echo -e "${RED}❌ SOME TESTS FAILED!${NC}"
    echo "Please fix critical issues before demo."
    exit 1
fi

