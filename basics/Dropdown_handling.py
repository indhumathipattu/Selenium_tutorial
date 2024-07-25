# SelectByindex, SelectByvalue, SelectByvisibletext
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys('Indhumathi')
time.sleep(5)
month_dd = driver.find_element(By.ID,"month")
Sel = Select(month_dd)
Sel.select_by_visible_text("Jan")
time.sleep(5)
Sel.select_by_value("12")
time.sleep(5)
Sel.select_by_index(7)



