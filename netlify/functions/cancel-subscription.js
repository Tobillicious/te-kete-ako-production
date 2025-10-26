// Cancel Subscription
// Created: October 26, 2025
// Purpose: Allow users to cancel their subscription (at period end)

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
    const { subscriptionId } = JSON.parse(event.body);

    if (!subscriptionId) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Subscription ID required' })
      };
    }

    // Update Stripe subscription to cancel at period end
    const subscription = await stripe.subscriptions.update(subscriptionId, {
      cancel_at_period_end: true
    });

    // Update our database
    const { error: dbError } = await supabase
      .from('subscriptions')
      .update({
        cancel_at_period_end: true,
        updated_at: new Date().toISOString()
      })
      .eq('stripe_subscription_id', subscriptionId);

    if (dbError) {
      console.error('Database update error:', dbError);
    }

    return {
      statusCode: 200,
      body: JSON.stringify({ 
        success: true,
        message: 'Subscription will cancel at period end',
        periodEnd: subscription.current_period_end
      })
    };

  } catch (error) {
    console.error('Cancel subscription error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Failed to cancel subscription',
        details: error.message 
      })
    };
  }
};
