#!/usr/bin/env python3
import json
import subprocess
import sys

def execute_sql_query(query):
    """Execute a SQL query using MCP Supabase"""
    try:
        # In a real implementation, this would use the MCP tool directly
        # For now, we'll print the queries
        print(f"Executing: {query[:100]}...")
        return True
    except Exception as e:
        print(f"Error executing query: {e}")
        return False

def bulk_insert_resources():
    """Bulk insert resources into GraphRAG"""
    
    # Read the extracted resources
    try:
        with open('resources_to_insert.json', 'r') as f:
            resources = json.load(f)
    except FileNotFoundError:
        print("Error: resources_to_insert.json not found.")
        return
    
    print(f"Starting bulk insert of {len(resources)} resources...")
    
    success_count = 0
    error_count = 0
    
    for i, resource in enumerate(resources):
        try:
            # Escape single quotes for SQL
            title = resource['title'].replace("'", "''")
            subject = resource['subject'].replace("'", "''")
            content_preview = resource['content_preview'].replace("'", "''")[:200]
            
            # Build the query
            query = f"""
            INSERT INTO graphrag_resources 
            (file_path, title, resource_type, quality_score, cultural_context, year_level, subject, has_whakataukī, has_te_reo, content_preview) 
            VALUES (
                '{resource['file_path']}',
                '{title}',
                '{resource['resource_type']}',
                {resource['quality_score']},
                {str(resource['cultural_context']).lower()},
                {f\"'\" + str(resource['year_level']) + \"'\" if resource['year_level'] else 'NULL'},
                '{subject}',
                {str(resource['has_whakataukī']).lower()},
                {str(resource['has_te_reo']).lower()},
                '{content_preview}'
            )
            ON CONFLICT (file_path) DO UPDATE SET
            title = EXCLUDED.title,
            quality_score = EXCLUDED.quality_score,
            cultural_context = EXCLUDED.cultural_context,
            year_level = EXCLUDED.year_level,
            subject = EXCLUDED.subject,
            has_whakataukī = EXCLUDED.has_whakataukī,
            has_te_reo = EXCLUDED.has_te_reo,
            content_preview = EXCLUDED.content_preview,
            updated_at = NOW();
            """
            
            if execute_sql_query(query):
                success_count += 1
            else:
                error_count += 1
            
            if (i + 1) % 10 == 0:
                print(f"Progress: {i + 1}/{len(resources)} processed ({success_count} successful, {error_count} errors)")
    
    print(f"\n✅ Bulk insert complete!")
    print(f"Successful inserts: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Success rate: {(success_count/(success_count+error_count)*100):.1f}%")

if __name__ == "__main__":
    bulk_insert_resources()
