import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class TestDemoQASortable(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    # Написать 20 тест
    # 1. Перейти на страницу https://demoqa.com/
    # 2. Перейти в раздел 'Interaction'
    # 3. Выбрать пункт 'Sortable'
    # 4. Перейти на вкладку List
    # 5. Отсортировать значения в убывающем порядке
    def test_sortable_list(self):
        # 2. Перейти в раздел 'Interaction'
        interaction_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Interactions']")))
        interaction_section.click()

        # 3. Выбрать пункт 'Sortable'
        sortable_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sortable']")))
        sortable_tab.click()

        # 4. Перейти на вкладку List
        list_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#demo-tab-list")))
        list_tab.click()

        sorted_numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

        # Перетаскиваем элементы для сортировки в убывающем порядке
        actions = ActionChains(self.driver)

        # Координата начала списка
        y_start = self.driver.find_element(By.CSS_SELECTOR, ".tab-content").location['y'] 

        root = self.driver.find_element(By.ID, 'app')
        for sn in sorted_numbers:
            list_item = self.driver.find_element(By.XPATH, f"//div[@class='list-group-item list-group-item-action' and text()='{sn}']")
            # Вычисляем разницу в координатах между элементом и началом списка
            y_offset = list_item.location['y'] - y_start
            # Перетаскиваем элемент на нужное место
            actions.drag_and_drop_by_offset(list_item, 0, -y_offset).perform()
            root.click() #кликаем чтобы сбросить выделение
            time.sleep(0.5) #стабилизация


        new_list = self.driver.find_elements(By.CSS_SELECTOR, '.list-group-item')
        texts = [el.text for el in new_list if el.text.strip()]
        sorted_numbers.reverse()
        # # Сравниваем финальный порядок с отсортированным
        assert sorted_numbers == texts, 'Некорректная сортировка: [' + ','.join(texts) + '] <> [' + ','.join(sorted_numbers) + ']'


    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()
