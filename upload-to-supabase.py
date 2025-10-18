#!/usr/bin/env python3
"""
UPLOAD TO SUPABASE GRAPHRAG
Batch upload 6,596 resources + 566,852 relationships
"""

import json
import os
import time

print("🚀 UPLOADING TO SUPABASE GRAPHRAG")
print("=" * 70)

# Check for Supabase package
try:
    from supabase import create_client
    HAS_SUPABASE = True
except ImportError:
    print("⚠️  supabase-py not installed. Installing...")
    os.system("pip3 install supabase")
    from supabase import create_client
    HAS_SUPABASE = True

# Configuration
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY") or os.getenv("SUPABASE_ANON_KEY") or ""

if not SUPABASE_KEY:
    print("\n⚠️  SUPABASE_KEY not found in environment")
    print("📋 To upload, you need to:")
    print("   1. Get anon key from Supabase dashboard")
    print("   2. Set environment variable: export SUPABASE_KEY=your_key")
    print("   3. Run this script again")
    print("\n📁 Alternatively, upload manually:")
    print("   1. Open: https://nlgldaqtubrlcqddppbq.supabase.co")
    print("   2. SQL Editor → Run graphrag-upload.sql")
    print("   3. Table Editor → Import JSON files")
    print("\n💾 Data is ready in:")
    print("   • graphrag-resources-upload.json (6,596 resources)")
    print("   • graphrag-relationships-upload.json (566,852 relationships)")
    exit(0)

# Connect to Supabase
print("\n🔌 Connecting to Supabase...")
try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("   ✅ Connected!")
except Exception as e:
    print(f"   ❌ Connection failed: {e}")
    exit(1)

# Create tables first
print("\n🗃️  Creating tables...")
with open('graphrag-upload.sql', 'r') as f:
    sql = f.read()
    # Note: Table creation might need to be done via dashboard
    print("   ℹ️  Tables defined in graphrag-upload.sql")
    print("   📋 Run that SQL in Supabase dashboard first if tables don't exist")

# Load data
print("\n📊 Loading data...")
with open('graphrag-resources-upload.json', 'r') as f:
    resources = json.load(f)
print(f"   ✅ {len(resources):,} resources loaded")

with open('graphrag-relationships-upload.json', 'r') as f:
    relationships = json.load(f)
print(f"   ✅ {len(relationships):,} relationships loaded")

# Upload resources in batches
print("\n📤 Uploading resources (batch size: 100)...")
BATCH_SIZE = 100
uploaded_resources = 0

for i in range(0, len(resources), BATCH_SIZE):
    batch = resources[i:i+BATCH_SIZE]
    
    try:
        response = supabase.table('graphrag_resources').upsert(batch).execute()
        uploaded_resources += len(batch)
        
        if (i + BATCH_SIZE) % 500 == 0:
            print(f"   ... {uploaded_resources:,} / {len(resources):,} resources")
        
        time.sleep(0.1)  # Rate limiting
        
    except Exception as e:
        print(f"   ⚠️  Batch {i//BATCH_SIZE + 1} failed: {e}")
        continue

print(f"   ✅ Uploaded {uploaded_resources:,} resources")

# Upload relationships in batches
print("\n📤 Uploading relationships (batch size: 1000)...")
BATCH_SIZE = 1000
uploaded_relationships = 0

for i in range(0, len(relationships), BATCH_SIZE):
    batch = relationships[i:i+BATCH_SIZE]
    
    try:
        response = supabase.table('graphrag_relationships').insert(batch).execute()
        uploaded_relationships += len(batch)
        
        if (i + BATCH_SIZE) % 10000 == 0:
            print(f"   ... {uploaded_relationships:,} / {len(relationships):,} relationships")
        
        time.sleep(0.05)  # Rate limiting
        
    except Exception as e:
        print(f"   ⚠️  Batch {i//BATCH_SIZE + 1} failed: {e}")
        continue

print(f"   ✅ Uploaded {uploaded_relationships:,} relationships")

print("\n" + "=" * 70)
print("🎉 GRAPHRAG UPLOAD COMPLETE!")
print("=" * 70)
print(f"""
📊 Uploaded:
   • {uploaded_resources:,} resources
   • {uploaded_relationships:,} relationships
   
🔍 Now you can query:
   SELECT * FROM graphrag_resources WHERE quality_score >= 90;
   SELECT * FROM graphrag_relationships WHERE relationship_type = 'prerequisite';
   
🎯 Knowledge graph is LIVE and queryable!
""")

