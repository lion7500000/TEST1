from time import sleep

from selenium.webdriver.common.by import By
from behave import given,when, then


@given ('Open Webstaurantstore page')
def open_Webstaurantstore_page (context):
    #context.driver.get('https://www.webstaurantstore.com/')
    context.app.main_page.open_page()

@when ('Search for {text}')
def serch_product(context, text):
    context.app.main_page.search_items(text)

@when ('Click serch_btn')
def click_btn (context):
    context.app.main_page.click_btn()

@then ('Verify word {text} its title')
def verify_text(context, text):
    # locator add in base_page verify_search_item
    context.app.search_page.verify_tect(text)

@then ('Add the last of found items to Cart')
def add_last_item(context):
    context.app.search_page.add_last_item()
    #problem here. Need use sleep
    sleep(8)
@then ('Wait_btn_to_be_clickable')
def wait_btn_be_clicable(context):
    context.app.search_page.wait_btn_be_clicable()
    #context.app.search_page.wait_invisibility_element()
    #context.app.search_page.visibility_btn()
@then ('Open card_btn')
def open_cart_btn(context):
    context.app.cart_page.open_cart_btn()
    #sleep(10)
@then ('Click_empty_cart')
def click_empty_btn(context):
    context.app.cart_page.click_empty_btn()
    sleep(3)
@then ('Click_comfirm_empty_btn')
def click_comfirm_empty (context):
    context.app.cart_page.click_comfirm_empty()
    sleep(3)
@then ('Verify text cart has {text} item')
def verify_cart_empty (context,text):
    context.app.cart_page.verify_cart_empty(text)





