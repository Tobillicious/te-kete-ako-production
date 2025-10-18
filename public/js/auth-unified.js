/**
 * UNIFIED AUTHENTICATION SYSTEM - Te Kete Ako
 * Consolidates all auth logic into ONE authoritative file
 */

// Configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

// Initialize Supabase client (SINGLE INSTANCE)
let supabaseClient = null;

function initSupabase() {
    if (supabaseClient) return supabaseClient;
    
    if (typeof window.supabase === 'undefined') {
        console.error('❌ Supabase library not loaded');
        return null;
    }
    
    supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
        auth: {
            autoRefreshToken: true,
            persistSession: true,
            detectSessionInUrl: true
        }
    });
    
    window.supabaseClient = supabaseClient;
    return supabaseClient;
}

// Wait for page load, then initialize
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSupabase);
} else {
    initSupabase();
}

// Export for global access
window.initSupabase = initSupabase;
window.getSupabaseClient = () => supabaseClient || initSupabase();

