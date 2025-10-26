// Create Stripe Billing Portal Session
// Created: October 26, 2025
// Purpose: Allow users to manage payment methods and view invoices

const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const { customerId } = JSON.parse(event.body);

    if (!customerId) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Customer ID required' })
      };
    }

    // Create billing portal session
    const session = await stripe.billingPortal.sessions.create({
      customer: customerId,
      return_url: `${process.env.URL}/my-subscription.html`,
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ url: session.url })
    };

  } catch (error) {
    console.error('Billing portal error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ 
        error: 'Failed to create billing portal session',
        details: error.message 
      })
    };
  }
};
