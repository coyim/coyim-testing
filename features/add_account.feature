Feature: Add account

  Scenario: Ask to add account when does not have it configured
    Given the user has no account configured
    When the user opens the application
    And choses to not encrypt the configuration file
    Then should display add account dialog

  Scenario: Add an existing account
    Given the user has no account configured
    When the user opens the application
    And choses to not encrypt the configuration file
    When user provides the account details
      """
      coyim(AT)riseup.net
      """
    And saves the account
    Then account should be added to account list
      """
      coyim@riseup.net
      """
