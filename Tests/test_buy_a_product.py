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
from Utilities.clear_screenshots import Clear


def test_buy_a_product(set_group, set_up):


    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_catalog()

    tp = Tablets(driver)
    tp.select_tablets(2)
    tp.go_to_the_cart()

    cp = Cart(driver)
    cp.product_confirmation()

    o = Order(driver)
    o.create_order()

    f = Finish(driver)
    f.get_screenshot()

    driver.quit()


@pytest.mark.second
def test_buy_a_product_2(set_up):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_catalog()

    tp = Tablets(driver)
    tp.select_tablets(2)
    tp.select_tablets_2(3)
    tp.go_to_the_cart()

    cp = Cart(driver)
    cp.product_confirmation()

    o = Order(driver)
    o.create_order()

    f = Finish(driver)
    f.get_screenshot()

    driver.quit()

@pytest.mark.first
def test_buy_a_product_3():


    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_catalog()

    tp = Tablets(driver)
    tp.select_tablets(2)
    tp.select_tablets_2(3)
    tp.select_tablets_3(4)
    tp.go_to_the_cart()

    cp = Cart(driver)
    cp.product_confirmation()

    o = Order(driver)
    o.create_order()

    f = Finish(driver)
    f.get_screenshot()

    driver.quit()















