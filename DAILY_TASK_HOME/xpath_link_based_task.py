import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
#normalazied_space
driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@class='oxd-userdropdown-link']").click()
time.sleep(5)


#https://register.rediff.com/register/register.php?FormName=user_details
#task today`