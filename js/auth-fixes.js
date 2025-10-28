// Temporary fixes for authentication issues
// This file provides workarounds until the database triggers are properly set up

// Fixed registration function that handles profile creation more robustly
async function fixedRegistrationSubmit(formData) {
    console.log('Starting fixed registration with formData:', formData);
    
    try {
        // 1. Ensure role is valid
        if (!formData.role || !['teacher', 'student', 'admin'].includes(formData.role)) {
            throw new Error('Invalid role specified. Must be teacher, student, or admin.');
        }
        
        // 2. Create Supabase auth user first
        const { data: authData, error: authError } = await supabase.auth.signUp({
            email: formData.email,
            password: formData.password,
            options: {
                data: {
                    full_name: formData.fullName,
                    role: formData.role,
                    school_name: formData.schoolName || 'Mangakōtukutuku College'
                }
            }
        });
        
        if (authError) {
            console.error('Auth signup error:', authError);
            throw authError;
        }
        
        if (!authData.user) {
            throw new Error('Registration failed - no user created');
        }
        
        console.log('User created successfully:', authData.user.id);
        
        // 3. Wait a moment for any potential triggers to run
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // 4. Check if profile already exists (in case trigger worked)
        const { data: existingProfile } = await supabase
            .from('profiles')
            .select('*')
            .eq('user_id', authData.user.id)
            .single();
            
        if (existingProfile) {
            console.log('Profile already exists from trigger:', existingProfile);
            return { success: true, user: authData.user, profile: existingProfile };
        }
        
        // 5. No profile exists, create it manually
        console.log('Creating profile manually...');
        
        // Set session first so RLS policies work
        if (authData.session) {
            await supabase.auth.setSession({
                access_token: authData.session.access_token,
                refresh_token: authData.session.refresh_token
            });
        }
        
        // Create profile with explicit role
        const profileData = {
            user_id: authData.user.id,
            email: formData.email,
            role: formData.role,  // Ensure this is exactly 'teacher', 'student', or 'admin'
            display_name: formData.fullName,
            school_name: formData.schoolName || 'Mangakōtukutuku College'
        };
        
        // Add role-specific fields
        if (formData.role === 'teacher') {
            profileData.teacher_role = formData.teacherRole || null;
            profileData.subjects_taught = formData.subjects || [];
            profileData.year_levels_taught = formData.yearLevels || [];
        } else if (formData.role === 'student') {
            profileData.year_level = formData.yearLevel || null;
            profileData.parent_email = formData.parentEmail || null;
        }
        
        console.log('Attempting to create profile with data:', profileData);
        
        const { data: profileResult, error: profileError } = await supabase
            .from('profiles')
            .insert(profileData)
            .select()
            .single();
            
        if (profileError) {
            console.error('Profile creation error:', profileError);
            
            // If profile creation fails, clean up the auth user
            await supabase.auth.signOut();
            
            throw new Error(`Profile creation failed: ${profileError.message}`);
        }
        
        console.log('Profile created successfully:', profileResult);
        
        return { 
            success: true, 
            user: authData.user, 
            profile: profileResult,
            requiresEmailVerification: !authData.session
        };
        
    } catch (error) {
        console.error('Registration error:', error);
        throw error;
    }
}

// Helper function to test if authentication is working
async function testAuthConnection() {
    try {
        // Test basic connection
        const { data, error } = await supabase.auth.getUser();
        console.log('Auth connection test:', { data, error });
        
        // Test database connection
        const { data: profileTest, error: profileError } = await supabase
            .from('profiles')
            .select('count')
            .limit(1);
            
        console.log('Database connection test:', { profileTest, profileError });
        
        return { authWorking: !error, dbWorking: !profileError };
    } catch (error) {
        console.error('Connection test failed:', error);
        return { authWorking: false, dbWorking: false, error };
    }
}

// Make functions available globally for testing
window.authFixes = {
    fixedRegistrationSubmit,
    testAuthConnection
};