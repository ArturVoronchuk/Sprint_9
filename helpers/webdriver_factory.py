from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class WebdriverFactory:
    @staticmethod
    def get_webdriver(headless, remote_url=None):
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        if remote_url:
            return webdriver.Remote(
                command_executor=remote_url,
                options=options
            )
        return webdriver.Chrome(options=options)