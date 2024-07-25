import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//html/body/center/form/div/table[2]/tbody/tr[3]/td/td[2]/input").send_keys("Meenachi")
time.sleep(5)
driver.find_element(By.XPATH,"html/body/center/form/div/table[2]/tbody/tr[8]/td[3]/input']").send_keys("meena123")
time.sleep(5)
#driver.find_element(By.XPATH,"//input[@type='password']").send_keys("mee12345")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("mee1234")
driver.find_element(By.XPATH,"//input[@style='width:185px;']").send_keys("reedif123@gmail.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("9605288863")
time.sleep(5)
driver.find_element(By.XPATH,"//select[@name='onchange='fieldTrack(this)']").send_keys("5")
driver.find_element(By.XPATH,"//select[@name='DOB_Monthf4993a6d']").send_keys("jan")
driver.find_element(By.XPATH,"//select[@name='DOB_Yearf4993a6d']").send_keys("2013")