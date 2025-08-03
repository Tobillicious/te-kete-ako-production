/**
 * Site-wide Authentication Gate for Te Kete Ako
 * Ensures no access to any page without being logged in
 * This script runs on every page and enforces authentication
 */

class AuthGate {
    constructor() {
        this.supabase = null;
        this.currentUser = null;
        this.isPublicPage = this.checkIfPublicPage();
        this.isInitializing = false;
        
        // Start initialization immediately
        this.init();
    }

    async init() {
        if (this.isInitializing) return;
        this.isInitializing = true;

        try {
            console.log('🔐 AuthGate: Initializing site-wide authentication...');
            
            // Wait for Supabase client
            await this.waitForSupabase();
            
            // Check authentication status
            await this.checkAuthStatus();
            
            // Set up auth state listeners
            this.setupAuthStateListener();
            
            console.log('🔐 AuthGate: Initialization complete');
            
        } catch (error) {
            console.error('🚨 AuthGate: Initialization failed:', error);
            this.handleAuthFailure();
        } finally {
            this.isInitializing = false;
        }
    }

    checkIfPublicPage() {
        const currentPath = window.location.pathname;
        const filename = currentPath.split('/').pop() || 'index.html';
        
        // Define public pages that don't require authentication
        const publicPages = [
            'index.html',
            'login.html', 
            'register-simple.html',
            'register.html',
            'forgot-password.html',
            'reset-password.html',
            'public-landing.html',
            'about.html',
            'contact.html',
            'privacy-policy.html',
            'terms.html'
        ];
        
        // Also allow root path
        if (currentPath === '/' || currentPath === '/index.html' || currentPath === '') {
            return true;
        }
        
        return publicPages.includes(filename);
    }

    async waitForSupabase() {
        // First check if getSupabaseClient exists (from shared-components.js)
        if (typeof window.getSupabaseClient === 'function') {
            this.supabase = window.getSupabaseClient();
            return;
        }
        
        // Wait for shared-components.js to load
        return new Promise((resolve, reject) => {
            let attempts = 0;
            const maxAttempts = 100; // 10 seconds
            
            const checkInterval = setInterval(() => {
                attempts++;
                
                if (typeof window.getSupabaseClient === 'function') {
                    clearInterval(checkInterval);
                    this.supabase = window.getSupabaseClient();
                    resolve();
                } else if (attempts >= maxAttempts) {
                    clearInterval(checkInterval);
                    
                    // Fallback: try to create Supabase client directly
                    if (typeof window.supabase !== 'undefined' && window.supabase.createClient) {
                        const url = 'https://nlgldaqtubrlcqddppbq.supabase.co';
                        const key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
                        this.supabase = window.supabase.createClient(url, key);
                        resolve();
                    } else {
                        reject(new Error('Supabase client not available after 10 seconds'));
                    }
                }
            }, 100);
        });
    }

    async checkAuthStatus() {
        try {
            const { data: { session } } = await this.supabase.auth.getSession();
            this.currentUser = session?.user || null;
            
            console.log('🔐 AuthGate: Auth status checked:', {
                isLoggedIn: !!this.currentUser,
                isPublicPage: this.isPublicPage,
                currentPath: window.location.pathname
            });

            // Apply authentication rules
            this.enforceAuthRules();
            
        } catch (error) {
            console.error('🚨 AuthGate: Auth status check failed:', error);
            this.handleAuthFailure();
        }
    }

    enforceAuthRules() {
        const isLoggedIn = !!this.currentUser;
        
        if (!isLoggedIn && !this.isPublicPage) {
            // User is not logged in and trying to access protected content
            console.log('🚨 AuthGate: Unauthorized access attempt, redirecting to login...');
            this.redirectToLogin();
        } else if (isLoggedIn && (window.location.pathname.endsWith('login.html') || window.location.pathname.endsWith('register-simple.html'))) {
            // User is logged in but on auth pages, redirect to main site
            console.log('🔐 AuthGate: User already logged in, redirecting to main site...');
            this.redirectToMainSite();
        } else {
            // Valid access - update UI accordingly
            this.updateAuthUI();
        }
    }

    setupAuthStateListener() {
        this.supabase.auth.onAuthStateChange((event, session) => {
            console.log('🔐 AuthGate: Auth state changed:', event, !!session?.user);
            
            this.currentUser = session?.user || null;
            
            // Re-enforce auth rules on state change
            this.enforceAuthRules();
        });
    }

