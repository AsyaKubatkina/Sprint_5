import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from locators import AuthLocators, HeaderLocators
from data import generate_user_credentials

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(BASE_URL)

    yield driver
    driver.quit()

@pytest.fixture
def user_credentials():
    return generate_user_credentials()

@pytest.fixture
def registered_user(driver, user_credentials):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable(AuthLocators.OPEN_AUTH_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()

    wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys(user_credentials["email"])
    wait.until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT)).send_keys(user_credentials["password"])
    wait.until(EC.visibility_of_element_located(AuthLocators.REPEAT_PASSWORD_INPUT)).send_keys(user_credentials["password"])
    wait.until(EC.element_to_be_clickable(AuthLocators.SUBMIT_REGISTER_BUTTON)).click()

    wait.until(EC.visibility_of_element_located(HeaderLocators.AVATAR_BUTTON))
    return user_credentials