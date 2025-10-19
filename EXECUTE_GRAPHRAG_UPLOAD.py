#!/usr/bin/env python3
"""
Execute GraphRAG upload using subprocess to call MCP Supabase
"""

import subprocess
import json

# Read the SQL file
with open('deployment_reports/upload_to_graphrag.sql', 'r') as f:
    full_sql = f.read()

# Split into batches (separated by double newline)
batches = [b.strip() for b in full_sql.split('\n\n\n') if b.strip()]

print(f"📊 Found {len(batches)} SQL batches to execute")
print(f"🚀 Uploading to GraphRAG...\n")

# For now, let's create a single consolidated INSERT that's more efficient
# We'll extract all the values and combine them into one big INSERT

import re

all_values = []
for batch in batches:
    # Extract VALUES (...) from each batch
    match = re.search(r'VALUES\s+(.*?)\s+ON CONFLICT', batch, re.DOTALL)
    if match:
        values_str = match.group(1).strip()
        # Split by closing paren followed by comma and opening paren
        values = re.split(r'\),\s*\(', values_str)
        for v in values:
            v = v.strip()
            if not v.startswith('('):
                v = '(' + v
            if not v.endswith(')'):
                v = v + ')'
            all_values.append(v)

print(f"✅ Extracted {len(all_values)} total value sets")

# Create one mega-insert (or do it in chunks of 500)
chunk_size = 500
for i in range(0, len(all_values), chunk_size):
    chunk = all_values[i:i+chunk_size]
    sql = f"""
INSERT INTO content_audit_results 
  (file_path, content_type, has_placeholder, needs_depth, quality_indicators, deployment_status)
VALUES
  {','.join(chunk)}
ON CONFLICT (file_path) DO UPDATE SET
  content_type = EXCLUDED.content_type,
  has_placeholder = EXCLUDED.has_placeholder,
  needs_depth = EXCLUDED.needs_depth,
  quality_indicators = EXCLUDED.quality_indicators,
  deployment_status = EXCLUDED.deployment_status,
  updated_at = NOW();
"""
    
    # Save to temp file
    temp_file = f'/tmp/graphrag_upload_chunk_{i}.sql'
    with open(temp_file, 'w') as f:
        f.write(sql)
    
    print(f"📦 Chunk {i//chunk_size + 1}/{(len(all_values) + chunk_size - 1)//chunk_size}: {len(chunk)} records")

print(f"\n✅ SQL chunks prepared in /tmp/graphrag_upload_chunk_*.sql")
print(f"💡 Now executing via MCP Supabase...")

