#!/usr/bin/env python3
"""Full import execution - Import all 2,114 records NOW"""

import requests
import json
import time
import re
from pathlib import Path

def import_records_batch(records):
    """Import a batch of records"""
    url = "https://nlgldaqtubrlcqddppbq.supabase.co"
    anon_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"
    
    headers = {
        "apikey": anon_key,
        "Authorization": f"Bearer {anon_key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    try:
        response = requests.post(
            f"{url}/rest/v1/graphrag_resources",
            headers=headers,
            json=records
        )
        
        return response.status_code in [200, 201], response.status_code, response.text
        
    except Exception as e:
        return False, 0, str(e)

def sql_to_json(sql_content):
    """Convert SQL INSERT to JSON records"""
    # Extract VALUES section
    values_match = re.search(r'VALUES\s*(.*?)\s*ON CONFLICT', sql_content, re.DOTALL)
    if not values_match:
        return []
    
    values_section = values_match.group(1)
    
    # Split by ),( to get individual records
    records_raw = re.split(r'\),\s*\(', values_section)
    
    records = []
    for i, record_raw in enumerate(records_raw):
        if i % 100 == 0:
            print(f"  Converting record {i+1}/{len(records_raw)}...")
        
        # Clean up the record
        record_raw = record_raw.strip('(),')
        
        # Parse the values (this is simplified - real parsing would be more robust)
        try:
            # Extract quoted strings and numbers
            parts = []
            current_part = ""
            in_quote = False
            
            for char in record_raw:
                if char == "'" and not in_quote:
                    in_quote = True
                    current_part = ""
                elif char == "'" and in_quote:
                    in_quote = False
                    parts.append(current_part)
                    current_part = ""
                elif in_quote:
                    current_part += char
                elif char == ',' and not in_quote:
                    if current_part.strip():
                        parts.append(current_part.strip())
                    current_part = ""
                elif not in_quote:
                    current_part += char
            
            if current_part.strip():
                parts.append(current_part.strip())
            
            # Map to record structure (simplified)
            if len(parts) >= 11:
                record = {
                    "file_path": parts[0] if parts[0] != 'NULL' else None,
                    "title": parts[1] if parts[1] != 'NULL' else None,
                    "resource_type": parts[2] if parts[2] != 'NULL' else 'lesson',
                    "subject": parts[3] if parts[3] != 'NULL' else 'Cross-Curricular',
                    "canonical_subject": parts[4] if parts[4] != 'NULL' else 'Cross-Curricular',
                    "year_level": parts[5] if parts[5] != 'NULL' else 'All Years',
                    "unit": parts[6] if parts[6] != 'NULL' else None,
                    "quality_score": int(parts[7]) if parts[7].isdigit() else 80,
                    "cultural_context": parts[8].lower() == 'true',
                    "has_te_reo": parts[9].lower() == 'true',
                    "has_whakataukī": parts[10].lower() == 'true',
                    "content_preview": parts[11] if len(parts) > 11 and parts[11] != 'NULL' else '',
                    "metadata": {"imported": True}
                }
                records.append(record)
        except Exception as e:
            print(f"⚠️ Error parsing record {i}: {e}")
            continue
    
    return records

def main():
    print("🚀 FULL IMPORT EXECUTION - 2,114 RECORDS")
    print("=" * 60)
    
    # Read SQL file
    sql_file = Path("scripts/graphrag-batch-index.sql")
    if not sql_file.exists():
        print("❌ SQL file not found!")
        return
    
    print("📝 Reading SQL file...")
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    print("🔄 Converting SQL to JSON...")
    records = sql_to_json(sql_content)
    print(f"✅ Converted {len(records)} records")
    
    if not records:
        print("❌ No records to import!")
        return
    
    # Import in batches of 50
    batch_size = 50
    total_imported = 0
    total_failed = 0
    
    print(f"🚀 Importing {len(records)} records in batches of {batch_size}...")
    
    for i in range(0, len(records), batch_size):
        batch = records[i:i+batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (len(records) + batch_size - 1) // batch_size
        
        print(f"📦 Batch {batch_num}/{total_batches}: Importing {len(batch)} records...")
        
        success, status_code, response_text = import_records_batch(batch)
        
        if success:
            total_imported += len(batch)
            print(f"✅ Batch {batch_num} successful!")
        else:
            total_failed += len(batch)
            print(f"❌ Batch {batch_num} failed: {status_code} - {response_text[:200]}")
        
        # Small delay to avoid rate limiting
        time.sleep(0.5)
    
    print("=" * 60)
    print("🎉 IMPORT COMPLETE!")
    print(f"✅ Successfully imported: {total_imported}")
    print(f"❌ Failed to import: {total_failed}")
    print(f"📊 Success rate: {(total_imported/(total_imported+total_failed)*100):.1f}%")

if __name__ == "__main__":
    main()