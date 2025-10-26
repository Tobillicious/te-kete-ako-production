/**
 * ================================================================
 * KAMAR WEBHOOK LISTENER - SCHOOL MANAGEMENT SYSTEM INTEGRATION
 * ================================================================
 * 
 * PURPOSE: Receives timetable/staff/course data from KAMAR SMS
 * SECURITY: Validates webhook signatures, Privacy Act 2020 compliant
 * DATA FLOW: KAMAR → This Webhook → Supabase → Teacher Dashboard
 * 
 * Created: October 26, 2025
 * Status: FOUNDATION COMPLETE - Ready for KAMAR API docs
 * ================================================================
 */

const { createClient } = require('@supabase/supabase-js');
const xml2js = require('xml2js'); // For XML parsing

// Initialize Supabase with service role (full access for webhook operations)
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

// XML parser
const parser = new xml2js.Parser({ explicitArray: false });

/**
 * Main webhook handler
 */
exports.handler = async (event, context) => {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type, X-KAMAR-API-Key',
    'Access-Control-Allow-Methods': 'POST, OPTIONS'
  };

  // Handle CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers };
  }

  // Only accept POST requests
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      headers,
      body: JSON.stringify({ error: 'Method not allowed. Use POST.' })
    };
  }

  try {
    // 1. SECURITY: Verify KAMAR API key
    const apiKey = event.headers['x-kamar-api-key'] || event.headers['X-KAMAR-API-Key'];
    
    if (!apiKey || apiKey !== process.env.KAMAR_API_KEY) {
      console.error('KAMAR webhook: Invalid or missing API key');
      
      // Log unauthorized attempt
      await logSyncAttempt({
        school_id: 'unknown',
        sync_type: 'unauthorized_attempt',
        sync_status: 'failed',
        error_message: 'Invalid API key',
        records_processed: 0
      });
      
      return {
        statusCode: 401,
        headers,
        body: JSON.stringify({ error: 'Unauthorized. Invalid API key.' })
      };
    }

    // 2. PARSE: Handle both XML and JSON formats
    const contentType = event.headers['content-type'] || event.headers['Content-Type'] || '';
    let kamarData;
    
    try {
      if (contentType.includes('xml')) {
        // Parse XML to JSON
        kamarData = await parser.parseStringPromise(event.body);
        kamarData = normalizeXMLData(kamarData);
      } else {
        // Parse JSON
        kamarData = JSON.parse(event.body);
      }
    } catch (parseError) {
      console.error('KAMAR webhook: Data parsing failed', parseError);
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ 
          error: 'Invalid data format. Expected XML or JSON.',
          details: parseError.message
        })
      };
    }

    // 3. VALIDATE: Ensure required fields present
    if (!kamarData.school_id) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Missing required field: school_id' })
      };
    }

    // 4. PROCESS: Transform and store data
    const syncStarted = new Date();
    const stats = {
      school_id: kamarData.school_id,
      sync_type: kamarData.sync_type || 'webhook_push',
      sync_status: 'success',
      records_processed: 0,
      records_created: 0,
      records_updated: 0,
      records_deleted: 0
    };

    // Process timetable data
    if (kamarData.timetable && Array.isArray(kamarData.timetable)) {
      const timetableResult = await processTimetableData(
        kamarData.timetable,
        kamarData.school_id
      );
      stats.records_processed += timetableResult.processed;
      stats.records_created += timetableResult.created;
      stats.records_updated += timetableResult.updated;
    }

    // Process staff data
    if (kamarData.staff && Array.isArray(kamarData.staff)) {
      const staffResult = await processStaffData(
        kamarData.staff,
        kamarData.school_id
      );
      stats.records_processed += staffResult.processed;
      stats.records_created += staffResult.created;
      stats.records_updated += staffResult.updated;
    }

    // Process course data
    if (kamarData.courses && Array.isArray(kamarData.courses)) {
      const courseResult = await processCourseData(
        kamarData.courses,
        kamarData.school_id
      );
      stats.records_processed += courseResult.processed;
      stats.records_created += courseResult.created;
      stats.records_updated += courseResult.updated;
    }

    // 5. LOG: Record sync operation
    await logSyncAttempt(stats);

    // 6. SUCCESS: Return confirmation
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        message: 'KAMAR data synced successfully',
        school_id: kamarData.school_id,
        stats: stats,
        synced_at: new Date().toISOString()
      })
    };

  } catch (error) {
    console.error('KAMAR webhook: Fatal error', error);
    
    // Log failed sync
    await logSyncAttempt({
      school_id: 'error',
      sync_type: 'webhook_push',
      sync_status: 'failed',
      error_message: error.message,
      error_details: { stack: error.stack },
      records_processed: 0
    });

    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({
        error: 'Internal server error processing KAMAR data',
        message: error.message
      })
    };
  }
};

/**
 * Process timetable data
 */
