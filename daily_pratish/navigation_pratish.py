import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(3)
driver.get('http://www.facebook.com')
time.sleep(2)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(3)
driver.close()