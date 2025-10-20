#!/usr/bin/env python3
"""
Execute GraphRAG Intelligence Boost via Supabase API
Quick execution of graphrag-quick-intelligence-boost.sql
"""

import requests
import json
from pathlib import Path

# Supabase configuration
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

print("🚀 EXECUTING GRAPHRAG INTELLIGENCE BOOST")
print("=" * 70)

# Read the SQL file
sql_file = Path("graphrag-quick-intelligence-boost.sql")
if not sql_file.exists():
    print(f"❌ File not found: {sql_file}")
    exit(1)

sql_content = sql_file.read_text()

print(f"📄 Loaded SQL file: {len(sql_content)} characters")
print(f"🎯 Executing via Supabase RPC...")

# Execute via Supabase SQL endpoint
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Note: This uses the raw SQL execution endpoint
# For production, we'd use the rpc or postgrest endpoints
url = f"{SUPABASE_URL}/rest/v1/rpc/exec_sql"

try:
    response = requests.post(
        url,
        headers=headers,
        json={"query": sql_content}
    )
    
    if response.status_code in [200, 201]:
        print("✅ Intelligence boost executed successfully!")
        print(f"📊 Response: {response.text[:500]}")
    else:
        print(f"⚠️  Response code: {response.status_code}")
        print(f"📄 Response: {response.text[:1000]}")
        print("\n💡 Note: You may need to execute the SQL directly in Supabase SQL Editor")
        print(f"   Go to: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/editor")
        print(f"   Paste contents of: {sql_file}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Alternative: Execute SQL directly in Supabase SQL Editor")
    print(f"   File ready: {sql_file.absolute()}")

print("\n" + "=" * 70)
print("✨ Intelligence boost ready for execution!")

