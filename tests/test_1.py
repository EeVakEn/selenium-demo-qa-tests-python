# Написать 1 тест:
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Elements'
# 3. Выбрать пункт 'Text Box'
# 4. Заполнить все поля форме валидными значениями
# 5. Нажать кнопку Submit
# 6. Проверить что ниже появились введенные данные

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestDemoQA(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.wait = WebDriverWait(self.driver, 10)
        # self.driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
        # 1. Перейти на страницу https://demoqa.com/
        self.driver.get("https://demoqa.com/")

    def test_text_box(self):
        
        # 2. Перейти в раздел 'Elements'
        elements_section = self.driver.find_element(By.XPATH, "//h5[text()='Elements']")
        elements_section.click()
        
        # 3. Выбрать пункт 'Text Box'
        text_box_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']")))
        text_box_option.click()
        
        # 4. Заполнить все поля форме валидными значениями
        self.wait.until(EC.presence_of_element_located((By.ID, 'userName')))
        self.driver.find_element(By.ID, "userName").send_keys("John Doe")
        self.driver.find_element(By.ID, "userEmail").send_keys("johndoe@example.com")
        self.driver.find_element(By.ID, "currentAddress").send_keys("1234 Main St")
        self.driver.find_element(By.ID, "permanentAddress").send_keys("5678 Secondary St")

        # 5. Нажать кнопку Submit
        self.driver.find_element(By.ID, "submit").click()


        # 6. Проверить что ниже появились введенные данные с явным ожиданием
        output_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[@id='output']//p[@id='name']")))
        output_email = self.wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[@id='output']//p[@id='email']")))
        output_current_address = self.wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[@id='output']//p[@id='currentAddress']")))
        output_permanent_address = self.wait.until(EC.visibility_of_element_located((By.XPATH, ".//div[@id='output']//p[@id='permanentAddress']")))


        self.assertIn("John Doe", output_name.text)
        self.assertIn("johndoe@example.com", output_email.text)
        self.assertIn("1234 Main St", output_current_address.text)
        self.assertIn("5678 Secondary St", output_permanent_address.text)

    def tearDown(self):
        # Закрыть браузер
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
