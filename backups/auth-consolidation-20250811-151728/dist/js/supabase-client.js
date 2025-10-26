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
(function() {
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
            throw new Error('Environment configuration not loaded');
        }
        
        // Wait for Supabase CDN to load
        attempts = 0;
        while (!window.supabase && attempts < 50) {
            await new Promise(resolve => setTimeout(resolve, 100));
            attempts++;
        }
        
        if (!window.supabase) {
            throw new Error('Supabase CDN not loaded');
        }
        
        const supabaseUrl = window.ENV.SUPABASE_URL;
        const supabaseKey = window.ENV.SUPABASE_ANON_KEY;
        
        if (!supabaseUrl || !supabaseKey) {
            throw new Error('Supabase configuration missing');
        }
        
        // Create Supabase client
        supabaseClient = window.supabase.createClient(supabaseUrl, supabaseKey, {
            auth: {
                autoRefreshToken: true,
                persistSession: true,
                detectSessionInUrl: true,
                flowType: 'pkce'
            }
        });
        
        console.log('✅ Supabase client initialized successfully');
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
            // Make client globally available
            window.supabase = client;
            
            // Dispatch ready event
            window.dispatchEvent(new CustomEvent('supabaseReady', {
                detail: { client }
            }));
        }).catch(error => {
            console.error('❌ Failed to initialize Supabase:', error);
            
            // Dispatch error event
            window.dispatchEvent(new CustomEvent('supabaseError', {
                detail: { error }
            }));
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