#!/bin/bash
# Quick GraphRAG Indexing Script - Te Kete Ako
# Indexes all HTML files in public/ directory

echo "🌿 NGA MIHI NUI! Starting GraphRAG indexing..."
echo ""

# Count files
HTML_COUNT=$(find ../public -name "*.html" -type f | wc -l)
echo "📊 Found $HTML_COUNT HTML files to process"
echo ""

# This would normally connect to Supabase
# For now, let's create a Python script instead which can use MCP
echo "✅ Script ready! Run with Python for Supabase integration"
echo ""
