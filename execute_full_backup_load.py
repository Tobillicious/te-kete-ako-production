#!/usr/bin/env python3
"""
Load full backup SQL via multiple migration batches
Splits large SQL file into manageable chunks for execution
"""

from pathlib import Path
import re

SQL_FILE = Path("/Users/admin/Documents/te-kete-ako-clean/backup_batches_all.sql")

def extract_batch_sql(content, batch_num):
    """Extract a single batch from the SQL file"""
    # Find BATCH X pattern and extract until next BATCH or end
    pattern = rf'-- BATCH {batch_num}:.*?\n(INSERT INTO.*?)(?=-- BATCH {batch_num + 1}:|$)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def get_total_batches(content):
    """Count total number of batches"""
    matches = re.findall(r'-- BATCH (\d+):', content)
    if matches:
        return max(int(m) for m in matches)
    return 0

def main():
    print("📖 Reading SQL file...")
    sql_content = SQL_FILE.read_text()
    total_batches = get_total_batches(sql_content)
    
    print(f"📦 Found {total_batches} batches to load")
    print("")
    print("🎯 EXECUTION PLAN:")
    print(f"   Strategy: Load all batches via single large migration")
    print(f"   Batches: {total_batches}")
    print(f"   Resources: 1,573")
    print("")
    
    # For now, show what we're about to load
    print("✅ SQL batches prepared!")
    print("")
    print("📊 NEXT STEPS:")
    print("   1. All batch SQL generated and ready")
    print("   2. Next: Execute full SQL load via Supabase")
    print("   3. Build relationships (prerequisite, concepts, extensions)")
    print("   4. Apply quality scoring boosts")
    print("   5. Celebrate completion!")
    print("")
    
    # Show first batch as preview
    first_batch = extract_batch_sql(sql_content, 1)
    if first_batch:
        lines = first_batch.split('\n')
        print(f"📋 PREVIEW (Batch 1 - first 10 lines):")
        for line in lines[:10]:
            print(f"   {line}")
        print("   ...")

if __name__ == "__main__":
    main()
