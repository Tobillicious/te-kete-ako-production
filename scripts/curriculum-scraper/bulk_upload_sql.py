#!/usr/bin/env python3
"""
Bulk upload SQL statements to Supabase using execute_sql.
This script takes a SQL file and executes it via direct database connection.
"""

import os
import sys
from supabase import create_client, Client

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    print("❌ Error: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in .env")
    sys.exit(1)

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# Read SQL file
sql_file = "science_phase_1_inserts.sql"

print(f"📖 Reading {sql_file}...")

with open(sql_file, "r") as f:
    sql_content = f.read()

# Split into individual INSERT statements
insert_statements = [stmt.strip() + ";" for stmt in sql_content.split(";") if stmt.strip() and stmt.strip().startswith("INSERT")]

print(f"Found {len(insert_statements)} INSERT statements")

# Execute in batches
batch_size = 10
successful = 0
failed = 0

for i in range(0, len(insert_statements), batch_size):
    batch = insert_statements[i:i+batch_size]
    batch_sql = "\n".join(batch)
    
    try:
        result = supabase.rpc('execute_sql', {'query': batch_sql}).execute()
        successful += len(batch)
        print(f"✅ Batch {i//batch_size + 1}: Inserted {len(batch)} statements (Total: {successful}/{len(insert_statements)})")
    except Exception as e:
        failed += len(batch)
        print(f"❌ Batch {i//batch_size + 1} failed: {e}")
        # Try individual inserts for this batch
        for stmt in batch:
            try:
                supabase.rpc('execute_sql', {'query': stmt}).execute()
                successful += 1
                failed -= 1
            except Exception as e2:
                print(f"   ❌ Statement failed: {stmt[:100]}...")

print(f"\n{'='*50}")
print(f"✅ Successfully inserted: {successful}")
print(f"❌ Failed: {failed}")
print(f"Total: {len(insert_statements)}")

