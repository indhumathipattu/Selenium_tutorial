import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/reg")
driver.maximize_window()
driver.find_element(By.NAME,"firstname").send_keys("INDHUMATHI")
driver.find_element(By.NAME,"lastname").send_keys("INDHUMATHI")
time.sleep(5)
driver.find_element(By.NAME,"reg_email__").send_keys("Meena1234@gmail.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("kala1234@gmail.com")
time.sleep(3)
driver.find_element(By.ID,"password_step_input").send_keys("Meena123")
