/**
 * 🏗️ SUPABASE SINGLETON - Prevents Multiple Client Instances
 * Centralized Supabase client to avoid "Multiple GoTrueClient instances" warnings
 */

class SupabaseSingleton {
    constructor() {
        this.client = null;
        this.initialized = false;
    }

    async getClient() {
        if (this.client && this.initialized) {
            return this.client;
        }

        // Wait for Supabase to load
        if (!window.supabase) {
            await this.waitForSupabase();
        }

        if (!this.client) {
            this.client = window.supabase.createClient(
                window.SUPABASE_URL || 'https://nlgldaqtubrlcqddppbq.supabase.co',
                window.SUPABASE_ANON_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
            );
            this.initialized = true;
        }

        return this.client;
    }

    async waitForSupabase() {
        return new Promise((resolve) => {
            const checkSupabase = () => {
                if (window.supabase) {
                    resolve();
                } else {
                    setTimeout(checkSupabase, 100);
                }
            };
            checkSupabase();
        });
    }

    // Reset client (useful for testing)
    reset() {
        this.client = null;
        this.initialized = false;
    }
}

// Global singleton instance
window.supabaseSingleton = new SupabaseSingleton();

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SupabaseSingleton;
}
