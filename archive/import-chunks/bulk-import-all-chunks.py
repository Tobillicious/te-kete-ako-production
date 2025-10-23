#!/usr/bin/env python3
"""
BULK IMPORT - Import all 212 micro-chunks via Supabase MCP
Uses the MCP Supabase tool to import systematically
"""

import subprocess
import json
from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
CHUNK_FILES = sorted(SCRIPT_DIR.glob("micro-*.sql"))

print("=" * 80)
print("🚀 BULK GRAPHRAG IMPORT - All 212 Chunks")
print("=" * 80)
print()
print(f"📂 Found {len(CHUNK_FILES)} chunk files")
print()

# Read all chunks and combine into one SQL
print("📝 Combining all chunks...")
full_sql_parts = []

# Add header once
with open(CHUNK_FILES[0], 'r') as f:
    lines = f.readlines()
    header = ''.join(lines[:8])  # Header lines
    
full_sql_parts.append(header)

# Add all VALUES from all chunks
all_values = []
for i, chunk_file in enumerate(CHUNK_FILES, 1):
    if i % 20 == 0:
        print(f"  Processing chunk {i}/{len(CHUNK_FILES)}...")
    
    with open(chunk_file, 'r') as f:
        lines = f.readlines()
        # Skip header (first 8 lines) and footer (last 5 lines)
        values_section = ''.join(lines[8:-5])
        all_values.append(values_section)

# Join all values
combined_values = ',\n'.join(all_values)
# Remove any trailing comma
combined_values = combined_values.rstrip(',')

# Add footer
footer = """
ON CONFLICT (file_path) DO UPDATE SET
  title = EXCLUDED.title,
  resource_type = EXCLUDED.resource_type,
  quality_score = EXCLUDED.quality_score,
  cultural_context = EXCLUDED.cultural_context,
  updated_at = NOW();
"""

full_sql = header + combined_values + footer

# Write combined SQL
output_file = SCRIPT_DIR / "graphrag-combined-import.sql"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(full_sql)

print(f"✅ Combined SQL written: {output_file}")
print(f"📊 Size: {len(full_sql):,} characters")
print()
print("=" * 80)
print("✅ READY TO IMPORT!")
print()
print("Next steps:")
print("  1. Open Supabase Dashboard:")
print("     https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql/new")
print()
print("  2. Copy the SQL file:")
print(f"     cat {output_file} | pbcopy")
print()
print("  3. Paste and RUN in Supabase")
print()
print("  OR use psql if you have database password")
print("=" * 80)

