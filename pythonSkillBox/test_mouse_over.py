import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCommitActivityGraph(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")

    def test_commit_activity_graph(self):
        # Подождем, пока загрузится график
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#commit-activity-master > svg"))
        )

        # Получаем 20-й элемент прямоугольникаt
        rect_element = self.driver.find_element(By.CSS_SELECTOR, "#commit-activity-master > svg > g > g:nth-child(20) > rect")

        # Утверждаем, что элемент присутствует и имеет ненулевую ширину
        self.assertIsNotNone(rect_element)
        self.assertGreater(rect_element.size["width"], 0)

        # Утверждаем, что элемент содержит текст/html/body/div[4]/text('commits the week of Sep 24')


