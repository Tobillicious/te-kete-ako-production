/**
 * ================================================================
 * SUPABASE CLIENT - TE KETE AKO UNIFIED AUTH
 * ================================================================
 * 
 * Unified Supabase client initialization for Te Kete Ako
 * Integrates with environment config and provides global client access
 * 
 * ================================================================
 */

// Initialize Supabase client once environment is loaded
(function () {
    if (window.supabaseClient) return;
    
    'use strict';
    
    let supabaseClient = null;
    let initializationPromise = null;
    
    /**
     * Initialize Supabase client with retry logic
     */
    async function initializeSupabaseClient() {
        // Wait for environment config
        let attempts = 0;
        while (!window.ENV && attempts < 50) {
            await new Promise(resolve => setTimeout(resolve, 100));
            attempts++;
        }
        
        if (!window.ENV) {
            console.warn('⚠️ ENV not loaded; initializing mock Supabase client for static/local context');
            const mock = {
                auth: {
                    getUser: () => Promise.resolve({ data: { user: null } }),
                    signInWithPassword: async () => ({ error: { message: 'Auth disabled in static preview' } }),
                    signOut: async () => ({})
                }
            };
            window.supabaseClient = mock;
            return mock;
        }
        
        // Wait for Supabase singleton to load
        attempts = 0;
        while (!window.supabaseSingleton && attempts < 50) {
            await new Promise(resolve => setTimeout(resolve, 100));
            attempts++;
        }
        
        if (!window.supabaseSingleton) {
            console.error('❌ Supabase singleton not loaded after 5 seconds - falling back to basic functionality');
            // Fallback: create mock client for testing
            const mock = {
                auth: {
                    getUser: () => Promise.resolve({ data: { user: null } }),
                    signInWithPassword: () => Promise.resolve({ error: { message: 'Singleton loading issue' } }),
                    signOut: () => Promise.resolve({})
                }
            };
            window.supabaseClient = mock;
            return mock;
        }
        
        const supabaseUrl = window.ENV.SUPABASE_URL;
        const supabaseKey = window.ENV.SUPABASE_ANON_KEY;
        
        if (!supabaseUrl || !supabaseKey) {
            console.warn('⚠️ Supabase config missing; using mock client');
            const mock = {
                auth: {
                    getUser: () => Promise.resolve({ data: { user: null } }),
                    signInWithPassword: async () => ({ error: { message: 'Missing Supabase config' } }),
                    signOut: async () => ({})
                }
            };
            window.supabaseClient = mock;
            return mock;
        }
        
        // Use Supabase singleton client
        supabaseClient = await window.supabaseSingleton.getClient();
        
        // Export globally to prevent re-initialization
        window.supabaseClient = supabaseClient;
        
        return supabaseClient;
    }
    
    /**
     * Get Supabase client (initializes if needed)
     */
    async function getSupabaseClient() {
        if (supabaseClient) {
            return supabaseClient;
        }
        
        if (!initializationPromise) {
            initializationPromise = initializeSupabaseClient();
        }
        
        return await initializationPromise;
    }
    
    /**
     * Initialize immediately when DOM is ready
     */
    function initialize() {
        getSupabaseClient().then(client => {
            // Make client globally available if it looks like a real client
            if (client && client.auth) {
                window.supabase = client;
            }
            // Dispatch ready event
            window.dispatchEvent(new CustomEvent('supabaseReady', {
                detail: { client }
            }));
        }).catch(error => {
            console.error('❌ Failed to initialize Supabase:', error);
            // As a last resort, expose a mock to prevent UI crashes
            const mock = {
                auth: {
                    getUser: () => Promise.resolve({ data: { user: null } }),
                    signInWithPassword: async () => ({ error: { message: 'Supabase init error' } }),
                    signOut: async () => ({})
                }
            };
            window.supabaseClient = mock;
            window.dispatchEvent(new CustomEvent('supabaseReady', { detail: { client: mock } }));
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initialize);
    } else {
        initialize();
    }
    
    // Export for global access
    window.getSupabaseClient = getSupabaseClient;
})();