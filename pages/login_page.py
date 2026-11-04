from locators import login_page_locators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def wait_login_form_visible(self, timeout=15):
        self.wait_element_visible(login_page_locators.LOGIN_BUTTON, timeout)
        return self

    def is_login_form_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_BUTTON)

    def enter_email(self, first_name):
        self.send_keys(
            login_page_locators.LOGIN_EMAIL_FIELD,
            first_name
        )
        return self

    def enter_password(self, last_name):
        self.send_keys(
            login_page_locators.LOGIN_PASSWORD_FIELD,
            last_name
        )
        return self

    def click_login_button(self):
        self.click_to_element(login_page_locators.LOGIN_BUTTON)
        return self
