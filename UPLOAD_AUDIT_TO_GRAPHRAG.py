#!/usr/bin/env python3
"""
Upload content audit results to GraphRAG/Supabase
"""

import json
import os

# Read audit data
with open('deployment_reports/content_audit_20251020_014708.json', 'r') as f:
    audit_data = json.load(f)

print(f"📊 Loading {len(audit_data)} audit records into GraphRAG...")

# Generate SQL INSERT statements in batches
batch_size = 100
total = len(audit_data)

sql_batches = []

for i in range(0, total, batch_size):
    batch = audit_data[i:i+batch_size]
    
    values = []
    for record in batch:
        file_path = record['file'].replace("'", "''")  # Escape quotes
        content_type = record['type']
        has_placeholder = 'TRUE' if record['has_placeholder'] else 'FALSE'
        needs_depth = 'TRUE' if record['needs_depth'] else 'FALSE'
        
        # Convert quality indicators to PostgreSQL array
        indicators = record.get('quality_indicators', [])
        indicators_str = "ARRAY[" + ",".join([f"'{ind}'" for ind in indicators]) + "]" if indicators else "ARRAY[]::TEXT[]"
        
        values.append(
            f"('{file_path}', '{content_type}', {has_placeholder}, {needs_depth}, {indicators_str}, 'clean')"
        )
    
    sql = f"""
INSERT INTO content_audit_results 
  (file_path, content_type, has_placeholder, needs_depth, quality_indicators, deployment_status)
VALUES
  {','.join(values)}
ON CONFLICT (file_path) DO UPDATE SET
  content_type = EXCLUDED.content_type,
  has_placeholder = EXCLUDED.has_placeholder,
  needs_depth = EXCLUDED.needs_depth,
  quality_indicators = EXCLUDED.quality_indicators,
  deployment_status = EXCLUDED.deployment_status,
  updated_at = NOW();
"""
    
    sql_batches.append(sql)
    print(f"✅ Batch {i//batch_size + 1}/{(total + batch_size - 1)//batch_size} prepared ({len(batch)} records)")

# Save SQL to file
with open('deployment_reports/upload_to_graphrag.sql', 'w') as f:
    f.write('\n\n'.join(sql_batches))

print(f"\n💾 SQL saved to: deployment_reports/upload_to_graphrag.sql")
print(f"🚀 Ready to upload {total} records to GraphRAG!")

