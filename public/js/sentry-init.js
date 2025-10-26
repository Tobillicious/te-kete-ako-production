/**
 * SENTRY ERROR MONITORING - Te Kete Ako
 * Professional error tracking for proactive quality
 * Created: October 26, 2025
 */

(function() {
    'use strict';

    // Only initialize if Sentry CDN is loaded
    if (typeof Sentry !== 'undefined') {
        Sentry.init({
            dsn: 'https://YOUR_SENTRY_DSN@sentry.io/YOUR_PROJECT_ID', // Replace with actual DSN from Sentry.io
            environment: window.location.hostname.includes('localhost') ? 'development' : 'production',
            
            // Performance Monitoring
            tracesSampleRate: 0.1, // Sample 10% of transactions for performance
            
            // Release tracking
            release: 'te-kete-ako@1.0.0',
            
            // User context
            beforeSend(event, hint) {
                // Add user context from Supabase if available
                if (window.supabaseClient) {
                    window.supabaseClient.auth.getUser().then(({ data: { user } }) => {
                        if (user) {
                            event.user = {
                                id: user.id,
                                email: user.email,
                                school: user.user_metadata?.school
                            };
                        }
                    });
                }

                // Filter out known non-critical errors
                if (event.exception && event.exception.values) {
                    const error = event.exception.values[0];
                    const errorMessage = error.value || '';

                    // Ignore browser quirks
                    if (errorMessage.includes('ResizeObserver loop')) return null;
                    if (errorMessage.includes('Non-Error promise rejection')) return null;
                    
                    // Ignore CDN loading issues (report but don't alert)
                    if (errorMessage.includes('cdn.jsdelivr.net')) {
                        event.level = 'warning';
                    }
                }

                return event;
            },

            // Breadcrumbs for debugging context
            integrations: [
                new Sentry.BrowserTracing({
                    tracingOrigins: ['localhost', 'tekete.netlify.app', /^\//],
                }),
            ],

            // Ignore certain URLs
            ignoreErrors: [
                'ResizeObserver loop',
                'Non-Error promise rejection',
                'NetworkError',
                'cancelled' // User cancelled requests
            ],

            // Tag errors by page type
            initialScope: {
                tags: {
                    page_type: detectPageType(),
                    has_sidebar: document.getElementById('sidebar-container') ? 'yes' : 'no',
                    authenticated: localStorage.getItem('supabase.auth.token') ? 'yes' : 'no'
                }
            }
        });

        console.log('✅ Sentry initialized - Professional error tracking active!');

        // Track page view for context
        if (window.posthog) {
            window.posthog.capture('sentry_initialized', {
                page_type: detectPageType()
            });
        }

    } else {
        console.warn('⚠️ Sentry CDN not loaded - error tracking disabled');
    }

    function detectPageType() {
        const path = window.location.pathname;
        if (path.includes('lesson')) return 'lesson';
        if (path.includes('unit')) return 'unit';
        if (path.includes('handout')) return 'handout';
        if (path.includes('hub')) return 'hub';
        if (path.includes('dashboard')) return 'dashboard';
        if (path.includes('account') || path.includes('settings')) return 'account';
        if (path.includes('pricing') || path.includes('subscription')) return 'pricing';
        if (path === '/' || path.includes('index')) return 'homepage';
        return 'other';
    }

    // Global error handler
    window.addEventListener('error', function(event) {
        console.error('Global error caught:', event.error);
        
        // Show user-friendly message for critical errors
        if (event.error && window.showToast) {
            window.showToast('Something went wrong. Our team has been notified.', 'error');
        }
    });

    // Unhandled promise rejection handler
    window.addEventListener('unhandledrejection', function(event) {
        console.error('Unhandled promise rejection:', event.reason);
        
        // Report to Sentry
        if (typeof Sentry !== 'undefined') {
            Sentry.captureException(event.reason);
        }
    });

})();

/**
 * SETUP INSTRUCTIONS:
 * 
 * 1. Create Sentry account at https://sentry.io (FREE tier!)
 * 2. Create project: "Te Kete Ako"
 * 3. Copy your DSN
 * 4. Replace 'YOUR_SENTRY_DSN@sentry.io/YOUR_PROJECT_ID' above
 * 5. Add Sentry CDN to pages:
 *    <script src="https://browser.sentry-cdn.com/7.x/bundle.min.js" crossorigin="anonymous"></script>
 * 6. Include this file after Sentry CDN
 * 7. Done! Errors automatically tracked!
 * 
 * FREE TIER INCLUDES:
 * - 5,000 errors/month
 * - 10,000 performance transactions/month
 * - Unlimited team members
 * - 30-day event retention
 * 
 * COST: $0/month! 🎊
 */
