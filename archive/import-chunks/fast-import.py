#!/usr/bin/env python3
"""
FAST GraphRAG Import - Direct to Supabase via REST API
Uses urllib (built-in) to POST SQL directly to Supabase
"""

import urllib.request
import json
import time
from pathlib import Path

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

SQL_FILE = Path(__file__).parent / "graphrag-batch-index.sql"

def execute_sql_via_rest(sql: str) -> dict:
    """Execute SQL via Supabase REST API."""
    # Use the postgrest SQL endpoint
    url = f"{SUPABASE_URL}/rest/v1/rpc/exec_sql"
    
    data = json.dumps({"query": sql}).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'apikey': ANON_KEY,
            'Authorization': f'Bearer {ANON_KEY}',
            'Content-Type': 'application/json',
            'Prefer': 'return=minimal'
        },
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            return {'success': True, 'status': response.status}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def import_full_sql():
    """Import the complete SQL file."""
    print("=" * 80)
    print("🚀 FAST GRAPHRAG IMPORT - Direct REST API")
    print("=" * 80)
    print()
    
    print(f"📂 Reading {SQL_FILE}...")
    with open(SQL_FILE, 'r', encoding='utf-8') as f:
        sql = f.read()
    
    print(f"✅ SQL loaded: {len(sql):,} characters, {len(sql.splitlines()):,} lines")
    print()
    
    # Try direct import
    print("💾 Attempting direct import via REST API...")
    print("⏳ This may take 30-60 seconds...")
    print()
    
    start = time.time()
    result = execute_sql_via_rest(sql)
    elapsed = time.time() - start
    
    if result.get('success'):
        print(f"✅ IMPORT SUCCESSFUL!")
        print(f"⏱️  Time taken: {elapsed:.1f} seconds")
        print()
        print("📊 Verifying...")
        print("Run this SQL to verify:")
        print("  SELECT COUNT(*) FROM graphrag_resources WHERE file_path LIKE '/public/%';")
        print("  Expected: ~2,114")
    else:
        print(f"❌ Import failed: {result.get('error')}")
        print()
        print("💡 FALLBACK: Use Supabase Dashboard")
        print("  1. Open: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql/new")
        print(f"  2. Copy/paste: {SQL_FILE}")
        print("  3. Click RUN")
    
    print()
    print("=" * 80)

if __name__ == "__main__":
    import_full_sql()

