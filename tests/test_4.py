# Написать 4 тест
# 1. Перейти на страницу https://demoqa.com/
# 2. Перейти в раздел 'Elements'
# 3. Выбрать пункт 'Buttons'
# 4. Нажать на кнопку Click Me
# 5. Проверить что появилась надпись You have done a dynamic click
# 6. Сделать двойной клик на кнопку Double Click Me
# 7. Проверить что появилась надпись You have done a double click
# 8. Сделать клик правой кнопкой кнопку Right Click Me
# 9. Проверить что появилась надпись You have done a right click



import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class TestButtons(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)  # ChromeDriver
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_buttons(self):
        # 2. Перейти в раздел 'Elements'
        elements_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
        elements_section.click()

        

        # 3. Выбрать пункт 'Buttons'
        buttons_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buttons']")))
        buttons_option.click()

        

        # 4. Нажать на кнопку 'Click Me'
        click_me_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']")))
        click_me_button.click()

        

        # 5. Проверить, что появилась надпись 'You have done a dynamic click'
        dynamic_click_message = self.wait.until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage")))
        self.assertTrue(dynamic_click_message.is_displayed())
        self.assertEqual(dynamic_click_message.text, "You have done a dynamic click")

        

        # 6. Сделать двойной клик на кнопку 'Double Click Me'
        double_click_button = self.wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
        actions = ActionChains(self.driver)
        # Не убирать time sleep иначе дабл клик не работает 🤔
        time.sleep(0.5)
        actions.double_click(double_click_button).perform()

        

        # 7. Проверить, что появилась надпись 'You have done a double click'
        double_click_message = self.wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage")))
        self.assertTrue(double_click_message.is_displayed())
        self.assertEqual(double_click_message.text, "You have done a double click")

        

        # 8. Сделать клик правой кнопкой на кнопку 'Right Click Me'
        right_click_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
        actions.context_click(right_click_button).perform()

        

        # 9. Проверить, что появилась надпись 'You have done a right click'
        right_click_message = self.wait.until(EC.visibility_of_element_located((By.ID, "rightClickMessage")))
        self.assertTrue(right_click_message.is_displayed())
        self.assertEqual(right_click_message.text, "You have done a right click")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
