#!/bin/bash
# DEPLOY TO VERCEL - SIMPLEST METHOD
# Run this script to deploy in 2 minutes

echo "🚀 DEPLOYING TE KETE AKO TO VERCEL"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if vercel is installed
if ! command -v vercel &> /dev/null; then
    echo "📦 Installing Vercel CLI..."
    npm install -g vercel
    echo "✅ Vercel CLI installed!"
    echo ""
fi

# Build the site
echo "🔨 Building with Vite..."
npm run build
echo "✅ Build complete!"
echo ""

# Deploy to Vercel
echo "🚀 Deploying to Vercel..."
echo ""
echo "Follow the prompts:"
echo "  • Project name: te-kete-ako"
echo "  • Directory: . (just press enter)"
echo "  • Deploy: Yes"
echo ""

vercel --prod

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ DEPLOYMENT COMPLETE!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Your site is now live! Copy the URL above."
echo ""
echo "🎯 Next steps:"
echo "  1. Test the live URL"
echo "  2. Share with team"
echo "  3. Bookmark for demo"
echo ""

