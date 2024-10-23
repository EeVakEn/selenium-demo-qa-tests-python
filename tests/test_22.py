# Написать 22 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Book Store Application'
# 3. Выбрать пункт 'Login'
# 4. Ввести UserName
# 5. Ввести Password
# 6. Нажать Login
# 7. Проверить что появилась надпись Invalid username or password!
# 8. Нажать NewUser
# 9. Заполнить First Name
# 10. Заполнить Last Name
# 11. Заполнить UserName
# 12. Заполнить Password 1 символом
# 13. Нажать Register
# 14. Проверить что появилась надпись Please verify reCaptcha to register!
# 15. Поставить чек бокс I`m not a robot
# 16. Нажать Register
# 17. Проверить что появилась надпись Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.
# 18. Заполнить Password валидным значением
# 19. Поставить чек бокс I`m not a robot
# 20. Нажать Register
# 21. В модальном окне нажать ОК

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium_recaptcha_solver import RecaptchaSolver


class TestDemoQABookStore(unittest.TestCase):

    def setUp(self):
        test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

        options = Options()
        options.page_load_strategy = 'eager'
        options.add_argument(f'--user-agent={test_ua}')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=options) 
        self.solver = RecaptchaSolver(driver=self.driver)
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)


    def test_register_invalid_password(self):
        # 2. Перейти в раздел 'Book Store Application'
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Book Store Application']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
        # 3. Выбрать пункт 'Login'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Login']"))).click()
        
        # 4. Ввести UserName
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='userName']"))).send_keys("invalidUser")
        
        # 5. Ввести Password
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("invalidPassword")
        
        # 6. Нажать Login
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))).click()
        
        # 7. Проверить, что появилась надпись Invalid username or password!
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#output #name"))).text
        assert error_message == "Invalid username or password!"

        # 8. Нажать New User
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#newUser"))).click()
        
        # 9. Заполнить First Name
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='firstname']"))).send_keys("FirstName")
        
        # 10. Заполнить Last Name
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='lastname']"))).send_keys("LastName")
        
        # 11. Заполнить UserName
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='userName']"))).send_keys("NewUserName")
        
        # 12. Заполнить Password 1 символом
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("a")
        
        # 13. Нажать Register
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='register']"))).click()
        
        # 14. Проверить, что появилась надпись Please verify reCaptcha to register!
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#output #name"))).text
        self.assertEqual(error_message, "Please verify reCaptcha to register!")
        
        # Поставить чекбокс "I'm not a robot"
        # Ожидание доступности iframe и переключение на него
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="reCAPTCHA"]')))
        time.sleep(5)
        # Ожидание, пока чекбокс будет доступен и клик по нему
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))).click()
        time.sleep(5)
        # Возврат к основному контенту страницы
        self.driver.switch_to.default_content()

        # 16. Нажать Register
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='register']"))).click()
        
        # 17. Проверить, что появилась надпись Passwords must have at least one non alphanumeric character, ...
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#output #name"))).text
        self.assertIn("Passwords must have at least one non alphanumeric character", error_message)
        
        # 18. Заполнить Password валидным значением
        valid_password = "Valid1!"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).clear()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(valid_password)

        # Поставить чекбокс "I'm not a robot"
        # Ожидание доступности iframe и переключение на него
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="reCAPTCHA"]')))
        time.sleep(5)
        # Ожидание, пока чекбокс будет доступен и клик по нему
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))).click()
        time.sleep(5)
        # Возврат к основному контенту страницы
        self.driver.switch_to.default_content()

        # 20. Нажать Register
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='register']"))).click()
        
        # 21. В модальном окне нажать ОК
        alert = self.wait.until(EC.alert_is_present())
        time.sleep(1)
        alert.accept()

    def tearDown(self):
        # Закрыть драйвер
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
