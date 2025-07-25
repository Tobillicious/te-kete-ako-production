const { createClient } = require('@supabase/supabase-js');

// Initialize Supabase client
const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

exports.handler = async (event, context) => {
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
    return {
      statusCode: 405,
      headers,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const { email, password, role, displayName, schoolName, yearLevel } = JSON.parse(event.body);

    // Input validation
    if (!email || !password || !role) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ 
          success: false, 
          message: 'Email, password, and role are required' 
        })
      };
    }

    // Validate role
    if (!['teacher', 'student'].includes(role)) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ 
          success: false, 
          message: 'Role must be either teacher or student' 
        })
      };
    }

    // Validate email domain for teachers (optional security measure)
    if (role === 'teacher' && !email.includes('@')) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ 
          success: false, 
          message: 'Valid email address required' 
        })
      };
    }

    // Create user with Supabase Auth
    const { data: authData, error: authError } = await supabase.auth.admin.createUser({
      email,
      password,
      email_confirm: true, // Auto-confirm for school environment
      user_metadata: {
        role,
        display_name: displayName,
        school_name: schoolName || 'Mangakōtukutuku College',
        year_level: yearLevel
      }
    });

    if (authError) {
      console.error('Auth error:', authError);
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ 
          success: false, 
          message: authError.message 
        })
      };
    }

    // Create profile record
    const { data: profileData, error: profileError } = await supabase
      .from('profiles')
      .insert([{
        user_id: authData.user.id,
        email: email,
        role: role,
        display_name: displayName || email.split('@')[0],
        school_name: schoolName || 'Mangakōtukutuku College',
        year_level: role === 'student' ? yearLevel : null,
        created_at: new Date().toISOString()
      }]);

    if (profileError) {
      console.error('Profile creation error:', profileError);
      // Clean up auth user if profile creation fails
      await supabase.auth.admin.deleteUser(authData.user.id);
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ 
          success: false, 
          message: 'Failed to create user profile' 
        })
      };
    }

    // Return success without exposing sensitive data
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
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ 
        success: false, 
        message: 'Internal server error during registration' 
      })
    };
  }
};