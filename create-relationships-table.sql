-- ================================================================
-- CREATE GRAPHRAG RELATIONSHIPS TABLE
-- ================================================================
-- Run this in Supabase SQL Editor to enable relationship building
-- ================================================================

-- 1. Create the relationships table
CREATE TABLE IF NOT EXISTS graphrag_relationships (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    source_id UUID REFERENCES resources(id) ON DELETE CASCADE,
    target_id UUID REFERENCES resources(id) ON DELETE CASCADE,
    relationship_type TEXT NOT NULL,
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0 AND confidence_score <= 1),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_relationships_source ON graphrag_relationships(source_id);
CREATE INDEX IF NOT EXISTS idx_relationships_target ON graphrag_relationships(target_id);
CREATE INDEX IF NOT EXISTS idx_relationships_type ON graphrag_relationships(relationship_type);
CREATE INDEX IF NOT EXISTS idx_relationships_confidence ON graphrag_relationships(confidence_score DESC);
CREATE INDEX IF NOT EXISTS idx_relationships_source_target ON graphrag_relationships(source_id, target_id);

-- 3. Prevent duplicate relationships
CREATE UNIQUE INDEX IF NOT EXISTS idx_relationships_unique 
ON graphrag_relationships(source_id, target_id, relationship_type);

-- 4. Add helpful documentation
COMMENT ON TABLE graphrag_relationships IS 'Intelligent relationships between resources for discovery and recommendations';
COMMENT ON COLUMN graphrag_relationships.relationship_type IS 'Types: variant_of, same_subject, same_year_level, lesson_has_handout, unit_contains_lesson, prerequisite, related_topic, cultural_pair';
COMMENT ON COLUMN graphrag_relationships.confidence_score IS 'Similarity/confidence score 0.0-1.0';

-- 5. Enable Row Level Security
ALTER TABLE graphrag_relationships ENABLE ROW LEVEL SECURITY;

-- 6. Create security policies
CREATE POLICY "Allow public read access to relationships"
ON graphrag_relationships FOR SELECT
TO public
USING (true);

CREATE POLICY "Allow authenticated users to insert relationships"
ON graphrag_relationships FOR INSERT
TO authenticated
WITH CHECK (true);

CREATE POLICY "Allow service role full access"
ON graphrag_relationships FOR ALL
TO service_role
USING (true);

-- ================================================================
-- VERIFICATION QUERIES (run after to verify)
-- ================================================================

-- Check table exists
SELECT EXISTS (
    SELECT FROM information_schema.tables 
    WHERE table_schema = 'public' 
    AND table_name = 'graphrag_relationships'
) as table_exists;

-- Check indexes
SELECT indexname, indexdef 
FROM pg_indexes 
WHERE tablename = 'graphrag_relationships';

-- Check policies
SELECT policyname, cmd, qual 
FROM pg_policies 
WHERE tablename = 'graphrag_relationships';

-- ================================================================
-- YOU'RE READY!
-- After running this, run: python3 build-relationships-intelligent.py
-- ================================================================
