-- ============================================
-- MULTI-AGENT COORDINATION SYSTEM
-- Te Kete Ako - GraphRAG-Based Agent Collaboration
-- ============================================

-- 1. AGENT ACTIVITY TRACKING
-- Track what each agent is doing in real-time
CREATE TABLE IF NOT EXISTS agent_activity (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id TEXT NOT NULL,
    agent_name TEXT NOT NULL,
    status TEXT NOT NULL, -- 'active', 'idle', 'offline'
    current_task TEXT,
    task_priority TEXT, -- 'high', 'medium', 'low'
    started_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_heartbeat TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    progress_percentage INTEGER DEFAULT 0,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index for quick agent lookups
CREATE INDEX IF NOT EXISTS idx_agent_activity_agent_id ON agent_activity(agent_id);
CREATE INDEX IF NOT EXISTS idx_agent_activity_status ON agent_activity(status);
CREATE INDEX IF NOT EXISTS idx_agent_activity_last_heartbeat ON agent_activity(last_heartbeat);

-- 2. AGENT COORDINATION & PLANNING
-- Shared decisions, plans, and coordination between agents
CREATE TABLE IF NOT EXISTS agent_coordination (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    coordination_type TEXT NOT NULL, -- 'decision', 'plan', 'question', 'update'
    priority TEXT NOT NULL DEFAULT 'medium', -- 'critical', 'high', 'medium', 'low'
    title TEXT NOT NULL,
    description TEXT,
    initiating_agent_id TEXT NOT NULL,
    target_agents TEXT[], -- Array of agent IDs (null = all agents)
    status TEXT DEFAULT 'open', -- 'open', 'in_progress', 'resolved', 'blocked'
    resolution TEXT,
    resolved_by TEXT,
    resolved_at TIMESTAMP WITH TIME ZONE,
    tags TEXT[],
    related_resources UUID[], -- Links to resources table
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_coordination_type ON agent_coordination(coordination_type);
CREATE INDEX IF NOT EXISTS idx_coordination_priority ON agent_coordination(priority);
CREATE INDEX IF NOT EXISTS idx_coordination_status ON agent_coordination(status);
CREATE INDEX IF NOT EXISTS idx_coordination_created ON agent_coordination(created_at DESC);

-- 3. AGENT RESPONSES
-- Responses to coordination items
CREATE TABLE IF NOT EXISTS agent_responses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    coordination_id UUID NOT NULL REFERENCES agent_coordination(id) ON DELETE CASCADE,
    agent_id TEXT NOT NULL,
    agent_name TEXT NOT NULL,
    response_text TEXT NOT NULL,
    response_type TEXT DEFAULT 'comment', -- 'comment', 'approval', 'rejection', 'suggestion'
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_responses_coordination ON agent_responses(coordination_id);
CREATE INDEX IF NOT EXISTS idx_responses_agent ON agent_responses(agent_id);

-- 4. KNOWLEDGE UPDATES
-- New knowledge discovered by agents
CREATE TABLE IF NOT EXISTS knowledge_updates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id TEXT NOT NULL,
    update_type TEXT NOT NULL, -- 'discovery', 'bug_found', 'solution', 'pattern', 'insight'
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    impact TEXT DEFAULT 'medium', -- 'critical', 'high', 'medium', 'low'
    verified BOOLEAN DEFAULT FALSE,
    verified_by TEXT[],
    tags TEXT[],
    related_files TEXT[],
    related_resources UUID[],
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_knowledge_type ON knowledge_updates(update_type);
CREATE INDEX IF NOT EXISTS idx_knowledge_impact ON knowledge_updates(impact);
CREATE INDEX IF NOT EXISTS idx_knowledge_verified ON knowledge_updates(verified);
CREATE INDEX IF NOT EXISTS idx_knowledge_created ON knowledge_updates(created_at DESC);

-- 5. TASK QUEUE
-- Centralized task queue for all agents
CREATE TABLE IF NOT EXISTS task_queue (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_name TEXT NOT NULL,
    task_description TEXT NOT NULL,
    priority TEXT NOT NULL DEFAULT 'medium', -- 'critical', 'high', 'medium', 'low'
    status TEXT DEFAULT 'pending', -- 'pending', 'assigned', 'in_progress', 'completed', 'blocked'
    assigned_to TEXT,
    estimated_minutes INTEGER,
    requires_graphrag BOOLEAN DEFAULT TRUE,
    requires_browser_test BOOLEAN DEFAULT FALSE,
    dependencies UUID[], -- Task IDs that must complete first
    tags TEXT[],
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    started_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX IF NOT EXISTS idx_tasks_status ON task_queue(status);
CREATE INDEX IF NOT EXISTS idx_tasks_priority ON task_queue(priority);
CREATE INDEX IF NOT EXISTS idx_tasks_assigned ON task_queue(assigned_to);

-- 6. DECISION LOG
-- Track all major decisions made by agents
CREATE TABLE IF NOT EXISTS decision_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    decision_title TEXT NOT NULL,
    decision_description TEXT NOT NULL,
    decision_type TEXT NOT NULL, -- 'technical', 'content', 'cultural', 'design', 'coordination'
    made_by TEXT NOT NULL,
    approved_by TEXT[],
    impact_level TEXT DEFAULT 'medium', -- 'critical', 'high', 'medium', 'low'
    reasoning TEXT,
    alternatives_considered TEXT[],
    outcome TEXT,
    was_successful BOOLEAN,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_decisions_type ON decision_log(decision_type);
CREATE INDEX IF NOT EXISTS idx_decisions_made_by ON decision_log(made_by);

-- 7. PROGRESS EVENTS
-- Real-time progress events from all agents
CREATE TABLE IF NOT EXISTS progress_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id TEXT NOT NULL,
    event_type TEXT NOT NULL, -- 'start', 'update', 'complete', 'error', 'question', 'discovery'
    message TEXT NOT NULL,
    task_id UUID, -- Optional reference to task_queue
    severity TEXT DEFAULT 'info', -- 'critical', 'error', 'warning', 'info', 'success'
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_events_agent ON progress_events(agent_id);
CREATE INDEX IF NOT EXISTS idx_events_type ON progress_events(event_type);
CREATE INDEX IF NOT EXISTS idx_events_created ON progress_events(created_at DESC);

-- ============================================
-- ROW LEVEL SECURITY (RLS) - Allow all agents to read/write
-- ============================================

ALTER TABLE agent_activity ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_coordination ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_responses ENABLE ROW LEVEL SECURITY;
ALTER TABLE knowledge_updates ENABLE ROW LEVEL SECURITY;
ALTER TABLE task_queue ENABLE ROW LEVEL SECURITY;
ALTER TABLE decision_log ENABLE ROW LEVEL SECURITY;
ALTER TABLE progress_events ENABLE ROW LEVEL SECURITY;

-- Allow anon access (since we're using anon key)
CREATE POLICY "Allow all access" ON agent_activity FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all access" ON agent_coordination FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all access" ON agent_responses FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all access" ON knowledge_updates FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all access" ON task_queue FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all access" ON decision_log FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all access" ON progress_events FOR ALL USING (true) WITH CHECK (true);

-- ============================================
-- HELPER FUNCTIONS
-- ============================================

-- Function to update agent heartbeat
CREATE OR REPLACE FUNCTION update_agent_heartbeat(p_agent_id TEXT)
RETURNS VOID AS $$
BEGIN
    UPDATE agent_activity 
    SET last_heartbeat = NOW(),
        updated_at = NOW()
    WHERE agent_id = p_agent_id;
END;
$$ LANGUAGE plpgsql;

-- Function to get active agents
CREATE OR REPLACE FUNCTION get_active_agents()
RETURNS TABLE (
    agent_id TEXT,
    agent_name TEXT,
    current_task TEXT,
    minutes_since_heartbeat INTEGER
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        aa.agent_id,
        aa.agent_name,
        aa.current_task,
        EXTRACT(EPOCH FROM (NOW() - aa.last_heartbeat))::INTEGER / 60 as minutes_since_heartbeat
    FROM agent_activity aa
    WHERE aa.status = 'active'
    AND aa.last_heartbeat > NOW() - INTERVAL '30 minutes'
    ORDER BY aa.last_heartbeat DESC;
END;
$$ LANGUAGE plpgsql;

-- ============================================
-- INITIAL DATA - Seed tasks from user feedback
-- ============================================

INSERT INTO task_queue (task_name, task_description, priority, status, requires_browser_test, tags) VALUES
('styling-diagnosis', 'User reports website styling appears broken. Need browser DevTools testing (NOT file checks) to diagnose CSS loading issue.', 'critical', 'pending', true, ARRAY['styling', 'css', 'urgent']),
('orphan-integration', 'Integrate 47 excellent resources from /public/generated-resources-alpha/ into main navigation. Use GraphRAG to categorize by cultural value.', 'high', 'pending', true, ARRAY['navigation', 'content', 'integration']),
('high-cultural-featuring', 'Query GraphRAG for 53 high cultural integration resources and feature them prominently on homepage and navigation.', 'high', 'pending', false, ARRAY['cultural', 'content', 'graphrag']),
('navigation-improvement', 'Fix broken links, improve site structure using GraphRAG data about resource relationships.', 'medium', 'pending', true, ARRAY['navigation', 'links']),
('graphrag-verification', 'Verify all 467 resources in GraphRAG are accessible and properly categorized.', 'medium', 'pending', false, ARRAY['graphrag', 'qa']);

-- Seed initial coordination item about agent collaboration
INSERT INTO agent_coordination (coordination_type, priority, title, description, initiating_agent_id, status, tags) VALUES
('decision', 'critical', 'Agents Must Use GraphRAG for Coordination', 
'User feedback: Agents are working solo instead of collaborating through GraphRAG. ALL agents must:
1. Write progress to GraphRAG (progress_events table)
2. Check coordination table before making decisions
3. Update knowledge_updates table with discoveries
4. Query task_queue for work assignments
5. Use GraphRAG as single source of truth',
'system', 'open', ARRAY['coordination', 'critical', 'graphrag']);

-- ============================================
-- VIEWS FOR COMMON QUERIES
-- ============================================

-- View: Recent agent activity
CREATE OR REPLACE VIEW v_recent_activity AS
SELECT 
    pe.agent_id,
    pe.event_type,
    pe.message,
    pe.severity,
    pe.created_at,
    aa.agent_name,
    aa.current_task
FROM progress_events pe
LEFT JOIN agent_activity aa ON pe.agent_id = aa.agent_id
ORDER BY pe.created_at DESC
LIMIT 100;

-- View: Open coordination items
CREATE OR REPLACE VIEW v_open_coordination AS
SELECT 
    ac.*,
    COUNT(ar.id) as response_count
FROM agent_coordination ac
LEFT JOIN agent_responses ar ON ac.id = ar.coordination_id
WHERE ac.status IN ('open', 'in_progress')
GROUP BY ac.id
ORDER BY 
    CASE ac.priority
        WHEN 'critical' THEN 1
        WHEN 'high' THEN 2
        WHEN 'medium' THEN 3
        WHEN 'low' THEN 4
    END,
    ac.created_at DESC;

-- View: Pending tasks by priority
CREATE OR REPLACE VIEW v_pending_tasks AS
SELECT *
FROM task_queue
WHERE status IN ('pending', 'assigned')
ORDER BY 
    CASE priority
        WHEN 'critical' THEN 1
        WHEN 'high' THEN 2
        WHEN 'medium' THEN 3
        WHEN 'low' THEN 4
    END,
    created_at ASC;

COMMENT ON TABLE agent_activity IS 'Real-time tracking of what each agent is doing';
COMMENT ON TABLE agent_coordination IS 'Shared decisions, plans, and coordination between agents';
COMMENT ON TABLE knowledge_updates IS 'New knowledge discovered by agents';
COMMENT ON TABLE task_queue IS 'Centralized task queue for all agents';
COMMENT ON TABLE decision_log IS 'Track all major decisions made by agents';
COMMENT ON TABLE progress_events IS 'Real-time progress events from all agents';

