import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver =webdriver.Chrome(options=opt)
driver.get("https://www.flipkart.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"q").send_keys("TV 55 INCH")

#driver.find_element(By.XPATH,"  /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/button[1]").click()

# later sir asked how to run this program