    redirectToLogin() {
        // Store the intended destination
        sessionStorage.setItem('authGate_redirectAfterLogin', window.location.href);
        
        // Show brief notification
        this.showAuthNotification('Please sign in to access Te Kete Ako resources', 'info');
        
        // Redirect to login after a brief delay
        setTimeout(() => {
            window.location.href = '/login.html';
        }, 1000);
    }

    redirectToMainSite() {
        // Check if there's a stored redirect URL
        const redirectUrl = sessionStorage.getItem('authGate_redirectAfterLogin');
        
        if (redirectUrl && redirectUrl !== window.location.href) {
            sessionStorage.removeItem('authGate_redirectAfterLogin');
            window.location.href = redirectUrl;
        } else {
            window.location.href = '/index.html';
        }
    }

    handleAuthFailure() {
        if (!this.isPublicPage) {
            console.log('🚨 AuthGate: Auth system failure, redirecting to public landing...');
            this.showAuthNotification('Authentication system temporarily unavailable', 'error');
            
            setTimeout(() => {
                window.location.href = '/public-landing.html';
            }, 2000);
        }
    }

    updateAuthUI() {
        // Update navigation and UI elements based on auth state
        if (this.currentUser) {
            this.showAuthenticatedUI();
        } else {
            this.showUnauthenticatedUI();
        }
    }

    showAuthenticatedUI() {
        // Show/hide elements for authenticated users
        const authElements = document.querySelectorAll('[data-auth="required"]');
        authElements.forEach(el => el.style.display = 'block');
        
        const noAuthElements = document.querySelectorAll('[data-auth="hidden"]');
        noAuthElements.forEach(el => el.style.display = 'none');
        
        // Show My Kete link
        const myKeteLink = document.querySelector('.my-kete-link');
        if (myKeteLink) {
            myKeteLink.style.display = 'block';
        }
        
        // Update auth navigation
        this.updateAuthNavigation(true);
    }

    showUnauthenticatedUI() {
        // Show/hide elements for unauthenticated users
        const authElements = document.querySelectorAll('[data-auth="required"]');
        authElements.forEach(el => el.style.display = 'none');
        
        const noAuthElements = document.querySelectorAll('[data-auth="hidden"]');
        noAuthElements.forEach(el => el.style.display = 'block');
        
        // Hide My Kete link
        const myKeteLink = document.querySelector('.my-kete-link');
        if (myKeteLink) {
            myKeteLink.style.display = 'none';
        }
        
        // Update auth navigation
        this.updateAuthNavigation(false);
    }

    updateAuthNavigation(isLoggedIn) {
        const authNavItems = document.querySelectorAll('.auth-nav');
        
        if (isLoggedIn && this.currentUser) {
            // Update navigation for logged-in users
            if (authNavItems[0]) {
                authNavItems[0].innerHTML = `
                    <div class="user-menu" style="position: relative;">
                        <button class="user-menu-toggle" style="
                            background: none; 
                            border: none; 
                            color: inherit; 
                            font: inherit; 
                            cursor: pointer;
                            display: flex;
                            align-items: center;
                            gap: 0.5rem;
                        ">
                            <span class="nav-icon">👤</span>
                            <span class="nav-text-en">${this.getUserDisplayName()}</span>
                            <span style="font-size: 0.8em;">▼</span>
                        </button>
                        <div class="user-dropdown" style="
                            display: none;
                            position: absolute;
                            top: 100%;
                            right: 0;
                            background: white;
                            border: 1px solid #ddd;
                            border-radius: 8px;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                            min-width: 180px;
                            z-index: 1000;
                            margin-top: 0.5rem;
                        ">
                            <div style="padding: 1rem; border-bottom: 1px solid #eee;">
                                <div style="font-weight: bold; color: var(--color-primary);">${this.getUserDisplayName()}</div>
                                <div style="font-size: 0.85em; color: #666;">${this.currentUser.email}</div>
                            </div>
                            <a href="/my-kete.html" style="
                                display: block;
                                padding: 0.75rem 1rem;
                                color: var(--color-text);
                                text-decoration: none;
                                border-bottom: 1px solid #eee;
                            ">
                                🧺 My Kete
                            </a>
                            <button class="auth-gate-logout-btn" style="
                                width: 100%;
                                text-align: left;
                                padding: 0.75rem 1rem;
                                background: none;
                                border: none;
                                color: #dc3545;
                                cursor: pointer;
                                font: inherit;
                            ">
                                🚪 Sign Out
                            </button>
                        </div>
                    </div>
                `;
            }

            // Hide register button
            if (authNavItems[1]) {
                authNavItems[1].style.display = 'none';
            }
        } else {
            // Show login/register for unauthenticated users
            if (authNavItems[0]) {
                authNavItems[0].innerHTML = `
                    <a href="/login.html" class="login-btn">
                        <span class="nav-icon">🔐</span>
                        <span class="nav-text-en">Login</span>
                        <span class="nav-text-mi" lang="mi">Takiuru</span>
                    </a>
                `;
            }

            if (authNavItems[1]) {
                authNavItems[1].innerHTML = `
                    <a href="/register-simple.html" class="register-btn">
                        <span class="nav-icon">📝</span>
                        <span class="nav-text-en">Register</span>
                        <span class="nav-text-mi" lang="mi">Rēhita</span>
                    </a>
                `;
                authNavItems[1].style.display = 'block';
            }
        }

        // Set up event listeners
        this.setupUIEventListeners();
    }

