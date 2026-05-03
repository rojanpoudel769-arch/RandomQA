import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

#Alert with OK
signup_nav = driver.find_element(By.CSS_SELECTOR, ".analystic[href='#OKTab']")
signup_nav.click()

button = driver.find_element(By.XPATH, "//button[contains(text(),'click the button to display an')]")
button.click()
time.sleep(3)
driver.switch_to.alert.accept()

#Alert with ok and cancel
Nav1 = driver.find_element(By.CSS_SELECTOR, ".analystic[href='#CancelTab']")
Nav1.click()

button1 = driver.find_element(By.XPATH, "//button[normalize-space()='click the button to display a confirm box']")
button1.click()
time.sleep(3)

driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()


#Alert with Message
Nav2 = driver.find_element(By.XPATH, "//a[normalize-space()='Alert with Textbox']")
Nav2.click()

button2 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-info")
button2.click()
time.sleep(3)
driver.switch_to.alert.send_keys("Welcome to my class")
driver.switch_to.alert.accept()
time.sleep(3)


