# Написать 10 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Alerts, Frame & Windows'
# 3. Выбрать пункт 'Alerts'
# 4. Нажать 1 кнопку Click Me
# 5. Проверить текст в модальном окне
# 6. Нажать ОК
# 7. Нажать 2 кнопку Click Me
# 8. Проверить текст в модальном окне
# 9. Нажать ОК
# 10. Нажать 3 кнопку Click Me
# 11. Проверить текст в модальном окне
# 12. Нажать Отмена
# 13. Нажать 4 кнопку Click Me
# 14. Ввести текст в модальном окне
# 15. Нажать ОК


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQAAlerts(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options) 
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_alerts(self):
        # 2. Перейти в раздел 'Alerts, Frame & Windows'
        alerts_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))
        alerts_section.click()

        # 3. Выбрать пункт 'Alerts'
        alerts_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Alerts']")))
        alerts_tab.click()

        # 4. Нажать 1 кнопку Click Me
        first_button = self.wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
        first_button.click()

        # 5. Проверить текст в модальном окне
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text == "You clicked a button", f"Unexpected alert text: {alert_text}"

        # 6. Нажать ОК
        alert.accept()

        # 7. Нажать 2 кнопку Click Me
        second_button = self.wait.until(EC.element_to_be_clickable((By.ID, "timerAlertButton")))
        second_button.click()

        # 8. Проверить текст в модальном окне
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text == "This alert appeared after 5 seconds", f"Unexpected alert text: {alert_text}"

        # 9. Нажать ОК
        alert.accept()

        # 10. Нажать 3 кнопку Click Me
        third_button = self.wait.until(EC.element_to_be_clickable((By.ID, "confirmButton")))
        third_button.click()

        # 11. Проверить текст в модальном окне
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text == "Do you confirm action?", f"Unexpected alert text: {alert_text}"

        # 12. Нажать Отмена
        alert.dismiss()

        # 13. Нажать 4 кнопку Click Me
        fourth_button = self.wait.until(EC.element_to_be_clickable((By.ID, "promtButton")))
        fourth_button.click()

        # 14. Ввести текст в модальном окне
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys("Test message")

        # 15. Нажать ОК
        alert.accept()

    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()

