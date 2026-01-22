from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import AuthLocators, HeaderLocators


class TestLogout:
    def test_user_can_logout(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        # Нажать "Выйти"
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()

        # Проверка: снова видна кнопка "Вход и регистрация"
        assert wait.until(EC.visibility_of_element_located(AuthLocators.OPEN_AUTH_BUTTON)).is_displayed()