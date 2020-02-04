from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchPage( Page ):
    CHOSE_ITEMS = (By.CSS_SELECTOR, "div.ag-item.gtm-product")
    #TEXT_IN_ITEMS = (By.CSS_SELECTOR, "div a.description")
    CART_BTNS = (By.CSS_SELECTOR, "div input.btn-cart")
    CART_BTN = (By.CSS_SELECTOR, "span.btn-primary")
    NOTIFICATION = (By.CSS_SELECTOR, "div.notification-center")

    def verify_tect(self,serch_word):
        self.verify_search_item (serch_word, *self.CHOSE_ITEMS)

    def add_last_item(self):
        self.add_to_cart_last_item(*self.CART_BTNS)

    def wait_btn_be_clicable (self):
        self.wait_for_element_to_be_clickable( *self.CART_BTN )

    def wait_invisibility_element (self):
        self.invisibility_of_element(*self.NOTIFICATION)

    def visibility_btn (self):
        self.visibility_of_element(*self.CART_BTN)
