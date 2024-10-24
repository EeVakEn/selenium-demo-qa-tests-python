# Написать 2 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Elements'
# 3. Выбрать пункт 'Check Box'
# 4. Нажать на +
# 5. Поставить чек боксы на пункты: Notes, Veu, Private
# 6. Нажать -


import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckBox(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.wait = WebDriverWait(self.driver, 10)
        # 1. Перейти на страницу https://demoqa.com/
        self.driver.get("https://demoqa.com/")

    def test_check_box(self):
        
        # 2. Перейти в раздел 'Elements'
        elements_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
        elements_section.click()
        
        # 3. Выбрать пункт 'Check Box'
        check_box_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Check Box']")))
        check_box_option.click()

        # 4. Нажать на +
        plus_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Expand all']")))
        plus_button.click()

        

        # 5. Поставить чек боксы на пункты: Notes, Veu, Private
        notes_title = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Notes" and @class="rct-title"]')))
        notes_title.click()

        

        veu_title = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Veu" and @class="rct-title"]')))
        veu_title.click()

        

        private_title = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Private" and @class="rct-title"]')))
        private_title.click()

        

        # 6. Нажать -
        minus_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Collapse all']")))
        minus_button.click()

        

        # Проверка, что чекбоксы выбраны
        result = self.wait.until(EC.visibility_of_element_located((By.ID, 'result')));
        self.assertTrue(result.find_element(By.XPATH, '//span[text()="notes"]'))
        self.assertTrue(result.find_element(By.XPATH, '//span[text()="veu"]'))
        self.assertTrue(result.find_element(By.XPATH, '//span[text()="private"]'))


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
