-- ================================================================
-- NZ EDUCATION PLATFORM - AUTHENTICATION SCHEMA
-- Date: October 16, 2025
-- Purpose: Extend auth system for NZ students and teachers
-- ================================================================

-- ================================================================
-- EXTEND PROFILES TABLE FOR NZ EDUCATION
-- ================================================================

-- Add student-specific fields
ALTER TABLE public.profiles 
ADD COLUMN IF NOT EXISTS first_name text,
ADD COLUMN IF NOT EXISTS last_name text,
ADD COLUMN IF NOT EXISTS date_of_birth date,
ADD COLUMN IF NOT EXISTS gender text CHECK (gender IN ('Male', 'Female', 'Non-binary', 'Takatāpui', 'Prefer not to say', 'Other')),
ADD COLUMN IF NOT EXISTS cultural_identity text[], -- Array for multiple identities
ADD COLUMN IF NOT EXISTS iwi_affiliation text,
ADD COLUMN IF NOT EXISTS preferred_language text CHECK (preferred_language IN ('English', 'Te Reo Māori', 'Both')) DEFAULT 'English',
ADD COLUMN IF NOT EXISTS consent_given boolean DEFAULT false,
ADD COLUMN IF NOT EXISTS terms_accepted_at timestamp with time zone,
ADD COLUMN IF NOT EXISTS parent_email text; -- For students under 16

-- Add teacher-specific fields
ALTER TABLE public.profiles
ADD COLUMN IF NOT EXISTS title text CHECK (title IN ('Mr', 'Mrs', 'Ms', 'Miss', 'Mx', 'Dr', 'Prof')),
ADD COLUMN IF NOT EXISTS teacher_registration_number text, -- NZ Teaching Council registration
ADD COLUMN IF NOT EXISTS teacher_role text CHECK (teacher_role IN ('Classroom Teacher', 'HOD', 'HOF', 'DP', 'AP', 'Principal', 'Tutor')),
ADD COLUMN IF NOT EXISTS subjects_taught jsonb DEFAULT '[]'::jsonb, -- Array of subjects
ADD COLUMN IF NOT EXISTS year_levels_taught integer[] DEFAULT ARRAY[]::integer[], -- Array of year levels (7-13)
ADD COLUMN IF NOT EXISTS kamar_school_code text,
ADD COLUMN IF NOT EXISTS kamar_sync_enabled boolean DEFAULT false,
ADD COLUMN IF NOT EXISTS class_lists jsonb DEFAULT '[]'::jsonb,
ADD COLUMN IF NOT EXISTS timetable jsonb DEFAULT '{}'::jsonb;

-- Add personalization and settings
ALTER TABLE public.profiles
ADD COLUMN IF NOT EXISTS personalization_settings jsonb DEFAULT '{}'::jsonb,
ADD COLUMN IF NOT EXISTS onboarding_completed boolean DEFAULT false,
ADD COLUMN IF NOT EXISTS profile_picture_url text,
ADD COLUMN IF NOT EXISTS bio text;

-- Add indexes for performance
CREATE INDEX IF NOT EXISTS idx_profiles_school_name ON public.profiles(school_name);
CREATE INDEX IF NOT EXISTS idx_profiles_year_level ON public.profiles(year_level);
CREATE INDEX IF NOT EXISTS idx_profiles_role ON public.profiles(role);
CREATE INDEX IF NOT EXISTS idx_profiles_cultural_identity ON public.profiles USING GIN(cultural_identity);

-- Add comments for documentation
COMMENT ON COLUMN public.profiles.cultural_identity IS 'Array of cultural identities (Māori, Pasifika, Pākehā, Asian, etc)';
COMMENT ON COLUMN public.profiles.iwi_affiliation IS 'Iwi affiliation for Māori students/teachers';
COMMENT ON COLUMN public.profiles.teacher_registration_number IS 'NZ Teaching Council registration number';
COMMENT ON COLUMN public.profiles.kamar_school_code IS 'KAMAR SMS school code for integration';

-- ================================================================
-- CREATE NZ SCHOOLS TABLE
-- ================================================================

