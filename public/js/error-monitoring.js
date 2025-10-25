/**
 * 🚨 TE KETE AKO - AUTOMATIC ERROR MONITORING
 * Captures JavaScript errors and sends to PostHog + Supabase
 * 
 * Features:
 * - Automatic console error capture
 * - Unhandled promise rejection tracking
 * - Network error detection
 * - User context preservation
 * - GraphRAG-compatible logging
 */

class ErrorMonitoring {
    constructor() {
        this.errorCount = 0;
        this.maxErrorsPerSession = 50; // Prevent spam
        this.supabaseUrl = window.SUPABASE_URL || 'https://nlgldaqtubrlcqddppbq.supabase.co';
        this.supabaseKey = window.SUPABASE_ANON_KEY;
        
        this.init();
    }
    
    init() {
        // User feedback provided via UI
        
        // Capture JavaScript errors
        window.addEventListener('error', (event) => this.handleError(event));
        
        // Capture unhandled promise rejections
        window.addEventListener('unhandledrejection', (event) => this.handlePromiseRejection(event));
        
        // Capture console errors (optional - can be noisy)
        // this.interceptConsole();
    }
    
    async handleError(event) {
        if (this.errorCount >= this.maxErrorsPerSession) return;
        this.errorCount++;
        
        const errorData = {
            type: 'javascript_error',
            message: event.message,
            filename: event.filename,
            line_number: event.lineno,
            column_number: event.colno,
            stack: event.error?.stack || '',
            page_url: window.location.href,
            page_title: document.title,
            user_agent: navigator.userAgent,
            timestamp: new Date().toISOString(),
            session_errors: this.errorCount,
        };
        
        // Send to PostHog (if available)
        this.sendToPostHog(errorData);
        
        // Send to Supabase (if error_logs table exists)
        this.sendToSupabase(errorData);
        
        // Log to console for debugging
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
    }
    
    async handlePromiseRejection(event) {
        if (this.errorCount >= this.maxErrorsPerSession) return;
        this.errorCount++;
        
        const errorData = {
            type: 'unhandled_promise_rejection',
            message: String(event.reason),
            stack: event.reason?.stack || '',
            page_url: window.location.href,
            page_title: document.title,
            user_agent: navigator.userAgent,
            timestamp: new Date().toISOString(),
            session_errors: this.errorCount,
        };
        
        this.sendToPostHog(errorData);
        this.sendToSupabase(errorData);
        
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
    }
    
    sendToPostHog(errorData) {
        try {
            if (window.posthog && typeof window.posthog.capture === 'function') {
                window.posthog.capture('error_occurred', {
                    ...errorData,
                    $set: {
                        last_error_time: errorData.timestamp
                    }
                });
                // User feedback provided via UI
            }
        } catch (err) {
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
        }
    }
    
    async sendToSupabase(errorData) {
        // Only send to Supabase if we have credentials
        if (!this.supabaseKey || this.supabaseKey.includes('YOUR_KEY')) return;
        
        try {
            const response = await fetch(`${this.supabaseUrl}/rest/v1/error_logs`, {
                method: 'POST',
                headers: {
                    'apikey': this.supabaseKey,
                    'Authorization': `Bearer ${this.supabaseKey}`,
                    'Content-Type': 'application/json',
                    'Prefer': 'return=minimal', // Don't return data, faster
                },
                body: JSON.stringify({
                    error_type: errorData.type,
                    error_message: errorData.message,
                    error_stack: errorData.stack,
                    page_url: errorData.page_url,
                    page_title: errorData.page_title,
                    filename: errorData.filename,
                    line_number: errorData.line_number,
                    column_number: errorData.column_number,
                    user_agent: errorData.user_agent,
                    session_errors: errorData.session_errors,
                })
            });
            
            if (response.ok) {
                // User feedback provided via UI
            }
        } catch (err) {
            // Silently fail - don't create infinite error loop
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
        }
    }
    
    interceptConsole() {
        // Intercept console.error calls
        const originalError = console.error;
        console.error = (...args) => {
            // Call original first
            originalError.apply(console, args);
            
            // Then log to monitoring
            if (this.errorCount < this.maxErrorsPerSession) {
                this.errorCount++;
                const errorData = {
                    type: 'console_error',
                    message: args.map(a => String(a)).join(' '),
                    page_url: window.location.href,
                    page_title: document.title,
                    timestamp: new Date().toISOString(),
                };
                this.sendToPostHog(errorData);
            }
        };
    }
    
    // Manual error reporting (for caught errors)
    reportError(error, context = {}) {
        const errorData = {
            type: 'manual_report',
            message: error.message || String(error),
            stack: error.stack || '',
            context: context,
            page_url: window.location.href,
            page_title: document.title,
            user_agent: navigator.userAgent,
            timestamp: new Date().toISOString(),
        };
        
        this.sendToPostHog(errorData);
        this.sendToSupabase(errorData);
    }
}

// Initialize error monitoring
let errorMonitoring;
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        errorMonitoring = new ErrorMonitoring();
        window.errorMonitoring = errorMonitoring;
    });
} else {
    errorMonitoring = new ErrorMonitoring();
    window.errorMonitoring = errorMonitoring;
}

// Export for global access
window.ErrorMonitoring = ErrorMonitoring;

