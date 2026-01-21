from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import AuthLocators, HeaderLocators


class TestLogin:
    def test_user_can_login(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        email = registered_user["email"]
        password = registered_user["password"]

        # Выходим
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.OPEN_AUTH_BUTTON))

        # Логинимся тем же пользователем
        wait.until(EC.element_to_be_clickable(AuthLocators.OPEN_AUTH_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(AuthLocators.SUBMIT_LOGIN_BUTTON)).click()

        # Проверка: User. и аватар отображаются
        user_text = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        assert user_text == "User."

        assert wait.until(EC.visibility_of_element_located(HeaderLocators.AVATAR_BUTTON)).is_displayed()