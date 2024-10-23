# Написать 14 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Widgets'
# 3. Выбрать пункт 'Accordian'
# 4. Раскрыть аккордион 'What is Lorem Ipsum?'
# 5. Проверить наличие текста
# 6. Раскрыть аккордион 'Where does it come from?'
# 7. Проверить наличие текста
# 8. Раскрыть аккордион 'Why do we use it?'
# 9. Проверить наличие текста

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQAAccordian(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_accordion(self):
        # 2. Перейти в раздел 'Widgets'
        widgets_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']")))
        widgets_section.click()

        # 3. Выбрать пункт 'Accordian'
        accordion_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Accordian']")))
        accordion_tab.click()

        # 4. Раскрыть аккордион 'What is Lorem Ipsum?'
        section_1_header = self.driver.find_element(By.CSS_SELECTOR, "#section1Heading")
        section_1_header.click()

        # 5. Проверить наличие текста
        section_1_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#section1Content>p"))).text
        assert section_1_text != '', "Текст в разделе 'What is Lorem Ipsum?' пустой."

        # 6. Раскрыть аккордион 'Where does it come from?'
        section_2_header = self.driver.find_element(By.CSS_SELECTOR, "#section2Heading")
        section_2_header.click()

        # 7. Проверить наличие текста
        section_2_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#section2Content>p"))).text
        assert section_2_text != '', "Текст в разделе 'Where does it come from?' пустой."

        # 8. Раскрыть аккордион 'Why do we use it?'
        section_3_header = self.driver.find_element(By.CSS_SELECTOR, "#section3Heading")
        section_3_header.click()

        # 9. Проверить наличие текста
        section_3_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#section3Content>p"))).text
        assert section_3_text != '', "Текст в разделе 'Why do we use it?' пустой."


    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()

