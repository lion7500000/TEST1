from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):

    CART_BTN = (By.CSS_SELECTOR, "span.btn-primary")
    EMPTY_CART_BTN = (By.CSS_SELECTOR, "a.emptyCartButton")
    #CONFIRM_EMPTY_CART_BTN = (By.CSS_SELECTOR, "div.modal-footer button.btn-primary")
    CONFIRM_EMPTY_CART_BTN = (By.XPATH,"//button[@class='btn btn-primary'and starts-with(text(),'Empty Cart')]")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "span.btn-glass-cart")
#"p.header-1"

    def open_cart_btn(self):
        #self.wait_for_element_to_be_clickable( *self.CART_BTN )
        #self.ivisibility_of_element(*self.CART_BTN)
        self.click(*self.CART_BTN)

    def click_empty_btn(self):
        self.click(*self.EMPTY_CART_BTN)
        #BTN = self.driver.find_elements(*self.CONFIRM_EMPTY_CART_BTN)[2].click()
        #self.wait_for_element_to_be_clickable(*BTN)

    def click_comfirm_empty(self):
        self.click(*self.CONFIRM_EMPTY_CART_BTN)

    def verify_cart_empty(self,text):
        self.verify_text(text,*self.EMPTY_CART_TEXT)

