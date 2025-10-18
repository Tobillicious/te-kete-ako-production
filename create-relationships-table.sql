-- CREATE RELATIONSHIPS TABLE IN SUPABASE
-- This transforms GraphRAG from flat database to true knowledge GRAPH
-- Enables graph queries, learning pathways, network analysis

-- Drop if exists (for clean start)
DROP TABLE IF EXISTS resource_relationships CASCADE;

-- Create relationships table
CREATE TABLE resource_relationships (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_path TEXT NOT NULL,
  target_path TEXT NOT NULL,
  relationship_type TEXT DEFAULT 'links_to',
  strength INTEGER DEFAULT 1,
  created_at TIMESTAMP DEFAULT NOW(),
  metadata JSONB DEFAULT '{}'::jsonb
);

-- Create indexes for fast queries
CREATE INDEX idx_relationships_source ON resource_relationships(source_path);
CREATE INDEX idx_relationships_target ON resource_relationships(target_path);
CREATE INDEX idx_relationships_type ON resource_relationships(relationship_type);

-- Create view for easy queries
CREATE OR REPLACE VIEW resource_graph AS
SELECT 
  r1.path as source_path,
  r1.title as source_title,
  r1.type as source_type,
  rr.relationship_type,
  r2.path as target_path,
  r2.title as target_title,
  r2.type as target_type
FROM resource_relationships rr
LEFT JOIN resources r1 ON rr.source_path = r1.path
LEFT JOIN resources r2 ON rr.target_path = r2.path;

-- Grant access
GRANT SELECT, INSERT, UPDATE ON resource_relationships TO anon, authenticated;
GRANT SELECT ON resource_graph TO anon, authenticated;

-- Success message
SELECT 'Relationships table created! Ready for 85,291 connections!' as status;

