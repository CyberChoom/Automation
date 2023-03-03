Feature: Registration functionality


  Background:
    Given user launched the registration page

  @positive @wip
  Scenario Outline: Account Registration
    When user enters his "<first_name>" in the First Name field
    And "<last_name>" in the Last Name field
    And "<email>" in the E-Mail field
    And "<phone>" in the Telephone field
    And "<address>" in the Address 1 field
    And "<city>" in the City field
    And "<country>" in the Country field
    And "<state>" in the Region / State field
    And "<password>" in the Password field
    And "<password>" in the Password Confirm field
    And user clicks on the "Privacy Policy" checkbox
    And user clicks on the "Register" button
    Then user account is created, message stating "Your Account Has Been Created!" is shown

  Examples:
      |first_name|last_name|email       |phone  |password  |address |city       |country      |state  |
      |Bob       |Smith    |czr@test.com|1234561|testp4sw  |12 Red  |Bobtown    |United States|Georgia|
      |Douglas   |Wilson   |dz@gmail.com|09876  |lk4dj7sf41|45 Colt |Chersonesos|Ukraine      |Crimea |

  @negative
  Scenario Outline: User will not be able to register if the 'Privacy Policy' checkbox is not ticked
    When user enters his "<first_name>" in the First Name field
    And "<last_name>" in the Last Name field
    And "<email>" in the E-Mail field
    And "<phone>" in the Telephone field
    And "<address>" in the Address 1 field
    And "<city>" in the City field
    And "<country>" in the Country field
    And "<state>" in the Region / State field
    And "<password>" in the Password field
    And "<password>" in the Password Confirm field
    And user clicks on the "Register" button
    Then user account is not created, message stating "Warning: You must agree to the Privacy Policy!" is shown

  Examples:
      |first_name|last_name|email        |phone|password  |address   |city    |country      |state   |
      |John      |Markus   |mtcv@test.com|1234522|testp4sw|11 Good st|Racetown|United States|New York|
