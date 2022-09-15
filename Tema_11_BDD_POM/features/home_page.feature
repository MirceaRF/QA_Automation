Feature: Testing scenarios on herokuap

  Scenario: I am on herokuap and I want to login
    Given Home Page I am on herokuap homepage
    When Home Page I want to complete username as 'tomsmith' and password as 'SuperSecretPassword!'
    Then Home Page I should be able to login


# Scenario Outline: I am on herokuap and I want to check that i cannot login if i add a username or password incorrect
#    Given Home Page I am on herokuap homepage
#    When Home Page I want to complete username as '<username>' and password as '<password>'
#    Then Home Page I should not be able to login
#   Examples:
#     | username | password |
#     | tomsmith  | parola   |
#     | Mircea   |  SuperSecretPassword!|
#     |Mircea    |  parola               |
