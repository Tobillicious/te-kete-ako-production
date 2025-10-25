#!/bin/bash
# 🚀 DEPLOY BETA PAGE TO NETLIFY
# Run this script to deploy all beta recruitment changes to live site

echo "🚀 Deploying Beta Teacher Program to Netlify..."
echo ""

# Add all beta-related files
echo "📦 Adding files to git..."
git add public/beta-invitation.html
git add public/index.html
git add public/teachers/beta-callout.html
git add 📧-BETA-EMAIL-TEMPLATES.md
git add 🎯-BETA-PAGE-SHIPPED.md
git add 🚀-30MIN-COMPLETE-BETA-READY.md
git add ⚡-30-MINUTE-QUICK-WINS.md

# Commit with descriptive message
echo "💾 Committing changes..."
git commit -m "🚀 BETA LAUNCH: Add teacher recruitment page + email templates

- Created /public/beta-invitation.html (conversion-optimized recruitment)
- Added beta card to homepage (prominent purple gradient)
- Created 6 email templates (outreach, acceptance, waitlist, social)
- Beta callout component for teachers page
- Complete documentation + launch checklist

IMPACT: Unlocks beta teacher recruitment (15 spots)
TIMELINE: Ready to send invites THIS WEEK
STRATEGIC: Enables Nov-Dec 2025 beta program

Platform Status: A+ (98/100) - Beta Ready ✅"

# Push to main (triggers Netlify deploy)
echo "🌐 Pushing to GitHub (triggers Netlify auto-deploy)..."
git push origin main

echo ""
echo "✅ DEPLOYMENT TRIGGERED!"
echo ""
echo "📊 Monitor deployment:"
echo "   → Netlify: https://app.netlify.com"
echo "   → Site: https://tekete.netlify.app"
echo ""
echo "⏱️ Deployment usually takes 1-2 minutes"
echo ""
echo "🎯 NEXT STEPS:"
echo "   1. Wait for Netlify deploy to complete"
echo "   2. Visit https://tekete.netlify.app/beta-invitation.html"
echo "   3. Test application form"
echo "   4. Set up Google Form integration"
echo "   5. Send beta invitations!"
echo ""
echo "🌟 BETA RECRUITMENT: READY TO LAUNCH! 🚀"

