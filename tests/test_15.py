# Написать 15 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Widgets'
# 3. Выбрать пункт 'Auto Complete'
# 4. В поле 'Type multiple color names' выбрать значения: Black, Red, Magenta
# 5. В поле 'Type single color name' выбрать значения: Black
# 5. В поле 'Type single color name' заменить значения на Red

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQA_AutoComplete(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_auto_complete(self):
        # 1. Перейти в раздел 'Widgets'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']"))).click()

        # 2. Выбрать пункт 'Auto Complete'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Auto Complete']"))).click()

        # 3. В поле 'Type multiple color names' выбрать значения: Black, Red, Magenta
        multi_color_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#autoCompleteMultipleInput")))
        multi_color_input.send_keys("Black")
        multi_color_input.send_keys(Keys.ENTER)  
        multi_color_input.send_keys("Red")
        multi_color_input.send_keys(Keys.ENTER)  
        multi_color_input.send_keys("Magenta")
        multi_color_input.send_keys(Keys.ENTER)  
        
        time.sleep(1)

        # 4. В поле 'Type single color name' выбрать значение: Black
        single_color_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#autoCompleteSingleInput")))
        single_color_input.send_keys("Black")
        single_color_input.send_keys(Keys.ENTER)  

        time.sleep(1)

        # 5. В поле 'Type single color name' заменить значение на Red
        single_color_input.clear()  # Очистить поле
        single_color_input.send_keys("Red")
        single_color_input.send_keys(Keys.ENTER)  

        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()

