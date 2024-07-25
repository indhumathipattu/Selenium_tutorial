import time

from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://www.amazon.com")
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(2)

driver.minimize_window()
time.sleep(3)













