#!/usr/bin/env python3
"""
Parse SQL batches file and extract key information
Shows what will be loaded and summary statistics
"""

import re
from pathlib import Path

SQL_FILE = Path("/Users/admin/Documents/te-kete-ako-clean/backup_batches_all.sql")

def extract_batches(sql_content):
    """Extract individual batch statements"""
    
    # Split by "-- BATCH X:" comments
    batch_pattern = r'-- BATCH \d+:.*?\n'
    batches_split = re.split(batch_pattern, sql_content)
    
    batches = []
    for batch_sql in batches_split[1:]:  # Skip empty first element
        if batch_sql.strip():
            batches.append(batch_sql.strip())
    
    return batches

def extract_resource_count(batch_sql):
    """Count how many VALUES rows in a batch"""
    # Count opening parens that start a VALUES row
    return batch_sql.count("('backup_before_css_migration")

def main():
    print("📖 Reading SQL batches file...")
    sql_content = SQL_FILE.read_text()
    
    print(f"📦 Parsing batches...")
    batches = extract_batches(sql_content)
    
    total_resources = 0
    for i, batch in enumerate(batches, 1):
        count = extract_resource_count(batch)
        total_resources += count
        print(f"  Batch {i}: {count} resources")
    
    print("")
    print("📊 SUMMARY:")
    print(f"   Total batches: {len(batches)}")
    print(f"   Total resources: {total_resources}")
    print(f"   Average per batch: {total_resources // len(batches)}")
    print("")
    print("✅ SQL is ready for loading!")
    print("")
    print("📌 TO LOAD ALL BATCHES:")
    print("   Run: cat backup_batches_all.sql | psql -U ... -d ... -h ...")
    print("   OR: Copy entire backup_batches_all.sql to Supabase SQL editor")
    print("")

if __name__ == "__main__":
    main()
