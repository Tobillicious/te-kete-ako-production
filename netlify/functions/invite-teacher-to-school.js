// Invite Teacher to School License
// Created: October 26, 2025
// Purpose: School admins can invite teachers to their school license

const { createClient } = require('@supabase/supabase-js');

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const {
      teacherEmail,
      schoolName,
      adminName,
      maxUsers
    } = JSON.parse(event.body);

    if (!teacherEmail || !schoolName || !adminName) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Missing required fields' })
      };
    }

    // Check if school has reached max users
    const { count: currentTeachers } = await supabase
      .from('profiles')
      .select('*', { count: 'exact', head: true })
      .eq('school_name', schoolName)
      .eq('role', 'teacher');

    if (currentTeachers >= maxUsers) {
      return {
        statusCode: 400,
        body: JSON.stringify({ 
          error: `Your school has reached its maximum of ${maxUsers} teachers. Please upgrade your plan.`
        })
      };
    }

    // Check if teacher already exists
    const { data: existingTeacher } = await supabase
      .from('profiles')
      .select('*')
      .eq('email', teacherEmail)
      .single();

    if (existingTeacher) {
      // Teacher already exists, update their school
      if (existingTeacher.school_name === schoolName) {
        return {
          statusCode: 200,
          body: JSON.stringify({ 
            message: 'Teacher is already in your school!',
            alreadyEnrolled: true
          })
        };
      } else {
        return {
          statusCode: 400,
          body: JSON.stringify({ 
            error: 'This teacher is already enrolled in another school. They must contact support to transfer.'
          })
        };
      }
    }

    // Create invitation email
    const invitationEmailContent = `
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background: #2F4F2F; color: white; padding: 20px; border-radius: 8px 8px 0 0; }
        .content { background: #f9f9f9; padding: 20px; border-radius: 0 0 8px 8px; }
        .button { display: inline-block; padding: 12px 24px; margin: 20px 0; 
                  background: #8B4513; color: white; text-decoration: none; 
                  border-radius: 8px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎓 You're Invited to Te Kete Ako!</h1>
        </div>
        <div class="content">
            <p>Kia ora!</p>
            
            <p><strong>${adminName}</strong> from <strong>${schoolName}</strong> has invited you to join Te Kete Ako!</p>
            
            <h3>What is Te Kete Ako?</h3>
            <p>Te Kete Ako is a professional educational platform with:</p>
            <ul>
                <li>✅ 3,500+ culturally-integrated teaching resources</li>
                <li>✅ AI lesson planning assistant</li>
                <li>✅ KAMAR integration (automatic timetable sync)</li>
                <li>✅ Weekly planner & teacher dashboard</li>
                <li>✅ 621 gold-standard lessons (Q90+)</li>
                <li>✅ Professional development tools</li>
            </ul>
            
            <h3>Your School License Includes:</h3>
            <ul>
                <li>Full access to all premium features</li>
                <li>KAMAR integration (sync your timetable)</li>
                <li>Collaboration with ${schoolName} teachers</li>
                <li>School-wide analytics dashboard</li>
                <li>Priority support</li>
            </ul>
            
            <div style="text-align: center;">
                <a href="${process.env.URL}/signup-teacher.html?school=${encodeURIComponent(schoolName)}" class="button">
                    Accept Invitation & Join ${schoolName}
                </a>
            </div>
            
            <p><strong>Next Steps:</strong></p>
            <ol>
                <li>Click the button above to create your account</li>
                <li>Complete your teacher profile</li>
                <li>Start exploring 3,500+ resources!</li>
                <li>Sync your KAMAR timetable (if your school has KAMAR)</li>
            </ol>
            
            <p>We're excited to have you join Te Kete Ako!</p>
            
            <p>Ngā mihi,<br>
            Te Kete Ako Team</p>
            
            <p style="color: #666; font-size: 0.9em; margin-top: 20px;">
                Questions? Contact your school admin (${adminName}) or email support@tekete.co.nz
            </p>
        </div>
    </div>
</body>
</html>
    `;

    // Log for now (TODO: Integrate email service)
    console.log('Teacher Invitation Email:');
    console.log('To:', teacherEmail);
    console.log('School:', schoolName);
    console.log('From:', adminName);
    console.log('Email content:', invitationEmailContent);

    // Create invitation record (optional - for tracking)
    // Could add an 'invitations' table later

    return {
      statusCode: 200,
      body: JSON.stringify({ 
        success: true,
        message: `Invitation sent to ${teacherEmail}`,
        note: 'Email integration pending - currently logging only'
      })
    };

  } catch (error) {
    console.error('Teacher invitation error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Failed to send invitation',
        details: error.message 
      })
    };
  }
};
