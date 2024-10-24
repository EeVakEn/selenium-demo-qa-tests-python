import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestDromWebsite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        # options.add_argument("--headless")  # Запуск в фоновом режиме
        cls.driver = webdriver.Chrome(options=options, service=Service(executable_path='/usr/bin/chromedriver'))
        cls.wait = WebDriverWait(cls.driver, 15)
        cls.start_url = "https://www.drom.ru/"

    def test_page_title(self):
        """Тест 1: Проверка заголовка страницы"""
        self.driver.get(self.start_url)
        expected_title = "Дром - цены на машины"
        self.wait.until(EC.title_is(expected_title))
        assert expected_title == self.driver.title

    def test_navigation_functionality(self):
        """Тест 2: Проверка функциональности навигации по маркам авто"""
        show_more_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-ftid='component_cars-list']//div[text()='Показать все']")))
        show_more_btn.click()
        lincoln_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-ftid='component_cars-list']//a[text()='Lincoln']")))
        lincoln_btn.click()
    
        self.wait.until_not(EC.url_changes(self.driver.current_url))
        assert "https://auto.drom.ru/lincoln/" == self.driver.current_url



    def test_vin_form(self):
        """Тест 3: Проверка формы VIN/госномер"""
        
        self.driver.get(self.start_url)
        # Проверка на ввод некорректного VIN
        vin_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-ftid='autostory-widget_input']")))
        vin_input.send_keys('123')  # Вводим некорректный VIN
        vin_input.send_keys(Keys.ENTER)
        
        # Проверяем сообщение об ошибке
        check_auto_form_error = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-ftid='autostory-widget']//span[@data-ftid='error_message']")))
        assert 'Введите корректный VIN' in check_auto_form_error.text

        # Проверка на ввод корректного VIN
        vin_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-ftid='autostory-widget_input']")))
        vin_input.clear()
        vin_input.send_keys('У345ВТ55')  # Вводим корректный госномер
        vin_input.send_keys(Keys.ENTER)
        
        # Проверяем, что URL изменился
        self.wait.until(EC.url_contains('vin.drom.ru'))
        assert self.driver.current_url.startswith('https://vin.drom.ru'), "URL не изменился на ожидаемый"


    def test_carousel_hide_element_after_scroll(self):
        """Тест 4: Проверка скрытия элемента карусели после перетаскивания"""
        
        self.driver.get(self.start_url)
        
        # Ожидаем появления карусели
        carousel = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-ftid='component_premium-carousel']")))
        assert carousel.is_displayed(), "Карусель с объявлениями не отображается"
        
        # Находим первый слайд
        first_slide = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-ftid='component_premium-carousel']//a[@data-ftid='component_premium-carousel_item'][1]")))
        
        old_alt=first_slide.find_element(By.CSS_SELECTOR, 'img').get_attribute('alt')
        assert first_slide.is_displayed(), "Первый слайд карусели не отображается"
        
        next_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-ftid='component_premium-carousel']//button[@aria-label='листать вперед']")))
        next_btn.click()
        next_btn.click()
        time.sleep(1)
        new_first_slide = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-ftid='component_premium-carousel']//a[@data-ftid='component_premium-carousel_item'][1]")))
        new_alt=new_first_slide.find_element(By.CSS_SELECTOR, 'img').get_attribute('alt')

        assert new_alt != old_alt, "Первый слайд карусели все еще виден после перетаскивания"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
