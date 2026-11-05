from selenium.webdriver.common.by import By

FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="first_name"]')
LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="last_name"]')
USERNAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')

SIGNUP_BUTTON = (By.XPATH, '//button[normalize-space()="Создать аккаунт"]')
