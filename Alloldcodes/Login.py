import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def test_login(self):
        try:
            nav_login = self.driver.find_element(By.ID, 'login2')
            nav_login.click()
            self.driver.implicitly_wait(10)
            uname = self.driver.find_element(By.ID, 'loginusername')
            uname.send_keys("testmorning")
            pwd = self.driver.find_element(By.ID, 'loginpassword')
            pwd.send_keys("test123")
            login_button = self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
            login_button.click()
            time.sleep(2)
            expectedresult = "Welcome testmorning"
            actualresult = self.driver.find_element(By.CSS_SELECTOR, "#nameofuser").text
            self.assertEqual(expectedresult, actualresult, msg="Login failed: Expected and actual result do not matched")
        except Exception as e:
            print(f"Test failed due to the exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
