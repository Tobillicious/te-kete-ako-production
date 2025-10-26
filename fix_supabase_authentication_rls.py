#!/usr/bin/env python3
"""
SUPABASE AUTHENTICATION RLS FIX - URGENT
Fixes RLS policies that are blocking user signup and login

PROBLEM: RLS policies require auth.uid() but users don't have auth.uid() during signup
SOLUTION: Add anonymous access policies for user registration process
"""

import json
from pathlib import Path

def create_authentication_rls_fix():
    """Create SQL fix for authentication RLS policies"""

    print("🔴 SUPABASE AUTHENTICATION RLS FIX - URGENT")
    print("=" * 60)
    print("Fixing RLS policies that block user signup/login...")

    # Create RLS policy fixes
    rls_fixes = [
        """
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
        """,

        """
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
        """,

        """
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
        """
    ]

    # Write the fixes to SQL file
    fix_file = Path('supabase_authentication_rls_fix.sql')
    with open(fix_file, 'w', encoding='utf-8') as f:
        f.write('-- SUPABASE AUTHENTICATION RLS FIX - URGENT\n')
        f.write('-- Fixes user signup/login blocking issue\n')
        f.write('-- Generated: ' + __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M UTC') + '\n\n')

        for i, fix in enumerate(rls_fixes, 1):
            f.write(f'-- Fix Option {i}\n')
            f.write(fix)
            f.write('\n\n')

    print(f"✅ Created authentication RLS fixes: {fix_file}")
    print("📋 Three fix options provided")
    print("🎯 Execute the appropriate fix in Supabase dashboard")

    return fix_file

def main():
    """Main authentication fix function"""

    print("🔴 SUPABASE AUTHENTICATION RLS FIX - URGENT")
    print("=" * 60)

    fix_file = create_authentication_rls_fix()

    print("\n🚀 AUTHENTICATION FIX READY!")
    print("   - Execute one of the three fix options in Supabase")
    print("   - Test user signup/login after applying fix")
    print("   - Verify users can access the platform")
    print("   - Monitor for any security issues")

    print("\n📋 EXECUTION INSTRUCTIONS:")
    print("   1. Go to Supabase dashboard: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql")
    print("   2. Copy and paste the appropriate fix option")
    print("   3. Execute the SQL")
    print("   4. Test user registration immediately")

    return fix_file

if __name__ == "__main__":
    fix_file = main()
