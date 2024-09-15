# test_skillbox_courses_selection.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_skillbox_courses_selection(web_driver_setup):
    driver = web_driver_setup
    test_name = "test_skillbox_courses_selection"
    driver.get("https://skillbox.ru/code/")

    try:
        # Выбор типа обучения
        education_type_radio = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='#app']/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/ul/li[2]/label/span"))
        )
        education_type_radio.click()

        # Указание длительности курса
        duration_slider_6_months = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id='#app']/main/div[1]/div[2]/div/div[1]/div[1]/div[5]/div[2]/div[2]/div/div[2]/button"))
        )
        duration_slider_6_months.click()

        duration_slider_12_months = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id='#app']/main/div[1]/div[2]/div/div[1]/div[1]/div[5]/div[2]/div[2]/div/div[3]/button"))
        )
        duration_slider_12_months.click()

        # Выбор тематики
        theme_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id='#app']/main/div[1]/div[2]/div/div[1]/div[1]/div[5]/div[2]/div[2]/div/div[3]/button"))
        )
        theme_checkbox.click()

        # Переход на страницу конкретного курса
        course_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id='#app']/main/div[1]/div[2]/div/div[1]/div[1]/div[5]/div[2]/div[2]/div/div[3]/button"))
        )
        course_link.click()





    except Exception as e:
        print(e)



