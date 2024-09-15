import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture(scope="session")
def web_driver_setup(request):
    chrome_options = Options()
    chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver = webdriver.Chrome(options=chrome_options)

    def fin():
        print("\nТесты завершены. Браузер открыт.")
        # Здесь можно добавить дополнительные действия перед закрытием браузера

    request.addfinalizer(fin)
    return driver

def pytest_configure(config):
    pass
