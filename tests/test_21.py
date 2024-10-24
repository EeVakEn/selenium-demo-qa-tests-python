# Написать 21 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Interaction'
# 3. Выбрать пункт 'Selectable'
# 4. Перейти на вкладку Grid
# 5. Выбрать все значения
# 6. Снять все значения
# 7. Выбрать только Five


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.action_chains import ActionChains


class TestDemoQASelectable(unittest.TestCase):
    def setUp(self):
        # Настройки для браузера
        options = Options()
        options.page_load_strategy = 'eager'  # Стратегия загрузки страницы
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)  # Ожидание элементов до 10 секунд

    def tearDown(self):
        # Закрытие браузера после выполнения тестов
        self.driver.quit()

    def test_selectable_grid(self):
        
        # 2. Перейти в раздел 'Interactions'
        interaction_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Interactions']")))
        interaction_section.click()

        # 3. Выбрать пункт 'Selectable'
        selectable_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Selectable']")))
        selectable_tab.click()

        # 4. Перейти на вкладку Grid
        grid_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#demo-tab-grid")))
        grid_tab.click()

        # 5. Выбрать все значения
        all_grid_items = self.driver.find_elements(By.CSS_SELECTOR, "#gridContainer .list-group-item")
        all_grid_items_len = len(all_grid_items)

        # Проходим по всем элементам и кликаем по каждому из них (в 2 цикла)
        for i in range(all_grid_items_len):
            self.wait.until(EC.element_to_be_clickable(all_grid_items[i])).click()
            time.sleep(0.2)  # Задержка для стабильности кликов

        # Снимаем выбор со всех элементов
        for i in range(all_grid_items_len):
            self.wait.until(EC.element_to_be_clickable(all_grid_items[i])).click()
            time.sleep(0.2) 

        # 7. Выбрать только 'Five'
        five_item = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='gridContainer']//li[text()='Five']")))
        five_item.click()

        # Проверяем, что только 'Five' выбрано
        selected_items = self.driver.find_elements(By.CSS_SELECTOR, ".list-group-item.active")
        self.assertEqual(len(selected_items), 1, "Только один элемент должен быть выбран")
        self.assertEqual(selected_items[0].text, "Five", "Выбранный элемент должен быть 'Five'")

if __name__ == "__main__":
    unittest.main()
