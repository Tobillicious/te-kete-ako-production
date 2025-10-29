// auth-ui.js
// Handles authentication state and UI updates across Te Kete Ako

/**
 * Authentication UI Manager
 * Updates navigation and page elements based on user login status
 */
class AuthUI {
    constructor() {
        this.currentUser = null;
        this.isInitialized = false;
        this.init();
    }

    async init() {
        try {
            // Wait for Supabase to be available
            if (typeof supabase === 'undefined') {
                setTimeout(() => this.init(), 100);
                return;
            }

            // Get current user session
            await this.updateAuthState();
            
            // Listen for auth state changes
            supabase.auth.onAuthStateChange((event, session) => {
                this.handleAuthStateChange(event, session);
            });

            this.isInitialized = true;
        } catch (error) {
            console.error('Error initializing Auth UI:', error);
        }
    }

    async updateAuthState() {
        try {
            const { data: { session }, error } = await supabase.auth.getSession();
            
            if (error) {
                console.error('Error getting session:', error);
                return;
            }

            this.currentUser = session?.user || null;
            this.updateUI();
        } catch (error) {
            console.error('Error updating auth state:', error);
        }
    }

    handleAuthStateChange(event, session) {
        this.currentUser = session?.user || null;
        this.updateUI();

        // Handle specific events
        switch (event) {
            case 'SIGNED_IN':
                this.showNotification('Welcome back! You are now signed in.', 'success');
                break;
            case 'SIGNED_OUT':
                this.showNotification('You have been signed out.', 'info');
                break;
            case 'TOKEN_REFRESHED':
                // Token refreshed silently
                break;
        }
    }

    updateUI() {
        this.updateNavigation();
        this.updatePageElements();
    }

    updateNavigation() {
        const loggedOutNav = document.querySelector('.auth-nav.auth-logged-out');
        const loggedInNav = document.querySelector('.auth-nav.auth-logged-in');
        
        if (this.currentUser) {
            // User is logged in
            // Hide login button
            if (loggedOutNav) {
                loggedOutNav.style.display = 'none';
            }
            
            // Hide the separate My Kete button (redundant - it's in the user dropdown)
            if (loggedInNav) {
                loggedInNav.style.display = 'none';
            }
            
            // Add user menu (if not already exists)
            if (!document.querySelector('.user-menu-nav')) {
                const nav = document.querySelector('.main-nav ul');
                if (nav) {
                    const userMenuItem = document.createElement('li');
                    userMenuItem.className = 'user-menu-nav';
                    userMenuItem.innerHTML = this.createUserMenuHTML();
                    nav.appendChild(userMenuItem);
                }
            }
        } else {
            // User is not logged in
            // Show login button
            if (loggedOutNav) {
                loggedOutNav.style.display = 'block';
            }
            
            // Hide My Kete button
            if (loggedInNav) {
                loggedInNav.style.display = 'none';
            }
            
            // Remove user menu
            const userMenuItem = document.querySelector('.user-menu-nav');
            if (userMenuItem) {
                userMenuItem.remove();
            }
        }
    }

    createUserMenuHTML() {
        const userEmail = this.currentUser.email;
        const userName = userEmail.split('@')[0]; // Use part before @ as display name
        
        // Match the exact structure of other nav items
        return `
            <a href="#">
                <span class="nav-icon">👤</span>
                <span class="nav-text-en">${userName}</span>
                <span class="nav-text-mi" lang="mi">Whakatere</span>
            </a>
            <div class="nav-dropdown user-dropdown">
                <div class="user-dropdown-header">
                    <div class="user-dropdown-name">${userName}</div>
                    <div class="user-dropdown-email">${userEmail}</div>
                </div>
                <a href="/my-kete.html"><span class="dropdown-mi">🧺 Tōku Kete</span><span class="dropdown-en">My Kete</span></a>
                <a href="/account-settings.html"><span class="dropdown-mi">⚙️ Ngā Tautuhinga</span><span class="dropdown-en">Account Settings</span></a>
                <a href="#" class="logout-btn"><span class="dropdown-mi">🚪 Puta</span><span class="dropdown-en">Sign Out</span></a>
            </div>
        `;
    }

    resetNavigationToDefault() {
        const authNavItems = document.querySelectorAll('.auth-nav');
        
        authNavItems.forEach((item, index) => {
            if (index === 0) {
                // First auth nav item -> Login
                item.innerHTML = `
                    <a href="login.html" class="login-btn">
                        <span class="nav-icon">🔐</span>
                        <span class="nav-text-en">Login</span>
                        <span class="nav-text-mi" lang="mi">Takiuru</span>
                    </a>
                `;
            } else if (index === 1) {
                // Second auth nav item -> Register
                item.innerHTML = `
                    <a href="register.html" class="register-btn">
                        <span class="nav-icon">📝</span>
                        <span class="nav-text-en">Register</span>
                        <span class="nav-text-mi" lang="mi">Rēhita</span>
                    </a>
                `;
            }
        });
    }

    updatePageElements() {
        // Update page-specific elements based on auth state
        const pageType = document.body.dataset.currentPage;
        
        switch (pageType) {
            case 'home':
                this.updateHomepageElements();
                break;
            case 'login':
            case 'register':
                // Redirect if already logged in
                if (this.currentUser) {
                    window.location.href = 'index.html';
                }
                break;
        }
    }

    updateHomepageElements() {
        // Add any homepage-specific auth updates here
        // e.g., showing personalized content, save buttons, etc.
    }

    async signOut() {
        try {
            const { error } = await supabase.auth.signOut();
            if (error) {
                throw error;
            }
            
            // Redirect to homepage after logout
            window.location.href = 'index.html';
        } catch (error) {
            console.error('Error signing out:', error);
            this.showNotification('Error signing out. Please try again.', 'error');
        }
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
        
        // Set type-specific class for styling
        const bgColor = type === 'error' ? '#f56565' : type === 'success' ? '#48bb78' : '#4299e1';
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${bgColor};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 10000;
            font-weight: 500;
            max-width: 300px;
            animation: slideInRight 0.3s ease-out;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        `;

        notification.innerHTML = `
            <span>${type === 'error' ? '❌' : type === 'success' ? '✅' : 'ℹ️'}</span>
            <span>${message}</span>
            <button onclick="this.parentElement.remove()" 
                    style="background: none; border: none; color: white; font-size: 1.2rem; cursor: pointer; margin-left: auto;">
                ×
            </button>
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

    // Public methods for other scripts to use
    async isAuthenticated() {
        if (!this.isInitialized) {
            await this.updateAuthState();
        }
        return !!this.currentUser;
    }

    getCurrentUser() {
        return this.currentUser;
    }
}

// Initialize Auth UI when DOM is loaded
let authUI;

document.addEventListener('DOMContentLoaded', () => {
    authUI = new AuthUI();
    
    // Set up event delegation for logout button
    document.addEventListener('click', (e) => {
        // Handle logout button click (including parent elements with dropdown-en/dropdown-mi)
        if (e.target.classList.contains('logout-btn') || e.target.closest('.logout-btn')) {
            e.preventDefault();
            authUI.signOut();
        }
    });
});

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .user-dropdown a:hover,
    .user-dropdown button:hover {
        background-color: #f8f9fa;
    }
`;
document.head.appendChild(style);

// Make authUI available globally
window.authUI = authUI;