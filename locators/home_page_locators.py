from selenium.webdriver.common.by import By

def recipe_card_by_name(recipe_name: str):
    return (
        By.XPATH,
        f'//div[contains(@class, "style_cardList")]//a[normalize-space()="{recipe_name}"]'
    )