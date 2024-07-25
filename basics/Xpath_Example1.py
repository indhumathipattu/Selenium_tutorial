import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()

#single attribute
driver.find_element(By.XPATH, "//input[@data-testid='royal_email']").send_keys("indhumathi")
time.sleep(5)

#text function
h2_text = driver.find_element(By.XPATH,"//h2[text()='Facebook helps you connect and share with the people in your life.']").text
print(h2_text)

#contains text function

h2_text1 = driver.find_element(By.XPATH,"//h2[contains(text(),' people')]").text
print(h2_text1)


#starts-with

h2_text2 = driver.find_element(By.XPATH,"//h2[starts-with(text(),'F')]").text
print(h2_text2)

#contains attribute

cna_text1 = driver.find_element(By.XPATH,"//a[contains(@id,'_0_0_')]").text
print(cna_text1)

#startswith attribute
cna_text2 = driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0')]").text
print(cna_text2)

driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
time.sleep(5)

#Multiple attribute
driver.find_element(By.XPATH, "//input[@class='_8esa'][@value='2']").click()
time.sleep(5)

#text function
signup_text = driver.find_element(By.XPATH,"//div[text()='Sign Up']").text
print(signup_text)
time.sleep(5)




#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#task