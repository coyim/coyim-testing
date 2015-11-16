Feature: Add account

  Scenario: Ask to add account when does not have it configured
    Given the user has no account configured
    When the user opens the application
    And choses to not encrypt the configuration file
    Then add account dialog is displayed

