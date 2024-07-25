import time
from optparse import Option

from selenium import webdriver
from selenium.webdriver.common.by import By

opt=Option()
opt.add_expirimental("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://facebook.com")
driver.maximize_window()
driver.minimize_window()
driver.implicitly_wait(30)
time.sleep(3)
actual_tittle=driver.title
print(actual_tittle)
current_url=driver.current_url
print(current_url)
act_text=driver.find_element(By.ID,"email").get_attribute("aria-label")
print(act_text)

