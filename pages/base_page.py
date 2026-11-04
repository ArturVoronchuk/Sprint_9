from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def _wait(self, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def click_to_element(self, locator):
        self._wait().until(ec.element_to_be_clickable(locator)).click()
        return self

    def send_keys(self, locator, text):
        element = self._wait().until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self

    def get_current_url(self):
        return self.driver.current_url

    def is_element_present(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.5)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def find_visible_element(self, locator, timeout=None):
        return self._wait(timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_element_visible(self, locator, timeout=10):
        self._wait(timeout).until(
            ec.visibility_of_element_located(locator)
        )
        return self

    def send_keys_to_hidden_input(self, locator, text):
        element = self._wait().until(ec.presence_of_element_located(locator))
        element.send_keys(text)
        return self