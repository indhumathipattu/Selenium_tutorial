from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Mathu ")
driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("mathi")
driver.find_element(By.XPATH,"//input[@name='phone']").send_keys("9652037896")
driver.find_element(By.XPATH,"//input[@name='userName']").send_keys("meena1234@gmail.com")
driver.find_element(By.XPATH,"//input[@name='address1']").send_keys("No:78,tre nager")
driver.find_element(By.XPATH,"//input[@name='city']").send_keys("chennai")
driver.find_element(By.XPATH,"//input[@name='state']").send_keys("Tamil Nadu")
driver.find_element(By.XPATH,"//input[@name='postalCode']").send_keys("600079")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Mathu")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("meena12")
driver.find_element(By.XPATH,"//input[@name='confirmPassword']").send_keys("meena12")