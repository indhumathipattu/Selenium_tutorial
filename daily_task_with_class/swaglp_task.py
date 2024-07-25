import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@data-test='username']").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Open Menu']").click()
driver.find_element(By.XPATH,"//a[text()='Logout']").click()

#complated my task