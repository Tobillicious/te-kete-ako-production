/**
 * UNIFIED AUTHENTICATION SYSTEM - Te Kete Ako
 * Consolidates all auth logic into ONE authoritative file
 */

// Configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

// Initialize Supabase client (SINGLE INSTANCE)
let supabaseClient = null;
let currentUser = null;
let authState = 'loading';

// Te Kete Auth System State
window.teKeteAuth = {
    authState: 'loading',
    currentUser: null,
    signIn: null,
    signOut: null,
    getCurrentUserToken: null
};

async function initSupabase() {
    if (supabaseClient) return supabaseClient;

    if (typeof window.supabaseSingleton === 'undefined') {
        console.error('❌ Supabase singleton not loaded');
        window.teKeteAuth.authState = 'error';
        return null;
    }

    supabaseClient = await window.supabaseSingleton.getClient();

    // Setup auth state listener
    setupAuthStateListener();

    // Check current session
    checkCurrentSession();

    window.supabaseClient = supabaseClient;
    return supabaseClient;
}

/**
 * Setup auth state change listener
 */
function setupAuthStateListener() {
    if (!supabaseClient) return;

    supabaseClient.auth.onAuthStateChange((event, session) => {
        currentUser = session?.user || null;
        window.teKeteAuth.currentUser = currentUser;

        // Update auth state
        if (event === 'SIGNED_IN') {
            authState = 'signed_in';
            window.teKeteAuth.authState = 'signed_in';
            handleSignInSuccess(currentUser);
        } else if (event === 'SIGNED_OUT') {
            authState = 'signed_out';
            window.teKeteAuth.authState = 'signed_out';
            handleSignOutSuccess();
        } else if (event === 'TOKEN_REFRESHED') {
            authState = 'signed_in';
            window.teKeteAuth.authState = 'signed_in';
        } else if (event === 'USER_UPDATED') {
            authState = 'signed_in';
            window.teKeteAuth.authState = 'signed_in';
        }

        // Dispatch event for other components
        window.dispatchEvent(new CustomEvent('teKeteAuthChange', {
            detail: { authState, currentUser }
        }));
    });
}

/**
 * Check current session on page load
 */
async function checkCurrentSession() {
    if (!supabaseClient) return;

    try {
        const { data: { session } } = await supabaseClient.auth.getSession();
        currentUser = session?.user || null;
        window.teKeteAuth.currentUser = currentUser;

        if (currentUser) {
            authState = 'signed_in';
            window.teKeteAuth.authState = 'signed_in';
        } else {
            authState = 'signed_out';
            window.teKeteAuth.authState = 'signed_out';
        }

        // Dispatch event for other components
        window.dispatchEvent(new CustomEvent('teKeteAuthChange', {
            detail: { authState, currentUser }
        }));
    } catch (error) {
        console.error('Session check error:', error);
        authState = 'error';
        window.teKeteAuth.authState = 'error';
    }
}

/**
 * Sign in with email and password
 */
async function signIn(email, password) {
    if (!supabaseClient) {
        throw new Error('Authentication system not initialized');
    }

    if (!email || !password) {
        throw new Error('Email and password are required');
    }

    try {
        const { data, error } = await supabaseClient.auth.signInWithPassword({
            email,
            password
        });

        if (error) {
            throw error;
        }

        return data;
    } catch (error) {
        console.error('Sign in error:', error);
        throw error;
    }
}

/**
 * Sign out current user
 */
async function signOut() {
    if (!supabaseClient) {
        throw new Error('Authentication system not initialized');
    }

    try {
        const { error } = await supabaseClient.auth.signOut();
        if (error) throw error;
    } catch (error) {
        console.error('Sign out error:', error);
        throw error;
    }
}

/**
 * Get current user JWT token
 */
async function getCurrentUserToken() {
    if (!supabaseClient || !currentUser) return null;

    try {
        const { data: { session } } = await supabaseClient.auth.getSession();
        return session?.access_token || null;
    } catch (error) {
        console.error('Token retrieval error:', error);
        return null;
    }
}

/**
 * Handle successful sign in
 */
function handleSignInSuccess(user) {
    document.body.classList.add('logged-in');
    document.body.classList.remove('logged-out');

    // Dispatch event for other components
    window.dispatchEvent(new CustomEvent('teKeteAuthSignIn', {
        detail: { user }
    }));
}

/**
 * Handle successful sign out
 */
function handleSignOutSuccess() {
    document.body.classList.add('logged-out');
    document.body.classList.remove('logged-in');

    // Dispatch event for other components
    window.dispatchEvent(new CustomEvent('teKeteAuthSignOut'));
}

/**
 * Role-based redirect after successful login
 */
async function redirectByRole(user) {
    try {
        // Fetch user profile to get role
        const { data: profile, error } = await supabaseClient
            .from('profiles')
            .select('role, first_name')
            .eq('user_id', user.id)
            .single();

        if (error) {
            console.error('Error fetching profile:', error);
            // Default redirect if profile not found
            window.location.href = '/getting-started.html';
            return;
        }

        // Role-based redirect using consistent routing
        const userRole = profile.role || 'student';

        if (userRole === 'teacher' || userRole === 'admin') {
            window.location.href = '/teacher-dashboard-unified.html';
        } else if (userRole === 'student') {
            window.location.href = '/student-dashboard.html';
        } else {
            window.location.href = '/getting-started.html';
        }
    } catch (error) {
        console.error('Redirect error:', error);
        // Fallback to getting started
        window.location.href = '/getting-started.html';
    }
}

// Set up Te Kete Auth System methods
window.teKeteAuth.signIn = signIn;
window.teKeteAuth.signOut = signOut;
window.teKeteAuth.getCurrentUserToken = getCurrentUserToken;
window.teKeteAuth.redirectByRole = redirectByRole;

// Wait for page load, then initialize
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSupabase);
} else {
    initSupabase();
}

// Export for global access
window.initSupabase = initSupabase;
window.getSupabaseClient = () => supabaseClient || initSupabase();

