import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME,"firstName").send_keys("Indhumathi")
time.sleep(5)
driver.find_element(By.NAME,"lastName").send_keys("Indhumathi")
time.sleep(5)
driver.find_element(By.NAME,"phone").send_keys("8680091836")
driver.find_element(By.NAME,"userName").send_keys("indhumeena@gmail.com")
time.sleep(5)
driver.find_element(By.NAME,"address1").send_keys("NO:78,TTS Nagar")
time.sleep(5)
driver.find_element(By.NAME,"city").send_keys("Chennai")
time.sleep(5)
driver.find_element(By.NAME,"state").send_keys("Tamil Nadu")
time.sleep(5)
driver.find_element(By.NAME,"postalCode").send_keys("600077")
time.sleep(5)
driver.find_element(By.NAME,"email").send_keys("indhumeena@gmail.com")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("Indhu@123")
time.sleep(5)
driver.find_element(By.NAME,"confirmPassword").send_keys("Indhu@123")
time.sleep(5)
actual_title= driver.title
print(actual_title)
actual_url= driver.current_url
print(actual_url)




