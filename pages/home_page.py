from selenium.common import TimeoutException

import urls
from locators import home_page_locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class HomePage(BasePage):

    def go_to_main_page_url(self):
        self.go_to_url(urls.MAIN_PAGE_URL)
        return self

    def is_recipe_card_visible(self, recipe_name, timeout=10):
        try:
            self._wait(timeout).until(
                ec.visibility_of_element_located(
                    home_page_locators.recipe_card_by_name(recipe_name)
                )
            )
            return True
        except TimeoutException:
            return False

    def wait_recipe_visible(self, recipe_name, timeout=10):
        self._wait(timeout).until(
            ec.visibility_of_element_located(
                home_page_locators.recipe_card_by_name(recipe_name)
            )
        )
        return self

    def get_recipe_card_name(self, recipe_name: str):
        element = self.find_visible_element(
            home_page_locators.recipe_card_by_name(recipe_name)
        )
        return element.text.strip()