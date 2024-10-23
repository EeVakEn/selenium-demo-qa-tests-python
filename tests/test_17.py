import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDemoQASlider(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://demoqa.com/")
        self.wait = WebDriverWait(self.driver, 10)

    # Написать 17 тест
    # 1. Перейти на страницу https://demoqa.com/
    # 2. Перейти в раздел 'Widgets'
    # 3. Выбрать пункт 'Slider'
    # 4. Сдвинуть слайдер на значение 50
    # 5. Проверить что в окне справа значение 50
    def test_slider(self):
        # 2. Перейти в раздел 'Widgets'
        widgets_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']")))
        widgets_section.click()

        # 3. Выбрать пункт 'Slider'
        slider_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Slider']")))
        slider_tab.click()

        # 4. Сдвинуть слайдер на значение 50
        slider = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".range-slider__wrap")))
        
        # Получаем размеры слайдера и вычисляем позицию для 50
        slider_width = slider.size['width']
        move_to = slider_width * 0.5  # 50%
        
        time.sleep(1) # не убирать

        # Используем ActionChains для перемещения слайдера
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(move_to - (slider_width / 2), 0).release().perform()

        # 5. Проверить что в окне справа значение 50
        output_value = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#sliderValue"))).get_attribute('value')
        assert output_value == "50", f"Slider position is {output_value}"

    def tearDown(self):
        self.driver.quit()

# Запуск теста
if __name__ == "__main__":
    unittest.main()
