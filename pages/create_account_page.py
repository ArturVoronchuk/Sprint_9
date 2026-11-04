from locators import create_account_page_locators
from pages.base_page import BasePage


class CreateAccountPage(BasePage):

    def enter_first_name(self, first_name):
        self.send_keys(
            create_account_page_locators.FIRST_NAME_FIELD,
            first_name
        )
        return self

    def enter_last_name(self, last_name):
        self.send_keys(
            create_account_page_locators.LAST_NAME_FIELD,
            last_name
        )
        return self

    def enter_username(self, username):
        self.send_keys(
            create_account_page_locators.USERNAME_FIELD,
            username
        )
        return self

    def enter_email(self, email):
        self.send_keys(
            create_account_page_locators.EMAIL_FIELD,
            email
        )
        return self

    def enter_password(self, password):
        self.send_keys(
            create_account_page_locators.PASSWORD_FIELD,
            password
        )
        return self

    def click_to_signup_btn(self):
        self.click_to_element(create_account_page_locators.SIGNUP_BUTTON)
        return self
