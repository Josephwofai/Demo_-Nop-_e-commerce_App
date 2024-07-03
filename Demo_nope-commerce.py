from modulefinder import Module

import select
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
time.sleep(4)
driver.maximize_window()

# Navigate to the URL
driver.get("https://demo.nopcommerce.com/")
time.sleep(6)

# # Register
# driver.find_element(By.LINK_TEXT, "Register").click()
# time.sleep(2)
# driver.find_element(By.ID, "gender-male").click()
# time.sleep(2)
# driver.find_element(By.ID, "FirstName").send_keys("John")
# time.sleep(2)
# driver.find_element(By.ID, "LastName").send_keys("Doe")
# time.sleep(2)
# driver.find_element(By.NAME, "DateOfBirthDay").send_keys("20")
# time.sleep(1)
# driver.find_element(By.NAME, "DateOfBirthMonth").send_keys("December")
# time.sleep(1)
# driver.find_element(By.NAME, "DateOfBirthYear").send_keys("1916")
# time.sleep(1)
# driver.find_element(By.NAME, "Email").send_keys("qoi567hyu@gmail.com")
# time.sleep(1)
# driver.find_element(By.ID, "Password").send_keys("12390we@@")
# time.sleep(2)
# driver.find_element(By.ID, "ConfirmPassword").send_keys("12390we@@")
# time.sleep(2)
# driver.find_element(By.ID, "register-button").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div[2]/a").click()
# time.sleep(5)


# Input Credentials: Login
driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element(By.ID, "Email").send_keys("qoi567hyu@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "Password").send_keys("12390we@@")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button").click()
time.sleep(6)

# Shopping


