const { createClient } = require('@supabase/supabase-js');

exports.handler = async (event) => {
  // Handle CORS
  const headers = {
    'Access-Control-Allow-Origin': process.env.SITE_URL || '*',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    const { email, password, role, displayName, schoolName, yearLevel } = JSON.parse(event.body);

    // Input validation
    if (!email || !password || !role) {
      return { statusCode: 400, headers, body: JSON.stringify({ success: false, message: 'Email, password, and role are required' }) };
    }
    if (!['teacher', 'student'].includes(role)) {
      return { statusCode: 400, headers, body: JSON.stringify({ success: false, message: 'Role must be either teacher or student' }) };
    }

    const supabase = createClient(
      process.env.SUPABASE_URL,
      process.env.SUPABASE_SERVICE_ROLE_KEY
    );

    // Create user with Supabase Auth. The trigger will handle the profile.
    const { data: authData, error: authError } = await supabase.auth.admin.createUser({
      email,
      password,
      email_confirm: true, // Auto-confirm for school environment
      user_metadata: {
        role,
        display_name: displayName || email.split('@')[0],
        school_name: schoolName || 'Mangakōtukutuku College',
        year_level: role === 'student' ? yearLevel : null
      }
    });

    if (authError) {
      console.error('Auth error:', authError);
      return { statusCode: 400, headers, body: JSON.stringify({ success: false, message: authError.message }) };
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        success: true,
        message: 'Registration successful! You can now log in.',
        user: {
          id: authData.user.id,
          email: authData.user.email,
          role: role
        }
      })
    };

  } catch (error) {
    console.error('Registration error:', error);
    return { statusCode: 500, headers, body: JSON.stringify({ success: false, message: 'Internal server error during registration' }) };
  }
};