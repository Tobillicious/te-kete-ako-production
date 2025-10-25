/**
 * ================================================================
 * LOGIN SYSTEM - TE KETE AKO
 * Role-based authentication with automatic redirect
 * ================================================================
 */

let supabaseClient = null;

// Wait for Supabase to be ready
window.addEventListener('supabaseReady', (event) => {
    supabaseClient = event.detail.client;
    checkExistingSession();
});

/**
 * Check if user is already logged in
 */
async function checkExistingSession() {
    try {
        const { data: { user } } = await supabaseClient.auth.getUser();
        
        if (user) {
            // User is logged in, redirect to appropriate dashboard
            await redirectByRole(user.id);
        }
    } catch (error) {
    }
}

/**
 * Handle login form submission
 */
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const loginBtn = document.getElementById('loginBtn');
    
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const email = document.getElementById('email')?.value;
            const password = document.getElementById('password')?.value;
            
            if (!email || !password) {
                showMessage('Please enter both email and password', 'error');
                return;
            }
            
            // Disable button
            if (loginBtn) {
                loginBtn.disabled = true;
                loginBtn.innerHTML = '⏳ Logging in...';
            }
            
            try {
                // Authenticate with Supabase
                const { data, error } = await supabaseClient.auth.signInWithPassword({
                    email: email,
                    password: password
                });
                
                if (error) throw error;
                
                // Success - redirect based on role
                showMessage('✅ Login successful! Redirecting...', 'success');
                
                // Wait briefly then redirect
                setTimeout(async () => {
                    await redirectByRole(data.user.id);
                }, 1000);
                
            } catch (error) {
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
                showMessage(error.message || 'Login failed. Please check your credentials.', 'error');
                
                if (loginBtn) {
                    loginBtn.disabled = false;
                    loginBtn.innerHTML = 'Log In →';
                }
            }
        });
    }
});

/**
 * Redirect user based on their role
 */
async function redirectByRole(userId) {
    try {
        // Get user profile to check role
        const { data: profile, error } = await supabaseClient
            .from('profiles')
            .select('role, first_name')
            .eq('user_id', userId)
            .single();
        
        if (error) throw error;
        
        // Redirect based on role
        if (profile.role === 'student') {
            window.location.href = '/student-dashboard.html';
        } else if (profile.role === 'teacher' || profile.role === 'admin') {
            window.location.href = '/teacher-dashboard-unified.html';
        } else {
            // Unknown role - go to homepage
            window.location.href = '/';
        }
        
    } catch (error) {
        // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
        // Fallback to homepage
        window.location.href = '/';
    }
}

/**
 * Show message
 */
function showMessage(message, type = 'info') {
    const messageEl = document.getElementById('loginMessage');
    if (!messageEl) return;
    
    messageEl.textContent = message;
    messageEl.style.display = 'block';
    
    if (type === 'error') {
        messageEl.style.background = '#fee2e2';
        messageEl.style.color = '#991b1b';
        messageEl.style.border = '1px solid #fca5a5';
    } else if (type === 'success') {
        messageEl.style.background = '#d1fae5';
        messageEl.style.color = '#065f46';
        messageEl.style.border = '1px solid #6ee7b7';
    } else {
        messageEl.style.background = '#dbeafe';
        messageEl.style.color = '#1e40af';
        messageEl.style.border = '1px solid #93c5fd';
    }
}

/**
 * Password reset
 */
async function resetPassword() {
    const email = prompt('Enter your email address to reset your password:');
    
    if (!email) return;
    
    try {
        const { error } = await supabaseClient.auth.resetPasswordForEmail(email, {
            redirectTo: `${window.location.origin}/reset-password.html`
        });
        
        if (error) throw error;
        
        alert('✅ Password reset email sent! Please check your inbox.');
        
    } catch (error) {
        // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
        alert('Error sending password reset email. Please try again.');
    }
}


