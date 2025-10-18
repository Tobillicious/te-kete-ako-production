#!/usr/bin/env python3
"""
Create GraphRAG tables in Supabase
"""
import os
import requests
import json

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

headers = {
    'apikey': SUPABASE_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=minimal'
}

print("🔍 Checking existing tables...")

# Check resources table
try:
    response = requests.get(
        f'{SUPABASE_URL}/rest/v1/graphrag_resources?limit=1',
        headers=headers
    )
    print(f"   📊 graphrag_resources: {response.status_code}")
    if response.status_code == 200:
        print(f"      ✅ Table exists with data")
except Exception as e:
    print(f"   ❌ graphrag_resources: {str(e)}")

# Check relationships table
try:
    response = requests.get(
        f'{SUPABASE_URL}/rest/v1/graphrag_relationships?limit=1',
        headers=headers
    )
    print(f"   📊 graphrag_relationships: {response.status_code}")
    if response.status_code == 200:
        print(f"      ✅ Table exists with data")
except Exception as e:
    print(f"   ❌ graphrag_relationships: {str(e)}")

print("\n📋 SQL to run in Supabase SQL Editor:")
print("=" * 70)
print("""
-- Create resources table
CREATE TABLE IF NOT EXISTS graphrag_resources (
    id SERIAL PRIMARY KEY,
    file_path TEXT UNIQUE NOT NULL,
    resource_type TEXT,
    title TEXT,
    quality_score INTEGER,
    cultural_context BOOLEAN DEFAULT FALSE,
    year_level TEXT,
    subject TEXT,
    unit TEXT,
    whakataukī BOOLEAN DEFAULT FALSE,
    te_reo_māori BOOLEAN DEFAULT FALSE,
    content_preview TEXT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create relationships table
CREATE TABLE IF NOT EXISTS graphrag_relationships (
    id SERIAL PRIMARY KEY,
    source_path TEXT NOT NULL,
    target_path TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_resources_path ON graphrag_resources(file_path);
CREATE INDEX IF NOT EXISTS idx_resources_type ON graphrag_resources(resource_type);
CREATE INDEX IF NOT EXISTS idx_resources_quality ON graphrag_resources(quality_score);
CREATE INDEX IF NOT EXISTS idx_relationships_source ON graphrag_relationships(source_path);
CREATE INDEX IF NOT EXISTS idx_relationships_target ON graphrag_relationships(target_path);
CREATE INDEX IF NOT EXISTS idx_relationships_type ON graphrag_relationships(relationship_type);

-- Enable Row Level Security (optional, for public access)
ALTER TABLE graphrag_resources ENABLE ROW LEVEL SECURITY;
ALTER TABLE graphrag_relationships ENABLE ROW LEVEL SECURITY;

-- Create policies for anon access (if needed)
CREATE POLICY "Enable read access for all users" ON graphrag_resources FOR SELECT USING (true);
CREATE POLICY "Enable read access for all users" ON graphrag_relationships FOR SELECT USING (true);
""")
print("=" * 70)
print("\n💡 Run this SQL in Supabase dashboard → SQL Editor")
print("   Then re-run upload-to-supabase.py")

