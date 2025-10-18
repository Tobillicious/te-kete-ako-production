#!/usr/bin/env python3
"""
Create relationships table in Supabase via API
"""

from supabase_graphrag_connector import SupabaseGraphRAGConnector
import os

print("🔗 CREATING RELATIONSHIPS TABLE IN SUPABASE")
print("=" * 70)

# Connect to Supabase
connector = SupabaseGraphRAGConnector()
supabase = connector.client

# SQL to create relationships table
create_table_sql = """
-- Create relationships table for knowledge graph
CREATE TABLE IF NOT EXISTS relationships (
    id BIGSERIAL PRIMARY KEY,
    source_path TEXT NOT NULL,
    target_path TEXT NOT NULL,
    relationship_type TEXT NOT NULL DEFAULT 'links_to',
    strength INTEGER DEFAULT 1,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_relationships_source ON relationships(source_path);
CREATE INDEX IF NOT EXISTS idx_relationships_target ON relationships(target_path);
CREATE INDEX IF NOT EXISTS idx_relationships_type ON relationships(relationship_type);
CREATE INDEX IF NOT EXISTS idx_relationships_source_target ON relationships(source_path, target_path);

-- Create updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

DROP TRIGGER IF EXISTS update_relationships_updated_at ON relationships;
CREATE TRIGGER update_relationships_updated_at
    BEFORE UPDATE ON relationships
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Grant permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON relationships TO anon;
GRANT SELECT, INSERT, UPDATE, DELETE ON relationships TO authenticated;
"""

try:
    # Try to execute SQL via RPC or direct query
    print("📋 Attempting to create table via API...")
    
    # Try using the PostgreSQL REST API
    response = supabase.postgrest.rpc('exec', {'query': create_table_sql}).execute()
    
    print("✅ Table created successfully!")
    
except Exception as e:
    print(f"⚠️  API creation failed: {e}")
    print("\n📝 Alternative: Run this SQL manually in Supabase SQL editor:")
    print("-" * 70)
    print(create_table_sql)
    print("-" * 70)
    print("\nThen run: python3 import-relationships-to-supabase.py")

print("\n" + "=" * 70)

