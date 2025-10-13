-- Supabase GraphRAG Coordination Tables
-- Run this in the Supabase SQL editor to initialize the coordination system

-- Agents table - Track all 12 agents
CREATE TABLE IF NOT EXISTS agents (
    id TEXT PRIMARY KEY,
    status TEXT NOT NULL DEFAULT 'inactive', -- active, inactive, busy
    capabilities TEXT[], -- Array of capabilities like ['styling', 'content', 'cultural']
    last_seen TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tasks table - Track task claiming and completion
CREATE TABLE IF NOT EXISTS tasks (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'unclaimed', -- unclaimed, claimed, completed
    claimed_by TEXT REFERENCES agents(id),
    claimed_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    priority TEXT DEFAULT 'medium', -- low, medium, high, critical
    outcome TEXT, -- Description of what was accomplished
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Decisions table - Track decisions made by agents
CREATE TABLE IF NOT EXISTS decisions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    agent_id TEXT REFERENCES agents(id),
    decision TEXT NOT NULL,
    rationale TEXT NOT NULL,
    alternatives TEXT[], -- Alternative options considered
    made_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Agent communications table - Track messages between agents
CREATE TABLE IF NOT EXISTS agent_communications (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    from_agent TEXT REFERENCES agents(id),
    to_agent TEXT REFERENCES agents(id), -- NULL for broadcast
    message TEXT NOT NULL,
    message_type TEXT DEFAULT 'info', -- info, question, request, alert
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    read_at TIMESTAMP WITH TIME ZONE
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_agents_status ON agents(status);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_tasks_claimed_by ON tasks(claimed_by);
CREATE INDEX IF NOT EXISTS idx_decisions_agent_id ON decisions(agent_id);
CREATE INDEX IF NOT EXISTS idx_decisions_made_at ON decisions(made_at);
CREATE INDEX IF NOT EXISTS idx_communications_from_agent ON agent_communications(from_agent);
CREATE INDEX IF NOT EXISTS idx_communications_to_agent ON agent_communications(to_agent);

-- Row Level Security (RLS) policies
-- Enable RLS on all tables
ALTER TABLE agents ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE decisions ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_communications ENABLE ROW LEVEL SECURITY;

-- Agents table policies
CREATE POLICY "Agents can view all agents" ON agents FOR SELECT USING (true);
CREATE POLICY "Agents can update their own record" ON agents FOR UPDATE USING (id = auth.jwt() ->> 'agent_id');

-- Tasks table policies
CREATE POLICY "All can view tasks" ON tasks FOR SELECT USING (true);
CREATE POLICY "Agents can create tasks" ON tasks FOR INSERT WITH CHECK (true);
CREATE POLICY "Agents can update tasks they claimed" ON tasks FOR UPDATE USING (claimed_by = auth.jwt() ->> 'agent_id');

-- Decisions table policies
CREATE POLICY "All can view decisions" ON decisions FOR SELECT USING (true);
CREATE POLICY "Agents can create decisions" ON decisions FOR INSERT WITH CHECK (agent_id = auth.jwt() ->> 'agent_id');

-- Communications table policies
CREATE POLICY "Agents can view communications involving them" ON agent_communications FOR SELECT USING (from_agent = auth.jwt() ->> 'agent_id' OR to_agent = auth.jwt() ->> 'agent_id' OR to_agent IS NULL);
CREATE POLICY "Agents can create communications" ON agent_communications FOR INSERT WITH CHECK (from_agent = auth.jwt() ->> 'agent_id');
CREATE POLICY "Agents can update read status" ON agent_communications FOR UPDATE USING (to_agent = auth.jwt() ->> 'agent_id');

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger to automatically update updated_at
CREATE TRIGGER update_agents_updated_at BEFORE UPDATE ON agents
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Insert sample data for testing
INSERT INTO agents (id, status, capabilities, last_seen) VALUES
('Agent-1', 'active', ARRAY['styling', 'css', 'frontend'], NOW()),
('Agent-2', 'active', ARRAY['content', 'cultural', 'mātauranga'], NOW()),
('Agent-3', 'active', ARRAY['navigation', 'structure', 'organization'], NOW()),
('Agent-4', 'inactive', ARRAY['testing', 'qa', 'accessibility'], NOW()),
('Agent-5', 'inactive', ARRAY['backend', 'api', 'database'], NOW())
ON CONFLICT (id) DO NOTHING;

-- Sample tasks
INSERT INTO tasks (description, status, priority) VALUES
('Fix CSS styling issues on homepage', 'unclaimed', 'high'),
('Add missing cultural context to resources', 'unclaimed', 'medium'),
('Improve navigation between pages', 'unclaimed', 'medium')
ON CONFLICT DO NOTHING;

-- Sample decisions
INSERT INTO decisions (agent_id, decision, rationale, alternatives) VALUES
('Agent-1', 'Use te-kete-professional.css as main stylesheet', 'Single CSS file reduces conflicts and improves performance', ARRAY['Use multiple CSS files', 'Use inline styles'])
ON CONFLICT DO NOTHING;

-- Create a view for agent status summary
CREATE OR REPLACE VIEW agent_status_summary AS
SELECT 
    a.id,
    a.status,
    a.capabilities,
    a.last_seen,
    COUNT(t.id) as claimed_tasks,
    COUNT(d.id) as decisions_made
FROM agents a
LEFT JOIN tasks t ON a.id = t.claimed_by AND t.status = 'claimed'
LEFT JOIN decisions d ON a.id = d.agent_id
GROUP BY a.id, a.status, a.capabilities, a.last_seen
ORDER BY a.last_seen DESC;

-- Create a view for task summary
CREATE OR REPLACE VIEW task_summary AS
SELECT 
    t.id,
    t.description,
    t.status,
    t.priority,
    t.claimed_by,
    t.claimed_at,
    t.completed_at,
    CASE 
        WHEN t.status = 'completed' THEN '✅'
        WHEN t.status = 'claimed' THEN '🔄'
        ELSE '⏳'
    END as status_icon
FROM tasks t
ORDER BY 
    CASE t.priority 
        WHEN 'critical' THEN 1 
        WHEN 'high' THEN 2 
        WHEN 'medium' THEN 3 
        ELSE 4 
    END,
    t.created_at DESC;
