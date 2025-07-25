#!/bin/bash

# Te Kete Ako - Copy Essential Files to Clean Deployment
# This copies only the production-ready files we need

echo "🚀 Creating clean Te Kete Ako deployment..."
echo ""

SOURCE_DIR="/Users/admin/Documents/Mangakōtukutuku/2025/Term 3/Coding!/14Jul"
TARGET_DIR="/Users/admin/Documents/te-kete-ako-clean"

echo "📂 Source: $SOURCE_DIR"
echo "📂 Target: $TARGET_DIR"
echo ""

# Create target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

echo "📋 Copying essential website files..."

# Copy main HTML files
cp "$SOURCE_DIR"/*.html "$TARGET_DIR/" 2>/dev/null

# Copy essential directories
echo "📁 Copying CSS..."
cp -r "$SOURCE_DIR/css" "$TARGET_DIR/" 2>/dev/null

echo "📁 Copying JavaScript..."
cp -r "$SOURCE_DIR/js" "$TARGET_DIR/" 2>/dev/null

echo "📁 Copying Games..."
cp -r "$SOURCE_DIR/games" "$TARGET_DIR/" 2>/dev/null

echo "📁 Copying Handouts..."
cp -r "$SOURCE_DIR/handouts" "$TARGET_DIR/" 2>/dev/null

echo "📁 Copying Units..."
cp -r "$SOURCE_DIR/units" "$TARGET_DIR/" 2>/dev/null

echo "📁 Copying Y8 Systems..."
cp -r "$SOURCE_DIR/y8-systems" "$TARGET_DIR/" 2>/dev/null

echo "📁 Copying Data..."
cp -r "$SOURCE_DIR/data" "$TARGET_DIR/" 2>/dev/null

echo "📁 Copying Icons..."
cp -r "$SOURCE_DIR/icons" "$TARGET_DIR/" 2>/dev/null

# Copy PWA files
echo "📱 Copying PWA files..."
cp "$SOURCE_DIR/manifest.json" "$TARGET_DIR/" 2>/dev/null
cp "$SOURCE_DIR/sw.js" "$TARGET_DIR/" 2>/dev/null
cp "$SOURCE_DIR/offline.html" "$TARGET_DIR/" 2>/dev/null

# Create netlify.toml for deployment
echo "⚙️ Creating Netlify configuration..."
cat > "$TARGET_DIR/netlify.toml" << 'EOF'
[build]
  publish = "."

[[redirects]]
  from = "/curriculum"
  to = "/curriculum-alignment.html"
  status = 301

[[redirects]]
  from = "/maori-wordle"
  to = "/games/te-reo-wordle.html"
  status = 301

[[redirects]]
  from = "/activities"
  to = "/activities.html"
  status = 301

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 404

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Cache-Control = "public, max-age=3600"
EOF

# Create _redirects as backup
cat > "$TARGET_DIR/_redirects" << 'EOF'
/curriculum /curriculum-alignment.html 301
/maori-wordle /games/te-reo-wordle.html 301
/activities /activities.html 301
/* /index.html 404
EOF

echo ""
echo "🌟 SUCCESS! Clean Te Kete Ako deployment ready!"
echo ""
echo "📁 Clean deployment location: $TARGET_DIR"
echo ""
echo "🚀 DEPLOYMENT OPTIONS:"
echo ""
echo "1️⃣ NETLIFY (Recommended):"
echo "   • Go to https://app.netlify.com/drop"
echo "   • Drag the 'te-kete-ako-clean' folder"
echo "   • LIVE in 30 seconds!"
echo ""
echo "2️⃣ SURGE (Fastest):"
echo "   • cd '$TARGET_DIR'"
echo "   • npx surge ."
echo "   • LIVE immediately!"
echo ""
echo "🎓 Your mint teaching resources will be serving the community!"
echo "🌟 No more git corruption or deployment issues!"
echo ""