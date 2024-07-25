
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
month_dd3=driver.find_element(By.ID,"month")
sel= Select(month_dd3)
dlist= sel.options
for d1 in dlist:
    print(d1.text)














