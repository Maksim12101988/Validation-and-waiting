import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_github_commit_activity(driver):
    # Открываем страницу GitHub
    url = "https://github.com/microsoft/vscode/graphs/commit-activity"
    driver.get(url)

    # Ждем, пока элемент будет виден и кликабелен
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#commit-activity-master > svg > g > g.bar.mini.active > rect"))
    )
    print(f"Element found: {element}")

    # Нажимаем на элемент
    try:
        element.click()
        print("Clicked successfully")
    except Exception as e:
        print(f"Error clicking element: {str(e)}")

    # Ждем появления всплывающей подсказки
    try:
        # Вариант 1: Измененный селектор
        tooltip = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'svg-tip') and contains(@class, 'n')]")))


    except TimeoutException:
        print("Tooltip not found within the specified timeout.")
        assert False

    print("Тест пройден успешно!")
