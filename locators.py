from selenium.webdriver.common.by import By

class AuthLocators:
    OPEN_AUTH_BUTTON = (By.XPATH, "//button[normalize-space()='Вход и регистрация']")

    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Нет аккаунта']")
    SUBMIT_REGISTER_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Создать аккаунт']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Войти']")

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")

class HeaderLocators:
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Выйти']")

    CREATE_AD_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space()='Разместить объявление']")

class RegistrationErrorLocators:
    EMAIL_ERROR_TEXT = (By.XPATH, "//span[normalize-space()='Ошибка']")

    EMAIL_ERROR_BORDER = (By.XPATH, "//input[@name='email']/ancestor::div[contains(@class,'input_inputError')]")
    PASSWORD_ERROR_BORDER = (By.XPATH, "//input[@name='password']/ancestor::div[contains(@class,'input_inputError')]")
    REPEAT_PASSWORD_ERROR_BORDER = (By.XPATH, "//input[@name='submitPassword']/ancestor::div[contains(@class,'input_inputError')]")

class AdLocators:
    UNAUTHORIZED_MODAL_TITLE = (By.XPATH, "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']")

class AdCreateLocators:
    # поля формы
    TITLE_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")

    # категория
    CATEGORY_ARROW_BUTTON = (By.XPATH, "//input[@name='category']/following::button[1]")
    CATEGORY_OPTION = (By.XPATH, "//button[.//span[normalize-space()='Технологии']]")

    # город
    CITY_ARROW_BUTTON = (By.XPATH, "//input[@name='city']/following::button[1]")
    CITY_OPTION = (By.XPATH, "//button[normalize-space()='Нижний Новгород']")

    # состояние
    CONDITION_LABEL = (By.XPATH, "//label[normalize-space()='Б/У']")

    # publish
    PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Опубликовать']")

    # профиль / проверка
    MY_ADS_TITLE = (By.XPATH, "//h1[normalize-space()='Мои объявления']")
    TITLE_IN_PROFILE = (By.XPATH, "//h1[normalize-space()='Мои объявления']/following::h2[normalize-space()='Палочка Гарри Поттера'][1]")