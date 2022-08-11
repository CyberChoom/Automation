Feature: Registration functionality

  Background:
    Given User launched the registration page

  Scenario: User can register using his first name, last name, e-mail address and a preferred password
    Given User is not registered
    And User is not logged in
    When User enters his first name, last name, email and password
    And User clicks on the 'Register' button
    Then User account is created
    And Message stating 'Account is successfully registered' is shown

  Scenario: User will receive a warning message if tries to register while logged in
    Given User is logged in
    When User clicks on the 'Register account' button
    Then User receives a warning message stating 'You are already logged in, log off to register another account'

  Scenario Outline: Account Registration
    Given User is not registered
    And User is not logged in
    When User enters the following information:
    * His <first_name>
    * <last_name>
    * <email>
    * <password>
    And User clicks on the 'Register' button
    Then User account is created
    And Message stating 'Account is successfully registered' is shown

    Examples:
      |first_name|last_name|email       |password|
      |Bob       |Smith    |bs@test.com |testp4sw|
      |Marietta  |Clever   |mc@test.com |qwerty12|
      |Douglas   |Wilson   |dw@gmail.com|lkdjsf41|