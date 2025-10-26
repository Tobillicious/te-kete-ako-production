// Te Kete Ako Authentication Gate
// Created: October 26, 2025
// Purpose: Protect all content pages behind login and subscription

class TeKeteAuth {
    constructor() {
        this.supabase = null;
        this.currentUser = null;
        this.subscription = null;
        this.isInitialized = false;
    }

    async init() {
        if (this.isInitialized) return;

        try {
            // Initialize Supabase
            const { createClient } = supabase;
            this.supabase = createClient(
                'https://nlgldaqtubrlcqddppbq.supabase.co',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
            );

            // Get current user
            const { data: { user }, error } = await this.supabase.auth.getUser();
            
            if (error) {
                console.error('Auth error:', error);
                this.redirectToLogin();
                return;
            }

            this.currentUser = user;

            if (user) {
                // Load subscription details
                await this.loadSubscription();
            }

            this.isInitialized = true;

        } catch (error) {
            console.error('Auth initialization error:', error);
            this.redirectToLogin();
        }
    }

    async loadSubscription() {
        if (!this.currentUser) return;

        try {
            const { data: subscription, error } = await this.supabase
                .from('subscriptions')
                .select(`
                    *,
                    subscription_plans (
                        name,
                        amount_cents,
                        currency,
                        interval,
                        max_users
                    )
                `)
                .eq('user_id', this.currentUser.id)
                .order('created_at', { ascending: false })
                .limit(1)
                .single();

            if (error) {
                console.error('Subscription load error:', error);
                return;
            }

            this.subscription = subscription;

        } catch (error) {
            console.error('Subscription loading error:', error);
        }
    }

    isLoggedIn() {
        return !!this.currentUser;
    }

    hasActiveSubscription() {
        if (!this.subscription) return false;
        
        const validStatuses = ['active', 'trialing'];
        const isActive = validStatuses.includes(this.subscription.status);
        const notExpired = !this.subscription.current_period_end || 
                          new Date(this.subscription.current_period_end) > new Date();
        
        return isActive && notExpired;
    }

    getSubscriptionTier() {
        if (!this.subscription) return 'free';
        return this.subscription.subscription_plans?.name || 'free';
    }

    getRole() {
        if (!this.currentUser) return 'guest';
        
        // Check user metadata for role
        const role = this.currentUser.user_metadata?.role;
        if (role) return role;
        
        // Default to teacher for now
        return 'teacher';
    }

    redirectToLogin() {
        const currentPath = window.location.pathname;
        const redirectUrl = encodeURIComponent(currentPath);
        window.location.href = `/login.html?redirect=${redirectUrl}`;
    }

    redirectToPricing() {
        window.location.href = '/pricing.html';
    }

    showSubscriptionRequired() {
        // Create modal for subscription required
        const modal = document.createElement('div');
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
        `;
        
        modal.innerHTML = `
            <div style="
                background: white;
                padding: 3rem;
                border-radius: 16px;
                max-width: 500px;
                text-align: center;
                box-shadow: 0 16px 32px rgba(0, 0, 0, 0.3);
            ">
                <div style="font-size: 4rem; margin-bottom: 1rem;">🔒</div>
                <h2 style="color: var(--bmad-forest-green, #2F4F2F); margin-bottom: 1rem;">
                    Subscription Required
                </h2>
                <p style="color: var(--bmad-warm-gray, #8B7D6B); margin-bottom: 2rem;">
                    This content requires an active subscription. Start your 14-day free trial today!
                </p>
                <div style="display: flex; gap: 1rem; justify-content: center;">
                    <button onclick="window.location.href='/pricing.html'" style="
                        background: var(--bmad-earth-brown, #8B4513);
                        color: white;
                        border: none;
                        padding: 1rem 2rem;
                        border-radius: 12px;
                        font-weight: 600;
                        cursor: pointer;
                    ">
                        View Pricing
                    </button>
                    <button onclick="this.closest('div').parentElement.remove()" style="
                        background: var(--bmad-warm-gray, #8B7D6B);
                        color: white;
                        border: none;
                        padding: 1rem 2rem;
                        border-radius: 12px;
                        font-weight: 600;
                        cursor: pointer;
                    ">
                        Maybe Later
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
    }

    // Check if current page requires subscription
    requiresSubscription() {
        const protectedPaths = [
            '/teacher-dashboard.html',
            '/teacher-weekly-planner.html',
            '/ai-serverless-functions.html',
            '/subscription-dashboard.html'
        ];
        
        const currentPath = window.location.pathname;
        return protectedPaths.some(path => currentPath.includes(path));
    }

    // Main protection method
    async protectPage() {
        await this.init();
        
        // Check if user is logged in
        if (!this.isLoggedIn()) {
            this.redirectToLogin();
            return false;
        }
        
        // Check if page requires subscription
        if (this.requiresSubscription() && !this.hasActiveSubscription()) {
            this.showSubscriptionRequired();
            return false;
        }
        
        return true;
    }

    // Get user info for personalization
    getUserInfo() {
        return {
            user: this.currentUser,
            subscription: this.subscription,
            role: this.getRole(),
            tier: this.getSubscriptionTier(),
            hasAccess: this.hasActiveSubscription()
        };
    }
}

// Initialize global auth instance
window.TeKeteAuth = new TeKeteAuth();

// Auto-protect page on load
document.addEventListener('DOMContentLoaded', async () => {
    const isProtected = await window.TeKeteAuth.protectPage();
    
    if (isProtected) {
        // Page is protected, user has access
        console.log('✅ Page access granted');
        
        // Personalize page based on user role
        const userInfo = window.TeKeteAuth.getUserInfo();
        
        if (userInfo.role === 'teacher') {
            // Show teacher-specific features
            document.body.classList.add('teacher-view');
        } else if (userInfo.role === 'student') {
            // Show student-specific features
            document.body.classList.add('student-view');
        }
        
        // Show subscription tier features
        if (userInfo.tier !== 'free') {
            document.body.classList.add('premium-features');
        }
        
    } else {
        console.log('❌ Page access denied');
    }
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TeKeteAuth;
}
