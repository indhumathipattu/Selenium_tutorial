import time
from selenium import webdriver

driver =webdriver.ChromiumEdge()
driver.get("http://www.facebook.com")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()
time.sleep(5)