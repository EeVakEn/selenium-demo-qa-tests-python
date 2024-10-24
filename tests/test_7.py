# Написать 7 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Elements'
# 3. Выбрать пункт 'Dynamic Properties'
# 4. Подождать пока текст кнопки 'Color Change' не сменит цвет
# 5. Обновить страницу
# 6. Подождать пока кнопка 'Visible After 5 Seconds' не появится

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDynamicProperties(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_dynamic_properties(self):
        # 2. Перейти в раздел 'Elements'
        elements_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
        elements_section.click()

        # 3. Выбрать пункт 'Dynamic Properties'
        dynamic_properties_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dynamic Properties']")))
        dynamic_properties_option.click()

        # 4. Подождать пока текст кнопки 'Color Change' не сменит цвет
        color_change_button = self.wait.until(EC.presence_of_element_located((By.ID, "colorChange")))
        initial_color = color_change_button.value_of_css_property("color")
        
        # Используем явное ожидание, чтобы дождаться изменения цвета кнопки
        self.wait.until(lambda driver: driver.find_element(By.ID, "colorChange").value_of_css_property("color") != initial_color)
        new_color = color_change_button.value_of_css_property("color")
        self.assertNotEqual(initial_color, new_color, "Цвет кнопки не изменился")

        # 5. Обновить страницу
        self.driver.refresh()

        # 6. Подождать пока кнопка 'Visible After 5 Seconds' не появится
        visible_after_button = self.wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
        self.assertTrue(visible_after_button.is_displayed(), "Кнопка не появилась через 5 секунд")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
