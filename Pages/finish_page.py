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
import sys


from Base.base_class import Base



class Finish(Base):

    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods

    def finish(self):

        self.get_current_url()
        self.assert_url("https://upstore24.ru/new_order")
        self.get_screenshot()
























