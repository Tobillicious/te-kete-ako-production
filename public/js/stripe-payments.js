/**
 * Stripe Payments Integration - Te Kete Ako
 * School subscriptions and premium features
 * Phase 1 of Tech Stack Evolution
 */

class TeKeteStripe {
    constructor() {
        this.stripe = null;
        this.elements = null;
        this.paymentElement = null;
        this.init();
    }

    async init() {
        // Load Stripe.js
        await this.loadStripe();
        this.setupPaymentForms();
        this.setupSubscriptionPlans();
    }

    async loadStripe() {
        if (window.Stripe) {
            this.stripe = window.Stripe('pk_test_51234567890abcdef'); // Replace with your publishable key
            return;
        }

        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://js.stripe.com/v3/';
            script.onload = () => {
                this.stripe = window.Stripe('pk_test_51234567890abcdef'); // Replace with your publishable key
                resolve();
            };
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    setupPaymentForms() {
        // School Subscription Form
        const schoolForm = document.getElementById('school-subscription-form');
        if (schoolForm) {
            schoolForm.addEventListener('submit', (e) => this.handleSchoolSubscription(e));
        }

        // Premium Features Form
        const premiumForm = document.getElementById('premium-features-form');
        if (premiumForm) {
            premiumForm.addEventListener('submit', (e) => this.handlePremiumFeatures(e));
        }
    }

    setupSubscriptionPlans() {
        // Display subscription plans
        this.renderSubscriptionPlans();
    }

    renderSubscriptionPlans() {
        const plansContainer = document.getElementById('subscription-plans');
        if (!plansContainer) return;

        const plans = [
            {
                name: 'Individual Teacher',
                price: '$29',
                period: '/month',
                features: [
                    'Access to all lessons',
                    'Premium handouts',
                    'AI-powered recommendations',
                    'Priority support'
                ],
                popular: false,
                stripePriceId: 'price_individual_monthly'
            },
            {
                name: 'School License',
                price: '$199',
                period: '/month',
                features: [
                    'Unlimited teachers',
                    'School-wide analytics',
                    'Custom branding',
                    'Bulk lesson creation',
                    'Admin dashboard'
                ],
                popular: true,
                stripePriceId: 'price_school_monthly'
            },
            {
                name: 'District License',
                price: '$999',
                period: '/month',
                features: [
                    'Multiple schools',
                    'District analytics',
                    'Custom curriculum',
                    'Training sessions',
                    'Dedicated support'
                ],
                popular: false,
                stripePriceId: 'price_district_monthly'
            }
        ];

        plansContainer.innerHTML = plans.map(plan => `
            <div class="subscription-plan ${plan.popular ? 'popular' : ''}">
                <div class="plan-header">
                    <h3>${plan.name}</h3>
                    ${plan.popular ? '<span class="popular-badge">Most Popular</span>' : ''}
                </div>
                <div class="plan-price">
                    <span class="price">${plan.price}</span>
                    <span class="period">${plan.period}</span>
                </div>
                <ul class="plan-features">
                    ${plan.features.map(feature => `<li>✓ ${feature}</li>`).join('')}
                </ul>
                <button class="subscribe-btn" data-price-id="${plan.stripePriceId}">
                    Choose Plan
                </button>
            </div>
        `).join('');

        // Add event listeners to subscribe buttons
        plansContainer.querySelectorAll('.subscribe-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.handlePlanSelection(e));
        });
    }

    async handlePlanSelection(e) {
        const priceId = e.target.getAttribute('data-price-id');
        const planName = e.target.closest('.subscription-plan').querySelector('h3').textContent;
        
        try {
            // Create checkout session
            const response = await fetch('/api/create-checkout-session', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    priceId: priceId,
                    planName: planName,
                    successUrl: `${window.location.origin}/payment-success.html`,
                    cancelUrl: `${window.location.origin}/pricing.html`
                })
            });

            const { sessionId } = await response.json();
            
            // Redirect to Stripe Checkout
            const { error } = await this.stripe.redirectToCheckout({
                sessionId: sessionId
            });

            if (error) {
                this.showError('Payment failed. Please try again.');
            }
            
        } catch (error) {
            console.error('Stripe error:', error);
            this.showError('Unable to process payment. Please try again.');
        }
    }

    async handleSchoolSubscription(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const schoolData = {
            schoolName: formData.get('schoolName'),
            contactEmail: formData.get('contactEmail'),
            numberOfTeachers: formData.get('numberOfTeachers'),
            planType: formData.get('planType')
        };

        try {
            // Create school subscription
            const response = await fetch('/api/create-school-subscription', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(schoolData)
            });

            const { sessionId } = await response.json();
            
            // Redirect to Stripe Checkout
            const { error } = await this.stripe.redirectToCheckout({
                sessionId: sessionId
            });

            if (error) {
                this.showError('School subscription failed. Please try again.');
            }
            
        } catch (error) {
            console.error('School subscription error:', error);
            this.showError('Unable to process school subscription. Please try again.');
        }
    }

    async handlePremiumFeatures(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const features = formData.getAll('premiumFeatures');
        
        try {
            // Create premium features checkout
            const response = await fetch('/api/create-premium-checkout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    features: features,
                    successUrl: `${window.location.origin}/payment-success.html`,
                    cancelUrl: `${window.location.origin}/premium-features.html`
                })
            });

            const { sessionId } = await response.json();
            
            // Redirect to Stripe Checkout
            const { error } = await this.stripe.redirectToCheckout({
                sessionId: sessionId
            });

            if (error) {
                this.showError('Premium features purchase failed. Please try again.');
            }
            
        } catch (error) {
            console.error('Premium features error:', error);
            this.showError('Unable to process premium features. Please try again.');
        }
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showSuccess(message) {
        this.showNotification(message, 'success');
    }

    showNotification(message, type) {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'success' ? 'bg-green-500 text-white' : 'bg-red-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
}

// Initialize Stripe when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new TeKeteStripe());
} else {
    new TeKeteStripe();
}

// Export for global access
window.TeKeteStripe = TeKeteStripe;
