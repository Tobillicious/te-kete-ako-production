/**
 * ENHANCED AUTHENTICATION
 * Extends auth-unified.js with additional features for premium users
 */

import { supabase } from './supabase-singleton.js';

class EnhancedAuth {
    constructor() {
        this.user = null;
        this.subscription = null;
        this.schoolLicense = null;
        this.init();
    }

    async init() {
        // Get current session
        const { data: { session }, error } = await supabase.auth.getSession();
        
        if (session?.user) {
            this.user = session.user;
            await this.loadUserMetadata();
        }

        // Listen for auth changes
        supabase.auth.onAuthStateChange((event, session) => {
            if (event === 'SIGNED_IN' && session?.user) {
                this.user = session.user;
                this.loadUserMetadata();
            } else if (event === 'SIGNED_OUT') {
                this.user = null;
                this.subscription = null;
                this.schoolLicense = null;
            }
        });
    }

    async loadUserMetadata() {
        if (!this.user) return;

        try {
            // Load subscription status
            const { data: subscription } = await supabase
                .from('subscriptions')
                .select('*, subscription_plans(*)')
                .eq('user_id', this.user.id)
                .eq('status', 'active')
                .single();

            this.subscription = subscription;

            // Load school license if exists
            const { data: schoolLicense } = await supabase
                .from('school_licenses')
                .select('*')
                .eq('email', this.user.email)
                .eq('status', 'active')
                .single();

            this.schoolLicense = schoolLicense;

            // Emit custom event
            window.dispatchEvent(new CustomEvent('auth-metadata-loaded', {
                detail: {
                    user: this.user,
                    subscription: this.subscription,
                    schoolLicense: this.schoolLicense
                }
            }));

        } catch (error) {
            console.error('Error loading user metadata:', error);
        }
    }

    hasActiveSubscription() {
        return this.subscription?.status === 'active';
    }

    hasSchoolLicense() {
        return this.schoolLicense?.status === 'active';
    }

    isSchoolAdmin() {
        return this.schoolLicense?.role === 'admin';
    }

    isPremium() {
        return this.hasActiveSubscription() || this.hasSchoolLicense();
    }

    getSubscriptionTier() {
        if (this.schoolLicense) {
            return this.schoolLicense.license_type;
        }
        if (this.subscription) {
            return this.subscription.subscription_plans.name;
        }
        return 'free';
    }

    async requireAuth() {
        if (!this.user) {
            window.location.href = '/login.html?redirect=' + encodeURIComponent(window.location.pathname);
            return false;
        }
        return true;
    }

    async requirePremium() {
        if (!await this.requireAuth()) return false;
        
        if (!this.isPremium()) {
            window.location.href = '/pricing.html?upgrade=true';
            return false;
        }
        return true;
    }

    async requireSchoolAdmin() {
        if (!await this.requireAuth()) return false;
        
        if (!this.isSchoolAdmin()) {
            alert('This feature is only available to school administrators.');
            return false;
        }
        return true;
    }
}

// Export singleton instance
export const enhancedAuth = new EnhancedAuth();

// Also expose globally for non-module usage
if (typeof window !== 'undefined') {
    window.enhancedAuth = enhancedAuth;
}

