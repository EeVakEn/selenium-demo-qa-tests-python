# Написать 5 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Elements'
# 3. Выбрать пункт 'Links'
# 4. Нажать на кнопку Home
# 5. Переключиться на открывшееся окно
# 6. Проверить адрес открывшегося окна
# 7. Переключиться на первое окно
# 8. Нажать Moved
# 9. Проверить что появилась надпись Link has responded with staus 301 and status text Moved Permanently


import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLinks(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_links(self):
        # 2. Перейти в раздел 'Elements'
        elements_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
        elements_section.click()

        

        # 3. Выбрать пункт 'Links'
        links_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Links']")))
        links_option.click()

        

        # 4. Нажать на кнопку 'Home'
        home_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_link.click()

        

        # 5. Переключиться на открывшееся окно

        # Ожидать, пока появится новое окно и переключиться на него
        self.wait.until(lambda d: len(self.driver.window_handles) > 1)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

        

        # 6. Проверить адрес открывшегося окна
        self.assertEqual(self.driver.current_url, "https://demoqa.com/")

        

        # 7. Переключиться на первое окно
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        

        # 8. Нажать 'Moved'
        moved_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Moved")))
        moved_link.click()

        

        # 9. Проверить, что появилась надпись 'Link has responded with status 301 and status text Moved Permanently'
        moved_message = self.wait.until(EC.visibility_of_element_located((By.ID, "linkResponse")))
        self.assertTrue(moved_message.is_displayed())
        self.assertIn("Link has responded with staus 301 and status text Moved Permanently", moved_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
