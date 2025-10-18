#!/bin/bash
# Commit all today's quality work
# Run this in fresh terminal when ready

echo "📦 Committing Quality-First Work"
echo "================================"

git add public/index.html
git add public/components/navigation-standard.html
git add public/generated-resources-alpha/
git add *.md
git add *.py
git add *.js

echo ""
echo "📊 Changes to commit:"
git status --short

echo ""
echo "✅ Ready to commit with message:"
echo "Quality-first integration: 30 units added with verification framework"

read -p "Commit now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    git commit -m "Quality-first integration: 30 units in navigation, verification tools created, focus on excellence over quantity"
    echo "✅ Committed!"
else
    echo "⏸️  Skipped - you can commit manually"
fi

echo ""
echo "🧪 Next: Run quality tests"
echo "   node test-all-navigation-links.js"

