import pytest
import os
import urls
from helpers import webdriver_factory
from helpers.user_generator import UserGenerator
from pages.create_account_page import CreateAccountPage
from pages.header_page import HeaderPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.create_recipe_page import CreateRecipePage

@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--remote-url",
        action="store",
        default=None,
        help="URL of Selenoid (e.g. http://selenoid:4444/wd/hub)"
    )

@pytest.fixture(scope="function")
def driver(request):
    headless = request.config.getoption("--headless")
    remote_url = (
        request.config.getoption("--remote-url")
        or os.getenv("SELENIUM_REMOTE_URL")
    )
    driver = webdriver_factory.WebdriverFactory.get_webdriver(
        headless=headless,
        remote_url=remote_url
    )
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    page = HomePage(driver)
    return page

@pytest.fixture(scope="function")
def login_page(driver):
    page = LoginPage(driver)
    page.go_to_url(urls.SIGNIN_URL)
    return page

@pytest.fixture(scope="function")
def header_page(driver):
    page = HeaderPage(driver)
    return page

@pytest.fixture(scope="function")
def create_account_page(driver):
    page = CreateAccountPage(driver)
    return page

@pytest.fixture(scope="function")
def generate_user_payload():
    payload = UserGenerator.generate_user_payload()
    return payload

@pytest.fixture(scope="function")
def create_recipe_page(driver):
    page = CreateRecipePage(driver)
    page.go_to_url(urls.RECIPES_URL)
    return page
