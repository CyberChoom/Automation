Feature: Adding music to cargo bay


  Background:
    Given user is logged in
    And user launched the 'Add Music Product' page


  Scenario Outline: User can add a Music Product with filling in only required fields
    When user enters <artist_name>
    * <album_name>
    * <format>
    * <quantity>
    * <media_condition>
    * <sleeve_condition>
    * <opening_price>
    * <asking_price>
    And clicks the 'Add Product' button
    Then the Music Product is added

  Examples:
    |artist_name|album_name|format      |quantity|media_condition|sleeve_condition|opening_price|asking_price|
    |Skillet    |Awake     |CD          |1       |MT             |SLD             |1            |3           |
    |Test       |Test      |Vinyl       |2       |VG -           |NM              |2            |5           |
    |Metallica  |Reload    |Casette     |3       |G              |VG +            |3            |4           |
    |Elton John |The Union |8-Track     |5       |G +            |VG              |4            |6           |

  # Negative Scenario

  Scenario Outline: User is not able to add a Music Product if any of the required fields is not filled out
    When user enters <artist_name>
    * <album_name>
    * <format>
    * <quantity>
    * <media_condition>
    * <sleeve_condition>
    * <opening_price>
    * <asking_price>
    And clicks the 'Add Product' button
    Then the Music Product is not added, warning message: "This field is required." is shown

  Examples:
    |artist_name|album_name|format      |quantity|media_condition|sleeve_condition|opening_price|asking_price|
    |           |Awake     |CD          |1       |               |SLD             |1            |3           |
    |Test       |          |Vinyl       |2       |VG -           |NM              |             |5           |
    |Metallica  |Reload    |            |3       |G              |VG +            |3            |4           |
    |Elton John |The Union |8-Track     |        |G +            |VG              |4            |6           |
