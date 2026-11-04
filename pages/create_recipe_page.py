from helpers.path import get_asset_path
from locators import create_recipe_page_locators
from pages.base_page import BasePage

class CreateRecipePage(BasePage):

    def enter_recipe_name(self, name):
        self.send_keys(
            create_recipe_page_locators.RECIPE_NAME_FIELD,
            name
        )
        return self

    def select_tag_lunch(self):
        self.click_to_element(create_recipe_page_locators.TAG_LUNCH)
        return self

    def select_tag_dinner(self):
        self.click_to_element(create_recipe_page_locators.TAG_DINNER)
        return self

    def enter_ingredient_name(self, name):
        self.send_keys(create_recipe_page_locators.INGREDIENT_NAME_FIELD, name)
        return self

    def select_ingredient_from_dropdown(self, name):
        self.click_to_element(create_recipe_page_locators.ingredient_option(name))
        return self

    def enter_ingredient_amount(self, amount):
        self.send_keys(create_recipe_page_locators.INGREDIENT_AMOUNT_FIELD, amount)
        return self

    def click_add_ingredient_btn(self):
        self.click_to_element(create_recipe_page_locators.ADD_INGREDIENT_BTN)
        return self

    def enter_cooking_time(self, time):
        self.send_keys(
            create_recipe_page_locators.COOKING_TIME_FIELD,
            time
        )
        return self

    def enter_description(self, description):
        self.send_keys(create_recipe_page_locators.DESCRIPTION_FIELD, description)
        return self

    def click_create_recipe_btn(self):
        self.click_to_element(create_recipe_page_locators.CREATE_RECIPE_BTN)
        return self

    def upload_image(self, filename):
        self.send_keys_to_hidden_input(
            create_recipe_page_locators.FILE_INPUT,
            get_asset_path(filename)
        )
        return self