#!/bin/bash

# Build script for Te Kete Ako - Copy files to public directory for Netlify deployment

echo "🚀 Building Te Kete Ako for deployment..."

# Ensure public directory exists
mkdir -p public/js

# Copy Firebase authentication files
echo "📁 Copying Firebase Auth files..."
cp js/firebase-config.js public/js/
cp login.html public/
cp register-simple.html public/

# Copy any other updated root files to public
echo "📁 Syncing updated files..."
rsync -av --exclude='public' --exclude='node_modules' --exclude='.git' --exclude='previews' . public/

echo "✅ Build complete! Files ready for Netlify deployment."