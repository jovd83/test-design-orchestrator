Feature: Checkout with valid and invalid payment details
  As a shopper
  I want to pay for my basket
  So that I can complete my order

  Scenario: Successful card payment with valid details
    Given a shopper has items in the basket
    And the payment gateway is available
    When the shopper submits valid card details
    Then the payment is authorized
    And the order is confirmed

  Scenario: Payment is rejected for an expired card
    Given a shopper has items in the basket
    And the payment gateway is available
    When the shopper submits an expired card
    Then the payment is rejected
    And the shopper sees an expiration error
