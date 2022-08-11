Feature: Registration functionality


  Background:
    Given user launched the registration page

  Scenario: User can register using his first name, last name, e-mail address and a preferred password
    Given user is not registered
    And user is not logged in
    When user enters his first name, last name, email and password
    And user clicks on the 'Register' button
    Then user account is created
    And message stating 'Account is successfully registered' is shown

  Scenario: User will receive a warning message if tries to register while logged in
    Given user is logged in
    When user clicks on the 'Register account' button
    Then user receives a warning message stating 'You are already logged in, log off to register another account'

  Scenario Outline: Account Registration
    Given user is not registered
    And user is not logged in
    When user enters his <first_name>
    * <last_name>
    * <email>
    * <password>
    And user clicks on the 'Register' button
    Then user account is created
    And message stating 'Account is successfully registered' is shown

    Examples:
      |first_name|last_name|email       |password|
      |Bob       |Smith    |bs@test.com |testp4sw|
      |Marietta  |Clever   |mc@test.com |qwerty12|
      |Douglas   |Wilson   |dw@gmail.com|lkdjsf41|