#!/bin/bash
# Safe Curriculum Scraper Runner
# Creates .env file with credentials and runs the scraper

cd "$(dirname "$0")"

# Create .env file with Supabase credentials
cat > .env << 'EOF'
# Supabase Configuration
SUPABASE_URL=https://nlgldaqtubrlcqddppbq.supabase.co
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM

# Scraping Configuration
SCRAPE_DELAY=1.5
MAX_RETRIES=3
TIMEOUT=30

# Output Configuration
OUTPUT_DIR=./scraped-data
LOG_LEVEL=INFO
EOF

echo "✓ .env file created"
echo ""
echo "Running scraper (English only - test run)..."
echo ""

# Run the scraper
python3 scraper.py --version temataiaho_2025 --learning-area English --delay 1.5

echo ""
echo "✓ Scraping complete! Check ./scraped-data for output"
echo ""
echo "Next steps:"
echo "  1. Validate: python3 validator.py ./scraped-data"
echo "  2. Upload: python3 uploader.py ./scraped-data"
echo ""

