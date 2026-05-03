import time

from selenium.webdriver.common.by import By
from locator.Locator import Locator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locator()

    def get_login_nav(self):
        return self.driver.find_element(By.XPATH, self.lc.login_xpath)

    def click_login_nav(self):
        self.get_login_nav().click()
        time.sleep(3)

    def get_username_input(self):
        return self.driver.find_element(By.ID, self.lc.username_id)

    def enter_username(self, username):
        self.get_username_input().send_keys(username)

    def get_password_input(self):
        return self.driver.find_element(By.ID, self.lc.password_id)

    def enter_password(self, password):
        self.get_password_input().send_keys(password)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.lc.login_button_xpath)

    def click_login_button(self):
        self.get_login_button().click()
        time.sleep(3)

    def login_function(self, username, password):
            self.click_login_nav()
            self.enter_username(username)
            self.enter_password(password)
            self.click_login_button()

            # Alternative way without using separate methods for each element



        # login_nav = self.driver.find_element(By.XPATH, self.lc.login_xpath)
        # login_nav.click()
        # time.sleep(2)
        # username_input = self.driver.find_element(By.ID, self.lc.username_id)
        # username_input.send_keys(username)
        # password_input = self.driver.find_element(By.ID, self.lc.password_id)
        # password_input.send_keys(password)
        # login_button = self.driver.find_element(By.XPATH, self.lc.login_button_xpath)
        # login_button.click()
        # time.sleep(3)
