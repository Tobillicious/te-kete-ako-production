#!/usr/bin/env python3
"""
Convert backup_migration_catalog.json to SQL INSERT statements
for batch loading into graphrag_resources table
"""

import json
from pathlib import Path

CATALOG_FILE = Path("/Users/admin/Documents/te-kete-ako-clean/backup_migration_catalog.json")
OUTPUT_FILE = Path("/Users/admin/Documents/te-kete-ako-clean/backup_load_sql.sql")

def generate_sql_insert(resources):
    """Generate SQL INSERT statement for batch loading"""
    
    sql_lines = [
        "-- BACKUP MIGRATION: BATCH LOAD TO GRAPHRAG_RESOURCES",
        "-- Generated from: backup_migration_catalog.json",
        "-- Resources: " + str(len(resources)),
        "",
        "INSERT INTO graphrag_resources (",
        "    file_path, resource_type, title, quality_score, cultural_context,",
        "    year_level, subject, canonical_subject, has_te_reo, has_whakataukī,",
        "    content_preview, metadata, archive_status, is_backup, backup_type,",
        "    created_at, updated_at",
        ") VALUES",
        ""
    ]
    
    for idx, resource in enumerate(resources):
        # Escape single quotes in strings
        def sql_quote(s):
            if s is None:
                return "NULL"
            return "'" + str(s).replace("'", "''") + "'"
        
        subject = resource.get("subject", "Cross-Curricular")
        metadata = {
            "subject": subject,
            "year_level": resource.get("year_level"),
            "content_type": resource.get("content_type"),
            "has_te_reo": resource.get("has_te_reo", False),
            "has_whakataukī": resource.get("has_whakataukī", False)
        }
        
        values = [
            sql_quote(resource["file_path"]),  # file_path
            sql_quote(resource["content_type"]),  # resource_type
            sql_quote(resource["title"]),  # title
            str(resource["quality_score"]),  # quality_score
            "true",  # cultural_context
            sql_quote(resource["year_level"]),  # year_level
            sql_quote(subject),  # subject
            sql_quote(subject),  # canonical_subject (same as subject)
            "true" if resource.get("has_te_reo") else "false",  # has_te_reo
            "true" if resource.get("has_whakataukī") else "false",  # has_whakataukī
            sql_quote(resource["content_preview"][:500]),  # content_preview (limit to 500)
            sql_quote(json.dumps(metadata)),  # metadata
            "'active'",  # archive_status
            "true",  # is_backup
            "'pre_css_migration'",  # backup_type
            "NOW()",  # created_at
            "NOW()"  # updated_at
        ]
        
        line = "(" + ", ".join(values) + ")"
        
        if idx < len(resources) - 1:
            line += ","
        
        sql_lines.append(line)
    
    sql_lines.extend([
        "",
        "ON CONFLICT (file_path) DO NOTHING;",
        "",
        "-- VERIFICATION",
        "SELECT COUNT(*) as total_inserted FROM graphrag_resources WHERE is_backup = true;",
        ""
    ])
    
    return "\n".join(sql_lines)

def main():
    print("📖 Reading extraction catalog...")
    with open(CATALOG_FILE) as f:
        resources = json.load(f)
    
    print(f"📝 Generating SQL for {len(resources)} resources...")
    sql = generate_sql_insert(resources)
    
    print(f"💾 Writing to {OUTPUT_FILE}...")
    OUTPUT_FILE.write_text(sql)
    
    print(f"✅ SQL generated successfully!")
    print(f"   File: {OUTPUT_FILE}")
    print(f"   Lines: {len(sql.split(chr(10)))}")
    print(f"   Resources: {len(resources)}")

if __name__ == "__main__":
    main()
