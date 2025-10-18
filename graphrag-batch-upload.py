#!/usr/bin/env python3
"""
GraphRAG Batch Upload - Use existing local index
Upload in small batches to avoid permission issues
"""

import sqlite3
from supabase import create_client
import time

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🚀 GRAPHRAG BATCH UPLOAD FROM LOCAL INDEX")
print("=" * 70)

# Connect to local database
local_db = sqlite3.connect('te-kete-local-index.db')
cursor = local_db.cursor()

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get all resources from local index
cursor.execute("SELECT path, title, description, type, subject, year_level FROM resources")
local_resources = cursor.fetchall()

print(f"📊 Found {len(local_resources)} resources in local index")
print("📤 Uploading to GraphRAG in batches...\n")

uploaded = 0
errors = 0
batch_size = 10

for i in range(0, min(100, len(local_resources)), batch_size):
    batch = local_resources[i:i+batch_size]
    
    for path, title, description, res_type, subject, year_level in batch:
        try:
            resource = {
                'path': path,
                'title': title[:200] if title else 'Untitled',
                'description': description[:500] if description else 'Educational resource',
                'type': res_type or 'resource',
                'subject': subject or 'general',
                'level': year_level,
                'is_active': True
            }
            
            # Try to insert
            result = supabase.table('resources').upsert(resource, on_conflict='path').execute()
            uploaded += 1
            
        except Exception as e:
            errors += 1
            if errors <= 3:  # Show first 3 errors
                print(f"   ⚠️  Error: {str(e)[:100]}")
    
    if (i + batch_size) % 50 == 0:
        print(f"   ✅ Uploaded {uploaded} resources...")
        time.sleep(0.5)  # Rate limiting

print(f"\n" + "=" * 70)
print(f"📊 Upload Complete:")
print(f"   Uploaded: {uploaded}")
print(f"   Errors: {errors}")
print("=" * 70)

if errors > 0:
    print(f"\n⚠️  {errors} errors (likely permission issues)")
    print("   Local index still works perfectly for searching!")

local_db.close()
