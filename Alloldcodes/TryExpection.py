import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")

try:
    nav_login = driver.find_element(By.ID, 'login2')
    nav_login.click()
    uname = driver.find_element(By.ID, 'loginusername')
    uname.send_keys("testmorning")
    pwd = driver.find_element(By.ID, 'loginpassword')
    pwd.send_keys("test123")
    login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()

except ElementNotInteractableException:
    print("Element not interactable, trying again after 2 seconds...")
    driver.implicitly_wait(2)
    uname = driver.find_element(By.ID, 'loginusername')
    uname.send_keys("testmorning")
    pwd = driver.find_element(By.ID, 'loginpassword')
    pwd.send_keys("test123")
    login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()
    time.sleep(5)

except Exception as e:
    print("An error occurred:", str(e))
finally:
    driver.quit()