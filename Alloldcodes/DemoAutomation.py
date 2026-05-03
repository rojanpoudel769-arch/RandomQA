import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

First_Name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
First_Name.send_keys("Roshan")
Last_Name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
Last_Name.send_keys("Poudel")

Address = driver.find_element(By.XPATH, "//textarea[@class='form-control ng-pristine ng-untouched ng-valid']")
Address.send_keys("Baneshwor")

email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
email.send_keys("roshanpoudel@gmail.com")

phone = driver.find_element(By.CSS_SELECTOR, "input[type='tel']")
phone.send_keys("1234567892")

gender = driver.find_element(By.XPATH, "//label[normalize-space()='Male']")
gender.click()

Hobbies = driver.find_element(By.XPATH, "//input[@id='checkbox1']")
Hobbies.click()
time.sleep(3)

Language = driver.find_element(By.XPATH, "//div[@id='msdd']")
Language.click()

language1 = driver.find_element(By.XPATH, "//a[normalize-space()='English']")
language1.click()

outside = driver.find_element(By.XPATH, "//label[normalize-space()='Skills']")
outside.click()

skills = driver.find_element(By.XPATH, "//select[@id='Skills']")
skills.click()

skills1 = driver.find_element(By.XPATH, "//option[@value='Certifications']")
skills1.click()

country = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span')
country.click()

country1 = driver.find_element(By.XPATH, '//*[@id="select2-country-results"]/li[4]')
country1.click()

Year = driver.find_element(By.CSS_SELECTOR, "#yearbox")
Year.click()

Year_value = driver.find_element(By.CSS_SELECTOR, "option[value='2010']")
Year_value.click()

Password = driver.find_element(By.XPATH, "//input[@id='firstpassword']")
Password.send_keys("1234567")

Conform_Password = driver.find_element(By.CSS_SELECTOR, "#secondpassword")
Conform_Password.send_keys("1234567")
time.sleep(3)
