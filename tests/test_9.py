# Написать 9 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Alerts, Frame & Windows'
# 3. Выбрать пункт 'Browser Windows'
# 4. Нажать New Tab
# 5. Переключиться в открывшуюся вкладку
# 6. Проверить адрес вкладки
# 7. Вернуться на первоначальную вкладку
# 8. Нажать New Window
# 9. Переключиться в открывшуюся вкладку
# 10. Проверить адрес вкладки
# 11. Вернуться на первоначальную вкладку

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestBrowserWindows(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)
        

    def test_browser_windows(self):
        # 2. Перейти в раздел 'Alerts, Frame & Windows'
        alerts_frame_windows_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']")))
        alerts_frame_windows_section.click()

        # 3. Выбрать пункт 'Browser Windows'
        browser_windows_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Browser Windows']")))
        browser_windows_option.click()

        # Сохранение начального окна
        initial_window = self.driver.current_window_handle

        # 4. Нажать New Tab
        new_tab_button = self.wait.until(EC.element_to_be_clickable((By.ID, "tabButton")))
        new_tab_button.click()

        # 5. Переключиться в открывшуюся вкладку
        self.wait.until(EC.number_of_windows_to_be(2))
        new_tab = [window for window in self.driver.window_handles if window != initial_window][0]
        self.driver.switch_to.window(new_tab)

        # 6. Проверить адрес вкладки
        self.assertEqual(self.driver.current_url, "https://demoqa.com/sample")

        # 7. Вернуться на первоначальную вкладку
        self.driver.close()
        self.driver.switch_to.window(initial_window)

        # 8. Нажать New Window
        new_window_button = self.wait.until(EC.element_to_be_clickable((By.ID, "windowButton")))
        new_window_button.click()

        # 9. Переключиться в открывшуюся вкладку
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles if window != initial_window][0]
        self.driver.switch_to.window(new_window)

        # 10. Проверить адрес вкладки
        self.assertEqual(self.driver.current_url, "https://demoqa.com/sample")

        # 11. Вернуться на первоначальную вкладку
        self.driver.close()
        self.driver.switch_to.window(initial_window)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
