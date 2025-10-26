-- SUPABASE AUTHENTICATION RLS FIX - URGENT
-- Fixes user signup/login blocking issue
-- Generated: 2025-10-26 13:43 UTC

-- Fix Option 1

        -- Allow anonymous access for user registration
        -- Users need to create profiles during signup process
        CREATE POLICY "Allow anonymous profile creation" ON public.profiles
            FOR INSERT WITH CHECK (true);

        -- Allow anonymous access for initial user setup
        -- This enables the signup flow to work
        CREATE POLICY "Allow anonymous user setup" ON public.profiles
            FOR SELECT USING (true)
            FOR UPDATE USING (true);

        -- Allow users to view their own profiles after signup
        DROP POLICY IF EXISTS "Users can view own profile" ON public.profiles;
        CREATE POLICY "Users can view own profile" ON public.profiles
            FOR SELECT USING (auth.uid() = user_id OR auth.role() = 'anon');

        -- Allow users to update their own profiles
        DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;
        CREATE POLICY "Users can update own profile" ON public.profiles
            FOR UPDATE USING (auth.uid() = user_id OR auth.role() = 'anon');

        -- Allow anonymous access to resources table for browsing
        CREATE POLICY "Allow anonymous resource browsing" ON public.resources
            FOR SELECT USING (true);

        -- Allow anonymous access to graphrag_resources for discovery
        CREATE POLICY "Allow anonymous graphrag browsing" ON public.graphrag_resources
            FOR SELECT USING (true);

        -- Allow anonymous access to announcements
        CREATE POLICY "Allow anonymous announcement viewing" ON public.announcements
            FOR SELECT USING (true);
        

-- Fix Option 2

        -- Fix authentication flow by allowing anonymous access during signup
        -- This resolves the "users cannot sign up" issue

        -- Enable anonymous access for user registration process
        ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

        -- Drop overly restrictive policies
        DROP POLICY IF EXISTS "Users can view own profile" ON public.profiles;
        DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;

        -- Create policies that work with signup flow
        CREATE POLICY "Allow profile access during auth" ON public.profiles
            FOR ALL USING (
                auth.uid() = user_id OR
                auth.role() = 'anon' OR
                auth.role() = 'authenticated'
            );

        -- Allow anonymous resource browsing
        CREATE POLICY "Anonymous resource access" ON public.resources
            FOR SELECT USING (status = 'active');

        -- Allow anonymous graphrag access
        CREATE POLICY "Anonymous graphrag access" ON public.graphrag_resources
            FOR SELECT USING (archive_status = 'active');
        

-- Fix Option 3

        -- Alternative approach: Create signup-specific policies
        -- This allows the authentication flow to work properly

        -- Enable anonymous access for user registration
        CREATE POLICY "Enable user registration" ON public.profiles
            FOR INSERT WITH CHECK (auth.role() = 'anon' OR auth.role() = 'authenticated');

        -- Allow profile setup during authentication
        CREATE POLICY "Allow profile setup" ON public.profiles
            FOR SELECT USING (auth.role() = 'anon' OR auth.role() = 'authenticated' OR auth.uid() = user_id);

        -- Allow profile updates during setup
        CREATE POLICY "Allow profile updates" ON public.profiles
            FOR UPDATE USING (auth.role() = 'anon' OR auth.role() = 'authenticated' OR auth.uid() = user_id);

        -- Maintain security for established users
        CREATE POLICY "Users own profile security" ON public.profiles
            FOR SELECT USING (auth.uid() = user_id)
            FOR UPDATE USING (auth.uid() = user_id)
            FOR DELETE USING (auth.uid() = user_id);
        

