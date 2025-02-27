import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


from Pages.login_page import Login_page
from Pages.main_page import Main_page
from Pages.tablets_page import Tablets
from Pages.cart_page import Cart
from Pages.order_page import Order
from Pages.finish_page import Finish



def test_clear_the_cart(set_group, set_up):


    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = Login_page(driver)
    login.authorization()
    login.go_to_the_cart()


    cp = Cart(driver)
    cp.clear_the_cart()

    f = Finish(driver)
    f.get_screenshot()

    driver.quit()















