#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Create the public directory if it doesn't exist
mkdir -p public

# Copy all top-level HTML files, including new ones
cp *.html public/
cp forgot-password.html public/
cp reset-password.html public/

# Copy essential manifest and service worker files
cp manifest.json public/
cp sw.js public/
cp _redirects public/

# Create directories and copy their contents
mkdir -p public/css
cp -r css/* public/css/

mkdir -p public/js
cp -r js/* public/js/

mkdir -p public/icons
cp -r icons/* public/icons/

mkdir -p public/games
cp -r games/* public/games/

mkdir -p public/handouts
cp -r handouts/* public/handouts/

mkdir -p public/lessons
cp -r lessons/* public/lessons/

mkdir -p public/units
cp -r units/* public/units/

mkdir -p public/y8-systems
cp -r y8-systems/* public/y8-systems/

mkdir -p public/guided-inquiry-unit
cp -r guided-inquiry-unit/* public/guided-inquiry-unit/

echo "All files copied to /public directory."