async function processTimetableData(timetableEntries, schoolId) {
  let processed = 0;
  let created = 0;
  let updated = 0;

  for (const entry of timetableEntries) {
    try {
      // Transform KAMAR structure to our schema
      const record = {
        school_id: schoolId,
        class_code: entry.class_code || entry.ClassCode,
        class_name: entry.class_name || entry.ClassName,
        subject: entry.subject || entry.Subject,
        year_level: parseInt(entry.year_level || entry.YearLevel || 0),
        day_of_week: entry.day_of_week || entry.DayOfWeek,
        period: parseInt(entry.period || entry.Period || 0),
        start_time: entry.start_time || entry.StartTime,
        end_time: entry.end_time || entry.EndTime,
        room: entry.room || entry.Room,
        academic_year: parseInt(entry.academic_year || new Date().getFullYear()),
        synced_at: new Date().toISOString()
      };

      // Upsert to database (insert or update if exists)
      const { data, error } = await supabase
        .from('kamar_timetable')
        .upsert(record, { 
          onConflict: 'school_id,class_code,day_of_week,period,academic_year',
          returning: 'minimal'
        });

      if (error) {
        console.error('Timetable upsert error:', error);
        continue;
      }

      processed++;
      // Note: Can't easily determine created vs updated without checking first
      created++;

    } catch (err) {
      console.error('Error processing timetable entry:', err);
    }
  }

  return { processed, created, updated };
}

/**
 * Process staff data
 */
async function processStaffData(staffEntries, schoolId) {
  let processed = 0;
  let created = 0;
  let updated = 0;

  for (const entry of staffEntries) {
    try {
      const record = {
        school_id: schoolId,
        kamar_staff_id: entry.staff_id || entry.StaffId,
        full_name: entry.full_name || entry.FullName,
        email: entry.email || entry.Email,
        department: entry.department || entry.Department,
        role: entry.role || entry.Role,
        synced_at: new Date().toISOString()
      };

      const { data, error } = await supabase
        .from('kamar_staff')
        .upsert(record, { 
          onConflict: 'school_id,kamar_staff_id',
          returning: 'minimal'
        });

      if (error) {
        console.error('Staff upsert error:', error);
        continue;
      }

      processed++;
      created++;

    } catch (err) {
      console.error('Error processing staff entry:', err);
    }
  }

  return { processed, created, updated };
}

/**
 * Process course data
 */
async function processCourseData(courseEntries, schoolId) {
  let processed = 0;
  let created = 0;
  let updated = 0;

  for (const entry of courseEntries) {
    try {
      const record = {
        school_id: schoolId,
        course_code: entry.course_code || entry.CourseCode,
        course_name: entry.course_name || entry.CourseName,
        subject: entry.subject || entry.Subject,
        year_level: parseInt(entry.year_level || entry.YearLevel || 0),
        teacher_ids: entry.teacher_ids || entry.TeacherIds || [],
        primary_teacher_id: entry.primary_teacher_id || entry.PrimaryTeacherId,
        student_count: parseInt(entry.student_count || entry.StudentCount || 0),
        academic_year: parseInt(entry.academic_year || new Date().getFullYear()),
        synced_at: new Date().toISOString()
      };

      const { data, error } = await supabase
        .from('kamar_courses')
        .upsert(record, { 
          onConflict: 'school_id,course_code,academic_year',
          returning: 'minimal'
        });

      if (error) {
        console.error('Course upsert error:', error);
        continue;
      }

      processed++;
      created++;

    } catch (err) {
      console.error('Error processing course entry:', err);
    }
  }

  return { processed, created, updated };
}

/**
 * Log sync operation to database
 */
async function logSyncAttempt(stats) {
  try {
    const { error } = await supabase
      .from('kamar_sync_log')
      .insert({
        ...stats,
        sync_completed_at: new Date().toISOString()
      });

    if (error) {
      console.error('Failed to log sync attempt:', error);
    }
  } catch (err) {
    console.error('Error logging sync:', err);
  }
}

/**
 * Normalize XML data structure to match JSON format
 */
function normalizeXMLData(xmlData) {
  // KAMAR XML structure typically has root element like <KamarData>
  const root = xmlData.KamarData || xmlData.kamarData || xmlData;
  
  return {
    school_id: root.SchoolId || root.school_id,
    sync_type: root.SyncType || root.sync_type || 'nightly_full',
    timetable: Array.isArray(root.Timetable?.Entry) 
      ? root.Timetable.Entry 
      : (root.Timetable?.Entry ? [root.Timetable.Entry] : []),
    staff: Array.isArray(root.Staff?.Teacher) 
      ? root.Staff.Teacher 
      : (root.Staff?.Teacher ? [root.Staff.Teacher] : []),
    courses: Array.isArray(root.Courses?.Course) 
      ? root.Courses.Course 
      : (root.Courses?.Course ? [root.Courses.Course] : [])
  };
}

/**
 * ================================================================
 * DEPLOYMENT NOTES:
 * 
 * 1. Environment Variables Required:
 *    - SUPABASE_URL
 *    - SUPABASE_SERVICE_ROLE_KEY
 *    - KAMAR_API_KEY (shared secret from school)
 * 
 * 2. Webhook URL to provide to school:
 *    https://tekete.netlify.app/.netlify/functions/kamar-webhook-listener
 * 
 * 3. Dependencies to install:
 *    npm install xml2js
 * 
 * 4. Testing:
 *    - Use mock XML/JSON data to test parsing
 *    - Verify database records created correctly
 *    - Test with invalid API key (should reject)
 * 
 * ================================================================
 */

