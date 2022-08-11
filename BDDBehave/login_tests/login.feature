Feature: Login functionality


  Background:
    Given user launch login page

  Scenario: A user can login using correct email and password
    Given user is not logged in
    When user enters email and password
    And user clicks Login button
    Then the user's profile page will be launched

  Scenario: User can't login without entering password
    Given user is not logged in
    When user enters email
    And user clicks Login button
    Then warning will be shown about 'No match for E-Mail Address and/or Password'
