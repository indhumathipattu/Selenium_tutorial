import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()
#single antibuter
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("muth123@gmail.com")
time.sleep(5)
#text()funtion
h2_text=driver.find_element(By.XPATH,"//h2[text()='Facebook helps you connect and share with the people in your life.']").text
print(h2_text)
time.sleep(3)
#contiontext() funtion
h2_taxt1=driver.find_element(By.XPATH,"//h2[contains(text()=',connect')]").text
print(h2_taxt1)
driver.find_element(By.XPATH,"//input[@name='pass']").send_keys("muth123")
time.sleep(5)