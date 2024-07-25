import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http:///www.triantickets.com")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()
time.sleep(7)