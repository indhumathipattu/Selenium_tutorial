import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()
#ID
driver.find_element(By.ID, "email").send_keys("indumathi@gmail.com")
time.sleep(5)

#name
driver.find_element(By.NAME,"pass").send_keys("indumathi@123")
time.sleep(5)

#classname
actual_text = driver.find_element(By.CLASS_NAME, "_8eso").text
print(actual_text)

#link text
actual_text1 = driver.find_element(By.LINK_TEXT,"Forgotten password?").text
print(actual_text1)

# partial link text
actual_text2 = driver.find_element(By.PARTIAL_LINK_TEXT,"got").text
print(actual_text2)
