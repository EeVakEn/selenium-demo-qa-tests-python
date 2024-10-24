# Написать 3 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Elements'
# 3. Выбрать пункт 'Radio Button'
# 4. Выбрать Yes
# 5. Проверить что появилась надпись Yes
# 6. Выбрать Impressive
# 7. Проверить что появилась надпись Impressive
# 8. Проверить что кнопка No недоступна

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRadioButton(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_radio_button(self):
        # 2. Перейти в раздел 'Elements'
        elements_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
        elements_section.click()
        
        # 3. Выбрать пункт 'Radio Button'
        radio_button_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Radio Button']")))
        radio_button_option.click()

        # 4. Выбрать Yes
        yes_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='yesRadio']")))
        yes_option.click()

        

        # 5. Проверить, что появилась надпись Yes
        yes_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Yes']")))
        self.assertTrue(yes_text.is_displayed())

        

        # 6. Выбрать Impressive
        impressive_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='impressiveRadio']")))
        impressive_option.click()

        

        # 7. Проверить, что появилась надпись Impressive
        impressive_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Impressive']")))
        self.assertTrue(impressive_text.is_displayed())

        

        # 8. Проверить, что кнопка No недоступна
        no_radio = self.driver.find_element(By.ID, "noRadio")
        self.assertFalse(no_radio.is_enabled())

        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
