/**
 * STRIPE CONFIGURATION - Te Kete Ako
 * Professional SaaS Subscription System
 * 
 * ACTIVATED: October 26, 2025
 */

// Stripe configuration
const STRIPE_CONFIG = {
    publishableKey: 'pk_test_51SMGLWDhKhPdHioTA315YQtT44VGdqaL1YcnL4sotO2MZY1OcQ3Spr7kyXKdpOsOEkzT0BcOFqi7eE2bkPaguvxv00YrLzu9WB',
    plans: {
        individual_monthly: {
            priceId: null, // Set after creating in Stripe dashboard
            name: 'Individual Monthly',
            price: '$15 NZD/month',
            trial: 14,
            features: [
                'Full access to 3,500+ resources',
                'AI lesson planning assistant',
                'Progress tracking',
                'Unlimited downloads',
                'Mobile app access',
                'Email support'
            ]
        },
        individual_annual: {
            priceId: null,
            name: 'Individual Annual',
            price: '$150 NZD/year',
            savings: 'Save $30/year!',
            trial: 14,
            features: [
                'Everything in Monthly',
                'Best value - 2 months free!'
            ]
        },
        school_annual: {
            priceId: null,
            name: 'School License',
            price: '$499 NZD/year',
            users: 'Up to 50 users',
            trial: 30,
            features: [
                'All Individual features',
                'School-wide dashboard',
                'Teacher collaboration',
                'Student progress tracking',
                'KAMAR integration ready',
                'Priority support',
                '2 training workshops/year'
            ]
        }
    }
};

// Initialize Stripe
const stripe = Stripe(STRIPE_CONFIG.publishableKey);

// Export for use in other files
window.TeKeteStripe = {
    stripe: stripe,
    config: STRIPE_CONFIG,
    
    // Create checkout session
    createCheckout: async function(plan) {
        try {
            const response = await fetch('/.netlify/functions/create-checkout-session', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ plan: plan })
            });
            
            const session = await response.json();
            
            // Redirect to Stripe checkout
            const result = await stripe.redirectToCheckout({
                sessionId: session.id
            });
            
            if (result.error) {
                console.error('Stripe error:', result.error);
                alert('Payment error: ' + result.error.message);
            }
        } catch (error) {
            console.error('Checkout error:', error);
            alert('Unable to start checkout. Please try again.');
        }
    },
    
    // Check subscription status
    checkSubscription: async function() {
        try {
            const response = await fetch('/.netlify/functions/check-subscription', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            });
            
            return await response.json();
        } catch (error) {
            console.error('Subscription check error:', error);
            return { active: false };
        }
    }
};

console.log('✅ Stripe initialized - Professional subscriptions ready!');

