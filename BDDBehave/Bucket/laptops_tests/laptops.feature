Feature: Laptops page functionality


  Background:
    Given user launched "Laptops & Notebooks" page

  @access_all
  Scenario Outline: User can access the page of every product listed on this page
    When user clicks on "<laptop>" thumbnail
    Then the "<laptop>" page is open

  Examples:
    |laptop     |
    |HP LP3065  |
    |MacBook    |
    |MacBook Air|
    |MacBook Pro|
    |Sony VAIO  |

  @view
  Scenario Outline: User can change the grid/list view of the page
    When user clicks on "<view>"
    Then page view changes to the "<view>" option
    And all the products are visible

  Examples:
    |view|
    |list|
    |grid|

  @sort
  Scenario: User can successfully sort items by Name(A-Z)
    When user clicks on "Sort By" dropdown
    And user chooses "Name(A-Z)" option
    Then all the items on the page are sorted by name