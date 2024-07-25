import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(5)
