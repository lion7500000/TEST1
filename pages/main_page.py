from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    SERCH_ICON=(By.ID, 'searchval')
    SERCH_BTN= (By.CSS_SELECTOR, "button.banner-search-btn")

    def open_page(self):
        self.driver.get(self.base_url)

    def search_items(self, text):
        self.input_text(text,*self.SERCH_ICON)

    def click_btn(self):
        self.click (*self.SERCH_BTN)








