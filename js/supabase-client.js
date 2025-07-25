// supabase-client.js
// CRITICAL: This file must be loaded AFTER the Supabase CDN script but BEFORE any dependent scripts

// Initialize Supabase client - using actual project credentials
const supabaseUrl = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE2NzM2MDQsImV4cCI6MjAzNzI0OTYwNH0.8tJj0dBaFKHKZQQP_5K_bSkU6W3yl4dj-mJ9V8XGmU8';

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
