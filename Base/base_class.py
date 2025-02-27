import datetime
import os

import Screen


class Base():
    def __init__(self, driver):
        self.driver = driver

    """ Method get current URL """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    """ Method assert word """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value")

    """ Method assert URL """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")


    """ Method screenshot """

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'Screenshot' + now_date + '.png'
        self.driver.save_screenshot("C:\\Users\\G_GoodLike\\PycharmProjects\\SeleniumLessonFinalProject\\Screen\\" + name_screenshot)

