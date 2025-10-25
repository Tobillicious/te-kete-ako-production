/**
 * PROFESSIONAL SIDEBAR AUTO-LOADER
 * Automatically loads professional-sidebar-cultural.html on all authenticated pages
 * Created: Oct 26, 2025
 * Status: Production-ready deployment system
 */

(function() {
    'use strict';
    
    // Check if sidebar should load (authenticated pages only)
    function shouldLoadSidebar() {
        // Check for Supabase session
        const hasSession = localStorage.getItem('supabase.auth.token');
        
        // Don't load on login/register pages
        const isAuthPage = window.location.pathname.includes('/login') || 
                          window.location.pathname.includes('/register');
        
        return hasSession && !isAuthPage;
    }
    
    // Load sidebar component
    async function loadSidebar() {
        try {
            // Fetch sidebar template
            const response = await fetch('/components/professional-sidebar-cultural.html');
            if (!response.ok) {
                console.log('Sidebar template not available');
                return;
            }
            
            const html = await response.text();
            
            // Create temporary div to parse HTML
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = html;
            
            // Extract template content
            const template = tempDiv.querySelector('#professional-sidebar-template');
            if (!template) {
                console.log('Sidebar template element not found');
                return;
            }
            
            // Clone and inject sidebar
            const sidebar = template.content.cloneNode(true);
            document.body.insertBefore(sidebar, document.body.firstChild);
            
            // Add body class for styling
            document.body.classList.add('has-sidebar');
            
            // Load user profile
            await loadUserProfile();
            
            // Initialize interactions
            initializeSidebarInteractions();
            
            console.log('✅ Professional sidebar loaded!');
            
            // Track with PostHog
            if (window.posthog) {
                posthog.capture('sidebar_loaded', {
                    page: window.location.pathname
                });
            }
            
        } catch (error) {
            console.log('Sidebar load error:', error.message);
        }
    }
    
    // Load user profile from Supabase
    async function loadUserProfile() {
        try {
            // Get Supabase client
            if (!window.supabase) {
                console.log('Supabase not available yet');
                return;
            }
            
            // Get current user
            const { data: { user }, error } = await window.supabase.auth.getUser();
            
            if (error || !user) {
                console.log('No authenticated user');
                return;
            }
            
            // Get profile from profiles table
            const { data: profile, error: profileError } = await window.supabase
                .from('profiles')
                .select('display_name, role, school_name')
                .eq('user_id', user.id)
                .single();
            
            if (profile) {
                // Update sidebar with user data
                const nameEl = document.querySelector('.profile-name');
                const roleEl = document.querySelector('.profile-role');
                const schoolEl = document.querySelector('.profile-school');
                
                if (nameEl) nameEl.textContent = profile.display_name || user.email.split('@')[0];
                if (roleEl) roleEl.textContent = profile.role || 'Teacher';
                if (schoolEl) schoolEl.textContent = profile.school_name || 'Te Kete Ako';
            }
            
        } catch (error) {
            console.log('Profile load error:', error.message);
        }
    }
    
    // Initialize sidebar interactions
    function initializeSidebarInteractions() {
        // Logout button
        const logoutBtn = document.querySelector('.sidebar-logout');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', async () => {
                if (window.supabase) {
                    await window.supabase.auth.signOut();
                    window.location.href = '/login.html';
                }
            });
        }
        
        // Track sidebar link clicks
        const sidebarLinks = document.querySelectorAll('.sidebar-link, .sidebar-link-sub');
        sidebarLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                if (window.posthog) {
                    posthog.capture('sidebar_navigation', {
                        link_text: e.target.textContent.trim(),
                        link_href: e.target.getAttribute('href'),
                        section: e.target.closest('.sidebar-section')?.className || 'unknown'
                    });
                }
            });
        });
        
        // Highlight current page
        const currentPath = window.location.pathname;
        sidebarLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
                link.style.background = 'rgba(255, 255, 255, 0.2)';
                link.style.borderLeftColor = '#ffd700';
            }
        });
    }
    
    // Initialize on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            if (shouldLoadSidebar()) {
                loadSidebar();
            }
        });
    } else {
        if (shouldLoadSidebar()) {
            loadSidebar();
        }
    }
    
})();

