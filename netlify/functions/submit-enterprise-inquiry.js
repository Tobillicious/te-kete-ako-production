// Enterprise Inquiry Submission Handler
// Created: October 26, 2025
// Purpose: Process enterprise contact form submissions

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
      name,
      email,
      organization,
      role,
      userCount,
      features,
      timeline,
      message
    } = JSON.parse(event.body);

    // Validate required fields
    if (!name || !email || !organization) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Missing required fields' })
      };
    }

    // Store in database
    const { data, error } = await supabase
      .from('enterprise_inquiries')
      .insert([{
        name,
        email,
        organization,
        role,
        user_count: userCount,
        features_interested: features,
        timeline,
        message,
        status: 'new',
        created_at: new Date().toISOString()
      }]);

    if (error) throw error;

    // Send notification email to sales team
    const salesEmailContent = `
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background: #1a4d2e; color: white; padding: 20px; border-radius: 8px 8px 0 0; }
        .content { background: #f9f9f9; padding: 20px; border-radius: 0 0 8px 8px; }
        .details { background: white; padding: 15px; margin: 10px 0; border-left: 4px solid #16a34a; }
        .high-value { background: #fef3c7; border-left-color: #f59e0b; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 New Enterprise Inquiry!</h1>
        </div>
        <div class="content">
            <p><strong>New enterprise lead received!</strong></p>
            
            <div class="details ${parseInt(userCount) > 100 ? 'high-value' : ''}">
                <strong>Contact Information:</strong><br>
                Name: ${name}<br>
                Email: ${email}<br>
                Organization: ${organization}<br>
                Role: ${role || 'Not specified'}
            </div>
            
            <div class="details">
                <strong>Opportunity Size:</strong><br>
                User Count: ${userCount || 'Not specified'}<br>
                Timeline: ${timeline || 'Not specified'}
            </div>
            
            <div class="details">
                <strong>Features of Interest:</strong><br>
                ${Array.isArray(features) ? features.join(', ') : features || 'Not specified'}
            </div>
            
            <div class="details">
                <strong>Message:</strong><br>
                ${message || 'No message provided'}
            </div>
            
            <h3>💰 Revenue Potential:</h3>
            <p>${calculateRevenuePotential(userCount, timeline)}</p>
            
            <p><strong>Next Steps:</strong></p>
            <ol>
                <li>Contact ${name} within 24 hours at ${email}</li>
                <li>Schedule discovery call</li>
                <li>Prepare custom proposal</li>
                <li>Close deal! 🎯</li>
            </ol>
            
            <p>Kia kaha!<br>
            Te Kete Ako Sales System</p>
        </div>
    </div>
</body>
</html>
    `;

    // Send confirmation email to prospect
    const prospectEmailContent = `
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
            <h1>Thank You for Your Interest!</h1>
        </div>
        <div class="content">
            <p>Kia ora ${name},</p>
            
            <p>Thank you for your interest in Te Kete Ako Enterprise! We're excited about the opportunity to work with ${organization}.</p>
            
            <p><strong>What happens next?</strong></p>
            <ol>
                <li>A member of our team will contact you within 24 hours</li>
                <li>We'll schedule a discovery call to understand your needs</li>
                <li>We'll prepare a custom proposal tailored to ${organization}</li>
                <li>We'll work together to create an implementation plan</li>
            </ol>
            
            <p><strong>Why schools choose Te Kete Ako Enterprise:</strong></p>
            <ul>
                <li>✅ 1,640 culturally-integrated resources (621 gold standard)</li>
                <li>✅ KAMAR integration (automatic timetable sync)</li>
                <li>✅ AI-powered features ($500K+ in development)</li>
                <li>✅ Dedicated account manager</li>
                <li>✅ Custom content development</li>
                <li>✅ On-site training and workshops</li>
                <li>✅ 100% Aotearoa-focused platform</li>
            </ul>
            
            <p>We look forward to speaking with you soon!</p>
            
            <p>Ngā mihi nui,<br>
            Te Kete Ako Enterprise Team<br>
            enterprise@tekete.co.nz</p>
        </div>
    </div>
</body>
</html>
    `;

    // Log for now (TODO: Integrate email service)
    console.log('Enterprise Inquiry Received:');
    console.log('From:', name, email);
    console.log('Organization:', organization);
    console.log('User Count:', userCount);
    console.log('Sales Email:', salesEmailContent);
    console.log('Prospect Email:', prospectEmailContent);

    return {
      statusCode: 200,
      body: JSON.stringify({ 
        success: true,
        message: 'Thank you! We will contact you within 24 hours.',
        note: 'Inquiry saved to database'
      })
    };

  } catch (error) {
    console.error('Enterprise inquiry error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Failed to submit inquiry',
        details: error.message 
      })
    };
  }
};

// Calculate revenue potential
function calculateRevenuePotential(userCount, timeline) {
  const users = parseInt(userCount) || 50;
  const basePrice = users <= 12 ? 200 : 
                   users <= 50 ? 450 : 
                   users <= 1000 ? 600 : 1000; // Enterprise custom
  
  const monthlyRevenue = basePrice;
  const annualRevenue = monthlyRevenue * 12;
  
  return `Monthly: $${monthlyRevenue} NZD | Annual: $${annualRevenue} NZD`;
}
