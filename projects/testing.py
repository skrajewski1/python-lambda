from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
time.sleep(2)
driver.get("http://54.196.208.187:8080/")

username = driver.find_element(by=By.NAME, value='j_username')
password = driver.find_element(by=By.NAME, value='j_password')

username.send_keys('admin')
password.send_keys('admin1234')
submit_button = driver.find_element(by=By.NAME, value='Submit')
submit_button.click()

time.sleep(2)

