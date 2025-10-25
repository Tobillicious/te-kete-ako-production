#!/usr/bin/env python3
"""
Execute batch migration to GraphRAG
Loads 1,573 backup resources via SQL batching
"""

import json
import re
from pathlib import Path

# Supabase connection details (from environment or direct)
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def parse_sql_inserts(sql_content):
    """Parse the SQL file and extract individual INSERT statements"""
    
    # Find all VALUE tuples
    values_pattern = r'\(([^()]+(?:\([^)]*\)[^()]*)*)\)(?:,|\s*ON CONFLICT)'
    
    inserts = []
    match_count = 0
    
    for match in re.finditer(values_pattern, sql_content, re.DOTALL):
        match_count += 1
        inserts.append(match.group(0))
    
    print(f"📊 Parsed {match_count} insert statements from SQL file")
    return inserts[:5]  # Start with first 5 for testing

def batch_load_resources():
    """Load resources in batches via SQL execution"""
    
    sql_file = Path("/Users/admin/Documents/te-kete-ako-clean/backup_load_sql.sql")
    
    print("📂 Reading SQL file...")
    sql_content = sql_file.read_text()
    
    print(f"📏 SQL file size: {len(sql_content)} bytes")
    
    # Extract the INSERT statement start
    insert_start = sql_content.find("INSERT INTO graphrag_resources")
    values_start = sql_content.find("VALUES", insert_start) + 6
    values_end = sql_content.find("ON CONFLICT", values_start)
    
    values_section = sql_content[values_start:values_end].strip()
    
    # Count expected resources
    value_count = values_section.count("),(") + 1
    print(f"✅ Found {value_count} resources to load")
    
    # Split into batches of 50
    batch_size = 50
    batches = []
    
    # Parse values - split by "),(" 
    value_tuples = []
    current = ""
    depth = 0
    
    for char in values_section:
        current += char
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0 and current.rstrip().endswith(")"):
                value_tuples.append(current.rstrip(",").strip())
                current = ""
    
    print(f"✅ Parsed {len(value_tuples)} value tuples")
    
    # Create SQL batches
    for i in range(0, len(value_tuples), batch_size):
        batch = value_tuples[i:i+batch_size]
        batch_num = i // batch_size + 1
        
        sql = f"""
        INSERT INTO graphrag_resources (
            file_path, resource_type, title, quality_score, cultural_context,
            year_level, subject, canonical_subject, has_te_reo, has_whakataukī,
            content_preview, metadata, archive_status, is_backup, backup_type,
            created_at, updated_at
        ) VALUES
        {','.join(batch)}
        ON CONFLICT (file_path) DO NOTHING;
        """
        
        batches.append({
            'num': batch_num,
            'count': len(batch),
            'sql': sql
        })
    
    print(f"✅ Created {len(batches)} batches of ~{batch_size} resources each")
    
    return batches

def main():
    print("🚀 GRAPHRAG BATCH MIGRATION EXECUTOR\n")
    
    batches = batch_load_resources()
    
    print(f"\n📋 BATCH PLAN:")
    total_resources = sum(b['count'] for b in batches)
    print(f"   Total batches: {len(batches)}")
    print(f"   Total resources: {total_resources}")
    print(f"   Batch size: ~50 resources/batch")
    
    print(f"\n💡 NEXT STEPS:")
    print(f"   1. Copy each batch's SQL to Supabase SQL Editor")
    print(f"   2. Execute batches 1-10 (500 resources)")
    print(f"   3. Verify with: SELECT COUNT(*) FROM graphrag_resources WHERE is_backup=true;")
    print(f"   4. Continue with remaining batches")

if __name__ == '__main__':
    main()
