import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("detach", True)
#opt.add_argument("--headless")
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)
time.sleep(5)
print(driver.current_url)

# add_expirimental(detach,True)browes close akama irukka ues panurathuku that means runing visabe.