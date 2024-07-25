import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie import options

#"https://www.techlistic.com/p/selenium-practice-form.html#google_vignette"(pratish use this web)
#handless for fb

opt=Options()
opt.add_argument("__headless")
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.close()
