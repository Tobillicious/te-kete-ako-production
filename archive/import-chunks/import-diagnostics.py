#!/usr/bin/env python3
"""
Import Diagnostics - Te Kete Ako GraphRAG
=========================================
Helps troubleshoot database import issues and provides real-time monitoring.
"""

import os
import json
import requests
from datetime import datetime

def check_supabase_connection():
    """Test Supabase connectivity with different keys."""
    url = "https://nlgldaqtubrlcqddppbq.supabase.co"
    anon_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"
    
    print("🔍 SUPABASE CONNECTION DIAGNOSTICS")
    print("=" * 50)
    
    # Test anon key
    headers = {
        "apikey": anon_key,
        "Authorization": f"Bearer {anon_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(f"{url}/rest/v1/graphrag_resources?limit=1", headers=headers)
        print(f"✅ Anon key status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Current records in GraphRAG: {len(data)}")
        else:
            print(f"⚠️ Response: {response.text}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    # Check service key from environment
    service_key = os.getenv('SUPABASE_SERVICE_KEY')
    if service_key:
        print(f"✅ Service key found in environment")
        headers_service = {
            "apikey": service_key,
            "Authorization": f"Bearer {service_key}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(f"{url}/rest/v1/graphrag_resources?limit=1", headers=headers_service)
            print(f"✅ Service key status: {response.status_code}")
        except Exception as e:
            print(f"❌ Service key error: {e}")
    else:
        print(f"⚠️ No service key in environment")

def monitor_import_progress():
    """Monitor import progress from tracker file."""
    tracker_file = "IMPORT-PROGRESS-TRACKER.md"
    
    print("\n📊 IMPORT PROGRESS MONITOR")
    print("=" * 50)
    
    if os.path.exists(tracker_file):
        with open(tracker_file, 'r') as f:
            content = f.read()
        
        # Extract key metrics
        lines = content.split('\n')
        for line in lines:
            if 'Chunks Completed:' in line:
                completed = line.split(':')[1].strip()
                print(f"✅ Chunks completed: {completed}")
            elif 'Records Imported:' in line:
                imported = line.split(':')[1].strip()
                print(f"📥 Records imported: {imported}")
            elif 'Success Rate:' in line:
                rate = line.split(':')[1].strip()
                print(f"📈 Success rate: {rate}")
    else:
        print("⚠️ Progress tracker file not found")

def suggest_fixes():
    """Suggest common fixes for import issues."""
    print("\n🔧 COMMON FIXES")
    print("=" * 50)
    print("1. Service Key Issues:")
    print("   export SUPABASE_SERVICE_KEY='your_key_here'")
    print("2. RLS Permissions:")
    print("   Check graphrag_resources table policies")
    print("3. Network Issues:")
    print("   Verify internet connection and Supabase status")
    print("4. Rate Limiting:")
    print("   Add delays between chunks (cursor agent handles this)")

if __name__ == "__main__":
    print(f"🚀 GRAPHRAG IMPORT DIAGNOSTICS - {datetime.now()}")
    print()
    
    check_supabase_connection()
    monitor_import_progress()
    suggest_fixes()
    
    print("\n" + "=" * 50)
    print("✅ Diagnostics complete!")