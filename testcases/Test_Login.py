import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage
from Utilities.ReadCSVData import ReadCSVData
from ddt import ddt, data, unpack

@ddt()
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.lp = LoginPage(self.driver)
    @data(*ReadCSVData.read_data_from_csv("Testdata/login_credentials.csv"))
    @unpack
    def test_login(self, username, password, user_type):
        try:
            self.lp.login_function(username, password)
            time.sleep(3)
            if user_type=="p":
                expectedresult = f"Welcome {username}"
                actualresult = self.driver.find_element(By.ID, "nameofuser").text
                self.assertEqual(expectedresult, actualresult, msg="Login failed")
            else:
                print("Negative tese case are execuated successfully")
        except Exception as e:
            self.fail("Login failed: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
