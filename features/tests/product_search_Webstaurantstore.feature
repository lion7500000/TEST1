# Created by Andrey at 1/26/2020
Feature: Test for Webstaurantstore search functionality

  Scenario: User can serach a products
    Given Open Webstaurantstore page
    When Search for stainless work table
    And Click serch_btn
    Then Verify word Table its title
    And Add the last of found items to Cart
    Then Open card_btn
    Then Click_empty_cart
    And Click_comfirm_empty_btn
    Then Verify text cart has 0 item


