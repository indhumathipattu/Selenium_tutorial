import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opt)
driver.get("http://www.google.com")
driver.maximize_window()
driver.save_screenshot("C:\\Users\\mathi\\Desktop\\Screenshot\\screenshot2.png")
time.sleep(5)
driver.close()