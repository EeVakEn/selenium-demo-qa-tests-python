# Написать 13 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Alerts, Frame & Windows'
# 3. Выбрать пункт 'Modal Dialogs'
# 4. Нажать Small Modal
# 5. В открывшемся окне сверить заголовок
# 6. В открывшемся окне сверить основной текст
# 7. Нажать Close



import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQAModalDialogs(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_small_modal(self):
        # 2. Перейти в раздел 'Alerts, Frame & Windows'
        alerts_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))
        alerts_section.click()

        # 3. Выбрать пункт 'Modal Dialogs'
        modal_dialogs_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Modal Dialogs']")))
        modal_dialogs_tab.click()

        # 4. Нажать Small Modal
        small_modal_button = self.wait.until(EC.element_to_be_clickable((By.ID, "showSmallModal")))
        small_modal_button.click()

        # 5. В открывшемся окне сверить заголовок
        modal_title = self.wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-sm"))).text
        assert modal_title == "Small Modal", f"Unexpected modal title: {modal_title}"

        # 6. В открывшемся окне сверить основной текст
        modal_body_text = self.driver.find_element(By.CSS_SELECTOR, ".modal-body").text
        expected_body_text = "This is a small modal. It has very less content"
        assert modal_body_text == expected_body_text, f"Unexpected modal body text: {modal_body_text}"

        # 7. Нажать Close
        close_button = self.driver.find_element(By.ID, "closeSmallModal")
        close_button.click()

    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()

