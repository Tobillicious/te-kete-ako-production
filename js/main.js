/**
 * Te Kete Ako - Main JavaScript
 * Core functionality and initialization
 */

// Initialize Te Kete Ako when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('🌟 Te Kete Ako initialized - World\'s first culturally-grounded AI educational platform');
    
    // Initialize components
    initializeNavigation();
    initializeAuth();
    initializePWA();
    initializeAnalytics();
});

/**
 * Navigation enhancements
 */
function initializeNavigation() {
    // Highlight current page in navigation
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.main-nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.style.color = '#2C5F41';
            link.style.fontWeight = '600';
        }
    });

    // Mobile navigation toggle if needed
    const navToggle = document.querySelector('.nav-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    if (navToggle && mainNav) {
        navToggle.addEventListener('click', () => {
            mainNav.classList.toggle('nav-open');
        });
    }
}

/**
 * Authentication helpers
 */
function initializeAuth() {
    // Check if user is logged in
    const token = localStorage.getItem('teKeteAko_token');
    const user = localStorage.getItem('teKeteAko_user');
    
    if (token && user) {
        // User is logged in
        updateAuthState(JSON.parse(user));
    }
}

function updateAuthState(user) {
    // Update navigation for logged-in users
    const authNavItems = document.querySelectorAll('.auth-nav');
    
    authNavItems.forEach(item => {
        if (user) {
            // Replace login/register with user menu
            item.innerHTML = `
                <a href="${user.role === 'student' ? 'student-dashboard.html' : 'teacher-dashboard.html'}">
                    <span class="nav-icon">👤</span>
                    <span class="nav-text-en">${user.display_name || user.email}</span>
                </a>
            `;
        }
    });
}

/**
 * PWA initialization
 */
function initializePWA() {
    // Register service worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('📱 PWA: Service Worker registered successfully');
            })
            .catch(error => {
                console.log('❌ PWA: Service Worker registration failed:', error);
            });
    }
}

/**
 * Analytics initialization
 */
function initializeAnalytics() {
    // Track page views and user interactions
    const user = localStorage.getItem('teKeteAko_user');
    
    if (user) {
        // Track authenticated user analytics
        trackPageView(JSON.parse(user));
    }
    
    // Track general site usage
    trackSiteInteractions();
}

function trackPageView(user = null) {
    const pageData = {
        page: window.location.pathname,
        timestamp: new Date().toISOString(),
        user_id: user ? JSON.parse(localStorage.getItem('teKeteAko_user')).id : null,
        device_type: /Mobile|Android|iPhone/i.test(navigator.userAgent) ? 'mobile' : 'desktop'
    };
    
    // Send to analytics endpoint (if implemented)
    console.log('📊 Page view tracked:', pageData);
}

function trackSiteInteractions() {
    // Track clicks on key elements
    document.addEventListener('click', (e) => {
        const target = e.target.closest('a, button');
        
        if (target) {
            const interactionData = {
                element: target.tagName.toLowerCase(),
                text: target.textContent?.trim(),
                href: target.href || null,
                timestamp: new Date().toISOString()
            };
            
            console.log('🖱️ Interaction tracked:', interactionData);
        }
    });
}

/**
 * Utility functions
 */

// Show loading state
function showLoading(element) {
    if (element) {
        element.disabled = true;
        element.innerHTML = '<div class="spinner"></div> Loading...';
    }
}

// Hide loading state
function hideLoading(element, originalText) {
    if (element) {
        element.disabled = false;
        element.innerHTML = originalText;
    }
}

// Show message to user
function showMessage(message, type = 'info') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${type}`;
    messageDiv.textContent = message;
    
    document.body.appendChild(messageDiv);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.parentNode.removeChild(messageDiv);
        }
    }, 5000);
}

// Format date for display
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-NZ', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Check if user has specific role
function hasRole(requiredRole) {
    const user = localStorage.getItem('teKeteAko_user');
    if (!user) return false;
    
    const userData = JSON.parse(user);
    return userData.role === requiredRole;
}

// Redirect based on user role
function redirectToDashboard() {
    const user = localStorage.getItem('teKeteAko_user');
    if (!user) {
        window.location.href = 'login.html';
        return;
    }
    
    const userData = JSON.parse(user);
    if (userData.role === 'student') {
        window.location.href = 'student-dashboard.html';
    } else if (userData.role === 'teacher') {
        window.location.href = 'teacher-dashboard.html';
    } else {
        window.location.href = 'index.html';
    }
}

// Logout function
function logout() {
    localStorage.removeItem('teKeteAko_token');
    localStorage.removeItem('teKeteAko_refreshToken');
    localStorage.removeItem('teKeteAko_user');
    
    showMessage('Successfully logged out', 'success');
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1000);
}

// Global error handler
window.addEventListener('error', (e) => {
    console.error('🚨 JavaScript error:', e.error);
    
    // Don't show errors to users in production
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        showMessage(`Error: ${e.error.message}`, 'error');
    }
});

// Export functions for other scripts
window.TeKeteAko = {
    showLoading,
    hideLoading,
    showMessage,
    formatDate,
    hasRole,
    redirectToDashboard,
    logout,
    trackPageView
};

console.log('🚀 Te Kete Ako main.js loaded successfully');