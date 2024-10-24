# Написать 16 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Widgets'
# 3. Выбрать пункт 'Date Picker'
# 4. В поле 'Select Date' выбрать 1 декабря 2023 годя
# 5. В поле 'Date And Time' 2 ноября 2022 года 20:00

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQA_DatePicker(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_date_picker(self):
        # 1. Перейти в раздел 'Widgets'
        widgets_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']")))
        widgets_section.click()

        # 2. Выбрать пункт 'Date Picker'
        date_picker_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Date Picker']")))
        date_picker_tab.click()

        # 3. В поле 'Select Date' выбрать 1 декабря 2023 года
        date_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#datePickerMonthYearInput")))
        date_input.click()

        # Ждем, пока элемент календаря станет видимым
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".react-datepicker")))

        year_selector = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__year-select")))
        year_selector.click()
        year_selector.send_keys("2023")  # 2023 год

        time.sleep(0.5)

        # Изменяем месяц и год, если необходимо
        month_selector = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__month-select")))
        month_selector.click()
        month_selector.send_keys("December")  # декабрь

        time.sleep(0.5)

        # Нажимаем на 1 декабря
        day_selector = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day--001")))
        day_selector.click()

        # 4. В поле 'Date And Time' выбрать 2 ноября 2022 года 20:00
        datetime_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#dateAndTimePickerInput")))
        datetime_input.click()

        # Ждем, пока элемент календаря станет видимым
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".react-datepicker")))

        # Нажимаем на 2024
        year_selector = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__year-read-view")))
        year_selector.click()
        year_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='react-datepicker__year-dropdown']//div[text()='2022']")))
        year_option.click()

        time.sleep(0.5)

        # Ноябрь
        month_selector = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__month-read-view")))
        month_selector.click()
        month_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='react-datepicker__month-dropdown']//div[text()='November']")))
        month_option.click()

        time.sleep(0.5)

        # Второе число
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".react-datepicker__day--002"))).click()

        time.sleep(0.5)

        # Вводим время 20:00
        time_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='react-datepicker__time-list']//li[text()='20:00']")))
        time_input.click()

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()

