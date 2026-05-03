import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qah.bishalkarki.com/")
driver.maximize_window()
time.sleep(2)
login_nav = driver.find_element(By.XPATH, "/html/body/main/header/nav/div/div/div[1]/div[2]/div[1]/div/a/span")
login_nav.click()
username = driver.find_element(By.ID, "field-email")
username.send_keys("msangam994@gmail.com")
password = driver.find_element(By.CSS_SELECTOR, "#field-password")
password.send_keys("SamG@m12#4")
button = driver.find_element(By.CSS_SELECTOR, "#submit-login")
button.click()
time.sleep(2)
