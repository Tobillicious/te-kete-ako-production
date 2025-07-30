// Environment Configuration for Te Kete Ako
// This file loads environment variables safely for frontend use

// For development, these would be injected by build process or server
// For production, use Netlify environment variables: https://docs.netlify.com/configure-builds/environment-variables/

window.ENV = {
    // Supabase Configuration
    SUPABASE_URL: window.location.hostname === 'localhost' 
        ? 'https://kpawkfxdqzhrhumlutjw.supabase.co'  // Development
        : window.ENV?.SUPABASE_URL || 'https://kpawkfxdqzhrhumlutjw.supabase.co', // Production
    
    SUPABASE_ANON_KEY: window.location.hostname === 'localhost'
        ? 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtwYXdrZnhkcXpocmh1bWx1dGp3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE3ODE0MzUsImV4cCI6MjAzNzM1NzQzNX0.te0kutquDw1nIft0mcrvxOn_TEEtybBzM9IYf_IQa88'
        : window.ENV?.SUPABASE_ANON_KEY || 'ENVIRONMENT_VARIABLE_REQUIRED',
    
    // Environment indicators
    NODE_ENV: window.location.hostname === 'localhost' ? 'development' : 'production',
    IS_DEVELOPMENT: window.location.hostname === 'localhost'
};

// Security check
if (window.ENV.SUPABASE_ANON_KEY === 'ENVIRONMENT_VARIABLE_REQUIRED') {
    console.error('🚨 SECURITY: Supabase key not properly configured');
    console.error('Please set SUPABASE_ANON_KEY environment variable');
}

console.log('🔐 Environment loaded:', {
    hostname: window.location.hostname,
    env: window.ENV.NODE_ENV,
    supabase_configured: window.ENV.SUPABASE_ANON_KEY !== 'ENVIRONMENT_VARIABLE_REQUIRED'
});