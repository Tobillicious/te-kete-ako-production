-- GraphRAG Tables for Te Kete Ako Site Structure
-- These tables will store the comprehensive site map and relationships

-- Table for storing site structure (files, dependencies, etc.)
CREATE TABLE IF NOT EXISTS site_structure (
  id SERIAL PRIMARY KEY,
  path TEXT NOT NULL,
  type TEXT NOT NULL, -- html, css, js, image, etc.
  page_type TEXT, -- homepage, unit, lesson, handout, etc.
  title TEXT,
  description TEXT,
  css_links TEXT[], -- Array of CSS file paths
  js_scripts TEXT[], -- Array of JS file paths
  internal_links TEXT[], -- Array of internal link paths
  components TEXT[], -- Array of component paths
  content TEXT, -- First 1000 chars of content for search
  project_root TEXT NOT NULL,
  crawled_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  UNIQUE(path, project_root)
);

-- Table for storing content hierarchy (Units → Lessons → Handouts)
CREATE TABLE IF NOT EXISTS content_hierarchy (
  id SERIAL PRIMARY KEY,
  type TEXT NOT NULL, -- unit, lesson, handout
  path TEXT NOT NULL,
  name TEXT NOT NULL,
  parent TEXT, -- Path to parent item
  children JSONB, -- Array of child items with path and name
  metadata JSONB, -- Additional metadata
  project_root TEXT NOT NULL,
  crawled_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  UNIQUE(path, project_root)
);

-- Table for storing duplicate files and conflicts
CREATE TABLE IF NOT EXISTS duplicate_files (
  id SERIAL PRIMARY KEY,
  file_name TEXT NOT NULL,
  paths TEXT[] NOT NULL, -- Array of file paths
  similarity_score FLOAT, -- For potential near-duplicates
  resolution_status TEXT DEFAULT 'unresolved', -- unresolved, reviewed, merged, deleted
  project_root TEXT NOT NULL,
  identified_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Table for storing navigation structure
CREATE TABLE IF NOT EXISTS navigation_structure (
  id SERIAL PRIMARY KEY,
  nav_type TEXT NOT NULL, -- header, footer, sidebar, breadcrumb
  path TEXT NOT NULL,
  title TEXT NOT NULL,
  parent_path TEXT, -- For nested navigation
  order_index INTEGER,
  is_active BOOLEAN DEFAULT TRUE,
  project_root TEXT NOT NULL,
  crawled_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Table for storing CSS conflicts
CREATE TABLE IF NOT EXISTS css_conflicts (
  id SERIAL PRIMARY KEY,
  selector TEXT NOT NULL,
  file_paths TEXT[] NOT NULL, -- Files that define this selector
  conflict_type TEXT NOT NULL, -- duplicate, override, incompatible
  severity TEXT DEFAULT 'medium', -- low, medium, high, critical
  resolution_status TEXT DEFAULT 'unresolved',
  project_root TEXT NOT NULL,
  identified_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for efficient querying
CREATE INDEX IF NOT EXISTS idx_site_structure_path ON site_structure(path);
CREATE INDEX IF NOT EXISTS idx_site_structure_type ON site_structure(type);
CREATE INDEX IF NOT EXISTS idx_site_structure_page_type ON site_structure(page_type);
CREATE INDEX IF NOT EXISTS idx_content_hierarchy_type ON content_hierarchy(type);
CREATE INDEX IF NOT EXISTS idx_content_hierarchy_path ON content_hierarchy(path);
CREATE INDEX IF NOT EXISTS idx_content_hierarchy_parent ON content_hierarchy(parent);
CREATE INDEX IF NOT EXISTS idx_duplicate_files_name ON duplicate_files(file_name);
CREATE INDEX IF NOT EXISTS idx_navigation_structure_type ON navigation_structure(nav_type);
CREATE INDEX IF NOT EXISTS idx_css_conflicts_selector ON css_conflicts(selector);

-- Enable full-text search on content
CREATE INDEX IF NOT EXISTS idx_site_structure_content_fts ON site_structure USING gin(to_tsvector('english', content));

-- Row Level Security (RLS) for public access
ALTER TABLE site_structure ENABLE ROW LEVEL SECURITY;
ALTER TABLE content_hierarchy ENABLE ROW LEVEL SECURITY;
ALTER TABLE duplicate_files ENABLE ROW LEVEL SECURITY;
ALTER TABLE navigation_structure ENABLE ROW LEVEL SECURITY;
ALTER TABLE css_conflicts ENABLE ROW LEVEL SECURITY;

-- Policies for public read access
CREATE POLICY "Public read access to site_structure" ON site_structure
  FOR SELECT USING (true);

CREATE POLICY "Public read access to content_hierarchy" ON content_hierarchy
  FOR SELECT USING (true);

CREATE POLICY "Public read access to duplicate_files" ON duplicate_files
  FOR SELECT USING (true);

CREATE POLICY "Public read access to navigation_structure" ON navigation_structure
  FOR SELECT USING (true);

CREATE POLICY "Public read access to css_conflicts" ON css_conflicts
  FOR SELECT USING (true);

-- Functions for the crawler to call
CREATE OR REPLACE FUNCTION create_site_structure_table()
RETURNS void AS $$
BEGIN
  -- Table already created above
  NULL;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_content_hierarchy_table()
RETURNS void AS $$
BEGIN
  -- Table already created above
  NULL;
END;
$$ LANGUAGE plpgsql;
