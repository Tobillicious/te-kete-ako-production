// Stripe Checkout Session Creator
// Created: October 26, 2025
// Purpose: Handle subscription checkout with your Stripe price ID

const { createClient } = require('@supabase/supabase-js');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const { priceId, userId, planType, trialDays } = JSON.parse(event.body);

    if (!priceId || !userId) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Missing required parameters' })
      };
    }

    // Get user details from Supabase
    const { data: user, error: userError } = await supabase.auth.admin.getUserById(userId);
    
    if (userError || !user) {
      return {
        statusCode: 404,
        body: JSON.stringify({ error: 'User not found' })
      };
    }

    // Get subscription plan details
    const { data: plan, error: planError } = await supabase
      .from('subscription_plans')
      .select('*')
      .eq('stripe_price_id', priceId)
      .single();

    if (planError || !plan) {
      return {
        statusCode: 404,
        body: JSON.stringify({ error: 'Subscription plan not found' })
      };
    }

    // Create or get Stripe customer
    let customer;
    try {
      // Check if customer already exists
      const { data: existingSubscription } = await supabase
        .from('subscriptions')
        .select('stripe_customer_id')
        .eq('user_id', userId)
        .single();

      if (existingSubscription?.stripe_customer_id) {
        customer = await stripe.customers.retrieve(existingSubscription.stripe_customer_id);
      } else {
        // Create new customer
        customer = await stripe.customers.create({
          email: user.email,
          name: user.user_metadata?.full_name || user.email,
          metadata: {
            user_id: userId,
            plan_type: planType
          }
        });
      }
    } catch (stripeError) {
      console.error('Stripe customer error:', stripeError);
      return {
        statusCode: 500,
        body: JSON.stringify({ error: 'Failed to create customer' })
      };
    }

    // Create checkout session
    const session = await stripe.checkout.sessions.create({
      customer: customer.id,
      payment_method_types: ['card'],
      line_items: [
        {
          price: priceId, // Your price ID: price_1SMHrsDhKhPdHioTGHtK83M4
          quantity: 1,
        },
      ],
      mode: 'subscription',
      success_url: `${process.env.SITE_URL}/subscription-success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.SITE_URL}/pricing?cancelled=true`,
      subscription_data: {
        trial_period_days: trialDays || 14,
        metadata: {
          user_id: userId,
          plan_type: planType,
          plan_id: plan.id
        }
      },
      metadata: {
        user_id: userId,
        plan_type: planType,
        plan_id: plan.id
      },
      allow_promotion_codes: true,
      billing_address_collection: 'required',
      customer_update: {
        address: 'auto',
        name: 'auto'
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ 
        sessionId: session.id,
        url: session.url 
      })
    };

  } catch (error) {
    console.error('Checkout session error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Internal server error',
        details: error.message 
      })
    };
  }
};