Feature: Laptops page functionality


  Background:
    Given User launched "Laptops & Notebooks" page

  Scenario Outline: User can access the page of every product listed on this page
    When User clicks on <laptop> thumbnail
    Then The <laptop> page is open

  Examples:
    |laptop     |
    |HP LP3065  |
    |MacBook    |
    |MacBook Air|
    |MacBook Pro|
    |Sony VAIO  |

  Scenario Outline: User can change the grid/list view of the page
    When User clicks on <view>
    Then Page view changes to the <view> option
    And All the products are visible

  Examples:
    |view|
    |list|
    |grid|

  Scenario: User can successfully sort items by Name(A-Z)
    When User clicks on "Sort By" dropdown
    And User chooses "Name(A-Z)" option
    Then All the items on the page are sorted by name