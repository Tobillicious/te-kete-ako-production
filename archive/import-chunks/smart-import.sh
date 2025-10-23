#!/bin/bash
# Smart Import - Uses Supabase CLI if available, otherwise provides instructions

echo "🚀 SMART GRAPHRAG IMPORT"
echo "======================="
echo ""
echo "Checking for Supabase CLI..."

if command -v supabase &> /dev/null; then
    echo "✅ Supabase CLI found! Running import..."
    cd "$(dirname "$0")/.."
    supabase db execute -f scripts/graphrag-batch-index.sql
    echo "✅ Import complete!"
else
    echo "⚠️  Supabase CLI not found"
    echo ""
    echo "📋 MANUAL IMPORT OPTIONS:"
    echo ""
    echo "1️⃣  Supabase Dashboard (Easiest):"
    echo "    https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql/new"
    echo "    Copy/paste: scripts/graphrag-batch-index.sql"
    echo ""
    echo "2️⃣  Install Supabase CLI:"
    echo "    brew install supabase/tap/supabase"
    echo "    supabase link --project-ref nlgldaqtubrlcqddppbq"
    echo "    Then run this script again"
    echo ""
    echo "3️⃣  psql (if you have postgres password):"
    echo '    psql "postgresql://postgres:[PASSWORD]@db.nlgldaqtubrlcqddppbq.supabase.co:5432/postgres" \'
    echo "      < scripts/graphrag-batch-index.sql"
    echo ""
fi

