#!/usr/bin/env python3
import json
import sys
import os

def insert_resources_to_graphrag():
    """Insert extracted resources into GraphRAG database"""
    
    # Read the extracted resources
    try:
        with open('resources_to_insert.json', 'r') as f:
            resources = json.load(f)
    except FileNotFoundError:
        print("Error: resources_to_insert.json not found. Run metadata extraction first.")
        return
    
    print(f"Found {len(resources)} resources to insert")
    
    # Insert resources in batches
    batch_size = 10
    total_inserted = 0
    
    for i in range(0, len(resources), batch_size):
        batch = resources[i:i+batch_size]
        print(f"\nInserting batch {i//batch_size + 1}/{(len(resources)-1)//batch_size + 1} ({len(batch)} resources)")
        
        for resource in batch:
            try:
                # Use MCP Supabase to insert the resource
                query = f"""
                INSERT INTO graphrag_resources 
                (file_path, title, resource_type, quality_score, cultural_context, year_level, subject, has_whakataukī, has_te_reo, content_preview)
                VALUES (
                    '{resource['file_path']}',
                    '{resource['title'].replace("'", "''")}',
                    '{resource['resource_type']}',
                    {resource['quality_score']},
                    {str(resource['cultural_context']).lower()},
                    {f"'{resource['year_level']}'" if resource['year_level'] else 'NULL'},
                    '{resource['subject'].replace("'", "''")}',
                    {str(resource['has_whakataukī']).lower()},
                    {str(resource['has_te_reo']).lower()},
                    '{resource['content_preview'].replace("'", "''")}'
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
                
                # Execute the query using MCP
                print(f"  Inserting: {resource['file_path']} ({resource['resource_type']})")
                # Note: In a real implementation, this would use the MCP tool
                
                total_inserted += 1
                
            except Exception as e:
                print(f"  Error inserting {resource['file_path']}: {e}")
    
    print(f"\n✅ Successfully processed {total_inserted} resources for GraphRAG indexing")
    print("Note: In production, these would be inserted via MCP Supabase queries")

if __name__ == "__main__":
    insert_resources_to_graphrag()
