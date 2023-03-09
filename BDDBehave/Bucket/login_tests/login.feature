Feature: Login functionality


  Background:
    Given user launched the login page

  @negative
  Scenario: User can't login without entering password
    Given user is not logged in
    When user enters email
    And user clicks Login button
    Then warning is shown: "No match for E-Mail Address and/or Password"

  @negative @skip
  Scenario: User can't login without entering email
    Given user is not logged in
    When user enters password
    And user clicks Login button
    Then warning is shown: "No match for E-Mail Address and/or Password"
