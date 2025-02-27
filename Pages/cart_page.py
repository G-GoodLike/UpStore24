import select
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


from Base.base_class import Base
from Utilities.logger import Logger


class Cart(Base):

    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    submit_button = "//input[@type = 'submit']"
    title = "//h1[@class = 'text-title']"
    bin_button = "//button[@class = 'button button--empty button--icon button--medium button--remove']"


    # Getters
    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_title_word(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_bin_button(self):
        try:
            return WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, self.bin_button)))
        except TimeoutException:
            return None # чтобы успешно выйти из цикла и не было ошибки

    # Actions

    def click_submit_button(self):
        self.get_current_url() # Тест. Получаем ссылку текущей URL
        self.assert_word(self.get_title_word(), "Корзина")

        self.get_submit_button().click()
        print("Click submit button")

    def click_bin_button(self):
        self.get_current_url() # Тест. Получаем ссылку текущей URL
        self.assert_word(self.get_title_word(), "Корзина")
        print("Click bin button")
        i = 0
        while True:
            if self.get_bin_button():
                self.get_bin_button().click()
                i+=1
                time.sleep(1)
            else:
                break

        print(f"Was deleted {i} items")


    # Methods

    def product_confirmation(self):
        Logger.add_start_step(method="product_confirmation")
        print("\n--- cart_page.py ---\n")

        self.click_submit_button()

        Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")



    def clear_the_cart(self):
        Logger.add_start_step(method="clear_the_cart")
        print("\n--- cart_page.py ---\n")

        self.click_bin_button()
        print("Whole cart was clear!")

        Logger.add_end_step(url=self.driver.current_url, method="clear_the_cart")

























