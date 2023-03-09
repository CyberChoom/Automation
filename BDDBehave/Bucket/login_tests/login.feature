Feature: Login functionality


  Background:
    Given user launched the login page

  @negative
  Scenario Outline: User can't login without entering password/email
    Given user is not logged in
    When user types "<value>" in "<field>"
    And user clicks Login button
    Then warning is shown "Warning: No match for E-Mail Address and/or Password."

      Examples:
    | field    | value |
    | email    | None  |
    | password | None  |

