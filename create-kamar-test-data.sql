-- Create Test Data for KAMAR Weekly Planner
-- Purpose: Demo data so teachers can see the weekly planner in action
-- Date: October 26, 2025

-- Note: Replace 'YOUR_USER_ID' with actual authenticated user ID when testing

-- Insert sample timetable for a Year 9 Mathematics teacher
INSERT INTO kamar_timetable (
    teacher_id,
    class_code,
    class_name,
    day_of_week,
    period,
    start_time,
    end_time,
    room,
    subject,
    year_level,
    academic_year,
    is_active
) VALUES
-- Monday
('YOUR_USER_ID', '9MAT1', 'Year 9 Mathematics', 'Monday', 1, '09:00', '09:55', 'M12', 'Mathematics', 9, 2025, true),
('YOUR_USER_ID', '10MAT2', 'Year 10 Mathematics', 'Monday', 2, '10:00', '10:55', 'M12', 'Mathematics', 10, 2025, true),
('YOUR_USER_ID', '9MAT2', 'Year 9 Mathematics', 'Monday', 4, '13:00', '13:55', 'M12', 'Mathematics', 9, 2025, true),

-- Tuesday
('YOUR_USER_ID', '9MAT1', 'Year 9 Mathematics', 'Tuesday', 1, '09:00', '09:55', 'M12', 'Mathematics', 9, 2025, true),
('YOUR_USER_ID', '11MAT1', 'Year 11 Mathematics', 'Tuesday', 3, '11:30', '12:25', 'M12', 'Mathematics', 11, 2025, true),
('YOUR_USER_ID', '10MAT2', 'Year 10 Mathematics', 'Tuesday', 5, '14:00', '14:55', 'M12', 'Mathematics', 10, 2025, true),

-- Wednesday  
('YOUR_USER_ID', '9MAT2', 'Year 9 Mathematics', 'Wednesday', 2, '10:00', '10:55', 'M12', 'Mathematics', 9, 2025, true),
('YOUR_USER_ID', '11MAT1', 'Year 11 Mathematics', 'Wednesday', 4, '13:00', '13:55', 'M12', 'Mathematics', 11, 2025, true),

-- Thursday
('YOUR_USER_ID', '10MAT2', 'Year 10 Mathematics', 'Thursday', 1, '09:00', '09:55', 'M12', 'Mathematics', 10, 2025, true),
('YOUR_USER_ID', '9MAT1', 'Year 9 Mathematics', 'Thursday', 3, '11:30', '12:25', 'M12', 'Mathematics', 9, 2025, true),
('YOUR_USER_ID', '9MAT2', 'Year 9 Mathematics', 'Thursday', 5, '14:00', '14:55', 'M12', 'Mathematics', 9, 2025, true),

-- Friday
('YOUR_USER_ID', '11MAT1', 'Year 11 Mathematics', 'Friday', 2, '10:00', '10:55', 'M12', 'Mathematics', 11, 2025, true),
('YOUR_USER_ID', '10MAT2', 'Year 10 Mathematics', 'Friday', 4, '13:00', '13:55', 'M12', 'Mathematics', 10, 2025, true);

-- Add sample staff entry
INSERT INTO kamar_staff (
    kamar_staff_id,
    full_name,
    email,
    department,
    role,
    synced_at
) VALUES (
    'STAFF001',
    'Demo Teacher',
    'demo@school.nz',
    'Mathematics',
    'Teacher',
    NOW()
);

-- Add sample courses
INSERT INTO kamar_courses (
    course_code,
    course_name,
    subject,
    year_level,
    teacher_ids,
    student_count,
    synced_at
) VALUES
('9MAT1', 'Year 9 Mathematics - Class 1', 'Mathematics', 9, ARRAY['STAFF001'], 28, NOW()),
('9MAT2', 'Year 9 Mathematics - Class 2', 'Mathematics', 9, ARRAY['STAFF001'], 26, NOW()),
('10MAT2', 'Year 10 Mathematics - Class 2', 'Mathematics', 10, ARRAY['STAFF001'], 24, NOW()),
('11MAT1', 'Year 11 Mathematics - Class 1', 'Mathematics', 11, ARRAY['STAFF001'], 22, NOW());

-- Verify data inserted
SELECT 
    'Timetable entries created: ' || COUNT(*) as status
FROM kamar_timetable
WHERE teacher_id = 'YOUR_USER_ID';

SELECT 
    'Courses created: ' || COUNT(*) as status
FROM kamar_courses;
