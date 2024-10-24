# Написать 6 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Elements'
# 3. Выбрать пункт 'Upload and Download'
# 4. Загрузить файл
# 5. Проверить в поле с именем файла его имя
# 6. Проверить в поле с полным именем директории имя всего пути

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class TestUploadAndDownload(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))  # ChromeDriver
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_upload_file(self):
        # 2. Перейти в раздел 'Elements'
        elements_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
        elements_section.click()

        # 3. Выбрать пункт 'Upload and Download'
        upload_and_download_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Upload and Download']")))
        upload_and_download_option.click()


        
        # Указываем путь к тестовому файлу
        file_name = "testfile.txt"
        file_path = os.path.abspath(file_name)
        with open(file_path, "w") as f:  # Создаем тестовый файл
            f.write("This is a test file.")
        os.chmod(file_path, 0o777)
        assert os.path.exists(file_path), f"Файл {file_path} не был создан!"
        
        # 4. Загрузить файл
        upload_input = self.wait.until(EC.presence_of_element_located((By.ID, "uploadFile")))
        upload_input.send_keys(file_path)

        # 5. Проверить в поле с именем файла его имя
        uploaded_file_path = self.wait.until(EC.presence_of_element_located((By.ID, "uploadedFilePath"))).text
        
        self.assertIn(file_name, uploaded_file_path) 


        # 6. Проверить в поле с полным именем директории имя всего пути
        # Проверяем, что путь отображается корректно
        # Не должно соответвовать так как в поле приходит fakepath
        # print('Fullpath: ', file_path, ', Name from site: ', uploaded_file_path)
        self.assertNotIn(file_path, uploaded_file_path) 

    def tearDown(self):
        # Удаляем созданный файл после завершения теста
        file_path = os.path.abspath("testfile.txt")
        if os.path.exists(file_path):
            os.remove(file_path)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
