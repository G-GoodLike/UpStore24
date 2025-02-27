import select
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys


from Base.base_class import Base
from Utilities.logger import Logger


class Tablets(Base):

    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    price_slider = "//span[contains(@class, 'irs-slider from')]"  # Слайдер цены
    more_filters = "(//button[@class= 'button button--empty button--info button--small js-filter-hidden-toggle'])"
    color_check_box = "//label[@for = 'filter-value-109849120']" # Серебристый цвет
    cpu_check_box ="//label[@for = 'filter-value-247481722']" # apple M4
    sort_container = "//select[@class = 'js-filter-sort input--sort']"  # Сортировка
    select_item_cart = "(//button[@class = 'button button--icon button--small button--empty button--empty--inverse'])"
    message_cart = "body"  # Pop-up сообщение, которое появляется, после добавления товара в корзину
    pop_up = "fancybox-container"
    cart_button = "//a[@class = 'button button--primary button--block button--large']"


    # Getters
    def get_price_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider)))

    def get_sort_container(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_container)))

    def get_more_filters(self,index):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"({self.more_filters})[{index}]")))

    def get_color(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.color_check_box)))

    def get_cpu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cpu_check_box)))

    def get_item_cart(self,amount):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"({self.select_item_cart})[{amount}]")))

    def get_message_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, self.message_cart)))

    def get_wait(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, self.pop_up)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions


    def move_price_bar(self):
        time.sleep(1)
        action = ActionChains(self.driver)
        offset_x = 30
        action.drag_and_drop_by_offset(self.get_price_slider(),offset_x,0).perform()
        print("Slide price bar")

    def select_sort_container(self):
        time.sleep(1)
        select = Select(self.get_sort_container())
        select.select_by_value('price')
        print("Sort by price")

    def click_color_check_box(self):
        self.get_color().click()
        print("Pick Silver color")

    def click_more_filters(self,index):
        self.get_more_filters(index).click()
        print("More CPU filter")

    def click_cpu_check_box(self):
        self.get_cpu().click()
        print("Pick CPU")

    def click_cart_item(self,amount):
        time.sleep(3)
        new_item = self.get_item_cart(amount)
        new_item.click()
        print(f"Add tablet number {amount} to cart")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    # Methods

    def select_tablets(self,number):
        Logger.add_start_step(method="select_catalog")

        print("\n--- tablets_page.py ---\n")
        self.move_price_bar()
        self.select_sort_container()
        self.click_color_check_box()
        self.click_more_filters(2)
        self.click_cpu_check_box()
        self.click_cart_item(number) # Для выбора товара, необходимо изменить переменную number в файле test_buy_a_product. Line 37
        print(f"Tablet {number} just added to the cart")

        Logger.add_end_step(url=self.driver.current_url, method="select_tablets")


    def select_tablets_2(self,number_2):
        Logger.add_start_step(method="select_tablets_2")

        self.get_wait()  # ждем, чтобы появился pop-up
        self.get_message_cart().send_keys(Keys.ESCAPE) # Нажимаю ESC для того, чтобы выйти из pop-up сообщения
        print("ESC is pressed!")
        self.click_cart_item(number_2)
        print(f"Tablet {number_2} just added to the cart")

        Logger.add_end_step(url=self.driver.current_url, method="select_tablets_2")


    def select_tablets_3(self,number_3):
        Logger.add_start_step(method="select_tablets_3")

        self.get_wait() # ждем, чтобы появился pop-up
        self.get_message_cart().send_keys(Keys.ESCAPE) # Нажимаю ESC для того, чтобы выйти из pop-up сообщения
        print("ESC is pressed!")
        self.click_cart_item(number_3)
        print(f"Tablet {number_3} just added to the cart")

        Logger.add_end_step(url=self.driver.current_url, method="select_tablets_3")


    def go_to_the_cart(self):
        Logger.add_start_step(method="go_to_the_cart")
        self.click_cart_button()
        Logger.add_end_step(url=self.driver.current_url, method="go_to_the_cart")

























