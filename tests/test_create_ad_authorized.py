from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import HeaderLocators, AdCreateLocators
from data import AD_TITLE, AD_PRICE, AD_DESCRIPTION

class TestCreateAdAuthorized:
    def test_authorized_user_can_create_ad(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        # Ждём, что пользователь авторизовался (появился аватар)
        wait.until(EC.visibility_of_element_located(HeaderLocators.AVATAR_BUTTON))

        # Нажимаем разместить объявление
        wait.until(EC.element_to_be_clickable(HeaderLocators.CREATE_AD_BUTTON)).click()

        # Заполнить поля
        wait.until(EC.visibility_of_element_located(AdCreateLocators.TITLE_INPUT)).send_keys(AD_TITLE)

        desc_el = wait.until(EC.visibility_of_element_located(AdCreateLocators.DESCRIPTION_TEXTAREA))
        driver.execute_script("arguments[0].scrollIntoView(true);", desc_el)
        desc_el.send_keys(AD_DESCRIPTION)

        price_el = wait.until(EC.visibility_of_element_located(AdCreateLocators.PRICE_INPUT))
        driver.execute_script("arguments[0].scrollIntoView(true);", price_el)
        price_el.send_keys(AD_PRICE)

        # Категория -> Технологии
        wait.until(EC.element_to_be_clickable(AdCreateLocators.CATEGORY_ARROW_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AdCreateLocators.CATEGORY_OPTION)).click()

        # Состояние -> Б/У
        wait.until(EC.element_to_be_clickable(AdCreateLocators.CONDITION_LABEL)).click()

        # Город -> Нижний Новгород
        wait.until(EC.element_to_be_clickable(AdCreateLocators.CITY_ARROW_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(AdCreateLocators.CITY_OPTION)).click()

        # Опубликовать
        wait.until(EC.element_to_be_clickable(AdCreateLocators.PUBLISH_BUTTON)).click()

        # Дождаться окончания submit (кнопка стала не кликабельной / исчезла)
        wait.until(EC.invisibility_of_element_located(AdCreateLocators.PUBLISH_BUTTON))

        # Прокрутить к аватару
        wait.until(EC.presence_of_element_located(HeaderLocators.AVATAR_BUTTON))
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            driver.find_element(*HeaderLocators.AVATAR_BUTTON)
        )

        # Перейти в профиль (по аватару)
        wait.until(EC.element_to_be_clickable(HeaderLocators.AVATAR_BUTTON)).click()

        # Доскроллить до "Мои объявления" и проверить наличие объявления
        my_ads = wait.until(EC.visibility_of_element_located(AdCreateLocators.MY_ADS_TITLE))
        driver.execute_script("arguments[0].scrollIntoView(true);", my_ads)

        found_title = wait.until(EC.visibility_of_element_located(AdCreateLocators.TITLE_IN_PROFILE)).text
        assert found_title == AD_TITLE


