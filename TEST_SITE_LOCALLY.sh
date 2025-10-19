#!/bin/bash

echo "🧪 TESTING TE KETE AKO - BMAD DEPLOYMENT"
echo "========================================"
echo ""

# Start local server
echo "🌐 Starting local test server on http://localhost:8000"
echo "📂 Serving from: /public"
echo ""
echo "🔍 TEST CHECKLIST:"
echo "   1. Open http://localhost:8000/index.html"
echo "   2. Check BMAD styling is visible"
echo "   3. Test sample lesson: /lessons.html"
echo "   4. Test sample handout: /handouts/ecosystem-survey-checklist.html"
echo "   5. Verify cultural patterns in background"
echo "   6. Check Framer Motion animations"
echo "   7. Test mobile responsive (resize browser)"
echo ""
echo "Press Ctrl+C to stop server"
echo ""

cd public && python3 -m http.server 8000

