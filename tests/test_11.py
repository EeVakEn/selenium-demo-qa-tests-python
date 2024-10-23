# Написать 11 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Alerts, Frame & Windows'
# 3. Выбрать пункт 'Frames'
# 4. Проверить наличие текста 'This is a sample page' в 1 frame
# 5. Проверить наличие текста 'This is a sample page' в 2 frame


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQAFrames(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options) 
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_frames(self):
        # 2. Перейти в раздел 'Alerts, Frame & Windows'
        alerts_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))
        alerts_section.click()

        # 3. Выбрать пункт 'Frames'
        frames_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Frames']")))
        frames_tab.click()

        # 4. Проверить наличие текста 'This is a sample page' в 1 frame
        # Переход в первый фрейм по ID
        self.driver.switch_to.frame("frame1")
        frame1_text = self.wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading"))).text
        assert frame1_text == "This is a sample page", f"Unexpected text in Frame 1: {frame1_text}"

        # Возврат к основному контенту страницы
        self.driver.switch_to.default_content()

        # 5. Проверить наличие текста 'This is a sample page' в 2 frame
        # Переход во второй фрейм по ID
        self.driver.switch_to.frame("frame2")
        frame2_text = self.wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading"))).text
        assert frame2_text == "This is a sample page", f"Unexpected text in Frame 2: {frame2_text}"

        # Возврат к основному контенту страницы
        self.driver.switch_to.default_content()

    def tearDown(self):
        self.driver.quit()


# Запуск теста
if __name__ == "__main__":
    unittest.main()

