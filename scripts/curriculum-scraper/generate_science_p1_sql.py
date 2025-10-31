#!/usr/bin/env python3
"""
Generate SQL INSERT statements for Science Phase 1
"""

import json

# Import the statements from insert_science_p1.py
from insert_science_p1 import statements

sql_inserts = []

for group in statements:
    for statement_text in group["statements"]:
        # Escape single quotes in SQL
        escaped_statement = statement_text.replace("'", "''")
        
        # Build the INSERT statement
        sql = f"""INSERT INTO curriculum_statements (
    curriculum_version, version_status, learning_area, phase, strand, sub_strand,
    element, statement_text, year_levels, tahurangi_url
) VALUES (
    '{group["curriculum_version"]}',
    '{group["version_status"]}',
    '{group["learning_area"]}',
    '{group["phase"]}',
    '{group["strand"]}',
    '{group.get("sub_strand", "")}',
    '{group["element"]}',
    '{escaped_statement}',
    ARRAY{group["year_levels"]},
    'https://newzealandcurriculum.tahurangi.education.govt.nz/new-zealand-curriculum-online/nzc---science-phase-1-years-0-3/5637292339.p'
);"""
        
        sql_inserts.append(sql)

# Write to file
output_file = "science_phase_1_inserts.sql"
with open(output_file, "w") as f:
    f.write("-- Science Phase 1 (Years 0-3) Curriculum Statements\n")
    f.write("-- Total: 137 statements\n")
    f.write("-- Extracted: October 29, 2025\n\n")
    f.write("\n\n".join(sql_inserts))
    f.write("\n")

print(f"✅ Generated {len(sql_inserts)} SQL INSERT statements")
print(f"📄 Saved to: {output_file}")
print(f"\n🚀 Now executing via MCP Supabase...")

