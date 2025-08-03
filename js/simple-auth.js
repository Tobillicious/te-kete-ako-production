// simple-auth.js
// A basic working authentication system for Te Kete Ako

class SimpleAuth {
    constructor() {
        this.currentUser = null;
        this.supabase = null;
        this.init();
    }

    async init() {
        try {
            // Wait for Supabase client to be available
            await this.waitForSupabase();
            
            // Check current session
            const { data: { session } } = await this.supabase.auth.getSession();
            if (session?.user) {
                this.currentUser = session.user;
                this.updateUI();
            }
            
            // Listen for auth state changes
            this.supabase.auth.onAuthStateChange((event, session) => {
                this.currentUser = session?.user || null;
                this.updateUI();
            });
            
            console.log('Unified Supabase Auth initialized');
        } catch (error) {
            console.error('Auth initialization failed:', error);
        }
    }

    async login(email, password) {
        try {
            const { data, error } = await this.supabase.auth.signInWithPassword({
                email,
                password
            });
            
            if (error) {
                return { success: false, error: error.message };
            }
            
            return { success: true, user: data.user };
        } catch (error) {
            return { success: false, error: 'Login failed. Please try again.' };
        }
    }

    async register(email, password, name, role = 'student') {
        try {
            const { data, error } = await this.supabase.auth.signUp({
                email,
                password,
                options: {
                    data: {
                        full_name: name,
                        display_name: name,
                        role: role, // 'student' or 'teacher'
                        account_type: role
                    }
                }
            });
            
            if (error) {
                return { success: false, error: error.message };
            }
            
            return { success: true, user: data.user };
        } catch (error) {
            return { success: false, error: 'Registration failed. Please try again.' };
        }
    }

    async logout() {
        try {
            const { error } = await this.supabase.auth.signOut();
            if (error) {
                return { success: false, error: error.message };
            }
            return { success: true };
        } catch (error) {
            return { success: false, error: 'Logout failed. Please try again.' };
        }
    }

    isLoggedIn() {
        return !!this.currentUser;
    }

    getCurrentUser() {
        return this.currentUser;
    }

    updateUI() {
        this.updateNavigation();
        this.triggerAuthStateChange();
    }

    updateNavigation() {
        const authNavItems = document.querySelectorAll('.auth-nav');
        const myKeteLink = document.querySelector('.my-kete-link');
        
        if (this.currentUser) {
            // User is logged in - update first two auth nav items
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
                                <div style="font-size: 0.85em; color: #666;">${this.currentUser?.email}</div>
                            </div>
                            <a href="my-kete.html" style="
                                display: block;
                                padding: 0.75rem 1rem;
                                color: var(--color-text);
                                text-decoration: none;
                                border-bottom: 1px solid #eee;
                            ">
                                🧺 My Kete
                            </a>
                            <button class="logout-btn" style="
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

            // Show My Kete link
            if (myKeteLink) {
                myKeteLink.style.display = 'block';
            }
        } else {
            // User is not logged in - restore default navigation
            if (authNavItems[0]) {
                authNavItems[0].innerHTML = `
                    <a href="login.html" class="login-btn">
                        <span class="nav-icon">🔐</span>
                        <span class="nav-text-en">Login</span>
                        <span class="nav-text-mi" lang="mi">Takiuru</span>
                    </a>
                `;
            }

            if (authNavItems[1]) {
                authNavItems[1].innerHTML = `
                    <a href="register.html" class="register-btn">
                        <span class="nav-icon">📝</span>
                        <span class="nav-text-en">Register</span>
                        <span class="nav-text-mi" lang="mi">Rēhita</span>
                    </a>
                `;
                authNavItems[1].style.display = 'block';
            }

            // Hide My Kete link
            if (myKeteLink) {
                myKeteLink.style.display = 'none';
            }
        }

        // Set up event listeners for dynamic elements
        this.setupEventListeners();
    }

    setupEventListeners() {
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
        const logoutBtn = document.querySelector('.logout-btn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', async (e) => {
                e.preventDefault();
                const result = await this.logout();
                if (result.success) {
                    this.showNotification('You have been signed out', 'info');
                    // Redirect to homepage if on protected page
                    if (window.location.pathname.includes('my-kete')) {
                        window.location.href = 'index.html';
                    }
                } else {
                    this.showNotification(result.error, 'error');
                }
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

    triggerAuthStateChange() {
        // Dispatch custom event for other parts of the app to listen to
        const event = new CustomEvent('authStateChanged', {
            detail: { user: this.currentUser, isLoggedIn: this.isLoggedIn() }
        });
        document.dispatchEvent(event);
    }

    showNotification(message, type = 'info') {
        // Remove any existing notifications
        const existingNotification = document.querySelector('.auth-notification');
        if (existingNotification) {
            existingNotification.remove();
        }

        // Create notification element
        const notification = document.createElement('div');
        notification.className = `auth-notification auth-notification-${type}`;
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
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
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

    // Get user display name helper
    getUserDisplayName() {
        if (!this.currentUser) return 'User';
        
        // Try user metadata first (from registration)
        if (this.currentUser.user_metadata?.full_name) {
            return this.currentUser.user_metadata.full_name;
        }
        
        // Fallback to email prefix
        if (this.currentUser.email) {
            return this.currentUser.email.split('@')[0];
        }
        
        return 'User';
    }

    // Wait for Supabase to be available
    async waitForSupabase() {
        // First check if getSupabaseClient exists (from shared-components.js)
        if (typeof window.getSupabaseClient === 'function') {
            this.supabase = window.getSupabaseClient();
            return;
        }
        
        // If not, wait for shared-components.js to load
        return new Promise((resolve, reject) => {
            const checkInterval = setInterval(() => {
                if (typeof window.getSupabaseClient === 'function') {
                    clearInterval(checkInterval);
                    this.supabase = window.getSupabaseClient();
                    resolve();
                }
            }, 100);
            
            // Timeout after 10 seconds
            setTimeout(() => {
                clearInterval(checkInterval);
                
                // Try direct Supabase if available
                if (typeof window.supabase !== 'undefined' && window.supabase.createClient) {
                    const url = 'https://nlgldaqtubrlcqddppbq.supabase.co';
                    const key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
                    this.supabase = window.supabase.createClient(url, key);
                    resolve();
                } else {
                    reject(new Error('Supabase client not available'));
                }
            }, 10000);
        });
    }
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
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
document.head.appendChild(style);

// Initialize simple auth
window.simpleAuth = new SimpleAuth();

console.log('Unified Supabase Auth system loaded');
console.log('Authentication ready - fully integrated with Supabase');