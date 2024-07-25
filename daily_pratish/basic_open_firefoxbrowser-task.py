import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.fb.com")
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(2)
driver.close()