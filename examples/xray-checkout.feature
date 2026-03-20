@REQ-CHECKOUT-001
@manual
Feature: Checkout payment processing
  As a shopper
  I want to complete payment during checkout
  So that I can place my order

  Scenario: Successful payment with valid card details
    Given a shopper has items in the basket
    And the payment gateway is available
    When the shopper submits valid card details
    Then the payment is authorized
    And the order is confirmed

  Scenario: Payment rejection for an expired card
    Given a shopper has items in the basket
    And the payment gateway is available
    When the shopper submits an expired card
    Then the payment is rejected
    And the shopper sees an expiration error
