import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoQATabs(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    # Написать 18 тест
    # 1. Перейти на страницу https://demoqa.com/
    # 2. Перейти в раздел 'Widgets'
    # 3. Выбрать пункт 'Tabs'
    # 4. Открыть вкладку What
    # 5. Проверить что на ней есть текст
    # 6. Открыть вкладку Origin
    # 7. Проверить что на ней есть текст
    # 8. Открыть вкладку Use
    # 9. Проверить что на ней есть текст
    # 10. Проверить что вкладка More недоступна
    def test_tabs(self):
        # 2. Перейти в раздел 'Widgets'
        widgets_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']")))
        widgets_section.click()

        # 3. Выбрать пункт 'Tabs'
        tabs_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Tabs']")))
        tabs_tab.click()

        # 4. Открыть вкладку What
        what_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#demo-tab-what")))
        what_tab.click()

        # 5. Проверить что на ней есть текст
        what_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#demo-tabpane-what.show")))
        assert what_text.text != ""

        # 6. Открыть вкладку Origin
        origin_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#demo-tab-origin")))
        origin_tab.click()

        # 7. Проверить что на ней есть текст
        origin_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#demo-tabpane-origin.show")))
        assert origin_text.text != ""

        # 8. Открыть вкладку Use
        use_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#demo-tab-use")))
        use_tab.click()

        # 9. Проверить что на ней есть текст
        use_text = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#demo-tabpane-use.show")))
        assert use_text.text != ""

        # 10. Проверить что вкладка More недоступна
        more_tab = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#demo-tab-more")))
        
        assert 'disabled' in more_tab.get_attribute('class') and not self.driver.find_element(By.CSS_SELECTOR, '#demo-tabpane-more').is_displayed()

    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()
