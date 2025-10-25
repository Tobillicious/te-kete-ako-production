/**
 * AUTH GATE COMPONENT
 * Redirects unauthenticated users to login page
 * Use on premium/protected content pages
 */

(async function initAuthGate() {
    // Check if user is authenticated via Supabase
    const { createClient } = supabase;
    
    const supabaseClient = createClient(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
    );
    
    try {
        // Get current session
        const { data: { session }, error } = await supabaseClient.auth.getSession();
        
        if (error) {
            console.error('Auth check error:', error);
            redirectToLogin();
            return;
        }
        
        if (!session) {
            // No active session - redirect to login
            redirectToLogin();
        } else {
            // User is authenticated - show content
            showProtectedContent();
        }
        
    } catch (err) {
        console.error('Auth gate error:', err);
        redirectToLogin();
    }
})();

function redirectToLogin() {
    // Save current page URL to return after login
    const currentPage = window.location.pathname + window.location.search;
    sessionStorage.setItem('returnUrl', currentPage);
    
    // Show loading message
    document.body.innerHTML = `
        <div style="display: flex; align-items: center; justify-content: center; height: 100vh; background: linear-gradient(135deg, #1a4d2e 0%, #2d5a3d 100%); font-family: system-ui, sans-serif;">
            <div style="text-align: center; color: white; max-width: 500px; padding: 40px;">
                <h1 style="font-size: 2.5em; margin-bottom: 20px;">🔐 Premium Content</h1>
                <p style="font-size: 1.2em; margin-bottom: 30px;">
                    This resource requires an active Te Kete Ako subscription.
                </p>
                <p style="font-size: 1em; opacity: 0.9; margin-bottom: 30px;">
                    Redirecting you to login...
                </p>
                <div class="spinner" style="border: 4px solid rgba(255,255,255,0.3); border-top: 4px solid white; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto;"></div>
            </div>
        </div>
        <style>
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    `;
    
    // Redirect after brief delay
    setTimeout(() => {
        window.location.href = '/login.html?redirect=' + encodeURIComponent(currentPage);
    }, 1500);
}

function showProtectedContent() {
    // Content is already visible, just add authenticated class
    document.body.classList.add('authenticated');
    
    // Optional: Show user info in header
    displayUserInfo();
}

async function displayUserInfo() {
    const { createClient } = supabase;
    const supabaseClient = createClient(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
    );
    
    const { data: { user } } = await supabaseClient.auth.getUser();
    
    if (user) {
        // Add user indicator to header if exists
        const header = document.querySelector('header') || document.querySelector('nav');
        if (header && !document.getElementById('user-indicator')) {
            const userIndicator = document.createElement('div');
            userIndicator.id = 'user-indicator';
            userIndicator.style.cssText = 'position: absolute; top: 20px; right: 20px; background: #f4d03f; color: #1a4d2e; padding: 8px 16px; border-radius: 20px; font-weight: bold;';
            userIndicator.innerHTML = `👤 Kia ora, ${user.email?.split('@')[0] || 'User'}`;
            header.style.position = 'relative';
            header.appendChild(userIndicator);
        }
    }
}

