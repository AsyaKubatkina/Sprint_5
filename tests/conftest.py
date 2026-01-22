import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from locators import AuthLocators, HeaderLocators
from data import generate_email, PASSWORD

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(BASE_URL)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def registered_user(driver):
    wait = WebDriverWait(driver, 10)

    email = generate_email()
    password = PASSWORD

    wait.until(EC.element_to_be_clickable(AuthLocators.OPEN_AUTH_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()

    wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys(email)
    wait.until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.visibility_of_element_located(AuthLocators.REPEAT_PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(AuthLocators.SUBMIT_REGISTER_BUTTON)).click()

    wait.until(EC.visibility_of_element_located(HeaderLocators.AVATAR_BUTTON))
    return {"email": email, "password": password}