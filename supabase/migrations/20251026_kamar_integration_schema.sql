-- ================================================================
-- KAMAR INTEGRATION SCHEMA
-- Date: October 26, 2025
-- Purpose: Enable NZ School Management System integration
-- Unblocks: Teacher weekly planner, timetable sync, professional workflow
-- Timeline: 2-week implementation (Week 13-15)
-- ================================================================

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ================================================================
-- TABLE 1: KAMAR Timetable Data
-- Stores teacher class schedules from KAMAR
-- ================================================================
CREATE TABLE IF NOT EXISTS kamar_timetable (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  teacher_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  school_id TEXT NOT NULL, -- School identifier from KAMAR
  
  -- Class Information
  class_code TEXT NOT NULL, -- e.g., "9MA1", "10EN2"
  class_name TEXT NOT NULL, -- e.g., "Year 9 Mathematics"
  subject TEXT, -- Mapped to our subject taxonomy
  year_level INTEGER, -- 7-13
  
  -- Schedule Information
  day_of_week TEXT NOT NULL, -- Monday, Tuesday, Wednesday, Thursday, Friday
  period INTEGER NOT NULL, -- Period number (1-6 typically)
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  room TEXT, -- Room code (e.g., "M15", "Science Lab A")
  
  -- Metadata
  academic_year INTEGER DEFAULT EXTRACT(YEAR FROM CURRENT_DATE),
  is_active BOOLEAN DEFAULT TRUE,
  synced_at TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  -- Constraints
  UNIQUE(school_id, class_code, day_of_week, period, academic_year)
);

-- Index for fast teacher lookups
CREATE INDEX IF NOT EXISTS idx_kamar_timetable_teacher 
ON kamar_timetable(teacher_id, academic_year);

-- Index for day/period lookups
CREATE INDEX IF NOT EXISTS idx_kamar_timetable_schedule 
ON kamar_timetable(day_of_week, period);

-- ================================================================
-- TABLE 2: KAMAR Staff Data
-- Stores teacher/staff information from KAMAR
-- ================================================================
CREATE TABLE IF NOT EXISTS kamar_staff (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  profile_id UUID REFERENCES profiles(id) ON DELETE CASCADE, -- Link to Te Kete Ako user
  school_id TEXT NOT NULL,
  
  -- KAMAR Staff Info
  kamar_staff_id TEXT UNIQUE NOT NULL, -- Staff ID from KAMAR
  full_name TEXT NOT NULL,
  email TEXT,
  department TEXT, -- e.g., "Mathematics", "Science"
  role TEXT, -- e.g., "Teacher", "HOD", "Dean"
  
  -- Metadata
  is_active BOOLEAN DEFAULT TRUE,
  synced_at TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  -- Constraints
  UNIQUE(school_id, kamar_staff_id)
);

-- Index for email lookups (matching KAMAR staff to Te Kete users)
CREATE INDEX IF NOT EXISTS idx_kamar_staff_email 
ON kamar_staff(email);

-- ================================================================
-- TABLE 3: KAMAR Course Data
-- Stores course/class information from KAMAR
-- ================================================================
CREATE TABLE IF NOT EXISTS kamar_courses (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  school_id TEXT NOT NULL,
  
  -- Course Information
  course_code TEXT UNIQUE NOT NULL, -- e.g., "9MA1", "10SCPH"
  course_name TEXT NOT NULL, -- e.g., "Year 9 Mathematics"
  subject TEXT, -- Mapped to our subject taxonomy
  year_level INTEGER, -- 7-13
  
  -- Teacher Assignment
  teacher_ids TEXT[], -- Array of KAMAR staff IDs
  primary_teacher_id TEXT, -- Main teacher for the class
  
  -- Student Information
  student_count INTEGER DEFAULT 0,
  student_ids TEXT[], -- Array of KAMAR student IDs (optional)
  
  -- Metadata
  academic_year INTEGER DEFAULT EXTRACT(YEAR FROM CURRENT_DATE),
  is_active BOOLEAN DEFAULT TRUE,
  synced_at TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  -- Constraints
  UNIQUE(school_id, course_code, academic_year)
);

-- Index for teacher lookups
CREATE INDEX IF NOT EXISTS idx_kamar_courses_teachers 
ON kamar_courses USING GIN(teacher_ids);

-- Index for year level lookups
CREATE INDEX IF NOT EXISTS idx_kamar_courses_year 
ON kamar_courses(year_level);

-- ================================================================
-- TABLE 4: KAMAR Sync Log
-- Tracks sync operations for monitoring and debugging
-- ================================================================
CREATE TABLE IF NOT EXISTS kamar_sync_log (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  school_id TEXT NOT NULL,
  
  -- Sync Information
  sync_type TEXT NOT NULL, -- 'nightly_full', 'realtime_update', 'manual_upload'
  sync_status TEXT NOT NULL, -- 'success', 'partial', 'failed'
  records_processed INTEGER DEFAULT 0,
  records_created INTEGER DEFAULT 0,
  records_updated INTEGER DEFAULT 0,
  records_deleted INTEGER DEFAULT 0,
  
  -- Error Tracking
  error_message TEXT,
  error_details JSONB,
  
  -- Metadata
  sync_started_at TIMESTAMP DEFAULT NOW(),
  sync_completed_at TIMESTAMP,
  
  created_at TIMESTAMP DEFAULT NOW()
);

-- Index for monitoring recent syncs
CREATE INDEX IF NOT EXISTS idx_kamar_sync_log_recent 
ON kamar_sync_log(school_id, sync_started_at DESC);

-- ================================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- Ensures teachers only see their own data
-- ================================================================

