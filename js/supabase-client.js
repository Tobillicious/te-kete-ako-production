// supabase-client.js
// CRITICAL: This file must be loaded AFTER the Supabase CDN script but BEFORE any dependent scripts

// Initialize Supabase client - using environment variables for security
const supabaseUrl = window.ENV?.SUPABASE_URL || 'https://kpawkfxdqzhrhumlutjw.supabase.co';
const supabaseKey = window.ENV?.SUPABASE_ANON_KEY || 'ENVIRONMENT_VARIABLE_REQUIRED';

// Create the global supabase client using the CDN-loaded library
const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);

// Global authentication helper functions
window.authHelpers = {
  async getCurrentUser() {
    const { data: { user } } = await supabase.auth.getUser();
    return user;
  },
  
  async signOut() {
    const { error } = await supabase.auth.signOut();
    if (error) throw error;
    return true;
  },
  
  async isLoggedIn() {
    const user = await this.getCurrentUser();
    return !!user;
  }
};

console.log('Supabase client initialized successfully');
