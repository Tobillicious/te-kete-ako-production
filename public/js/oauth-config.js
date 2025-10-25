/**
 * OAuth Configuration - Te Kete Ako
 * Google & Microsoft OAuth integration for one-click teacher signup
 * Phase 1 of Tech Stack Evolution
 */

class TeKeteOAuth {
    constructor() {
        this.supabase = null;
        this.initAsync();
    }
    
    async initAsync() {
        if (window.supabaseSingleton) {
            this.supabase = await window.supabaseSingleton.getClient();
        }
        this.init();
    }

    init() {
        this.setupOAuthButtons();
        this.handleOAuthRedirects();
    }

    setupOAuthButtons() {
        // Google OAuth Button
        const googleBtn = document.getElementById('google-signin-btn');
        if (googleBtn) {
            googleBtn.addEventListener('click', () => this.signInWithGoogle());
        }

        // Microsoft OAuth Button  
        const microsoftBtn = document.getElementById('microsoft-signin-btn');
        if (microsoftBtn) {
            microsoftBtn.addEventListener('click', () => this.signInWithMicrosoft());
        }
    }

    async signInWithGoogle() {
        try {
            const { data, error } = await this.supabase.auth.signInWithOAuth({
                provider: 'google',
                options: {
                    redirectTo: `${window.location.origin}/auth-callback.html`,
                    queryParams: {
                        access_type: 'offline',
                        prompt: 'consent',
                    }
                }
            });

            if (error) throw error;
            
            // Show loading state
            this.showLoadingState('google');
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.showError('Google sign-in failed. Please try again.');
        }
    }

    async signInWithMicrosoft() {
        try {
            const { data, error } = await this.supabase.auth.signInWithOAuth({
                provider: 'azure',
                options: {
                    redirectTo: `${window.location.origin}/auth-callback.html`,
                    scopes: 'openid email profile'
                }
            });

            if (error) throw error;
            
            // Show loading state
            this.showLoadingState('microsoft');
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.showError('Microsoft sign-in failed. Please try again.');
        }
    }

    async handleOAuthRedirects() {
        // Check if we're returning from OAuth
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        const error = urlParams.get('error');

        if (error) {
            this.showError(`OAuth error: ${error}`);
            return;
        }

        if (code) {
            // Handle OAuth callback
            await this.handleOAuthCallback(code);
        }
    }

    async handleOAuthCallback(code) {
        try {
            const { data, error } = await this.supabase.auth.exchangeCodeForSession(code);
            
            if (error) throw error;
            
            if (data.user) {
                // Success! Redirect to dashboard
                this.showSuccess('Welcome to Te Kete Ako!');
                setTimeout(() => {
                    window.location.href = '/teacher-dashboard.html';
                }, 2000);
            }
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.showError('Authentication failed. Please try again.');
        }
    }

    showLoadingState(provider) {
        const btn = document.getElementById(`${provider}-signin-btn`);
        if (btn) {
            btn.innerHTML = `
                <svg class="animate-spin h-4 w-4 mr-2" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
                    <path d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" fill="currentColor"/>
                </svg>
                Signing in...
            `;
            btn.disabled = true;
        }
    }

    showSuccess(message) {
        this.showNotification(message, 'success');
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showNotification(message, type) {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'success' ? 'bg-green-500 text-white' : 'bg-red-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
}

// Initialize OAuth when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new TeKeteOAuth());
} else {
    new TeKeteOAuth();
}

// Export for global access
window.TeKeteOAuth = TeKeteOAuth;
