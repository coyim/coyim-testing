Feature: Configuration assistant

  Scenario: Show configuration assistant
    Given the user has no account configured
    When the user opens the application
    And choses to not encrypt the configuration file
    Then the configuration assistant is displayed

  Scenario: Add existing account
    Given the user has no account configured
    And Tor is listening on port 9050
    When the user opens the application
    And choses to not encrypt the configuration file
    Then the configuration assistant is displayed
    And the "Welcome" page is displayed
    Then the user goes to the next page
    And Tor is detected to be running on port 9050
    Then the user goes to the next page
    And the user provides the following account information
      | XMPP ID         | Password     |
      | user@riseup.net | use diceware |
    Then the user goes to the next page
    And SRV consult will returns the server info
    Then the user goes to the next page
    And the configuration step will be finished
    Then the user applies the configuration
    And the assistent will be closed
    Then the account "user@riseup.net" will be configured
    And it will have a safe default configuration

  Scenario: Add existing account that requires server config
    Given the user has no account configured
    And Tor is listening on port 9050
    When the user opens the application
    And choses to not encrypt the configuration file
    Then the configuration assistant is displayed
    And the "Welcome" page is displayed
    Then the user goes to the next page
    And the "Account details" page is displayed
    Then Tor is detected to be running on port 9050
    And the user provides the following account information
      | XMPP ID            |
      | user@someserver.im |
    Then the XMPP server can't be found
    And the "Server configuration" section is displayed with the following config
      | Server        | Port |
      | someserver.im | 5222 |
    Then the user accepts the configuration
    And the account "coyim@riseup.net" will be configured
    And it will have a safe default configuration

