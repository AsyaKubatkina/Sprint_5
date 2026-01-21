from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import AuthLocators
from locators import HeaderLocators
from locators import RegistrationErrorLocators


class TestRegistration:
    def test_user_can_register(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        # Проверка: отображается User и аватар
        user_text = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_NAME)).text
        assert user_text == "User."
        assert wait.until(EC.visibility_of_element_located(HeaderLocators.AVATAR_BUTTON)).is_displayed()

    def test_registration_with_invalid_email_shows_error(self, driver):
        wait = WebDriverWait(driver, 10)

        # Открыть форму регистрации
        wait.until(EC.element_to_be_clickable(AuthLocators.OPEN_AUTH_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()

        # Ввести невалидный email и отправить форму
        wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys("123@")
        wait.until(EC.element_to_be_clickable(AuthLocators.SUBMIT_REGISTER_BUTTON)).click()

        # Проверки: ошибка под Email и красная подсветка у 3 полей
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.EMAIL_ERROR_TEXT)).text == "Ошибка"
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.EMAIL_ERROR_BORDER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.PASSWORD_ERROR_BORDER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.REPEAT_PASSWORD_ERROR_BORDER)).is_displayed()

    def test_registration_existing_user_shows_error(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        email = registered_user["email"]
        password = registered_user["password"]

        # Выходим
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()

        # Пытаемся зарегистрироваться тем же email ещё раз
        wait.until(EC.element_to_be_clickable(AuthLocators.OPEN_AUTH_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)).send_keys(email)
        wait.until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.visibility_of_element_located(AuthLocators.REPEAT_PASSWORD_INPUT)).send_keys(password)
        wait.until(EC.element_to_be_clickable(AuthLocators.SUBMIT_REGISTER_BUTTON)).click()

        # Проверки: "Ошибка" и красные поля
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.EMAIL_ERROR_TEXT)).text == "Ошибка"
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.EMAIL_ERROR_BORDER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.PASSWORD_ERROR_BORDER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(RegistrationErrorLocators.REPEAT_PASSWORD_ERROR_BORDER)).is_displayed()