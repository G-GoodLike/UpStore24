import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


from Base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

from Utilities.logger import Logger


class Main_page(Base):

    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog_hamburger = "//a[@data-target='hamburger']"
    catalog_hamburger_tablets = "(//a[@class = 'nav-collections-toggle js-nav-collections-toggle nav-collections-toggle--next'])[2]"
    reviews = "(//a[@href='https://yandex.ru/maps/org/upstore24/65273314325/reviews/?indoorLevel=1&ll=37.502786%2C55.741140&z=17'])[2]"
    title = "//h1[@class = 'orgpage-header-view__header']"
    catalog_title = "//h1[@class = 'section-title']"

    # Getters
    def get_catalog_hamburger(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_hamburger)))

    def get_catalog_hamburger_tablets(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.catalog_hamburger_tablets)))

    def get_reviews(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.reviews)))

    def get_title_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH,self.title)))

    def get_catalog_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH,self.catalog_title)))


    # Action

    def move_to_catalog(self):
        # Мышка наводится на бургер-меню "Каталог", но не кликает на него

        action = ActionChains(self.driver)
        action.move_to_element(self.get_catalog_hamburger()).perform()
        print("Open catalog")

    def click_catalog_tablets(self):
        # Выбирается раздел каталога "Планшеты"

        self.get_catalog_hamburger_tablets().click()
        print("Clicked on tablets")

    def click_reviews(self):
        # Кликаем на раздел "Отзывы" (о магазине)

        self.get_reviews().click()
        print("Clicked on reviews")



    # Method

    def select_catalog(self):
        """ Select Tablets from catalog """
        Logger.add_start_step(method="select_catalog")
        print("\n--- main_page.py ---\n")

        self.driver.get(self.url)
        self.move_to_catalog()
        self.click_catalog_tablets()

        self.get_current_url() # Тест. Получаем ссылку текущей URL
        self.assert_word(self.get_catalog_title(), "Планшеты")
        print("\n")
        Logger.add_end_step(url=self.driver.current_url, method="select_catalog")


    def select_reviews_about_store(self):
        """ Go to the reviews about store """
        Logger.add_start_step(method="select_reviews_about_store")
        print("\n--- main_page.py ---\n")

        self.driver.get(self.url)
        self.click_reviews()

        self.get_current_url() # Тест. Получаем ссылку текущей URL
        self.assert_word(self.get_title_name(), "Upstore24")
        print("\n")
        Logger.add_end_step(url=self.driver.current_url, method="select_reviews_about_store")
























