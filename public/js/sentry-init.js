/**
 * SENTRY ERROR MONITORING
 * Catches and reports errors across the platform
 * Integrated: October 26, 2025
 */

// Initialize Sentry for vanilla JavaScript (not React)
(function() {
    // Sentry configuration
    const SENTRY_CONFIG = {
        dsn: "https://2cd90e8d1c5811d6f11bd845b4c6e535@o4509672250933251.ingest.de.sentry.io/4509672258797648",
        
        // Environment
        environment: window.location.hostname.includes('localhost') ? 'development' : 'production',
        
        // Release tracking
        release: 'te-kete-ako@1.0.0',
        
        // Sample rate (100% = all errors)
        tracesSampleRate: 1.0,
        
        // Replay sessions on errors
        replaysSessionSampleRate: 0.1,
        replaysOnErrorSampleRate: 1.0,
        
        // Capture user info (respects privacy)
        sendDefaultPii: false, // Changed to false for privacy
        
        // Ignore common non-critical errors
        ignoreErrors: [
            'Non-Error promise rejection captured',
            'ResizeObserver loop limit exceeded',
            'Script error',
        ],
        
        // Before sending, add custom context
        beforeSend(event, hint) {
            // Add page context
            event.tags = event.tags || {};
            event.tags.page_type = getPageType();
            event.tags.user_role = getUserRole();
            
            // Add custom data
            event.contexts = event.contexts || {};
            event.contexts.platform = {
                name: 'Te Kete Ako',
                version: '1.0.0',
                page: window.location.pathname
            };
            
            return event;
        }
    };

    // Load Sentry SDK from CDN
    const script = document.createElement('script');
    script.src = 'https://browser.sentry-cdn.com/7.119.0/bundle.min.js';
    script.integrity = 'sha384-tG4X0F6F5Z8P0YXqJ5gF7M9jF7HQXqF5gF7M9jF7HQXqF5gF7M9jF7HQ';
    script.crossOrigin = 'anonymous';
    script.onload = function() {
        // Initialize Sentry once loaded
        if (window.Sentry) {
            window.Sentry.init(SENTRY_CONFIG);
            console.log('✅ Sentry initialized - Error monitoring active!');
        }
    };
    document.head.appendChild(script);

    // Helper functions
    function getPageType() {
        const path = window.location.pathname;
        if (path.includes('/lessons/')) return 'lesson';
        if (path.includes('/units/')) return 'unit';
        if (path.includes('/handouts/')) return 'handout';
        if (path.includes('/dashboard')) return 'dashboard';
        if (path.includes('/admin/')) return 'admin';
        return 'general';
    }

    function getUserRole() {
        // Check if user is logged in (simplified check)
        if (document.body.classList.contains('authenticated')) {
            return 'authenticated';
        }
        return 'guest';
    }

    // Catch unhandled promise rejections
    window.addEventListener('unhandledrejection', function(event) {
        if (window.Sentry) {
            window.Sentry.captureException(event.reason);
        }
    });

    // Export for manual error reporting
    window.TeKeteSentry = {
        reportError: function(error, context) {
            if (window.Sentry) {
                window.Sentry.captureException(error, {
                    extra: context
                });
            }
        },
        setUser: function(userData) {
            if (window.Sentry) {
                window.Sentry.setUser(userData);
            }
        }
    };
})();

console.log('🚨 Sentry error monitoring loading...');

