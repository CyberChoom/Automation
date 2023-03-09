Feature: Error messages during registration process


  Scenario Outline: enter in "<field>" "<type>" value
    Given user is on the registration page
    When user types "<value>" in "<field>"
    And user clicks Continue button
    Then error is shown under "<field>" field

  Examples:
    | field       | type  | value                             |
    | first_name  | short | None                              |
    | last_name   | short | None                              |
    | first_name  | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |
    | last_name   | long  | abcdeabcdeabcdeabcdeabcdeabcdeabc |
    | phonenumber | short | 12                                |
    | phonenumber | long  | 123456789123456789123456789123456 |
    | password    | short | Aa1                               |
    | password    | long  | 123456789123456789aAs             |
    | email       | short | None                              |
    | email       | long  | iljhasdfk2324.fe                  |
    | address_1   | short | wt                                |
    | address_1   | long  | dfgkjhwdfligheiughelkrjhgieurh9374y9uhfd8yg87ewyrg987y34iuhlkrjhlgkshdflgjhlskdfjhgifgh95yt9349gisudfhgilhesgiuherg973ygiu9op3e4g |
    | city        | short | X                                 |
    | city        | long  | jhsdfbgkjsdhbfgkjshdbg83yg83yg83ygjfhgbjkhgbuhgHJGUYGuy8yg8yg8ygre8gy8yg8y287t2386t3ghjdsjfhjsdhgfjhsdfgig874g8g211111111husdhgfh |
