from selenium.webdriver.common.by import By

RECIPE_NAME_FIELD = (
    By.XPATH,
    '//label[.//div[normalize-space()="Название рецепта"]]//input'
)

TAG_LUNCH = (By.XPATH, '//span[normalize-space()="Обед"]/preceding-sibling::button')
TAG_DINNER = (By.XPATH, '//span[normalize-space()="Ужин"]/preceding-sibling::button')

INGREDIENT_NAME_FIELD = (
    By.CSS_SELECTOR,
    'input.styles_ingredientsInput__1zzql'
)

INGREDIENT_DROPDOWN = (
    By.XPATH,
    '//div[contains(@class, "styles_container")]'
)

def ingredient_option(ingredient_name: str):
    return (
        By.XPATH,
        f'//div[contains(@class, "styles_container")]//div[normalize-space()="{ingredient_name}"]'
    )

INGREDIENT_AMOUNT_FIELD = (
    By.CSS_SELECTOR,
    'input.styles_ingredientsAmountValue__2matT'
)

COOKING_TIME_FIELD = (
    By.XPATH,
    '//label[.//div[normalize-space()="Время приготовления"]]//input'
)

ADD_INGREDIENT_BTN = (
    By.XPATH,
    '//div[normalize-space()="Добавить ингредиент"]'
)

DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'textarea.styles_textareaField__1wfhC')

FILE_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')

CREATE_RECIPE_BTN = (
    By.XPATH,
    '//button[normalize-space()="Создать рецепт"]'
)