import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# driver can wait for a particular time to load all the webelements in to the webpage
opt = Options()
opt.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"email").send_keys("indumathi")
driver.find_element(By.ID,"pass").send_keys("indhu@123")
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("Indhumathi")
driver.find_element(By.NAME,"lastname").send_keys('M')