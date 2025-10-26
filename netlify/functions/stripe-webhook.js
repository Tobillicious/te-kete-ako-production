// Stripe Webhook Handler
// Created: October 26, 2025
// Purpose: Process Stripe subscription events and update database

const { createClient } = require('@supabase/supabase-js');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

exports.handler = async (event, context) => {
  const sig = event.headers['stripe-signature'];
  const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

  let stripeEvent;

  try {
    stripeEvent = stripe.webhooks.constructEvent(event.body, sig, endpointSecret);
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message);
    return { statusCode: 400, body: 'Webhook signature verification failed' };
  }

  try {
    switch (stripeEvent.type) {
      case 'checkout.session.completed':
        await handleCheckoutCompleted(stripeEvent.data.object);
        break;
        
      case 'customer.subscription.created':
        await handleSubscriptionCreated(stripeEvent.data.object);
        break;
        
      case 'customer.subscription.updated':
        await handleSubscriptionUpdated(stripeEvent.data.object);
        break;
        
      case 'customer.subscription.deleted':
        await handleSubscriptionDeleted(stripeEvent.data.object);
        break;
        
      case 'invoice.payment_succeeded':
        await handlePaymentSucceeded(stripeEvent.data.object);
        break;
        
      case 'invoice.payment_failed':
        await handlePaymentFailed(stripeEvent.data.object);
        break;
        
      default:
        console.log(`Unhandled event type: ${stripeEvent.type}`);
    }

    return { statusCode: 200, body: 'Webhook processed successfully' };

  } catch (error) {
    console.error('Webhook processing error:', error);
    return { statusCode: 500, body: 'Webhook processing failed' };
  }
};

// Handle successful checkout
async function handleCheckoutCompleted(session) {
  console.log('Checkout completed:', session.id);
  
  const { data: subscription, error } = await supabase
    .from('subscriptions')
    .insert({
      user_id: session.metadata.user_id,
      plan_id: session.metadata.plan_id,
      stripe_customer_id: session.customer,
      stripe_subscription_id: session.subscription,
      status: 'trialing',
      created_at: new Date().toISOString()
    });

  if (error) {
    console.error('Error creating subscription:', error);
    throw error;
  }

  // Update user profile
  await supabase
    .from('profiles')
    .update({
      subscription_status: 'trialing',
      subscription_tier: session.metadata.plan_type
    })
    .eq('id', session.metadata.user_id);

  console.log('Subscription created successfully');
}

// Handle subscription creation
async function handleSubscriptionCreated(subscription) {
  console.log('Subscription created:', subscription.id);
  
  const { error } = await supabase
    .from('subscriptions')
    .update({
      stripe_subscription_id: subscription.id,
      status: subscription.status,
      current_period_start: new Date(subscription.current_period_start * 1000).toISOString(),
      current_period_end: new Date(subscription.current_period_end * 1000).toISOString(),
      updated_at: new Date().toISOString()
    })
    .eq('stripe_customer_id', subscription.customer);

  if (error) {
    console.error('Error updating subscription:', error);
    throw error;
  }

  console.log('Subscription updated successfully');
}

// Handle subscription updates
async function handleSubscriptionUpdated(subscription) {
  console.log('Subscription updated:', subscription.id);
  
  const { error } = await supabase
    .from('subscriptions')
    .update({
      status: subscription.status,
      current_period_start: new Date(subscription.current_period_start * 1000).toISOString(),
      current_period_end: new Date(subscription.current_period_end * 1000).toISOString(),
      cancel_at_period_end: subscription.cancel_at_period_end,
      canceled_at: subscription.canceled_at ? new Date(subscription.canceled_at * 1000).toISOString() : null,
      updated_at: new Date().toISOString()
    })
    .eq('stripe_subscription_id', subscription.id);

  if (error) {
    console.error('Error updating subscription:', error);
    throw error;
  }

  // Update user profile status
  const { data: subData } = await supabase
    .from('subscriptions')
    .select('user_id, plan_id')
    .eq('stripe_subscription_id', subscription.id)
    .single();

  if (subData) {
    const { data: planData } = await supabase
      .from('subscription_plans')
      .select('name')
      .eq('id', subData.plan_id)
      .single();

    await supabase
      .from('profiles')
      .update({
        subscription_status: subscription.status,
        subscription_tier: planData?.name || 'unknown'
      })
      .eq('id', subData.user_id);
  }

  console.log('Subscription and user profile updated successfully');
}

// Handle subscription deletion
async function handleSubscriptionDeleted(subscription) {
  console.log('Subscription deleted:', subscription.id);
  
  const { error } = await supabase
    .from('subscriptions')
    .update({
      status: 'canceled',
      canceled_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    })
    .eq('stripe_subscription_id', subscription.id);

  if (error) {
    console.error('Error updating subscription:', error);
    throw error;
  }

  // Update user profile
  const { data: subData } = await supabase
    .from('subscriptions')
    .select('user_id')
    .eq('stripe_subscription_id', subscription.id)
    .single();

  if (subData) {
    await supabase
      .from('profiles')
      .update({
        subscription_status: 'canceled',
        subscription_tier: 'free'
      })
      .eq('id', subData.user_id);
  }

  console.log('Subscription canceled successfully');
}

// Handle successful payment
async function handlePaymentSucceeded(invoice) {
  console.log('Payment succeeded:', invoice.id);
  
  // Record payment in payment_history
  const { data: subscription } = await supabase
    .from('subscriptions')
    .select('id, user_id')
    .eq('stripe_customer_id', invoice.customer)
    .single();

  if (subscription) {
    await supabase
      .from('payment_history')
      .insert({
        subscription_id: subscription.id,
        stripe_payment_intent_id: invoice.payment_intent,
        amount_cents: invoice.amount_paid,
        currency: invoice.currency,
        status: 'succeeded',
        payment_method: invoice.payment_method_types?.[0] || 'card'
      });
  }

  console.log('Payment recorded successfully');
}

// Handle failed payment
async function handlePaymentFailed(invoice) {
  console.log('Payment failed:', invoice.id);
  
  // Update subscription status
  const { error } = await supabase
    .from('subscriptions')
    .update({
      status: 'past_due',
      updated_at: new Date().toISOString()
    })
    .eq('stripe_customer_id', invoice.customer);

  if (error) {
    console.error('Error updating subscription status:', error);
    throw error;
  }

  console.log('Subscription status updated to past_due');
}
