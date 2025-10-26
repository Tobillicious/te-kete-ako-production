/**
 * SUBSCRIPTION CHECK COMPONENT
 * Verifies active subscription via Stripe
 * Shows upgrade prompt for free users
 */

(async function initSubscriptionCheck() {
    const { createClient } = supabase;
    
    const supabaseClient = createClient(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
    );
    
    try {
        // Get current user
        const { data: { user }, error } = await supabaseClient.auth.getUser();
        
        if (error || !user) {
            // Not logged in - auth gate should handle this
            return;
        }
        
        // Check subscription status in user metadata
        const subscriptionStatus = user.user_metadata?.subscription_status || 'free';
        const subscriptionTier = user.user_metadata?.subscription_tier || 'free';
        const trialEnd = user.user_metadata?.trial_end;
        
        // Check if trial active
        const now = new Date();
        const trialEndDate = trialEnd ? new Date(trialEnd) : null;
        const onTrial = trialEndDate && now < trialEndDate;
        
        // Determine access level
        const hasFullAccess = subscriptionStatus === 'active' || onTrial;
        
        if (!hasFullAccess) {
            // Free user or expired - show upgrade prompt
            showUpgradePrompt(subscriptionTier, trialEndDate);
        } else {
            // Has access - show subscription indicator
            showSubscriptionIndicator(subscriptionTier, trialEndDate);
        }
        
    } catch (err) {
        console.error('Subscription check error:', err);
    }
})();

function showUpgradePrompt(currentTier, trialEnd) {
    // Create upgrade banner
    const banner = document.createElement('div');
    banner.id = 'upgrade-banner';
    banner.style.cssText = `
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(135deg, #1a4d2e 0%, #2d5a3d 100%);
        color: white;
        padding: 20px;
        text-align: center;
        box-shadow: 0 -4px 12px rgba(0,0,0,0.3);
        z-index: 9999;
        animation: slideUp 0.5s ease-out;
    `;
    
    const trialExpired = trialEnd && new Date() > new Date(trialEnd);
    
    banner.innerHTML = `
        <div style="max-width: 1200px; margin: 0 auto;">
            <h3 style="margin: 0 0 10px 0; font-size: 1.5em; color: #f4d03f;">
                ${trialExpired ? '🔓 Free Trial Expired' : '⭐ Enjoying Te Kete Ako?'}
            </h3>
            <p style="margin: 0 0 15px 0; font-size: 1.1em;">
                ${trialExpired 
                    ? 'Upgrade to continue accessing premium lessons, units, and professional tools!'
                    : 'Unlock 3,500+ premium resources, AI tools, and professional features!'}
            </p>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="/pricing-professional.html" style="background: #f4d03f; color: #1a4d2e; padding: 12px 32px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 1.1em;">
                    View Plans & Pricing →
                </a>
                <button onclick="document.getElementById('upgrade-banner').remove()" style="background: transparent; border: 2px solid white; color: white; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-weight: bold;">
                    Maybe Later
                </button>
            </div>
        </div>
        <style>
            @keyframes slideUp {
                from { transform: translateY(100%); }
                to { transform: translateY(0); }
            }
        </style>
    `;
    
    document.body.appendChild(banner);
}

function showSubscriptionIndicator(tier, trialEnd) {
    // Show subtle subscription badge
    const indicator = document.createElement('div');
    indicator.id = 'subscription-indicator';
    indicator.style.cssText = `
        position: fixed;
        top: 80px;
        right: 20px;
        background: #f4d03f;
        color: #1a4d2e;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9em;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        z-index: 9998;
    `;
    
    const now = new Date();
    const trialEndDate = trialEnd ? new Date(trialEnd) : null;
    const daysLeft = trialEndDate ? Math.ceil((trialEndDate - now) / (1000 * 60 * 60 * 24)) : 0;
    
    if (trialEndDate && now < trialEndDate) {
        indicator.innerHTML = `🎁 Free Trial (${daysLeft} days left)`;
    } else if (tier === 'individual') {
        indicator.innerHTML = `⭐ Individual Plan`;
    } else if (tier === 'school') {
        indicator.innerHTML = `🏫 School Plan`;
    } else if (tier === 'enterprise') {
        indicator.innerHTML = `🌟 Enterprise Plan`;
    } else {
        return; // Don't show for free tier with no trial
    }
    
    document.body.appendChild(indicator);
}

// Export for use in other components
window.SubscriptionCheck = {
    async hasAccess() {
        const { createClient } = supabase;
        const supabaseClient = createClient(
            'https://nlgldaqtubrlcqddppbq.supabase.co',
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
        );
        
        const { data: { user } } = await supabaseClient.auth.getUser();
        if (!user) return false;
        
        const subscriptionStatus = user.user_metadata?.subscription_status || 'free';
        const trialEnd = user.user_metadata?.trial_end;
        const onTrial = trialEnd && new Date() < new Date(trialEnd);
        
        return subscriptionStatus === 'active' || onTrial;
    }
};


