from faker import Faker
import select
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


from Base.base_class import Base



class Order(Base):

    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    delivery_rb = "//label[@for = 'order_delivery_variant_id_2654338']"
    city = ""
    address_text_area = "//textarea[@class = 'co-input-field js-input-field']"
    delivery_date_area = "//div[@id='delivery-date-calendar-block']"
    day_of_delivery = "//td[contains(@class, 'rd-day-body')][not(contains(@class, 'disabled')) and not(contains(@class, 'selected'))]"

    calendar = "//div[@class = 'rd-container rd-container-attachment']"

    time_area = "//div[@class = 'co-input-select']"
    time_of_delivery = "//select[@id = 'delivery-time-intervals-select']"

    title = "//h2[@class = 'co-title co-title--h2']"



    # Getters
    def get_delivery_rb(self):
        return self.driver.find_element(By.XPATH, self.delivery_rb)

    def get_address(self,address):
        return WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH,address)))

    def get_address_text_area(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_text_area)))

    def get_delivery_date_area(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_date_area)))

    def get_day_of_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.day_of_delivery)))

    def get_time_area(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.time_area)))

    def get_time_of_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.time_of_delivery)))

    def get_title(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.title)))

    # Actions




    def click_delivery_rb(self):
        self.get_delivery_rb().click()
        print("Click delivery radio button")

    def click_address(self):
        try:

            address = "//div[@class = 'co-input  co-input--textarea co-input--address  co-input--nested co-input--empty_nested']" # Если поле было пустое
            self.get_address(address).click()

        except:
            address = "//div[@class = 'co-input  co-input--textarea co-input--address  co-input--nested']" # Если поле было заполнено до этого
            self.get_address(address).click()
            self.get_address_text_area().clear()


    def write_address_text_area(self):
        time.sleep(1)
        fake = Faker("ru_RU")
        fake_address = fake.city() + ", " + fake.street_address()
        self.get_address_text_area().send_keys(fake_address)
        print(fake_address)

    def click_delivery_date(self):
        time.sleep(1)
        self.get_delivery_date_area().click()

        print("Click delivery date")

    def choose_day_of_delivery(self):
        self.get_day_of_delivery().click()
        print(f'Select tomorrow')

    def click_time_area(self):
        self.get_time_area().click()


    def choose_time_of_delivery(self):
        time.sleep(1)
        select = Select(self.get_time_of_delivery())
        try:
            select.select_by_value('14:00-18:00')
            print("14:00-18:00")
        except:
            select.select_by_value('16:00-20:00')
            print("Alas, u can take only: 16:00-20:00")


    # Methods

    def create_order(self):
        print("\n--- order_page.py ---\n")
        self.click_delivery_rb()
        self.click_address()

        self.write_address_text_area()

        """ Нестабильные тесты """
        # self.click_delivery_date()
        # self.choose_day_of_delivery()
        # self.click_time_area()
        # self.choose_time_of_delivery()

        self.get_current_url() # Тест. Получаем ссылку текущей URL
        self.assert_word(self.get_title(), "Доставка")
        print("\n")

























