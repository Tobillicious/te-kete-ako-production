// Te Kete Ako - Environment Configuration
// This file sets up environment variables for frontend use securely

// Load environment variables into window.ENV
window.ENV = window.ENV || {};

// Configuration loader - checks multiple sources
function loadEnvironmentConfig() {
    // For production deployment, these should come from build-time injection
    // For local development, use the .env file values
    
    const isDevelopment = window.location.hostname === 'localhost' || 
                         window.location.hostname === '127.0.0.1' ||
                         window.location.hostname === '';
    
    if (isDevelopment) {
        // Development environment - load from .env equivalent
        window.ENV.SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
        window.ENV.SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtwYXdrZnhkcXpocmh1bWx1dGp3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE3ODE0MzUsImV4cCI6MjAzNzM1NzQzNX0.te0kutquDw1nIft0mcrvxOn_TEEtybBzM9IYf_IQa88';
        window.ENV.NEO4J_URI = 'neo4j+s://cd5763ca.databases.neo4j.io';
        window.ENV.NODE_ENV = 'development';
        
        console.log('🔧 Development environment loaded');
    } else {
        // Production environment - should be injected by build process
        if (!window.ENV.SUPABASE_URL || !window.ENV.SUPABASE_ANON_KEY) {
            console.error('🚨 Production environment variables not configured!');
            console.error('Please ensure build process injects SUPABASE_URL and SUPABASE_ANON_KEY');
            
            // Fallback values for graceful degradation
            window.ENV.SUPABASE_URL = window.ENV.SUPABASE_URL || 'ENVIRONMENT_VARIABLE_REQUIRED';
            window.ENV.SUPABASE_ANON_KEY = window.ENV.SUPABASE_ANON_KEY || 'ENVIRONMENT_VARIABLE_REQUIRED';
        }
        
        window.ENV.NODE_ENV = 'production';
        console.log('🌐 Production environment loaded');
    }
    
    // Set environment flags
    window.ENV.IS_DEVELOPMENT = isDevelopment;
    window.ENV.IS_CONFIGURED = window.ENV.SUPABASE_ANON_KEY !== 'ENVIRONMENT_VARIABLE_REQUIRED';
}

// Configuration validation
function validateConfiguration() {
    const required = ['SUPABASE_URL', 'SUPABASE_ANON_KEY'];
    const missing = required.filter(key => 
        !window.ENV[key] || window.ENV[key] === 'ENVIRONMENT_VARIABLE_REQUIRED'
    );
    
    if (missing.length > 0) {
        console.error('❌ Missing environment variables:', missing);
        return false;
    }
    
    console.log('✅ All required environment variables configured');
    return true;
}

// Initialize configuration
loadEnvironmentConfig();
const isConfigured = validateConfiguration();

// Export helpers
window.checkEnvironmentConfig = validateConfiguration;
window.isEnvironmentConfigured = () => isConfigured;

// Development helper
if (window.ENV.IS_DEVELOPMENT) {
    window.setDevEnvironment = function(config) {
        Object.assign(window.ENV, config);
        console.log('🔧 Development environment updated:', config);
    };
}

console.log('🌟 Te Kete Ako environment configuration ready:', {
    environment: window.ENV.NODE_ENV,
    configured: window.ENV.IS_CONFIGURED,
    development: window.ENV.IS_DEVELOPMENT
});