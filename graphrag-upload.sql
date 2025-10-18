
-- Upload resources to GraphRAG
-- Run this in Supabase SQL editor

-- First, ensure table exists (if not already created)
CREATE TABLE IF NOT EXISTS graphrag_resources (
    id BIGSERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content_path TEXT UNIQUE,
    resource_type TEXT,
    quality_score INTEGER,
    status TEXT,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS graphrag_relationships (
    id BIGSERIAL PRIMARY KEY,
    from_path TEXT,
    to_path TEXT,
    relationship_type TEXT,
    confidence FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_resources_path ON graphrag_resources(content_path);
CREATE INDEX IF NOT EXISTS idx_resources_status ON graphrag_resources(status);
CREATE INDEX IF NOT EXISTS idx_relationships_from ON graphrag_relationships(from_path);
CREATE INDEX IF NOT EXISTS idx_relationships_to ON graphrag_relationships(to_path);
