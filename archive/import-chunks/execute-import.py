#!/usr/bin/env python3
"""Execute GraphRAG import via Supabase REST API"""

import requests
import json
import os
from pathlib import Path

def execute_sql_via_supabase(sql_content):
    """Execute SQL via Supabase REST API"""
    
    url = "https://nlgldaqtubrlcqddppbq.supabase.co"
    service_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.CJHZCNMwuBmLPR5IH7qn_-X8Uw8Jcz9yZUWQZhgIZYc"
    
    headers = {
        "apikey": service_key,
        "Authorization": f"Bearer {service_key}",
        "Content-Type": "application/json"
    }
    
    # Try direct SQL execution via Supabase
    try:
        print("🚀 Executing SQL import...")
        
        # Use the RPC endpoint for custom SQL
        response = requests.post(
            f"{url}/rest/v1/rpc/execute_sql",
            headers=headers,
            json={"sql": sql_content}
        )
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
        return response.status_code == 200
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🚀 GRAPHRAG IMPORT EXECUTOR")
    print("=" * 50)
    
    # Start with tiny test
    tiny_sql_file = Path("test-import-tiny.sql")
    
    if tiny_sql_file.exists():
        print(f"📝 Testing with: {tiny_sql_file}")
        with open(tiny_sql_file, 'r') as f:
            sql_content = f.read()
        
        success = execute_sql_via_supabase(sql_content)
        
        if success:
            print("✅ Test import successful!")
            print("🚀 Ready for full import!")
        else:
            print("❌ Test import failed")
    else:
        print("❌ Test SQL file not found")

if __name__ == "__main__":
    main()