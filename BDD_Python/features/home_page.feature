Feature: Testing scenarios on ebay.com

  Scenario: Searching product on Ebay home page
    Given I am on Ebay home page
    When I search an item
    Then I have at least 2 results returned