    setupUIEventListeners() {
        // User menu toggle
        const menuToggle = document.querySelector('.user-menu-toggle');
        if (menuToggle) {
            menuToggle.addEventListener('click', (e) => {
                e.preventDefault();
                const dropdown = menuToggle.nextElementSibling;
                dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
            });
        }

        // Logout button
        const logoutBtn = document.querySelector('.auth-gate-logout-btn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', async (e) => {
                e.preventDefault();
                await this.logout();
            });
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.user-menu')) {
                const dropdowns = document.querySelectorAll('.user-dropdown');
                dropdowns.forEach(dropdown => {
                    dropdown.style.display = 'none';
                });
            }
        });
    }

    async logout() {
        try {
            const { error } = await this.supabase.auth.signOut();
            if (error) throw error;
            
            this.showAuthNotification('Successfully signed out', 'success');
            
            // Clear stored redirect URL
            sessionStorage.removeItem('authGate_redirectAfterLogin');
            
            // Redirect to home page
            setTimeout(() => {
                window.location.href = '/index.html';
            }, 1000);
            
        } catch (error) {
            console.error('🚨 AuthGate: Logout failed:', error);
            this.showAuthNotification('Error signing out: ' + error.message, 'error');
        }
    }

    getUserDisplayName() {
        if (!this.currentUser) return 'User';
        
        // Try user metadata first
        if (this.currentUser.user_metadata?.full_name) {
            return this.currentUser.user_metadata.full_name;
        }
        
        // Fallback to email prefix
        if (this.currentUser.email) {
            return this.currentUser.email.split('@')[0];
        }
        
        return 'User';
    }

    showAuthNotification(message, type = 'info') {
        // Remove any existing notifications
        const existingNotification = document.querySelector('.auth-gate-notification');
        if (existingNotification) {
            existingNotification.remove();
        }

        // Create notification element
        const notification = document.createElement('div');
        notification.className = `auth-gate-notification auth-gate-notification-${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'error' ? '#f56565' : type === 'success' ? '#48bb78' : '#4299e1'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 10000;
            font-weight: 500;
            max-width: 300px;
            animation: slideInRight 0.3s ease-out;
        `;

        notification.innerHTML = `
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span>${type === 'error' ? '❌' : type === 'success' ? '✅' : 'ℹ️'}</span>
                <span>${message}</span>
                <button onclick="this.parentElement.parentElement.remove()" 
                        style="background: none; border: none; color: white; font-size: 1.2rem; cursor: pointer; margin-left: auto;">
                    ×
                </button>
            </div>
        `;

        document.body.appendChild(notification);

        // Auto-remove after 4 seconds
        setTimeout(() => {
            if (notification.parentElement) {
                notification.style.animation = 'slideOutRight 0.3s ease-in';
                setTimeout(() => notification.remove(), 300);
            }
        }, 4000);
    }

    // Public API methods
    isLoggedIn() {
        return !!this.currentUser;
    }

    getCurrentUser() {
        return this.currentUser;
    }

    requireAuth() {
        if (!this.isLoggedIn()) {
            this.redirectToLogin();
            return false;
        }
        return true;
    }
}

// CSS for animations
const authGateStyle = document.createElement('style');
authGateStyle.textContent = `
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    .user-dropdown a:hover,
    .user-dropdown button:hover {
        background-color: #f8f9fa;
    }
`;
document.head.appendChild(authGateStyle);

// Initialize the auth gate
window.authGate = new AuthGate();

// Export for use by other scripts
window.AuthGate = AuthGate;

console.log('🔐 Site-wide Authentication Gate loaded successfully');