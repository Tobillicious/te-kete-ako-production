// Sentry Error Tracking Integration
// Created: October 26, 2025
// Purpose: Track JavaScript errors across the platform

// Sentry Configuration
const SENTRY_CONFIG = {
  dsn: "https://2cd90e8d1c5811d6f11bd845b4c6e535@o4509672250933251.ingest.de.sentry.io/4509672258797648",
  environment: window.location.hostname === 'localhost' ? 'development' : 'production',
  release: 'te-kete-ako@1.0.0',
  
  // Performance Monitoring
  tracesSampleRate: 0.1, // 10% of transactions
  
  // Session Replay
  replaysSessionSampleRate: 0.1, // 10% of sessions
  replaysOnErrorSampleRate: 1.0, // 100% of sessions with errors
  
  // Privacy
  sendDefaultPii: true, // Track user info for better debugging
  
  // Integrations
  integrations: [
    // Browser Tracing (automatic)
    // Replay (automatic)
  ],
  
  // Before Send Hook (filter sensitive data)
  beforeSend(event, hint) {
    // Don't send errors from browser extensions
    if (event.exception) {
      const values = event.exception.values || [];
      for (const value of values) {
        if (value.stacktrace) {
          const frames = value.stacktrace.frames || [];
          for (const frame of frames) {
            if (frame.filename && (
              frame.filename.includes('extension://') ||
              frame.filename.includes('chrome-extension://') ||
              frame.filename.includes('moz-extension://')
            )) {
              return null; // Don't send
            }
          }
        }
      }
    }
    
    return event;
  }
};

// Initialize Sentry with CDN
(function() {
  // Load Sentry from CDN
  const script = document.createElement('script');
  script.src = 'https://browser.sentry-cdn.com/7.100.0/bundle.tracing.replay.min.js';
  script.integrity = 'sha384-xxx'; // Add integrity hash in production
  script.crossOrigin = 'anonymous';
  script.onload = function() {
    if (window.Sentry) {
      window.Sentry.init(SENTRY_CONFIG);
      
      console.log('✅ Sentry error tracking initialized');
      
      // Track page view
      window.Sentry.addBreadcrumb({
        category: 'navigation',
        message: 'Page loaded: ' + window.location.pathname,
        level: 'info'
      });
      
      // Set user context if logged in
      if (window.TeKeteAuth && window.TeKeteAuth.currentUser) {
        window.Sentry.setUser({
          id: window.TeKeteAuth.currentUser.id,
          email: window.TeKeteAuth.currentUser.email,
          role: window.TeKeteAuth.getRole()
        });
      }
    }
  };
  
  document.head.appendChild(script);
})();

// Global error handler (backup)
window.addEventListener('error', function(event) {
  console.error('JavaScript Error:', event.error);
  
  // Log to our own error tracking table as well
  if (window.supabase && window.supabaseClient) {
    logErrorToDatabase(event.error, event.filename, event.lineno, event.colno);
  }
});

// Unhandled promise rejections
window.addEventListener('unhandledrejection', function(event) {
  console.error('Unhandled Promise Rejection:', event.reason);
  
  if (window.Sentry) {
    window.Sentry.captureException(event.reason);
  }
});

// Log to our database for redundancy
async function logErrorToDatabase(error, filename, lineno, colno) {
  try {
    if (!window.supabaseClient) return;
    
    const { data: { user } } = await window.supabaseClient.auth.getUser();
    
    await window.supabaseClient
      .from('error_logs')
      .insert([{
        error_type: error?.name || 'Error',
        error_message: error?.message || String(error),
        error_stack: error?.stack || '',
        page_url: window.location.href,
        page_title: document.title,
        filename: filename,
        line_number: lineno,
        column_number: colno,
        user_agent: navigator.userAgent,
        user_id: user?.id || null,
        session_errors: 1
      }]);
  } catch (dbError) {
    console.error('Failed to log error to database:', dbError);
  }
}

// Helper function to manually track errors
window.trackError = function(errorMessage, context = {}) {
  if (window.Sentry) {
    window.Sentry.captureMessage(errorMessage, {
      level: 'error',
      extra: context
    });
  }
  
  console.error('Tracked Error:', errorMessage, context);
};

// Helper function to track events
window.trackEvent = function(eventName, properties = {}) {
  if (window.Sentry) {
    window.Sentry.addBreadcrumb({
      category: 'user-action',
      message: eventName,
      level: 'info',
      data: properties
    });
  }
  
  // Also send to PostHog if available
  if (window.posthog) {
    window.posthog.capture(eventName, properties);
  }
};

console.log('🔍 Sentry error tracking script loaded');

