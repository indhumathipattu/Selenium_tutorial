import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)
time.sleep(5)
print(driver.current_url)
time.sleep(3)
driver.close()
#back round la run ku add_arugment(__headless)not visable to window.