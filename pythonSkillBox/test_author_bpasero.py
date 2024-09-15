from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_author_bpasero_issues(web_driver_setup):
    driver = web_driver_setup
    driver.get("https://github.com/microsoft/vscode/issues")
    print("Страница загружена")

    # Ожидание появления элемента и нажатие на него
    author_select_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='author-select-menu']/summary/span"))
    )
    author_select_menu.click()
    print("Нажато на элемент author-select-menu")

    # Ожидание появления поля для ввода и установка курсора
    author_filter_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='author-filter-field']"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(author_filter_field).click().send_keys("bpasero").perform()
    print("Введено bpasero и нажата Enter")