CREATE TABLE IF NOT EXISTS public.nz_schools (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    name text NOT NULL UNIQUE,
    location text,
    region text CHECK (region IN (
        'Northland', 'Auckland', 'Waikato', 'Bay of Plenty', 'Gisborne',
        'Hawkes Bay', 'Taranaki', 'Manawatū-Whanganui', 'Wellington',
        'Tasman', 'Nelson', 'Marlborough', 'West Coast', 'Canterbury',
        'Otago', 'Southland'
    )),
    school_type text CHECK (school_type IN ('Intermediate', 'Secondary', 'Composite', 'Area School', 'Special School')),
    authority text CHECK (authority IN ('State', 'State Integrated', 'Private')),
    decile integer CHECK (decile >= 1 AND decile <= 10),
    roll_count integer,
    kamar_enabled boolean DEFAULT false,
    website_url text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

-- Create index for school search
CREATE INDEX IF NOT EXISTS idx_nz_schools_name ON public.nz_schools(name);
CREATE INDEX IF NOT EXISTS idx_nz_schools_region ON public.nz_schools(region);

-- Insert Mangakōtukutuku College
INSERT INTO public.nz_schools (name, location, region, school_type, authority, decile, roll_count, kamar_enabled)
VALUES ('Mangakōtukutuku College', 'Hamilton', 'Waikato', 'Secondary', 'State', 5, 850, true)
ON CONFLICT (name) DO NOTHING;

-- Insert some major NZ schools for testing
INSERT INTO public.nz_schools (name, location, region, school_type, authority, decile, roll_count, kamar_enabled)
VALUES 
    ('Auckland Grammar School', 'Auckland', 'Auckland', 'Secondary', 'State', 10, 2500, true),
    ('Wellington High School', 'Wellington', 'Wellington', 'Secondary', 'State', 7, 1200, true),
    ('Christchurch Boys High School', 'Christchurch', 'Canterbury', 'Secondary', 'State', 9, 1400, true),
    ('Otago Girls High School', 'Dunedin', 'Otago', 'Secondary', 'State', 8, 1100, false),
    ('Hamilton Boys High School', 'Hamilton', 'Waikato', 'Secondary', 'State', 8, 1300, true),
    ('Whangarei Boys High School', 'Whangarei', 'Northland', 'Secondary', 'State', 6, 900, true),
    ('Mount Albert Grammar School', 'Auckland', 'Auckland', 'Secondary', 'State', 10, 3000, true),
    ('Takapuna Grammar School', 'Auckland', 'Auckland', 'Secondary', 'State', 10, 1800, true),
    ('Palmerston North Boys High School', 'Palmerston North', 'Manawatū-Whanganui', 'Secondary', 'State', 7, 1100, true),
    ('Nelson College', 'Nelson', 'Nelson', 'Secondary', 'State', 9, 900, false)
ON CONFLICT (name) DO NOTHING;

COMMENT ON TABLE public.nz_schools IS 'Registry of New Zealand schools for student/teacher profiles';

-- ================================================================
-- CREATE TEACHER CLASSES TABLE
-- ================================================================

CREATE TABLE IF NOT EXISTS public.teacher_classes (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    teacher_id uuid NOT NULL REFERENCES public.profiles(user_id) ON DELETE CASCADE,
    class_code text NOT NULL, -- e.g., "10MAT1", "11ENG2"
    class_name text NOT NULL, -- e.g., "Year 10 Mathematics"
    year_level integer NOT NULL CHECK (year_level >= 7 AND year_level <= 13),
    subject text NOT NULL,
    student_ids uuid[] DEFAULT ARRAY[]::uuid[], -- Array of student user_ids
    period_times jsonb DEFAULT '{}'::jsonb, -- When class meets
    room text,
    description text,
    archived boolean DEFAULT false,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    UNIQUE(teacher_id, class_code)
);

CREATE INDEX IF NOT EXISTS idx_teacher_classes_teacher ON public.teacher_classes(teacher_id);
CREATE INDEX IF NOT EXISTS idx_teacher_classes_year_level ON public.teacher_classes(year_level);
CREATE INDEX IF NOT EXISTS idx_teacher_classes_subject ON public.teacher_classes(subject);

COMMENT ON TABLE public.teacher_classes IS 'Teacher class management with student lists';

-- ================================================================
-- CREATE STUDENT PROGRESS TABLE
-- ================================================================

CREATE TABLE IF NOT EXISTS public.student_progress (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id uuid NOT NULL REFERENCES public.profiles(user_id) ON DELETE CASCADE,
    resource_id uuid NOT NULL REFERENCES public.resources(id) ON DELETE CASCADE,
    progress_percentage integer DEFAULT 0 CHECK (progress_percentage >= 0 AND progress_percentage <= 100),
    completed_at timestamp with time zone,
    score integer,
    time_spent_minutes integer DEFAULT 0,
    notes text,
    teacher_feedback text,
    cultural_engagement_score integer CHECK (cultural_engagement_score >= 0 AND cultural_engagement_score <= 100),
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    UNIQUE(student_id, resource_id)
);

CREATE INDEX IF NOT EXISTS idx_student_progress_student ON public.student_progress(student_id);
CREATE INDEX IF NOT EXISTS idx_student_progress_resource ON public.student_progress(resource_id);
CREATE INDEX IF NOT EXISTS idx_student_progress_completed ON public.student_progress(completed_at) WHERE completed_at IS NOT NULL;

COMMENT ON TABLE public.student_progress IS 'Student learning progress tracking';

-- ================================================================
-- CREATE KAMAR SYNC LOG TABLE
-- ================================================================

CREATE TABLE IF NOT EXISTS public.kamar_sync_log (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    teacher_id uuid NOT NULL REFERENCES public.profiles(user_id) ON DELETE CASCADE,
    sync_type text NOT NULL CHECK (sync_type IN ('classes', 'students', 'timetable', 'full')),
    status text NOT NULL CHECK (status IN ('pending', 'in_progress', 'success', 'failed')),
    records_synced integer DEFAULT 0,
    error_message text,
    sync_data jsonb DEFAULT '{}'::jsonb,
    started_at timestamp with time zone DEFAULT now(),
    completed_at timestamp with time zone
);

CREATE INDEX IF NOT EXISTS idx_kamar_sync_teacher ON public.kamar_sync_log(teacher_id);
CREATE INDEX IF NOT EXISTS idx_kamar_sync_status ON public.kamar_sync_log(status);

COMMENT ON TABLE public.kamar_sync_log IS 'Log of KAMAR integration sync operations';

-- ================================================================
-- UPDATE RLS POLICIES
-- ================================================================

-- Enable RLS on new tables
ALTER TABLE public.nz_schools ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.teacher_classes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.student_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.kamar_sync_log ENABLE ROW LEVEL SECURITY;

-- NZ Schools: Public read access
CREATE POLICY "NZ schools are viewable by everyone"
    ON public.nz_schools FOR SELECT
    USING (true);

-- Teacher Classes: Teachers can manage their own classes
CREATE POLICY "Teachers can view their own classes"
    ON public.teacher_classes FOR SELECT
    USING (auth.uid() = teacher_id);

CREATE POLICY "Teachers can insert their own classes"
    ON public.teacher_classes FOR INSERT
    WITH CHECK (auth.uid() = teacher_id);

CREATE POLICY "Teachers can update their own classes"
    ON public.teacher_classes FOR UPDATE
    USING (auth.uid() = teacher_id);

CREATE POLICY "Teachers can delete their own classes"
    ON public.teacher_classes FOR DELETE
    USING (auth.uid() = teacher_id);

-- Student Progress: Students see own progress, teachers see their students
CREATE POLICY "Students can view their own progress"
    ON public.student_progress FOR SELECT
    USING (auth.uid() = student_id);

CREATE POLICY "Students can insert their own progress"
    ON public.student_progress FOR INSERT
    WITH CHECK (auth.uid() = student_id);

CREATE POLICY "Students can update their own progress"
    ON public.student_progress FOR UPDATE
    USING (auth.uid() = student_id);

-- Teachers can view progress of students in their classes
CREATE POLICY "Teachers can view student progress in their classes"
    ON public.student_progress FOR SELECT
    USING (
        EXISTS (
            SELECT 1 FROM public.teacher_classes tc
            WHERE tc.teacher_id = auth.uid()
            AND student_id = ANY(tc.student_ids)
        )
    );

-- KAMAR Sync: Teachers manage their own sync
CREATE POLICY "Teachers can view their own KAMAR sync logs"
    ON public.kamar_sync_log FOR SELECT
    USING (auth.uid() = teacher_id);

CREATE POLICY "Teachers can insert their own KAMAR sync logs"
    ON public.kamar_sync_log FOR INSERT
    WITH CHECK (auth.uid() = teacher_id);

-- ================================================================
-- CREATE UPDATED_AT TRIGGERS
-- ================================================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Add triggers to new tables
DROP TRIGGER IF EXISTS update_nz_schools_updated_at ON public.nz_schools;
CREATE TRIGGER update_nz_schools_updated_at
    BEFORE UPDATE ON public.nz_schools
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_teacher_classes_updated_at ON public.teacher_classes;
CREATE TRIGGER update_teacher_classes_updated_at
    BEFORE UPDATE ON public.teacher_classes
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_student_progress_updated_at ON public.student_progress;
CREATE TRIGGER update_student_progress_updated_at
    BEFORE UPDATE ON public.student_progress
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ================================================================
-- GRANT PERMISSIONS
-- ================================================================

-- Grant appropriate permissions
GRANT SELECT ON public.nz_schools TO authenticated;
GRANT ALL ON public.teacher_classes TO authenticated;
GRANT ALL ON public.student_progress TO authenticated;
GRANT ALL ON public.kamar_sync_log TO authenticated;

-- ================================================================
-- MIGRATION COMPLETE
-- ================================================================

-- Log migration
DO $$
BEGIN
    RAISE NOTICE 'NZ Education Auth Schema Migration Complete - October 16, 2025';
    RAISE NOTICE 'Tables created: nz_schools, teacher_classes, student_progress, kamar_sync_log';
    RAISE NOTICE 'Profiles table extended with NZ-specific fields';
    RAISE NOTICE 'RLS policies configured for all tables';
END $$;

