-- Deploy only the resources table to existing Supabase database
-- This adds the resources table to the existing schema

-- Create the resources table
CREATE TABLE IF NOT EXISTS resources (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    path TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    type TEXT NOT NULL CHECK (type IN ('handout', 'lesson', 'game', 'unit-plan', 'assessment', 'activity', 'video', 'interactive')),
    subject TEXT NOT NULL,
    level TEXT NOT NULL,
    featured BOOLEAN DEFAULT FALSE,
    tags TEXT[] DEFAULT '{}',
    curriculum_alignment JSONB DEFAULT '{}',
    cultural_elements JSONB DEFAULT '{}',
    difficulty_level TEXT CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')) DEFAULT 'intermediate',
    estimated_duration_minutes INTEGER,
    author TEXT DEFAULT 'Te Kete Ako Team',
    is_active BOOLEAN DEFAULT TRUE
);

-- Enable Row Level Security
ALTER TABLE resources ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY "Allow all authenticated users to view resources" ON resources
    FOR SELECT USING (auth.role() = 'authenticated' OR is_active = true);

CREATE POLICY "Allow teachers to manage resources" ON resources
    FOR ALL USING (
        EXISTS (
            SELECT 1 FROM profiles 
            WHERE user_id = auth.uid() 
            AND role IN ('teacher', 'admin')
        )
    );

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_resources_type ON resources(type);
CREATE INDEX IF NOT EXISTS idx_resources_subject ON resources(subject);
CREATE INDEX IF NOT EXISTS idx_resources_level ON resources(level);
CREATE INDEX IF NOT EXISTS idx_resources_featured ON resources(featured) WHERE featured = true;
CREATE INDEX IF NOT EXISTS idx_resources_created_at ON resources(created_at);
CREATE INDEX IF NOT EXISTS idx_resources_active ON resources(is_active) WHERE is_active = true;
CREATE INDEX IF NOT EXISTS idx_resources_tags ON resources USING GIN(tags);

-- Create trigger for automatic updated_at timestamp
CREATE TRIGGER update_resources_updated_at 
    BEFORE UPDATE ON resources 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();