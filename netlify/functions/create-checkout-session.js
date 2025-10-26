/**
 * CREATE STRIPE CHECKOUT SESSION
 * Handles subscription checkout for Te Kete Ako
 */

const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event, context) => {
    // Only allow POST
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' })
        };
    }

    try {
        const { plan, userEmail } = JSON.parse(event.body);

        // Price IDs from Stripe dashboard
        const priceIds = {
            'individual_monthly': 'price_1SMHrsDhKhPdHioTGHtK83M4', // ✅ ACTIVATED!
            'individual_annual': 'price_individual_annual',   // Needs Price ID
            'school_annual': 'price_school_annual'            // Needs Price ID
        };

        if (!priceIds[plan]) {
            return {
                statusCode: 400,
                body: JSON.stringify({ error: 'Invalid plan' })
            };
        }

        // Create Stripe checkout session
        const session = await stripe.checkout.sessions.create({
            payment_method_types: ['card'],
            mode: 'subscription',
            line_items: [
                {
                    price: priceIds[plan],
                    quantity: 1,
                },
            ],
            customer_email: userEmail,
            allow_promotion_codes: true,
            subscription_data: {
                trial_period_days: plan === 'school_annual' ? 30 : 14,
                metadata: {
                    plan: plan
                }
            },
            success_url: `${process.env.URL || 'https://tekete.netlify.app'}/success?session_id={CHECKOUT_SESSION_ID}`,
            cancel_url: `${process.env.URL || 'https://tekete.netlify.app'}/pricing`,
        });

        return {
            statusCode: 200,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: session.id })
        };

    } catch (error) {
        console.error('Checkout error:', error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: error.message })
        };
    }
};

