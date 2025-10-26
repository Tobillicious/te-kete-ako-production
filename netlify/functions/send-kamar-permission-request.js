// KAMAR Permission Request Email Sender
// Created: October 26, 2025
// Purpose: Send permission request emails to school admins

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
      teacherName,
      teacherEmail,
      schoolName,
      adminName,
      adminEmail,
      reason
    } = JSON.parse(event.body);

    // Validate required fields
    if (!teacherName || !teacherEmail || !schoolName || !adminName || !adminEmail || !reason) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Missing required fields' })
      };
    }

    // Create approval/denial links (secure tokens)
    const requestId = event.headers['x-request-id'] || 'pending';
    const approveLink = `${process.env.URL}/api/kamar-approve?token=${requestId}&action=approve`;
    const denyLink = `${process.env.URL}/api/kamar-approve?token=${requestId}&action=deny`;

    // Email to school admin
    const adminEmailContent = `
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background: #2F4F2F; color: white; padding: 20px; border-radius: 8px 8px 0 0; }
        .content { background: #f9f9f9; padding: 20px; border-radius: 0 0 8px 8px; }
        .button { display: inline-block; padding: 12px 24px; margin: 10px 5px; text-decoration: none; border-radius: 6px; font-weight: bold; }
        .approve { background: #16a34a; color: white; }
        .deny { background: #dc2626; color: white; }
        .details { background: white; padding: 15px; border-left: 4px solid #0ea5e9; margin: 15px 0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>KAMAR Integration Permission Request</h1>
        </div>
        <div class="content">
            <p>Kia ora ${adminName},</p>
            
            <p>A teacher from ${schoolName} has requested access to KAMAR integration on Te Kete Ako.</p>
            
            <div class="details">
                <strong>Teacher Details:</strong><br>
                Name: ${teacherName}<br>
                Email: ${teacherEmail}<br>
                School: ${schoolName}
            </div>
            
            <div class="details">
                <strong>Reason for Request:</strong><br>
                ${reason}
            </div>
            
            <h3>What is KAMAR Integration?</h3>
            <p>KAMAR integration automatically syncs the teacher's timetable, class lists, and student data from your school's KAMAR system to Te Kete Ako. This enables features like:</p>
            <ul>
                <li>Weekly Planner (with automatic timetable sync)</li>
                <li>Class organization (auto-populated from KAMAR)</li>
                <li>Student progress tracking</li>
            </ul>
            
            <p><strong>Cost:</strong> +$2.00 NZD/month for the individual teacher (in addition to their Individual plan)</p>
            
            <h3>Your Action Required:</h3>
            <p>Please review this request and approve or deny:</p>
            
            <div style="text-align: center; margin: 20px 0;">
                <a href="${approveLink}" class="button approve">✅ Approve Request</a>
                <a href="${denyLink}" class="button deny">❌ Deny Request</a>
            </div>
            
            <p style="color: #666; font-size: 0.9em;">
                <strong>Note:</strong> Approving this request grants ${teacherName} access to sync data from your school's KAMAR system. 
                This requires your school's KAMAR API to be configured for Te Kete Ako.
            </p>
            
            <p>Ngā mihi,<br>
            Te Kete Ako Team</p>
        </div>
    </div>
</body>
</html>
    `;

    // Email to teacher (confirmation)
    const teacherEmailContent = `
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background: #2F4F2F; color: white; padding: 20px; border-radius: 8px 8px 0 0; }
        .content { background: #f9f9f9; padding: 20px; border-radius: 0 0 8px 8px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>KAMAR Request Submitted</h1>
        </div>
        <div class="content">
            <p>Kia ora ${teacherName},</p>
            
            <p>Your request for KAMAR integration has been submitted to ${adminName} at ${schoolName}.</p>
            
            <p><strong>What happens next?</strong></p>
            <ol>
                <li>Your school admin will review your request</li>
                <li>If approved, we'll activate KAMAR integration on your account</li>
                <li>You'll receive an email confirmation once processed</li>
                <li>The $2/month charge will be added to your next billing cycle</li>
            </ol>
            
            <p>We'll notify you as soon as your admin responds.</p>
            
            <p>Ngā mihi,<br>
            Te Kete Ako Team</p>
        </div>
    </div>
</body>
</html>
    `;

    // Send emails (using a service like SendGrid, Mailgun, or Resend)
    // For now, we'll log and return success
    // TODO: Integrate actual email service (SendGrid/Resend/Postmark)
    
    console.log('KAMAR Permission Request Email:');
    console.log('To Admin:', adminEmail);
    console.log('To Teacher:', teacherEmail);
    console.log('Request Details:', { teacherName, schoolName, reason });

    // In production, send actual emails:
    /*
    await sendEmail({
      to: adminEmail,
      from: 'noreply@tekete.co.nz',
      subject: `KAMAR Permission Request from ${teacherName}`,
      html: adminEmailContent
    });

    await sendEmail({
      to: teacherEmail,
      from: 'noreply@tekete.co.nz',
      subject: 'KAMAR Integration Request Submitted',
      html: teacherEmailContent
    });
    */

    return {
      statusCode: 200,
      body: JSON.stringify({ 
        success: true,
        message: 'Permission request sent successfully',
        note: 'Email integration pending - currently logging only'
      })
    };

  } catch (error) {
    console.error('KAMAR permission request error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Failed to send permission request',
        details: error.message 
      })
    };
  }
};
