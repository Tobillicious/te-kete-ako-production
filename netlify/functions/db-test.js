const { createClient } = require('@supabase/supabase-js');

exports.handler = async (event) => {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers };
  }

  try {
    const supabase = createClient(
      process.env.SUPABASE_URL,
      process.env.SUPABASE_SERVICE_ROLE_KEY
    );

    // Test 1: Check if profiles table exists and what's in it
    const { data: profiles, error: profilesError } = await supabase
      .from('profiles')
      .select('*')
      .limit(5);

    // Test 2: Check authentication users
    const { data: users, error: usersError } = await supabase.auth.admin.listUsers();

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({
        success: true,
        tests: {
          profiles: {
            error: profilesError?.message || null,
            data: profiles || [],
            count: profiles?.length || 0
          },
          users: {
            error: usersError?.message || null,
            count: users?.users?.length || 0,
            recent_users: users?.users?.slice(0, 3).map(u => ({
              id: u.id,
              email: u.email,
              created_at: u.created_at,
              user_metadata: u.user_metadata
            })) || []
          }
        }
      })
    };

  } catch (error) {
    console.error('Database test error:', error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({
        success: false,
        error: error.message
      })
    };
  }
};