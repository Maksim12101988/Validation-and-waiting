from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_advanced_search(web_driver_setup):
    driver = web_driver_setup

    driver.get("https://github.com/search/advanced")

    try:
        # Выбор языка Python
        language_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_language"))
        )
        language_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='search_language']/optgroup[1]/option[19]"))
        )
        language_option.click()

        # Ввод количества звезд (>20000)
        stars_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_stars"))
        )
        stars_input.clear()
        stars_input.send_keys(">20000")

        # Ввод названия файла (environment.yml)
        filename_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_filename"))
        )
        filename_input.send_keys("environment.yml")

        # Нажатие кнопки поиска
        search_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#search_form > div.container-lg.p-responsive.advanced-search-form > div > div > button"))
        )
        search_button.click()

        # Проверка результата поиска
        WebDriverWait(driver, 15).until(
            EC.url_contains(
                "https://github.com/search?q=stars%3A%3E20000+path%3A**%2Fenvironment.yml+language%3APython&type=Repositories&ref=advsearch&l=Python&l=")
        )
        assert driver.current_url == "https://github.com/search?q=stars%3A%3E20000+path%3A**%2Fenvironment.yml+language%3APython&type=Repositories&ref=advsearch&l=Python&l=", "URL результата поиска не соответствует ожидаемому"
    except Exception as e:
        raise AssertionError(f"Ошибка при выполнении теста: {str(e)}")