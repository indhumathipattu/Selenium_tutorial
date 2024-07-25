import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()
driver.find_element(By.XPATH,"html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("indhumathi")
time.sleep(5)
driver.find_element(By.XPATH,"html/body/div/div/div/div/div/div/div[2]/div/div/form/div/div/div/input").send_keys("meena22")
driver.find_element(By.XPATH,'html/body/div/div/div/div/div/div/div[2]/div/div/form/div[5]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,"html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input").send_keys("indhumathi")
driver.find_element(By.XPATH,"html/body/div[3]/div[2]/div/div/div[2]/div/div/div/form/div/div/div/div[2]/div/div/input")
driver.find_element(By.XPATH,"html/body/div[3]/div/div/div/div[2]/div/div/div/form/div/div/div/div[2]/div/div/input").send_keys("muthumeena123@gmail.com")
h2_text=driver.find_element(By.XPATH,"//form/div/div[4]/div/div/input").send_keys("murugan123")

#complated with my task