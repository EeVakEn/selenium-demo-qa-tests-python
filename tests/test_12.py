# Написать 12 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Alerts, Frame & Windows'
# 3. Выбрать пункт 'Nested Frames'
# 4. Проверить наличие текста 'Child Iframe' в 1 frame
# 5. Проверить наличие текста 'Parent frame' в 2 frame


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQANestedFrames(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options) 
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_nested_frames(self):
        # 2. Перейти в раздел 'Alerts, Frame & Windows'
        alerts_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))
        alerts_section.click()

        # 3. Выбрать пункт 'Nested Frames'
        nested_frames_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Nested Frames']")))
        nested_frames_tab.click()

        # 4. Проверить наличие текста 'Child Iframe' в child frame
        # Переход в родительский фрейм по его имени или ID
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "frame1"))

        # Переход во вложенный (child) фрейм
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))
        child_frame_text = self.driver.find_element(By.TAG_NAME, "p").text
        assert child_frame_text == "Child Iframe", f"Unexpected text in child frame: {child_frame_text}"

        # Возврат к родительскому фрейму
        self.driver.switch_to.parent_frame()

        # 5. Проверить наличие текста 'Parent frame' в parent frame
        parent_frame_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Parent frame" in parent_frame_text, f"Unexpected text in parent frame: {parent_frame_text}"

        # Возврат к основному контенту страницы
        self.driver.switch_to.default_content()

    def tearDown(self):
        self.driver.quit()


# Запуск теста
if __name__ == "__main__":
    unittest.main()

