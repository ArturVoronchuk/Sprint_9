from selenium.webdriver.common.by import By

HEADER_CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, 'a[href="/signup"]')
HEADER_LOGIN_BTN = (By.CSS_SELECTOR, 'a[href="/signin"]')
HEADER_LOGOUT_BTN = (By.XPATH, '//a[normalize-space()="Выход"]')
HEADER_CREATE_RECIPE_BTN = (By.CSS_SELECTOR, 'a[href="/recipes/create"]')
