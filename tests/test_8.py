# Написать 8 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Forms'
# 3. Выбрать пункт 'Practice Form'
# 4. Заполнить поля Name
# 5. Заполнить поле Email валидным значение
# 6. Выбрать Gender
# 7. Заполнить поле Mobile валидным значением
# 8. Заполнить поле Date of Birth
# 9. Выбрать в поле Subject 3 любых значения
# 10. Выбрать Hobbies
# 11. Заполнить Current Addres
# 12. Выбрать State and City
# 13. Нажать Submit
# 14. Проверить что в открывшимся окне есть введенные данные.
# 15. Нажать Close

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestPracticeForm(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_practice_form(self):
        # 2. Перейти в раздел 'Forms'
        forms_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']")))
        forms_section.click()

        # 3. Выбрать пункт 'Practice Form'
        practice_form_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']")))
        practice_form_option.click()

        # 4. Заполнить поля Name
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "firstName")))
        last_name_input = self.driver.find_element(By.ID, "lastName")
        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")

        # 5. Заполнить поле Email валидным значением
        email_input = self.driver.find_element(By.ID, "userEmail")
        email_input.send_keys("johndoe@example.com")

        # 6. Выбрать Gender
        gender_radio = self.driver.find_element(By.XPATH, "//label[text()='Male']")
        gender_radio.click()

        # 7. Заполнить поле Mobile валидным значением
        mobile_input = self.driver.find_element(By.ID, "userNumber")
        mobile_input.send_keys("1234567890")

        # 8. Заполнить поле Date of Birth
        date_of_birth_input = self.driver.find_element(By.ID, "dateOfBirthInput")
        date_of_birth_input.click()
        date_of_birth_input.send_keys(Keys.CONTROL + "a")
        date_of_birth_input.send_keys("10 Jan 1990")
        date_of_birth_input.send_keys(Keys.ENTER)

        # 9. Выбрать в поле Subject 3 любых значения
        subjects_input = self.driver.find_element(By.ID, "subjectsInput")
        subjects_input.send_keys("Math")
        subjects_input.send_keys(Keys.TAB)
        subjects_input.send_keys("Physics")
        subjects_input.send_keys(Keys.TAB)
        subjects_input.send_keys("Computer Science")
        subjects_input.send_keys(Keys.TAB)

        # 10. Выбрать Hobbies
        hobbies_checkbox = self.driver.find_element(By.XPATH, "//label[text()='Sports']")
        hobbies_checkbox.click()

        # 11. Заполнить Current Address
        current_address_input = self.driver.find_element(By.ID, "currentAddress")
        current_address_input.send_keys("123 Main Street, City, Country")

        # 12. Выбрать State and City
        state_dropdown = self.driver.find_element(By.ID, "react-select-3-input")
        state_dropdown.send_keys("NCR")
        state_dropdown.send_keys(Keys.ENTER)

        city_dropdown = self.driver.find_element(By.ID, "react-select-4-input")
        city_dropdown.send_keys("Delhi")
        city_dropdown.send_keys(Keys.ENTER)

        # 13. Нажать Submit
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        # 14. Проверить что в открывшемся окне есть введенные данные
        modal_content = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

        # Проверяем, что данные присутствуют
        self.assertIn("John Doe", modal_content.text)
        self.assertIn("johndoe@example.com", modal_content.text)
        self.assertIn("1234567890", modal_content.text)
        self.assertIn("10 January,1990", modal_content.text)
        self.assertIn("Math", modal_content.text)
        self.assertIn("Physics", modal_content.text)
        self.assertIn("Computer Science", modal_content.text)
        self.assertIn("Sports", modal_content.text)
        self.assertIn("123 Main Street", modal_content.text)
        self.assertIn("NCR Delhi", modal_content.text)

        # 15. Нажать Close
        close_button = self.driver.find_element(By.ID, "closeLargeModal")
        close_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
