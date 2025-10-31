#!/usr/bin/env python3
"""
Bulk upload Science Phase 1 statements to Supabase.
Uses the structured data from insert_science_p1.py
"""

import os
import sys
from supabase import create_client, Client

# Load environment variables
from dotenv import load_dotenv
# Load .env from workspace root (two directories up)
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(env_path)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    print("❌ Error: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in .env")
    sys.exit(1)

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# Import the statements data
from insert_science_p1 import statements

print(f"📊 Preparing to insert Science Phase 1 curriculum statements...")
print(f"Total statement groups: {len(statements)}")

# Flatten statements into individual records
all_records = []
for group in statements:
    for statement_text in group["statements"]:
        record = {
            "curriculum_version": group["curriculum_version"],
            "version_status": group["version_status"],
            "learning_area": group["learning_area"],
            "phase": group["phase"],
            "strand": group["strand"],
            "sub_strand": group.get("sub_strand", ""),
            "element": group["element"],
            "statement_text": statement_text,
            "year_levels": group["year_levels"],
            "tahurangi_url": "https://newzealandcurriculum.tahurangi.education.govt.nz/new-zealand-curriculum-online/nzc---science-phase-1-years-0-3/5637292339.p"
        }
        all_records.append(record)

print(f"Total individual statements to insert: {len(all_records)}")

# Insert in batches (Supabase handles batch inserts efficiently)
batch_size = 50
successful = 0
failed = 0

for i in range(0, len(all_records), batch_size):
    batch = all_records[i:i+batch_size]
    
    try:
        result = supabase.table('curriculum_statements').insert(batch).execute()
        successful += len(batch)
        print(f"✅ Batch {i//batch_size + 1}/{(len(all_records) + batch_size - 1)//batch_size}: Inserted {len(batch)} statements (Total: {successful}/{len(all_records)})")
    except Exception as e:
        print(f"❌ Batch {i//batch_size + 1} failed: {e}")
        # Try individual inserts for this batch
        for record in batch:
            try:
                supabase.table('curriculum_statements').insert(record).execute()
                successful += 1
            except Exception as e2:
                failed += 1
                print(f"   ❌ Failed to insert: {record['strand']} | {record['element']} | Year {record['year_levels'][0]}")
                print(f"      Error: {str(e2)[:100]}")

print(f"\n{'='*60}")
print(f"🎉 Science Phase 1 Upload Complete!")
print(f"✅ Successfully inserted: {successful}")
print(f"❌ Failed: {failed}")
print(f"📊 Total: {len(all_records)}")
print(f"{'='*60}")

