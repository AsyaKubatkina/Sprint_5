from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import HeaderLocators, AdLocators


class TestCreateAd:
    def test_unauthorized_user_cannot_open_create_ad_form(self, driver):
        wait = WebDriverWait(driver, 10)

        # Нажать "Разместить объявление"
        wait.until(EC.element_to_be_clickable(HeaderLocators.CREATE_AD_BUTTON)).click()

        # Проверка: появилось модальное окно с нужным заголовком
        assert wait.until(EC.visibility_of_element_located(AdLocators.UNAUTHORIZED_MODAL_TITLE)).is_displayed()
