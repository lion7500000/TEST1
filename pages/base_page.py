from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Page:

    TEXT_IN_ITEMS = (By.CSS_SELECTOR, "div a.description")

    def __init__ (self, driver):
        self.driver = driver
        self.base_url = 'https://www.webstaurantstore.com/'
        self.wait = WebDriverWait(self.driver,15)
        self.action = ActionChains(self.driver)

    def input_text (self, text, *locator):
        serch_icon = self.driver.find_element (*locator)
        serch_icon.clear()
        serch_icon.send_keys(text)

    def click (self, *locator):
        self.driver.find_element(*locator).click()

    def serch_items (self, *locator):
        self.driver.find_elements(*locator)

    def  add_to_cart_last_item(self, *locator):
        self.driver.find_elements( *locator )[-1].click()

    def verify_search_item (self, text, *locator):
        TEXT_IN_ITEMS = (By.CSS_SELECTOR, "div a.description")
        products = self.driver.find_elements(*locator)
        for product in products:
            title = product.find_element(*TEXT_IN_ITEMS)
            assert text in title.text, f'Expected {text}, but got {title}'

    def wait_for_element_to_be_clickable(self,*locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator))

    def visibility_of_element (self, *locator):
        self.driver.wait.until(EC.visibility_of_element_located (locator))

    def invisibility_of_element(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element (locator))

    def action_btn(self,*locator):
        Menu = self.driver.find_element( *locator )
        self.action.move_to_element(Menu).perform()

    def verify_text(self, expected_text,*locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, bot got {actual_text}'

