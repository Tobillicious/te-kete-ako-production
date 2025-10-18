#!/usr/bin/env python3
"""
Explore GraphRAG Schema
Dives deeper into the schema of key tables.
"""

from supabase import create_client
import os

# Use the service key for full access
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

print("🧠 Exploring GraphRAG Schema")
print("=" * 70)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def explore_table(table_name):
    print(f"\n🔍 Exploring '{table_name}' table...")
    print("-" * 70)
    try:
        # Get total count
        result = supabase.table(table_name).select('*', count='exact').limit(1).execute()
        total = result.count if hasattr(result, 'count') else 'Unknown'
        print(f"  Total entries: {total}")

        # Get a sample record to inspect columns
        if total == 0 or total == 'Unknown':
            print("  Table is empty or inaccessible.")
            return

        sample = supabase.table(table_name).select('*').limit(1).execute()
        if sample.data:
            print("\n  Columns:")
            for key, value in sample.data[0].items():
                print(f"    - {key}: (e.g., '{str(value)[:50]}...')")
        else:
            print("  Could not retrieve a sample record.")

    except Exception as e:
        print(f"  ⚠️  Error exploring table '{table_name}': {e}")

# Explore the main tables
explore_table('resources')
explore_table('quality_assessments')
explore_table('knowledge_nodes')
explore_table('knowledge_edges')


print("\n" + "=" * 70)
print("✅ Schema exploration complete.")