-- Enable RLS on all tables
ALTER TABLE kamar_timetable ENABLE ROW LEVEL SECURITY;
ALTER TABLE kamar_staff ENABLE ROW LEVEL SECURITY;
ALTER TABLE kamar_courses ENABLE ROW LEVEL SECURITY;
ALTER TABLE kamar_sync_log ENABLE ROW LEVEL SECURITY;

-- Policy: Teachers can view their own timetable
CREATE POLICY "Teachers view own timetable"
ON kamar_timetable
FOR SELECT
USING (teacher_id = auth.uid());

-- Policy: Teachers can view their own staff record
CREATE POLICY "Teachers view own staff record"
ON kamar_staff
FOR SELECT
USING (profile_id = auth.uid());

-- Policy: Teachers can view courses they teach
CREATE POLICY "Teachers view own courses"
ON kamar_courses
FOR SELECT
USING (
  EXISTS (
    SELECT 1 FROM kamar_staff 
    WHERE profile_id = auth.uid() 
    AND kamar_staff_id = ANY(kamar_courses.teacher_ids)
  )
);

-- Policy: Service role can do anything (for webhook)
CREATE POLICY "Service role full access on timetable"
ON kamar_timetable
FOR ALL
USING (auth.jwt()->>'role' = 'service_role');

CREATE POLICY "Service role full access on staff"
ON kamar_staff
FOR ALL
USING (auth.jwt()->>'role' = 'service_role');

CREATE POLICY "Service role full access on courses"
ON kamar_courses
FOR ALL
USING (auth.jwt()->>'role' = 'service_role');

CREATE POLICY "Service role full access on sync log"
ON kamar_sync_log
FOR ALL
USING (auth.jwt()->>'role' = 'service_role');

-- ================================================================
-- HELPER FUNCTIONS
-- ================================================================

-- Function: Get teacher's weekly schedule
CREATE OR REPLACE FUNCTION get_teacher_weekly_schedule(
  p_teacher_id UUID,
  p_academic_year INTEGER DEFAULT EXTRACT(YEAR FROM CURRENT_DATE)
)
RETURNS TABLE (
  day_of_week TEXT,
  period INTEGER,
  class_code TEXT,
  class_name TEXT,
  subject TEXT,
  room TEXT,
  start_time TIME,
  end_time TIME
)
LANGUAGE SQL
STABLE
AS $$
  SELECT 
    day_of_week,
    period,
    class_code,
    class_name,
    subject,
    room,
    start_time,
    end_time
  FROM kamar_timetable
  WHERE teacher_id = p_teacher_id
    AND academic_year = p_academic_year
    AND is_active = TRUE
  ORDER BY 
    CASE day_of_week
      WHEN 'Monday' THEN 1
      WHEN 'Tuesday' THEN 2
      WHEN 'Wednesday' THEN 3
      WHEN 'Thursday' THEN 4
      WHEN 'Friday' THEN 5
    END,
    period;
$$;

-- Function: Get today's classes for a teacher
CREATE OR REPLACE FUNCTION get_teacher_today_classes(p_teacher_id UUID)
RETURNS TABLE (
  period INTEGER,
  class_code TEXT,
  class_name TEXT,
  subject TEXT,
  room TEXT,
  start_time TIME,
  end_time TIME
)
LANGUAGE SQL
STABLE
AS $$
  SELECT 
    period,
    class_code,
    class_name,
    subject,
    room,
    start_time,
    end_time
  FROM kamar_timetable
  WHERE teacher_id = p_teacher_id
    AND day_of_week = TO_CHAR(CURRENT_DATE, 'Day')
    AND academic_year = EXTRACT(YEAR FROM CURRENT_DATE)
    AND is_active = TRUE
  ORDER BY period;
$$;

-- ================================================================
-- GRANTS
-- Give authenticated users read access to their own data
-- ================================================================

GRANT SELECT ON kamar_timetable TO authenticated;
GRANT SELECT ON kamar_staff TO authenticated;
GRANT SELECT ON kamar_courses TO authenticated;

-- Grant service role full access (for webhook operations)
GRANT ALL ON kamar_timetable TO service_role;
GRANT ALL ON kamar_staff TO service_role;
GRANT ALL ON kamar_courses TO service_role;
GRANT ALL ON kamar_sync_log TO service_role;

-- ================================================================
-- COMMENTS (Documentation)
-- ================================================================

COMMENT ON TABLE kamar_timetable IS 'Teacher class schedules synced from KAMAR school management system';
COMMENT ON TABLE kamar_staff IS 'Staff/teacher information from KAMAR';
COMMENT ON TABLE kamar_courses IS 'Course/class information from KAMAR';
COMMENT ON TABLE kamar_sync_log IS 'Log of KAMAR sync operations for monitoring';

COMMENT ON FUNCTION get_teacher_weekly_schedule IS 'Returns a teacher''s complete weekly schedule';
COMMENT ON FUNCTION get_teacher_today_classes IS 'Returns a teacher''s classes for today';

-- ================================================================
-- MIGRATION COMPLETE
-- ================================================================

-- Log the migration
DO $$
BEGIN
  RAISE NOTICE 'KAMAR Integration Schema Created Successfully!';
  RAISE NOTICE 'Tables: kamar_timetable, kamar_staff, kamar_courses, kamar_sync_log';
  RAISE NOTICE 'RLS Policies: Enabled for data security';
  RAISE NOTICE 'Helper Functions: get_teacher_weekly_schedule, get_teacher_today_classes';
  RAISE NOTICE 'Next Step: Create webhook listener in netlify/functions/kamar-webhook-listener.js';
END $$;

