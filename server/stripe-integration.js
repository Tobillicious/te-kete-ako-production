/**
 * Stripe Integration - Te Kete Ako
 * Backend server for handling Stripe payments and subscriptions
 * 
 * SETUP INSTRUCTIONS:
 * 1. npm install express stripe dotenv @supabase/supabase-js
 * 2. Create .env file with:
 *    STRIPE_SECRET_KEY=sk_test_...
 *    STRIPE_WEBHOOK_SECRET=whsec_...
 *    SUPABASE_URL=https://...
 *    SUPABASE_SERVICE_KEY=...
 * 3. Run: node server/stripe-integration.js
 */

const express = require('express');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

const app = express();
const supabase = createClient(
    process.env.SUPABASE_URL,
    process.env.SUPABASE_SERVICE_KEY
);

// Middleware
app.use(express.json());
app.use(express.static('public'));

// Stripe Price IDs (Set these up in Stripe Dashboard)
const PRICES = {
    individual: 'price_individual_monthly', // Replace with actual price ID
    school: 'price_school_yearly'           // Replace with actual price ID
};

/**
 * CREATE SUBSCRIPTION
 * Handle new subscription creation
 */
app.post('/api/create-subscription', async (req, res) => {
    try {
        const { paymentMethodId, plan, customerInfo } = req.body;

        // 1. Create or retrieve customer
        const customer = await stripe.customers.create({
            payment_method: paymentMethodId,
            email: customerInfo.email,
            name: `${customerInfo.firstName} ${customerInfo.lastName}`,
            metadata: {
                school: customerInfo.school,
                role: customerInfo.role,
                plan: plan
            },
            invoice_settings: {
                default_payment_method: paymentMethodId,
            },
        });

        // 2. Create subscription
        const subscription = await stripe.subscriptions.create({
            customer: customer.id,
            items: [{ price: PRICES[plan] }],
            trial_period_days: 14, // 14-day free trial
            expand: ['latest_invoice.payment_intent'],
        });

        // 3. Store customer in Supabase
        await supabase.from('customers').insert({
            stripe_customer_id: customer.id,
            email: customerInfo.email,
            first_name: customerInfo.firstName,
            last_name: customerInfo.lastName,
            school: customerInfo.school,
            role: customerInfo.role,
            plan: plan,
            subscription_id: subscription.id,
            subscription_status: subscription.status,
            trial_end: new Date(subscription.trial_end * 1000),
        });

        // 4. Return success
        res.json({
            subscriptionId: subscription.id,
            status: subscription.status,
            clientSecret: subscription.latest_invoice.payment_intent.client_secret,
        });

    } catch (error) {
        console.error('Subscription creation error:', error);
        res.status(400).json({ error: error.message });
    }
});

/**
 * CREATE PORTAL SESSION
 * Allow customers to manage their subscription
 */
app.post('/api/create-portal-session', async (req, res) => {
    try {
        const { customerId } = req.body;

        const session = await stripe.billingPortal.sessions.create({
            customer: customerId,
            return_url: `${req.headers.origin}/account`,
        });

        res.json({ url: session.url });
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

/**
 * WEBHOOK HANDLER
 * Handle Stripe events
 */
app.post('/api/webhook', express.raw({type: 'application/json'}), async (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;

    try {
        event = stripe.webhooks.constructEvent(
            req.body,
            sig,
            process.env.STRIPE_WEBHOOK_SECRET
        );
    } catch (err) {
        console.error('Webhook signature verification failed:', err.message);
        return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Handle the event
    switch (event.type) {
        case 'customer.subscription.created':
            await handleSubscriptionCreated(event.data.object);
            break;
        
        case 'customer.subscription.updated':
            await handleSubscriptionUpdated(event.data.object);
            break;
        
        case 'customer.subscription.deleted':
            await handleSubscriptionDeleted(event.data.object);
            break;
        
        case 'invoice.paid':
            await handleInvoicePaid(event.data.object);
            break;
        
        case 'invoice.payment_failed':
            await handlePaymentFailed(event.data.object);
            break;

        default:
            console.log(`Unhandled event type: ${event.type}`);
    }

    res.json({ received: true });
});

/**
 * WEBHOOK HANDLERS
 */
async function handleSubscriptionCreated(subscription) {
    console.log('Subscription created:', subscription.id);
    
    // Update Supabase
    await supabase
        .from('customers')
        .update({
            subscription_status: subscription.status,
            current_period_end: new Date(subscription.current_period_end * 1000),
        })
        .eq('subscription_id', subscription.id);
}

async function handleSubscriptionUpdated(subscription) {
    console.log('Subscription updated:', subscription.id);
    
    await supabase
        .from('customers')
        .update({
            subscription_status: subscription.status,
            current_period_end: new Date(subscription.current_period_end * 1000),
        })
        .eq('subscription_id', subscription.id);
}

async function handleSubscriptionDeleted(subscription) {
    console.log('Subscription cancelled:', subscription.id);
    
    await supabase
        .from('customers')
        .update({
            subscription_status: 'cancelled',
            cancelled_at: new Date(),
        })
        .eq('subscription_id', subscription.id);
}

async function handleInvoicePaid(invoice) {
    console.log('Invoice paid:', invoice.id);
    
    // Log payment
    await supabase.from('payments').insert({
        stripe_invoice_id: invoice.id,
        customer_id: invoice.customer,
        amount: invoice.amount_paid / 100,
        status: 'paid',
        paid_at: new Date(invoice.status_transitions.paid_at * 1000),
    });
}

async function handlePaymentFailed(invoice) {
    console.log('Payment failed:', invoice.id);
    
    // Send notification email (implement email service)
    // Update customer status
    await supabase
        .from('customers')
        .update({ payment_status: 'failed' })
        .eq('stripe_customer_id', invoice.customer);
}

/**
 * CHECK SUBSCRIPTION STATUS
 * API endpoint for frontend to check access
 */
app.get('/api/subscription-status/:email', async (req, res) => {
    try {
        const { email } = req.params;
        
        const { data, error } = await supabase
            .from('customers')
            .select('*')
            .eq('email', email)
            .single();

        if (error || !data) {
            return res.json({ hasAccess: false });
        }

        const hasAccess = ['active', 'trialing'].includes(data.subscription_status);
        
        res.json({
            hasAccess,
            plan: data.plan,
            status: data.subscription_status,
            trialEnd: data.trial_end,
            currentPeriodEnd: data.current_period_end,
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 Stripe integration server running on port ${PORT}`);
    console.log(`📊 Ready to accept payments for Te Kete Ako`);
});

module.exports = app;

