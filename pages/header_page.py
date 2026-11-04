from locators import header_page_locators
from pages.base_page import BasePage

class HeaderPage(BasePage):

    def click_to_header_create_account_btn(self):
        self.click_to_element(header_page_locators.HEADER_CREATE_ACCOUNT_BTN)
        return self

    def click_to_header_login_btn(self):
        self.click_to_element(header_page_locators.HEADER_LOGIN_BTN)
        return self

    def wait_logout_btn_visible(self, timeout=15):
        self.wait_element_visible(header_page_locators.HEADER_LOGOUT_BTN, timeout)
        return self

    def is_logout_btn_visible(self):
        return self.is_element_present(header_page_locators.HEADER_LOGOUT_BTN)

    def click_create_recipe_btn(self):
        self.click_to_element(header_page_locators.HEADER_CREATE_RECIPE_BTN)
        return self
