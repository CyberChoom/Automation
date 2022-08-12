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