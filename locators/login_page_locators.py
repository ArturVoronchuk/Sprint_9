from selenium.webdriver.common.by import By

LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
LOGIN_BUTTON = (By.XPATH, '//button[normalize-space()="Войти"]')
