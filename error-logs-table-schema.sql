-- =====================================================
-- ERROR LOGS TABLE - Automatic Console Error Tracking
-- =====================================================
-- This table stores JavaScript errors from the live site
-- Integrates with PostHog for comprehensive error monitoring

CREATE TABLE IF NOT EXISTS error_logs (
    id BIGSERIAL PRIMARY KEY,
    
    -- Error Details
    error_type TEXT NOT NULL,  -- 'javascript_error', 'unhandled_promise_rejection', 'console_error', 'manual_report'
    error_message TEXT NOT NULL,
    error_stack TEXT,
    
    -- Location Details
    page_url TEXT NOT NULL,
    page_title TEXT,
    filename TEXT,
    line_number INTEGER,
    column_number INTEGER,
    
    -- User Context
    user_agent TEXT,
    session_errors INTEGER DEFAULT 1,
    user_id UUID REFERENCES auth.users(id) ON DELETE SET NULL,  -- Optional: if user is logged in
    
    -- Metadata
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_error_logs_timestamp ON error_logs(timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_error_logs_error_type ON error_logs(error_type);
CREATE INDEX IF NOT EXISTS idx_error_logs_page_url ON error_logs(page_url);
CREATE INDEX IF NOT EXISTS idx_error_logs_filename ON error_logs(filename);

-- RLS Policies (allow anonymous inserts, restrict reads to admins)
ALTER TABLE error_logs ENABLE ROW LEVEL SECURITY;

-- Allow anyone to INSERT errors (anonymous tracking)
CREATE POLICY "Allow anonymous error logging"
ON error_logs
FOR INSERT
TO anon
WITH CHECK (true);

-- Only admins can SELECT error logs
CREATE POLICY "Admins can read error logs"
ON error_logs
FOR SELECT
TO authenticated
USING (
    EXISTS (
        SELECT 1 FROM profiles
        WHERE profiles.user_id = auth.uid()
        AND profiles.role = 'admin'
    )
);

-- Grant permissions
GRANT INSERT ON error_logs TO anon;
GRANT ALL ON error_logs TO authenticated;

-- =====================================================
-- ERROR SUMMARY VIEW - For GraphRAG Analytics
-- =====================================================
CREATE OR REPLACE VIEW error_summary AS
SELECT 
    error_type,
    error_message,
    page_url,
    filename,
    COUNT(*) as occurrence_count,
    MAX(timestamp) as last_occurred,
    MIN(timestamp) as first_occurred,
    ARRAY_AGG(DISTINCT user_agent) as affected_browsers
FROM error_logs
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY error_type, error_message, page_url, filename
ORDER BY occurrence_count DESC;

-- Grant access to error summary
GRANT SELECT ON error_summary TO authenticated;

-- =====================================================
-- COMMENTS FOR DOCUMENTATION
-- =====================================================
COMMENT ON TABLE error_logs IS 'Automatic JavaScript error tracking from production site. Populated by error-monitoring.js script.';
COMMENT ON COLUMN error_logs.error_type IS 'Type of error: javascript_error, unhandled_promise_rejection, console_error, or manual_report';
COMMENT ON COLUMN error_logs.session_errors IS 'Number of errors in this user session (capped at 50 to prevent spam)';
COMMENT ON VIEW error_summary IS 'Aggregated error statistics for the last 7 days - useful for GraphRAG analysis';

