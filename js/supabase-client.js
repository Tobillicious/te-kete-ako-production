import { createClient } from '@supabase/supabase-js';

// It's recommended to use environment variables for these
// In a local development environment, you might use a .env file
// In production (like on Netlify), you'll set these in the Netlify UI
const supabaseUrl = process.env.SUPABASE_URL || 'https://nlgldaqtubrlcqddppbq.supabase.co';
const supabaseAnonKey = process.env.SUPABASE_ANON_KEY || 'YOUR_FALLBACK_ANON_KEY';

// Export the Supabase client
export const supabase = createClient(supabaseUrl, supabaseAnonKey);
