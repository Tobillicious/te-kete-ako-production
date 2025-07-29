#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "🚀 Building Te Kete Ako for deployment..."

# Create the public directory if it doesn't exist
mkdir -p public

# Copy all top-level HTML files, including new ones
cp *.html public/
cp manifest.json public/
cp sw.js public/ 2>/dev/null || echo "sw.js not found, skipping"
cp _redirects public/

# Copy Firebase authentication files
echo "📁 Copying Firebase Auth files..."
mkdir -p public/js
cp js/firebase-config.js public/js/ 2>/dev/null || echo "Firebase config not found"

# Create directories and copy their contents
echo "📁 Copying core directories..."
mkdir -p public/css && cp -r css/* public/css/
mkdir -p public/js && cp -r js/* public/js/
mkdir -p public/icons && cp -r icons/* public/icons/ 2>/dev/null || echo "Icons not found"
mkdir -p public/games && cp -r games/* public/games/
mkdir -p public/handouts && cp -r handouts/* public/handouts/
mkdir -p public/lessons && cp -r lessons/* public/lessons/
mkdir -p public/units && cp -r units/* public/units/
mkdir -p public/y8-systems && cp -r y8-systems/* public/y8-systems/
mkdir -p public/guided-inquiry-unit && cp -r guided-inquiry-unit/* public/guided-inquiry-unit/

# Copy educational content from old-lessons (includes interactive literacy site)
echo "📁 Copying educational content..."
mkdir -p public/old-lessons && cp -r old-lessons/* public/old-lessons/ 2>/dev/null || echo "old-lessons not found"

# Copy curriculum data for alignment features
mkdir -p public/data && cp -r data/* public/data/ 2>/dev/null || echo "data not found"

# Copy agent knowledge hub for teacher resources
mkdir -p public/agent-knowledge-hub && cp -r agent-knowledge-hub/* public/agent-knowledge-hub/ 2>/dev/null || echo "agent-knowledge-hub not found"

# Copy utility scripts that might be needed
mkdir -p public/scripts && cp -r scripts/* public/scripts/ 2>/dev/null || echo "scripts not found"

# Copy any additional educational directories
mkdir -p public/netlify && cp -r netlify/* public/netlify/ 2>/dev/null || echo "netlify functions not found"
mkdir -p public/supabase && cp -r supabase/* public/supabase/ 2>/dev/null || echo "supabase not found"

echo "✅ Build complete! All educational content deployed including Firebase Auth."