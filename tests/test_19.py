import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestDemoQASelectMenu(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    # Написать 19 тест
    # 1. Перейти на страницу https://demoqa.com/
    # 2. Перейти в раздел 'Widgets'
    # 3. Выбрать пункт 'Select Menu'
    # 4. В поле 'Select Value' выбрать 'A root option'
    # 5. В поле 'Select One' выбрать 'Ms.'
    # 6. В поле 'Old Style Select Menu' выбрать 'Black'
    # 7. В поле 'Multiselect drop down' выбрать: Black, Red
    # 8. В поле 'Standard multi select' выбрать 'Opel'
    def test_select_menu(self):
        # 2. Перейти в раздел 'Widgets'
        widgets_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']")))
        widgets_section.click()

       # 3. Выбрать пункт 'Select Menu'
        select_menu_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Select Menu']")))
        select_menu_tab.click()

        # 4. В поле 'Select Value' выбрать 'A root option'
        select_value = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#withOptGroup")))
        select_value.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='A root option']"))).click()

        # 5. В поле 'Select One' выбрать 'Ms.'
        select_one = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selectOne")))
        select_one.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Ms.']"))).click()

        # 6. В поле 'Old Style Select Menu' выбрать 'Black'
        old_style_select = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#oldSelectMenu")))
        old_style_select.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Black']"))).click()

        # 7. В поле 'Multiselect drop down' выбрать: Black, Red
        multi_select = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Select...']")))
        multi_select.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Black']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Red']"))).click()

        # 8. В поле 'Standard multi select' выбрать 'Opel'
        standard_multi_select = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cars")))
        standard_multi_select.click()
        self.wait.until(EC.element_located_to_be_selected((By.XPATH, "//option[@value='opel']")))
        self.driver.find_element(By.ID, 'selectMenuContainer').click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
