#!/usr/bin/env python3
"""
Batch load backup resources into graphrag_resources table
Reads backup_migration_catalog.json directly and inserts via prepared statements
"""

import json
from pathlib import Path

CATALOG_FILE = Path("/Users/admin/Documents/te-kete-ako-clean/backup_migration_catalog.json")

def generate_batch_sql(resources, batch_size=100):
    """Generate SQL batches (100 at a time) for safe database loading"""
    
    batches = []
    
    for i in range(0, len(resources), batch_size):
        batch = resources[i:i+batch_size]
        
        sql_lines = [
            f"-- BATCH {i//batch_size + 1}: Resources {i+1} to {min(i+batch_size, len(resources))}",
            "",
            "INSERT INTO graphrag_resources (",
            "    file_path, resource_type, title, quality_score, cultural_context,",
            "    year_level, subject, canonical_subject, has_te_reo, has_whakataukī,",
            "    content_preview, metadata, archive_status, is_backup, backup_type,",
            "    created_at, updated_at",
            ") VALUES",
            ""
        ]
        
        def sql_quote(s):
            if s is None:
                return "NULL"
            return "'" + str(s).replace("'", "''") + "'"
        
        for idx, resource in enumerate(batch):
            subject = resource.get("subject", "Cross-Curricular")
            metadata = {
                "subject": subject,
                "year_level": resource.get("year_level"),
                "content_type": resource.get("content_type"),
                "has_te_reo": resource.get("has_te_reo", False),
                "has_whakataukī": resource.get("has_whakataukī", False)
            }
            
            values = [
                sql_quote(resource["file_path"]),
                sql_quote(resource["content_type"]),
                sql_quote(resource["title"]),
                str(resource["quality_score"]),
                "true",
                sql_quote(resource["year_level"]),
                sql_quote(subject),
                sql_quote(subject),
                "true" if resource.get("has_te_reo") else "false",
                "true" if resource.get("has_whakataukī") else "false",
                sql_quote(resource["content_preview"][:500]),
                sql_quote(json.dumps(metadata)),
                "'active'",
                "true",
                "'pre_css_migration'",
                "NOW()",
                "NOW()"
            ]
            
            line = "(" + ", ".join(values) + ")"
            if idx < len(batch) - 1:
                line += ","
            
            sql_lines.append(line)
        
        sql_lines.extend([
            "",
            "ON CONFLICT (file_path) DO NOTHING;",
            ""
        ])
        
        batches.append("\n".join(sql_lines))
    
    return batches

def main():
    print("📖 Reading extraction catalog...")
    with open(CATALOG_FILE) as f:
        resources = json.load(f)
    
    print(f"📦 Generating {len(resources)} resources in batches...")
    batches = generate_batch_sql(resources, batch_size=100)
    
    # Write all batches to a master file
    master_file = Path("/Users/admin/Documents/te-kete-ako-clean/backup_batches_all.sql")
    all_sql = "\n\n".join(batches)
    master_file.write_text(all_sql)
    
    print(f"✅ Batches generated successfully!")
    print(f"   Total batches: {len(batches)}")
    print(f"   Master file: {master_file}")
    print(f"   Total SQL size: {len(all_sql)} bytes")
    print("")
    print("📊 SUMMARY:")
    print(f"   Resources to load: {len(resources)}")
    print(f"   Batch size: 100 resources per batch")
    print(f"   Total batches: {len(batches)}")
    print("")
    print("🚀 NEXT: Load master SQL file via Supabase MCP")

if __name__ == "__main__":
    main()
