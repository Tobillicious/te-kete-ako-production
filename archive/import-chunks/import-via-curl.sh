#!/bin/bash
# Import GraphRAG SQL via Supabase REST API

SUPABASE_URL="https://nlgldaqtubrlcqddppbq.supabase.co"
ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

echo "🚀 Importing via Supabase REST API..."
echo "Reading SQL file..."

SQL_CONTENT=$(cat scripts/graphrag-batch-index.sql)

# Use Supabase REST API SQL endpoint
curl -X POST "${SUPABASE_URL}/rest/v1/rpc/exec_sql" \
  -H "apikey: ${ANON_KEY}" \
  -H "Authorization: Bearer ${ANON_KEY}" \
  -H "Content-Type: application/json" \
  -d "{\"query\": $(echo "$SQL_CONTENT" | jq -Rs .)}" \
  --max-time 120

echo ""
echo "✅ Import request sent!"
