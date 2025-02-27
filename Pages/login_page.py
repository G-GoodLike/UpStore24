import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


from Base.base_class import Base
from Utilities.logger import Logger


class Login_page(Base):

    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    user_icon_main_page = "//li[@class = 'user_icons-item js-user_icons-item nav-hide']"
    user_name = "//input[@id='email']"
    password = "//input[@id='password']"
    login_button = "//button[@name= 'commit']"
    account_word = "//h1[@class='co-checkout-title co-title co-title--h1']"
    cart_button = "(//li[@class = 'user_icons-item js-user_icons-item'])[3]"

    # Getters
    def get_user_icon_main_page(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_icon_main_page)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_account_word(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.account_word)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions

    
    def click_user_icon_main_page(self):
        """ Click on icon in the right top corner to authorize """

        self.get_user_icon_main_page().click()
        print("Click user icon main page")


    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")


    # Methods

    def authorization(self):

        Logger.add_start_step(method="authorization")
        self.driver.get(self.url) # Переход на главную страницу стайта
        print("\n--- login_page.py ---\n")
        self.click_user_icon_main_page() # Для авторизации кликаем на иконку человека в верх. правом углу
        self.input_user_name("stepik_email@mail.ru") # Вводим логин
        self.input_password("Stepik_AS") # Вводим пароль
        self.click_login_button() # Ждем на кнопку авторизации


        self.get_current_url() # Тест. Получаем ссылку текущей URL
        self.assert_word(self.get_account_word(), "История заказов")
        print("\n")
        Logger.add_end_step(url=self.driver.current_url, method="authorization")


    def go_to_the_cart(self):
        print("\n--- login_page.py ---\n")

        self.click_cart_button()
























