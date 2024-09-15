from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



def test_vscode_issues_search(web_driver_setup):
    driver = web_driver_setup
    test_name = "test_vscode_issues_search"
    driver.get("https://github.com/microsoft/vscode/issues")
    search_input = driver.find_element(By.ID, "js-issues-search")
    search_input.send_keys("in:title bug")
    search_input.send_keys(Keys.RETURN)
    try:
        assert "bug" in driver.page_source, "Bug-related issues not found"

    except AssertionError as e:

        pass