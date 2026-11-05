from locators import login_page_locators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def wait_login_form_visible(self, timeout=15):
        self.wait_element_visible(login_page_locators.LOGIN_BUTTON, timeout)

    def is_login_form_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_BUTTON)

    def enter_email(self, username):
        self.send_keys(
            login_page_locators.LOGIN_EMAIL_FIELD,
            username
        )

    def enter_password(self, password):
        self.send_keys(
            login_page_locators.LOGIN_PASSWORD_FIELD,
            password
        )

    def click_login_button(self):
        self.click_to_element(login_page_locators.LOGIN_BUTTON)
